## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Grant only the minimum tools required (principle of least privilege). | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Include concrete examples of expected input/output when format matters. | Correctness | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Keep each subagent single-responsibility / one agent per file. | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Keep the system prompt concise with a token/word cap. | Performance | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| State explicit success criteria / output contract. | Correctness | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use a consistent section ordering/structure across definitions. | Structure | ✓ | ✓ |  | ✓ | ✓ |  | 4 |
| Write descriptions/prompts in clear imperative, active language. | Style | ✓ | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Define explicit stop conditions / failure-mode handling. | Error Handling | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Avoid scope overlap between subagents to prevent routing conflicts. | Maintainability |  |  | ✓ | ✓ | ✓ |  | 3 |
| Constrain or scope shell/bash tool access narrowly (no unconstrained Bash). | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Explicitly forbid dangerous/destructive actions in the system prompt. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Keep scope anchored to specific files/paths/globs. | Scope | ✓ |  | ✓ | ✓ |  |  | 3 |
| Write the description as a precise, action-oriented trigger for delegation. | Structure |  |  | ✓ | ✓ | ✓ |  | 3 |
| Require human approval/confirmation for high-impact or state-changing operations. | Safety | ✓ |  |  |  | ✓ | ✓ | 3 |
| Version subagent definitions and track changes (changelog/history). | Maintainability | ✓ |  |  | ✓ |  | ✓ | 3 |
| Treat tool additions as reviewed, deliberate changes (avoid tool creep). | Maintainability | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use a standardized naming convention for subagent files. | Structure | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Do not contradict the tool allowlist within the system prompt. | Correctness |  |  |  | ✓ |  |  | 1 |
| Remove/archive unused or orphaned subagents. | Maintainability |  |  | ✓ | ✓ |  |  | 2 |
| Define and document input/preconditions explicitly. | Correctness | ✓ |  |  |  | ✓ |  | 2 |
| Require a plan-first / dry-run step before writes. | Safety | ✓ |  |  |  |  |  | 1 |
| Treat repository content as untrusted (guard against prompt injection). | Safety | ✓ |  |  |  |  | ✓ | 2 |
| Disable network access by default; allowlist specific hosts. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Set explicit runtime/tool-call budgets. | Performance | ✓ |  |  |  |  |  | 1 |
| Prefer targeted searches/scopes over whole-repo scans. | Performance | ✓ |  |  |  |  |  | 1 |
| Redact secrets/PII and never handle credentials directly. | Safety | ✓ |  |  |  |  |  | 1 |
| Assign an owner/team for each subagent. | Maintainability | ✓ |  |  |  |  |  | 1 |
| Commit team subagents to the repo; keep personal ones in user dir. | Governance |  |  | ✓ |  |  |  | 1 |
| Assume zero shared context with the caller in the system prompt. | Correctness |  |  | ✓ |  |  |  | 1 |
| Write descriptions in third person (not first person). | Style |  |  | ✓ |  |  |  | 1 |
| Use trigger phrases like "PROACTIVELY"/"MUST BE USED" when auto-routing is needed. | Style |  |  | ✓ |  |  |  | 1 |
| Return structured, concise output rather than full logs. | Performance |  |  | ✓ |  |  |  | 1 |
| Prefer running formatters/linters over describing style in prose. | Style | ✓ |  |  |  |  |  | 1 |
| Test subagents with smoke scenarios / CI against repo snapshots. | Testing | ✓ |  |  |  |  | ✓ | 2 |
| Enforce idempotence for repeatable runs. | Correctness | ✓ |  |  |  |  |  | 1 |
| Review subagent definitions periodically (e.g., quarterly). | Maintainability |  |  |  | ✓ |  |  | 1 |
| Include a "Last Updated" or version marker in the file. | Maintainability |  |  |  | ✓ |  |  | 1 |
| Don't leave TODO/placeholder comments in definitions. | Style |  |  |  | ✓ |  |  | 1 |
| Forbid self-modifying subagents (agents editing their own/other definitions). | Safety |  |  |  | ✓ |  |  | 1 |
| Document known limitations/assumptions explicitly. | Documentation | ✓ |  |  | ✓ |  |  | 2 |
| Prefer fewer broader domain agents over many hyper-specialized ones. | Maintainability |  |  | ✓ |  | ✓ |  | 2 |
| Set tools allowlist explicitly rather than inheriting defaults. | Safety |  |  | ✓ | ✓ | ✓ |  | 3 |
| Do not use wildcards in tool allowlists. | Safety |  |  |  |  | ✓ |  | 1 |
| Include robust error-handling / retry guidance. | Error Handling |  | ✓ |  |  |  | ✓ | 2 |
| Guard against prompt injection from user inputs. | Safety |  |  |  |  |  | ✓ | 1 |
| Define non-goals / explicit "will not" boundaries. | Scope | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use consistent terminology throughout a definition. | Style |  | ✓ |  | ✓ |  |  | 2 |
| Keep description brief and free of marketing/vague language. | Style |  |  | ✓ | ✓ |  |  | 2 |
| Avoid duplicating policy text shared across agents (DRY). | Maintainability | ✓ |  | ✓ |  |  |  | 2 |
| Provide a handoff/escalation rubric with required context. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Maintain up-to-date documentation alongside code changes. | Documentation |  | ✓ |  |  |  |  | 1 |

