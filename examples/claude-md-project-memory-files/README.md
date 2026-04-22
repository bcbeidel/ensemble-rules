# Sample run: CLAUDE.md Project Memory Files

Frozen snapshot of one `make claude-md` invocation. Copied from the
gitignored `runs/20260422T204050Z-claude-md-project-memory-files/`.

## Run metadata

- **Topic:** CLAUDE.md Project Memory Files
- **Timestamp:** 2026-04-22T20:40:50Z
- **Wall time:** 171.3s
- **Panel:** 6/6 models returned non-errored responses (`openai/gpt-5`,
  `openai/gpt-4o-mini`, `anthropic/claude-opus-4-7`,
  `anthropic/claude-haiku-4-5`, `vertex_ai/gemini-2.5-pro`, `xai/grok-3-mini`)
- **Synthesizer:** `anthropic/claude-opus-4-7`
- **Total cost:** $0.64 ($0.20 panel + $0.44 synthesizer)

## Files

- `raw.json` — six panel elicitations
- `synthesis.md` — consensus / strong-minority / divergences / omissions / final rules
- `coverage.md` — deterministic rule × model matrix (`rapidfuzz` @ 85)
- `coverage-llm.md` — LLM-judged rule × model matrix
- `meta.json` — per-model usage & cost
