from __future__ import annotations

import asyncio
import time

import litellm

from ensemble_rules._litellm import extract_usage
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
            usage=extract_usage(response),
            elapsed_seconds=elapsed,
        )

    return ModelResponse(
        model=model,
        reasoning=reasoning,
        rules_file=rules_file,
        error=None,
        usage=extract_usage(response),
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
