from __future__ import annotations

from ensemble_rules._litellm import build_model_blocks, call
from ensemble_rules.prompts import render
from ensemble_rules.schema import CollectedRun, Usage


async def build_async(
    run: CollectedRun,
    template: str,
    model: str,
) -> tuple[str, Usage]:
    blocks = build_model_blocks(run.responses)
    prompt = render(template, collected_responses=blocks)
    return await call(model, prompt)
