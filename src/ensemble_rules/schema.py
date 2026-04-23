from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime


@dataclass
class Usage:
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    total_tokens: int | None = None
    cost_usd: float | None = None


@dataclass
class ModelResponse:
    model: str
    reasoning: str
    rules_file: str
    deterministic_checks: str
    error: str | None
    usage: Usage
    elapsed_seconds: float


@dataclass
class CollectedRun:
    topic: str
    topic_description: str
    timestamp: str
    panel: list[str]
    synthesizer: str
    responses: list[ModelResponse]


@dataclass
class RunMeta:
    topic: str
    started_at: str
    finished_at: str
    elapsed_seconds: float
    panel: list[str]
    synthesizer: str
    usage_by_model: dict[str, Usage] = field(default_factory=dict)
    synthesis_usage: Usage = field(default_factory=Usage)
    coverage_llm_usage: Usage = field(default_factory=Usage)


def dump(run: CollectedRun) -> dict:
    return asdict(run)


def dump_meta(meta: RunMeta) -> dict:
    return asdict(meta)


def validate_raw(payload: dict) -> CollectedRun:
    _require_keys(
        payload,
        {"topic", "topic_description", "timestamp", "panel", "synthesizer", "responses"},
        "raw payload",
    )
    _require_type(payload, "topic", str)
    _require_type(payload, "topic_description", str)
    _require_type(payload, "timestamp", str)
    _require_type(payload, "synthesizer", str)
    _parse_utc_timestamp(payload["timestamp"])

    panel = payload["panel"]
    if not isinstance(panel, list) or not panel or not all(isinstance(m, str) for m in panel):
        raise ValueError("panel must be a non-empty list of strings")

    raw_responses = payload["responses"]
    if not isinstance(raw_responses, list):
        raise ValueError("responses must be a list")

    responses = [_validate_response(r, i) for i, r in enumerate(raw_responses)]

    return CollectedRun(
        topic=payload["topic"],
        topic_description=payload["topic_description"],
        timestamp=payload["timestamp"],
        panel=list(panel),
        synthesizer=payload["synthesizer"],
        responses=responses,
    )


def _validate_response(r: object, idx: int) -> ModelResponse:
    if not isinstance(r, dict):
        raise ValueError(f"responses[{idx}] must be an object")
    _require_keys(
        r,
        {
            "model",
            "reasoning",
            "rules_file",
            "deterministic_checks",
            "error",
            "usage",
            "elapsed_seconds",
        },
        f"responses[{idx}]",
    )
    _require_type(r, "model", str, idx)
    _require_type(r, "reasoning", str, idx)
    _require_type(r, "rules_file", str, idx)
    _require_type(r, "deterministic_checks", str, idx)
    if r["error"] is not None and not isinstance(r["error"], str):
        raise ValueError(f"responses[{idx}].error must be str or null")
    if not isinstance(r["elapsed_seconds"], (int, float)):
        raise ValueError(f"responses[{idx}].elapsed_seconds must be a number")
    usage = _validate_usage(r["usage"], idx)
    return ModelResponse(
        model=r["model"],
        reasoning=r["reasoning"],
        rules_file=r["rules_file"],
        deterministic_checks=r["deterministic_checks"],
        error=r["error"],
        usage=usage,
        elapsed_seconds=float(r["elapsed_seconds"]),
    )


def _validate_usage(u: object, idx: int) -> Usage:
    if not isinstance(u, dict):
        raise ValueError(f"responses[{idx}].usage must be an object")
    for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
        if u.get(key) is not None and not isinstance(u[key], int):
            raise ValueError(f"responses[{idx}].usage.{key} must be int or null")
    if u.get("cost_usd") is not None and not isinstance(u["cost_usd"], (int, float)):
        raise ValueError(f"responses[{idx}].usage.cost_usd must be number or null")
    return Usage(
        prompt_tokens=u.get("prompt_tokens"),
        completion_tokens=u.get("completion_tokens"),
        total_tokens=u.get("total_tokens"),
        cost_usd=u.get("cost_usd"),
    )


def _require_keys(d: object, required: set[str], ctx: str) -> None:
    if not isinstance(d, dict):
        raise ValueError(f"{ctx} must be an object")
    missing = required - d.keys()
    if missing:
        raise ValueError(f"{ctx} missing keys: {sorted(missing)}")


def _require_type(d: dict, key: str, typ: type, idx: int | None = None) -> None:
    if not isinstance(d[key], typ):
        loc = f"responses[{idx}].{key}" if idx is not None else key
        raise ValueError(f"{loc} must be {typ.__name__}")


def _parse_utc_timestamp(ts: str) -> None:
    parsed = datetime.fromisoformat(ts)
    if parsed.tzinfo is None:
        raise ValueError(f"timestamp {ts!r} must be timezone-aware")
