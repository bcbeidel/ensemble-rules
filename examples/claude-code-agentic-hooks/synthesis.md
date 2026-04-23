# Synthesis of Claude Code Agentic Hooks Best Practices

## 1. Consensus Rules

### Structure & Organization

- **Store hook logic in versioned script files, not inline commands in settings.json.** Inline pipelines escape review and linting. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Keep each hook single-purpose; compose multiple hooks rather than branching inside one.** Independent hooks are independently testable and auditable. *(substantively similar across GPT-5, Claude Opus, Gemini, Grok, GPT-4o-mini)*
- **Give every hook script a shebang and executable bit.** Prevents interpreter ambiguity across machines. *(near-identical wording across GPT-5 and Claude Opus)*
- **Name hook scripts by event and purpose (e.g., `pre-tool-use--block-rm.sh`).** Directory listings should read like a contract. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Keep hook files short (under ~50–200 LOC; functions under ~50 LOC).** Forces simplicity and focused responsibility. *(substantively similar across GPT-5, Claude Haiku, Gemini, Grok)*

### Protocol & I/O Contracts

- **Reserve stdout exclusively for the hook protocol (JSON or nothing); send all logs to stderr.** Stray output corrupts the agent's view of decisions. *(near-identical wording across GPT-5 and Claude Opus; also present in Gemini)*
- **Parse hook input from stdin as strict JSON; validate before using.** The stdin JSON is the contract; reject on parse error. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Use exit codes deterministically (0 = allow, 2 = block with feedback, other non-zero = hook bug).** Mixing these silently allows unsafe actions or creates noise. *(near-identical wording across GPT-5 and Claude Opus)*
- **Parse structured data with dedicated libraries (`jq`, `json.loads`), never regex.** Regex is fragile and bypassable via quoting/escaping. *(substantively similar across Claude Opus, Claude Haiku, Gemini)*

### Safety

- **Never pass tool-input fields directly into `eval`, `bash -c`, `sh -c`, `shell=True`, or `os.system`.** Tool inputs are LLM-generated and may contain injected metacharacters. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Validate and canonicalize filesystem paths (via `realpath`) against a workspace/allowlist prefix.** Prevents path traversal via `../` or symlinks. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Treat all agent/tool input as untrusted and validate explicitly.** The agent may generate malformed, unexpected, or adversarially-injected data. *(substantively similar across all six models)*
- **Fail closed for safety-critical gates; fail open for advisory/observability hooks.** A crashed secret scanner that allows commits is worse than a noisy one. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Redact secrets and never dump environment variables to logs.** Minimizes leakage via log aggregation. *(substantively similar across GPT-5 and Claude Haiku)*

### Error Handling

- **Set `set -euo pipefail` at the top of every bash hook.** Silent failures produce silently-broken gates. *(near-identical wording across GPT-5 and Claude Opus)*
- **Wrap external I/O in try/catch (or equivalent) with explicit error handling; never swallow exceptions silently.** Silent catches make hooks un-debuggable. *(substantively similar across Claude Haiku, Grok, GPT-4o-mini)*
- **Enforce a per-hook timeout (≤ 2–5 seconds) and abort cleanly on expiry.** Preserves agent responsiveness. *(substantively similar across GPT-5, Claude Haiku)*
- **Write a human-readable reason to stderr before any blocking exit.** Unexplained blocks destroy trust in the hook system. *(substantively similar across GPT-5 and Claude Opus)*

### Performance

- **Keep PreToolUse hooks fast (target sub-100ms for broad matchers, sub-1s overall).** Hooks are synchronous and compound across sessions. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Avoid network I/O in PreToolUse hooks.** Network latency makes agents feel sluggish and breaks offline use. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Use narrow `matcher` patterns rather than `.*` or empty matchers.** Broad matchers add latency to every tool call. *(raised by Claude Opus; aligns with performance rules in GPT-5)*

### Style

- **Quote every variable expansion in bash (`"$var"`).** Unquoted expansion is the single largest source of shell bugs. *(near-identical wording across GPT-5 and Claude Opus)*
- **Enforce linters/formatters in CI (shellcheck, ruff/black for Python).** Sustains readability and catches common bugs early. *(substantively similar across GPT-5, Claude Opus, Gemini)*
- **Prefer Python over bash once logic exceeds ~20 lines or handles structured data.** Bash branching and data handling degrades fast. *(substantively similar across GPT-5, Claude Opus, Gemini)* (contested — see §3)

