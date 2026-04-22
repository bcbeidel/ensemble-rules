from __future__ import annotations

import asyncio
import time

import litellm

from ensemble_rules.errors import MalformedResponseError
from ensemble_rules.parse import split_sections
from ensemble_rules.schema import ModelResponse, Usage


async def elicit_one(model: str, prompt: str) -> ModelResponse:
    started = time.monotonic()
    try:
        response = await litellm.acompletion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
    except Exception as exc:
        return _errored(model, started, f"{type(exc).__name__}: {exc}")

    elapsed = time.monotonic() - started

    try:
        content = response.choices[0].message.content
    except (AttributeError, IndexError, KeyError) as exc:
        return _errored(model, started, f"unexpected response shape: {exc}")

    if not content:
        return _errored(model, started, "empty response content", elapsed=elapsed)

    try:
        reasoning, rules_file = split_sections(content)
    except MalformedResponseError as exc:
        return ModelResponse(
            model=model,
            reasoning=content.strip(),
            rules_file="",
            error=f"MalformedResponseError: {exc}",
            usage=_extract_usage(response),
            elapsed_seconds=elapsed,
        )

    return ModelResponse(
        model=model,
        reasoning=reasoning,
        rules_file=rules_file,
        error=None,
        usage=_extract_usage(response),
        elapsed_seconds=elapsed,
    )


async def elicit_all(prompt: str, panel: list[str]) -> list[ModelResponse]:
    results = await asyncio.gather(
        *(elicit_one(model, prompt) for model in panel),
        return_exceptions=True,
    )
    normalized: list[ModelResponse] = []
    for model, result in zip(panel, results):
        if isinstance(result, BaseException):
            normalized.append(_errored(model, time.monotonic(), f"gather: {result!r}", elapsed=0.0))
        else:
            normalized.append(result)
    return normalized


def _errored(model: str, started: float, message: str, elapsed: float | None = None) -> ModelResponse:
    return ModelResponse(
        model=model,
        reasoning="",
        rules_file="",
        error=message,
        usage=Usage(),
        elapsed_seconds=elapsed if elapsed is not None else time.monotonic() - started,
    )


def _extract_usage(response: object) -> Usage:
    usage_obj = getattr(response, "usage", None)
    prompt_tokens = _get(usage_obj, "prompt_tokens")
    completion_tokens = _get(usage_obj, "completion_tokens")
    total_tokens = _get(usage_obj, "total_tokens")
    cost = _extract_cost(response)
    return Usage(
        prompt_tokens=_coerce_int(prompt_tokens),
        completion_tokens=_coerce_int(completion_tokens),
        total_tokens=_coerce_int(total_tokens),
        cost_usd=_coerce_float(cost),
    )


def _extract_cost(response: object) -> object:
    hidden = getattr(response, "_hidden_params", None)
    if isinstance(hidden, dict):
        return hidden.get("response_cost")
    return None


def _get(obj: object, key: str) -> object:
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


def _coerce_int(value: object) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _coerce_float(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
