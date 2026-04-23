# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Decide upfront whether hooks are for *detection* (log and allow) or *prevention* (log and block).** Security-critical hooks should prevent; compliance hooks can be detective-only and allow the action while logging for audit | Observability & Audit |  |  |  | ✓ |  |  | 1 |
| **(contested) Prefer minimal, dependency-free Python over shell for non-trivial logic.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Add a comment above any non-obvious conditional.** If a hook blocks a tool only on certain days, or only for users in a specific group, explain why in a comment | Style & Clarity |  |  |  | ✓ |  |  | 1 |
| **Assume the agent is adversarial when writing security hooks.** Do not assume the agent will respect your intent or follow your logic | Safety |  |  |  | ✓ |  |  | 1 |
| **Avoid complex algorithms or heavy computation.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Avoid object serialization or JSON stringification in the critical path.** If you need to log a decision, serialize only the fields you need (hook name, decision, reason), not the entire payload | Performance |  |  |  | ✓ |  |  | 1 |
| **Block by default on ambiguity; never allow an action if the hook is unsure.** If a hook cannot parse tool arguments, or if tool metadata is missing, return block and log the anomaly | Safety |  |  |  | ✓ |  |  | 1 |
| **Cache expensive computations (e.g., resolved `.gitignore`, parsed configs) in `/tmp` or a project-local cache keyed by mtime.** Re-parsing on every invocation is waste | Performance |  |  | ✓ |  |  |  | 1 |
| **Check that required tools (`jq`, `rg`, linters) exist and exit with a clear stderr message if not.** A missing `jq` should say "install jq", not crash with "command not found" | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Commit `.claude/settings.json` for team-shared gates; keep personal hooks in `.claude/settings.local.json` and gitignore it.** Shared gates need review; personal workflow does not | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Define all configuration and allowlist data as module-level constants at the top of the file.** Use `const BLOCKED_TOOLS = [...]`, `const MAX_PAYLOAD_BYTES = ...`, etc | Structure |  |  |  | ✓ |  |  | 1 |
| **Distinguish between *block* (agent action is forbidden), *allow* (agent action is permitted), and *escalate* (agent action requires human review or external approval).** Log the decision code, not a prose description | Observability & Audit |  |  |  | ✓ |  |  | 1 |
| **Do not invoke shell commands (exec, spawn, etc.) from within a hook function.** If you need to check file system state, use Node.js file system APIs (fs module) | Safety |  |  |  | ✓ |  |  | 1 |
| **Do not log sensitive information (credentials, PII, full SQL queries on PII fields).** Log tool names, event types, and decisions | Safety |  |  |  | ✓ |  |  | 1 |
| **Do not make a hook decision depend on the full agent memory or conversation history.** If you need historical context, accept a specific, bounded input (e.g., the last tool call, the current turn count) | Performance |  |  |  | ✓ |  |  | 1 |
| **Do not make network calls from `PreToolUse` hooks on common tools.** Network latency multiplied across a session is unacceptable, and offline use becomes impossible | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not make network calls.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Do not make security or compliance decisions based on user-supplied input alone.** Security hooks must cross-reference user input against trusted lists (hardcoded allowlists, tool definitions, API-level permissions) | Safety |  |  |  | ✓ |  |  | 1 |
| **Do not perform blocking file I/O on large files.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Do not use regular expressions for parsing structured data (JSON, shell commands, SQL, etc.).** Parse tool arguments as JSON if the tool returns JSON; use a real parser (e.g., sql-parser) for SQL queries | Safety |  |  |  | ✓ |  |  | 1 |
| **Document every hook in a top-of-file comment stating: event, matcher, what it blocks/allows, and how to bypass.** Hooks are security-adjacent; undocumented hooks get disabled in frustration | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Don't run full test suites or type-checkers from `PostToolUse` on single-file edits.** Scope checks to the file that changed | Performance |  |  | ✓ |  |  |  | 1 |
| **Emit `{"decision": "block", "reason": "..."}` on stdout when you need the model to see structured feedback; otherwise prefer exit-code signaling.** JSON responses are for cases where the reason must reach the model verbatim | Protocol & I/O |  |  | ✓ |  |  |  | 1 |
| **Ensure the script has a "fail-closed" default path.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Exit with a non-zero status code to block an agent action.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Fail closed for safety-critical gates (secret scanning, destructive-command blocks); fail open for advisory gates (lint, format).** A crashed secret scanner that allows the commit is worse than a noisy one | Safety |  |  | ✓ |  |  |  | 1 |
| **Give every hook script a shebang and executable bit.** Relying on the shell to guess the interpreter is fragile across machines | Structure |  |  | ✓ |  |  |  | 1 |
| **If shelling out, use fixed commands and pass agent data as arguments.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Include a JSDoc comment block for each hook function.** Document the event type, decision logic (allow/block/escalate/log), preconditions, and any limitations or known false positives | Structure |  |  |  | ✓ |  |  | 1 |
| **Include a trace ID or request ID in logs, if available from the hook payload.** This enables correlation with agent logs and other system events | Observability & Audit |  |  |  | ✓ |  |  | 1 |
| **Include at least one test per hook that pipes a representative JSON payload to stdin and asserts exit code and stdout.** Hooks without tests rot silently | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Keep `settings.json` hook entries to a single `command:` field pointing at a script path; no inline pipelines.** Pipelines in JSON strings are unreviewable | Style |  |  | ✓ |  |  |  | 1 |
| **Keep each hook single-purpose; compose multiple hooks rather than branching inside one.** Independent hooks are independently testable and disable-able | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep hook functions under 50 lines of code.** Complex logic should be refactored into pure utility functions (above the hook definition) or moved out of the hook entirely | Performance |  |  |  | ✓ |  |  | 1 |
| **Keep hook scripts to a single file.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Keep hooks under 50 lines of code (LOC).** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Log all diagnostic and error information to `stderr`.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Log decisions and anomalies in a structured format (JSON, if possible).** Include fields: timestamp, hook name, event type, decision, reason, and any relevant input digest | Observability & Audit |  |  |  | ✓ |  |  | 1 |
| **Log every hook decision (allow, block, escalate, or inconclusive).** Include the hook name, event type, decision, and a one-line reason | Error Handling |  |  |  | ✓ |  |  | 1 |
| **Name hook functions with a prefix matching the event type.** Use `preToolUse*`, `postToolUse*`, `userPromptSubmit*`, or `stop*` as appropriate (e.g., `preToolUseSQLInjectionCheck`, not `validateToolCall`) | Structure |  |  |  | ✓ |  |  | 1 |
| **Name hook scripts by event and purpose, e.g | Structure |  |  | ✓ |  |  |  | 1 |
| **Never `exit 2` without writing a human-readable reason to stderr (or a `reason` field).** Unexplained blocks destroy trust in the hook system | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Never execute or evaluate strings received from the agent.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Never pass tool-input fields directly into `bash -c`, `eval`, `sh -c`, or equivalent.** Tool inputs are LLM-generated and may contain injected shell metacharacters | Safety |  |  | ✓ |  |  |  | 1 |
| **Never throw an unhandled exception from a hook function.** If the hook encounters an unexpected state (malformed payload, missing field), log an error and return a safe default (allow for security hooks; log for observability hooks) | Error Handling |  |  |  | ✓ |  |  | 1 |
| **Parse hook input from stdin as JSON; do not rely on positional arguments or environment for tool payloads.** The stdin JSON is the contract; argv is not | Protocol & I/O |  |  | ✓ |  |  |  | 1 |
| **Parse structured data (JSON) with a dedicated library.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Pin hook dependencies (linters, formatters) to versions via the project's existing dep manager.** Divergent versions across teammates produce phantom failures | Style |  |  | ✓ |  |  |  | 1 |
| **Place a comment block at the top of the file explaining the hook's purpose.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Prefer `rg` over `grep -r`, `jq` over `python -c 'json.load'`, and avoid spinning up interpreters for trivial checks.** Startup time dominates for short hooks | Performance |  |  | ✓ |  |  |  | 1 |
| **Quote every variable expansion (`"$var"`) in bash hooks.** Unquoted expansion is the largest single source of shell bugs | Style |  |  | ✓ |  |  |  | 1 |
| **Reserve stdout exclusively for the hook protocol (JSON or nothing).** Any stray `echo` corrupts the agent's view of the hook's decision | Protocol & I/O |  |  | ✓ |  |  |  | 1 |
| **Resolve and canonicalize paths (`realpath`) before comparing them to allowlists.** Otherwise `../../../etc/passwd` slips through a naive prefix check | Safety |  |  | ✓ |  |  |  | 1 |
| **Send all logs, debug output, and human-readable messages to stderr.** Claude Code surfaces stderr on non-zero exits and ignores it otherwise, which is what you want | Protocol & I/O |  |  | ✓ |  |  |  | 1 |
| **Set `set -euo pipefail` at the top of every bash hook.** Silent failures in hooks produce silently-broken gates | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Set a timeout for any external I/O operation; abort if the timeout is exceeded.** Use a timeout of no more than 5 seconds for a security/compliance check, 10 seconds for an observability hook | Error Handling |  |  |  | ✓ |  |  | 1 |
| **Store hook logic in versioned scripts under `.claude/hooks/`, not inline in `settings.json`.** Inline commands escape review, defeat `shellcheck`, and become unreadable past one line | Structure |  |  | ✓ |  |  |  | 1 |
| **Target under 100 ms for hooks that match on every tool call; under 1 s for narrow matchers.** Hooks are synchronous and compound across a session | Performance |  |  | ✓ |  |  |  | 1 |
| **Test hooks with realistic tool arguments and payloads.** If a hook that claims to run in < 1ms takes 50ms in production, there is likely a hidden loop or I/O | Performance |  |  |  | ✓ |  |  | 1 |
| **Trap and log unexpected errors to a known file (e.g., `.claude/hooks/hook.log`) before exiting.** Debugging a hook that "sometimes blocks" is impossible without logs | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Treat `UserPromptSubmit` injected context as untrusted when it originates from fetched content.** Prompt injection via injected context is a real attack surface | Safety |  |  | ✓ |  |  |  | 1 |
| **Treat all input from the agent event payload as untrusted.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Use a standard linter and formatter for the chosen language.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Use camelCase for function and variable names; use UPPER_SNAKE_CASE for constants.** This makes configuration data visually distinct from logic | Style & Clarity |  |  |  | ✓ |  |  | 1 |
| **Use constant-time or O(log n) data structures for lookups.** Define blocked tools, allowed patterns, etc., as Sets or Maps, not arrays | Performance |  |  |  | ✓ |  |  | 1 |
| **Use early returns to flatten control flow.** Instead of `if (condition) { | Style & Clarity |  |  |  | ✓ |  |  | 1 |
| **Use exit code `2` to block with feedback, `0` to allow, and non-zero-non-2 only for hook bugs.** Mixing these up either silently allows unsafe actions or spams the user with "hook failed" noise | Protocol & I/O |  |  | ✓ |  |  |  | 1 |
| **Use explicit control flow (if/else, switch, early returns).** Avoid nested ternary operators, reduce/filter chains, or boolean algebra that requires mental parsing | Structure |  |  |  | ✓ |  |  | 1 |
| **Use narrow `matcher` patterns, not `.*` or empty matchers, unless the hook truly applies to every tool.** Broad matchers add latency to every tool call | Structure |  |  | ✓ |  |  |  | 1 |
| **Validate file paths against an allowlist of project-relative prefixes before acting on them.** A hook that trusts `$file_path` will happily `rm` `/etc/passwd` when the model hallucinates | Safety |  |  | ✓ |  |  |  | 1 |
| **Wrap all external I/O (API calls, file system reads, subprocess invocations) in try-catch blocks with explicit error handling.** Log the error with context (hook name, input, exception message), then return a safe default (e.g., log and allow, never silently block) | Error Handling |  |  |  | ✓ |  |  | 1 |
| **Write bash for hooks under ~20 lines; switch to Python or Node beyond that.** Bash branching and data-structure handling degrades fast | Style |  |  | ✓ |  |  |  | 1 |
| **Write clear, specific variable names.** Use `blockedToolNames`, not `blocked` | Style & Clarity |  |  |  | ✓ |  |  | 1 |
| **Write each hook as a single, self-contained JavaScript function exported as a named export.** Each hook event (PreToolUse, PostToolUse, UserPromptSubmit, Stop) should have its own clearly-named function with a signature matching the documented hook payload schema | Structure |  |  |  | ✓ |  |  | 1 |
| Add an integration test that loads settings.json and executes each registered hook with sample payloads | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers and AI coding assistants authoring, reviewing, and operating hook scripts to enforce quality gates, block unsafe actions, and instrument behavior | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid network I/O in PreToolUse; if unavoidable, cache results within-session | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Bound and capture subprocess stdout/stderr; treat truncated output as nonfatal with a safe decision | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cap input/output size processed by hooks (e.g., 1 MB) and skip with observe if exceeded | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare a shebang and make scripts executable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Disallow outbound network access in PreToolUse | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do enforce type checks where applicable (contested) | Safety |  | ✓ |  |  |  |  | 1 |
| Do follow a consistent coding style throughout hooks | Style |  | ✓ |  |  |  |  | 1 |
| Do include error handling logic | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do keep hooks small and focused | Structure |  | ✓ |  |  |  |  | 1 |
| Do not download or generate hook scripts at runtime; check them into source control | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not register a hook you do not need | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not write logs to stdout; write all human-readable logs to stderr | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do profile hooks to monitor their execution time | Performance |  | ✓ |  |  |  |  | 1 |
| Do validate user input explicitly | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t allow execution of untrusted code | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t ignore exceptions | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t introduce complex logic that may degrade performance | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t use global variables within hooks | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t use magic numbers or hard-coded strings | Style |  | ✓ |  |  |  |  | 1 |
| Emit one structured JSON log line to stderr per invocation with hook, event, requestId, decision, durationMs, version, and sha | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce a per-hook timeout (default 2s, max 5s) and abort on timeout with a clear decision | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce formatting and linting (black, ruff for Python; shellcheck for Bash) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce linters in CI (ruff, black --check, shellcheck) and fail the build on violations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Exit 0 on protocol success (allow/deny/modify/observe) and non-zero only for internal hook errors | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fail closed on parse, validation, or internal errors in PreToolUse | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Forbid dangerous patterns: rm -rf, curl\|sh, sudo, dd to block devices, and unquoted variable expansion in shells | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In Bash, set: set -euo pipefail; IFS=$'\n\t' | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In Python, use sys.stdin.read(), json.loads, and explicit sys.exit codes in an if __name__ == "__main__" guard | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In settings.json, declare hooks only under the hooks key with the standard event names | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep PreToolUse p95 under 2s and typical checks under 50ms | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep hook files under 200 LOC and functions under 50 LOC | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep hooks stateless and idempotent | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Maintain an explicit allowlist of tools and subcommands; deny by default | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make decisions deterministic given inputs; do not use randomness without a fixed seed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make each hook a single small entrypoint; compose multiple hooks by registering multiple scripts, not by branching internally | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never construct shells from untrusted strings; pass argv arrays to subprocess without shell=True | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Normalize and validate all filesystem paths via realpath and enforce a workspace root prefix; reject symlinks escaping the workspace | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin Python dependencies in requirements.txt or a lockfile; vendor single-file utilities when feasible | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin interpreter/binary paths explicitly (e.g., /usr/bin/python3, /usr/bin/env bash) and avoid bare names | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer ./relative paths rooted at the repo for scripts; do not rely on changing CWD at runtime | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer Python for nontrivial hooks; use Bash only for trivial glue | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer sandboxed execution (container, seccomp, or no_new_privs) for high-risk hooks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Produce exactly one JSON object on stdout containing decision, reason, and optionally patch or metadata | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide fixtures under tests/fixtures/{Event}/ covering allow, deny, and malformed cases | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put all hook scripts under hooks/ with filenames {Event}__{purpose}.{sh\|py} | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Read the hook payload from stdin as strict JSON; reject on parse error | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Redact or drop secrets from logs and outputs; never print env dumps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Register only supported events: PreToolUse, PostToolUse, UserPromptSubmit, Stop | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Retry only idempotent, transient operations with capped exponential backoff (max 2 retries) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return stable reason codes from a fixed enum; avoid free-text only | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run hooks with least privilege and without sudo | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Sample heavy PostToolUse instrumentation to ≤10% unless mandated by compliance | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Opinionated best practices for Claude Code Agentic Hooks configured under the hooks: key in settings.json for events PreToolUse, PostToolUse, UserPromptSubmit, and Stop | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Spawn at most one subprocess per hook invocation; batch checks when needed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Tag logs with a stable hook name matching the filename | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Unit test each hook’s stdin→stdout/exit behavior; assert no stdout noise and correct exit codes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use absolute or ./-prefixed command paths in settings.json; never rely on PATH | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use argv-array command form when supported by the platform; avoid shell-string commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use comments to document each allow/deny rule with rationale and examples | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use monotonic timing for duration; include timeout flag when applicable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate required fields (at least event, requestId, timestamp) and normalize inputs before use | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

