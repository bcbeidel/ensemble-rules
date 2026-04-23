# Synthesis of Agent Skills Best-Practices Guidance

## 1. Consensus Rules

### Structure & File Layout

- **Name the file `SKILL.md` and place it in a dedicated skill directory.** (substantively similar but differently worded across GPT-5, Claude Opus, Gemini) — Standard, discoverable naming enables tooling and agent loaders to find skills without configuration.

- **Begin with YAML frontmatter containing at minimum `name`, `description`, and `version`.** (substantively similar across GPT-5, Claude Opus; Gemini uses H2 sections instead) — Structured metadata is the discovery and routing signal; without it, skills cannot be reliably indexed.

- **Use a consistent set of required H2 sections (e.g., When to use, Prerequisites, Steps/Instructions, Failure modes, Examples) in a predictable order.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Predictable structure aids both model retrieval and human review.

- **Keep the SKILL.md short; cap around 300–400 lines and move reference detail to sibling files.** (substantively similar across GPT-5 (400), Claude Opus (300), Grok (2000 words)) — Every line is paid for in context tokens on invocation; long skills degrade both model focus and review quality.

- **Use a lowercase, hyphen/kebab-case name as the unique identifier.** (near-identical wording across GPT-5 and Claude Opus) — Portable, machine-safe identifiers for routing and lookup.

