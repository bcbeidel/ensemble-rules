---
name: v1-implementation-plan
description: Ship the ensemble-rules v1 CLI — elicit six LLMs in parallel, persist raw responses, produce synthesis and both deterministic and LLM-judged coverage artifacts.
type: plan
status: executing
branch: v1-implementation
created: 2026-04-22
---

# v1 Implementation Plan — ensemble-rules

## Goal

Ship a working Python implementation of the ensemble-rules thought experiment: poll a fixed panel of six LLMs with the same best-practices prompt, collect and persist their responses, and synthesize them into artifacts that surface consensus, minority rules, divergences, and per-model coverage. The interesting artifact is the pattern of agreement and divergence across model lineages — not a single "final rules file."

## Scope

In scope for v1 (from `prompts/kickoff-design-and-build.md`):

- CLI entry point `ensemble-rules run <topic> --description "..."` installed via `console_scripts`.
- Per-run artifact directory `runs/<timestamp>-<topic>/` containing `raw.json`, `synthesis.md`, `coverage.md`, `coverage-llm.md`, `meta.json`.
- Panel and synthesizer configured in a single Python module (`src/ensemble_rules/config.py`).
- Prompt templates as separate files under `prompts/templates/`, loaded with `{{var}}` substitution.
- Async fan-out (`asyncio` + `litellm.acompletion`) to the panel.
- Loud failure on malformed model responses (no silent empty strings).
- Timezone-aware UTC timestamps.
- Unit tests for the section splitter (including malformed input) and coverage-matrix builder (fixture-based). No live LLM calls in tests.
- README update covering env-var prerequisites, install command, and one example invocation.

Out of scope for v1: multi-pass synthesis, model weighting, dogfood test harness, web UI, retries/rate-limiting/cost caps beyond LiteLLM defaults.

## Approach

Three-stage pipeline — elicit → persist → synthesize — with parallelism where it cheaply helps and explicit errors where silent failure would hide signal. All open questions from the kickoff are resolved in §5 below; the headline resolutions:

- **Panel (OQ1):** six models — one frontier + one smaller/older per provider family: `gpt-5`, `gpt-4o-mini`, `claude-opus-4-7`, `claude-haiku-3-5`, `gemini-2.5-pro`, `grok-4`. Diversity of lineage is the point.
- **Coverage (OQ2):** produce both a deterministic `rapidfuzz`-clustered `coverage.md` and an LLM-judged `coverage-llm.md`. Their disagreement is itself a signal.
- **Rule extraction (OQ3):** regex-based (`-`/`*`/`N.` line prefixes, ≥20 chars, nearest preceding heading = theme).
- **Synthesis size (OQ4):** no cap. LiteLLM surfaces context overflows.
- **Total-failure policy (OQ5):** write `raw.json` + `meta.json` as forensic artifacts, skip synthesis, exit 2.
- **Template vars (OQ6):** strict `{{name}}` via `str.replace`.
- **Slug (OQ7):** `[a-z0-9]+` with `-` separator, 40-char cap.
- **Layout (OQ8):** `src/` layout.

The full design — module responsibilities, `raw.json` schema, step-by-step control flow, deviations from the source design, and resolved open questions — lives in the Design appendix below. That appendix is the authoritative reference for each task's acceptance criteria.

## File Changes

Created under `src/ensemble_rules/`:

- `__init__.py`, `errors.py`, `parse.py`, `schema.py`, `config.py`, `prompts.py`, `coverage.py`, `coverage_llm.py`, `elicit.py`, `synthesize.py`, `artifacts.py`, `pipeline.py`, `cli.py`.

Created under `prompts/templates/`:

- `elicitation.md`, `synthesis.md`, `coverage_llm.md`.

Created under `tests/`:

- `test_parse.py`, `test_schema.py`, `test_coverage.py`, `fixtures/` (fake model responses).

Created at repo root:

- `pyproject.toml` (package metadata, `src/` layout, `console_scripts` entry point, deps: `litellm`, `rapidfuzz`; dev deps: `pytest`).

