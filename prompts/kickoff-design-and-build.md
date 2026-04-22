# Kickoff: design and build ensemble-rules

## Goal

Build a working Python implementation of the ensemble-rules thought experiment: poll N LLMs with the same best-practices prompt for a given topic, collect their responses, and synthesize them into a single output that surfaces consensus, minority rules, and disagreements.

Source design: `docs/original-design-notes.md` (three-stage elicit → collect → synthesize pipeline, LiteLLM-based, reference implementation included).

## What's already decided

These come from prior discussion and should be treated as constraints, not open questions:

- **Stack.** Python 3.11+ with LiteLLM. Single-provider SDKs are out of scope for v1.
- **Panel composition matters.** Include weaker/older models intentionally alongside frontier models. A rule that appears only in frontier models is a different signal than one that appears everywhere. Do not filter for "best" models — diversity of lineage is the point.
- **Accept synthesizer bias.** The user is fine letting one model (likely Claude) synthesize. This is a thought experiment, not an unbiased-artifact factory.
- **Async from day one.** The reference implementation uses a serial loop; use `asyncio` + `litellm.acompletion` in the first pass.
- **Fail loud on format deviations.** The reference `split_sections` silently returns empty strings on missing markers. Raise explicit errors so malformed model output is visible, not hidden.
- **Use timezone-aware timestamps.** `datetime.now(timezone.utc)`, not deprecated `utcnow()`.
- **Panel config location.** Put model roster and synthesizer selection in a single module (`ensemble_rules/config.py`) with a `PANEL: list[str]` constant and a `SYNTHESIZER: str` constant. No YAML/TOML config file for v1.
- **CLI mechanism.** Expose `ensemble-rules` as a `console_scripts` entry point via `pyproject.toml`. Subcommand: `run <topic> --description "..."`.

## What the output should emphasize

The interesting artifact isn't the "final rules file" — it's the pattern of agreement and divergence. In addition to the three sections in the source design (Consensus / Strong Minority / Divergences / Final), the output should include:

- **Coverage matrix.** A rule × model table. Which rules appear in which models' responses. The single highest-value artifact for pattern-spotting.
- **Wording variance note.** When models "agree" on a rule, flag whether phrasing is near-identical (suggests shared training source) vs. substantively similar but differently worded (suggests genuine convergence).
- **Omissions list.** Rules that appear in a majority but are notably absent from one model — sometimes the absence is the signal.

## Deliverables for v1

1. A CLI entry point installed as `ensemble-rules` (via `console_scripts`) that runs `ensemble-rules run <topic> --description "..."` and writes artifacts to `runs/<timestamp>-<topic>/`.
2. Persisted artifacts per run:
   - `raw.json` — collected responses, one per model, with reasoning and rules sections split
   - `synthesis.md` — the synthesizer's output
   - `coverage.md` — the rule × model matrix
   - `meta.json` — run metadata (models used, token usage/cost per model, elapsed time)
3. Panel configuration in `ensemble_rules/config.py` so swapping the roster is a one-file change.
4. Elicitation and synthesis prompt templates as separate files under `prompts/templates/`, not inlined as Python string literals. Loaded at runtime with `{{topic}}` / `{{topic_description}}` / `{{collected_responses}}` substitution.
5. A minimal `README.md` update covering: prerequisites (env vars), install command, and a single example invocation.
6. Basic test coverage: at minimum, a unit test for the section-splitter with a malformed-input case, and a unit test for the coverage-matrix builder with a fixture of fake responses. No live LLM calls in tests.

## Out of scope for v1

- Multi-pass synthesis with a second synthesizer model
- Model weighting in the synthesis prompt
- Test harness that dogfoods generated rules files back into the models
- Web UI, dashboards, persistence beyond flat files
- Retries, rate limiting, or cost caps beyond what LiteLLM provides by default

## Task for the agent

Produce a concrete implementation plan before writing any code. Save it to `plans/v1-implementation-plan.md`.

The plan must contain, in this order:

1. **Module layout.** Each file you intend to create, with a one-sentence responsibility. Include test files.
2. **Data contracts.** The JSON schema of `raw.json`, the Python type(s) that represent it in memory, and the single function/module where schema validation happens. Name the validation approach (e.g., `dataclasses` + manual check, `pydantic`, `jsonschema`).
3. **Control flow.** A step-by-step trace of one `ensemble-rules run` invocation from CLI parse to final artifact write, naming the function at each step.
4. **Deviations from the source design.** List each place in `docs/original-design-notes.md` where the reference code needs to change to meet the constraints above. Quote or cite the specific lines/sections you're replacing.
5. **Open questions.** A numbered list of ambiguities in this kickoff that need resolution before implementation. For each, propose a default and explain the trade-off so the reviewer can accept the default or override it.

### Plan acceptance criteria

The reviewer will approve the plan only if:

- Every v1 deliverable above is traceable to at least one module in the plan.
- Every "already decided" constraint is visibly respected (no silent deviations).
- Each open question has a proposed default — unresolved questions without a default are not acceptable.
- The plan fits in one markdown file and is scannable in under 5 minutes.

### Hard constraints

- Do not write implementation code in this pass. Only the plan document.
- Do not modify `docs/original-design-notes.md` — treat it as read-only source material.
- If a constraint in this kickoff conflicts with the source design, the kickoff wins; note the conflict under "Deviations from the source design".
