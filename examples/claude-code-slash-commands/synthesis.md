# Synthesis: Claude Code Slash Commands Best Practices

## 1. Consensus Rules

### Structure & Organization

- **Use one file per command, named in kebab-case matching the invocation.** (substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini) — Discoverability, modularity, and consistent mapping between filename and `/command`.
- **Include a clear, one-line description/summary at the top of every command.** (substantively similar across all 6 models) — Users (and `/help`) need to understand intent in seconds.
- **Use frontmatter or a structured header to declare metadata (description, arguments, tools).** (substantively similar across GPT-5, Claude Opus, Gemini, Grok) — Structured metadata enables tooling and serves as a public API.
- **Keep commands focused on a single purpose; split monolithic commands.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — Single-responsibility commands are easier to review, compose, and reuse.
- **Include usage examples in the command file.** (substantively similar across GPT-5, Claude Haiku, Gemini, Grok) — Examples reduce friction and resolve ambiguity faster than prose.

### Arguments & Inputs

- **Document every argument with name, type, and expected behavior.** (substantively similar across all 6 models) — Explicit contracts prevent misuse and silent misinterpretation.
- **Validate arguments before any side effects and fail fast with actionable messages.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — Early exit preserves state and surfaces errors clearly.
- **Use explicit, unambiguous argument names (e.g., `currentFile` not `file`, `$1` not `$ARGUMENTS`).** (substantively similar across Claude Opus, Claude Haiku, Gemini) — Ambiguous names invite silent wrong-target bugs.
- **Never interpolate unsanitized user input into shell or executable contexts.** (near-identical wording across GPT-5, Claude Haiku, Gemini, Grok) — Injection is the primary vulnerability in this surface area.

### Safety

- **Require explicit confirmation or an opt-in flag for destructive operations.** (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini, GPT-4o-mini, Grok) — Irreversible actions demand a human-in-the-loop.
- **Declare all side effects prominently in the description.** (substantively similar across Claude Opus, Claude Haiku, Gemini, Grok) — Users should never be surprised by what a command modifies.
- **Apply the principle of least privilege to tools and permissions (`allowed-tools` minimal, no `Bash(*)`).** (substantively similar across GPT-5, Claude Opus, Gemini) — Minimize blast radius when something goes wrong.
- **Never embed secrets, tokens, or credentials in command files.** (substantively similar across GPT-5, Claude Opus, GPT-4o-mini) — Command files are committed to git; treat them as public.

### Error Handling & Correctness

- **Provide actionable, specific error messages — not generic failures.** (substantively similar across GPT-5, Claude Haiku, GPT-4o-mini, Grok) — "Install Python 3.12" beats "Error: failed."
- **Document environment prerequisites (tools, versions, auth) upfront.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Missing-setup failures are the most frustrating kind.
- **Make commands idempotent where feasible.** (substantively similar across GPT-5, Gemini) — Retries should converge to the same state.

### Style

- **Write instructions in imperative, active voice.** (substantively similar across Claude Opus, Claude Haiku, Grok) — "Run the tests" invites action; hedging invites skipping steps.
- **Use structured markdown (headings, numbered lists, code blocks) rather than dense prose.** (substantively similar across Claude Opus, Claude Haiku, Grok) — Structure anchors both human and LLM attention.
- **Use consistent naming conventions across your command library.** (substantively similar across GPT-5, GPT-4o-mini, Gemini, Grok) — Consistency reduces cognitive load.

### Maintenance

- **Version commands in git and review them like code.** (substantively similar across GPT-5, Claude Opus, Claude Haiku) — These files execute on contributor machines; they deserve code-review rigor.
- **Test commands manually after changes, especially to frontmatter or shell preambles.** (substantively similar across Claude Opus, Claude Haiku) — There is no type system; invocation is the only test.

---

## 2. Strong Minority Rules

