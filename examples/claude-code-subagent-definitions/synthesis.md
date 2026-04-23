# Synthesized Best-Practices Guidance: Claude Code Subagent Definitions

## 1. Consensus Rules

### File Location and Structure

- **Store subagent definitions in `.claude/agents/` with a `.md` extension.** (substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini)
  *Rationale: Predictable location enables tool discovery and code review.*

- **Begin each file with a YAML frontmatter block delimited by `---` for machine-parseable metadata.** (substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Grok)
  *Rationale: Structured metadata powers linting, validation, and tooling.*

- **Require `name` and `description` as mandatory frontmatter fields.** (near-identical wording across Claude Opus and Claude Haiku; substantively similar in GPT-5)
  *Rationale: These are the minimum contract for subagent discovery and routing.*

- **Organize the file with consistent, predictable sections (headings or frontmatter keys) across all subagents.** (substantively similar across all six models)
  *Rationale: Pattern recognition shortens review and debugging time.*

### Naming

- **Use kebab-case for subagent identifiers/filenames and match the filename stem to the identifier.** (near-identical wording across GPT-5 and Claude Opus; substantively similar in Claude Haiku, Gemini)
  *Rationale: Stable, portable identifiers ease cross-referencing; mismatches confuse reviewers.*

- **Name files descriptively after the agent's primary role (e.g., `typescript-linter.md`), not generically.** (substantively similar across Claude Haiku, Gemini, GPT-5)
  *Rationale: Filename is the first signal of purpose; discoverability matters.*

### Description Field

- **Write the description for the routing agent, not for humans.** (substantively similar but differently worded across Claude Opus, Claude Haiku, Gemini)
  *Rationale: The main agent uses description semantically to decide delegation; it's a classifier prompt, not documentation.*

- **Keep the description short (≤ ~160–400 characters or ~1–2 sentences) and action-oriented, starting with a verb phrase.** (substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini)
  *Rationale: Concise descriptions fit dashboards and produce stronger routing signal; vague descriptions ("helps with X") cause misrouting.*

### Single Responsibility

- **Give each subagent a single, well-defined responsibility.** (substantively similar but differently worded across Claude Opus, Claude Haiku, Gemini, GPT-4o-mini)
  *Rationale: Overlapping scopes cause non-deterministic routing; monoliths get called for everything but route to nothing reliably.*

### Tool Allowlists and Least Privilege

- **Declare `tools` explicitly; never omit the field, use wildcards, or list "all".** (near-identical in spirit across GPT-5, Claude Opus, Claude Haiku, Grok, GPT-4o-mini)
  *Rationale: Omitting or wildcarding tools grants maximum privilege by default, defeating the primary safety mechanism.*

- **Grant the minimum set of tools required for the task (principle of least privilege).** (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)
  *Rationale: Narrow tool access limits blast radius on misinterpretation or prompt injection.*

- **Do not grant write, edit, or shell execution tools to read-only/review/analysis subagents.** (substantively similar across GPT-5, Claude Opus, Claude Haiku)
  *Rationale: Read-only intent requires read-only tools; shell is the widest attack surface.*

### System Prompt Content

- **Open the system prompt with a one-line role/goal statement.** (substantively similar across Claude Opus, Claude Haiku, Gemini)
  *Rationale: Anchors the model's attention before elaboration.*

- **Write instructions in the imperative mood; avoid hedging and apologies.** (near-identical wording across Claude Opus and Claude Haiku; similar in Gemini)
  *Rationale: "Try your best" licenses mediocre output; directness improves reliability.*

- **Mandate a specific, machine-parsable output format.** (near-identical wording across Claude Opus, Gemini; similar in GPT-5)
  *Rationale: Conversational prose breaks downstream automation; callers need to parse results.*

- **Include at least one concrete input/output example when the task is ambiguous.** (substantively similar across GPT-5, Claude Opus, Claude Haiku; flagged "contested" by Opus and Haiku due to token cost)
  *Rationale: Few-shot examples outperform abstract instructions but cost tokens; use sparingly.*

- **Keep the system prompt bounded (roughly 1500–3000 characters / ≤ ~2 KB / ≤ ~1500 tokens).** (substantively similar but with different thresholds across GPT-5, Claude Opus, Claude Haiku, Grok)
  *Rationale: Long prompts dilute focus, increase cost/latency, and consume the subagent's own context budget.*

