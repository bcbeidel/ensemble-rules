# Sample run: Agent Rule Files

Frozen snapshot of one `make agent-rules` invocation. Copied verbatim from
`runs/20260422T183037Z-agent-rule-files/` (which is gitignored).

## Run metadata

- **Topic:** Agent Rule Files
- **Timestamp:** 2026-04-22T18:30:37Z
- **Wall time:** 210.6 seconds
- **Panel:** 6/6 models returned non-errored responses
  - `openai/gpt-5`, `openai/gpt-4o-mini`
  - `anthropic/claude-opus-4-7`, `anthropic/claude-haiku-4-5`
  - `vertex_ai/gemini-2.5-pro`
  - `xai/grok-3-mini`
- **Synthesizer:** `anthropic/claude-opus-4-7` (called twice — once for
  `synthesis.md`, once for `coverage-llm.md`)
- **Total cost:** $0.62 ($0.18 for the six elicitations, $0.43 for the
  two synthesizer calls combined)

## Files

- `raw.json` — all six responses, split into `reasoning` and `rules_file`
- `synthesis.md` — consensus / strong-minority / divergences / omissions / final rules
- `coverage.md` — deterministic rule × model matrix (`rapidfuzz` @ 85)
- `coverage-llm.md` — LLM-judged rule × model matrix (synthesizer bias flagged in the file header)
- `meta.json` — per-model usage & cost, plus synthesis and coverage-LLM call usage

## What to look at first

1. **`synthesis.md` §1 Consensus Rules.** Rules that landed across a majority
   of the panel, with an inline flag distinguishing *near-identical wording*
   (shared training prior art) from *substantively similar but differently
   worded* (genuine convergence).
2. **`coverage.md` vs `coverage-llm.md`.** The same inputs clustered two
   different ways — deterministic string similarity vs one model's judgment.
   Disagreements between them are interesting.
3. **`synthesis.md` §4 Notable Omissions.** Rules that a majority of the
   panel raised but that one model conspicuously skipped.
