# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested)** Prefer prompt logic over scripting | Scripting & Side Effects |  |  |  |  | ✓ |  | 1 |
| **Audit `!` shell preambles on every PR touching commands.** They execute before the model sees anything — this is a supply-chain surface | Safety |  |  | ✓ |  |  |  | 1 |
| **Avoid meta-instructions about how the model should "think".** Specify what to do and what output you want | Style |  |  | ✓ |  |  |  | 1 |
| **Compose commands by invoking other commands or scripts, not by sourcing shared markdown.** Explicit delegation is debuggable; transclusion isn't | Composition & Reuse |  |  | ✓ |  |  |  | 1 |
| **Delete unused commands aggressively.** Dead commands mislead both humans and the model about "how we do things here" | Review & Maintenance |  |  | ✓ |  |  |  | 1 |
| **Document non-obvious prerequisites (env vars, installed tools, auth) at the top of the body.** Failures from missing setup are the worst kind of failure | Review & Maintenance |  |  | ✓ |  |  |  | 1 |
| **Don't `@`-include large generated files, lockfiles, or `node_modules`.** They crowd out the context that matters | Model & Performance |  |  | ✓ |  |  |  | 1 |
| **Don't accept free-form `$ARGUMENTS` for destructive commands.** Structured inputs prevent "I thought you meant the other branch." | Arguments & Inputs |  |  | ✓ |  |  |  | 1 |
| **Don't duplicate Claude Code's built-in behavior (file reading, tool use).** Tell it *what*, not *how to use its tools* | Style |  |  | ✓ |  |  |  | 1 |
| **Fail fast: validate args and preconditions before any expensive tool call.** Wasted tokens are wasted time and money | Model & Performance |  |  | ✓ |  |  |  | 1 |
| **Forbid `curl \| sh` and equivalent remote-execution patterns in `!` blocks.** No exceptions | Safety |  |  | ✓ |  |  |  | 1 |
| **Gate destructive commands behind an explicit flag argument (e.g., `$1 == "--yes"`).** Dry-run by default, act on opt-in | Safety |  |  | ✓ |  |  |  | 1 |
| **Gather repo state with `!` preambles (e.g., `!git status`, `!git branch --show-current`).** Deterministic context beats asking the model to infer | Arguments & Inputs |  |  | ✓ |  |  |  | 1 |
| **Give every command a single, stated purpose in the first line after frontmatter.** A command that does two things should be two commands | Structure |  |  | ✓ |  |  |  | 1 |
| **Inherit the default model unless the command has a specific capability need.** Pinning `model:` per command creates drift and surprise | Model & Performance |  |  | ✓ |  |  |  | 1 |
| **Inline shared instructions until duplicated three times, then extract.** Premature factoring creates indirection worse than duplication | Composition & Reuse |  |  | ✓ |  |  |  | 1 |
| **Keep commands under ~100 lines.** If it's longer, it's doing too much or should delegate to a script | Structure |  |  | ✓ |  |  |  | 1 |
| **Move deterministic logic (parsing, formatting, file manipulation) into scripts called from `!`.** Use the model for judgment, not string processing | Composition & Reuse |  |  | ✓ |  |  |  | 1 |
| **Move judgment-heavy steps (code review, diagnosis, design) into the prompt body.** Don't try to script what needs reasoning | Composition & Reuse |  |  | ✓ |  |  |  | 1 |
| **Name files by verb-object (`fix-flaky-test.md`, `review-pr.md`).** Slash syntax reads as an imperative; names should too | Structure |  |  | ✓ |  |  |  | 1 |
| **Never embed secrets, tokens, or env-specific URLs in command files.** They're committed to git; treat them as public | Safety |  |  | ✓ |  |  |  | 1 |
| **Prefer letting the model open files on demand over front-loading with `@`.** Targeted reads beat speculative dumps | Model & Performance |  |  | ✓ |  |  |  | 1 |
| **Prefer positional `$1`, `$2`, `$3` over `$ARGUMENTS`.** Named slots force you to think about arity and make missing args detectable | Structure |  |  | ✓ |  |  |  | 1 |
| **Put personal commands in `~/.claude/commands/`, shared ones in `.claude/commands/`.** Don't pollute the team namespace with your workflow | Structure |  |  | ✓ |  |  |  | 1 |
| **Reference specific files with `@path/to/file`, not glob dumps.** Context window is a budget; spend it on what matters | Arguments & Inputs |  |  | ✓ |  |  |  | 1 |
| **Require explicit confirmation before destructive actions (force push, rm, DB writes, external sends).** A slash command should never silently lose work | Safety |  |  | ✓ |  |  |  | 1 |
| **Review slash commands in PRs with the same rigor as code.** They run on every contributor's machine with tool access | Review & Maintenance |  |  | ✓ |  |  |  | 1 |
| **Set `allowed-tools:` to the minimum required.** Never ship a shared command with `Bash(*)` or unrestricted `Write` | Safety |  |  | ✓ |  |  |  | 1 |
| **State argument semantics explicitly ("$1 is the PR number, numeric").** The model will guess types otherwise | Arguments & Inputs |  |  | ✓ |  |  |  | 1 |
| **State success criteria explicitly ("Done when all tests pass and the diff is committed").** Without a finish line, the model stops arbitrarily | Style |  |  | ✓ |  |  |  | 1 |
| **Structure the body as: Purpose → Inputs → Context → Steps → Success Criteria.** The model follows structured prompts far more reliably than prose | Structure |  |  | ✓ |  |  |  | 1 |
| **Test commands manually after changes to frontmatter or `!` preambles.** There's no type system; the only test is invocation | Review & Maintenance |  |  | ✓ |  |  |  | 1 |
| **Use `argument-hint:` whenever the command takes arguments.** Users discover shape through autocomplete, not by reading the file | Structure |  |  | ✓ |  |  |  | 1 |
| **Use fenced code blocks for exact commands the model should run.** Prose shell commands get paraphrased | Style |  |  | ✓ |  |  |  | 1 |
| **Use numbered lists for procedures, not paragraphs.** Ordering is semantic; don't hide it in prose | Structure |  |  | ✓ |  |  |  | 1 |
| **Validate arguments in the first step and abort with a clear message if invalid.** Garbage-in produces confidently wrong output | Arguments & Inputs |  |  | ✓ |  |  |  | 1 |
| **Write a `description:` in frontmatter for every command.** It's what `/help` shows; without it the command is invisible | Structure |  |  | ✓ |  |  |  | 1 |
| **Write instructions in the imperative ("Run the tests", not "You might want to run the tests").** Hedging invites the model to skip steps | Style |  |  | ✓ |  |  |  | 1 |
| Abort on partial success and clearly report which sub-step failed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add a `description` field to the frontmatter of every command | Style & Documentation |  |  |  |  | ✓ |  | 1 |
| Add lightweight self-checks (tools present, versions, sample validation) runnable via --check | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Apply timeouts to network calls and long-running steps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Assign CODEOWNERS for .claude/commands and require review for changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers and AI coding assistants creating or maintaining reusable command workflows with argument interpolation and optional scripted side effects | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid GNU-only flags unless you check and handle alternatives | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid tight loops that spawn many processes; batch work when possible | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid unnecessary complexity in command logic | Style |  | ✓ |  |  |  |  | 1 |
| Avoid using globally mutable state in commands | Performance |  | ✓ |  |  |  |  | 1 |
| Cache expensive results under .claude/cache with clear invalidation keys | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Check required tool presence and minimum versions with actionable install hints | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Clearly state the desired output format, persona, and constraints | Prompting Best Practices |  |  |  |  | ✓ |  | 1 |
| Cover commands in CI on supported OSes and shells | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Create one file per command | File & Command Structure |  |  |  |  | ✓ |  | 1 |
| Declare every argument explicitly and reject unknown or misspelled args | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default to the smallest safe scope (e.g., changed files) rather than “all.” Rationale: Minimizes unintended work and risk | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define all user-provided arguments in the frontmatter | Arguments |  |  |  |  | ✓ |  | 1 |
| Deny network access by default for local-only commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Deprecate with clear warnings and migration hints for at least one release | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Detect OS and tool variants explicitly and branch accordingly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Detect non-TTY and disable ANSI colors automatically | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do cache results for frequently used commands if applicable | Performance |  |  |  |  |  | ✓ | 1 |
| Do follow a consistent naming convention for commands, like lowercase-kebab-case | Style |  |  |  |  |  | ✓ | 1 |
| Do implement confirmation prompts for commands with destructive side effects | Safety |  |  |  |  |  | ✓ | 1 |
| Do keep scripted side effects minimal and asynchronous where possible | Performance |  |  |  |  |  | ✓ | 1 |
| Do limit each command file to a single primary action (contested) | Structure |  |  |  |  |  | ✓ | 1 |
| Do log all side effect executions for auditing | Safety |  |  |  |  |  | ✓ | 1 |
| Do not hard-code sensitive information into commands | Safety |  | ✓ |  |  |  |  | 1 |
| Do not ignore edge cases in command logic | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do not print secrets or environment variables by default; mask known patterns | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not solicit chain-of-thought; request structured, verifiable outputs (diffs, JSON, steps) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use eval for command construction; pass arguments as arrays | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize content into clear sections: "Description", "Arguments", "Examples", and "Side Effects" | Structure |  |  |  |  |  | ✓ | 1 |
| Do provide meaningful error messages for invalid inputs or failures | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do restrict argument types to strings or simple objects, avoiding executable code | Safety |  |  |  |  |  | ✓ | 1 |
| Do use a YAML frontmatter at the top of each file to define metadata like name, description, and arguments | Structure |  |  |  |  |  | ✓ | 1 |
| Do use bullet points for arguments and examples to improve scannability | Style |  |  |  |  |  | ✓ | 1 |
| Do validate all required arguments at the start of the command | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do write descriptions in plain, concise language using active voice | Style |  |  |  |  |  | ✓ | 1 |
| Document all parameters with name, type, required/default, and allowed values | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't allow unchecked external API calls or file modifications | Safety |  |  |  |  |  | ✓ | 1 |
| Don't assume user inputs are safe; always sanitize strings to avoid injection attacks | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't embed complex logic directly in markdown; instead, reference external scripts for side effects | Structure |  |  |  |  |  | ✓ | 1 |
| Don't include computationally intensive operations in the command itself | Performance |  |  |  |  |  | ✓ | 1 |
| Don't include unnecessary verbosity, such as redundant examples | Style |  |  |  |  |  | ✓ | 1 |
| Don't use try-catch blocks in markdown; handle errors via predefined exit strategies in scripts | Error Handling |  |  |  |  |  | ✓ | 1 |
| Emit a concise summary with exit status and next steps at the end | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enclose all interpolated arguments and user-provided context in XML tags | Prompting Best Practices |  |  |  |  | ✓ |  | 1 |
| Ensure each command file has a clear and descriptive title | Structure |  | ✓ |  |  |  |  | 1 |
| Ensure scripts are idempotent where possible | Scripting & Side Effects |  |  |  |  | ✓ |  | 1 |
| Favor specific commands over a single, monolithic command | File & Command Structure |  |  |  |  | ✓ |  | 1 |
| Goal: Make commands readable, maintainable, correct, safe, performant, and predictable for teams | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Handle spaces and newlines in paths robustly across tooling | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Implement permission checks to restrict command access | Safety |  | ✓ |  |  |  |  | 1 |
| Implement try-catch blocks to manage potential exceptions | Error Handling |  | ✓ |  |  |  |  | 1 |
| Include a commented-out usage example in the file | Style & Documentation |  |  |  |  | ✓ |  | 1 |
| Include a summary of arguments and expected outputs at the top of each command | Structure |  | ✓ |  |  |  |  | 1 |
| Include a support/escalation note with contact or channel | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include at least one copy-pastable example invocation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep commands focused on one job and compose via underlying scripts/tools | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep default output concise and elevate detail behind --verbose | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep prompts specific with clear goals, constraints, and acceptance criteria | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Limit context to relevant files/snippets and state strict token bounds | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Limit script permissions to the absolute minimum required | Safety |  |  |  |  | ✓ |  | 1 |
| Limit the frequency of external API calls within commands | Performance |  | ✓ |  |  |  |  | 1 |
| List prerequisites (CLIs, versions, auth) in a “Prereqs” section | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make commands idempotent so repeated runs converge to the same end state | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mark non-obvious arguments as `optional: false` to enforce their presence | Arguments |  |  |  |  | ✓ |  | 1 |
| Name commands and files identically in kebab-case with a leading verb (e.g., “fix-tests”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never execute code fetched from the network without signature, checksum, or pinned revision verification | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never execute unvalidated input via `eval`, `exec`, or direct shell interpolation | Safety |  |  |  |  | ✓ |  | 1 |
| Normalize relative paths against the repo root and verify existence | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Operate on changed files by default using git queries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Optimize commands to minimize execution time | Performance |  | ✓ |  |  |  |  | 1 |
| Organize commands immediately under a well-defined section | Structure |  | ✓ |  |  |  |  | 1 |
| Parallelize independent work with safe tooling (e.g., xargs -P, tool-native concurrency) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Parse list arguments safely (e.g., newline-delimited or JSON) rather than ad-hoc splitting | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Perform write-heavy operations in a throwaway branch or worktree by default | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place instructions before context and examples | Prompting Best Practices |  |  |  |  | ✓ |  | 1 |
| Prefer bash for authoring complex shell steps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer hermetic toolchains (e.g., dev containers or pinned envs) for complex stacks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Preview effects (file lists, diffs, counts) in --dry-run before making changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Print commands before execution when --verbose is set | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Propagate non-zero exit codes and stop on first failure unless --keep-going is set | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide --dry-run, --force, and --verbose flags with consistent semantics | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide /help and category listings to enumerate available commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a --check mode that validates and reports without modifying files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a clear, one-sentence `description` for every argument | Arguments |  |  |  |  | ✓ |  | 1 |
| Provide a concrete, high-quality example of the desired output in the prompt | Prompting Best Practices |  |  |  |  | ✓ |  | 1 |
| Provide helpful remediation hints on common failures | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put exactly one command per file under .claude/commands named <command>.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Quote every interpolated value in shell, JSON, and URL contexts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Read all dynamic data from standard input and pass arguments as flags | Scripting & Side Effects |  |  |  |  | ✓ |  | 1 |
| Redact secrets and sensitive data from prompts and model inputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Refuse to run with a dirty working tree unless the command declares it safe | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require confirmation for destructive operations unless --force is provided | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require explicit user confirmation within the command's workflow for any destructive action | Safety |  |  |  |  | ✓ |  | 1 |
| Require human confirmation before applying LLM-generated edits | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return meaningful error messages rather than generic ones | Error Handling |  | ✓ |  |  |  |  | 1 |
| Scope tokens to the minimum permissions and load them explicitly from env vars | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Standards for authoring Claude Code Slash Commands stored in .claude/commands/*.md and invoked with /<name> | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set a strict shell mode at the top of shell blocks: set -euo pipefail and IFS=$'\n\t' | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set bounded retries with exponential backoff for flaky networks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set temperature to 0 for deterministic refactors and to >0 only for ideation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Show a unified diff of proposed edits and provide a one-command revert | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start each file with a one-line summary and a Usage block | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Store prompt templates alongside the command for transparency | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Treat all arguments passed to a script as potentially malicious strings, not trusted code | Safety |  |  |  |  | ✓ |  | 1 |
| Use YAML frontmatter for metadata (name, summary, version, owners, tags) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use a shebang line (e.g., `#!/usr/bin/env python3`) to specify the script interpreter | Scripting & Side Effects |  |  |  |  | ✓ |  | 1 |
| Use clear, action-oriented messages (“Fix applied to 3 files; review diff below”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use confirmation prompts for actions that modify data | Safety |  | ✓ |  |  |  |  | 1 |
| Use consistent naming conventions for commands and arguments | Style |  | ✓ |  |  |  |  | 1 |
| Use descriptive, `snake_case` argument names | Arguments |  |  |  |  | ✓ |  | 1 |
| Use kebab-case for command filenames (e.g., `generate-unit-test.md`) | File & Command Structure |  |  |  |  | ✓ |  | 1 |
| Use locale-independent settings (e.g., export LC_ALL=C) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use markdown comments (`<!-- | Style & Documentation |  |  |  |  | ✓ |  | 1 |
| Validate all inputs and preconditions before any side effects | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate arguments with enums or regex before any side effects | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Version commands in metadata and record changes in a CHANGELOG | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write all primary output to standard output | Scripting & Side Effects |  |  |  |  | ✓ |  | 1 |
| Write clear and concise documentation for each command | Style |  | ✓ |  |  |  |  | 1 |
| Write prompts from the perspective of instructing an expert assistant | Prompting Best Practices |  |  |  |  | ✓ |  | 1 |
| Write transient artifacts to .claude/tmp and clean them on success | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| cd to the repo root at the start of execution | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