- **Write the Steps/Instructions section as a numbered ordered list, one atomic action per step.** (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — Models follow numbered sequences more reliably than prose or bullets.

### Descriptions & Triggers

- **Write the description to enumerate concrete invocation triggers, not capabilities.** (substantively similar across Claude Opus, Claude Haiku, Gemini, Grok) — The description is the retrieval signal; "Use when the user asks to convert .csv to .parquet" beats "Handles tabular conversion."

- **Provide an explicit "When to use" section with scannable, concrete conditions.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Reduces misrouting and skill collisions; vague triggers are the top cause of wrong-skill invocation.

### Instructions & Clarity

- **Write steps in imperative, active voice addressed to the agent.** (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Grok) — Reduces hedging, ambiguous pronouns, and passive-voice mis-parsing.

- **State preconditions explicitly and check them in the first step.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Assumed state is the single biggest source of silent skill failures; fail fast.

- **Include at least one worked example with inputs, outputs, and side effects.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Concrete examples anchor the model better than abstract rules.

- **Ban vague/hedging language (e.g., "etc.", "maybe", "generally", vague pronouns).** (substantively similar across GPT-5, Claude Opus, Grok) — Ambiguity propagates directly into model behavior.

### Safety

- **Never embed secrets, API keys, or credentials; reference environment variables or vault paths instead.** (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Grok) — Skills are version-controlled documentation; a committed credential is a breach.

- **Require explicit user confirmation (or human-approval gating) before any destructive or production-affecting operation.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Agents execute what they read; irreversible actions must be human-gated.

- **Prefer dry-run or preview steps before executing destructive variants.** (substantively similar across Claude Opus, Gemini) — "Show the plan, then apply" is the safe-by-default pattern.

- **Do not use unverified remote-execution patterns (e.g., `curl | bash`, `eval` of remote content).** (substantively similar across Claude Opus, Gemini) — These are supply-chain vectors; pin versions and verify hashes instead.

### Error Handling & Dependencies

- **Declare expected failure modes and recovery actions for any step that can fail externally.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Without explicit guidance, the agent invents recovery behavior.

- **Declare all external dependencies (tools, APIs, env vars, versions) in a Prerequisites section.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Undeclared dependencies surface as confusing runtime errors.

- **Specify explicit timeouts and retry/backoff parameters for polling, waits, and retries.** (near-identical wording across GPT-5, Claude Haiku, Gemini) — Without limits, agents can hang indefinitely or retry-storm.

### Versioning & Ownership

- **Include an `owner` field and bump `version` (semver) on material changes.** (substantively similar across GPT-5, Claude Opus) — Unowned skills rot; version bumps are the cache-busting signal consumers rely on.

### Style

- **Use fenced code blocks with language tags for all commands and code.** (substantively similar across Claude Opus, Claude Haiku) — Aids both parser and model in distinguishing executable content.

- **Keep lines under ~120 characters where practical.** (near-identical wording across GPT-5 and Claude Opus) — Improves diff readability; soft rule excluding code/URLs.

## 2. Strong Minority Rules

- **Scope discipline: one skill per workflow; split rather than branch at the top level.** (Claude Opus, Claude Haiku) — Kitchen-sink skills degrade retrieval (too-broad description) and execution (wrong branch selection). This is an important maintainability lever and worth keeping even though it requires judgment.

- **Don't have skills invoke other skills.** (Claude Opus, contested) — Cross-skill calls create hidden coupling and break the independent-capability mental model. Worth including as a default with explicit contestation noted.

- **Include a "Do not use when" list alongside "Use when".** (GPT-5) — Negative triggers measurably improve dispatcher accuracy and prevent collisions. A small authoring cost for significant routing benefit.

- **Include a final verification step that confirms the desired outcome was achieved.** (Gemini) — Transforms a skill from blind instructions into a self-validating procedure; directly addresses the silent-failure mode that multiple models flagged.

- **Filter and reduce command output early in pipelines; return minimal data to the agent.** (Gemini) — Performance rule specific to agent context: verbose output pollutes the context window and degrades subsequent reasoning. Unique and practical.

- **Use non-interactive flags (`-y`, `BatchMode=yes`, etc.) for commands that might prompt.** (Gemini) — Prevents agent execution from stalling on interactive prompts — a concrete, mechanically checkable rule worth preserving.

- **Declare privilege level and required IAM/RBAC roles at the top.** (Claude Haiku) — For skills operating in production or with elevated access, making blast radius visible at the top of the file is a high-value safety gate.

- **Log state-changing actions with timestamp, actor, reason, and old/new values.** (Claude Haiku) — Auditability is often overlooked in agent workflows; worth including for any skill that mutates state.

- **Reference bundled files only by relative path from the skill directory.** (Claude Opus) — Critical for portability; absolute paths break the skill immediately on relocation.

## 3. Divergences

### Metadata richness: minimal vs. extensive frontmatter

- **GPT-5** prescribes an extensive required frontmatter set (~18 fields including `safety_tier`, `cost_budget_usd`, `llm_token_budget`, `retry_policy`, `data_access`, `idempotent`, etc.).
- **Claude Opus** argues for minimal frontmatter (`name`, `description`, `version`, plus `owner`), with everything else expressed in prose sections.
- **Gemini** uses H2 sections rather than frontmatter for all metadata.
- **Claude Haiku, Grok** are in between.

**Recommendation:** Require a small, mandatory core (`name`, `description`, `version`, `owner`) and treat richer fields as optional-but-standardized. Rich frontmatter helps tooling but raises authoring friction; the core four are non-negotiable, the rest should be conventions a team opts into. GPT-5's schema is a reasonable reference for teams that need policy gating.

### File length cap

- **Claude Opus** says 300 lines; **GPT-5** says 400; **Grok** says 2000 words (~300 lines).
- All three flag this as somewhat arbitrary.

**Recommendation:** Use 300 lines as the default cap with 400 as a hard ceiling. The exact number matters less than having a bright line that triggers the "split this skill" conversation.

### Code blocks embedded in the skill vs. externalized scripts

- **Claude Opus, Gemini** recommend externalizing complex scripts into sibling files referenced by relative path.
- **GPT-5, Claude Haiku** allow inline code blocks without a strict ceiling.

**Recommendation:** Externalize any shell block over ~10 lines. Inline commands are fine for single-line invocations; longer logic belongs in a tested, versioned script file. This matches both portability and testability goals.

### How prescriptive to be about ambiguous language bans

- **GPT-5, Grok** list specific banned words ("etc.", "maybe", "somehow", "TBD", "???").
- **Claude Opus** targets pronoun ambiguity rather than word lists.
- **Others** gesture at clarity without a specific list.

**Recommendation:** Ban both — specific hedging words (mechanically checkable) and unqualified pronouns (requires review). The banned-word list is easy to enforce; the pronoun rule is a style principle for human reviewers.

### Parameterized vs. single-purpose skills

- **Claude Opus, Claude Haiku** prefer single-purpose skills; branching indicates a split.
- **Gemini** takes a middle ground: a skill is a "single logical workflow" that may include multiple steps.
- **Grok** does not take a position.

**Recommendation:** Prefer single-purpose, but allow parameterization where the branches are shallow (e.g., `region` as a parameter) and the workflow is genuinely the same. If the top-level step sequence diverges, split.

## 4. Notable Omissions

- **GPT-4o-mini and Grok omit numbered-step instructions specifics and most structural requirements** that the other four models converge on (required section order, frontmatter fields, concrete trigger enumeration). These responses are notably shallower and less opinionated than the others; their omissions don't carry strong signal.

- **Claude Opus omits explicit performance budgets (token budgets, cost budgets, timeout declarations as frontmatter).** Given Claude Opus's otherwise thorough treatment, this appears to be a deliberate stance that performance is a review-time concern, not a per-skill declared constraint. A defensible minority position.

- **Gemini omits versioning and ownership entirely.** Conspicuous given four other models flagged it. Given Gemini's otherwise thoughtful treatment, this reads as an oversight worth correcting rather than a principled position.

- **GPT-5 omits the "one skill per workflow / scope discipline" rule** that Claude Opus and Claude Haiku both emphasize. Worth noting because scope creep is a real maintainability failure mode.

- **Claude Haiku omits explicit guidance on file length.** Given the other four models' convergence on a cap, this absence weakens the signal slightly but doesn't undermine the consensus.

- **GPT-4o-mini omits almost all concrete guidance** (trigger enumeration, example inclusion, semver, secret handling, dependency declaration). This is not a disagreement — it's a shallower response. Its rules are too generic ("use consistent naming") to meaningfully contradict the others.

## 5. Shared Deterministic Checks

### Shared checks (raised by multiple models)

- **Check** — Verify the skill file is named exactly `SKILL.md` (case-sensitive).
  - **Signal** — Filename on disk.
  - **Tool candidate** — ad-hoc (trivial filename comparison).
  - **Raised by** — GPT-5, Gemini.
  - **Variance** — None; models agreed on exact match.

- **Check** — Parse YAML frontmatter and assert presence of required keys.
  - **Signal** — First bytes of file; YAML block delimited by `---`.
  - **Tool candidate** — any YAML parser (PyYAML, js-yaml) plus schema validator; could use `yamllint` for syntactic layer.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Required key set differs: GPT-5 requires ~18 fields; Claude Opus requires 3–4. Resolve by making the core four (`name`, `description`, `version`, `owner`) mandatory and the rest configurable.

- **Check** — Verify `name` / skill slug matches `^[a-z0-9]+(-[a-z0-9]+)*$` (lowercase kebab-case).
  - **Signal** — Parsed frontmatter.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — Claude Opus adds a 64-char cap and a uniqueness check across the collection; others only check format. Recommend both.

- **Check** — Verify required H2 section headings are present (and optionally in a specified order).
  - **Signal** — Parsed Markdown AST, H2 nodes in document order.
  - **Tool candidate** — any Markdown AST library (remark, markdown-it, mistune); `markdownlint` does not enforce heading names natively.
  - **Raised by** — GPT-5, Claude Opus, Gemini, Grok.
  - **Variance** — Section names differ (GPT-5: Overview/When to use/Preconditions/Inputs/Outputs/Steps/Error handling/Safety/Tools/Examples; Claude Opus: When to use/Prerequisites/Steps/Failure modes/Examples; Gemini: Name/Description/When to Use/Instructions). Order-enforcement strictness varies. Recommend configurable section list with order enforcement on by default.

- **Check** — Verify total line count is under the configured cap (default 300–400).
  - **Signal** — Raw file line count.
  - **Tool candidate** — `wc -l` or equivalent.
  - **Raised by** — GPT-5 (400), Claude Opus (300), Grok (2000 words).
  - **Variance** — Threshold differs. Recommend 300 warn / 400 fail as defaults with opt-out comment marker.

- **Check** — Verify the Steps/Instructions section is an ordered list, starting at 1 with sequential numbering.
  - **Signal** — Markdown AST nodes under the Steps heading.
  - **Tool candidate** — any Markdown AST parser; `markdownlint` rules MD029/MD030 cover list numbering partially.
  - **Raised by** — GPT-5, Claude Opus, Gemini, Grok.
  - **Variance** — GPT-5 requires strict 1..N increment; Claude Opus requires just "first block is ordered list"; Gemini similar to Claude. Recommend Claude's check plus GPT-5's sequential-numbering check.

- **Check** — Scan for embedded secrets (API keys, tokens, private keys, passwords).
  - **Signal** — Raw text of SKILL.md and bundled files.
  - **Tool candidate** — `gitleaks detect`, `trufflehog filesystem`, or `detect-secrets scan`.
  - **Raised by** — Claude Opus, Claude Haiku.
  - **Variance** — None on approach; models agreed on using off-the-shelf scanners. Both note false-positive handling via allowlists.

- **Check** — Detect unverified remote-execution patterns (`curl | bash`, `eval $(curl ...)`, etc.).
  - **Signal** — Text of fenced code blocks.
  - **Tool candidate** — ad-hoc regex set; `shellcheck` does not flag this directly.
  - **Raised by** — Claude Opus, Gemini.
  - **Variance** — None substantive.

- **Check** — Verify `version` field matches semver (`MAJOR.MINOR.PATCH`).
  - **Signal** — Parsed frontmatter.
  - **Tool candidate** — `semver` validator library or regex `^\d+\.\d+\.\d+$`.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Claude Opus additionally requires version bump on material changes (requires git context); GPT-5 checks format only.

- **Check** — Verify Examples section contains at least one fenced code block.
  - **Signal** — Markdown AST under the Examples heading.
  - **Tool candidate** — Markdown AST parser.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 requires one input JSON block and one output JSON block; Claude Opus requires any fenced block; Haiku requires inputs, outputs, and side effects all present. Recommend "at least one fenced block" as floor, with richer structural checks as opt-in.

- **Check** — Detect destructive shell commands (`rm`, `mv`, `dd`, `drop`, `truncate`) lacking safety flags or prior approval gates.
  - **Signal** — Text content of shell code blocks.
  - **Tool candidate** — ad-hoc regex; no off-the-shelf linter covers this.
  - **Raised by** — Claude Haiku, Gemini.
  - **Variance** — Haiku pairs detection with an "approval gate" check (look for approval keywords in preceding steps); Gemini checks for dry-run/interactive flags. Recommend both checks combined.

- **Check** — Detect polling/retry/wait language without explicit timeout and backoff parameters.
  - **Signal** — Raw text or parsed steps.
  - **Tool candidate** — ad-hoc keyword+regex matching.
  - **Raised by** — GPT-5, Claude Haiku, Gemini.
  - **Variance** — All three propose similar keyword lists (poll, wait, retry, loop). Fragile to phrasing.

- **Check** — Scan for banned hedging/filler words (`etc.`, `maybe`, `probably`, `somehow`, `TBD`, `???`).
  - **Signal** — Raw source text (case-insensitive whole-word match).
  - **Tool candidate** — ad-hoc regex; `vale` with a custom style could work.
  - **Raised by** — GPT-5, Grok.
  - **Variance** — Minor list differences; GPT-5's is more comprehensive.

- **Check** — Verify line length ≤ 120 characters (excluding fenced code blocks and URLs).
  - **Signal** — Raw source text.
  - **Tool candidate** — `markdownlint` MD013.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — None.

- **Check** — Verify every fenced code block has a non-empty language tag.
  - **Signal** — Markdown AST.
  - **Tool candidate** — `markdownlint` MD040.
  - **Raised by** — Claude Opus (and implicit in Claude Haiku).
  - **Variance** — None.

- **Check** — Placeholder token hygiene: every `{{inputs.X}}` / `{{env.Y}}` reference resolves to a declared input or env var.
  - **Signal** — Raw source text + parsed frontmatter.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.
  - **Variance** — Only GPT-5 defines this, but it's directly useful wherever placeholder syntax is used.

### Singleton checks worth extracting

- **Check** — Verify the parent directory basename equals the `name` field (after lowercasing).
  - **Signal** — Filesystem + parsed frontmatter.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Compute pairwise `description` similarity across the skill collection and flag pairs above a threshold for human review.
  - **Signal** — All `description` strings across the skill collection.
  - **Tool candidate** — ad-hoc Jaccard or embedding-based similarity.
  - **Raised by** — Claude Opus.

- **Check** — Ensure inline backticked `tool.operation` references resolve to a declared tool and operation in the frontmatter.
  - **Signal** — Markdown inline code spans + parsed frontmatter.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — If `requires_human_approval: true`, ensure a step contains an explicit `[HUMAN-APPROVAL]` marker.
  - **Signal** — Frontmatter + raw text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — If `idempotent: false`, ensure the Error handling section contains compensation/rollback language.
  - **Signal** — Frontmatter + raw text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Detect common interactive-prompt commands (`apt-get install` without `-y`, `ssh` without `BatchMode=yes`, etc.).
  - **Signal** — Shell code block contents.
  - **Tool candidate** — ad-hoc; partially covered by `shellcheck` via SC2086-adjacent rules but not this class directly.
  - **Raised by** — Gemini.

- **Check** — Cap description length at ~500 characters.
  - **Signal** — Parsed frontmatter.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — If an input is an array type, require a `batch_size` declaration.
  - **Signal** — Parsed frontmatter.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Line-count shell code blocks in the Instructions section; flag any block over ~10 lines for externalization.
  - **Signal** — Markdown AST code nodes.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Gemini.

---

## 6. Final Rules File

# Agent Skills: Authoring Rules

**Scope:** Authoring and reviewing `SKILL.md` files and their bundled assets — reusable, model-invocable workflow definitions.
**Audience:** Engineers, reviewers, and AI coding assistants producing or modifying skills.

## Structure & Packaging

- **Name the file `SKILL.md` and place it in a dedicated directory named after the skill.** Standard layout is the unit of packaging; loaders depend on it.
- **Name the parent directory to match the skill's `name` field (lowercased).** Directory and identifier should not drift.
- **Begin the file with YAML frontmatter delimited by `---`.** Required keys: `name`, `description`, `version`, `owner`. Optional-but-recommended: `safety_tier`, `requires_human_approval`, `timeout_seconds`, `env_vars`, `inputs`, `outputs`, `last_updated`, `changelog`.
- **Use a lowercase kebab-case `name` matching `^[a-z0-9]+(-[a-z0-9]+)*$`, ≤ 64 characters, unique across the skill collection.** Names are stable identifiers, not marketing.
- **Use semantic versioning (`MAJOR.MINOR.PATCH`) in `version`.** Bump on any material change to steps, description, or bundled executables.
- **Include an `owner` field identifying a resolvable person or team.** Unowned skills rot.
- **Keep `SKILL.md` under 300 lines (hard cap 400).** Every line is paid for in context tokens on invocation; longer skills degrade both model focus and review quality. If you exceed the cap, split the skill or move reference detail to sibling files.
- **Structure the body with these H2 sections, in order:** `## When to use`, `## Prerequisites`, `## Steps`, `## Failure modes`, `## Examples`. Additional H2 sections (`## Safety`, `## Outputs`) are permitted between them.
- **Reference bundled files by relative path from the skill directory.** Absolute paths (`/home/...`, `~/...`, `C:\...`) break portability.

## Description & Triggers

- **Write the `description` to enumerate concrete invocation triggers, not capabilities.** Start with "Use when..." and name specific user phrases, file extensions, error strings, or event types. "Use when the user asks to convert .csv to .parquet" beats "Handles tabular conversion."
- **Cap `description` at ~500 characters.** Longer descriptions dilute the retrieval signal.
- **Provide an explicit `## When to use` section with both positive triggers and "Do not use when" conditions**, each with at least three concrete bullets. Negative triggers measurably reduce misrouting.
- **Don't create skills whose descriptions substantially overlap with another skill's.** Overlap forces arbitrary selection.

## Scope

- **Write one skill per workflow.** If the top-level logic branches ("if X do A, else B"), split into separate skills.
- **Don't have skills invoke other skills.** *(contested)* Cross-skill calls create hidden coupling; prefer composition at the agent level.

## Instructions

- **Write `## Steps` as a numbered ordered list, starting at 1, with sequential increments, one atomic action per step.** Numbered sequences are followed more reliably than bullets or prose.
- **Write each step in imperative, active voice addressed to the agent.** "Run `foo`" — not "The agent should run foo" or "foo is run."
- **Include the exact command or code to execute, not a description of it.** Models copy-paste better than they translate.
- **State preconditions explicitly in `## Prerequisites` and verify them in step 1.** Assumed state is the top cause of silent skill failures. Fail fast with a clear error message.
- **Don't use pronouns ("it", "this", "that") without an unambiguous nearby referent.** Pronoun ambiguity measurably degrades instruction-following.
- **Include a final verification step that confirms the desired outcome was achieved.** Without explicit verification, skills silently "succeed" without doing the job.
- **Don't nest conditional logic more than two levels deep.** Deeper branching belongs in separate skills.
- **Externalize shell blocks over ~10 lines into sibling scripts.** Keeps `SKILL.md` focused on workflow; makes scripts independently testable.

## Safety

- **Never embed secrets, API keys, tokens, or credentials in the skill or bundled files.** Reference environment variables or vault paths by name only.
- **Require explicit user confirmation before any destructive or production-affecting operation** (file deletion, force push, database drop, production deploy, secret rotation). Agents execute what they read.
- **Prefer dry-run or preview as the default step, with the destructive variant as a human-gated follow-up.** "Show the plan, then apply" is the safe-by-default pattern.
- **Don't use destructive shell commands (`rm`, `mv`, `dd`, `drop`, `truncate`) without a safe flag** (`-i`, `--dry-run`) or a preceding approval gate.
- **Don't include unverified remote-execution patterns** (`curl | bash`, `eval $(curl ...)`, `source <(curl ...)`). If a skill needs a remote tool, pin a version and verify a hash.
- **Scope file operations to the working directory or paths the user has explicitly named.** Skills that touch `$HOME`, `/etc`, or parent directories without explicit user direction are bugs.
- **Declare privilege level and required IAM/RBAC roles in `## Prerequisites`** for skills that access elevated systems. Blast radius must be visible.
- **Log state-changing actions with timestamp, actor, reason, and old/new values** for any skill that mutates persistent state. Auditability is not optional.

## Dependencies & Environment

- **Declare all required tools, language versions, OS assumptions, and env vars in `## Prerequisites`.** Undeclared dependencies surface as confusing runtime errors.
- **Check for tool availability in step 1 with a command that fails loudly** (e.g., `command -v foo >/dev/null || { echo "foo required"; exit 1; }`). Fail fast beats fail weird.
- **Pin versions for anything where behavior has shifted across releases** (e.g., `ffmpeg >= 6`, `python >= 3.11`). Floating versions rot silently.

## Failure Handling

- **Include a `## Failure modes` section listing at least the three most likely failures and their recovery actions.** Without this, the agent invents recovery behavior.
- **For every step that can fail externally (network, filesystem, subprocess), specify what to do on failure.** "Retry once then surface the error" is a fine default.
- **Declare explicit timeouts and retry/backoff parameters for polling, waits, and retries.** "Poll every 10s for up to 5 minutes, then return `status=timeout`" — not "poll until done."
- **Don't swallow errors in bundled scripts.** Exit non-zero with a message naming the failing step.

## Performance

- **Set timeouts (and, where relevant, token or cost budgets) explicitly.** Caps runaway latency and cost.
- **Filter and reduce command output early in pipelines; return minimal data to the agent.** Verbose output pollutes the context window and degrades subsequent reasoning.
- **Use non-interactive flags for all commands that might prompt** (`apt-get install -y`, `ssh -o BatchMode=yes`, etc.). Prevents the agent from stalling on an unexpected prompt.
- **Warn when a step is O(n) in some parameter** and call out scale expectations ("~1s per 10k rows"). Prevents unexpected long-running invocations.

## Examples

- **Provide at least one worked example with concrete inputs, expected outputs, and observable side effects.** Abstract rules alone do not anchor model behavior.
- **Use fenced code blocks with explicit language tags** (` ```bash `, ` ```json `) for all commands, code, and structured examples.

## Style

- **Ban hedging and filler words**: `etc.`, `maybe`, `probably`, `somehow`, `generally`, `sometimes`, `TBD`, `???`. Ambiguity propagates directly into model behavior.
- **Use ATX-style headings (`##`) consistently.** Mixed heading styles break some parsers.
- **Keep lines under 120 characters where practical**, excluding code blocks and URLs. Improves diff readability.
- **Write in plain English; define domain jargon on first use.** Don't assume the agent shares your team's shorthand.
- **Use consistent terminology across skills.** If one skill uses `service_name`, don't call it `svc` or `service_id` elsewhere.
- **Don't embed design rationale or commentary inside the step sequence.** Reasoning belongs in a separate section or a design doc.

## Versioning & Maintenance

- **Update `last_updated` (ISO 8601 date) and append to `changelog` on every material change.** Preserves auditability and enables staleness detection.
- **Bump `version` when `## Steps`, `description`, or bundled executables change.** Consumers and caches rely on version changes as cache-busting signals.
- **Date-stamp or version-stamp references to external APIs in comments.** Makes staleness detectable during review.