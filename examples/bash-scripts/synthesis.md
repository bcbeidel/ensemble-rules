# Synthesis of Bash Scripts Best Practices

## 1. Consensus Rules

### Interpreter & Shebang
- **Declare an explicit shebang at the top of every script.** Eliminates ambiguity about the interpreter and surfaces dialect assumptions. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok — models disagreed on exact form; see Divergences)*
- **Do not mix Bash-only features under a `#!/bin/sh` shebang.** Silent bashisms under POSIX shebangs cause failures on dash/BusyBox/Alpine. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Error Handling
- **Enable `set -euo pipefail` near the top of every Bash script.** Turns silent failures, unset-variable typos, and mid-pipeline errors into loud, early exits. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini — flagged as contested by GPT-5, Claude Opus, Claude Haiku)*
- **Install a `trap` on `EXIT` (and often `INT`/`TERM`) to clean up temp files and resources.** Prevents leaked state when scripts die mid-run. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok (as "handle signals gracefully"))*
- **Verify required external commands exist up front with `command -v`.** Fails fast with an actionable message instead of crashing mid-run. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Quoting & Variable Safety
- **Always double-quote variable expansions and command substitutions unless splitting or globbing is explicitly intended.** The single largest source of real-world Bash bugs. *(near-identical wording across all six models)*
- **Use `"$@"` to forward arguments; never use unquoted `$@` or `$*`.** Preserves argument boundaries across whitespace and special characters. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Use `$(...)` for command substitution, not backticks.** Nestable, more readable, and universally supported by linters (SC2006). *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Declare function-scoped variables with `local`.** Prevents accidental global leakage and cross-call state bugs. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Never `eval` untrusted input.** Shell's equivalent of SQL injection. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Grok, GPT-4o-mini)*

### Structure
- **Wrap execution logic in a `main` function and call `main "$@"` at the end.** Makes the script sourceable for testing and gives a single entry point. *(substantively similar across Claude Opus, Claude Haiku, Gemini)*
- **Put scripts through functions rather than sprawling top-level flow.** Improves testability, reuse, and readability. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)*

### Control Flow & Idioms
- **Prefer `[[ ... ]]` over `[ ... ]` in Bash for conditionals.** Avoids word-splitting and globbing inside tests. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Read files line-by-line with `while IFS= read -r line; do ...; done < file`, never `for line in $(cat file)`.** The latter word-splits and globs; it's incorrect, not merely slow. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Do not parse the output of `ls`.** Filenames with spaces, newlines, or leading dashes break it; use globs or `find -print0`. *(near-identical wording across Claude Opus, Claude Haiku, Gemini)*
- **Create temporary files with `mktemp`, and clean them up via `trap`.** Predictable names are race-prone and symlink-attack vectors. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Style
- **Use lowercase `snake_case` for local/script variables; reserve UPPERCASE for exported environment variables and constants.** Matches long-standing Unix convention and avoids collisions. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Prefer `printf` over `echo` for anything beyond a literal string.** `echo`'s handling of flags and escapes varies across shells. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Safety
- **Validate and sanitize script inputs before use.** Scripts run in automation where malformed data is the norm. *(substantively similar across Claude Haiku, Grok, GPT-4o-mini)*

### Performance
- **Avoid useless use of `cat` (`cat file | cmd` → `cmd < file` or `cmd file`).** Unnecessary fork; flagged by SC2002. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku)*
- **Prefer Bash builtins and parameter expansion over external commands in hot loops.** Forking dominates runtime at scale. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok, GPT-4o-mini)*

### Tooling
- **Run ShellCheck in CI and treat warnings as errors; document any local disables.** Catches ~80% of the bugs described elsewhere in this document. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*

## 2. Strong Minority Rules