Modified:

- `README.md` — env-var prerequisites, install command, example invocation.
- `.gitignore` — add `runs/`, `.venv/`, `*.egg-info/`, `__pycache__/`, `.pytest_cache/` if not already present.

## Tasks

- [ ] Task 1: `pyproject.toml` with `src/` layout, `console_scripts` entry point, runtime deps (`litellm`, `rapidfuzz`), dev dep (`pytest`), Python 3.11+ requirement. Also update `.gitignore` for `runs/`, `.venv/`, egg-info, pycache.
- [ ] Task 2: `src/ensemble_rules/__init__.py` (version), `src/ensemble_rules/errors.py` (`MalformedResponseError`, `PanelError`), `src/ensemble_rules/parse.py` (`split_sections` raising on missing marker), and `tests/test_parse.py` covering both valid split and the malformed-input raise case.
- [ ] Task 3: `src/ensemble_rules/schema.py` (dataclasses: `Usage`, `ModelResponse`, `CollectedRun`, `RunMeta`; `dump`/`validate_raw` helpers), plus `tests/test_schema.py` round-trip and malformed-payload cases.
- [ ] Task 4: `src/ensemble_rules/coverage.py` (`extract_rules`, `build_matrix`, `render_markdown`) with `rapidfuzz`-based clustering; `tests/fixtures/` static fake responses; `tests/test_coverage.py` exercising extraction, clustering, and rendering.
- [ ] Task 5: `prompts/templates/elicitation.md`, `prompts/templates/synthesis.md`, `prompts/templates/coverage_llm.md` (the three templates with `{{var}}` placeholders as specified in the kickoff and Design appendix), plus `src/ensemble_rules/prompts.py` loader with strict `{{name}}` substitution.
- [ ] Task 6: `src/ensemble_rules/config.py` with `PANEL` (six models) and `SYNTHESIZER` (`anthropic/claude-opus-4-7`) constants.
- [ ] Task 7: `src/ensemble_rules/elicit.py` (`elicit_one`, `elicit_all` using `litellm.acompletion` + `asyncio.gather(..., return_exceptions=True)`; per-call timing; usage/cost capture; catches `MalformedResponseError` and LiteLLM errors into errored `ModelResponse`).
- [ ] Task 8: `src/ensemble_rules/synthesize.py` (`synthesize_async`) and `src/ensemble_rules/coverage_llm.py` (`build_async`) — both single `litellm.acompletion` calls against `SYNTHESIZER`.
- [ ] Task 9: `src/ensemble_rules/artifacts.py` (`ensure_run_dir`, `slugify`, `write_raw`, `write_synthesis`, `write_coverage`, `write_coverage_llm`, `write_meta`) and `src/ensemble_rules/pipeline.py` (`run(topic, description)` orchestrating the full pipeline; gathers synthesis + llm-coverage in parallel; implements the total-failure exit-2 policy).
- [ ] Task 10: `src/ensemble_rules/cli.py` (argparse with `run` subcommand, dispatches to `pipeline.run`) + `README.md` update (prerequisites, install, example invocation).

## Validation

- `pytest` passes on a clean checkout with no API keys set. No test performs a live LLM call.
- `pip install -e .` succeeds and exposes `ensemble-rules` on `PATH`.
- `ensemble-rules run --help` prints the subcommand help.
- A live `ensemble-rules run <topic> --description "..."` invocation (with API keys set) produces a new `runs/<timestamp>-<slug>/` directory containing exactly five files: `raw.json`, `synthesis.md`, `coverage.md`, `coverage-llm.md`, `meta.json`. `raw.json` validates against `schema.validate_raw`. `meta.json` contains non-null usage for each successful panel model plus separate synthesizer-call usage entries.
- A forced-failure run (e.g., invalid model names in `PANEL`) writes `raw.json` + `meta.json` only, skips synthesis/coverage artifacts, exits with code 2.
- All "already decided" kickoff constraints are observably respected in the code: `datetime.now(timezone.utc)` (grep for absence of `utcnow`), `PANEL`/`SYNTHESIZER` as module-level constants in `config.py`, `console_scripts` entry point in `pyproject.toml`, no silent fallback in `split_sections`.

