# Synthesis of Claude Code Slash Command Best Practices

## 1. Consensus Rules

### Structure & Metadata

- **Require YAML frontmatter with at minimum a `description` field at the top of each command file.** Makes commands discoverable, parseable, and usable in the command picker. (substantively similar but differently worded across GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok)
- **Use lowercase kebab-case filenames that match the invocation name (e.g., `review-pr.md` → `/review-pr`).** Eliminates ambiguity between file and command; shell- and URL-friendly. (near-identical wording across GPT-5, Claude Opus, Gemini)
- **Keep one primary purpose per command file; split multi-purpose commands.** Reduces coupling, simplifies reasoning, and makes commands composable. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Keep `description` short — ideally a single sentence under ~80 characters.** Command pickers truncate; long descriptions drift into prose. (near-identical across Claude Opus and Claude Haiku)
- **Include a Usage/Examples section showing a realistic invocation.** Examples communicate intent more reliably than prose. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)

### Arguments

- **Declare every argument explicitly with name, type, and description; do not accept ad-hoc or undocumented inputs.** Implicit arguments produce silent failures and hide the contract. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Validate arguments before use and fail with clear, actionable messages.** Input errors caught early prevent destructive mid-run failures. (substantively similar across GPT-5, GPT-4o-mini, Claude Haiku, Gemini, Grok)
- **State the argument contract (shape, required/optional, examples) in the prompt body itself.** Positional slots (`$1`, `$2`) and front-matter types document intent; prose confirms it for the model. (substantively similar across GPT-5, Claude Opus, Claude Haiku)

### Prompt Content

- **Write prompts in imperative mood, directly addressing Claude.** "Refactor this function" is clearer to an LLM than narrative description. (near-identical across Claude Opus, Claude Haiku, Gemini)
- **State success criteria and expected output explicitly.** Ambiguous targets produce inconsistent model behavior. (substantively similar across GPT-5, Claude Haiku, Gemini)

### Shell / Scripted Side Effects

- **Begin every bash/sh block with `set -euo pipefail` (or equivalent strict mode).** Prevents silent failures and undefined-variable bugs. (near-identical across GPT-5, Claude Haiku, Gemini)
- **Quote every interpolated argument in shell commands; never splice raw user input into shell.** The primary injection vector; unquoted variables break on spaces and enable arbitrary code execution. (near-identical across GPT-5, Claude Opus, Gemini, Grok)
- **Scope and bound filesystem operations; never run unbounded `find .` or `grep -r` without a path.** Unbounded scans blow out context windows and hang IDEs on large repos. (substantively similar across GPT-5, Claude Opus, Claude Haiku)
- **Prefer extracting non-trivial logic (roughly >15–20 lines) into version-controlled external scripts.** External scripts can be tested, linted, and reviewed independently. (substantively similar across GPT-5, Gemini) — (contested; see Divergences)

### Safety

- **Require explicit confirmation before destructive or irreversible actions (deletes, force-pushes, migrations, overwrites).** The loudest safety affordance; prevents accidental data loss. (near-identical across GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok)
- **Never hardcode credentials, tokens, or secrets in command files.** Command files are committed, reviewed, and shared; secrets leak permanently. (near-identical across GPT-5, GPT-4o-mini, Claude Haiku, Grok)
- **Default to read-only / no-side-effect behavior; mutation must be opt-in (via `dry_run`, `--force`, or explicit flag).** First-run safety is a property users rely on. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)
- **Do not auto-commit, auto-push, or fetch-and-execute remote content.** Supply-chain and irreversibility risks. (substantively similar across Claude Opus, Claude Haiku)

### Performance