- **Do not assume shared state or prior conversation; subagents run in fresh contexts.** (raised by Claude Opus and Claude Haiku; substantively similar)
  *Rationale: "Continue what we were doing" has no referent in an isolated subagent context.*

### Safety Guardrails

- **Do not embed secrets, API keys, or credentials in subagent definitions.** (substantively similar across GPT-5, Claude Haiku)
  *Rationale: Secrets in version-controlled files are hard to purge and leak easily.*

- **Define explicit refusal/escalation/error-handling behavior for out-of-scope or failed tasks.** (substantively similar across GPT-5, Claude Haiku, Gemini)
  *Rationale: Deterministic exits prevent loops, hallucinated workarounds, and unsafe flailing.*

### Performance

- **Keep system prompts concise and task-focused to reduce token usage and latency.** (substantively similar across GPT-5, Claude Haiku, Gemini, Grok, GPT-4o-mini)
  *Rationale: Bloated prompts degrade latency, cost, and often accuracy.*

## 2. Strong Minority Rules

- **Use keywords like `PROACTIVELY` or `MUST BE USED` in the description when the agent should self-invoke.** (Claude Opus only)
  Kept because this is a documented Claude Code convention with concrete routing impact — not a general best practice but specific to this tool's behavior.

- **Keep frontmatter and the system prompt body separate: metadata in frontmatter, prompt in the markdown body.** (Claude Opus only)
  Kept because it cleanly separates concerns and matches Claude Code's actual file format more faithfully than GPT-5's "everything in YAML" approach.

- **Select the model (`haiku`/`sonnet`/`opus`) intentionally based on task complexity; don't default to `opus`.** (Claude Opus only)
  Kept because model selection has large cost/latency implications and is a frequent source of waste.

- **Document non-obvious subagents in a project README or index; document related/composed subagents.** (Claude Opus, Claude Haiku)
  Kept because discoverability is a real problem when routing is implicit.

- **Mark deprecated subagents rather than deleting them; maintain a changelog for significant changes.** (GPT-5, Claude Haiku)
  Kept because it addresses graceful migration and audit trails for shared infrastructure.

- **Detect and flag overlapping/duplicate descriptions across subagents in the same directory.** (Claude Opus)
  Kept because overlapping descriptions are a documented failure mode and the check is mechanical (Jaccard similarity).

- **Do not include instructions in the system prompt that contradict the tool allowlist (e.g., "run the build" without `Bash`).** (Claude Haiku)
  Kept because it's a specific, mechanically-checkable anti-pattern.

- **Declare path constraints for file-modifying tools when the tool supports them.** (Claude Haiku, GPT-5)
  Kept because path scoping is a major defense-in-depth mechanism beyond tool-level allowlists.

## 3. Divergences

### System prompt location: frontmatter vs. body

- **GPT-5**: Put the system_prompt inside YAML frontmatter as a single string block.
- **Claude Opus, Claude Haiku, Gemini**: Put the system prompt in the markdown body, outside frontmatter.

**Synthesis**: The Claude-family and Gemini models describe the actual Claude Code file format accurately; the system prompt is the markdown body, and frontmatter holds only metadata. GPT-5's "all in YAML" approach conflicts with this. **Recommendation: system prompt in the markdown body; frontmatter for metadata only.**

### Naming convention for the `name` field

- **Claude Opus**: kebab-case (`code-reviewer`).
- **Claude Haiku**: CamelCase/PascalCase (`CodeReviewer`).
- **GPT-5**: Title Case for display, kebab-case for `id`.

**Synthesis**: Claude Code documentation uses kebab-case for `name` in practice. **Recommendation: kebab-case for the `name` field**, matching the filename stem. Haiku's PascalCase claim appears incorrect.

### System prompt length thresholds

- **GPT-5**: ≤ 3000 characters.
- **Claude Haiku, Grok**: ≤ 2 KB / ≤ 500 tokens.
- **Claude Opus**: ≤ ~1500 tokens.

**Synthesis**: All models agree on "keep it bounded"; the specific number varies. **Recommendation: target ≤ ~1500 tokens as a soft warning, fail above ~3000 tokens / ~2 KB.** Treat the threshold as heuristic and tunable.

### Granularity of subagents

- **Gemini**: explicitly notes this is contested — fine-grained vs. consolidated.
- **Claude Opus, Claude Haiku, GPT-5**: prefer single-responsibility/fine-grained.
- **GPT-4o-mini**: also leans fine-grained.