- **Format with `shfmt` and fail CI on drift.** (GPT-5, Claude Opus) — Eliminates style debates and produces consistent diffs; a mechanical, low-cost control worth keeping.
- **Separate diagnostic output to stderr (`>&2`).** (Claude Haiku, Gemini) — Allows callers to pipe data and diagnostics independently; a basic Unix contract often missed.
- **Use `${var:?message}` for required inputs and `${var:-default}` for optional ones.** (Claude Opus, Claude Haiku) — Concise fail-fast idiom; superior to ad-hoc emptiness checks.
- **Always verify `cd` succeeded (`cd foo || exit`).** (Claude Opus, Claude Haiku) — A failed `cd` followed by `rm -rf *` is a recurring disaster pattern; trivially checkable (SC2164).
- **Do not rely on GNU-specific flags (`sed -i`, `grep -P`, `readlink -f`) without declaring the dependency.** (Claude Opus, Claude Haiku implicitly) — Silent cross-platform breakage between Linux and macOS/BSD is a very common real-world failure.
- **Set `IFS=$'\n\t'` at the top of Bash scripts.** (Claude Opus, Claude Haiku) — Reduces word-splitting surprises; contested because unnecessary for scripts that don't do field splitting.
- **Pass `--` before untrusted arguments to option-parsing commands (e.g., `rm -- "$path"`).** (GPT-5) — Prevents option injection from filenames beginning with `-`.
- **Keep scripts under ~300 lines; rewrite in a real language beyond that.** (Claude Opus) — Soft signal but a useful heuristic; Bash's lack of data structures and error handling doesn't scale.
- **Make scripts sourceable by guarding `main` with `[[ "${BASH_SOURCE[0]}" == "$0" ]]`.** (Claude Opus, Claude Haiku) — Enables unit testing with bats/shunit2.
- **Pin locale with `LC_ALL=C` for sort, comparison, and regex when semantics matter.** (Claude Opus) — Locale-dependent sort has caused real production outages.
- **Support a debug mode (e.g., `DEBUG=1` enabling `set -x`).** (Claude Opus, Claude Haiku) — Post-hoc debugging without tracing is painful.

## 3. Divergences

### Shebang form: `#!/bin/bash` vs `#!/usr/bin/env bash`
- **`#!/usr/bin/env bash`**: GPT-5, Claude Opus (as acceptable), Claude Haiku (with fallback).
- **`#!/bin/bash` (hard path)**: Gemini (strongly, citing predictability in controlled production environments), Claude Haiku (as primary).
- **Synthesis**: Both are defensible; the trade-off is PATH portability (env form) vs predictability/security in controlled environments (hard path). Recommend `#!/usr/bin/env bash` as the default (broader portability, works on macOS with Homebrew Bash), but allow `#!/bin/bash` in tightly controlled CI/container contexts where PATH is trusted. This is genuinely contested; projects should pick one and stay consistent.

### `set -e` as universal default
- **Use it**: GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini — all endorse `set -euo pipefail`.
- **Caveats raised**: GPT-5, Claude Opus, and Claude Haiku all explicitly flag that `-e` has subtle semantics (ignored in conditionals, `&&` chains, function calls in `if`) and that some practitioners prefer explicit checks.
- **Synthesis**: Enable `set -euo pipefail`, but understand its limits and write explicit error handling where `-e` does not help. The consensus is strong enough to keep as the rule; the "contested" tag is about when to supplement, not whether to enable.

### Indentation width
- **2 spaces**: GPT-5, Claude Opus (2 or 4), Claude Haiku, Gemini.
- **4 spaces**: Grok.
- **Synthesis**: Consistency matters more than the specific width. Default to 2 spaces (matches Google Shell Style Guide and the majority here); enforce via `shfmt` or `.editorconfig`.

