from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

from ensemble_rules.schema import CollectedRun, RunMeta, dump, dump_meta

_RUNS_DIR = Path("runs")
_MAX_SLUG = 40


def slugify(topic: str) -> str:
    lowered = topic.lower()
    dashed = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    if not dashed:
        return "topic"
    return dashed[:_MAX_SLUG].rstrip("-") or "topic"


def make_run_dir(topic: str, started_at: datetime) -> Path:
    stamp = started_at.strftime("%Y%m%dT%H%M%SZ")
    return _RUNS_DIR / f"{stamp}-{slugify(topic)}"


def ensure_run_dir(run_dir: Path) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)


def write_raw(run_dir: Path, run: CollectedRun) -> None:
    _write_json(run_dir / "raw.json", dump(run))


def write_meta(run_dir: Path, meta: RunMeta) -> None:
    _write_json(run_dir / "meta.json", dump_meta(meta))


def write_synthesis(run_dir: Path, text: str) -> None:
    (run_dir / "synthesis.md").write_text(text, encoding="utf-8")


def write_coverage(run_dir: Path, text: str) -> None:
    (run_dir / "coverage.md").write_text(text, encoding="utf-8")


def write_coverage_llm(run_dir: Path, text: str) -> None:
    (run_dir / "coverage-llm.md").write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
