import json
from datetime import datetime, timezone
from pathlib import Path

from ensemble_rules.artifacts import (
    ensure_run_dir,
    make_run_dir,
    slugify,
    write_coverage,
    write_coverage_llm,
    write_meta,
    write_raw,
    write_synthesis,
)
from ensemble_rules.schema import RunMeta, Usage, validate_raw
from tests.fixtures.fake_responses import sample_run


def test_slugify_basic():
    assert slugify("Shell Scripts") == "shell-scripts"
    assert slugify("terraform/aws") == "terraform-aws"
    assert slugify("  C++ templates  ") == "c-templates"


def test_slugify_empty_and_non_ascii_fallback():
    assert slugify("") == "topic"
    assert slugify("日本語") == "topic"


def test_slugify_truncates_to_40_chars():
    long = "a" * 100
    assert len(slugify(long)) == 40


def test_make_run_dir_stamps_utc():
    dt = datetime(2026, 4, 22, 10, 30, 45, tzinfo=timezone.utc)
    path = make_run_dir("shell scripts", dt)
    assert path.name == "20260422T103045Z-shell-scripts"
    assert path.parts[0] == "runs"


def test_write_all_artifacts_round_trips(tmp_path):
    run_dir = tmp_path / "run"
    ensure_run_dir(run_dir)

    run = sample_run()
    write_raw(run_dir, run)
    write_synthesis(run_dir, "# synthesis\n")
    write_coverage(run_dir, "# coverage\n")
    write_coverage_llm(run_dir, "# coverage-llm\n")
    meta = RunMeta(
        topic=run.topic,
        started_at=run.timestamp,
        finished_at=run.timestamp,
        elapsed_seconds=1.0,
        panel=run.panel,
        synthesizer=run.synthesizer,
        usage_by_model={r.model: r.usage for r in run.responses},
        synthesis_usage=Usage(total_tokens=500, cost_usd=0.01),
        coverage_llm_usage=Usage(total_tokens=300, cost_usd=0.006),
    )
    write_meta(run_dir, meta)

    raw_loaded = json.loads((run_dir / "raw.json").read_text())
    restored = validate_raw(raw_loaded)
    assert restored.topic == run.topic

    meta_loaded = json.loads((run_dir / "meta.json").read_text())
    assert meta_loaded["synthesis_usage"]["total_tokens"] == 500
    assert meta_loaded["coverage_llm_usage"]["cost_usd"] == 0.006

    assert (run_dir / "synthesis.md").read_text() == "# synthesis\n"
    assert (run_dir / "coverage.md").read_text() == "# coverage\n"
    assert (run_dir / "coverage-llm.md").read_text() == "# coverage-llm\n"
