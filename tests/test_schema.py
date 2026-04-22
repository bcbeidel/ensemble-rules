from datetime import datetime, timezone

import pytest

from ensemble_rules.schema import (
    CollectedRun,
    ModelResponse,
    Usage,
    dump,
    validate_raw,
)


def _sample_run() -> CollectedRun:
    return CollectedRun(
        topic="shell-scripts",
        topic_description="Bash/POSIX shell scripts",
        timestamp=datetime.now(timezone.utc).isoformat(),
        panel=["openai/gpt-5", "anthropic/claude-opus-4-7"],
        synthesizer="anthropic/claude-opus-4-7",
        responses=[
            ModelResponse(
                model="openai/gpt-5",
                reasoning="reason",
                rules_file="## Section 2\n- Do X.",
                error=None,
                usage=Usage(prompt_tokens=10, completion_tokens=20, total_tokens=30, cost_usd=0.001),
                elapsed_seconds=1.25,
            ),
            ModelResponse(
                model="anthropic/claude-opus-4-7",
                reasoning="",
                rules_file="",
                error="timeout",
                usage=Usage(),
                elapsed_seconds=0.0,
            ),
        ],
    )


def test_dump_validate_round_trip():
    original = _sample_run()
    restored = validate_raw(dump(original))

    assert restored.topic == original.topic
    assert restored.panel == original.panel
    assert restored.synthesizer == original.synthesizer
    assert len(restored.responses) == 2
    assert restored.responses[0].usage.total_tokens == 30
    assert restored.responses[1].error == "timeout"


def test_validate_raw_rejects_missing_top_level_key():
    payload = dump(_sample_run())
    del payload["panel"]
    with pytest.raises(ValueError, match="missing keys"):
        validate_raw(payload)


def test_validate_raw_rejects_empty_panel():
    payload = dump(_sample_run())
    payload["panel"] = []
    with pytest.raises(ValueError, match="panel"):
        validate_raw(payload)


def test_validate_raw_rejects_naive_timestamp():
    payload = dump(_sample_run())
    payload["timestamp"] = "2026-04-22T10:00:00"
    with pytest.raises(ValueError, match="timezone-aware"):
        validate_raw(payload)


def test_validate_raw_rejects_malformed_response():
    payload = dump(_sample_run())
    del payload["responses"][0]["usage"]
    with pytest.raises(ValueError, match="responses\\[0\\]"):
        validate_raw(payload)


def test_validate_raw_rejects_wrong_error_type():
    payload = dump(_sample_run())
    payload["responses"][0]["error"] = 42
    with pytest.raises(ValueError, match="error"):
        validate_raw(payload)
