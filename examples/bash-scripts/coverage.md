# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Reserve uppercase variable names for exported environment variables.** | Variables & Quoting |  |  |  |  | ✓ |  | 1 |
| **(contested) Stick to Bash features documented in the `bash` manual (version 4.0+); avoid undocumented internals or version-specific quirks.** Ensures scripts run on any modern Bash without surprises | Portability & Alternatives |  |  |  | ✓ |  |  | 1 |
| **(contested) Use 2 spaces for indentation.** | Style |  |  |  |  | ✓ |  | 1 |
| **(contested) Wrap external commands in defensive patterns** (e.g., `set +e; cmd; rc=$?; set -e`) **only when you genuinely need to handle a non-zero exit; otherwise, let `set -e` do its job.** Overuse of this pattern makes scripts harder to read and defeats the purpose of `set -e` | Error Handling & Debugging |  |  |  | ✓ |  |  | 1 |
| **Add comments explaining *why*, not *what*: the code shows what it does; comments explain intent and non-obvious trade-offs.** Saves time for the next reader | Style & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Always check `cd` succeeded, or use `cd foo \|\| exit`.** A failed `cd` followed by `rm -rf *` has destroyed many systems | Safety |  |  | ✓ |  |  |  | 1 |
| **Always quote variable expansions (`"$var"`).** | Variables & Quoting |  |  |  |  | ✓ |  | 1 |
| **Always use braces when expanding variables (`"${var}"`).** | Variables & Quoting |  |  |  |  | ✓ |  | 1 |
| **Avoid `cat file \| cmd`; use `cmd < file` or `cmd file`.** Pointless fork; linters flag it (UUOC) | Performance |  |  | ✓ |  |  |  | 1 |
| **Avoid `eval` and `source` with untrusted input.** Both execute arbitrary code; a vector for injection attacks | Control Flow & Idioms |  |  |  | ✓ |  |  | 1 |
| **Avoid deeply nested conditionals; use early returns or guards.** Reduces cognitive load | Style & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Avoid unnecessary loops over large data; use `xargs`, `parallel`, or similar for bulk operations if performance is critical.** Bash loops are slow at scale; these tools are designed for bulk I/O | Performance & External Tools |  |  |  | ✓ |  |  | 1 |
| **Check that required commands are available at the start of the script using `command -v cmd >/dev/null 2>&1 \|\| error "cmd not found"`.** Fails fast with a clear message; beats silent failure or a cryptic error deep in execution | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Check the exit status of commands whose failure you can meaningfully handle; do not rely solely on `set -e`.** `-e` has well-known gaps (functions in conditions, `&&` chains) | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Create temp files with `mktemp`, never with `$$` or predictable names.** Predictable names are a symlink-attack vector and race-prone | Safety |  |  | ✓ |  |  |  | 1 |
| **Declare function-local variables with `local`.** Otherwise they leak into the global scope and persist across calls | Style |  |  | ✓ |  |  |  | 1 |
| **Declare function-scoped variables with `local`.** | Variables & Quoting |  |  |  |  | ✓ |  | 1 |
| **Declare required external commands at the top and verify with `command -v`.** Failing with "missing `jq`" beats failing with "parse error." | Dependencies & Portability |  |  | ✓ |  |  |  | 1 |
| **Declare the interpreter explicitly with `#!/usr/bin/env bash` or `#!/bin/sh`.** Ambiguous shebangs cause version-specific bugs that surface only in production | Structure |  |  | ✓ |  |  |  | 1 |
| **Define a `main()` function and call it at the end of the script, not inline.** Ensures all functions are defined before execution; clarifies entry point; aids testing | Structure & Initialization |  |  |  | ✓ |  |  | 1 |
| **Define and use an `error()` function that prints to stderr and exits with a non-zero code.** Centralizes error reporting; ensures consistent behavior | Error Handling & Debugging |  |  |  | ✓ |  |  | 1 |
| **Do not call external commands inside tight loops when a builtin or single `awk`/`sed` pass will do.** Forking dominates runtime for anything over a few thousand iterations | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not parse the output of `ls`.** | Commands & Pipes |  |  |  |  | ✓ |  | 1 |
| **Do not rely on GNU-specific flags (`sed -i`, `grep -P`, `readlink -f`) without declaring a GNU coreutils dependency.** These silently differ on macOS and BSD | Dependencies & Portability |  |  | ✓ |  |  |  | 1 |
| **Encapsulate all execution logic within functions.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Explicitly exit with a non-zero status code on failure.** | Error Handling |  |  |  |  | ✓ |  | 1 |
| **For complex logic, consider rewriting in a faster language (Python, Go, Rust) rather than trying to optimize Bash.** Bash is glue; sophisticated business logic belongs elsewhere | Portability & Alternatives |  |  |  | ✓ |  |  | 1 |
| **If POSIX `sh` compatibility is a requirement, test against `dash` or the host system's default shell and use only POSIX features; document any Bash-specific workarounds.** Signals intent; avoids silent failures in constrained environments | Portability & Alternatives |  |  |  | ✓ |  |  | 1 |
| **Immediately after the shebang, add a comment block explaining the script's purpose, usage, and any prerequisites.** Saves time during debugging and onboarding | Structure & Initialization |  |  |  | ✓ |  |  | 1 |
| **Include a header comment explaining the script's purpose, usage, and dependencies.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Install a `trap` for `EXIT` to clean up temp files and resources.** Scripts that die mid-run otherwise leak state | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Keep functions small and focused (under ~50 lines); break complex logic into named functions.** Eases testing and reasoning about behavior | Style & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Keep scripts under ~300 lines; rewrite in a real language past that.** Bash's lack of data structures and error handling doesn't scale | Structure |  |  | ✓ |  |  |  | 1 |
| **Limit lines to a maximum of 100 characters.** | Style |  |  |  |  | ✓ |  | 1 |
| **Name scripts with a `.sh` extension for libraries, and no extension for installed executables.** Executables on `$PATH` shouldn't advertise their implementation | Style |  |  | ✓ |  |  |  | 1 |
| **Name variables and functions in lowercase with underscores: `my_var`, `my_function()`.** Matches Bash conventions; uppercase is reserved for environment variables and constants | Style & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Never parse the output of `ls`.** Filenames with spaces, newlines, or leading dashes break it; use globs or `find -print0` | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Never use `eval` on input you don't fully control.** It's shell injection, full stop | Safety |  |  | ✓ |  |  |  | 1 |
| **Never use `rm -rf $var` with an unquoted variable; use `rm -rf "$var"` and validate that `$var` is set and non-empty.** One typo or unset variable away from deleting the wrong tree | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Never use unquoted command substitution: use `"$(cmd)"`, not `` `cmd` ``.** Modern syntax is clearer and nests safely; backticks are legacy and error-prone | Quoting & Variable Safety |  |  |  | ✓ |  |  | 1 |
| **Pass secrets via environment variables or files, never as command-line arguments.** Argv is visible in `ps` to other users | Safety |  |  | ✓ |  |  |  | 1 |
| **Pick one shell dialect per script and do not mix.** "Portable-ish Bash" under a `/bin/sh` shebang fails silently on dash and BusyBox | Structure |  |  | ✓ |  |  |  | 1 |
| **Pin behavior with `LC_ALL=C` for sort, comparison, and regex when locale would change semantics.** Locale-dependent sort has caused real outages | Dependencies & Portability |  |  | ✓ |  |  |  | 1 |
| **Prefer `"${var:?message}"` over silent defaults for required inputs.** Fails fast with a message instead of proceeding with empty strings | Safety |  |  | ✓ |  |  |  | 1 |
| **Prefer `$(...)` over backticks for command substitution.** Backticks don't nest cleanly and are deprecated in spirit | Style |  |  | ✓ |  |  |  | 1 |
| **Prefer `[[ | Commands & Pipes |  |  |  |  | ✓ |  | 1 |
| **Prefer `grep -q` over `grep | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Prefer `if [[ condition ]]` (Bash conditional) over `if [ condition ]` (POSIX test) in Bash scripts.** `[[` is more forgiving (no quote-splitting in operands) and supports pattern matching; worth the Bash dependency | Control Flow & Idioms |  |  |  | ✓ |  |  | 1 |
| **Prefer `printf` over `echo` for anything beyond a literal string.** `echo` behavior with flags and escapes varies by shell | Style |  |  | ✓ |  |  |  | 1 |
| **Prefer built-in Bash operations (`${var%suffix}`, `[[ ]]`) over spawning external commands when the same logic is available.** Avoids subshell overhead; still negligible in most cases but worth knowing | Performance & External Tools |  |  |  | ✓ |  |  | 1 |
| **Prefer explicit `if`/`then`/`else` over `&&`/`\|\|` chains for control flow.** More readable; less likely to have unintended side effects from short-circuit evaluation | Control Flow & Idioms |  |  |  | ✓ |  |  | 1 |
| **Prefer parameter expansion (`${var%.*}`, `${var##*/}`) over `basename`/`dirname`/`sed` for simple string manipulation.** No fork, and it's faster | Performance |  |  | ✓ |  |  |  | 1 |
| **Prefix external commands with `command` (e.g., `command git`) when there is a risk of alias or function shadowing.** Ensures you call the real command; matters in CI and automation contexts | Error Handling & Debugging |  |  |  | ✓ |  |  | 1 |
| **Print error and diagnostic messages to standard error (stderr).** | Error Handling |  |  |  |  | ✓ |  | 1 |
| **Put configuration (paths, flags, defaults) at the top as `readonly` variables.** Readers shouldn't hunt for magic values | Structure |  |  | ✓ |  |  |  | 1 |
| **Quote all variable references: `"$var"`, not `$var`, unless you have a specific reason to expand word-splitting or pathname globbing.** Prevents word-splitting and globbing bugs; the default case in well-written scripts is quotes everywhere | Quoting & Variable Safety |  |  |  | ✓ |  |  | 1 |
| **Quote every variable expansion unless you explicitly need word-splitting.** `"$var"` and `"$@"` are the defaults; `$var` and `$*` are the exceptions | Safety |  |  | ✓ |  |  |  | 1 |
| **Quote the right-hand side of `=~` operators to avoid regex interpretation of literal strings:** use `[[ $str =~ ^prefix ]]` for regex, or `[[ "$str" == prefix* ]]` for glob patterns.** (contested) Prevents unexpected regex metacharacter expansion; easier to read intent | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Read files with `while IFS= read -r line; do ...; done < file`, not with `for line in $(cat file)`.** The latter word-splits and globs; it's wrong, not just slow | Performance |  |  | ✓ |  |  |  | 1 |
| **Run ShellCheck on every script in CI and treat warnings as errors.** It catches roughly 80% of the bugs described in this document | Style |  |  | ✓ |  |  |  | 1 |
| **Set `IFS=$'\n\t'` after `set -euo pipefail` unless you have a specific reason not to.** Reduces word-splitting surprises; the default IFS (space, tab, newline) causes pathological behavior when filenames or values contain spaces | Structure & Initialization |  |  |  | ✓ |  |  | 1 |
| **Set `IFS=$'\n\t'` at the top of Bash scripts.** The default IFS splits on spaces, which interacts badly with filenames | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Set `set -euo pipefail` (or `set -e -u -o pipefail`) near the top of the script, before any meaningful code.** Makes error handling the default; unset variables and pipeline errors are caught | Structure & Initialization |  |  |  | ✓ |  |  | 1 |
| **Start every Bash script with `set -euo pipefail`.** Defaults let failures pass silently; this makes them loud | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Start every script with `#!/bin/bash` (or `#!/usr/bin/env bash` if portability across `/bin` vs `/usr/bin` is required).** Explicit shebang prevents accidental execution in `sh` and documents intent | Structure & Initialization |  |  |  | ✓ |  |  | 1 |
| **Start every script with `set -euo pipefail`.** | Error Handling |  |  |  |  | ✓ |  | 1 |
| **Support a `-x` or `DEBUG=1` mode that enables `set -x`.** Post-hoc debugging without tracing is painful | Testing & Debugging |  |  | ✓ |  |  |  | 1 |
| **Use 2-space indentation for consistency and to keep lines under 100 characters where practical.** Industry standard in modern shell; long lines are hard to follow | Style & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Use 2-space or 4-space indentation consistently; never tabs mixed with spaces.** Mixed whitespace breaks heredocs and diffs | Style |  |  | ✓ |  |  |  | 1 |
| **Use `"$@"` (quoted) when passing function arguments onward, not `$@` or `$*`.** Preserves argument boundaries; crucial for handling arguments with spaces or special characters | Quoting & Variable Safety |  |  |  | ✓ |  |  | 1 |
| **Use `"${var}"` instead of `"$var"` when the variable is adjacent to text that could be part of a variable name.** Prevents ambiguity; `"${foo}bar"` is clearer than `"$foobar"` if you mean the variable `foo` followed by literal `bar` | Quoting & Variable Safety |  |  |  | ✓ |  |  | 1 |
| **Use `#!/bin/bash` as the shebang.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Use `$(command)` for command substitution instead of backticks.** | Commands & Pipes |  |  |  |  | ✓ |  | 1 |
| **Use `${var:-default}` for optional variables, `${var:?error}` to assert a variable is set and non-empty.** Explicit; safer than ad-hoc fallbacks | Quoting & Variable Safety |  |  |  | ✓ |  |  | 1 |
| **Use `command -p` to call external commands with a minimal/secure PATH in sensitive contexts.** Reduces chance of PATH injection; rarely needed but matters in security-sensitive scripts | Performance & External Tools |  |  |  | ✓ |  |  | 1 |
| **Use `for item in "${arr[@]}"` (with quotes) when iterating over an array, not `for item in ${arr[@]}` or `for item in $arr`.** Preserves item boundaries | Control Flow & Idioms |  |  |  | ✓ |  |  | 1 |
| **Use `grep --` to separate flags from patterns, especially when patterns come from variables or input.** Prevents patterns like `-v` from being misinterpreted as flags | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Use `if [[ -v var ]]` to test whether a variable is set; use `if [[ -z "$var" ]]` to test whether it is empty.** Explicit; covers both cases correctly | Control Flow & Idioms |  |  |  | ✓ |  |  | 1 |
| **Use `local` for all function variables to avoid polluting the global scope.** Prevents subtle bugs from variable name collisions | Quoting & Variable Safety |  |  |  | ✓ |  |  | 1 |
| **Use `mv -i` or check `[[ -e "$target" ]]` before overwriting files in scripts that operate on user data.** Prevents accidental data loss | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Use `readonly` for variables that should not change after initialization.** Prevents accidental mutation; signals intent to readers | Structure & Initialization |  |  |  | ✓ |  |  | 1 |
| **Use `while read -r line; do | Control Flow & Idioms |  |  |  | ✓ |  |  | 1 |
| **Use `\|\| { echo "msg" >&2; exit 1; }` or a named `die` function rather than bare `exit`.** Errors without messages are unhelpful in logs | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Use a `main` function as the script's entry point.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Use a `while read` loop to process line-based data.** | Commands & Pipes |  |  |  |  | ✓ |  | 1 |
| **Use absolute paths for commands when called from cron or automation contexts where `PATH` may be unpredictable.** `/usr/bin/foo` beats `foo` when there is no guarantee about the environment | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Use descriptive exit codes: 0 for success, 1 for generic errors, >1 for specific failure types if the caller needs to distinguish them.** Aids debugging and automation | Style & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Use explicit error traps (`trap`) for cleanup (e.g., removing temporary files) and for context in debugging.** Ensures resources are released even if an error occurs; trap output aids diagnosis | Error Handling & Debugging |  |  |  | ✓ |  |  | 1 |
| **Use functions for any logic used more than once or longer than ~10 lines.** Inline pipelines past that length are unreadable | Structure |  |  | ✓ |  |  |  | 1 |
| **Use lowercase for your own variable names.** | Variables & Quoting |  |  |  |  | ✓ |  | 1 |
| **Use lowercase names for local variables and uppercase only for exported environment variables.** Matches long-standing Unix convention | Style |  |  | ✓ |  |  |  | 1 |
| **Use meaningful names: `temp_dir`, not `td`; `is_valid`, not `ok`.** Code is read far more often than written | Style & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Use temporary files and directories securely: `tmpdir=$(mktemp -d)` and `trap 'rm -rf "$tmpdir"' EXIT`.** Prevents predictable names and ensures cleanup; avoids race conditions | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **Validate and sanitize user input and command-line arguments; do not assume they are well-formed.** Input is the attack surface; scripts run in automation contexts where bad data is common | Safety & Defensive Practices |  |  |  | ✓ |  |  | 1 |
| **When a simple `set -e` is not sufficient (e.g., in conditionals or loops), use explicit `if` checks and call `error()`.** Makes failure modes visible in the code itself; does not rely on implicit error handling | Error Handling & Debugging |  |  |  | ✓ |  |  | 1 |
| **Wrap executable logic in a `main` function and call it with `main "$@"` at the bottom.** Makes the script sourceable for testing and gives a single entry point | Structure |  |  | ✓ |  |  |  | 1 |
| **Write comments for code that is complex, non-obvious, or has hidden dependencies.** | Style |  |  |  |  | ✓ |  | 1 |
| **Write scripts that are sourceable (guard `main` with `[[ "${BASH_SOURCE[0]}" == "$0" ]]`) so functions can be unit-tested.** Enables bats or shunit2 coverage | Testing & Debugging |  |  | ✓ |  |  |  | 1 |
| Add comments to explain non-obvious logic or decisions | Style |  |  |  |  |  | ✓ | 1 |
| Always double-quote variable expansions and command substitutions unless you need splitting or globbing | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Always quote variables in commands and expansions | Safety |  |  |  |  |  | ✓ | 1 |
| Audience: Engineers and AI coding assistants writing, reviewing, or generating shell scripts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid eval; never eval untrusted input | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid ignoring command errors with `\|\| true` (contested) | Error Handling |  |  |  |  |  | ✓ | 1 |
| Avoid trailing whitespace and ensure the file ends with a newline | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid unnecessary loops; use tools like `awk` or `sed` for bulk processing | Performance |  |  |  |  |  | ✓ | 1 |
| Avoid useless use of cat in single-process pipelines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid using `eval` or similar meta-programming | Safety |  |  |  |  |  | ✓ | 1 |
| Check that required external commands exist with command -v and fail fast | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Choose descriptive, lowercase-with-underscores variable names | Style |  |  |  |  |  | ✓ | 1 |
| Do check command exit statuses | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do handle signals gracefully | Safety |  | ✓ |  |  |  |  | 1 |
| Do limit line length to 80 characters | Structure |  | ✓ |  |  |  |  | 1 |
| Do not change IFS globally; set it locally for read only | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use Bash-only features in sh scripts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use pipefail in POSIX sh scripts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do structure code with functions | Structure |  | ✓ |  |  |  |  | 1 |
| Do use `#` comments to explain non-obvious code sections | Style |  | ✓ |  |  |  |  | 1 |
| Do use `set -e` at the beginning of scripts | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do use built-in Bash constructs over external commands | Performance |  | ✓ |  |  |  |  | 1 |
| Do use double quotes around variables | Style |  | ✓ |  |  |  |  | 1 |
| Do validate inputs | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t ignore errors in pipelines | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t include hard-coded paths | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t manipulate files without confirming they exist | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t use `eval` | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t use unnecessary subshells | Style |  | ✓ |  |  |  |  | 1 |
| End-to-end tests for non-trivial scripts (e.g., with bats) are strongly encouraged | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ensure executable scripts are executable and libraries are non-executable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Explicitly check the exit status of critical commands | Error Handling |  |  |  |  |  | ✓ | 1 |
| For commands expected to sometimes fail (e.g., grep), handle the non-zero exit explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Format scripts with shfmt using 2-space indentation, no tabs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Format with shfmt in CI and fail on drift | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If the file might be sourced or lacks a standard extension, add a top-of-file directive # shellcheck shell=bash or # shellcheck shell=sh | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If you use any Bash-only features, use a Bash shebang | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In Bash, enable set -euo pipefail (and set -E) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In Bash, prefer [[ … ]] over [ … ] for string tests | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In POSIX sh, do not enable options that the shell does not support; check command statuses explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In hot loops, prefer shell builtins over external processes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In sh, always quote string comparisons inside [ … ] | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a usage message or help function in every script | Structure |  |  |  |  |  | ✓ | 1 |
| Lint every script with shellcheck and fix or narrowly disable findings | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Organize code into small functions and call a main at the end | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Organize scripts into functions for modular code | Structure |  |  |  |  |  | ✓ | 1 |
| Pass -- before untrusted input to option-parsing commands (e.g., rm -- "$path") | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place one statement per line; avoid semicolons except after function declarations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer #!/usr/bin/env bash over hard-coded paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer Bash built-ins over external commands for common tasks | Performance |  |  |  |  |  | ✓ | 1 |
| Prefer POSIX sh when you don’t need Bash | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer find -exec … {} + over piping to xargs when feasible | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer long options over short where supported (e.g., grep --fixed-strings) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer printf over echo for data with escapes, leading dashes, or portability concerns | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put safety options at the top before other commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Quote all paths and globs in rm/mv/cp and similar commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Read lines with while IFS= read -r …; do …; done, not for x in $(cat file) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return or exit with explicit non-zero codes on failure paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Bash and POSIX sh scripts used in production ops tooling, CI pipelines, and local developer workflows where portability, safety, and quoting matter | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set `set -euo pipefail` at the start of every script | Error Handling |  |  |  |  |  | ✓ | 1 |
| Start every script with a shebang that matches the features you use | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use "$@" to forward argument lists; never use $* | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use $(…) for command substitution, not backticks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use a shebang line at the top of every script | Structure |  |  |  |  |  | ✓ | 1 |
| Use absolute paths for commands and files when possible | Safety |  |  |  |  |  | ✓ | 1 |
| Use consistent four-space indentation throughout the script | Style |  |  |  |  |  | ✓ | 1 |
| Use grep -F for fixed-string matches by default | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use local for function-scoped variables in Bash | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use snake_case for variables and functions; reserve UPPER_SNAKE for environment and constants | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use trap to clean up temporary files and handle INT/TERM/EXIT | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate all user inputs before processing | Safety |  |  |  |  |  | ✓ | 1 |
| When handling many paths, use find -print0 \| xargs -0 or find -exec … {} + | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

