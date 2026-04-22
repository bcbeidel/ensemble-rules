from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from pathlib import Path

from ensemble_rules import artifacts, config, coverage, coverage_llm, elicit, prompts, synthesize
from ensemble_rules.errors import PanelError
from ensemble_rules.schema import CollectedRun, RunMeta, Usage


def run(topic: str, description: str) -> Path:
    started_at = datetime.now(timezone.utc)
    run_dir = artifacts.make_run_dir(topic, started_at)
    artifacts.ensure_run_dir(run_dir)

    elicitation_template = prompts.load("elicitation")
    elicitation_prompt = prompts.render(
        elicitation_template,
        topic=topic,
        topic_description=description,
    )

    panel = list(config.PANEL)
    synthesizer = config.SYNTHESIZER

    responses = asyncio.run(elicit.elicit_all(elicitation_prompt, panel))
    collected = CollectedRun(
        topic=topic,
        topic_description=description,
        timestamp=started_at.isoformat(),
        panel=panel,
        synthesizer=synthesizer,
        responses=responses,
    )
    artifacts.write_raw(run_dir, collected)

    successful = [r for r in responses if r.error is None]
    synthesis_usage = Usage()
    coverage_llm_usage = Usage()

    if successful:
        report = coverage.build_matrix(collected)
        artifacts.write_coverage(run_dir, coverage.render_markdown(report))

        synthesis_template = prompts.load("synthesis")
        coverage_llm_template = prompts.load("coverage_llm")
        (synthesis_md, synthesis_usage), (coverage_llm_md, coverage_llm_usage) = asyncio.run(
            _run_synthesizer_calls(collected, synthesis_template, coverage_llm_template, synthesizer)
        )
        artifacts.write_synthesis(run_dir, synthesis_md)
        artifacts.write_coverage_llm(run_dir, coverage_llm_md)

    finished_at = datetime.now(timezone.utc)
    meta = RunMeta(
        topic=topic,
        started_at=started_at.isoformat(),
        finished_at=finished_at.isoformat(),
        elapsed_seconds=(finished_at - started_at).total_seconds(),
        panel=panel,
        synthesizer=synthesizer,
        usage_by_model={r.model: r.usage for r in responses},
        synthesis_usage=synthesis_usage,
        coverage_llm_usage=coverage_llm_usage,
    )
    artifacts.write_meta(run_dir, meta)

    if not successful:
        raise PanelError(
            f"all {len(responses)} panel models errored — see {run_dir}/raw.json",
            run_dir=run_dir,
        )

    return run_dir


async def _run_synthesizer_calls(
    collected: CollectedRun,
    synthesis_template: str,
    coverage_llm_template: str,
    synthesizer: str,
) -> tuple[tuple[str, Usage], tuple[str, Usage]]:
    return await asyncio.gather(
        synthesize.synthesize_async(collected, synthesis_template, synthesizer),
        coverage_llm.build_async(collected, coverage_llm_template, synthesizer),
    )