- **Provide `--dry-run`, `--force`, and `--verbose` flags with consistent semantics.** (GPT-5 only) — Worth keeping: predictable control flags enable safe experimentation across an entire command suite.
- **Structure the body as Purpose → Inputs → Context → Steps → Success Criteria.** (Claude Opus only) — Worth keeping: LLMs follow structured prompts far more reliably than freeform prose; this is a concrete, actionable template.
- **State explicit success criteria ("Done when all tests pass and the diff is committed").** (Claude Opus only) — Worth keeping: without a finish line, the model stops at arbitrary intermediate states.
- **Gather repo state with deterministic `!` preambles rather than asking the model to infer.** (Claude Opus only) — Worth keeping: specific to Claude Code's execution model and directly reduces confabulation.
- **Enclose interpolated arguments in XML tags in prompts.** (Gemini only) — Worth keeping: well-established prompt-engineering practice that reduces ambiguity and injection risk in AI contexts.
- **Prefer letting the model open files on demand over front-loading with `@`.** (Claude Opus only) — Worth keeping: context budget management is a real performance concern specific to this tool.
- **Distinguish personal commands (`~/.claude/commands/`) from project commands (`.claude/commands/`).** (Claude Opus only) — Worth keeping: a concrete operational rule that prevents namespace pollution.
- **Prefer positional `$1`, `$2` over `$ARGUMENTS` for detectable arity.** (Claude Opus only) — Worth keeping: tool-specific and directly addresses a common failure mode.
- **Forbid `curl | sh` and remote-execution patterns in `!` blocks.** (Claude Opus only) — Worth keeping: a hard, non-negotiable safety rule that's absent elsewhere.
- **Use `LC_ALL=C` and locale-independent settings for reproducibility.** (GPT-5 only) — Worth keeping: prevents subtle cross-machine failures that are hard to diagnose.

---

## 3. Divergences

### Prompt logic vs. scripted logic
- **Gemini**: Strongly favors prompt-first; scripts only for things the AI cannot do (filesystem, APIs).
- **Claude Opus**: Split by nature of work — deterministic logic (parsing, formatting) in scripts; judgment (review, design) in prompts.
- **Claude Haiku**: Scripts acceptable only if short, idempotent, and with explicit side effects.
- **GPT-5 / Grok**: Favor offloading complex logic to external scripts.

**Recommendation**: Adopt Claude Opus's split. Use scripts for deterministic string processing and state-gathering where determinism matters; use the prompt for anything requiring judgment. This matches how the tool is actually designed to be used and avoids both extremes (fragile AI-based parsing and opaque script black boxes).

### Command verbosity / chattiness
- **Claude Opus**: Chatty for destructive or external-touching commands; terse for read-only.
- **GPT-5**: Concise by default, detail behind `--verbose`.
- **Claude Haiku**: Concise and scannable.

**Recommendation**: Follow Claude Opus's risk-proportional approach. Terseness is a UX win for safe commands; verbosity is a safety feature for risky ones.

### Pinning model per command
- **Claude Opus**: Don't pin unless genuinely needed — creates drift and surprise.
- **GPT-5**: Set temperature=0 for deterministic edits (implicit pinning of generation parameters).

**Recommendation**: Don't pin `model:` without justification; do control generation parameters (temperature) when determinism matters.

### Shell choice (bash vs. POSIX sh)
- **GPT-5**: Prefers bash for safety features (arrays, strict mode).
- Others: Silent.

**Recommendation**: Use bash with `set -euo pipefail` for non-trivial shell blocks; the safety gains outweigh portability costs for most teams.

### When to extract shared instructions
- **Claude Opus**: "Rule of three" — inline until duplicated three times.
- Others: Silent or favor composition from the start.

**Recommendation**: Follow the rule of three. Premature extraction in prompt files creates indirection that's harder to debug than duplication.

### Network access defaults
- **GPT-5**: Deny by default for local-only commands (contested in its own file).
- Others: Silent.

**Recommendation**: Default-deny is a good principle but hard to enforce in Claude Code's model; instead, audit `!` preambles for network calls during review.

