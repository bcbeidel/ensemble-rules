# Synthesis of Claude Code Agentic Hooks Best Practices

## 1. Consensus Rules

### Structure & Organization

- **Keep each hook focused on a single concern/responsibility.** Single-purpose hooks are easier to test, audit, and reason about. *(substantively similar but differently worded across GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Name hooks descriptively by event and intent (e.g., `pretooluse-bash-guard.sh`, `block_force_push.py`).** Clear naming aids discoverability and incident response. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Document each hook's purpose, trigger events, and assumptions in a header comment.** Future maintainers and AI assistants need this context. *(substantively similar across Claude Opus, Claude Haiku, Gemini)*

### I/O Contract & Exit Codes

- **Write only machine-readable output to stdout; send logs/diagnostics to stderr.** Mixing channels corrupts the hook contract. *(near-identical across GPT-5, Claude Opus, Gemini)*
- **Use exit code 0 for allow/success and non-zero (specifically exit 2 in Claude Code) to block.** This is the documented contract with the agent runner. *(substantively similar across GPT-5, Claude Opus, Gemini)*
- **Validate and parse stdin JSON defensively before acting on it.** Malformed input should not crash or silently bypass the hook. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Safety

- **Never `eval` or interpolate stdin payload fields directly into a shell command.** Tool inputs can be attacker-controlled via ingested content — this is an RCE vector. *(near-identical across Claude Opus, Gemini; substantively similar in GPT-5, Claude Haiku)*
- **Default-deny / fail-closed on ambiguity, malformed input, or uncertainty in PreToolUse.** A false positive is recoverable; a false negative on a destructive action may not be. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Validate file paths against the project workspace (e.g., `$CLAUDE_PROJECT_DIR`) and canonicalize to prevent traversal.** Symlinks and `..` segments bypass naive checks. *(substantively similar across GPT-5, Claude Opus)*
- **Maintain explicit block rules for known-dangerous patterns (`rm -rf`, `curl | sh`, force-push, credential exfiltration).** The permission system is not a substitute for hardened denies. *(substantively similar across GPT-5, Claude Opus, Gemini)*
- **Validate input argument types, shapes, and required fields explicitly — don't rely on optional chaining as a defense.** Silent failures on missing fields hide bugs. *(substantively similar across Claude Haiku, Gemini, Grok)*

### Performance

- **Keep PreToolUse hooks under ~100–200ms on the common path.** Hooks are synchronous and tax every agent turn. *(near-identical budget across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Avoid network calls in synchronous hooks (especially PreToolUse).** Network latency is unpredictable and blocks the agent. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Defer expensive checks (full typecheck, test suite, security scan) to `Stop`, not per-edit `PostToolUse`.** Per-edit heavy checks cause retry storms and unusable slowness. *(substantively similar across GPT-5, Claude Opus)*
- **Short-circuit irrelevant events early (check tool name/extension before doing work).** A no-op hook should cost near-zero. *(substantively similar across GPT-5, Claude Opus, Grok)*

### Error Handling

- **Catch exceptions inside hooks and return a deterministic deny + log, rather than crashing.** Uncaught exceptions break the agent loop. *(substantively similar across Claude Haiku, Gemini, Grok, GPT-4o-mini)*
- **Never silently swallow errors or return ambiguous results.** Silent failures are a security smell and hide regressions. *(substantively similar across GPT-5, Claude Haiku, GPT-4o-mini, Grok)*
- **Set hard timeouts on any external I/O and default to deny on timeout.** Low confidence should not mean permissive. *(substantively similar across GPT-5, Claude Haiku)*

### Logging & Observability

- **Log every blocking decision with structured fields (timestamp, event, tool, rule, reason).** Unstructured logs can't be audited or alerted on. *(near-identical structure across GPT-5, Claude Opus, Claude Haiku)*
- **Make every block message tell the agent exactly what to do to unblock.** Vague "forbidden" messages cause retry loops; specific guidance causes correction. *(substantively similar across Claude Opus, Claude Haiku)*
- **Redact secrets and PII from all hook output and logs.** Hook output is shown to the agent and persisted. *(substantively similar across GPT-5, Claude Haiku)*

### Testing

- **Write fixture-based tests for each hook covering valid input, malformed input, and edge cases.** Hooks are security-critical code and deserve the same rigor as production logic. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok, GPT-4o-mini)*
- **Ship a `fixtures/` directory with sample payloads per event type.** Protects against schema drift and makes local debugging trivial. *(raised explicitly by Claude Opus, echoed by Claude Haiku)*

---

## 2. Strong Minority Rules

- **Put hook logic in a script file under `.claude/hooks/`, not inline in `settings.json` JSON.** *(Claude Opus)* — This is the single most Claude-Code-specific rule; JSON-escaped shell is unreviewable, undiffable, and untestable. Including because it's operationally correct and specific to this tool.
- **Begin every bash hook with `set -euo pipefail`.** *(Claude Opus)* — Without it, pipeline failures silently pass. Concrete, high-value, hard-won.
- **Scope destructive hooks to `.claude/settings.local.json`, not team-shared settings.** *(Claude Opus)* — Prevents one bad team-level hook from corrupting every teammate's workflow.
- **Roll new blocking hooks out as log-only for a period before flipping to exit 2.** *(Claude Opus)* — Pragmatic rollout practice that prevents friction spikes.
- **Use `UserPromptSubmit` for context injection (branch, style guide, PR), not prompt validation.** *(Claude Opus)* — Event-specific guidance grounded in how the events actually fire.
- **Use `SessionStart` (runs once) to warm caches and surface environment summary — amortize expensive setup here.** *(Claude Opus)* — The only safe place for network/slow work.
- **Prefer rejection over silent transformation of tool arguments.** *(Claude Haiku)* — Transformation obscures causality and confuses the agent's model of its own actions. Important correctness/transparency principle.
- **Base decisions on observable facts (tool name, args, resource), not inferred intent from the user's prompt.** *(Claude Haiku)* — Prompts are ambiguous; this is a sharp, non-obvious rule.
- **Prefer allowlists over blocklists for high-risk operations.** *(GPT-5, Claude Haiku)* — Blocklists grow forever and miss novel variants. Widely endorsed in security but worth stating explicitly.
- **Pin/cache static policy data in memory; refresh on a timer, not per-request.** *(Claude Haiku)* — Concrete performance pattern for hooks that need external data.
- **Emit silent success — do not print "✅ hook passed" on every run.** *(Claude Opus)* — Noise on every turn desensitizes users to real signals.

---

## 3. Divergences

### Auto-approval in PreToolUse
- **Claude Opus:** Almost never use `"decision": "approve"` — it bypasses the user permission prompt.
- **GPT-5:** Implicitly allows via default-deny + explicit allowlist model.
- **Synthesis:** Side with Claude Opus. Auto-approve trains users to trust unseen actions and defeats the permission system. Use allowlisting to *not block*, not to affirmatively approve.

### Language/runtime for hooks
- **GPT-5:** Standardize on one language (contested flag).
- **Gemini:** Strongly prefer Python 3; avoid dependencies entirely.
- **Claude Opus:** Bash for <30 lines, Python/Node for longer.
- **Synthesis:** The Claude Opus rule is the most operationally honest — bash is fine for tiny gates, but scales badly. Avoid heavy dependencies regardless of language. Team standardization is a nice-to-have, not a rule.

### Inline vs. file-based hook implementation
- **Claude Opus:** Strongly require script files, not inline JSON.
- **Others:** Silent on this.
- **Synthesis:** Claude Opus is right and this is the most tool-specific rule in the set. Include in final rules.

### PostToolUse transformation (e.g., auto-format)
- **Claude Opus:** OK for deterministic formatters on edited file; defer semantic rewrites to Stop.
- **Claude Haiku:** Avoid transformation entirely; prefer rejection.
- **Synthesis:** These are compatible if scoped carefully. Deterministic idempotent formatting of the *same file the agent just edited* is fine (agent will re-read). Transforming *arguments* (what Haiku is talking about) is a different operation and should be avoided. Final rules distinguish these.

### Fail-open vs. fail-closed policy posture
- **GPT-5:** Fail-closed on PreToolUse, fail-open on PostToolUse/Stop.
- **Claude Haiku:** Fail-closed on ambiguity everywhere.
- **Gemini, Grok:** Generally fail-closed.
- **Synthesis:** GPT-5's split is the most nuanced and correct. Enforcement events fail closed; telemetry/observability events fail open to preserve UX.

### Async hooks
- **Grok:** Use async for non-critical hooks (e.g., Stop logging).
- **GPT-5, Gemini, Claude Opus:** Treat hooks as synchronous; defer heavy work to later events, don't try to async within one.
- **Synthesis:** Side with the majority. Claude Code hooks are synchronous by design; "async" within a hook usually means fire-and-forget logging, which is fine but not a load-bearing pattern. Don't introduce async complexity into the hook runtime itself.

---

## 4. Notable Omissions

- **GPT-4o-mini** omits nearly everything concrete about the Claude Code hook contract: no mention of exit codes, stdin/stdout channels, event-type-specific guidance, or the `.claude/` directory structure. Its rules are generic "good software" rules that could apply to any script. This suggests shallow engagement with the actual tool.
- **GPT-4o-mini and Grok** omit the I/O contract (stdout = machine, stderr = logs) that Claude Opus, GPT-5, and Gemini all emphasize. This is critical — violating it breaks the hook silently.
- **GPT-4o-mini, Grok, and Gemini** omit **`eval`/injection safety on stdin payload**, which Claude Opus and Claude Haiku rightly flag as an RCE vector. A significant oversight.
- **Gemini and Grok** omit event-specific guidance (when to use Stop vs. PostToolUse vs. SessionStart). Claude Opus is uniquely strong here, and this is genuinely Claude Code-specific knowledge.
- **GPT-4o-mini** omits any mention of path canonicalization, allowlist vs. blocklist, or specific dangerous patterns like `rm -rf`. All other models raised at least one.
- **Grok** omits logging structure (what fields to log) and redaction of secrets — a meaningful safety gap.
- **Claude Haiku** omits the script-file-vs-inline-JSON rule that is arguably the most tool-specific best practice. Haiku focused on policy logic, not Claude Code's configuration mechanics.

---

## 5. Final Rules File

# Claude Code Agentic Hooks — Rules

**Scope.** Hooks configured under `hooks:` in `.claude/settings.json`, `.claude/settings.local.json`, or `~/.claude/settings.json`, across events: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `Notification`, `PreCompact`, and `SessionStart`.

**Audience.** Engineers authoring team-shared or personal hooks, and AI assistants generating hook configurations.

**Premise.** Hooks are synchronous, blocking gatekeepers on the agent's critical path. They are also a security boundary: they run with the user's full shell privileges on attacker-influenceable input. Design for speed, determinism, and hardened safety.

---

## Structure

- **Put hook logic in a script file (e.g., `.claude/hooks/pretooluse-bash-guard.sh`), not inline in `settings.json`.** JSON-escaped shell is unreviewable, undiffable, and untestable.
- **Store all hook scripts under `.claude/hooks/` in the repository.** Colocates hook behavior with code; makes hooks versioned and reviewable.
- **Make hook scripts executable with an explicit shebang (`#!/usr/bin/env bash`, `python3`, `node`).** Don't rely on the parent shell's interpreter.
- **Keep each hook focused on a single concern.** Compose multiple focused hooks rather than one mega-script with internal dispatch.
- **Name hooks by event and purpose (`posttooluse-format.sh`, `stop-run-tests.sh`).** Matches the mental model engineers bring to `settings.json`.
- **Include a header comment documenting purpose, triggered events, matchers, exit contract, and expected latency.** Future maintainers (including AI) need this context.
- **Write matchers as exact tool names (`"Bash"`, `"Edit"`, `"Write"`, `"MultiEdit"`), not regex wildcards.** Broad matchers fire on events you didn't intend and slow every turn.
- **Write hooks in bash for under ~30 lines of logic; switch to Python or Node for anything longer.** Bash at scale becomes a maintenance liability.

## I/O Contract and Exit Codes

- **Write machine-readable output (JSON response) only to stdout; write diagnostics and logs only to stderr.** Mixed channels corrupt the hook protocol.
- **Exit 0 to allow/succeed, exit 2 to block and feed stderr to the agent, other non-zero only for hook bugs.** This is the documented contract.
- **Prefer structured JSON output (`{"decision": "block", "reason": "..."}`) over exit-code-only signaling for anything beyond a binary gate.** JSON supports `reason`, `suppressOutput`, and `hookSpecificOutput`.
- **Validate the stdin JSON structure defensively at the start of every hook.** Malformed input should not crash or silently bypass the hook.
- **Do not write to stdout when exiting non-zero.** The runner ignores it; it will only mislead during debugging.
- **Exit silently on success — do not print status banners on every invocation.** Noise on every turn desensitizes users to real signals.

## Safety

- **Never `eval`, `bash -c`, or interpolate stdin payload fields directly into shell commands.** Tool inputs may contain attacker-controlled strings from files, issues, or web content. Parse with `jq` or a real JSON parser.
- **Base decisions on observable facts (tool name, arguments, target resource) rather than inferred intent from the user's prompt.** Prompts are ambiguous; observable structure is not.
- **Default-deny / fail-closed on PreToolUse for malformed input, ambiguity, or unrecognized high-risk operations.** A false positive is recoverable; a false negative on a destructive action may not be.
- **Fail-open on PostToolUse and Stop when errors occur.** Enforcement failures on telemetry should not block the user.
- **Validate file paths against `$CLAUDE_PROJECT_DIR` and canonicalize (realpath) before acting on them.** Prevents traversal via symlinks or `..` segments.
- **Maintain explicit block rules for `rm -rf`, `curl|sh`, `mkfs`, force-push, credential exfiltration patterns, and writes to metadata/private-network endpoints.** The permission system is not a substitute for hardened denies.
- **Prefer allowlists over blocklists for high-risk operations.** Blocklists grow forever and miss novel variants.
- **Scope destructive or side-effecting hooks (git commits, network calls, file deletion) to `.claude/settings.local.json`, not team settings.** Team-shared destructive automation corrupts repos at scale.
- **Never `"decision": "approve"` in PreToolUse to auto-approve calls that would normally prompt the user.** Bypasses the permission system and trains users to trust unseen actions.
- **Do not read secrets from the environment into any string that may reach stdout, stderr, or logs.** Hook output is shown to the agent and persisted.
- **Prefer rejection with a clear reason over silent transformation of tool arguments.** Transformation obscures causality and desynchronizes the agent from its own actions. (Deterministic formatting of a file the agent just edited is acceptable; rewriting the agent's intended arguments is not.)

## Performance

- **Keep PreToolUse hooks under 200ms and PostToolUse under 2s on the common path.** Hooks tax every agent turn.
- **Do not make network calls from PreToolUse or PostToolUse.** Network latency is unpredictable and blocks the agent. Use `SessionStart` for fetches and cache the results locally.
- **Set hard timeouts on any unavoidable external I/O and default to deny on timeout.** Low-confidence decisions should not fail permissive.
- **Short-circuit irrelevant events early — check tool name and file extension before doing real work.** A no-op hook should cost under 10ms.
- **Defer expensive checks (full typecheck, test suite, security scan) to `Stop`.** Per-edit heavy checks cause retry storms and unusable slowness.
- **Cache results by input hash or file mtime when the hook is deterministic.** Re-running a formatter on an unchanged file is waste multiplied by every turn.
- **Cache static policy data (protected tables, allowlisted domains) in memory; refresh on a timer, not per-request.** Per-call fetches dominate latency.
- **Minimize dependencies and prefer the standard library.** Fewer deps = faster cold start, smaller security surface, simpler deployment.

## Error Handling

- **Begin every bash hook with `set -euo pipefail`.** Without it, pipeline failures are silently swallowed and the hook appears to pass.
- **Catch exceptions in non-bash hooks and return a deterministic deny + structured log.** An uncaught exception breaks the agent loop.
- **Never silently swallow errors or return ambiguous results.** Silent failures are a security smell; make hook bugs loud.
- **Do not retry synchronously inside a hook.** Retries amplify latency and thundering-herd effects.
- **Distinguish policy violations from infrastructure errors in exit codes or JSON output.** Routing, alerting, and user messaging all depend on this distinction.

## Event-Specific Guidance

- **Use `PreToolUse` for policy enforcement and hardened denies only.** This is a security boundary; keep it fast and deterministic.
- **Use `PostToolUse` for deterministic, idempotent formatters (prettier, gofmt, ruff format) applied to the file just edited.** Fast, local, and agent-transparent.
- **Use `Stop` for semantic rewrites (import sorting, codemods, lint --fix), full typechecks, and test runs.** Running these per-edit confuses the agent's model of file contents.
- **Use `UserPromptSubmit` to inject project context (branch, open PR, style guide path) — not to validate the user's prompt.** Context injection is the killer use case.
- **Use `SessionStart` to warm caches, fetch remote config, and print environment summary.** It runs once; amortize expensive setup here.
- **Do not trigger state-modifying logic from `Notification` hooks.** They fire on idle/permission events and are not reliable control points.
- **Treat `Stop` as best-effort; do not rely on it for critical enforcement.** It may not fire on crashes or force-quits.

## Logging and Observability

- **Log every blocking decision as structured JSON with `timestamp`, `event`, `tool`, `rule_id`, `decision`, `reason`, and `policy_version`.** Unstructured logs can't be audited or alerted on.
- **Log to a local file (e.g., `.claude/hooks.log`) — do not log to stdout.** Stdout belongs to the protocol.
- **Make every block `reason` tell the agent exactly how to unblock.** "Forbidden" causes retry loops; "Use `rg` instead of `grep`" causes correction.
- **Redact secrets and PII from all log output.** Sanitize arguments before logging; log hashes or identifiers for sensitive fields.
- **Record the active policy version in every decision.** Enables rollback analysis and audit.

## Testing and Rollout

- **Test hooks by piping fixture JSON to the script: `cat fixtures/edit-event.json | .claude/hooks/posttooluse-format.sh`.** Unit-testable hooks are debuggable hooks.
- **Check in a `fixtures/` directory with a sample payload per event type your hooks handle.** Protects against Claude Code schema drift and enables fast local iteration.
- **Write tests covering valid input, malformed input, missing fields, boundary cases, and each explicit deny path.** Hooks are security code; treat them accordingly.
- **Roll new blocking hooks out in log-only mode (exit 0) for a week before flipping to exit 2.** Confirms the false-positive rate against real agent behavior before paying the friction cost.
- **Review `.claude/settings.json` changes with the same rigor as CI configuration.** A bad team-level hook blocks every engineer's agent until reverted.
- **Pin and verify hook dependencies (checksums or lockfiles).** Supply-chain compromise of a hook is a compromise of the agent's trust boundary.

## Hook Hygiene

- **Keep hooks stateless and idempotent.** Statelessness eliminates race conditions; idempotency makes retries and replays safe.
- **Do not modify repository files or agent memory from hooks unless that is the hook's explicit, documented purpose.** Hidden side effects erode trust and confuse the agent.
- **Do not have a hook invoke another tool or trigger another hook chain.** Risks recursion and loss of control.
- **Document the order and short-circuit behavior of any hook chain you configure.** Predictable order prevents conflicting decisions.