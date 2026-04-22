# Sample run: Claude Code Subagent Definitions

Frozen snapshot of one `make subagents` invocation. Copied from the
gitignored `runs/20260422T201953Z-claude-code-subagent-definitions/`.

## Run metadata

- **Topic:** Claude Code Subagent Definitions
- **Timestamp:** 2026-04-22T20:19:53Z
- **Wall time:** 172.2s
- **Panel:** 6/6 models returned non-errored responses (`openai/gpt-5`,
  `openai/gpt-4o-mini`, `anthropic/claude-opus-4-7`,
  `anthropic/claude-haiku-4-5`, `vertex_ai/gemini-2.5-pro`, `xai/grok-3-mini`)
- **Synthesizer:** `anthropic/claude-opus-4-7`
- **Total cost:** $0.68 ($0.20 panel + $0.48 synthesizer)

## Files

- `raw.json` — six panel elicitations
- `synthesis.md` — consensus / strong-minority / divergences / omissions / final rules
- `coverage.md` — deterministic rule × model matrix (`rapidfuzz` @ 85)
- `coverage-llm.md` — LLM-judged rule × model matrix
- `meta.json` — per-model usage & cost
