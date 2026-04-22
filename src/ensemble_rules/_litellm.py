from __future__ import annotations

import litellm

from ensemble_rules.schema import ModelResponse, Usage


async def call(model: str, prompt: str) -> tuple[str, Usage]:
    response = await litellm.acompletion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    content = response.choices[0].message.content or ""
    return content, extract_usage(response)


def extract_usage(response: object) -> Usage:
    usage_obj = getattr(response, "usage", None)
    hidden = getattr(response, "_hidden_params", None)
    cost = hidden.get("response_cost") if isinstance(hidden, dict) else None
    return Usage(
        prompt_tokens=_coerce_int(_get(usage_obj, "prompt_tokens")),
        completion_tokens=_coerce_int(_get(usage_obj, "completion_tokens")),
        total_tokens=_coerce_int(_get(usage_obj, "total_tokens")),
        cost_usd=_coerce_float(cost),
    )


def build_model_blocks(responses: list[ModelResponse]) -> str:
    blocks: list[str] = []
    for r in responses:
        if r.error is not None:
            continue
        blocks.append(
            f"===MODEL: {r.model}===\n\n{r.reasoning}\n\n{r.rules_file}"
        )
    return "\n\n".join(blocks)


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
