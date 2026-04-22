# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Avoid transforming arguments; prefer to reject and let the user refine.** | Transformation (Rare) |  |  |  | ✓ |  |  | 1 |
| **(contested) Do log the user and prompt context if available.** | Logging and Auditability |  |  |  | ✓ |  |  | 1 |
| **(contested) Prefer Python 3 for new hooks.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Add a comment block at the top of the file explaining the hook's purpose, inputs, and outputs.** | Style and Maintainability |  |  |  |  | ✓ |  | 1 |
| **Avoid dependencies on external packages or libraries.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Avoid heavy file I/O or calls to slow external processes.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Begin every bash hook with `set -euo pipefail`.** Without it, failures are silently swallowed and the hook appears to pass | Structure |  |  | ✓ |  |  |  | 1 |
| **Cache results by input hash or file mtime when the hook is deterministic.** Re-running prettier on an unchanged file is waste multiplied by every turn | Performance |  |  | ✓ |  |  |  | 1 |
| **Check in a `fixtures/` directory with a sample payload per event type your hooks handle.** Schema drift from Anthropic will break you; fixtures catch it immediately | Testing and Rollout |  |  | ✓ |  |  |  | 1 |
| **Design hooks to be stateless.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Do assume the hook has no special privileges; if you need elevated permissions, request them explicitly and document why.** | Safety and Permissions |  |  |  | ✓ |  |  | 1 |
| **Do avoid loops, recursion, or quadratic algorithms.** | Performance |  |  |  | ✓ |  |  | 1 |
| **Do cache static policy data (e.g., list of protected tables) in memory; refresh it on a timer, not per-request.** | Performance |  |  |  | ✓ |  |  | 1 |
| **Do catch exceptions in your hook; log and return a deny decision.** | Error Handling and Resilience |  |  |  | ✓ |  |  | 1 |
| **Do check argument types (string, number, array, object).** | Argument Validation |  |  |  | ✓ |  |  | 1 |
| **Do document the reasoning behind every deny decision in the log.** | Decision Logic |  |  |  | ✓ |  |  | 1 |
| **Do fail closed: if the request is malformed, ambiguous, or risky and you can't clearly allow it, deny it.** | Decision Logic |  |  |  | ✓ |  |  | 1 |
| **Do include a docstring at the top of each hook with purpose, trigger events, and key assumptions.** | Structure |  |  |  | ✓ |  |  | 1 |
| **Do include fixtures with realistic tool calls and arguments.** | Testing |  |  |  | ✓ |  |  | 1 |
| **Do include the full request context in logs: tool name, arguments, and the specific policy rule that fired.** | Logging and Auditability |  |  |  | ✓ |  |  | 1 |
| **Do isolate external calls: if a hook calls a webhook, use a separate, low-privilege endpoint and timeout aggressively.** | Safety and Permissions |  |  |  | ✓ |  |  | 1 |
| **Do keep hook code under 100 lines.** | Structure |  |  |  | ✓ |  |  | 1 |
| **Do keep hook execution under 100ms for common paths.** | Performance |  |  |  | ✓ |  |  | 1 |
| **Do log all transformations with the original and transformed arguments.** | Transformation (Rare) |  |  |  | ✓ |  |  | 1 |
| **Do log every decision: allow, deny, transform.** | Logging and Auditability |  |  |  | ✓ |  |  | 1 |
| **Do log the decision immediately in the hook; don't rely on downstream systems to log it.** | Logging and Auditability |  |  |  | ✓ |  |  | 1 |
| **Do make decisions based on observable facts: tool name, arguments, resource identifiers.** | Decision Logic |  |  |  | ✓ |  |  | 1 |
| **Do name hooks with a clear prefix and intent: `block_`, `log_`, `transform_`.** | Structure |  |  |  | ✓ |  |  | 1 |
| **Do not invoke the network from PreToolUse or PostToolUse.** Network latency is non-deterministic and blocks the agent; use `SessionStart` for fetches | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not make network calls in a hook script.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Do not read secrets from the environment inside hooks that echo to stdout/stderr.** Hook output is shown to the agent and logged | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not use `Notification` hooks to trigger anything that modifies state.** They fire on idle/permission events and are not reliable control points | Specific Event Guidance |  |  | ✓ |  |  |  | 1 |
| **Do not write to `stdout` if the script will exit with a non-zero code.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Do rotate credentials and API keys used by hooks; audit their usage.** | Safety and Permissions |  |  |  | ✓ |  |  | 1 |
| **Do separate policy logic from plumbing.** | Structure |  |  |  | ✓ |  |  | 1 |
| **Do set timeouts on any external I/O (HTTP, database); default to deny if timeout is exceeded.** | Error Handling and Resilience |  |  |  | ✓ |  |  | 1 |
| **Do test error cases: malformed JSON, missing fields, external service timeouts.** | Testing |  |  |  | ✓ |  |  | 1 |
| **Do use a schema validation library (e.g., `zod`, `joi`) for complex arguments; write simple `if` checks for simple cases.** | Argument Validation |  |  |  | ✓ |  |  | 1 |
| **Do use allowlists, not blocklists, wherever possible.** | Decision Logic |  |  |  | ✓ |  |  | 1 |
| **Do use structured logging: log as JSON with fields like `timestamp`, `hook_name`, `event_type`, `tool_name`, `decision`, `reason`.** | Error Handling and Resilience |  |  |  | ✓ |  |  | 1 |
| **Do validate all argument fields before using them; fail closed if validation fails.** | Argument Validation |  |  |  | ✓ |  |  | 1 |
| **Do write each hook as a single, focused policy.** | Structure |  |  |  | ✓ |  |  | 1 |
| **Do write test cases for every hook covering: valid requests, invalid arguments, boundary cases, and the specific deny cases.** | Testing |  |  |  | ✓ |  |  | 1 |
| **Document each hook's event, matcher, exit contract, and expected latency in a header comment.** Future-you reading `settings.json` will not remember | Style |  |  | ✓ |  |  |  | 1 |
| **Don't allow hooks to modify their own code or configuration.** | Safety and Permissions |  |  |  | ✓ |  |  | 1 |
| **Don't call external APIs in a tight loop.** | Performance |  |  |  | ✓ |  |  | 1 |
| **Don't log sensitive data (passwords, API keys, PII) even in deny cases.** | Logging and Auditability |  |  |  | ✓ |  |  | 1 |
| **Don't make decisions based on external state you can't verify synchronously.** | Decision Logic |  |  |  | ✓ |  |  | 1 |
| **Don't silently swallow errors or return an ambiguous result.** | Error Handling and Resilience |  |  |  | ✓ |  |  | 1 |
| **Don't use optional chaining (`?.`) as your only defense against missing fields.** | Argument Validation |  |  |  | ✓ |  |  | 1 |
| **Emit a single structured line on block, not a wall of text.** The agent reads every byte; verbosity dilutes the signal | Style |  |  | ✓ |  |  |  | 1 |
| **Ensure hooks are idempotent.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Exit 0 for allow/success, exit 2 to block and feed stderr back to the agent, other non-zero only for hook bugs.** This is the contract; ignoring it breaks agent feedback loops | Exit Codes and Output |  |  | ✓ |  |  |  | 1 |
| **Exit silently on success — do not print "✅ hook passed".** Noise on every turn trains users to ignore hook output | Style |  |  | ✓ |  |  |  | 1 |
| **Give the hook script a descriptive name that reflects its purpose (e.g., `block-force-push.py`).** | Style and Maintainability |  |  |  |  | ✓ |  | 1 |
| **If you transform, do so only for spec-defined, reversible changes.** | Transformation (Rare) |  |  |  | ✓ |  |  | 1 |
| **Keep PreToolUse hooks under 200ms and PostToolUse under 2s on the common path.** Hooks are synchronous; they tax every agent turn | Performance |  |  | ✓ |  |  |  | 1 |
| **Keep each hook implementation in a single, self-contained script file.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Keep the logic within a hook simple and focused on a single responsibility.** | Style and Maintainability |  |  |  |  | ✓ |  | 1 |
| **Log every blocking decision to `.claude/hooks.log` with timestamp, event, tool, and reason.** You will need this to debug why the agent is stuck | Safety |  |  | ✓ |  |  |  | 1 |
| **Make every block `reason` tell the agent exactly what to do to unblock.** "Forbidden" causes retry loops; "Use `rg` instead of `grep`" causes correction | Exit Codes and Output |  |  | ✓ |  |  |  | 1 |
| **Make hook scripts executable and start them with `#!/usr/bin/env bash` (or `python3`, `node`).** Relying on the parent shell's interpreter is non-portable | Structure |  |  | ✓ |  |  |  | 1 |
| **Name hook scripts by event and purpose: `pretooluse-bash-guard.sh`, `posttooluse-format.sh`, `stop-run-tests.sh`.** Matches the mental model engineers bring to `.claude/settings.json` | Style |  |  | ✓ |  |  |  | 1 |
| **Never `eval`, `bash -c`, or `sh -c` any field from the hook's stdin JSON.** Tool inputs can contain attacker-controlled strings from files, issues, or web content | Safety |  |  | ✓ |  |  |  | 1 |
| **Never execute or evaluate strings from the input payload directly.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Never use `"decision": "approve"` in PreToolUse to auto-approve tool calls the user would normally confirm.** (contested) It bypasses the permission prompt and trains users to trust unseen actions | Exit Codes and Output |  |  | ✓ |  |  |  | 1 |
| **One hook script per concern.** Compose multiple focused hooks rather than one mega-script with internal dispatch | Structure |  |  | ✓ |  |  |  | 1 |
| **Parse stdin JSON with `jq` or a real parser — never interpolate it into a shell command.** Tool input is attacker-controlled via agent-ingested content; string interpolation is RCE | Structure |  |  | ✓ |  |  |  | 1 |
| **Prefer structured JSON output (`{"decision": "block", "reason": "..."}`) over exit-code signaling for anything beyond a binary gate.** JSON gives you `reason`, `suppressOutput`, and `hookSpecificOutput`; exit codes don't | Exit Codes and Output |  |  | ✓ |  |  |  | 1 |
| **Put hook logic in a script file, not inline in JSON.** The `command` field should be `.claude/hooks/<name>.sh` or similar; JSON-escaped shell is unreviewable | Structure |  |  | ✓ |  |  |  | 1 |
| **Review `.claude/settings.json` hook changes with the same rigor as CI config changes.** A bad hook blocks every engineer's agent until reverted | Testing and Rollout |  |  | ✓ |  |  |  | 1 |
| **Roll new blocking hooks out as non-blocking (exit 0, log only) for one week before flipping to exit 2.** Confirms false-positive rate against real agent behavior before you pay the friction cost | Testing and Rollout |  |  | ✓ |  |  |  | 1 |
| **Run expensive checks (full typecheck, test suite, security scan) in `Stop`, not `PostToolUse`.** Per-edit heavy checks make the agent unusably slow and trigger retry storms | Performance |  |  | ✓ |  |  |  | 1 |
| **Sanitize all data from the agent payload before including it in logging or error messages.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Scope destructive hooks (git commits, network calls, file deletion) to `.claude/settings.local.json`, not team settings.** Team-shared destructive automation is how repos get corrupted at scale | Safety |  |  | ✓ |  |  |  | 1 |
| **Short-circuit hooks early when the event is irrelevant — check the tool name and file extension before doing any work.** A no-op hook should cost <10ms | Performance |  |  | ✓ |  |  |  | 1 |
| **Store all hook scripts under `.claude/hooks/` in the repo.** Colocates behavior with code and makes hooks versioned and reviewable | Structure |  |  | ✓ |  |  |  | 1 |
| **Target a total execution time under 100 milliseconds.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Test hooks by piping fixture JSON to the script: `cat fixtures/edit-event.json \| .claude/hooks/posttooluse-format.sh`.** Unit-testable hooks are debuggable hooks | Testing and Rollout |  |  | ✓ |  |  |  | 1 |
| **Treat PreToolUse on `Bash` as a security boundary: maintain an explicit deny-list for `rm -rf`, `curl \| sh`, credential exfiltration patterns, and force-push.** The default permission system is not a substitute for hardened block rules | Safety |  |  | ✓ |  |  |  | 1 |
| **Use `PostToolUse` for deterministic formatters (prettier, gofmt, ruff format) on the edited file only.** Fast, local, idempotent — the ideal PostToolUse workload | Specific Event Guidance |  |  | ✓ |  |  |  | 1 |
| **Use `SessionStart` to warm caches, print environment summary, and surface recent CI failures.** It runs once; amortize expensive setup here | Specific Event Guidance |  |  | ✓ |  |  |  | 1 |
| **Use `Stop` for semantic rewrites (import sorting, codemods, lint --fix).** (contested) Running these per-edit confuses the agent's mental model of file contents | Specific Event Guidance |  |  | ✓ |  |  |  | 1 |
| **Use `UserPromptSubmit` to inject project context (current branch, open PR, style guide path), not to validate the prompt.** Prompt validation belongs in the user's head; context injection is the killer use case | Specific Event Guidance |  |  | ✓ |  |  |  | 1 |
| **Use a non-zero exit code to signal a failure or to block an agent action.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Use exit code 0 to signal success and allow the agent to proceed.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Use hooks to explicitly block known dangerous patterns (e.g., `rm -rf`, credential exposure).** | Safety |  |  |  |  | ✓ |  | 1 |
| **Validate file paths against `$CLAUDE_PROJECT_DIR` before acting on them.** Prevents hooks from touching files outside the workspace when the agent is tricked | Safety |  |  | ✓ |  |  |  | 1 |
| **Validate the structure of the JSON input from `stdin` at the beginning of the script.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Write agent-facing messages to stderr when exiting 2; write user-facing status to stdout.** The channels have different audiences | Exit Codes and Output |  |  | ✓ |  |  |  | 1 |
| **Write all logging, debugging, and diagnostic output to `stderr`.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Write hooks in bash for <30 lines of logic, Python/Node for anything longer.** Bash past 30 lines becomes a maintenance liability | Style |  |  | ✓ |  |  |  | 1 |
| **Write matchers as exact tool names (`"Bash"`, `"Edit"`, `"Write"`, `"MultiEdit"`), not regex wildcards.** Broad matchers run on events you didn't intend and slow every turn | Structure |  |  | ✓ |  |  |  | 1 |
| Assign stable rule IDs and reference them in code comments and outputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Assumptions: Arguments are valid JSON; table name is in args.table | Structure |  |  |  | ✓ |  |  | 1 |
| Audience: Engineers and AI coding assistants implementing policy, safety, and telemetry in hooks that gate or instrument agent behavior | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid complex shell one-liners; use a real language for non-trivial logic | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid network calls in PreToolUse; if unavoidable, use sub-100ms budgets with circuit breaking | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Batch and defer non-critical telemetry to Stop | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Block network access to localhost, metadata endpoints, and RFC1918 by default unless explicitly allowed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cache compiled regexes and detectors across invocations when runtime allows | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Centralize shared policy data (allowlists, regexes, domains) in versioned config | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default-deny destructive or high-risk tools in PreToolUse (e.g., shell_exec, file_delete, package_install, unrestricted network) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default-deny high-risk tools and private-network egress | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Deny shell arguments that match known-destructive patterns (e.g., rm -rf, mkfs, dd to raw devices, chmod -R 777) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do adhere to a consistent naming convention for hooks and associated functions | Style |  | ✓ |  |  |  |  | 1 |
| Do implement robust error handling for all hooks | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do implement unit tests for each hook to catch edge cases early | Common Failure Modes |  | ✓ |  |  |  |  | 1 |
| Do keep hook functions small and focused | Structure |  | ✓ |  |  |  |  | 1 |
| Do log significant actions taken by hooks for audit purposes | Safety |  | ✓ |  |  |  |  | 1 |
| Do not call LLMs from hooks except sampled and asynchronous in PostToolUse/Stop | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not fetch remote policy/config without signature verification and pinning | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not retry synchronously inside hooks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not trigger tools from hooks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do profile hook execution to identify bottlenecks and optimize as necessary | Performance |  | ✓ |  |  |  |  | 1 |
| Do validate input parameters vigorously before processing | Safety |  | ✓ |  |  |  |  | 1 |
| Document and enforce a deterministic hook order with short-circuiting on terminal decisions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document supported environment variables, exit codes, and the I/O contract in a README adjacent to hooks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t allow hooks to execute actions that may lead to unsafe outcomes without explicit user confirmation | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t ignore the potential for environment-specific issues that may affect hook behavior | Common Failure Modes |  | ✓ |  |  |  |  | 1 |
| Don’t include magic numbers or arbitrary constants in your code | Style |  | ✓ |  |  |  |  | 1 |
| Don’t nest too many levels of hooks within each other | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t perform blocking operations in hooks that could degrade user experience | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t use silent failures that provide no feedback to the user or developer | Error Handling |  | ✓ |  |  |  |  | 1 |
| Emit exactly one structured response per invocation as specified by the platform | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Emit metrics for decisions, denials by rule, and durations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce hard timeouts for all hooks and cap PreToolUse at 200ms default, 2s maximum | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce tight PreToolUse time budgets (200ms default) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fail closed on PreToolUse errors/timeouts and fail open on PostToolUse/Stop errors | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Guard all external calls with timeouts and circuit breakers | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a short justification or diff snippet when blocking code or shell actions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a stable reason_code and human message in every deny/modify decision | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep each hook focused on one concern | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep hooks stateless and idempotent | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep rules declarative and data-driven; treat code as an engine over policy data | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Link to policy docs and rule IDs in user-facing messages | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Log structured JSON with correlation IDs (session_id, tool_name, rule_id, decision, policy_version) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make decisions purely from input + configuration and keep side-effects separate | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Minimize dependencies and load lazily | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name hooks by event and intent (e.g., pretool_allowlist, posttool_redact) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Neutralize prompt instructions that attempt to disable safeguards or exfiltrate tokens | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never modify repository files or agent memory from hooks unless it is the explicit, documented purpose | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Order hooks explicitly and document the chain | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin and verify dependencies with checksums or lockfiles | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer allowlists over blocklists for high-risk actions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer fail-closed for PreToolUse and fail-open for PostToolUse/Stop | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a controlled fail-open kill switch guarded by access controls and logging | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide clear remediation steps in deny messages | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Purpose: Block SQL mutations to production tables | Structure |  |  |  | ✓ |  |  | 1 |
| Rationale: Avoids race conditions, side effects, and reliance on external systems that make behavior unpredictable | Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: Complex business logic should reside in dedicated, testable services, not in a synchronous, blocking script | Style and Maintainability |  |  |  |  | ✓ |  | 1 |
| Rationale: Disk and process overhead introduce unacceptable delays into the agent's synchronous execution path | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Ensures a responsive and fluid user experience by minimizing the delay in the agent's action loop | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Guarantees that running the same hook on the same input multiple times produces the exact same result | Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: Improves discoverability and immediate understanding of the hook's function within the project | Style and Maintainability |  |  |  |  | ✓ |  | 1 |
| Rationale: Indicates a successful pass of the quality gate or instrumentation step | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: Minimizes script startup time, reduces the security surface area, and dramatically simplifies deployment | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Network latency is unpredictable and will severely degrade the agent's responsiveness for the user | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Offers an ideal balance of readability, a rich standard library, and widespread familiarity for most teams | Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents arbitrary code execution vulnerabilities introduced by malicious or malformed tool inputs | Safety |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents log injection attacks and the accidental exfiltration of sensitive information into log files | Safety |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents processing errors on unexpected or malformed agent event data, ensuring the hook fails gracefully | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: Provides essential context for future maintainers and AI assistants who need to understand or modify the script | Style and Maintainability |  |  |  |  | ✓ |  | 1 |
| Rationale: Simplifies configuration, deployment, and understanding of the hook's scope | Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: The agent runner ignores `stdout` on failure, so writing to it is pointless and can be misleading during debugging | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: This is a primary use case for hooks, serving as a critical safety layer for the agent | Safety |  |  |  |  | ✓ |  | 1 |
| Rationale: This is the primary contract for signaling to the agent runner that the current action should be halted | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: `stdout` is exclusively reserved for the JSON response payload to the agent; any other text will break the contract | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| Read the event payload only from the official input channel and write only machine-readable output to the official output channel | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Record the active policy version in every decision | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Redact secrets in logs and outputs by default with targeted allowlisting for diagnostics | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require an allowlist for external domains/APIs with purpose tags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require code owners and reviews for policy changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require explicit user confirmation for escalated actions (e.g., deleting directories, force pushes) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Restrict file operations to the workspace and require realpath canonicalization | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Restrict telemetry egress to allowlisted domains and TLS pin where feasible | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return exit 0 to allow and a non-zero exit to block unless the platform specifies otherwise | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return user-actionable messages on deny and hide internal details | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Roll out with canaries and monitor deny/error rates; auto-rollback on regressions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run hooks in CI against recorded real-world traces | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run hooks with least-privilege OS users and sandboxing where available | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Sample heavy telemetry (1–5%) and make the rate configurable via environment | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scan user prompts and tool args for secrets/PII and redact or block on match | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Operational rules for writing, reviewing, and running Claude Code Agentic Hooks configured under the hooks: key for events PreToolUse, PostToolUse, UserPromptSubmit, and Stop | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Share read-only policy state; avoid shared mutable state across hooks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ship a local test harness with fixtures for each event type | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Short-circuit cheap, high-signal checks first | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Standardize on one implementation language and a shared helper library | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Standardize on one language/runtime for hooks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Track and alert on hook latency percentiles by event type | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Treat Stop as best-effort and design telemetry to tolerate missing finalization | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Triggers: PreToolUse on tool_name="sql_query" | Structure |  |  |  | ✓ |  |  | 1 |
| Unit-test each rule with good/bad/golden cases | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use distinct exit codes for policy_violation vs infrastructure_error | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate and normalize the event payload before making decisions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Verify hook artifacts at startup (signatures/checksums) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Version policy configs and hook code; bump versions on any behavioral change | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write human-readable logs to stderr or a separate sink, never to stdout | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