---

## Design appendix

The sections below are the authoritative design reference for each task above. They are unchanged from `plans/v1-implementation-plan.md` (the pre-frontmatter plan file).

### Module layout

All source lives under `src/ensemble_rules/`. Tests live under `tests/`. Prompt templates live under `prompts/templates/`. Artifacts land in `runs/<timestamp>-<topic>/`.

| Path | Responsibility |
|---|---|
| `pyproject.toml` | Package metadata, dependencies (`litellm`, `rapidfuzz`), `console_scripts` entry point `ensemble-rules = ensemble_rules.cli:main`. |
| `src/ensemble_rules/__init__.py` | Package marker; exposes `__version__`. |
| `src/ensemble_rules/config.py` | Panel roster and synthesizer selection. `PANEL: list[str]` and `SYNTHESIZER: str` constants, per kickoff. |
| `src/ensemble_rules/cli.py` | Argparse CLI; `main()` dispatches the `run` subcommand to `pipeline.run`. |
| `src/ensemble_rules/pipeline.py` | Top-level orchestration: `run(topic, description)` calls elicit → collect → synthesize → persist, and constructs the run directory. |
| `src/ensemble_rules/elicit.py` | Async fan-out to the panel via `litellm.acompletion`. One coroutine per model, gathered with `asyncio.gather(..., return_exceptions=True)`. Per-model token/cost captured from LiteLLM usage object. |
| `src/ensemble_rules/parse.py` | `split_sections(text) -> (reasoning, rules_file)`. Raises `MalformedResponseError` when the expected section marker is missing — no silent empty return. |
| `src/ensemble_rules/synthesize.py` | Builds the synthesis prompt from collected responses, calls the synthesizer model, returns the synthesis markdown. |
| `src/ensemble_rules/coverage.py` | Extracts rules from each model's `rules_file`, clusters them deterministically via `rapidfuzz`, and renders `coverage.md` (matrix + omissions list + wording-variance note). |
| `src/ensemble_rules/coverage_llm.py` | Parallel LLM-judged clustering. Asks the synthesizer to produce the same matrix and renders `coverage-llm.md`. Kept separate from `coverage.py` so the two views can be diffed and the bias is explicit. |
| `src/ensemble_rules/prompts.py` | Loads templates from `prompts/templates/*.md` and performs `{{var}}` substitution. Locates the `prompts/` directory by walking up from `__file__` until it finds a sibling of `src/` — works for editable installs (`pip install -e .`), which is the only supported v1 install mode. If we ever ship a wheel, templates will need to move under `src/ensemble_rules/templates/` or be declared as package data. |
| `src/ensemble_rules/artifacts.py` | Writes `raw.json`, `synthesis.md`, `coverage.md`, `meta.json` into the run directory. Centralizes filesystem I/O. |
| `src/ensemble_rules/schema.py` | Dataclass definitions (`ModelResponse`, `CollectedRun`, `RunMeta`) and `validate_raw(payload)` — the single validation entry point. |
| `src/ensemble_rules/errors.py` | `MalformedResponseError`, `PanelError`. |
| `prompts/templates/elicitation.md` | Elicitation prompt; `{{topic}}`, `{{topic_description}}`. |
| `prompts/templates/synthesis.md` | Synthesis prompt; `{{topic}}`, `{{collected_responses}}`. |
| `prompts/templates/coverage_llm.md` | Prompt that asks the synthesizer to produce a rule × model coverage matrix in a fixed markdown format; `{{collected_responses}}`. |
| `tests/test_parse.py` | Unit tests for `split_sections`, including a malformed-input case that must raise. |
| `tests/test_coverage.py` | Unit tests for coverage-matrix builder against a fixture of fake responses. |
| `tests/test_schema.py` | Round-trip test: `validate_raw(dump(CollectedRun(...)))` succeeds; malformed payloads raise. |
| `tests/fixtures/` | Static fake model responses used by the above tests. No live LLM calls. |
| `README.md` | Prerequisites (env vars), install command, one example invocation. |

