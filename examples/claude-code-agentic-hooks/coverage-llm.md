## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Keep each hook focused on a single concern or responsibility. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Validate and sanitize event/input payload before acting on it. | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Keep hook execution fast (sub-100–200ms budget). | Performance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Log hook decisions with structured context for auditability. | Observability | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Write unit/integration tests for hooks covering edge cases. | Testing | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Handle errors explicitly; do not silently swallow failures. | Error Handling | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Block/deny known-destructive patterns (e.g., rm -rf, credential exfiltration). | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Avoid network calls / slow external I/O in synchronous hooks. | Performance | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use clear, intent-revealing names for hooks/scripts. | Style | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Fail closed on ambiguity/errors in gating hooks. | Safety | ✓ |  |  | ✓ | ✓ |  | 3 |
| Prefer allowlists over blocklists for high-risk actions. | Safety | ✓ |  |  | ✓ |  |  | 2 |
| Require user confirmation for destructive/escalated actions. | Safety | ✓ | ✓ |  |  |  |  | 2 |
| Never eval or shell-interpolate untrusted payload fields. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Cache compiled regexes / static policy data across invocations. | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Keep hooks stateless and idempotent. | Structure | ✓ |  |  |  | ✓ |  | 2 |
| Keep hooks deterministic (pure function of input + config). | Correctness | ✓ |  |  |  | ✓ |  | 2 |
| Document each hook's purpose, events, and contract in a header/readme. | Documentation | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Emit block messages that tell the agent exactly how to comply. | UX | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use conventional exit codes to signal allow/block. | I/O Contract | ✓ |  | ✓ |  | ✓ |  | 3 |
| Write logs/diagnostics to stderr, not stdout. | I/O Contract | ✓ |  | ✓ |  | ✓ |  | 3 |
| Redact secrets/PII from logs and outputs. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Version-control hooks and treat policy changes like code (review, changelog). | Operations | ✓ |  | ✓ | ✓ |  |  | 3 |
| Roll out new blocking hooks gradually (canary / log-only first). | Operations | ✓ |  | ✓ |  |  |  | 2 |
| Use least-privilege execution / limit hook permissions. | Safety | ✓ |  |  | ✓ | ✓ |  | 3 |
| Constrain file operations to the workspace and canonicalize paths. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Defer heavy checks (typecheck, test suite) to Stop rather than per-edit events. | Performance | ✓ |  | ✓ |  |  |  | 2 |
| Avoid auto-approving tool calls that would normally require user confirmation. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Prefer rejection over silent transformation of tool arguments. | Safety |  |  |  | ✓ |  |  | 1 |
| Prefer data-driven/declarative rules over hard-coded constants. | Style | ✓ | ✓ |  |  |  |  | 2 |
| Standardize on one implementation language/runtime for hooks. | Style | ✓ |  |  |  |  |  | 1 |
| Do not retry synchronously inside hooks. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Use tight timeouts (and circuit breakers) on any external call. | Error Handling | ✓ |  |  | ✓ |  |  | 2 |
| Emit exactly one structured response per invocation per the platform contract. | I/O Contract | ✓ |  | ✓ |  | ✓ |  | 3 |
| Use exact tool-name matchers, not broad wildcards. | Structure |  |  | ✓ |  |  |  | 1 |
| Start bash hooks with `set -euo pipefail`. | Style |  |  | ✓ |  |  |  | 1 |
| Put hook logic in script files rather than inline JSON strings. | Structure |  |  | ✓ |  |  |  | 1 |
| Avoid using the user's prompt to infer safety/intent. | Safety |  |  |  | ✓ |  |  | 1 |
| Validate argument types/schema, not just presence via optional chaining. | Correctness |  |  |  | ✓ |  |  | 1 |
| Avoid dependencies / keep startup overhead minimal. | Performance |  |  |  |  | ✓ |  | 1 |
| Limit hook code size (e.g., under ~50–100 lines). | Style |  |  |  | ✓ |  | ✓ | 2 |
| Avoid global/shared mutable state across hooks. | Structure | ✓ |  |  |  |  | ✓ | 2 |
| Scope destructive hooks to local/personal settings, not team-shared settings. | Operations |  |  | ✓ |  |  |  | 1 |
| Include stable rule IDs / policy-version in decisions. | Observability | ✓ |  |  |  |  |  | 1 |
| Track/alert on hook latency percentiles. | Observability | ✓ |  |  |  |  |  | 1 |
| Provide a controlled fail-open kill switch for emergencies. | Operations | ✓ |  |  |  |  |  | 1 |
| Treat Stop as best-effort; don't rely on it for critical enforcement. | Correctness | ✓ |  |  |  |  |  | 1 |
| Avoid magic numbers; use named constants. | Style |  | ✓ |  |  |  |  | 1 |
| Use asynchronous patterns for non-critical telemetry/logging. | Performance | ✓ | ✓ |  |  |  | ✓ | 3 |
| Implement rate limiting / cooldowns on repeated events. | Safety |  |  |  |  |  | ✓ | 1 |
| Separate policy logic from plumbing (logging, error handling). | Structure |  |  |  | ✓ |  |  | 1 |
| Pin/verify dependencies with lockfiles or checksums. | Operations | ✓ |  |  |  |  |  | 1 |
| Use UserPromptSubmit for context injection rather than prompt validation. | Event Guidance |  |  | ✓ |  |  |  | 1 |
| Use SessionStart to warm caches / amortize expensive setup. | Event Guidance |  |  | ✓ |  |  |  | 1 |
| Ship fixtures per event type and pipe them into hooks for testing. | Testing |  |  | ✓ | ✓ |  |  | 2 |
| Exit silently on success; avoid noisy success output. | Style |  |  | ✓ |  |  |  | 1 |
| Short-circuit cheap checks early to minimize latency. | Performance | ✓ |  | ✓ |  |  |  | 2 |