**Synthesis**: Consensus favors single-responsibility, but Gemini's framing is honest: agent inflation is a real cost. **Recommendation: prefer single-responsibility by default; consolidate only when two agents would have genuinely overlapping descriptions.**

### Required structural sections in the body

- **GPT-5**: Prescribes exactly six H2 sections (Scope, Out of scope, Input contract, Output contract, Handoff criteria, Examples).
- **Claude Haiku**: Prescribes Scope & Constraints, Context & Assumptions, Related Subagents, etc.
- **Gemini**: Prescribes `## Description`, `## Tools`, `## System prompt` (but this is really frontmatter + body).
- **Claude Opus**: Recommends headings (Responsibilities, Process, Output Format, Constraints) but doesn't mandate them.

**Synthesis**: GPT-5 and Haiku each invent elaborate schemas. There is no evidence Claude Code itself requires these. **Recommendation: use markdown headings within the system prompt body for readability, but don't mandate a specific set of headings across all subagents. Let each agent's structure fit its task.**

### Versioning fields in frontmatter

- **GPT-5**: Requires `owner`, `timeout_seconds`, `escalate_to`, `commit_preview_required`, etc.
- **Claude Opus, Claude Haiku**: Do not require these fields; they describe the actual minimal schema.

**Synthesis**: GPT-5 extrapolates a much richer schema than Claude Code actually supports. **Recommendation: require only the fields Claude Code recognizes (`name`, `description`, optional `tools`, optional `model`). Treat additional fields as local conventions, not universal rules.**

## 4. Notable Omissions

- **GPT-4o-mini** omits almost every concrete detail: no mention of frontmatter, no specific field names, no discussion of the `description` field's role as routing signal, no concrete length thresholds, no handling of shell/write tool risks specifically. Its rules are generic prompt-hygiene advice that could apply to any document. The absence suggests the model lacks specific knowledge of Claude Code's subagent format.

- **Grok** omits: the routing/delegation purpose of the `description` field, single-responsibility principle, and the distinction between metadata (frontmatter) and system prompt (body). Grok treats the file as a generic "definition" rather than a routing contract.

- **Gemini** omits: guidance on secrets/credentials, model selection, error handling beyond output format, and frontmatter schema specifics. Gemini's model of the file structure (three H2 sections only) is more minimal than the Claude-family description.

- **GPT-5** omits: the critical insight that `description` is consumed by the router/main agent rather than by humans — this is arguably the single most important concept Claude Opus and Haiku raise.

- **Claude Haiku and Grok** omit: explicit discussion of fresh-context isolation (no shared state between main agent and subagent), which Claude Opus correctly flags as a major failure mode.

## 5. Shared Deterministic Checks

### Cross-model checks

- **Check** — Verify the file is located under `.claude/agents/` and has a `.md` extension.
  - **Signal** — File path.
  - **Tool candidate** — ad-hoc (glob + extension test).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — GPT-5 also requires the filename stem to match the `id`/`name`. Claude Opus adds the user-global `~/.claude/agents/` location. Substance agreed.

- **Check** — Verify the file begins with a `---`-delimited YAML frontmatter block that parses as valid YAML.
  - **Signal** — First non-empty lines of raw source; YAML parse result.
  - **Tool candidate** — any YAML parser (`pyyaml`, `js-yaml`).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — Required keys differ (see next check).

- **Check** — Verify required frontmatter keys are present and non-empty.
  - **Signal** — Parsed YAML frontmatter.
  - **Tool candidate** — ad-hoc (schema validator like `jsonschema` or `ajv` with a shared schema).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — Substantial. Opus requires `name` + `description`. Haiku adds `tools` + `model`. GPT-5 requires ~9 fields including `owner`, `timeout_seconds`, `escalate_to`. Grok requires `agent_name` + `version`. **Recommendation: enforce only `name` and `description` as universally required; treat `tools` and `model` as strongly recommended; leave richer schemas to org-specific policy.**

- **Check** — Verify `name` follows a case convention and matches the filename stem.
  - **Signal** — Filename and parsed `name` value.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Convention differs (kebab-case per Opus/GPT-5; CamelCase per Haiku). Filename-stem-match agreed.

- **Check** — Verify `tools` is declared explicitly, is a non-empty list, and contains no wildcards (`*`, `all`, `all_tools`).
  - **Signal** — Parsed YAML `tools` field.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — None in substance. All agree absence or wildcard is a violation.