### Data contracts

**`raw.json` JSON schema (informal):**

```json
{
  "topic": "string",
  "topic_description": "string",
  "timestamp": "ISO-8601 string with UTC offset",
  "panel": ["string", "..."],
  "synthesizer": "string",
  "responses": [
    {
      "model": "string",
      "reasoning": "string",
      "rules_file": "string",
      "error": "string | null",
      "usage": {
        "prompt_tokens": "int | null",
        "completion_tokens": "int | null",
        "total_tokens": "int | null",
        "cost_usd": "float | null"
      },
      "elapsed_seconds": "float"
    }
  ]
}
```

Errored entries keep `reasoning`/`rules_file` empty and populate `error`. Excluded from synthesis and from the coverage matrix denominator (noted in `coverage.md`).

**In-memory types (dataclasses in `schema.py`):**

- `Usage(prompt_tokens: int | None, completion_tokens: int | None, total_tokens: int | None, cost_usd: float | None)`
- `ModelResponse(model, reasoning, rules_file, error, usage, elapsed_seconds)`
- `CollectedRun(topic, topic_description, timestamp, panel, synthesizer, responses)`
- `RunMeta(topic, started_at, finished_at, elapsed_seconds, panel, synthesizer, usage_by_model, synthesis_usage, coverage_llm_usage)` → `meta.json`. Synthesizer calls are recorded separately so their cost is visible.

**Validation:** `dataclasses` + manual `schema.validate_raw(payload: dict) -> CollectedRun`. No pydantic, no jsonschema. Centralized in `schema.py`.

### Control flow — one `ensemble-rules run <topic> --description "..."` invocation

1. `console_scripts` dispatches to `ensemble_rules.cli:main`.
2. `cli.main()` argparse reads `run` subcommand args, calls `pipeline.run(topic, description)`.
3. `pipeline.run` captures `started_at`, computes `run_dir = runs/<YYYYMMDDTHHMMSSZ>-<slug(topic)>/`, creates it.
4. `prompts.load("elicitation")` reads the template and substitutes `{{topic}}`/`{{topic_description}}`.
5. `asyncio.run(elicit.elicit_all(prompt, config.PANEL))` fans out one coroutine per model via `asyncio.gather(..., return_exceptions=True)`. Each `elicit_one` awaits `litellm.acompletion`, times the call, extracts `choices[0].message.content` + `usage`/`_hidden_params.response_cost`, and passes to `parse.split_sections`. `MalformedResponseError` and LiteLLM exceptions are converted to errored `ModelResponse`.
6. Assemble `CollectedRun` with UTC timestamp, panel, synthesizer.
7. `artifacts.write_raw(run_dir, collected)`.
8. Deterministic coverage: `coverage.build_matrix` → `coverage.render_markdown` → `artifacts.write_coverage` (`coverage.md`). Runs on successful responses; errored models listed separately.
9. Synthesis and LLM-judged coverage in parallel via `asyncio.gather`: `synthesize.synthesize_async` returns synthesis markdown; `coverage_llm.build_async` returns llm-coverage markdown.
10. `artifacts.write_synthesis` + `artifacts.write_coverage_llm`.
11. `artifacts.write_meta(run_dir, meta)` with per-model usage + synthesizer-call usage separately.
12. `cli.main` prints the run directory path and exits 0. Non-zero exit only if the entire panel errored or synthesis raised.

### Deviations from the source design

Each cites the line/section in `docs/original-design-notes.md` being replaced.