### Observability

- **Emit one structured log line per invocation to stderr, with hook name, event, decision, reason, and duration.** Enables correlation, audits, and alerting. *(substantively similar across GPT-5, Claude Haiku)*
- **Use a fixed enum of decision values (allow / block / escalate / observe).** Enables metrics and prevents ambiguous prose decisions. *(substantively similar across GPT-5, Claude Haiku)*

### Testing

- **Include at least one test per hook that pipes a representative JSON payload to stdin and asserts exit code and stdout.** Hooks without tests rot silently. *(raised substantively by GPT-5 and Claude Opus)*

---

## 2. Strong Minority Rules

- **Commit `.claude/settings.json` for team-shared gates; keep personal hooks in `.claude/settings.local.json` and gitignore it.** *(Claude Opus only.)* Well-reasoned: the distinction between shared policy and personal workflow is real, and gitignoring personal settings prevents accidental imposition of one engineer's workflow on the team.
- **Document every hook in a top-of-file comment stating: event, matcher, effect, bypass.** *(Claude Opus; echoed weakly by Claude Haiku's JSDoc rule.)* Kept because security-adjacent code needs reviewable intent; bypass instructions are especially valuable in incident response.
- **Pin interpreter paths explicitly (e.g., `/usr/bin/env bash`) and use absolute or `./`-prefixed paths; never rely on `$PATH`.** *(GPT-5 only.)* Kept because PATH-based resolution is a real injection and portability risk.
- **Do not download or generate hook scripts at runtime; check them into source control.** *(GPT-5 only.)* Kept because it closes a supply-chain attack vector that the other models implicitly assume closed.
- **Cache expensive computations (parsed configs, resolved `.gitignore`) in `/tmp` or a project-local cache keyed by mtime.** *(Claude Opus only.)* Concrete, actionable performance guidance with a clear pattern.
- **Check that required tools (`jq`, `rg`, linters) exist and exit with a clear stderr message if missing.** *(Claude Opus only.)* Prevents cryptic "command not found" failures on teammate machines.
- **Don't run full test suites or type-checkers from PostToolUse on single-file edits; scope to the changed file.** *(Claude Opus only.)* Specific, enforceable latency guardrail.
- **Use monotonic timing (`time.perf_counter` / `time.monotonic`) for duration measurement.** *(GPT-5 only.)* Small but real correctness win for observability.

---

## 3. Divergences

**Bash vs. Python threshold.**
- GPT-5: "Prefer Python for nontrivial hooks; Bash only for trivial glue."
- Claude Opus: "Bash up to ~20 lines, switch beyond that."
- Gemini: "Favor Python once logic involves parsing structured data or more than a few branches."
- Grok, GPT-4o-mini: silent.
- **Synthesis:** Use the ~20-line threshold as a concrete heuristic, but make structured-data parsing (JSON, SQL, shell command parsing) the hard trigger for switching to a real language regardless of line count. This operationalizes the principle across all three positions.

**Fail-open vs. fail-closed on internal hook errors.**
- GPT-5, Claude Haiku, Gemini: fail closed by default (security posture).
- Claude Opus: bifurcated — fail closed for safety-critical gates, fail open for advisory ones.
- **Synthesis:** Adopt Claude Opus's bifurcated rule. A hung lint-on-save hook shouldn't block productive work; a hung secret scanner must. Require every hook to declare its failure mode explicitly in its header comment.

**Whether to block the agent at all vs. merely warn.**
- Claude Opus notes this as contested and comes down on "blocking is the whole point for safety gates."
- No model seriously advocates for warn-only.
- **Synthesis:** Blocking is appropriate for safety-critical gates; advisory hooks should use exit 0 with stderr messages. Align with Claude Opus.

**Where decisions are expressed: exit codes vs. structured JSON on stdout.**
- Claude Opus: "prefer exit-code signaling; use JSON only when the reason must reach the model verbatim."
- GPT-5: "Produce exactly one JSON object on stdout containing decision, reason."
- **Synthesis:** Prefer exit codes for simple allow/block; use JSON only when feeding structured feedback to the model. This matches the actual Claude Code hook protocol more closely than GPT-5's always-JSON rule.

**Network access in hooks (beyond PreToolUse).**
- GPT-5: flagged contested; some allow in PostToolUse for telemetry.
- Claude Opus, Gemini: blanket ban on network calls from hooks.
- **Synthesis:** Blanket ban in PreToolUse; telemetry in PostToolUse may call network endpoints but must be non-blocking (fire-and-forget or bounded timeout ≤ 200ms) and fail open.

**LOC limits (50 vs. 100 vs. 200).**
- Gemini: 50 LOC.
- Grok: 100 LOC.
- GPT-5: 200 LOC for files, 50 LOC for functions.
- Claude Haiku: 50 LOC per hook function.
- **Synthesis:** 50 LOC per function, 200 LOC per file. Function limit catches real complexity; file limit is looser since one file may contain multiple helpers.

**Hook script naming / language conventions.**
- Claude Haiku assumes JavaScript and prescribes `camelCase` function naming.
- All other models are language-agnostic and prescribe kebab-case filenames.
- **Synthesis:** Claude Haiku's JS-centric framing appears to be an artifact of its training data rather than a property of Claude Code hooks (which are shell-invoked scripts). Adopt the language-agnostic filename convention; apply each language's idiomatic naming internally.

---

## 4. Notable Omissions

- **GPT-4o-mini** omits nearly everything concrete: no stdout/stderr separation, no exit-code protocol, no JSON parsing rules, no path canonicalization, no timeouts. Its output reads as generic software-engineering advice not specific to hooks. The absence is the signal — this model likely lacks training coverage of Claude Code hook semantics.
- **Grok** omits the stdout/stderr protocol discipline, exit-code conventions, and JSON stdin contract — the three rules most specific to Claude Code hooks. Like GPT-4o-mini, its output is generic scripting advice.
- **Gemini** omits observability/structured-logging rules, which appear in GPT-5, Claude Opus, and Claude Haiku. Given Gemini's explicit focus on "simplicity," this is a deliberate choice, but it leaves auditability under-specified.
- **Claude Haiku** omits the `set -euo pipefail` rule (because it assumes JavaScript). Also omits the matcher-specificity rule for performance.
- **Claude Opus** omits explicit rules on determinism and idempotency that GPT-5 emphasizes.
- **GPT-5** omits the documented-header/bypass-instructions rule that Claude Opus flags; auditability suffers without it.

---

## 5. Shared Deterministic Checks

### Multi-model checks

- **Check** — Verify every hook script begins with a shebang line and has user-executable file mode.
  - **Signal** — First two bytes of file + POSIX file-mode bits.
  - **Tool candidate** — ad-hoc (trivial file stat + byte read).
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — GPT-5 allows Windows `.py` without +x if invoked via explicit interpreter; Opus does not address Windows.

- **Check** — Verify filenames under the hooks directory match an event-prefix naming regex.
  - **Signal** — Filesystem listing under `hooks/` or `.claude/hooks/`.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 uses `{Event}__{purpose}.{ext}`; Opus uses `pre-tool-use--purpose.ext` (kebab-case with double dash); Haiku uses camelCase function-name prefix. The naming style diverges but the structural check (event prefix present) is shared.

- **Check** — Verify `settings.json` registers hooks only under known event keys (PreToolUse, PostToolUse, UserPromptSubmit, Stop, Notification, SubagentStop, PreCompact).
  - **Signal** — Parsed `settings.json`.
  - **Tool candidate** — ad-hoc JSON schema validation.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Opus includes the broader set of event names; GPT-5 lists only the four most common. Reconcile to the broader set.

- **Check** — Verify that `settings.json` hook commands point at script paths rather than containing shell pipelines, metacharacters (`|`, `&&`, `;`, `$(`, backticks), or `bash -c`/`sh -c` forms.
  - **Signal** — Parsed `settings.json` + tokenized command strings.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Agreed on substance; Opus additionally checks for `.sh`/`.py`/`.js`/`.ts` extensions.

- **Check** — Verify bash hooks contain `set -euo pipefail` (or equivalent decomposition) within the first ~10 lines.
  - **Signal** — Raw shell source text.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — GPT-5 also requires `IFS=$'\n\t'`; Opus does not. GPT-5 notes dash-compatibility caveat.

- **Check** — Verify Python hook source does not use `subprocess` with `shell=True`, `os.system`, `eval`, or `exec` on agent-supplied input.
  - **Signal** — Python AST.
  - **Tool candidate** — `bandit` (B307, B602, B608).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — All agree; Opus adds heuristic taint-tracking for variables derived from parsed stdin JSON.

- **Check** — Verify bash hooks pass shellcheck with SC2086 (unquoted expansion), SC2046, SC2068 clean.
  - **Signal** — `shellcheck --format=json` output.
  - **Tool candidate** — `shellcheck`.
  - **Raised by** — GPT-5, Claude Opus, Gemini, Grok.
  - **Variance** — Agreed on substance.

- **Check** — Verify Python hook files pass `ruff` and `black --check`.
  - **Signal** — Tool exit codes.
  - **Tool candidate** — `ruff`, `black --check`.
  - **Raised by** — GPT-5, Gemini.
  - **Variance** — Agreed.

- **Check** — Verify hook scripts read from stdin (via `sys.stdin`, `jq`, `cat`, `read`) rather than relying on argv or environment variables.
  - **Signal** — Source grep / AST reference check.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Agreed; both flag scripts that only use positional args.

- **Check** — Verify Python hooks `import json` (or use `jq`) rather than regex-parsing stdin content.
  - **Signal** — Python AST / shell source grep.
  - **Tool candidate** — ad-hoc AST query.
  - **Raised by** — Gemini, Claude Haiku.
  - **Variance** — Gemini checks for `import json` presence when stdin is read; Haiku's version is heuristic based on variable names.

- **Check** — Verify hooks do not invoke network tools (`curl`, `wget`, `nc`, `requests`, `urllib`, `httpx`, `fetch`) — especially in PreToolUse.
  - **Signal** — Source text / import statements.
  - **Tool candidate** — ad-hoc grep; `ruff` custom rule possible.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — GPT-5 and Opus restrict to PreToolUse; Gemini applies to all hooks.

- **Check** — Verify hook file and function size limits.
  - **Signal** — Line counts / AST function body spans.
  - **Tool candidate** — `radon`, `wc -l`, ad-hoc AST.
  - **Raised by** — GPT-5, Claude Haiku, Gemini, Grok.
  - **Variance** — Thresholds diverge: Gemini 50 LOC, Grok 100, GPT-5 200 (functions 50), Haiku 50 per function. Recommend 50 LOC per function, 200 LOC per file as reconciled default.

- **Check** — Verify `exit` statements use only 0, 2, or a documented hook-error code.
  - **Signal** — Shell / Python AST.
  - **Tool candidate** — ad-hoc grep + AST scan.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Agreed.

- **Check** — Verify a test fixture or test file exists for each hook script, invoking it with representative JSON stdin.
  - **Signal** — Filesystem listing under `tests/` or `hooks/tests/`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Naming conventions differ; substance agrees.

### Singleton checks

- **Check** — Verify `.gitignore` contains `.claude/settings.local.json` and that file is not tracked. **Signal** — `.gitignore` + `git ls-files`. **Tool candidate** — ad-hoc. **Raised by** — Claude Opus.
- **Check** — Verify hook script header contains `Event:`, `Matcher:`, `Effect:`, `Bypass:` tokens. **Signal** — First ~20 lines of each hook. **Tool candidate** — ad-hoc regex. **Raised by** — Claude Opus.
- **Check** — Verify Python hooks contain an `if __name__ == "__main__":` guard. **Signal** — Python AST. **Tool candidate** — ad-hoc AST walk. **Raised by** — GPT-5.
- **Check** — Verify `settings.json` command `argv[0]` matches a pinned interpreter path (`/usr/bin/env bash`, `/usr/bin/env python3`, or `./`-prefixed). **Signal** — Parsed `settings.json`. **Tool candidate** — ad-hoc. **Raised by** — GPT-5.
- **Check** — Verify CI workflow files invoke linters with non-zero-on-failure. **Signal** — Parsed `.github/workflows/*.yml`. **Tool candidate** — ad-hoc YAML parse. **Raised by** — GPT-5.
- **Check** — Verify Python duration measurement uses `time.perf_counter()` or `time.monotonic()` rather than `time.time()`. **Signal** — Python AST. **Tool candidate** — ad-hoc AST query. **Raised by** — GPT-5.
- **Check** — Verify PreToolUse/PostToolUse hook `matcher` fields in `settings.json` are not empty, `*`, or `.*`. **Signal** — Parsed `settings.json`. **Tool candidate** — ad-hoc. **Raised by** — Claude Opus.
- **Check** — Verify `exit 2` statements are preceded by a stderr write in the same control-flow branch. **Signal** — Shell/Python source with light control-flow analysis. **Tool candidate** — ad-hoc. **Raised by** — Claude Opus.
- **Check** — Verify hook scripts contain no `grep -r` / `grep -R` (prefer `rg`). **Signal** — Shell source grep. **Tool candidate** — ad-hoc. **Raised by** — Claude Opus.
- **Check** — Verify PostToolUse hooks matching `Edit|Write|MultiEdit` do not invoke full test suites (`npm test`, `pytest`, `mypy .`, `tsc` without file args) unscoped. **Signal** — Referenced scripts + `settings.json`. **Tool candidate** — ad-hoc. **Raised by** — Claude Opus.
- **Check** — Verify Python dependencies are pinned to exact versions in `requirements.txt` or a lockfile. **Signal** — Filesystem + requirements file. **Tool candidate** — `pip-compile --dry-run` or ad-hoc. **Raised by** — GPT-5.
- **Check** — Verify hooks do not log patterns matching `(?i)(token|secret|password|key)` or dump `os.environ`. **Signal** — Source grep. **Tool candidate** — `gitleaks`-style rules, ad-hoc. **Raised by** — GPT-5.

---

## 6. Final Rules File

# Claude Code Agentic Hooks — Rules

**Scope:** Hook scripts configured under `hooks:` in `.claude/settings.json` (or user/enterprise equivalents), invoked on `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `Notification`, `SubagentStop`, and `PreCompact` events.

**Audience:** Engineers and AI assistants authoring or reviewing hooks for a Claude Code project.

**Guiding principles:** Hooks sit in the critical path of agent execution. They must be fast, deterministic, fail safely, and be auditable by security reviewers who may not know the agent's internals. Push policy into reviewable scripts, not inline shell pipelines.

## Structure

- Store hook logic in versioned scripts under `.claude/hooks/`, not inline in `settings.json`. Inline commands escape review, defeat linting, and become unreadable past one line.
- Keep each hook single-purpose; compose multiple hooks rather than branching inside one. Independent hooks are independently testable and disable-able.
- Give every hook script a shebang (`#!/usr/bin/env bash`, `#!/usr/bin/env python3`) and an executable bit. Relying on the shell to guess the interpreter is fragile across machines.
- Name hook scripts by event and purpose, e.g. `pre-tool-use--block-rm-rf.sh`. Directory listings should read like a contract.
- Use narrow `matcher` patterns; avoid `.*` or empty matchers unless the hook truly applies to every tool. Broad matchers add latency to every tool call.
- Keep each hook file under 200 LOC and each function under 50 LOC. Longer hooks are signs the logic belongs elsewhere.
- Use absolute or `./`-prefixed script paths in `settings.json`; pin interpreters via `/usr/bin/env bash`/`python3` rather than bare names. Eliminates PATH injection and portability surprises.
- Do not download or generate hook scripts at runtime; check them into source control. Preserves provenance and reviewability.

## Protocol & I/O

- Reserve stdout exclusively for the hook protocol (JSON or nothing). Any stray `echo` corrupts the agent's view of the hook's decision.
- Send all logs, debug output, and human-readable messages to stderr. Claude Code surfaces stderr on blocking exits.
- Parse hook input from stdin as strict JSON; reject on parse error. Do not rely on positional arguments or environment for tool payloads.
- Use exit code `2` to block with feedback, `0` to allow, and other non-zero codes only for hook bugs. Mixing these silently allows unsafe actions or spams "hook failed" noise.
- Prefer exit-code signaling; emit `{"decision": "block", "reason": "..."}` on stdout only when the reason must reach the model verbatim.
- Parse structured data (JSON, SQL, shell) with dedicated libraries (`jq`, `json.loads`, a real SQL parser). Never use regex on serialized structured data — quoting, escaping, and Unicode tricks defeat it.
- Make decisions deterministic given inputs; do not use randomness or time-dependent logic without a fixed seed.

## Safety

- Treat all hook input as untrusted. Tool arguments are LLM-generated and may contain injected instructions from fetched web pages, files, or user prompts.
- Never pass tool-input fields directly into `eval`, `bash -c`, `sh -c`, `exec`, `os.system`, or `subprocess` with `shell=True`. Pass argv arrays instead.
- When invoking subprocesses, hardcode the command and allowlist arguments; pass untrusted data only as positional arguments to the fixed command.
- Validate file paths against an allowlist of project-relative prefixes after canonicalization via `realpath` / `os.path.realpath`. Naive prefix checks miss `../../../etc/passwd` and symlink escapes.
- Block by default on ambiguity in safety-critical gates. If a hook cannot parse its input or validate a field, exit non-zero.
- Fail closed for safety-critical gates (secret scanning, destructive-command blocks); fail open for advisory gates (lint, format). Declare each hook's failure mode in its header comment.
- Do not make network calls from `PreToolUse` hooks. Network latency multiplied across a session is unacceptable, and offline use becomes impossible.
- Redact or drop secrets from logs; never print `os.environ` or dump env. Use regex like `(?i)(token|secret|password|key)` to flag accidental leakage in review.
- Run hooks with least privilege; do not invoke `sudo` from hook scripts.

## Error Handling

- Set `set -euo pipefail` at the top of every bash hook. Silent failures produce silently-broken gates.
- Enforce a per-hook timeout (default 2 s, max 5 s). Wrap external I/O in `timeout`, `signal.alarm`, or subprocess `timeout=` arguments.
- Wrap external I/O (filesystem, subprocess, network) in try/catch with explicit handling. Never swallow exceptions silently; log them with context before exiting.
- Never `exit 2` (block) without writing a human-readable reason to stderr. Unexplained blocks destroy trust in the hook system.
- Check that required tools (`jq`, `rg`, linters) exist and exit with a clear stderr message if missing. A missing `jq` should say "install jq", not crash cryptically.
- Return stable reason codes from a fixed enum (allow / block / escalate / observe); avoid free-text-only decisions.

## Performance

- Target under 100 ms for hooks matching on every tool call; under 1 s for narrow matchers. Hooks are synchronous and compound across a session.
- Avoid network I/O in hooks generally; forbid it outright in PreToolUse. If a PostToolUse telemetry hook must call network, make it non-blocking with a ≤200 ms timeout and fail open.
- Cache expensive computations (parsed configs, resolved `.gitignore`) in `/tmp` or a project-local cache keyed by mtime.
- Prefer `rg` over `grep -r`, `jq` over `python -c 'json.load'`. Startup time dominates for short hooks.
- Don't run full test suites or type-checkers from `PostToolUse` on single-file edits. Scope checks to the changed file.
- Spawn at most one subprocess per hook invocation where practical.
- Use monotonic timing (`time.perf_counter`, `time.monotonic`) for duration measurements.

## Style

- Write bash for hooks under ~20 lines; switch to Python (or another real language) beyond that, or as soon as structured data parsing is involved. Bash branching and data-structure handling degrades fast.
- Quote every variable expansion (`"$var"`) in bash. Unquoted expansion is the single largest source of shell bugs.
- Enforce formatting and linting in CI: `shellcheck` for bash, `ruff` + `black --check` for Python. Fail the build on violations.
- Keep `settings.json` hook entries to a single `command:` field pointing at a script path; no pipelines, no shell metacharacters.
- Use clear, specific variable names; prefix booleans with `is_` or `should_`.

## Observability

- Emit one structured JSON log line to stderr per invocation, containing: `hook`, `event`, `decision`, `reason`, `duration_ms`, and a correlation/request ID when available. Enables audits and alerting.
- Tag logs with a stable hook name matching the filename.
- Use a fixed decision enum (allow / block / escalate / observe). Log the code, not a prose description.

## Repository Hygiene

- Commit `.claude/settings.json` for team-shared gates; keep personal hooks in `.claude/settings.local.json` and gitignore it. Shared gates need review; personal workflow does not.
- Document every hook in a top-of-file comment stating: **Event**, **Matcher**, **Effect** (what it blocks/allows), **Failure mode** (fail-open or fail-closed), **Bypass** (how to disable in emergencies). Undocumented hooks get disabled in frustration.
- Pin hook dependencies (linters, formatters, Python packages) to exact versions via the project's existing dep manager or a lockfile.
- Include at least one test per hook that pipes a representative JSON payload to stdin and asserts exit code and stdout. Hooks without tests rot silently.
- Add an integration test that loads `settings.json` and executes each registered hook with sample payloads. Verifies wiring matches config.