## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Include YAML frontmatter with required metadata keys. | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Never hardcode secrets, credentials, or sensitive values in commands. | Safety | ✓ | ✓ | ✓ |  | ✓ | ✓ | 5 |
| Validate argument inputs before use. | Arguments | ✓ | ✓ |  | ✓ | ✓ | ✓ | 5 |
| Keep each command focused on a single primary purpose. | Structure | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Quote interpolated variables in shell to prevent injection/word-splitting. | Safety | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Require confirmation (or dry-run gating) before destructive/mutating actions. | Safety | ✓ | ✓ |  | ✓ | ✓ |  | 4 |
| Start bash blocks with `set -euo pipefail` (or equivalent strict mode). | Actions & Shell | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Use kebab-case filenames matching the command name. | Naming | ✓ |  | ✓ |  | ✓ |  | 3 |
| Include a Usage section with concrete invocation example. | Structure | ✓ |  |  |  |  | ✓ | 2 |
| Include at least one end-to-end example of desired output. | Style & Readability | ✓ |  | ✓ | ✓ |  |  | 3 |
| Keep command bodies/scripts short; extract long logic to external scripts. | Structure/Scripting | ✓ |  | ✓ |  | ✓ |  | 3 |
| Keep the description to a single short sentence. | Structure | ✓ |  | ✓ | ✓ |  |  | 3 |
| Declare each argument with name, type, and description in frontmatter. | Arguments | ✓ |  |  | ✓ |  | ✓ | 3 |
| Bound/scope file operations; avoid unscoped repo-wide scans. | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Write prompts in imperative mood addressing Claude directly. | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Provide clear, actionable error messages on failure. | Error Handling |  | ✓ |  | ✓ |  | ✓ | 3 |
| Keep lines under a fixed character limit (80–120). | Style | ✓ |  |  |  |  | ✓ | 2 |
| Reference only declared arguments; no undeclared placeholders. | Arguments | ✓ |  |  |  |  |  | 1 |
| Use enums/choice types for constrained argument values. | Arguments | ✓ |  |  | ✓ |  |  | 2 |
| Declare `allowed-tools` / restrict tool scope for commands with side effects. | Safety |  |  | ✓ |  |  | ✓ | 2 |
| Never interpolate raw arguments directly into shell preludes. | Safety |  |  | ✓ |  |  | ✓ | 2 |
| Do not fetch remote content (curl/wget) inside preludes. | Safety |  |  | ✓ |  |  |  | 1 |
| Limit the number of shell preludes per command. | Performance |  |  | ✓ |  |  |  | 1 |
| Put `.claude/commands/` under CODEOWNERS / treat as reviewed source. | Ownership |  |  | ✓ |  |  |  | 1 |
| Avoid persona preambles in prompts. | Style |  |  | ✓ |  |  |  | 1 |
| Include semantic version in frontmatter. | Lifecycle | ✓ |  |  |  |  |  | 1 |
| Include an owner field in frontmatter. | Lifecycle | ✓ |  |  |  |  |  | 1 |
| Include `last_reviewed` date and re-review periodically. | Lifecycle | ✓ |  |  |  |  |  | 1 |
| Declare environment/tool requirements in frontmatter. | Portability | ✓ |  |  | ✓ |  |  | 2 |
| Use `bash` or `sh` language identifiers on shell code fences. | Portability | ✓ |  |  |  |  |  | 1 |
| Prefer POSIX-compatible shell features where practical. | Portability | ✓ |  |  |  |  |  | 1 |
| Preflight-check for required external tools before use. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Make actions idempotent where practical. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Don't use `sudo` inside command blocks. | Safety | ✓ |  |  |  |  |  | 1 |
| Don't use `~` in paths; use repo-relative or absolute paths. | Safety | ✓ |  |  |  |  |  | 1 |
| Prefer named arguments over positional in usage examples. | Arguments | ✓ |  |  |  |  |  | 1 |
| Use domain prefixes to namespace related commands. | Naming | ✓ |  |  |  |  |  | 1 |
| State success criteria/expected outputs in the prompt. | Prompt Content | ✓ |  |  | ✓ |  |  | 2 |
| Redact secrets from logs/outputs. | Safety | ✓ |  |  |  |  |  | 1 |
| Limit command structure nesting depth. | Structure |  | ✓ |  |  |  | ✓ | 2 |
| Use consistent markdown formatting across command files. | Style |  | ✓ |  |  |  | ✓ | 2 |
| Don't mix programming paradigms in a single command. | Style |  | ✓ |  |  |  |  | 1 |
| Limit external API calls within commands. | Performance |  | ✓ |  |  |  |  | 1 |
| Don't include unnecessary computation in command execution. | Performance |  | ✓ |  |  |  | ✓ | 2 |
| Provide clear documentation within each command file. | Structure |  | ✓ |  |  |  |  | 1 |
| Prefer positional `$1`/`$2` over `$ARGUMENTS` when arity is fixed. | Arguments |  |  | ✓ |  |  |  | 1 |
| Put the task statement/ask in the first few lines of the prompt body. | Style |  |  | ✓ |  |  |  | 1 |
| Use fenced code blocks for literal strings Claude must emit. | Style |  |  | ✓ |  |  |  | 1 |
| Don't duplicate guidance already in CLAUDE.md. | Structure |  |  | ✓ |  |  |  | 1 |
| Include an H1 title that equals the command name. | Structure | ✓ |  |  |  |  |  | 1 |
| Prefer git plumbing over porcelain in preludes. | Shell Preludes |  |  | ✓ |  |  |  | 1 |
| Fail loudly in preludes with a clear message. | Shell Preludes |  |  | ✓ |  |  |  | 1 |
| Don't use preludes for data Claude can retrieve on demand. | Shell Preludes |  |  | ✓ |  |  |  | 1 |
| Commit shared commands to the repo; keep personal ones per-user. | Repo Hygiene |  |  | ✓ |  |  |  | 1 |
| Remove stale/unused commands periodically. | Repo Hygiene |  |  | ✓ |  |  |  | 1 |
| Include full file/scope context when the command modifies code. | Prompt Content |  |  |  | ✓ |  |  | 1 |
| Don't rely on Claude to infer style/convention; state it explicitly. | Prompt Content |  |  |  | ✓ |  |  | 1 |
| Avoid asking Claude to do multiple distinct tasks in one command. | Prompt Content |  |  |  | ✓ |  |  | 1 |
| Warn users upfront about slow-running commands. | Performance |  |  |  | ✓ |  |  | 1 |
| Prefer a single batched Claude request over many sequential calls. | Performance |  |  |  | ✓ |  |  | 1 |
| Cache expensive computations across invocations. | Performance |  |  |  | ✓ |  | ✓ | 2 |
| Maintain a changelog / version notes for behavior changes. | Maintenance |  |  |  | ✓ |  |  | 1 |
| Don't leave hardcoded paths/URLs in commands. | Maintenance |  |  |  | ✓ |  |  | 1 |
| Document external dependencies used by the command. | Maintenance |  |  |  | ✓ |  |  | 1 |
| Provide a dry-run/test mode with no side effects. | Safety |  |  |  | ✓ |  |  | 1 |
| Don't auto-commit/push/merge command output. | Safety |  |  |  | ✓ |  |  | 1 |
| Show diff or summary of changes before finalizing. | Safety |  |  |  | ✓ |  |  | 1 |
| Restrict commands to the project scope (no writes to system dirs). | Safety |  |  |  | ✓ |  |  | 1 |
| Don't silently mutate global state (env, cwd); restore if changed. | Safety |  |  |  | ✓ |  |  | 1 |
| Use safeguards around glob expansion to bound match sets. | Safety |  |  |  | ✓ |  |  | 1 |
| Include few-shot examples to guide output format. | Prompt Content |  |  |  |  | ✓ |  | 1 |
| Use descriptive snake_case argument names. | Arguments |  |  |  |  | ✓ |  | 1 |
| Validate all shell scripts with `shellcheck`. | Safety |  |  |  |  | ✓ |  | 1 |
| Avoid unrecoverable operations (`rm -rf`, `git reset --hard`). | Safety |  |  |  |  | ✓ |  | 1 |
| Use descriptive, meaningful command names. | Naming |  | ✓ |  |  |  |  | 1 |
| Prefix argument names with the command name to avoid conflicts. | Style |  |  |  |  |  | ✓ | 1 |
| Default scripted side effects to read-only; require opt-in for writes. | Safety |  |  |  |  |  | ✓ | 1 |
| Validate paths/arguments of any external commands invoked. | Safety |  |  |  |  |  | ✓ | 1 |

