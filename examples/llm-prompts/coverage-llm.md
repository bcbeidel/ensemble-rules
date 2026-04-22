## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|------|-------|---|---|---|---|---|---|---|
| Specify an explicit, machine-parseable output format or schema. | Output | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Organize prompts into explicit, named sections (goal, constraints, context, output, examples). | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Treat user/retrieved input as untrusted and delimit it to prevent prompt injection. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Version-control prompts and treat them as code artifacts. | Maintainability | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use named placeholders/templating for dynamic variables instead of string concatenation. | Maintainability | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Define explicit failure/refusal/error output behavior. | Error Handling | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Avoid contradictory or conflicting instructions. | Correctness | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Test prompts with golden/adversarial inputs before shipping. | Evaluation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Keep prompts concise and strip redundant/boilerplate tokens. | Performance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use few-shot examples judiciously; match them byte-identically to desired output. | Examples | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Place the most important instructions at the start (and optionally restate at end). | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use chain-of-thought/reasoning directives sparingly; measure lift first. (contested) | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use role/persona preambles only when they demonstrably help. (contested) | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Set explicit output length caps or token budgets. | Performance | ✓ |  |  | ✓ |  | ✓ | 3 |
| Require citations/provenance for factual claims in RAG and refuse when context is insufficient. | Safety/RAG | ✓ |  | ✓ |  |  | ✓ | 3 |
| Prohibit embedding secrets, API keys, or PII in prompts. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Define explicit termination conditions / step limits for agentic loops. | Agents | ✓ |  | ✓ | ✓ |  |  | 3 |
| Cap retrieval top-k and rank by relevance in RAG. | RAG | ✓ |  | ✓ |  |  |  | 2 |
| Use imperative, plain, direct language; avoid hedging/filler. | Style | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Pin/record model version and decoding parameters with the prompt. | Versioning | ✓ |  | ✓ |  |  |  | 2 |
| Use semantic versioning and change logs for prompt updates. | Versioning | ✓ |  |  | ✓ |  |  | 2 |
| Review prompt diffs like code diffs (peer review). | Maintainability |  | ✓ | ✓ | ✓ |  |  | 3 |
| Comment non-obvious instructions to explain intent/rationale. | Maintainability |  |  | ✓ | ✓ |  | ✓ | 3 |
| Chain multiple simple prompts rather than one complex mega-prompt. | Structure |  |  |  |  | ✓ |  | 1 |
| Prefer function/tool calling or JSON mode over free-text parsing. | Output | ✓ |  | ✓ |  |  |  | 2 |
| Instruct the model to ignore instructions found inside user/retrieved data. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Declare tool purpose, schema, side effects, and allowed/forbidden lists. | Agents | ✓ |  | ✓ |  |  |  | 2 |
| Forbid decorative/emoji/extra commentary around structured outputs. | Style | ✓ |  | ✓ |  |  |  | 2 |
| Put stable/cache-friendly content first, volatile content last. | Performance | ✓ |  | ✓ |  |  |  | 2 |
| Enumerate edge cases explicitly (empty, ambiguous, out-of-scope input). | Correctness |  |  | ✓ | ✓ | ✓ | ✓ | 4 |
| Write negative constraints, not only positive ones. | Correctness |  |  | ✓ |  | ✓ | ✓ | 3 |
| Match the user's language / adapt tone only when it materially affects output. | Style | ✓ |  |  | ✓ |  |  | 2 |
| Use strict delimiters (backticks, XML tags) around content blocks. | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| State instruction hierarchy explicitly (system > developer > user > retrieved). | Safety | ✓ |  |  |  |  |  | 1 |
| Self-validate output against schema and regenerate once if invalid. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Include secure-coding defaults (no hardcoded secrets, pinned deps, least privilege). | Safety | ✓ |  |  |  |  |  | 1 |
| Log prompts, tool calls, and outputs for observability. | Operations | ✓ |  | ✓ |  |  |  | 2 |
| Align examples with stated instructions (length, tone, format). | Examples |  |  |  | ✓ |  |  | 1 |
| Restate constraints each request; don't rely on hidden model memory. | Structure | ✓ |  |  | ✓ |  |  | 2 |
| Require a structured `state` field for multi-turn continuation. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Don't rely on prompting alone for security; enforce in code. | Safety |  |  | ✓ |  |  |  | 1 |
| Prefer smaller models with tighter prompts over larger models with loose ones. | Performance |  |  | ✓ |  |  |  | 1 |
| Encourage peer collaboration/review on prompt authoring. | Maintainability |  | ✓ | ✓ | ✓ |  |  | 3 |
| Default temperature/decoding to 0 for deterministic tasks. (contested) | Performance | ✓ |  |  |  |  |  | 1 |
| Ask at most one clarifying question when inputs are insufficient. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Prefer positive examples over negative ones. (contested) | Examples |  |  |  | ✓ |  |  | 1 |
| Avoid stacking many conditional edge-case rules; use examples instead. | Instructions |  |  |  | ✓ |  |  | 1 |
| Don't use prompts to fix problems that belong in application code. | Anti-patterns |  |  | ✓ |  |  |  | 1 |