- **Avoid unnecessary external calls, repeated computation, and redundant work inside a single command.** Latency compounds in interactive use. (substantively similar across GPT-4o-mini, Claude Opus, Claude Haiku, Grok)
- **Bound the output of any pre-execution shell prelude (`| head`, `--max-count`, `--stat`).** Unbounded output blows context and slows first response. (raised by Claude Opus; echoed by GPT-5's "avoid repo-wide scans")

## 2. Strong Minority Rules

- **Declare `allowed-tools` in frontmatter and scope `Bash(...)` allowlists to specific subcommands, never `Bash(*)`.** *(Claude Opus only.)* This is Claude Code-specific and precisely targets the real attack surface; a bare `Bash(*)` defeats the permission model entirely. Worth including because it's the most Claude-Code-native safety control.
- **Never interpolate `$ARGUMENTS`/`$1` directly into a `!` shell prelude — treat arguments as attacker-controlled.** *(Claude Opus only.)* Prompt injection via argument → shell is an underappreciated and concrete vulnerability specific to this tool.
- **Limit shell preludes to ≤3 per command.** *(Claude Opus only.)* Each prelude is a synchronous blocking call; a specific, checkable bound that addresses real latency.
- **Include an `owner` field and `last_reviewed` date; review commands periodically (e.g., every 180 days).** *(GPT-5 only.)* Prompts rot silently; ownership and review cadence is the only mechanism that catches drift. Worth keeping because no other model addresses lifecycle.
- **Place `.claude/commands/` under CODEOWNERS.** *(Claude Opus only.)* Prompts that execute shell deserve the same review gate as CI config — a concrete, enforceable governance rule.
- **When a command processes multiple files, batch them into a single Claude request rather than invoking per file.** *(Claude Haiku only.)* Correct on both performance and consistency grounds; non-obvious enough to be worth stating.
- **Use few-shot examples in prompts when output structure matters.** *(Claude Opus, Gemini.)* Raised by two models; empirically the most reliable way to constrain output format.
- **Provide a dry-run mode for any command with side effects.** *(Claude Haiku, GPT-5.)* Makes review-before-execute the default.

## 3. Divergences

### Inline vs. external scripts
- **GPT-5, Gemini:** Strongly prefer extracting logic >~15–20 lines into external scripts for testability.
- **Claude Opus, Claude Haiku:** Prefer keeping commands self-contained; complexity in a prompt is a smell to split *commands*, not extract scripts.
- **Recommendation:** Both are right at different scales. Rule of thumb: if the logic is pure shell plumbing (bounded commands, grep, jq), keep it inline and bounded; if it involves control flow, data transformation, or would benefit from unit tests, extract it. Use the ~15-line threshold as a default, not a hard rule.

### Persona preambles ("You are a senior engineer...")
- **Claude Opus:** Explicitly discourages — wastes tokens without measurable benefit.
- **GPT-4o-mini, Grok:** Silent on this.
- **Recommendation:** Follow Claude Opus. Persona preambles are folklore from earlier, less-capable models; current practice is to state the task and constraints directly.

### Few-shot examples in prompts
- **Claude Opus, Gemini:** Recommend for structured output.
- **Claude Opus** flags as contested (context bloat vs. accuracy).
- **Recommendation:** Include when output format is non-obvious or must be parseable; skip when the task is conversational or open-ended.

### Line-length and heading-style enforcement
- **GPT-5 (120 chars, contested), Grok (80 chars in code blocks):** Propose specific limits.
- **Other models:** Silent.
- **Recommendation:** 120 is the better default; 80 is overly strict for prompts containing URLs or structured code. Mark as advisory rather than enforced.

### Repo-scoped vs. user-scoped commands
- **Claude Opus:** Prefer `.claude/commands/` in repo for team commands; `~/.claude/commands/` for personal experiments.
- **Others:** Don't address.
- **Recommendation:** Adopt Claude Opus's split — it aligns with review/governance goals.

### Heuristic sanitization checks
- **Grok:** Require explicit "sanitize inputs" step.
- **Claude Opus:** Stricter position — never interpolate arguments into shell at all.
- **Recommendation:** Claude Opus's rule is safer and more enforceable. "Sanitize" is vague; "don't interpolate into shell" is mechanically checkable.

## 4. Notable Omissions

- **GPT-4o-mini omits shell safety entirely** — no mention of `set -euo pipefail`, quoting, injection risk, or `allowed-tools`. This is the single biggest gap across any model's output; shell safety is consensus among every other model and is the most consequential category.
- **GPT-4o-mini and Grok omit argument-injection concerns.** Every other model treats this as the primary safety failure mode.
- **Claude Haiku omits the "use kebab-case filenames matching the invocation" rule** that appears in GPT-5, Claude Opus, and Gemini — a near-universal structural convention.
- **Grok omits prompt-quality rules (imperative mood, success criteria, few-shot examples).** These are consensus across Claude models and Gemini.
- **GPT-4o-mini and Grok omit the "one command per file, single purpose" rule** that appears everywhere else.
- **Everyone except Claude Opus omits Claude-Code-native features** (`allowed-tools`, `$ARGUMENTS` vs `$N`, `!` preludes). This suggests most models are reasoning from generic "slash command" priors rather than Claude Code specifics; Claude Opus's input carries disproportionate weight on tool-specific mechanics.
- **Only GPT-5 addresses lifecycle (`owner`, `last_reviewed`, versioning).** A real gap; prompt rot is a well-known failure mode.

## 5. Shared Deterministic Checks

### Shared checks (multiple models)

- **Check** — Verify each command file begins with valid YAML frontmatter containing required keys (at minimum `name`/`description`; optionally `arguments`, `allowed-tools`).
  - **Signal** — Raw source text; YAML parser over content between leading `---` fences.
  - **Tool candidate** — Ad-hoc (any YAML parser + key-presence assertions).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — Models differ on required keys: GPT-5 wants `name`/`description`/`version`/`owner`/`tags`/`args`; Claude Opus requires only `description`; Claude Haiku wants `name`/`description`/`arguments`. Substance agrees on frontmatter presence; disagrees on minimum key set.

- **Check** — Verify filename matches kebab-case regex `^[a-z][a-z0-9]*(-[a-z0-9]+)*\.md$`.
  - **Signal** — File path / basename.
  - **Tool candidate** — Ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — Identical in substance; regex phrasing varies.

- **Check** — Verify `description` field length is ≤80 characters and contains no newlines.
  - **Signal** — Parsed frontmatter `description` value.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.
  - **Variance** — Both agree on 80-char limit.

- **Check** — Verify every bash/sh code fence begins with `set -euo pipefail` (or `-e` plus `-u`/`-o pipefail` equivalent) as the first non-comment/non-shebang line.
  - **Signal** — Markdown code fences labeled `bash` or `sh`.
  - **Tool candidate** — Ad-hoc regex; optionally shellcheck directive check.
  - **Raised by** — GPT-5, Claude Haiku, Gemini.
  - **Variance** — Gemini allows split `set -e; set -u` forms; others require the combined form. Substance agrees.

- **Check** — Run `shellcheck` on every bash/sh code fence; fail on any SC2086 (unquoted variable) diagnostic at minimum.
  - **Signal** — Extracted shell content piped to `shellcheck --format=json`.
  - **Tool candidate** — `shellcheck` (explicitly named by Gemini and Grok, implied by GPT-5).
  - **Raised by** — GPT-5, Gemini, Grok.
  - **Variance** — GPT-5 targets SC2086 specifically in the context of `{{arg}}` interpolation; Gemini runs full shellcheck; Grok names SC2086. Converge on the tool.

- **Check** — Detect unquoted or direct interpolation of arguments (`$1`, `$ARGUMENTS`, `{{arg}}`) inside shell commands or preludes.
  - **Signal** — Regex over lines beginning with `!` (Claude Code prelude) or inside bash/sh code fences.
  - **Tool candidate** — Ad-hoc (regex) plus `shellcheck SC2086` for detection quality.
  - **Raised by** — GPT-5, Claude Opus, Grok.
  - **Variance** — Claude Opus is strictest (flag any direct interpolation, even quoted, in `!` preludes); GPT-5/Grok allow quoted interpolation.

- **Check** — Verify every placeholder `{{name}}` / `$N` referenced in the prompt body corresponds to a declared argument.
  - **Signal** — Regex extraction of placeholders; set-difference with declared arg names from frontmatter.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Claude Haiku (implicit via ordering check).
  - **Variance** — GPT-5 checks undeclared placeholders; Haiku checks placeholder–argument ordering consistency. Complementary.

- **Check** — Detect destructive filesystem or VCS operations (`rm -rf`, `git reset --hard`, `git push`, `kubectl delete`, `curl | sh`, etc.) in shell blocks and require either a confirmation prompt, a `--force`/`dry_run` guard, or `allowed-tools` scoping.
  - **Signal** — Regex union over bash/sh fences matching destructive command tokens.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 requires `dry_run` frontmatter arg; Claude Opus requires `allowed-tools` scoping; Haiku requires inline confirmation prompt. All three mechanisms solve the same problem.

- **Check** — Detect unbounded repo-wide scans (`find .`, `grep -r` without a path, `rg` with no path).
  - **Signal** — Regex over bash/sh fences.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Agree on substance; Claude Opus additionally flags missing output-bounding flags (`| head`, `--max-count`).

- **Check** — Scan source for embedded secrets (AWS keys `AKIA...`, GitHub tokens `ghp_...`, generic API-key assignment patterns).
  - **Signal** — Raw source file.
  - **Tool candidate** — `gitleaks`, `trufflehog`, or ad-hoc regex set.
  - **Raised by** — GPT-5, GPT-4o-mini.
  - **Variance** — GPT-5 gives specific regexes; GPT-4o-mini is more general. Both acknowledge high false-positive rate.

### Singleton checks (worth promoting)

- **Check** — Line count of command body (excluding frontmatter) is ≤100–120 lines; warn above threshold.
  - **Signal** — Source file line count minus frontmatter.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Count of `!` preludes in body is ≤3.
  - **Signal** — Regex count of lines beginning with `!`.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — If `.claude/commands/` exists, a matching CODEOWNERS entry must cover that path.
  - **Signal** — `.github/CODEOWNERS` (or equivalent) plus directory existence.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — If frontmatter declares `allowed-tools`, no entry may be `Bash(*)`, `Bash()`, or `Bash(:*)`.
  - **Signal** — Parsed frontmatter `allowed-tools`.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — `last_reviewed` frontmatter date is within N days (default 180) of current date.
  - **Signal** — Frontmatter `last_reviewed` + system date.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Version field matches semver `^\d+\.\d+\.\d+$`.
  - **Signal** — Frontmatter `version`.
  - **Tool candidate** — Ad-hoc regex.
  - **Raised by** — GPT-5.

- **Check** — Detect remote-fetch commands in preludes (`curl`, `wget`, `nc`, `ssh`).
  - **Signal** — Regex over `!` preludes.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Detect hardcoded absolute paths (`/home/`, `/tmp/`, `/Users/`) or URLs in scripts outside example blocks.
  - **Signal** — Regex over source.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Haiku.

- **Check** — If prompt asks Claude to modify code (keywords: refactor, fix, rewrite, modify), it must reference at least one code-context placeholder (`{{file_content}}`, `{{selection}}`, etc.).
  - **Signal** — Keyword scan of prompt body + placeholder scan.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Haiku.

---

## 6. Final Rules File

# Claude Code Slash Command Rules

**Scope.** Best practices for authoring and reviewing slash commands in `.claude/commands/*.md` (repo-scoped, team) and `~/.claude/commands/*.md` (user-scoped, personal).

**Audience.** Engineers authoring commands; reviewers gating them; AI assistants generating or modifying them.

---

## Structure & Metadata

- **Put every command in a single file at `.claude/commands/<name>.md`.** One command per file; one primary purpose per command. Split multi-mode commands (e.g., `/release` → `/release-notes`, `/release-tag`, `/release-publish`).
- **Begin every file with a YAML frontmatter block.** Required keys: `description`. Recommended: `name`, `arguments`, `allowed-tools`, `owner`, `version`, `last_reviewed`.
- **Use lowercase kebab-case filenames matching the invocation.** `review-pr.md` → `/review-pr`. Enforced by regex `^[a-z][a-z0-9]*(-[a-z0-9]+)*\.md$`.
- **Keep `description` to a single sentence under 80 characters.** It populates the command picker; be the one who chose where it truncates.
- **Include a `## Usage` section with a code-fenced example of the invocation.** Examples communicate intent more reliably than prose.
- **Keep the command body under ~100 lines.** Longer prompts stop being reviewed.
- **Commit team commands to `.claude/commands/`; keep personal experiments in `~/.claude/commands/`.** Mixing them produces "works on my machine" reviews.
- **Place `.claude/commands/` under CODEOWNERS.** Prompts that execute shell deserve the same review gate as CI config.

## Lifecycle & Ownership

- **Record an `owner` (person or team handle) in frontmatter.** Prompts rot; someone has to care.
- **Include `version` in semver (`MAJOR.MINOR.PATCH`) and `last_reviewed` as an ISO date.** Review at least every 180 days.

## Arguments

- **Declare every argument explicitly in frontmatter with name, type, and one-line description.** No undocumented inputs.
- **Prefer positional `$1`, `$2` over `$ARGUMENTS` when the command has fixed arity.** Positional slots document the contract; `$ARGUMENTS` hides it.
- **State the argument contract in the prompt body** (e.g., `Usage: /cmd <ticket-id>`; what each argument means; what to do if missing).
- **Only reference declared arguments in the prompt; do not interpolate undeclared `{{...}}` or `$N`.** Silent no-op expansion is a common bug.
- **Use enums/choices with an explicit list for constrained inputs.** Never accept free-form strings where a fixed set is intended.
- **Validate arguments before acting and fail with a clear, actionable message.** Prefer prompting Claude to ask the user over dying with a shell error.

## Prompt Content

- **Write prompts in the imperative, addressing Claude directly.** "Refactor the function…" beats "This command will refactor…".
- **Put the task statement in the first few lines; context and constraints follow.**
- **State success criteria and expected output format explicitly.** Ambiguous targets produce inconsistent behavior.
- **Use fenced code blocks for literal strings Claude must emit or match.** Prose descriptions of output drift; examples don't.
- **Include a concrete example of desired output when the format is non-obvious.** Few-shot beats description for structured output.
- **Do not duplicate guidance already in `CLAUDE.md`.** Link or rely on it; duplication drifts.
- **Avoid persona preambles ("You are a senior engineer…").** They consume tokens without measurably improving output.
- **If the command modifies code, include the relevant code context in the prompt** (e.g., `{{file_content}}`, `{{selection}}`). A modify-code prompt with no code context is a bug.

## Shell / Scripted Side Effects

- **Begin every `bash`/`sh` code fence with `set -euo pipefail`.** Fail fast, no undefined vars, no silent pipe failures.
- **Quote every interpolated argument in shell commands.** Unquoted `$var` or `{{arg}}` is the primary injection vector.
- **Never interpolate `$ARGUMENTS`, `$1`, etc. directly into a `!` shell prelude.** Arguments are attacker-controlled input; treat shell interpolation as command injection.
- **Declare `allowed-tools` in frontmatter for any command with shell preludes or write intent.**
- **Scope `Bash(...)` allowlists to specific subcommands** (e.g., `Bash(git diff:*)`). Never use `Bash(*)`.
- **Do not fetch remote content in preludes (`!curl`, `!wget`, `!ssh`).** Supply-chain risk and non-reproducible.
- **Bound every prelude's output** (`| head`, `--max-count`, `--stat`, `--name-only`). Unbounded output blows out context and slows the turn.
- **Do not recurse filesystem scans without a scope** (`find .`, `grep -r` with no path, `rg` with no path). Scope explicitly or let Claude search on demand.
- **Limit shell preludes to ≤3 per command.** Each is a synchronous blocking call before the model speaks.
- **Prefer extracting logic longer than ~15–20 lines into version-controlled external scripts.** Commands then become thin wrappers; scripts can be tested and linted independently.
- **Do not use `sudo`, `~` expansion, or hardcoded absolute paths (`/home/...`, `/Users/...`).** Use repo-root-relative paths and declared environment.
- **Validate shell blocks with `shellcheck`.** At minimum enforce SC2086 (quote variables).

## Safety

- **Default to read-only / no side effects.** Mutation must be explicit: a `dry_run` argument defaulting to `true`, or an explicit `--force` flag, or an in-prompt confirmation step.
- **Require confirmation before destructive or irreversible actions** (deletes, force-pushes, migrations, overwrites, `git reset --hard`, `kubectl delete`, `terraform apply`).
- **Show a diff or summary of proposed changes before finalizing** any code-modifying command.
- **Do not auto-commit, auto-push, or auto-merge.** Stage for user review.
- **Do not overwrite the user's uncommitted working-directory changes.** Write to a new branch, temp file, or confirmed location.
- **Never hardcode credentials, tokens, or secrets.** Use environment variables or a secure store.
- **Do not write outside the current repo** or to system directories.

## Error Handling

- **Check for required tools before use** (e.g., `command -v jq >/dev/null`). Fail with a message, not a cryptic shell error.
- **Catch foreseeable failure conditions** (missing file, invalid argument, empty selection) and surface an actionable message.
- **Do not let raw tracebacks or shell errors bubble to the user.** Wrap them in user-facing text.
- **Make operations idempotent where practical.** Reruns and partial failures should be safe.

## Performance

- **Batch multi-file work into a single Claude request** rather than one request per file. Faster and more consistent.
- **Do not use preludes for data Claude can retrieve on demand.** Preludes run every invocation; tool calls run only when needed.
- **Warn users upfront when a command will take more than ~10 seconds.** Silent long runs feel broken.
- **Avoid redundant computation, repeated network calls, and unnecessary loops in scripts.**

## Style

- **Use consistent markdown structure:** one H1 matching the command name; `##` sections for Usage, Arguments, Behavior, Examples.
- **Keep lines ≤120 characters** where practical; allow exceptions for URLs and long regexes.
- **Avoid commented-out alternatives, TODOs, and dead prompts in published command files.**