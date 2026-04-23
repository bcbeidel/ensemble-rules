## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Always double-quote variable expansions to prevent word splitting and globbing. | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Enable `set -euo pipefail` at the top of Bash scripts. | Error Handling | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Avoid `eval`, especially on untrusted input. | Safety | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Organize logic into functions with a `main` entry point. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Start every script with an explicit shebang. | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Use `$(...)` for command substitution instead of backticks. | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use `local` for function-scoped variables. | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use `trap` to clean up temp files/resources on exit. | Error Handling | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use `mktemp` for temporary files/directories. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use `[[ ... ]]` over `[ ... ]` for tests in Bash. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use `while IFS= read -r` to process lines, not `for x in $(cat file)`. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Check that required external commands exist before use. | Error Handling | ✓ |  | ✓ | ✓ |  |  | 3 |
| Lint scripts with ShellCheck (and treat findings as errors). | Tooling | ✓ |  | ✓ |  |  |  | 2 |
| Prefer `printf` over `echo` for non-trivial output. | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use `"$@"` (quoted) to forward arguments, not `$*`. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Avoid parsing the output of `ls`. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Avoid useless use of `cat` in pipelines. | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use `find -print0 | xargs -0` or `-exec ... +` for filename-safe iteration. | Safety | ✓ |  |  | ✓ |  |  | 2 |
| Prefer shell builtins over external processes in hot loops. | Performance | ✓ |  |  | ✓ |  | ✓ | 3 |
| Validate and sanitize user inputs. | Safety |  | ✓ |  | ✓ |  | ✓ | 3 |
| Use consistent indentation (spaces, not tabs). | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Set `IFS=$'\n\t'` after enabling strict mode. | Error Handling |  |  | ✓ | ✓ |  |  | 2 |
| Use lowercase names for local variables; uppercase for exported/env. | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Print error/diagnostic messages to stderr (and/or use a `die`/`error` helper). | Error Handling |  |  | ✓ | ✓ | ✓ |  | 3 |
| Limit line length (≤80–100 chars). | Style |  | ✓ |  | ✓ | ✓ |  | 3 |
| Add comments explaining intent / non-obvious logic. | Style |  | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Keep scripts small; rewrite complex logic in a real language. | Structure |  |  | ✓ | ✓ |  |  | 2 |
| Declare invariant config as `readonly` at the top. | Structure | ✓ |  | ✓ | ✓ |  |  | 3 |
| Verify `cd` succeeded before relying on it. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Exit with explicit non-zero codes on failure paths. | Error Handling | ✓ |  |  | ✓ | ✓ |  | 3 |
| Check command exit statuses explicitly where `set -e` is insufficient. | Error Handling | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Use braces in variable expansions (`"${var}"`). | Style |  |  |  | ✓ | ✓ |  | 2 |
| Avoid GNU-specific flags without declaring dependencies. | Portability | ✓ |  | ✓ |  |  |  | 2 |
| Format scripts with shfmt (or enforce format in CI). | Tooling | ✓ |  |  |  |  |  | 1 |
| Ensure scripts end with a newline and no trailing whitespace. | Style | ✓ |  |  |  |  |  | 1 |
| Prefer long options over short options. | Style | ✓ |  |  |  |  |  | 1 |
| Ensure executable vs sourced files have correct mode bits. | Tooling | ✓ |  |  |  |  |  | 1 |
| Use `# shellcheck shell=` directive when there's no shebang. | Tooling | ✓ |  |  |  |  |  | 1 |
| Write end-to-end / unit tests (bats/shunit2) for non-trivial scripts. | Tooling | ✓ |  | ✓ |  |  |  | 2 |
| Pass `--` before untrusted input to option-parsing commands. | Safety | ✓ |  |  | ✓ |  |  | 2 |
| Prefer parameter expansion over external tools for simple string ops. | Performance |  |  | ✓ |  |  |  | 1 |
| Do not change IFS globally. | Safety | ✓ |  |  |  |  |  | 1 |
| Include a header/usage comment documenting purpose and usage. | Structure |  |  |  | ✓ | ✓ | ✓ | 3 |
| Place safety options before any other commands. | Structure | ✓ |  |  |  |  |  | 1 |
| Support a debug/trace mode (e.g., `set -x` via `DEBUG=1`). | Testing |  |  | ✓ |  |  |  | 1 |
| Guard `main` so the script is sourceable for testing. | Testing |  |  | ✓ |  |  |  | 1 |
| Use `grep -q` for existence checks instead of redirecting output. | Style |  |  |  | ✓ |  |  | 1 |
| Use `grep --` to separate flags from user-supplied patterns. | Safety |  |  |  | ✓ |  |  | 1 |
| Prefer explicit `if/then/else` over `&&`/`||` chains. | Style |  |  |  | ✓ |  |  | 1 |
| Quote array expansions as `"${arr[@]}"`. | Safety |  |  |  | ✓ |  |  | 1 |
| Use `${var:-default}` / `${var:?msg}` for optional/required vars. | Safety |  |  |  | ✓ |  |  | 1 |
| Pin locale with `LC_ALL=C` when semantics depend on it. | Portability |  |  | ✓ |  |  |  | 1 |
| Never pass secrets as command-line arguments. | Safety |  |  | ✓ |  |  |  | 1 |
| Use absolute paths for commands in cron/automation contexts. | Safety |  |  |  | ✓ |  | ✓ | 2 |
| Prefer `command` prefix to avoid alias/function shadowing. | Safety |  |  |  | ✓ |  |  | 1 |
| Keep functions small / avoid deeply nested conditionals. | Style |  |  |  | ✓ |  |  | 1 |
| Use `mv -i` or check existence before overwriting user files. | Safety |  |  |  | ✓ |  |  | 1 |
| Avoid unnecessary subshells. | Performance |  | ✓ |  |  |  |  | 1 |
| Handle signals gracefully / clean up on interruption. | Safety |  | ✓ | ✓ | ✓ |  |  | 3 |
| Don't hard-code paths; use relative paths or config variables. | Structure |  | ✓ |  |  |  |  | 1 |
| Pick one shell dialect per script and don't mix (e.g., no bashisms in sh). | Portability | ✓ |  | ✓ |  |  |  | 2 |
| Prefer `#!/usr/bin/env bash` over hard-coded interpreter path. | Portability | ✓ |  |  |  |  |  | 1 |
| Use descriptive / consistent exit codes. | Error Handling |  |  |  | ✓ |  |  | 1 |
| Prefer POSIX sh when Bash features aren't needed. | Portability | ✓ |  |  | ✓ |  |  | 2 |

