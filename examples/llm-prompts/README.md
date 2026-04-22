# Sample run: LLM Prompts

Frozen snapshot of one `make prompts` invocation. Copied from the
gitignored `runs/20260422T205655Z-llm-prompts/`.

## Run metadata

- **Topic:** LLM Prompts
- **Timestamp:** 2026-04-22T20:56:55Z
- **Wall time:** 216.6s
- **Panel:** 6/6 models returned non-errored responses (`openai/gpt-5`,
  `openai/gpt-4o-mini`, `anthropic/claude-opus-4-7`,
  `anthropic/claude-haiku-4-5`, `vertex_ai/gemini-2.5-pro`, `xai/grok-3-mini`)
- **Synthesizer:** `anthropic/claude-opus-4-7`
- **Total cost:** $0.68 ($0.19 panel + $0.49 synthesizer)

## Files

- `raw.json` — six panel elicitations
- `synthesis.md` — consensus / strong-minority / divergences / omissions / final rules
- `coverage.md` — deterministic rule × model matrix (`rapidfuzz` @ 85)
- `coverage-llm.md` — LLM-judged rule × model matrix
- `meta.json` — per-model usage & cost