## Notes on clustering decisions

- **"Confirmation before destructive actions" vs. "dry_run default"**: I merged gpt-5's `dry_run` default + confirmation rules with haiku's "require explicit confirmation for destructive ops" and 4o-mini's "confirmation prompts." These are different mechanisms (a declarative flag vs. an interactive prompt) but address the same intent. A stricter matcher would split them.
- **"Never embed secrets"**: merged across models even though phrasings vary from "don't hardcode credentials" to "never embed secrets." Grok's "don't leave hardcoded paths/URLs" is listed separately since it's about maintainability/config, not secrets — but a lenient matcher might merge them.
- **"One command, one purpose"**: merged gpt-5's "Keep one primary purpose," 4o-mini's "Don't exceed three layers," opus's "One command does one thing," haiku's "don't do multiple tasks in one command" (partially — I also kept that one as a separate prompt-content rule), and grok's "limit to a single primary workflow." 4o-mini's is arguably about nesting depth rather than single-purpose; I put it in the separate "limit nesting" cluster too.
- **"Include example(s)"**: I conflated gpt-5's "Examples section," opus's "concrete example of desired output," and haiku's "at least one worked example." Gemini's "few-shot examples in prompts" is listed separately because it's about prompt engineering inside the body, not a user-facing Examples section — though a loose matcher would merge them.
- **"Bound file operations / avoid repo-wide scans"**: merged gpt-5's "scope file operations," opus's "don't recurse filesystem scans" and "bound prelude output," and haiku's "glob safeguards." These are related but not identical (output bounding vs. scope limiting vs. glob guards). A strict matcher would split into 2–3 rules.
- **"Validate arguments"**: merged a broad cluster — gpt-5's "validate argument values," 4o-mini's "validate user input thoroughly," haiku's "validate arguments before passing to Claude/shell," gemini's "validate paths/enums," and grok's "explicit error checks for arguments." All are argument validation in substance.
- **"Imperative prompt style"**: gpt-5 has "active voice and imperative mood" (style), opus has "write prompt in imperative addressed to Claude," haiku has "write prompts in imperative mood." Merged despite gpt-5's framing being about descriptions broadly.
- **Haiku's "don't ask Claude to do multiple distinct tasks"** vs. the general "one command, one purpose" cluster: I kept these separate because haiku's is specifically about prompt construction within a command, while the other is about command file scope. A lenient matcher would merge.
- **Opus's `allowed-tools` rules**: opus has three distinct rules (declare it, scope Bash allowlists narrowly, don't interpolate args into preludes). I kept them as separate rows; grok's "validate paths of external commands" partially overlaps with the Bash-scoping rule and I mapped it to a distinct row.
- **"Cache expensive computations"**: grok and haiku both mention caching; merged despite haiku marking it contested and grok not.
- **4o-mini's "consistent markdown formatting"** and grok's "consistent markdown headings + indent code blocks" were merged; they overlap in substance even if specifics differ.