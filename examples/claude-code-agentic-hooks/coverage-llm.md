## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Keep hook scripts small / bounded in size (LOC limits). | Style/Performance | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Handle errors explicitly; never let exceptions escape unhandled. | Error Handling | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Log hook decisions/diagnostics with structured context. | Observability | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Parse hook input as strict structured JSON rather than regex/string tricks. | Interface/Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Keep each hook single-purpose / one responsibility per hook. | Structure | ✓ | ✓ | ✓ |  |  | ✓ | 4 |
| Never pass agent/tool-supplied strings into a shell or eval. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Reserve stdout for the protocol; send logs to stderr. | Interface/Protocol | ✓ |  | ✓ |  | ✓ |  | 3 |
| Set a timeout on external/IO operations; abort on expiry. | Error Handling/Performance | ✓ |  |  | ✓ | ✓ |  | 3 |
| Avoid/forbid network I/O in hooks (especially PreToolUse). | Safety/Performance | ✓ |  | ✓ |  | ✓ |  | 3 |
| Validate and canonicalize filesystem paths against an allowlist/workspace root. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Enforce formatting/linting (ruff/black/shellcheck or equivalent). | Style/CI | ✓ | ✓ |  |  | ✓ |  | 3 |
| Follow a consistent naming convention for hooks/functions/constants. | Style | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Validate/schema-check all inputs from the agent before use. | Safety/Correctness | ✓ | ✓ |  | ✓ |  | ✓ | 4 |
| Use `set -euo pipefail` (or equivalent strict mode) in bash hooks. | Style/Error Handling | ✓ |  | ✓ |  |  |  | 2 |
| Fail closed on internal/parse errors in safety-critical gates. | Safety/Error Handling | ✓ |  | ✓ |  | ✓ |  | 3 |
| Keep hooks stateless, idempotent, and deterministic. | Correctness | ✓ |  |  | ✓ | ✓ |  | 3 |
| Use explicit, standardized exit codes / decision enum to signal allow/block. | Interface/Protocol | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Redact secrets/PII from logs; never dump env. | Safety/Observability | ✓ |  |  | ✓ |  |  | 2 |
| Use an explicit allowlist of tools/actions; deny by default. | Safety | ✓ |  |  | ✓ |  |  | 2 |
| Provide tests/fixtures covering allow, deny, and malformed payloads. | Testing/CI | ✓ |  | ✓ |  |  |  | 2 |
| Document each hook with a header comment describing event, intent, effect. | Style/Maintainability | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Register hooks only on supported/standard event names. | Structure/Config | ✓ |  |  |  |  |  | 1 |
| Declare a shebang and executable bit on hook scripts. | Structure | ✓ |  | ✓ |  |  |  | 2 |
| Use narrow matchers, not broad/wildcard matchers. | Structure | ✓ |  | ✓ |  |  |  | 2 |
| Keep hook logic in versioned script files, not inline in settings.json. | Structure/Config | ✓ |  | ✓ |  |  |  | 2 |
| Pin interpreter/command paths; don't rely on PATH. | Config | ✓ |  |  |  |  |  | 1 |
| Do not run full test suites / heavy compute from hot-path hooks. | Performance | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Quote all shell variable expansions in bash hooks. | Style/Safety | ✓ |  | ✓ |  |  |  | 2 |
| Run hooks with least privilege (no sudo). | Safety | ✓ |  |  |  |  |  | 1 |
| Cache expensive computations across invocations when safe. | Performance | ✓ |  | ✓ |  |  |  | 2 |
| Emit one structured log line per invocation with correlation/trace id. | Observability | ✓ |  |  | ✓ |  |  | 2 |
| Gitignore personal/local settings; commit only shared team gates. | Repo Hygiene | ✓ |  | ✓ |  |  |  | 2 |
| Avoid magic numbers / hard-coded strings; use named constants. | Style | ✓ | ✓ |  | ✓ |  | ✓ | 4 |
| Do not use global/module-mutable state inside hooks. | Structure/Safety | ✓ | ✓ |  | ✓ |  | ✓ | 4 |
| Prefer higher-level language (Python) over bash for nontrivial logic. | Style | ✓ |  | ✓ |  | ✓ |  | 3 |
| Profile/benchmark hooks to keep them fast (hot-path latency budget). | Performance | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Block by default when hook is unsure/ambiguous. | Safety | ✓ |  |  | ✓ | ✓ |  | 3 |
| Don't spawn subprocesses / shell out unnecessarily from hooks. | Safety/Performance | ✓ |  |  | ✓ |  |  | 2 |
| When shelling out, pass args as argv array, never interpolate into a shell string. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Distinguish decision outcomes (allow/block/escalate) as explicit enum values. | Observability/Interface | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use O(1)/bounded data structures for lookups; avoid unbounded collection scans. | Performance | ✓ |  |  | ✓ |  |  | 2 |
| Don't depend on full conversation/agent history inside a hook. | Correctness/Performance |  |  |  | ✓ |  |  | 1 |
| Use early returns / explicit control flow rather than nested ternaries or long chains. | Style |  |  |  | ✓ |  |  | 1 |
| Pin dependencies (lockfile / version pins) for hook tooling. | CI/Config | ✓ |  | ✓ |  |  |  | 2 |
| Add CI integration test that loads settings.json and runs each registered hook. | Testing/CI | ✓ |  |  |  |  |  | 1 |
| Cap hook input/output size; refuse or observe on oversize payloads. | Performance/Safety | ✓ |  |  |  |  |  | 1 |
| Treat injected/fetched prompt content as untrusted. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Do not download or dynamically generate hook scripts at runtime. | Safety/Repo Hygiene | ✓ |  |  |  |  |  | 1 |
| Use monotonic clocks when measuring hook duration. | Observability | ✓ |  |  |  |  |  | 1 |
| Provide a clear single entry point (main function) in each hook. | Structure | ✓ |  |  |  |  | ✓ | 2 |
| Include the hook version / commit SHA in emitted logs. | Observability | ✓ |  |  |  |  |  | 1 |