## Notes on clustering decisions

- **"Keep each hook focused on a single concern"** merges gpt-5's "single-purpose hooks", gpt-4o-mini's "small and focused", opus's "one hook script per concern", haiku's "single, focused policy", gemini's "single responsibility", and grok's "single, focused function per event". These are phrased quite differently but express the same norm.
- **"Validate and sanitize event/input payload"** collapses schema validation (gpt-5, haiku, gemini), generic input validation (gpt-4o-mini, grok), and opus's specific "parse stdin JSON with jq, never interpolate". A stricter clusterer might split schema-validation from injection-prevention; I kept them together because models often phrased both as one rule.
- **"Never eval / shell-interpolate untrusted payload"** is kept separate from the broader input-validation cluster because opus, gemini, and haiku (implicitly via "don't use optional chaining as your only defense" … actually no) explicitly call out code-execution risk. I credited opus and gemini; haiku's version is about validation, not eval, so not credited here.
- **"Block known-destructive patterns"** vs **"Avoid auto-approving"** vs **"Scope destructive hooks locally"**: kept as three clusters because they address different policy postures (deny-list content, approve-decision posture, where destructive logic lives).
- **"Fast hook execution budget"**: gpt-5 (200ms), opus (200ms/2s), haiku (100ms), gemini (100ms), grok (100ms), gpt-4o-mini (profile/optimize). I clustered gpt-4o-mini's softer "profile and optimize" with the latency-budget rule; a stricter reading would exclude it.
- **"Write logs to stderr, not stdout"**: gpt-5 and opus say this explicitly about the I/O channel contract; gemini says "all logging to stderr". Clustered together.
- **"Use conventional exit codes"**: gpt-5 (exit 0/nonzero), opus (exit 0/2), gemini (exit 0/nonzero). Opus's exit-2-specific semantics are Claude-Code-specific but I clustered them with the general rule.
- **"Redact secrets/PII"**: gpt-5, opus, haiku, gemini, grok all mention this under various guises (secret scanning, log redaction, sanitize payload in logs). Clustered as one.
- **"Async for non-critical telemetry"** vs **"Avoid network calls in sync hooks"**: kept distinct — the first is about deferring work, the second is about not doing it at all in the hot path. gpt-4o-mini's "don't perform blocking operations" straddles both; I put it under the async cluster.
- **"Document hook purpose in a header/readme"**: merged opus's header-comment rule, haiku's docstring rule, gemini's comment-block rule, and gpt-5's README-adjacent-to-hooks rule. These differ in location (inline vs adjacent file) but serve the same purpose.
- **"Emit block messages that tell the agent how to comply"**: opus is most explicit; gpt-5's "user-actionable deny messages" and haiku's "document reasoning behind deny" are close enough to cluster.
- **"Cache compiled regexes / static policy data"**: gpt-5 (compiled regexes), opus (cache by mtime), haiku (cache static policy in memory). Different cache targets but same underlying rule.
- I did **not** cluster gpt-4o-mini's "don't nest too many levels of hooks" with anything else — no other model raised nesting depth.
- I did **not** cluster grok's "don't use global variables" with gpt-5's "avoid shared mutable state across hooks" tightly; they're close but grok is scoped to within-hook style and gpt-5 is cross-hook. I ultimately put them in one row as the spirit matches.