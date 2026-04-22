# Sample run: Agent Skills

Frozen snapshot of one `make agent-skills` invocation. Copied from the
gitignored `runs/20260422T201148Z-agent-skills/`.

## Run metadata

- **Topic:** Agent Skills
- **Timestamp:** 2026-04-22T20:11:48Z
- **Wall time:** 208.7s
- **Panel:** 6/6 models returned non-errored responses (`openai/gpt-5`,
  `openai/gpt-4o-mini`, `anthropic/claude-opus-4-7`,
  `anthropic/claude-haiku-4-5`, `vertex_ai/gemini-2.5-pro`, `xai/grok-3-mini`)
- **Synthesizer:** `anthropic/claude-opus-4-7`
- **Total cost:** $0.71 ($0.19 panel + $0.52 synthesizer)

## Files

- `raw.json` — six panel elicitations
- `synthesis.md` — consensus / strong-minority / divergences / omissions / final rules
- `coverage.md` — deterministic rule × model matrix (`rapidfuzz` @ 85)
- `coverage-llm.md` — LLM-judged rule × model matrix
- `meta.json` — per-model usage & cost