---

## 4. Notable Omissions

- **GPT-4o-mini omits argument validation specifics, frontmatter/metadata structure, and single-purpose command guidance** — despite these being consensus rules across the other five models. Its output is notably shallow on the specifics of this tool.
- **Grok omits explicit frontmatter/metadata structure** beyond a passing mention, where GPT-5, Claude Opus, and Gemini all emphasize it as a public API.
- **GPT-4o-mini and Grok omit any mention of Claude Code-specific features** (`$ARGUMENTS` vs. `$1`, `!` preambles, `@` file references, `allowed-tools`) — suggesting these models may be generalizing from "slash commands in a CLI tool" rather than engaging with Claude Code specifically. This is itself a signal: rules grounded in the actual tool are more trustworthy.
- **Claude Haiku omits `allowed-tools` / least-privilege guidance** that GPT-5, Claude Opus, and Gemini all include — a meaningful safety gap.
- **GPT-4o-mini omits LLM-specific prompt engineering guidance** (XML tags, few-shot examples, output format constraints) that Claude Opus and Gemini emphasize.
- **Only Claude Opus explicitly addresses `.claude/commands/` as supply-chain surface area** — everyone else underweights that these files execute on every contributor's machine.
- **Only Claude Opus mentions the personal vs. project command directory distinction** — a practical rule the others miss.

---

## 5. Final Rules File