- **Check** — Verify `description` length is bounded (character or word count).
  - **Signal** — Parsed `description` string.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5 (≤160 chars), Claude Opus (≤400 chars), Claude Haiku (≤100 words).
  - **Variance** — Thresholds differ by ~4×. All agree on the principle; pick a project-level threshold.

- **Check** — Verify system prompt length is bounded (characters or tokens).
  - **Signal** — System prompt text (body or frontmatter field).
  - **Tool candidate** — `tiktoken` for token counting; otherwise ad-hoc byte/char count.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — Thresholds differ (500 tokens / 1500 tokens / 2 KB / 3000 chars). Substance agreed.

- **Check** — Scan for potential secrets (API keys, tokens, private-key headers) in frontmatter and body.
  - **Signal** — Raw source text.
  - **Tool candidate** — `gitleaks`, `trufflehog`, or ad-hoc regex.
  - **Raised by** — GPT-5, Claude Haiku (implicit).
  - **Variance** — GPT-5 gives explicit regex patterns; Haiku treats as policy.

### Singleton checks

- **Check** — Detect pairwise description overlap (lexical or embedding similarity) across all subagents in the directory.
  - **Signal** — All `description` fields.
  - **Tool candidate** — ad-hoc (Jaccard on token sets; embeddings for semantic).
  - **Raised by** — Claude Opus.

- **Check** — Flag subagents whose `name`/`description` matches review/audit/analysis keywords but whose `tools` include `Write` or `Edit`.
  - **Signal** — Parsed frontmatter (`name`, `description`, `tools`).
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Flag subagents granting `Bash`/`sh` whose description lacks justifying keywords (`run`, `execute`, `build`, `test`, `shell`).
  - **Signal** — Parsed `tools` and `description`.
  - **Tool candidate** — ad-hoc keyword match.
  - **Raised by** — Claude Haiku.

- **Check** — Detect system prompt instructions that reference tools not in the declared allowlist (e.g., body says "run `npm test`" but `Bash` is not listed).
  - **Signal** — Parsed `tools` list and system prompt body.
  - **Tool candidate** — ad-hoc (imperative-verb + command name matching).
  - **Raised by** — Claude Haiku.

- **Check** — Verify the system prompt contains an explicit output-format instruction (regex for keywords like "output JSON", "respond only with…", "do not include other text").
  - **Signal** — System prompt body.
  - **Tool candidate** — ad-hoc keyword match.
  - **Raised by** — Gemini.

- **Check** — Flag hedging/apology phrases in the system prompt (`try your best`, `sorry`, `might want to`, `if possible`).
  - **Signal** — System prompt body text.
  - **Tool candidate** — ad-hoc regex (exclude code blocks and quotes).
  - **Raised by** — Claude Opus.

- **Check** — Flag subagents listing `file_delete` (or equivalent destructive tools) without prohibition language in the prompt.
  - **Signal** — Parsed `tools` and system prompt body.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Haiku.

- **Check** — Validate `model` field against an allowed set (`haiku`, `sonnet`, `opus`, or unset) to catch typos like `claude-3-opus`.
  - **Signal** — Parsed `model` field.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verify subagent files under `.claude/agents/` are tracked in git.
  - **Signal** — `git ls-files` output vs. directory listing.
  - **Tool candidate** — ad-hoc git command.
  - **Raised by** — Claude Opus.

- **Check** — Validate each `tools` entry against a central approved-tools manifest.
  - **Signal** — Parsed `tools` list + external manifest file.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

---

## 6. Final Rules File

# Claude Code Subagent Definition Rules

**Scope:** Markdown files under `.claude/agents/` (project) or `~/.claude/agents/` (user) defining custom Claude Code subagents.
**Audience:** Engineers and AI assistants authoring, reviewing, or maintaining subagent definitions.

## File Location and Structure

- **Place subagent definitions in `.claude/agents/` with a `.md` extension.** Claude Code only discovers subagents in these directories.
- **Begin each file with a YAML frontmatter block delimited by `---`.** Frontmatter holds metadata; the markdown body holds the system prompt.
- **Put the system prompt in the markdown body, not inside frontmatter.** Frontmatter is for metadata keys only.
- **Require `name` and `description` as mandatory frontmatter fields.** These are the minimum contract for subagent discovery and routing.
- **Treat `tools` and `model` as strongly recommended frontmatter fields.** Omitting `tools` grants all tools by default.

## Naming

- **Name the file after the subagent's primary role (e.g., `typescript-linter.md`), not generically.** The filename is the first signal of purpose.
- **Use kebab-case for the `name` field, and match the filename stem.** Stable identifiers ease cross-referencing and review.
- **Avoid generic filenames like `agent.md` or `helper.md`.** Specificity aids discoverability.

