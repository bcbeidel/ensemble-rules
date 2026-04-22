# Sample run: Claude Code Agentic Hooks

Frozen snapshot of one `make agentic-hooks` invocation. Copied from the
gitignored `runs/20260422T203242Z-claude-code-agentic-hooks/`.

## Run metadata

- **Topic:** Claude Code Agentic Hooks
- **Timestamp:** 2026-04-22T20:32:42Z
- **Wall time:** 228.2s
- **Panel:** 6/6 models returned non-errored responses (`openai/gpt-5`,
  `openai/gpt-4o-mini`, `anthropic/claude-opus-4-7`,
  `anthropic/claude-haiku-4-5`, `vertex_ai/gemini-2.5-pro`, `xai/grok-3-mini`)
- **Synthesizer:** `anthropic/claude-opus-4-7`
- **Total cost:** $0.74 ($0.22 panel + $0.52 synthesizer)

## Files

- `raw.json` — six panel elicitations
- `synthesis.md` — consensus / strong-minority / divergences / omissions / final rules
- `coverage.md` — deterministic rule × model matrix (`rapidfuzz` @ 85)
- `coverage-llm.md` — LLM-judged rule × model matrix
- `meta.json` — per-model usage & cost
