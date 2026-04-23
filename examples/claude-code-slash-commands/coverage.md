# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Cache expensive computations (e.g., AST parsing, file indexing) across repeated invocations.** Improves user experience but adds state management complexity | Performance and Efficiency |  |  |  | ✓ |  |  | 1 |
| **(contested) Embed validation scripts in the command file itself (as a shebang or pre-prompt block) rather than relying on external tools.** Keeps the command self-contained and reduces hidden dependencies, but adds complexity; teams with strong CI/linting can skip this | Side Effects and Scripting |  |  |  | ✓ |  |  | 1 |
| **(contested) Extract logic exceeding ~15 lines into external, version-controlled scripts.** | Scripting |  |  |  |  | ✓ |  | 1 |
| **All side effects (modifying files, running commands, setting environment) must be explicit and guarded.** Document what gets written, where, and under what conditions | Side Effects and Scripting |  |  |  | ✓ |  |  | 1 |
| **Always quote variables and arguments in shell scripts.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Avoid commands with unrecoverable side effects (e.g., `rm -f`, `git reset --hard`).** | Safety |  |  |  |  | ✓ |  | 1 |
| **Avoid jargon, abbreviations, and acronyms unless they are standard in your codebase.** A teammate should not need to ask what a flag or parameter means | Style and Readability |  |  |  | ✓ |  |  | 1 |
| **Avoid persona preambles ("You are a senior engineer...").** They waste tokens without measurably improving output | Style |  |  | ✓ |  |  |  | 1 |
| **Avoid prompts that ask Claude to preserve or maintain existing code patterns without providing examples.** ("Keep the same error handling style" is vague; "Use the try-catch blocks with a `logError(err)` call, like in lines 20–30." is clear.) | Prompting |  |  |  | ✓ |  |  | 1 |
| **Avoid prompts that require Claude to maintain global consistency across multiple files without explicit instruction.** Claude's consistency degrades with scope; if you need consistency, provide a lint rule or formatter command, don't rely on aesthetic inference | Prompting |  |  |  | ✓ |  |  | 1 |
| **Begin all bash scripts with `set -euo pipefail`.** | Scripting |  |  |  |  | ✓ |  | 1 |
| **Begin every command file with a YAML front matter block containing `name`, `description`, and `arguments`.** Users and automation need to know what the command does before reading prose | Structure and Metadata |  |  |  | ✓ |  |  | 1 |
| **Bound every prelude's output (`\| head`, `--max-count`, `--stat`).** Unbounded output blows out context and slows the turn | Shell Preludes |  |  | ✓ |  |  |  | 1 |
| **Catch foreseeable error conditions (missing file, invalid argument, empty selection) and output a clear, actionable error message.** An error message should tell the user what went wrong and how to fix it | Error Handling and User Communication |  |  |  | ✓ |  |  | 1 |
| **Commands that modify code should show a diff or summary of changes before finalizing.** Users need confidence that the output is correct | Safety and Guardrails |  |  |  | ✓ |  |  | 1 |
| **Commit `.claude/commands/` to the repo for team commands; keep personal experiments in `~/.claude/commands/`.** Mixing them creates "works on my machine" reviews | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Declare `allowed-tools` in frontmatter for any command with shell preludes or write intent.** The default is too permissive for shared commands | Safety |  |  | ✓ |  |  |  | 1 |
| **Define every argument as an object with `name`, `type` (string, number, boolean, choice, or path), and `description`.** Optional arguments must explicitly set `required: false` | Structure and Metadata |  |  |  | ✓ |  |  | 1 |
| **Define one command per file.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Define what success looks like.** ("The file is reformatted and git-staged." not "The command ran without errors.") | Error Handling and User Communication |  |  |  | ✓ |  |  | 1 |
| **Do not ask Claude to do multiple distinct tasks in a single command if they might have different outcomes.** ("Find performance issues and suggest fixes" is okay; "Find performance issues, add comments, and refactor the API" should be two commands.) | Prompting |  |  |  | ✓ |  |  | 1 |
| **Do not ask Claude to infer intent from style or convention; state it explicitly.** ("Follow the existing naming convention: `camelCase` for functions." not "Use the style you see in this file.") | Prompting |  |  |  | ✓ |  |  | 1 |
| **Do not automatically commit, push, or merge the output of a command.** Always leave that to the user | Safety and Guardrails |  |  |  | ✓ |  |  | 1 |
| **Do not duplicate guidance already in `CLAUDE.md`.** Link to it or rely on it; duplication drifts | Structure |  |  | ✓ |  |  |  | 1 |
| **Do not fetch remote content in preludes (`!curl`, `!wget`).** Network fetches in preludes are supply-chain risk and non-reproducible | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not include commented-out code, alternative prompts, or TODOs in the published command file.** Those belong in a separate draft or issue, not in the production rules file | Style and Readability |  |  |  | ✓ |  |  | 1 |
| **Do not leave hardcoded paths, URLs, or config values in the command.** Use variables, environment, or arguments | Maintenance and Documentation |  |  |  | ✓ |  |  | 1 |
| **Do not let exceptions or error traces bubble up uncaught; wrap them in a user-friendly message.** Users should never see a Python traceback or cryptic shell error | Error Handling and User Communication |  |  |  | ✓ |  |  | 1 |
| **Do not make assumptions about the user's environment (OS, shell, tool versions).** If a command depends on `bash` 4.0+, a Rust toolchain, or a specific Node version, check for it and fail gracefully | Safety and Guardrails |  |  |  | ✓ |  |  | 1 |
| **Do not modify global state (environment variables, working directory, shell history) unless documented and necessary.** If the command must change directory, restore it at the end | Side Effects and Scripting |  |  |  | ✓ |  |  | 1 |
| **Do not modify uncommitted changes in the user's working directory; write to a new branch, temporary file, or explicitly confirmed location.** Users' uncommitted work is sacred and should never be silently overwritten | Side Effects and Scripting |  |  |  | ✓ |  |  | 1 |
| **Do not recurse filesystem scans in preludes (`find .`, `grep -r` without a path).** Use `rg` with a scope or let Claude search on demand | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not spawn multiple Claude requests in a single command without strong justification.** Each request adds latency and cost; if the task fits in one well-structured prompt, do that instead | Performance and Efficiency |  |  |  | ✓ |  |  | 1 |
| **Do not use preludes for data Claude can retrieve on demand.** Preludes run every invocation; tool calls run only when needed | Shell Preludes |  |  | ✓ |  |  |  | 1 |
| **Do not use shell glob expansion (`*.js`) in commands without explicit safeguards.** A glob that expands to thousands of files can cause the command to fail or timeout | Side Effects and Scripting |  |  |  | ✓ |  |  | 1 |
| **Do not write to system directories or outside the current project.** Commands should be isolated to the repo | Safety and Guardrails |  |  |  | ✓ |  |  | 1 |
| **Document any external dependencies (tools, libraries, permissions).** If the command requires a Python interpreter, linter, or API key, state it upfront | Maintenance and Documentation |  |  |  | ✓ |  |  | 1 |
| **Document the argument contract at the top of the body (`Usage: /cmd <ticket-id>`).** Users read the file when things break | Arguments |  |  | ✓ |  |  |  | 1 |
| **Fail loudly in preludes with a clear message (`\|\| echo "ERROR: ..."`).** Silent empty output produces silent wrong answers | Shell Preludes |  |  | ✓ |  |  |  | 1 |
| **For commands that generate or delete files, require explicit confirmation (a `--force` flag or user prompt) if the operation is destructive.** Users should never lose work by accident | Safety and Guardrails |  |  |  | ✓ |  |  | 1 |
| **Give every command a `description` field in YAML frontmatter.** It populates the command picker; without it the command is unusable in practice | Structure |  |  | ✓ |  |  |  | 1 |
| **Handle potential errors and provide meaningful error messages.** | Scripting |  |  |  |  | ✓ |  | 1 |
| **If a command processes multiple files, process them in a single Claude request (with all files in context) rather than invoking Claude for each file.** Batching is faster and produces more consistent output | Performance and Efficiency |  |  |  | ✓ |  |  | 1 |
| **If a command takes more than ~10 seconds to run, indicate that to the user upfront.** ("This command will scan all files and may take 30 seconds.") Users expect fast feedback in an IDE; a slow command without warning feels broken | Performance and Efficiency |  |  |  | ✓ |  |  | 1 |
| **If the command might produce unexpected output, prompt the user to review and confirm before making changes.** This is especially important for commands that delete or overwrite code | Error Handling and User Communication |  |  |  | ✓ |  |  | 1 |
| **Include at least one worked example showing input and expected output.** Ambiguity in the example often reveals ambiguity in the command itself | Style and Readability |  |  |  | ✓ |  |  | 1 |
| **Include few-shot examples in prompts to guide the AI's output format.** | Content & Prompting |  |  |  |  | ✓ |  | 1 |
| **Include one concrete example of desired output when the format is non-obvious.** Few-shot beats description for structured output | Style |  |  | ✓ |  |  |  | 1 |
| **Include the full file or relevant scope in the prompt context if the command modifies code.** A snippet without surrounding context often leads Claude to generate code that doesn't integrate | Prompting |  |  |  | ✓ |  |  | 1 |
| **Instruct the model to confirm before destructive actions (deletes, force-pushes, migrations).** Prompts must include an explicit "ask first" clause for irreversible steps | Safety |  |  | ✓ |  |  |  | 1 |
| **Keep `description` to a single sentence (≤80 chars).** Longer descriptions belong in the body; the description is a summary for command lists and help output | Structure and Metadata |  |  |  | ✓ |  |  | 1 |
| **Keep `description` to one sentence under 80 characters.** The picker truncates; be the one who chose where | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep command bodies under ~100 lines.** Longer prompts stop being reviewed and start being copy-pasted | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep embedded scripts short and focused.** | Scripting |  |  |  |  | ✓ |  | 1 |
| **Limit total prelude count to 3 per command.** Each one is a synchronous shell round-trip before the model speaks | Performance |  |  | ✓ |  |  |  | 1 |
| **List arguments in the order they appear in the prompt or are most likely to be specified.** Users invoke `/cmd arg1 arg2`, not `/cmd arg2 arg1` | Structure and Metadata |  |  |  | ✓ |  |  | 1 |
| **Maintain a changelog or version notes if the command's behavior or arguments change.** Users relying on the command in scripts or workflows need to know what changed | Maintenance and Documentation |  |  |  | ✓ |  |  | 1 |
| **Name command files descriptively using `kebab-case.md`.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Never interpolate `$ARGUMENTS`, `$1`, etc | Safety |  |  | ✓ |  |  |  | 1 |
| **One command does one thing.** Split `/release` into `/release-notes`, `/release-tag`, `/release-publish` rather than a mode flag | Structure |  |  | ✓ |  |  |  | 1 |
| **Prefer `$1`, `$2` over `$ARGUMENTS` when the command takes a fixed arity.** Positional slots document the contract; `$ARGUMENTS` hides it | Structure |  |  | ✓ |  |  |  | 1 |
| **Prefer `git` plumbing over parsing `git` porcelain.** `git rev-parse`, `git diff --name-only` are stable; `git status` text is not | Shell Preludes |  |  | ✓ |  |  |  | 1 |
| **Prompt for confirmation before executing any destructive or high-impact operation.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Provide a way to test or dry-run the command without side effects.** A `--dry-run` flag or example invocation reduces fear of breaking things | Maintenance and Documentation |  |  |  | ✓ |  |  | 1 |
| **Put `.claude/commands/` under CODEOWNERS.** Prompts that run shell deserve the same review gate as CI config | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Put the task statement in the first 3 lines of the body.** Context and constraints follow; the ask comes first | Style |  |  | ✓ |  |  |  | 1 |
| **Reject `$ARGUMENTS` concatenated into paths without sanitization guidance.** `read $ARGUMENTS/config.json` is how you read `/etc/passwd` | Arguments |  |  | ✓ |  |  |  | 1 |
| **Remove commands that have not been invoked in 90 days.** Stale commands mislead more than they help | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Require read-only preludes unless the command's purpose is to mutate.** `git status` is fine; `git push` belongs in a command explicitly named for it | Safety |  |  | ✓ |  |  |  | 1 |
| **Scope `Bash(...)` allowlists to specific subcommands, e.g | Safety |  |  | ✓ |  |  |  | 1 |
| **Separate the prompt and script into distinct, labeled markdown sections.** | Structure |  |  |  |  | ✓ |  | 1 |
| **State expected arguments explicitly in the prompt body.** Name each `$1`, `$2`, describe its shape, and say what to do when missing | Structure |  |  | ✓ |  |  |  | 1 |
| **Use Markdown headers and whitespace to organize the command file logically: Description, Arguments, Behavior, Prompt, Side Effects, Examples.** Readers should be able to scan the file and understand the command in 30 seconds | Style and Readability |  |  |  | ✓ |  |  | 1 |
| **Use YAML frontmatter for metadata.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Use `choice` type with an explicit `choices` array for enumerated arguments, not free-form strings.** Prevents ambiguous input like `/refactor style=prettier` where the intended choice is unclear | Structure and Metadata |  |  |  | ✓ |  |  | 1 |
| **Use `set -e` at the head of any embedded bash and fail loudly if a command fails.** Silent failures (e.g., a file write that silently fails) are invisible until much later | Side Effects and Scripting |  |  |  | ✓ |  |  | 1 |
| **Use descriptive, `snake_case` names for arguments.** | Content & Prompting |  |  |  |  | ✓ |  | 1 |
| **Use fenced code blocks for literal strings Claude must emit or match.** Prose descriptions of required output drift; examples don't | Style |  |  | ✓ |  |  |  | 1 |
| **Use kebab-case filenames matching the invocation (`review-pr.md` → `/review-pr`).** Anything else confuses users scanning `.claude/commands/` | Structure |  |  | ✓ |  |  |  | 1 |
| **Validate all shell scripts with `shellcheck`.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Validate argument presence in the prompt, not the shell.** Let Claude ask the user rather than dying with a shell error | Arguments |  |  | ✓ |  |  |  | 1 |
| **Validate arguments before passing them to Claude or into shell commands.** Check that paths exist, enums are valid, and numbers are in expected ranges; fail loudly with a helpful message | Side Effects and Scripting |  |  |  | ✓ |  |  | 1 |
| **Write a clear and concise `description` in the frontmatter.** | Content & Prompting |  |  |  |  | ✓ |  | 1 |
| **Write prompts in imperative mood, addressing Claude directly.** ("Refactor this function for readability." not "The function should be refactored…") | Prompting |  |  |  | ✓ |  |  | 1 |
| **Write prompts that are explicit and provide clear constraints.** | Content & Prompting |  |  |  |  | ✓ |  | 1 |
| **Write the prompt in the imperative, addressed to Claude.** "Analyze the diff and..." beats "This command will analyze..." | Style |  |  | ✓ |  |  |  | 1 |
| Audience: Engineers and AI coding assistants authoring, reviewing, or running commands in shared repos | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid positional arguments; require name=value pairs in usage examples | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Check for required tools before use (e.g., command -v jq >/dev/null) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare environment assumptions in front matter requires (e.g., os, tools with minimal versions) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare every argument in front matter args with name, type, required, and optional default | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default to no side effects: include a boolean dry_run argument with default true for any command that can mutate state | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do allow an optional scripting feature for advanced users (contested) | Contested |  | ✓ |  |  |  |  | 1 |
| Do cache results of repeatable computations in workflows where possible | Performance |  |  |  |  |  | ✓ | 1 |
| Do define a fallback behavior, such as logging an error and aborting, for any scripted side effects that could fail | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do implement confirmation prompts for destructive actions | Safety |  | ✓ |  |  |  |  | 1 |
| Do include a dedicated "Usage" section immediately after front matter to show invocation examples | Structure |  |  |  |  |  | ✓ | 1 |
| Do include explicit error checks for all user-provided arguments in the workflow | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do keep lines under 80 characters in code blocks | Style |  |  |  |  |  | ✓ | 1 |
| Do limit each command file to a single primary workflow; split complex ones into multiple files | Structure |  |  |  |  |  | ✓ | 1 |
| Do limit external API calls within commands | Performance |  | ✓ |  |  |  |  | 1 |
| Do provide clear documentation within each command file | Structure |  | ✓ |  |  |  |  | 1 |
| Do restrict scripted side effects to read-only operations by default; require explicit opt-in for writes | Safety |  |  |  |  |  | ✓ | 1 |
| Do sanitize all user inputs for scripted side effects, using escaping or validation functions | Safety |  |  |  |  |  | ✓ | 1 |
| Do use a YAML front matter at the top of each .md file to define metadata like command name, description, and arguments | Structure |  |  |  |  |  | ✓ | 1 |
| Do use consistent markdown formatting across all commands | Style |  | ✓ |  |  |  |  | 1 |
| Do use consistent markdown headings (e.g., # for command title, ## for sections) and indent code blocks properly | Style |  |  |  |  |  | ✓ | 1 |
| Do use descriptive and meaningful command names | Structure |  | ✓ |  |  |  |  | 1 |
| Do validate user input thoroughly before execution | Error Handling |  | ✓ |  |  |  |  | 1 |
| Document each argument with a one-line description | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't allow unchecked execution of external commands; always validate their paths and arguments | Safety |  |  |  |  |  | ✓ | 1 |
| Don't include unnecessary loops or redundant checks in scripts | Performance |  |  |  |  |  | ✓ | 1 |
| Don't nest scripted side effects deeper than one level in the markdown | Structure |  |  |  |  |  | ✓ | 1 |
| Don't rely on implicit error handling from underlying tools; always wrap scripts in try-catch equivalents | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't use ambiguous variable names in argument interpolation; always prefix with the command name (e.g., mycommand_arg) | Style |  |  |  |  |  | ✓ | 1 |
| Don’t exceed three layers of command structure | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t hardcode sensitive information directly in command scripts | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t include unnecessary computations during command execution | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t mix different programming paradigms within one command | Style |  | ✓ |  |  |  |  | 1 |
| Don’t use sudo in command blocks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t use vague error messages | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t use ~ in paths; use repo-root-relative or absolute paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Guard all mutating or destructive steps behind dry_run=false checks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a Usage section with at least one code-fenced example of /<name> invocation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a semantic version (MAJOR.MINOR.PATCH) in front matter | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include an Examples section with at least one realistic end-to-end run | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include an H1 title that equals the command name | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include an owner (person or team handle) in front matter | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include last_reviewed as an ISO 8601 date and review at least every 180 days | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Interpolate arguments only with the {{name}} syntax | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep lines to 120 characters or fewer | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep one primary purpose per command | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make actions idempotent where practical | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make the filename exactly the command name (kebab-case) plus .md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mark commands that can cause side effects with requires_confirmation: true in front matter | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never embed credentials, tokens, or secrets in the file | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer POSIX-compatible shell features unless bash-specific features are justified | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer calling vetted repo scripts over inline bash blocks longer than 20 lines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer domain prefixes for organization (e.g., ci-..., db-..., docs-...) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer enums or regex patterns for constrained inputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide opt-in flags for expensive operations (e.g., include_all=true) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put every slash command in .claude/commands/<name>.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put set -euo pipefail at the top of every bash/sh code fence that runs commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Quote every interpolated {{arg}} in shell commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Redact secrets from outputs and logs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Reference only declared arguments; do not interpolate undeclared {{...}} | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope file operations to explicit subpaths; avoid repo-wide scans by default | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Best practices for defining Claude Code slash commands as .claude/commands/*.md with argument interpolation and optional scripted side effects | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start each file with YAML front matter containing name, description, version, owner, tags, and args | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State clear success criteria and outputs in the prompt | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use active voice and imperative mood in descriptions and prompts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use bash or sh language identifiers for shell code fences | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use lowercase kebab-case for command names (e.g., fix-typos) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use unique argument names; never duplicate or shadow | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate argument values before performing actions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