## Notes on clustering decisions

- **"Least privilege / minimal tools"** absorbs several phrasings ranging from Opus's "minimum tools needed" to Grok's "principle of least privilege" and Gemini's "minimum set of tools" — all clearly the same norm despite different vocabularies.
- **"Avoid scope overlap"** and **"Ensure mutually exclusive descriptions"** were merged; they address the same routing failure mode even though Opus frames it as deletion and Gemini as design.
- **"Explicit tools allowlist rather than inheriting"** (Opus, Haiku, Gemini) was kept separate from the broader "least privilege" rule because it's a distinct mechanical requirement (don't omit the field) vs. a sizing principle.
- **"Constrain Bash / no unconstrained shell"** was kept distinct from the general least-privilege rule because multiple models call it out specifically as a shell-safety pattern (gpt-5's `set -euo pipefail`, Opus's `Bash(npm test:*)`, Haiku's forbid-`rm`).
- **"Keep system prompt concise with token/word cap"** merges different numeric caps (gpt-5: <1000 words; Opus: <1500 tokens; Haiku: <1000 tokens; Grok: <500 tokens). A stricter matcher might split these by threshold.
- **"Use consistent section ordering"** merges gpt-5's specific ordering, gpt-4o-mini's "consistent format," Haiku's explicit section order, and Gemini's "all three sections present" — arguably different granularities.
- **"Define non-goals / will-not boundaries"** merges gpt-5's "state non-goals," Opus's "forbid scope expansion," and Haiku's explicit "Will Not" list; Gemini's "define boundaries" is close but placed under examples/limitations.
- **"Concrete examples in prompts"** merges Opus ("one example beats three paragraphs"), Haiku ("concrete examples"), Gemini ("concrete examples of inputs/outputs"), Grok ("Don't include unnecessary examples" — note: Grok actually argues *against* verbose examples, so Grok was **not** counted here; only gpt-5's minimal-examples rule was counted as supportive).
- **"Write in imperative/active voice"** groups gpt-5's "imperative instructions," gpt-4o-mini's "plain concise language," Haiku's "plain imperative language," Gemini's "begin with a verb," and Grok's "active voice." These are all style guidance but span description-writing vs. prompt-writing; lumped together.
- **"Stop conditions / failure handling"** merges gpt-5's explicit `stop_conditions`, Haiku's "document failure modes," Gemini's "define boundaries/limitations," and Grok's "error-handling instructions." Gemini's inclusion here is a judgment call.
- **Grok's "version history section"** and Haiku's "Last Updated date" and gpt-5's `version` front-matter field were merged into a single versioning cluster despite different mechanisms.
- **gpt-4o-mini** contributed mostly high-level/abstract rules; many of its rules map weakly to multiple clusters (e.g., "robust error handling" is generic). I credited it only where the correspondence was clear.
- **"Prefer fewer broader agents"** (Opus, Gemini) is explicitly flagged contested by both; kept as one cluster.
- **"Test subagents"** merges gpt-5's CI-snapshot rule and Grok's latency-testing rule, which target different qualities (correctness vs. performance) but share the imperative to test definitions.