## Single Responsibility

- **Give each subagent a single, well-defined responsibility.** Overlapping scopes cause non-deterministic routing.
- **Do not duplicate trigger vocabulary across subagents.** If two descriptions match the same prompt, routing becomes a coin flip.

## Description Field

- **Write the description for the routing agent, not for humans.** The main agent uses this text to decide when to delegate; it is a classifier prompt.
- **Start the description with a verb phrase stating the core capability** (e.g., "Generates database migrations for…").
- **Keep the description concise — roughly one to two sentences, ≤ ~400 characters.** Short, specific descriptions route more reliably than long, vague ones.
- **Include explicit trigger conditions when applicable** ("Use when…", "after editing Python files"). These are load-bearing, not decorative.
- **Use `PROACTIVELY` or `MUST BE USED` only when the subagent should self-invoke without explicit request.** Without these keywords, Claude delegates only on explicit mention.

## Tools and Least Privilege

- **Declare the `tools` field explicitly; never omit it and never use wildcards (`*`, `all`).** Omission grants all tools, violating least privilege.
- **Grant only the tools the subagent actually uses.** A reviewer needs `Read`, `Grep`, `Glob` — not `Write` or `Bash`.
- **Do not grant `Write` or `Edit` to review, analysis, or reporting subagents.** Read-only intent requires read-only tools.
- **Do not grant `Bash` unless the subagent's core job requires shell execution.** Bash is the widest attack surface.
- **If granting `Bash`, enumerate allowed commands and prohibited actions in the system prompt.** Defense in depth beyond the tool allowlist.
- **Declare path constraints on file-modifying tools when the tool supports them.** Narrowing paths prevents accidental edits to unrelated files.
- **Do not include instructions in the system prompt that require tools not in the allowlist.** "Run `npm test`" without `Bash` is a self-contradiction.

## System Prompt Body

- **Open the prompt with a one-line role or goal statement** ("You are a …"). Anchors the model before instructions.
- **Write instructions in the imperative mood.** "Run the tests," not "You should probably run the tests."
- **Do not hedge or apologize** ("try your best," "unfortunately"). Hedging licenses mediocre output.
- **Structure longer prompts with markdown headings** (Responsibilities, Process, Output Format, Constraints). Headings aid mid-task retrieval.
- **Mandate a specific, machine-parsable output format.** Downstream callers parse the response; unstructured prose breaks automation.
- **Include at least one concrete input/output example when the task is ambiguous.** Few-shot examples outperform abstract instructions — but they cost tokens, so use sparingly.
- **Define how the subagent should behave on failure, ambiguity, or missing access.** Report the blocker clearly; do not flail into workarounds.
- **Do not assume prior conversation state or shared context.** Subagents run in fresh contexts; "continue what we were doing" has no referent.
- **Keep the system prompt bounded — target ≤ ~1500 tokens; hard-fail above ~3000 characters / ~2 KB.** Long prompts dilute focus, increase cost and latency, and consume the subagent's own context budget.
- **Do not interpolate untrusted user input into the prompt without escaping.** Raw interpolation is a prompt-injection surface.

## Model Selection

- **Omit the `model` field to inherit the session default unless there is a specific reason to override.** Explicit overrides should be intentional.
- **Use `haiku` for mechanical, high-volume tasks** (formatters, simple extractors). It is cheaper and fast enough.
- **Reserve `opus` for subagents doing genuinely hard reasoning.** Default-to-opus wastes budget.

## Safety

- **Do not embed secrets, API keys, tokens, or credentials in the file.** Version-controlled secrets are hard to purge.
- **Forbid destructive operations explicitly in the system prompt when the tool allows them** (e.g., prohibit deletion when `file_delete` is granted). Defense in depth.
- **Require a review or confirmation step for subagents that can modify sensitive files** (config, secrets, deployment manifests).

## Repository Hygiene

- **Commit project subagents to version control under `.claude/agents/`.** Team subagents are shared infrastructure.
- **Do not commit personal subagents (`~/.claude/agents/`) to the project repo.** Scope matters.
- **Document non-obvious or composed subagents in the project README.** Discoverability matters when routing is implicit.
- **Mark deprecated subagents rather than deleting them, and point to a replacement.** Allows graceful migration.
- **Bump a version and document breaking changes when scope or tools change significantly.** Consumers need to know when their delegations may break.