## Notes on clustering decisions

- **"Enable `set -euo pipefail`"** consolidates several variants: gpt-5's separate rules about errexit/nounset/pipefail, grok's single combined rule, and opus/haiku's "start with `set -euo pipefail`". The three flags are treated as one rule because every model that mentioned one mentioned the bundle.
- **"Check command exit statuses explicitly where `set -e` is insufficient"** merges gpt-4o-mini's generic "check exit statuses", gpt-5's "handle expected-failure commands explicitly", opus's "don't rely solely on set -e", haiku's rule 9 (explicit `if` checks), and grok's "explicitly check exit status". These range from "always check" to "check where strict mode doesn't help" — clustered together despite the contested framing differences.
- **"Use `[[ ... ]]` over `[ ... ]`"** — gpt-5 and haiku also recommend using `[ ]` in POSIX sh; I clustered the "prefer `[[`" advice regardless of the POSIX caveat since the core preference is the same.
- **"Use consistent indentation"** bundles gpt-5 (2-space shfmt), opus (2/4-space, not mixed), haiku (2-space), gemini (2-space). Different specific widths but same underlying rule.
- **"Lowercase local / uppercase env"** clustered across gpt-5, opus, haiku, gemini despite gemini marking part of it contested.
- **"Avoid useless use of `cat`"** — clustered gpt-5, opus, haiku even though gpt-5 marks it contested.
- **"Handle signals gracefully"** (gpt-4o-mini) was clustered with trap-based cleanup rules from opus/haiku since gpt-4o-mini's phrasing is vague but overlaps in substance. A stricter reading would separate them.
- **"Prefer shell builtins over externals"** merged gpt-5's "in hot loops", haiku's rule 40, and grok's "prefer builtins". Slightly different scope (hot loops vs general) but same principle.
- **"Include header/usage comment"** — gemini's "header comment with purpose/usage", haiku's "comment block explaining purpose", and grok's "include a usage/help function" were clustered. Grok's is arguably a separate rule (a `usage()` function vs. a comment) but the intent (documented entry point) is close enough.
- **Print errors to stderr / use `die` helper** — opus's `die` function rule and gemini's stderr rule and haiku's `error()` function rule were merged; they're distinct mechanisms but serve the same purpose.
- **"Validate user input"** — gpt-4o-mini, haiku, grok all phrased this generically; clustered together despite different levels of specificity.
- **gpt-5's "Do not use pipefail in POSIX sh"** and **"Do not use Bash features in sh"** were folded into the single "pick one dialect" cluster with opus's rule, since they're instances of the same underlying constraint.
- **"Avoid parsing `ls`"** from gpt-5 is implied (via the "for x in $(cat)" rule and filename-safety rules) but not stated as a separate rule; I gave it a ✓ only where explicitly called out (opus, haiku, gemini).