## Notes on clustering decisions

- **"Handle errors explicitly" cluster.** Merged gpt-5's "fail closed / separate internal errors from policy", gpt-4o-mini's "include error handling logic / don't ignore exceptions", opus's `set -euo pipefail` + trap rules, haiku's try/catch rules, and gemini's fail-closed rule. A stricter reading would split these into (a) wrap I/O, (b) never swallow, (c) fail-closed default; I kept them as one because every input framed the rule as "hooks must not silently fail." I then pulled `set -euo pipefail` and "fail closed on safety-critical gates" out as separate narrower rows where models explicitly called them out.
- **"Log hook decisions with structured context" vs "emit one structured log line per invocation with correlation id".** I split these: the first is the broad "log something structured" rule, the second is the narrower gpt-5/haiku rule that mandates a single JSON line with a request/trace id. A regex matcher would probably collapse them.
- **"Parse input as JSON" vs "don't regex structured data".** Merged — gpt-5, opus, haiku, gemini all framed this as "use a real JSON parser on stdin." Haiku additionally generalizes to SQL/shell parsers; I folded that in rather than splitting.
- **"Never pass agent strings to shell/eval" vs "argv array, not shell=True".** Kept as two rows because several models listed them as distinct rules (the first is "don't eval at all", the second is "if you must subprocess, use argv"). Opus, gemini, and gpt-5 have both; haiku has only the first.
- **"Keep hooks small" conflates two sub-rules.** gpt-5 says "<200 LOC file, <50 LOC function"; haiku says "<50 LOC function"; grok says "<100 LOC"; gemini says "<50 LOC"; opus implies it via "bash under ~20 lines." I clustered all size limits into one row because the intent (bound complexity) is identical, even though the numbers differ.
- **"Profile/benchmark hooks for hot-path latency".** I bundled gpt-5's explicit p95 budget, opus's 100 ms target, haiku's "test with realistic payloads," gemini's "milliseconds," and grok-4o-mini's "profile hooks." A stricter reading would separate "set a numeric budget" from "profile in staging."
- **"Don't run heavy compute / full test suites in hot path"** — merged opus's "don't run `npm test` from PostToolUse," haiku's "avoid heavy computation," gemini's "avoid complex algorithms," grok's "no unnecessary computations," and gpt-5's subprocess cap. These could reasonably be three rows (no-heavy-compute, no-full-test-suite, one-subprocess-max); I unified them.
- **"Document each hook with a header comment"** — opus specifies required fields (Event/Matcher/Effect/Bypass), haiku requires JSDoc with decision semantics, gpt-5 says "comment each allow/deny rule", grok says "comment block explaining purpose." Different specificity but same intent, so one row.
- **"Avoid magic numbers / use named constants"** — gpt-4o-mini, grok, and haiku (module-level UPPER_SNAKE_CASE constants) all raise this; gpt-5 raises it implicitly via "stable reason codes from a fixed enum." I counted the enum rule separately ("explicit enum for decisions") rather than folding it in.
- **"Keep each hook single-purpose"** vs **"narrow matcher patterns"** — kept distinct. Single-purpose is about script content; narrow matchers is about settings.json registration. Opus has both; gpt-5 effectively has both.
- **"Block by default on ambiguity"** vs **"fail closed on internal error"** — closely related but I kept them separate because haiku frames the first as a *policy* rule ("if unsure → block") while gpt-5/gemini frame the second as an *error-handling* rule ("if the hook itself crashed → block").
- **Haiku-only items** (early returns, O(1) lookups, no-history-dependency) are genuinely unique to that model's JS-oriented framing; I did not try to map them onto gpt-5's similar-in-spirit rules about determinism or bounded inputs.
- **grok-3-mini's rules are quite generic** ("validate inputs," "handle errors," "avoid magic numbers"). I mapped them to the closest specific cluster from other models rather than giving them their own rows, which inflates grok's coverage relative to a stricter reading.