1. **Serial loop → async fan-out.** Source 182–197 → `asyncio.gather` over `litellm.acompletion`. Source itself flags this at line 263.
2. **Silent `split_sections` fallback → raise.** Source 207–213 → explicit `MalformedResponseError` (caught per-model, visible in `raw.json`).
3. **`datetime.utcnow()` → `datetime.now(timezone.utc)`.** Source line 201.
4. **Flat topic-prefixed files → per-run directory.** Source 237–241 → `runs/<timestamp>-<topic>/` with five artifacts.
5. **No coverage artifact → added.** Source ends at "Final rules.md" (line 51). Kickoff adds coverage matrix, wording-variance note, omissions list as first-class outputs.
6. **No usage/cost persistence → added to `meta.json`.** Source mentions only as extension (line 266).
7. **`MODELS` → `PANEL`, centralized module.** Source line 165.
8. **Inline template strings → template files.** Source 174–175 → `prompts/templates/`.
9. **Script-style `run(...)` with `__main__` → `console_scripts` CLI.** Source 235–246.
10. **Synthesis prompt additions.** Source 102–132 four sections extended with (a) flag near-identical wording vs. substantive convergence on consensus rules and (b) call out notable omissions.

### Resolved open questions

1. **Panel.** `["openai/gpt-5", "openai/gpt-4o-mini", "anthropic/claude-opus-4-7", "anthropic/claude-haiku-3-5", "gemini/gemini-2.5-pro", "xai/grok-4"]`. Frontier + smaller/older per family. 6× API cost accepted.
2. **Coverage.** Produce both. `coverage.md` = `rapidfuzz.ratio >= 85` deterministic. `coverage-llm.md` = synthesizer-judged. Disagreement is signal.
3. **Rule extraction.** Regex: lines starting `-`/`*`/`N.`, ≥20 chars, nearest heading = theme. Raw text preserved in `raw.json` for re-parsing.
4. **Synthesis size.** No cap. LiteLLM surfaces context overflows.
5. **Total panel failure.** Write `raw.json` + `meta.json` forensic record, skip synthesis/coverage artifacts, exit 2.
6. **Template vars.** Strict `{{name}}` via `str.replace`.
7. **Slug.** Lowercase, `[a-z0-9]+` runs → `-`, strip outer `-`, 40-char cap.
8. **Layout.** `src/`. `[tool.setuptools.packages.find] where = ["src"]`.

### Traceability — v1 deliverables ↔ modules

| Deliverable | Modules / files |
|---|---|
| 1. CLI entry point `ensemble-rules run ...` | `pyproject.toml`, `src/ensemble_rules/cli.py`, `src/ensemble_rules/pipeline.py` |
| 2a. `raw.json` | `src/ensemble_rules/schema.py`, `artifacts.py`, `elicit.py`, `parse.py` |
| 2b. `synthesis.md` | `synthesize.py`, `prompts/templates/synthesis.md`, `artifacts.py` |
| 2c. `coverage.md` | `coverage.py`, `artifacts.py` |
| 2c′. `coverage-llm.md` | `coverage_llm.py`, `prompts/templates/coverage_llm.md`, `artifacts.py` |
| 2d. `meta.json` | `schema.py` (`RunMeta`), `artifacts.py`, `pipeline.py` |
| 3. Panel config in one file | `config.py` |
| 4. Prompt templates as files | `prompts/templates/*.md`, `prompts.py` |
| 5. README update | `README.md` |
| 6. Tests | `tests/test_parse.py`, `test_coverage.py`, `test_schema.py`, `tests/fixtures/` |

### Constraint check

- Python 3.11+ / LiteLLM-only ✓ (`pyproject.toml`; only `litellm` + `rapidfuzz` at runtime; `rapidfuzz` deliberate per OQ2).
- Panel diversity (include weaker/older models) ✓ (OQ1).
- Synthesizer bias accepted ✓ (single `SYNTHESIZER`; no multi-pass).
- Async from day one ✓ (`litellm.acompletion` in `elicit.py`, `synthesize.py`, `coverage_llm.py`).
- Fail loud on format deviations ✓ (`MalformedResponseError` in `parse.py`).
- Timezone-aware timestamps ✓ (`datetime.now(timezone.utc)`).
- Panel config in one module, Python constants ✓ (`config.py`, `PANEL`, `SYNTHESIZER`).
- `console_scripts` entry point ✓ (`pyproject.toml`, `cli.py`).
