from __future__ import annotations

from pathlib import Path


class MalformedResponseError(ValueError):
    pass


class PanelError(RuntimeError):
    def __init__(self, message: str, run_dir: Path | None = None):
        super().__init__(message)
        self.run_dir = run_dir