### Scope: Bash-only vs POSIX portability
- **Bash-first, acknowledge POSIX**: Claude Opus, Claude Haiku, Gemini, Grok.
- **POSIX-preferred when feasible**: GPT-5 (explicitly prefers `sh` when Bash features aren't needed).
- **Synthesis**: Target Bash 4.0+ by default for production ops tooling (the dominant case). Use POSIX `sh` only when genuine portability to dash/BusyBox is required, and declare that intent in the shebang and ShellCheck directive. Do not write "portable-ish Bash" under a `/bin/sh` shebang.

### `IFS=$'\n\t'` at top of script
- **Required**: Claude Opus, Claude Haiku.
- **Not mentioned or discouraged as default**: GPT-5 (warns against global IFS changes), Gemini, Grok, GPT-4o-mini.
- **Synthesis**: This is a genuinely contested practice. GPT-5's concern is real — a global IFS change can produce surprising behavior elsewhere. Recommend scoping IFS changes to the specific `read` invocation (`IFS=$'\n' read -r ...`) rather than globally. Keep the Claude recommendation as optional minority guidance.

### Useless use of `cat` (UUOC)
- **Avoid**: GPT-5 (contested), Claude Opus, Claude Haiku.
- **Synthesis**: Flag via SC2002 but accept that `cat file | cmd` is often chosen for readability or left-to-right reading of pipelines. Treat as a warning, not a hard error.

## 4. Notable Omissions

- **ShellCheck integration** is absent from GPT-4o-mini and Grok — a striking omission given it's the single highest-leverage tool mentioned by the other four models.
- **Quoting discipline** (SC2086) is mentioned by GPT-4o-mini but without the specificity of "command substitutions too" — Grok mentions it; otherwise coverage is universal.
- **`"$@"` vs `$*`** is absent from GPT-4o-mini and Grok, despite being a near-universal consensus rule.
- **`local` for function-scoped variables** is absent from GPT-4o-mini and Grok.
- **`mktemp` for temp files** is absent from GPT-4o-mini, Gemini, and Grok — a notable safety gap.
- **`$(...)` over backticks** is absent from GPT-4o-mini and Grok — one of the most universally agreed style rules.
- **Reading files with `while read`** is absent from GPT-4o-mini and Grok.
- **Never parsing `ls`** is absent from GPT-5, GPT-4o-mini, and Grok. GPT-5 covers it implicitly via the `find -print0` rule, but not by name.
- **`trap` for cleanup** is absent from Gemini and GPT-4o-mini.
- **`main "$@"` entry-point pattern** is absent from GPT-4o-mini and Grok.

The pattern: GPT-4o-mini and Grok produced shorter, less specific rule sets that omit several well-established practices. Their omissions likely reflect model capacity on this topic rather than a considered disagreement.

## 5. Shared Deterministic Checks

### Shared checks (multiple models)

- **Check** — Verify every script starts with a valid shebang (`#!/bin/bash`, `#!/usr/bin/env bash`, or `#!/bin/sh`) on line 1.
  - **Signal** — First line of raw source.
  - **Tool candidate** — `shellcheck SC2148` (catches missing shebang); ad-hoc regex for form preference.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — Models differ on which shebangs are acceptable (see Divergences). Gemini is strictest (hard path only); others accept either form.

- **Check** — Verify `set -euo pipefail` (or equivalent separate `set` statements covering all three options) appears in the prologue (first ~20 non-comment lines) of Bash scripts.
  - **Signal** — Raw source text.
  - **Tool candidate** — Ad-hoc regex; no single ShellCheck rule covers all three.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — Grok requires exact string match; others allow equivalent forms (`set -Eeuo pipefail`, three separate `set` lines). Claude Opus makes the rule configurable for teams that deliberately avoid `-e`.

- **Check** — Flag unquoted variable expansions that permit word-splitting or globbing.
  - **Signal** — Output of `shellcheck --format=json`.
  - **Tool candidate** — `shellcheck SC2086` (and SC2046 for unquoted command substitutions, SC2068 for unquoted `$@`).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — None of substance. Universal agreement that ShellCheck is the enforcement tool.

- **Check** — Flag legacy backtick command substitution in favor of `$(...)`.
  - **Signal** — Raw source text / ShellCheck output.
  - **Tool candidate** — `shellcheck SC2006`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — None.

- **Check** — Flag use of `ls` output in a `for` loop or pipeline (parsing `ls`).
  - **Signal** — ShellCheck output.
  - **Tool candidate** — `shellcheck SC2010` / `SC2012` / `SC2045`.
  - **Raised by** — Claude Opus, Claude Haiku, Gemini.
  - **Variance** — None.

- **Check** — Flag `for line in $(cat file)` idiom; require `while IFS= read -r` for line iteration.
  - **Signal** — ShellCheck output.
  - **Tool candidate** — `shellcheck SC2013` / `SC2162`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — None.

- **Check** — Flag `find ... | xargs ...` without `-print0`/`-0` or `-exec … {} +`.
  - **Signal** — ShellCheck output.
  - **Tool candidate** — `shellcheck SC2038`.
  - **Raised by** — GPT-5, Claude Opus (implicit).
  - **Variance** — None of substance.

- **Check** — Flag any occurrence of `eval`, requiring explicit justification comment to suppress.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc grep; `shellcheck SC2294` covers some cases.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — All models treat `eval` as a flag-worthy event; none attempt taint analysis.

- **Check** — Flag `cd` invocations not followed by `|| exit` / `|| return` in scripts lacking `set -e`.
  - **Signal** — ShellCheck output.
  - **Tool candidate** — `shellcheck SC2164`.
  - **Raised by** — Claude Opus, Claude Haiku.
  - **Variance** — None.

- **Check** — Flag useless use of `cat` (single-file `cat file | cmd`).
  - **Signal** — ShellCheck output.
  - **Tool candidate** — `shellcheck SC2002`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — All three note this is contested/style-level; treat as warning.

- **Check** — Flag variables assigned inside functions without `local`.
  - **Signal** — AST / ShellCheck output.
  - **Tool candidate** — `shellcheck SC2155` (partial).
  - **Raised by** — GPT-5 (with caveats), Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 notes full dataflow enforcement is hard; others accept the ShellCheck approximation.

- **Check** — Verify formatting with `shfmt -d` (diff mode); fail on non-empty diff.
  - **Signal** — Output of `shfmt`.
  - **Tool candidate** — `shfmt`.
  - **Raised by** — GPT-5, Claude Opus (implicitly via "run ShellCheck/formatter in CI").
  - **Variance** — GPT-5 specifies `-i 2 -ci -bn`; others leave configuration open.

- **Check** — Under a `#!/bin/sh` shebang, flag Bash-only constructs (`[[ ]]`, arrays, `local`, `<<<`, `$'...'`, `${var,,}`, process substitution).
  - **Signal** — ShellCheck with `shell=sh` directive; optionally `checkbashisms`.
  - **Tool candidate** — `shellcheck -s sh` (SC2039/SC3000-series); `checkbashisms`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 names `checkbashisms`; Claude Opus/Haiku rely on ShellCheck's dialect mode.

### Singleton checks (one model each, generally useful)

- **Check** — Verify trailing whitespace is absent and files end with a newline.
  - **Signal** — Raw source bytes.
  - **Tool candidate** — ad-hoc; covered by `editorconfig-checker`.
  - **Raised by** — GPT-5.

- **Check** — If a script calls `mktemp`, require at least one `trap ... EXIT` registered before the first `mktemp` call.
  - **Signal** — Raw source text / AST.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.

- **Check** — Flag hardcoded `/tmp/...` write targets (including `/tmp/$$`-style names) as unsafe temp file usage.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — Claude Opus.

- **Check** — Flag known GNU-only flag patterns (`sed -i` without backup, `grep -P`, `readlink -f`, `date -d`, `stat -c`, `xargs -r`, `cp --parents`) unless a `# requires: gnu-coreutils` prologue comment is present.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc regex against a curated list.
  - **Raised by** — Claude Opus.

- **Check** — If a `main` function exists, verify its invocation is guarded by `[[ "${BASH_SOURCE[0]}" == "$0" ]]`.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verify executable bit matches intent: scripts with shebangs should have execute bits; library files without shebangs should not.
  - **Signal** — File mode + raw source.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Under a non-`.sh` extension and no shebang, require a `# shellcheck shell=bash|sh` directive in the first 5 lines.
  - **Signal** — File extension + raw source.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Flag `grep ... >/dev/null` and suggest `grep -q`.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — Claude Haiku.

- **Check** — Flag `rm -rf $var` (unquoted) as a high-severity safety violation.
  - **Signal** — ShellCheck output (SC2086 scoped to `rm`).
  - **Tool candidate** — `shellcheck SC2086` filtered by command.
  - **Raised by** — Claude Haiku, GPT-5.

- **Check** — Verify line length does not exceed 100 characters.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc / `editorconfig-checker`.
  - **Raised by** — Claude Haiku, Gemini.

---

## 6. Final Rules File

# Bash Scripts — Rules

**Scope.** Bash (≥ 4.0) and POSIX `sh` scripts used in production ops tooling, CI/CD pipelines, and developer workflows. **Audience.** Engineers and AI coding assistants authoring, reviewing, or generating shell code.

## Interpreter & Portability

- **Start every script with an explicit shebang that matches the features it uses.** Eliminates ambiguity about dialect. Prefer `#!/usr/bin/env bash` by default; `#!/bin/bash` is acceptable in controlled environments; `#!/bin/sh` declares strict POSIX scope. (contested — see below)
- **Pick one shell dialect per script and do not mix.** Silently using Bash features under `#!/bin/sh` fails on dash/BusyBox/Alpine.
- **Do not rely on GNU-specific flags (`sed -i`, `grep -P`, `readlink -f`, `date -d`, `stat -c`, `xargs -r`) without declaring the dependency.** These silently differ on macOS/BSD.
- **Pin locale with `LC_ALL=C` for sort, comparison, and regex when semantics would otherwise vary.** Locale-dependent behavior has caused real outages.

## Structure

- **Wrap executable logic in a `main` function and call `main "$@"` at the end of the script.** Single entry point; makes the script sourceable for testing.
- **Keep scripts under ~300 lines; rewrite in a real language past that.** Bash's lack of data structures and error handling doesn't scale.
- **Put configuration (paths, flags, defaults) at the top as `readonly` variables.** Readers shouldn't hunt for magic values.
- **Declare function-local variables with `local`.** Prevents accidental global leakage between function calls.
- **Use functions for any logic used more than once or longer than ~10 lines.** Inline pipelines past that length are unreadable.
- **Include a header comment describing purpose, usage, and dependencies.** Essential context for future maintainers.
- **Make scripts sourceable: guard `main` with `[[ "${BASH_SOURCE[0]}" == "$0" ]] && main "$@"`.** Enables bats/shunit2 unit testing of internal functions.

## Error Handling

- **Start every Bash script with `set -euo pipefail`.** Defaults let failures pass silently; this makes them loud. (contested — understand the edge cases before relying on it)
- **Install a `trap` on `EXIT` (and typically `INT`/`TERM`) to clean up temp files and resources.** Prevents leaked state on interruption or error.
- **Check exit status of commands whose failure you can meaningfully handle; do not rely solely on `set -e`.** `-e` is skipped in `&&` chains, function calls in conditions, and similar contexts.
- **Verify required external commands exist up front with `command -v cmd >/dev/null || die "missing: cmd"`.** Fails fast with an actionable message.
- **Define a `die`/`error` helper that prints to stderr and exits non-zero; use it instead of bare `exit 1`.** Errors without messages are useless in logs.
- **Print diagnostic and error messages to stderr (`>&2`).** Lets callers pipe data and diagnostics independently.
- **Always check that `cd` succeeded (`cd foo || exit`).** A failed `cd` followed by `rm -rf *` has destroyed systems.

## Quoting & Variable Safety

- **Always double-quote variable expansions and command substitutions: `"$var"`, `"$(cmd)"`.** Prevents word-splitting and globbing — the largest class of shell bugs.
- **Use `"$@"` to forward arguments; never use unquoted `$@` or `$*`.** Preserves argument boundaries across whitespace and special characters.
- **Use `$(...)` for command substitution, not backticks.** Nestable, readable, and universally supported.
- **Prefer `"${var}"` over `"$var"` when the variable abuts text that could be part of an identifier.** `"${foo}bar"` is unambiguous.
- **Use `${var:-default}` for optional inputs and `${var:?message}` to assert a variable is set.** Fails fast with context instead of proceeding with empty strings.
- **Never `eval` input you don't fully control.** Shell injection, full stop.
- **Pass `--` before untrusted arguments to commands like `rm`, `grep`, `mv`, `cp`.** Prevents option injection from filenames beginning with `-`.
- **Do not change `IFS` globally; scope it to the specific `read` invocation (`IFS=$'\n' read -r ...`).** Global changes cause surprising behavior elsewhere.

## Control Flow & Idioms

- **In Bash, prefer `[[ ... ]]` over `[ ... ]` for conditionals.** Avoids word-splitting and globbing inside tests; supports pattern matching.
- **In POSIX `sh`, use `[ ... ]` and quote every operand.** `[[ ]]` is not portable.
- **Read files line-by-line with `while IFS= read -r line; do ...; done < file`, never `for line in $(cat file)`.** The latter word-splits and globs — it's wrong, not just slow.
- **Iterate arrays with `for item in "${arr[@]}"` (quoted).** Preserves element boundaries.
- **Never parse the output of `ls`.** Filenames with spaces, newlines, or leading dashes break it; use globs or `find -print0`.
- **When handling many paths, use `find -print0 | xargs -0` or `find -exec ... {} +`.** Safely handles spaces and newlines in filenames.
- **Prefer explicit `if`/`then`/`else` over long `&&`/`||` chains for control flow.** More readable and less error-prone than short-circuit evaluation.

## Safety

- **Create temporary files and directories with `mktemp -d`, never with `$$` or predictable names.** Predictable paths are race-prone and symlink-attack vectors.
- **Register cleanup for temp files immediately after `mktemp`: `trap 'rm -rf "$tmpdir"' EXIT`.** Ensures cleanup on any exit path.
- **Validate and sanitize all user input and command-line arguments.** Scripts run in automation where malformed data is the norm.
- **Never pass secrets as command-line arguments.** Argv is visible to other users via `ps`. Use environment variables or files.
- **Never use `rm -rf $var` unquoted; ensure the variable is both quoted and validated non-empty.** One typo away from catastrophe.

## Style

- **Use `snake_case` lowercase for local/script variables; reserve UPPERCASE for exported environment variables and constants.** Matches Unix convention; avoids collisions with env vars.
- **Prefer `printf` over `echo` for anything beyond a literal string.** `echo`'s handling of `-e`, `-n`, and escapes varies across shells.
- **Use 2-space indentation consistently; no tabs.** Enforce via `shfmt` or `.editorconfig`.
- **Keep lines under ~100 characters.** Improves readability and discourages overly complex one-liners.
- **Write comments explaining *why*, not *what*.** Code shows what it does; comments explain intent.
- **Avoid deeply nested conditionals; prefer early returns or guard clauses.** Reduces cognitive load.

## Performance

- **Avoid useless use of `cat` (`cat file | cmd` → `cmd < file`).** Unnecessary fork. (contested — some prefer for pipeline readability)
- **Prefer Bash builtins and parameter expansion (`${var##*/}`, `${var%.*}`) over `basename`/`dirname`/`sed` for simple string work.** No fork; faster.
- **Don't call external commands inside tight loops when a single `awk` or `sed` pass will do.** Forking dominates runtime at scale.
- **Use `grep -F` for fixed-string matches by default.** Faster and avoids regex pitfalls.
- **Use `grep -q` instead of `grep ... >/dev/null` for existence checks.** More direct.

## Tooling & CI

- **Run ShellCheck on every script in CI and treat warnings as errors.** Catches the majority of bugs described in this document. Document any local disables with a justification comment.
- **Format with `shfmt -d` in CI and fail on drift.** Eliminates style debates and produces clean diffs.
- **For files without a standard extension or without a shebang, add `# shellcheck shell=bash` (or `=sh`) at the top.** Ensures ShellCheck runs in the correct dialect.
- **Ensure executable scripts have execute bits and library files (meant for sourcing) do not.** Prevents accidental direct execution of libraries.
- **Support a debug mode (e.g., `[[ "${DEBUG:-}" ]] && set -x`).** Post-hoc debugging without tracing is painful.

## Testing

- **Write end-to-end tests for non-trivial scripts using `bats` or `shunit2`.** Catches regressions across environments.

---

### Contested Points (explicit)

- **`#!/usr/bin/env bash` vs `#!/bin/bash`.** The env form maximizes portability (especially on macOS with Homebrew Bash); the hard path is more predictable in controlled environments. Either is acceptable; be consistent within a project.
- **`set -e` itself.** A minority of expert practitioners prefer explicit error checking because of `-e`'s subtle semantics. This ruleset keeps `set -euo pipefail` as the default because the benefits outweigh the surprises for most scripts, but supplement with explicit checks where `-e` is known to miss.
- **`IFS=$'\n\t'` at script top.** Protects against word-splitting on spaces in filenames but can surprise code that relies on default IFS. Prefer scoping IFS to individual `read` calls unless you control the entire script's field-splitting model.
- **Useless use of `cat` (SC2002).** Some developers prefer left-to-right pipeline readability. Treat as a style warning, not a hard error.