```markdown
# Claude Code Slash Commands — Best Practices

**Scope:** Authoring and reviewing slash commands stored in `.claude/commands/*.md`
(project) and `~/.claude/commands/*.md` (personal), invoked via `/<name>`.
**Audience:** Engineers and AI coding assistants creating or maintaining
reusable command workflows with argument interpolation and optional scripted
side effects.

Treat `.claude/commands/` as code: it executes on every contributor's machine
with tool access. Review it with the same rigor.

---

## Structure & Organization

- **One command per file**, named in kebab-case, matching the invocation
  (`fix-flaky-test.md` → `/fix-flaky-test`). Name by verb-object.
- **Put personal commands in `~/.claude/commands/`**, shared ones in
  `.claude/commands/`. Don't pollute the team namespace with your workflow.
- **Start with YAML frontmatter** declaring at minimum: `description`,
  `argument-hint` (if takes args), and `allowed-tools`. This is the command's
  public API and what `/help` displays.
- **Keep each command focused on a single purpose.** Split monolithic commands.
  If it does two things, it should be two commands.
- **Keep commands under ~100 lines.** Longer commands are doing too much or
  should delegate to a script.
- **Structure the body as: Purpose → Inputs → Context → Steps → Success Criteria.**
  LLMs follow structured prompts far more reliably than freeform prose.
- **Use numbered lists for procedures and fenced code blocks for exact commands.**
  Ordering is semantic; don't hide it in prose.
- **Include at least one copy-pastable usage example.**

## Arguments & Inputs

- **Document every argument** with name, type, scope, default, and required/optional
  status. Explicit contracts prevent silent misinterpretation.
- **Prefer positional `$1`, `$2` over raw `$ARGUMENTS`.** Named slots force you
  to think about arity and make missing args detectable.
- **Use explicit, unambiguous argument names** (`currentFile`, `selectedFiles`,
  `workspacePath` — not `file` or `path`).
- **Validate arguments in the first step and abort with a clear message if invalid.**
  Fail fast before any side effects.
- **Never interpolate unsanitized user input into shell, JSON, or URL contexts.**
  Quote and escape everything. Use args as parameters to safe tools, never as
  code passed to `eval`/`exec`.
- **Enclose interpolated arguments in XML tags within prompts**
  (`<file_path>{{file_path}}</file_path>`). Reduces ambiguity and injection risk.
- **Gather repo state with deterministic `!` preambles** (e.g., `!git status`,
  `!git branch --show-current`) rather than asking the model to infer.
- **Reference specific files with `@path/to/file`, not glob dumps.** Context
  window is a budget; spend it on what matters. Prefer letting the model open
  files on demand over speculative front-loading.

## Safety

- **Set `allowed-tools` to the minimum required.** Never ship a shared command
  with `Bash(*)` or unrestricted `Write`.
- **Declare all side effects in the description.** If the command modifies files,
  commits code, or calls external systems, say so on the first line.
- **Require explicit confirmation or an opt-in flag for destructive operations**
  (force push, rm, DB writes, external sends, overwrites). Dry-run by default;
  act on opt-in.
- **Never embed secrets, tokens, or credentials** in command files. They're
  committed to git; treat them as public.
- **Audit `!` shell preambles on every PR touching commands.** They execute
  before the model sees anything — this is a supply-chain surface.
- **Forbid `curl | sh` and equivalent remote-execution patterns in `!` blocks.**
  No exceptions.
- **Refuse to run with a dirty working tree** unless the command explicitly
  declares it safe to do so.

## Correctness & Error Handling

- **Fail fast with actionable, specific error messages.** "Install Python 3.12"
  beats "Error: failed to process file."
- **Document environment prerequisites** (tools, versions, env vars, auth) at
  the top of the body. Missing-setup failures are the worst failures.
- **Make commands idempotent where feasible.** Repeated runs should converge.
- **State explicit success criteria** ("Done when all tests pass and the diff
  is committed"). Without a finish line, the model stops arbitrarily.
- **Never silently skip errors.** Report and stop; don't continue with partial
  results.

## Style

- **Write instructions in the imperative, active voice.** "Run the tests," not
  "You might want to run the tests." Hedging invites skipping steps.
- **Use structured markdown** (headings, numbered lists, fenced code) rather
  than dense prose. Structure anchors both human and LLM attention.
- **Use consistent naming conventions** across your command library.
- **Keep prompts specific**: goals, constraints, acceptance criteria, output
  format. Avoid meta-instructions about how the model should "think."
- **Don't duplicate Claude Code's built-in behavior** (file reading, tool use).
  Tell it *what*, not *how to use its tools*.

## Scripts vs. Prompts

- **Use scripts for deterministic work** the model shouldn't do: parsing,
  formatting, filesystem manipulation, state-gathering.
- **Use the prompt for judgment-heavy work**: code review, diagnosis, design,
  refactoring decisions.
- **Keep any embedded scripts short, idempotent, and inspectable.**
- **Prefer Bash tool calls over long opaque `!` pipelines** — the former is
  inspectable, the latter isn't.
- **Use `set -euo pipefail` and `IFS=$'\n\t'`** at the top of bash blocks.

## Flags & UX

- **Provide `--dry-run`, `--force`, and `--verbose` flags** with consistent
  semantics across your command library.
- **Preview effects (file lists, diffs, counts) in dry-run before changes.**
- **Keep default output concise; elevate detail behind `--verbose`.**
- **Be chatty for commands touching git history, external systems, or files
  outside the working tree; terse for read-only analysis.**

## Composition & Reuse

- **Inline shared instructions until duplicated three times, then extract.**
  Premature factoring creates indirection worse than duplication.
- **Compose by invoking other commands or scripts, not by sourcing shared
  markdown.** Explicit delegation is debuggable; transclusion isn't.

## Performance

- **Fail fast**: validate args and preconditions before any expensive tool call.
- **Don't `@`-include large generated files, lockfiles, or `node_modules`.**
  They crowd out context that matters.
- **Default to the smallest safe scope** (e.g., changed files via git) rather
  than full-repo scans.

## Maintenance

- **Version commands in git and review in PRs with the same rigor as code.**
- **Test commands manually after changes**, especially to frontmatter or `!`
  preambles. There's no type system; the only test is invocation.
- **Delete unused commands aggressively.** Dead commands mislead both humans
  and the model about "how we do things here."
- **Deprecate explicitly** with a migration hint, rather than silent deletion.
```