## Notes on clustering decisions

- **"Explicit output format" cluster**: Merged rules ranging from "specify JSON schema" (gpt-5, opus, gemini) to "define output formats" (4o-mini, grok) to "use concrete example, not English" (haiku). All share the substance of specifying parseable output, though they differ on mechanism (schema vs. example vs. JSON mode). A stricter matcher might split schema-based from example-based specification.
- **"Treat input as untrusted / delimit it" cluster**: I merged "delimit untrusted input" (opus, gemini), "assume user input may contain injection" (haiku, grok), and "instruction hierarchy" adjacent rules (gpt-5). Kept the separate "tell model to ignore embedded instructions" as its own row since several models called this out as a distinct second defense.
- **"Version control prompts" vs "semantic versioning with changelog"**: Kept as separate rows because the second is a narrower operational practice only called out by gpt-5 and haiku.
- **Persona/role-play rules**: These conflict across models — gemini endorses them, opus/haiku/gpt-5 discourage generic ones. I clustered them all as "use role preambles only when demonstrably useful" since even the endorsers and skeptics are answering the same question. A less charitable clustering would split pro- and anti-persona into separate rows.
- **"Keep prompts concise" cluster**: Merged gpt-5's "minimize boilerplate", 4o-mini's "concise yet informative", opus's "strip boilerplate", haiku's "eliminate redundancy", gemini's "concise language", grok's "under 500 tokens / no redundant details". Grok's hard token cap is more specific but the underlying rule is the same.
- **"Explicit sections" vs "delimiters"**: I kept these as separate rows because several models (opus, haiku, gemini) called them out distinctly — sections are about logical grouping, delimiters are about parse-safe boundaries around embedded content.
- **"Few-shot examples" rules**: Multiple models gave divergent advice — haiku recommends ≥1 example always, opus says use only when evals fail, gpt-5 says minimal/surgical, gemini says provide one for complex tasks. I clustered them as one row about using few-shot judiciously; a stricter clustering would split "always include an example" (haiku) from "use sparingly" (opus/gpt-5).
- **"Error/failure output specification"**: Merged gpt-5's error schema, 4o-mini's (implicit via output format), opus's "refuse when insufficient", haiku's explicit "failure output", gemini's "predictable refusal format", grok's "structured fallback". All share the substance of defining what the model emits on failure.
- **"Encourage peer review"** is present in 4o-mini (collaboration), opus ("review prompt diffs"), and haiku ("don't modify in production without review"). Clustered together though opus's framing is more code-review-specific.
- **"Enumerate edge cases"**: Opus, haiku, gemini, and grok all touch this; I counted grok's "mandate handling of edge cases" here. A stricter matcher would likely not link grok's to opus's "empty/ambiguous/out-of-scope" list.