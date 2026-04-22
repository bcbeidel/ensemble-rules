from __future__ import annotations

from pathlib import Path


def _templates_dir() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "prompts" / "templates"
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError(
        "Could not locate prompts/templates/ — expected it as a sibling of the "
        "src/ directory containing this package. v1 only supports editable "
        "installs (`pip install -e .`)."
    )


def load(name: str) -> str:
    path = _templates_dir() / f"{name}.md"
    if not path.is_file():
        raise FileNotFoundError(f"template not found: {path}")
    return path.read_text(encoding="utf-8")


def render(template: str, **variables: str) -> str:
    rendered = template
    for key, value in variables.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered
