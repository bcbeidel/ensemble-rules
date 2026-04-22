## 1. Consensus Rules

### Structure & Scoping

- **Use YAML frontmatter with `paths:` to scope rules narrowly.** Without path scoping, rules either never load or always load, wasting tokens and diluting signal. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Scope path globs as narrowly as the rule genuinely applies.** Over-scoping burns tokens and pollutes context; under-scoping misses edits. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Keep each rule file single-purpose / single-topic.** Mixed-topic files defeat path scoping and complicate maintenance. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Cap file size to protect the context budget** (GPT-5: ~120 lines/4 KB; Claude Opus: 200 lines; Claude Haiku: 2500 chars; Grok: 5 KB). Every loaded byte costs tokens on every turn. *(substantively similar; specific limits differ)*

- **Prefer many small, narrowly-scoped files over one monolithic document.** Easier to maintain, load, and own. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Content & Phrasing

- **Write each rule as a single imperative sentence.** Imperative mood is shorter, less ambiguous, and parses more reliably than hedged or second-person prose. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini — strong convergence suggesting shared prior art)*

- **Follow each rule with at most one line of rationale.** Explains "why" to human maintainers without bloating the AI's prompt. *(near-identical across GPT-5, Claude Opus, Gemini)*

- **Make rules falsifiable / mechanically checkable.** A reviewer should be able to point at a diff and say violated/not-violated; vague rules ("be readable") are noise. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Don't hedge** ("usually", "consider", "prefer", "where appropriate"). Hedging invites noncompliance; state rules absolutely and list exceptions explicitly. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

- **Encode only conventions the codebase actually follows today; avoid aspirational rules.** Aspirational rules cause agents to rewrite compliant code or train readers to ignore the file. *(substantively similar across Claude Opus, Claude Haiku)* — but strongly endorsed and worth promoting to consensus.

### Safety

- **Never include secrets, API keys, tokens, or credentials in rule files.** Rule files are logged, shared, and trusted; they are a prompt-injection and leak surface. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*

- **Explicitly forbid destructive operations without human confirmation** (`rm -rf`, force-push, `DROP TABLE`, production deploys, migrations). Agents default to helpful, not cautious. *(substantively similar across GPT-5, Claude Opus, Grok)*

- **Frame rules as guardrails, not shortcuts.** Rules must add constraints enforcing best practices, never weaken security, validation, or logging. *(substantively similar across GPT-5, Claude Opus, Gemini)*

### Maintainability

- **Assign ownership and review rule files periodically** (GPT-5: ≤6 months, Haiku: quarterly, Gemini: periodically). Stale rules mislead agents with full confidence and erode trust in the whole system. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Treat rule files as code: subject to review, versioning, and deletion.** Ensures correctness and team consensus before rules take effect. *(substantively similar across GPT-5, Claude Opus, Gemini)*

- **Don't duplicate what a formatter, linter, or CI check already enforces.** Redundant rules waste tokens and diverge from tooling. *(substantively similar across Claude Opus, Claude Haiku)* — flagged as contested by Claude Opus but majority view.

### Performance

- **Keep rules concise and deduplicated; link to canonical docs rather than embedding them.** Protects context budget and prevents doc drift. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

## 2. Strong Minority Rules

- **Define explicit precedence for overlapping rule files** (GPT-5, Claude Opus). When two files match the same path, nondeterministic agent behavior results unless precedence is spelled out. Critical for multi-file rule systems; worth keeping.

- **Use negative rules for behaviors the base model defaults to** (Claude Opus). "Don't catch bare `Exception`" preempts the highest-probability mistakes; complements positive guidance. A specific, testable insight unique to Opus.

- **Delete rules that merged code violates more than 2–3 times** (Claude Opus, Claude Haiku). An enforceable decision rule for pruning — converts the vague "review periodically" into an actionable trigger.

- **Validate rule files in CI: check frontmatter, zero-match globs, banned hedging words, size caps** (GPT-5). Automation prevents orphan and rotten rules; the only response with concrete tooling guidance.

- **Don't paste untrusted external content (issue bodies, third-party docs) into rule files** (Claude Opus). Rule files are a trusted-instruction channel and therefore a prompt-injection vector. Security-critical and underappreciated.

- **Start agent responses by restating which rules apply** (GPT-5). Self-check mechanism that helps reviewers audit compliance; uniquely operational.

- **Name exact modules/functions, not vague categories** (Claude Opus). "Use `@/lib/log.ts` `log.info()`" beats "use our logger" — specificity makes rules actionable.

- **When rules conflict or are impossible to satisfy, stop and ask owners** (GPT-5). Deterministic escalation beats guessing; a clean "when in doubt" fallback.

## 3. Divergences

### Rule file format/location
- **GPT-5**: prescribes `.claude/rules/` with specific naming conventions.
- **Claude Opus**: tool-agnostic (`.claude/rules/`, `.cursor/rules/`, `**/AGENTS.md`).
- **Others**: vague or unspecified.
- **Recommendation**: Tool-agnostic. Rule files should work across assistants; pinning to a single vendor folder is premature.

### Inline examples
- **GPT-5**: put examples in separate `.claude/examples/` files.
- **Claude Opus**: include minimal examples only when rule shape is non-obvious (contested).
- **Gemini**: short code examples for complex rules.
- **Grok**: examples ≤1 line.
- **Recommendation**: Allow minimal inline examples when rule shape is non-obvious, but keep them short. Externalize larger examples.

### Auto-execution of commands
- **GPT-5**: propose, don't execute (marked contested).
- **Claude Opus**: require human confirmation for destructive operations only.
- **Recommendation**: Opus's position. Blanket no-execution is too restrictive; scoped confirmation for destructive/irreversible actions is the right balance.

### Whether to duplicate formatter/linter rules
- **Claude Haiku, Gemini (implicit), Claude Opus (majority)**: don't duplicate.
- **Claude Opus**: notes belt-and-suspenders view exists.
- **Recommendation**: Don't duplicate. Tooling is the enforcement mechanism; rules should encode semantics beyond tool reach.

### Positive vs. negative framing
- **Gemini**: prefer positive ("use named exports"); marked contested.
- **Claude Opus**: prefer negative for base-model defaults.
- **Recommendation**: Both have merit. Default to positive framing; use negative rules specifically to counter model default behaviors.

### File size limits
- GPT-5: 120 lines / 4 KB; Claude Opus: 200 lines; Claude Haiku: 2.5 KB; Grok: 5 KB.
- **Recommendation**: Aim for under ~200 lines or ~5 KB as soft cap. Specific number matters less than the discipline of splitting.

### Line-length / style micro-rules
- **Grok**: 80-char max, no conditional logic in rules.
- **Others**: silent.
- **Recommendation**: Skip. Overly prescriptive for rule files themselves; let formatters handle it.

## 4. Notable Omissions

- **GPT-4o-mini and Grok omit the "avoid aspirational rules" principle** present in Opus, Haiku, and implicit in Gemini. This is one of the highest-leverage rules in the set; its absence is a real gap.

- **GPT-4o-mini omits path scoping entirely** — the central mechanism of path-scoped rule files. Striking absence given the prompt explicitly frames the topic around scoping.

- **GPT-4o-mini omits file size / token budget discussion** present in all four other responses. Performance-in-context was a core concern everywhere else.

- **Gemini and Grok omit explicit conflict-resolution / precedence rules** that GPT-5 and Claude Opus emphasize. For systems with multiple rule files, this is essential.

- **Claude Haiku and GPT-4o-mini omit destructive-command safeguards** (rm -rf, DROP, force-push). Given agents' readiness to execute, this is a safety-critical omission.

- **Grok omits "treat rule files as code / review them"** — the primary lifecycle mechanism in other responses.

- **GPT-4o-mini omits the "falsifiable rule" principle** — central to Opus, Haiku, and Gemini. Its absence reduces the file to vague aspirations.

- **Only GPT-5 and Claude Opus mention prompt-injection / untrusted content risk.** Underweighted across the field given rule files are trusted-instruction channels.

## 5. Final Rules File

```markdown
---
description: Best practices for authoring path-scoped agent rule files consumed by AI coding assistants
paths: [".claude/rules/**/*.md", ".cursor/rules/**/*.md", "**/AGENTS.md", ".agent/rules/**/*.md"]
---

# Agent Rule Files

**Scope:** Markdown files loaded conditionally by AI coding assistants to encode project-specific conventions.
**Audience:** Engineers authoring or reviewing these files, and AI assistants consuming them.

---

## Structure & Scoping

- Begin every file with YAML frontmatter containing at minimum `description` and `paths`. Without scope metadata the file either never loads or always loads — both defeat the purpose.
- Write `paths` globs as narrowly as the rule actually applies, and no narrower. Over-scoping wastes tokens; under-scoping misses edits.
- Give each file a single responsibility (one subsystem or one concern). Mixed-topic files defeat path scoping.
- Prefer many small, narrowly-scoped files over one monolithic document. Easier to load, own, and update.
- Cap each file at roughly 200 lines or 5 KB of active guidance. Longer files get truncated or ignored in the tail.
- Don't use `paths: "**/*"` in a path-scoped file. Universally-applicable guidance belongs in top-level memory (e.g., `CLAUDE.md`, `AGENTS.md`).
- Name files to reflect scope and purpose (e.g., `python-payments.md`, `react-component-props.md`). Clear naming aids discovery.
- Open each file with a one-line scope statement naming the code it governs. Agents prioritize the first tokens.

## Content & Phrasing

- Write every rule as a single imperative sentence ("Use X", "Return early on error"). Shorter, less ambiguous, parses reliably.
- Append at most one line of rationale per rule. More than that belongs in a design doc and should be linked, not pasted.
- Make every rule falsifiable against a diff. If a reviewer can't point at code and say violated/not-violated, delete it.
- Don't hedge. No "usually", "generally", "consider", "where appropriate". If a rule has exceptions, list them explicitly.
- Encode only conventions the codebase actually follows today. Aspirational rules cause agents to rewrite compliant code and train readers to ignore the file.
- Name the exact library, function, module, or version. "Use our logger" is useless; "Use `@/lib/log.ts` `log.info()`" is a rule.
- Prefer positive framing ("Use named exports") by default; use negative rules ("Don't catch bare `Exception`") specifically to counter common base-model defaults.
- Include minimal inline code examples only when the rule's shape is non-obvious from prose. Keep them short; externalize larger examples.
- Don't restate what a formatter, linter, type-checker, or CI check already enforces. Rules should encode semantics beyond tooling's reach.
- Don't explain language or framework basics. The model knows what a hook is.

## Safety

- Never include secrets, API keys, tokens, credentials, or private URLs in rule files. Rule files are logged, shared, and a leak surface.
- Explicitly forbid destructive commands without human confirmation: `rm -rf`, `git push --force`, `DROP`, `TRUNCATE`, production deploys, data backfills, package publishes. Agents default to helpful, not cautious.
- Frame every rule as a guardrail, not a shortcut. Rules must add constraints; never encode instructions that weaken security, validation, or logging.
- Never paste untrusted external content (issue bodies, external docs, user input) into a rule file. Rule files are a trusted-instruction channel and a prompt-injection vector.
- Require human confirmation for schema migrations, destructive data operations, and irreversible actions. Name the exact commands that require it.

## Maintainability

- Assign an owner in frontmatter and review each file at least quarterly or within 6 months. Stale rules mislead agents with full confidence.
- Treat rule files as code: require review, versioning, and deliberate deletion. Ensures correctness and team consensus.
- Delete or rewrite any rule that merged code violates more than 2–3 times. Either the rule is wrong or unenforceable; either way it's noise.
- Don't duplicate rules across files. Extract to a shared file and reference it, or keep one canonical location.
- Remove or update rule files when the code they govern is restructured. Orphan rules erode trust in the whole system.

## Performance (Context Budget)

- Keep rules concise and deduplicated. Every byte costs tokens on every loaded turn.
- Link to canonical documentation rather than embedding long excerpts. Prevents doc drift and context bloat.
- Omit rules that are obvious from the surrounding code. Rule files are supplemental, not comprehensive.

## Conflict Resolution

- When two rule files could match the same path, state precedence explicitly in the more specific file. Silent conflicts produce nondeterministic behavior.
- Resolve conflicts with a deterministic rule: most-specific path wins; on tie, lexicographic filename order. Prefer additive includes over negated exclusion globs (negative globs are error-prone).
- When rules conflict or are impossible to satisfy, stop and ask the file's owner. Halting beats guessing on contradictory directives.

## Tooling & CI (recommended)

- Validate rule-file frontmatter in CI and fail when a `paths` glob matches zero files. Prevents orphan rules.
- Lint rule files for hedging words ("should", "maybe", "consider", "try") and enforce imperative mood. Keeps rules crisp.
- Check rule-file size and line-count caps in CI. Enforces the performance budget automatically.
- Verify referenced tools, libraries, or versions exist in the dev environment. Prevents unusable prescriptions.

## Assistant Interaction

- When editing in-scope code, restate the applicable rules being followed at the start of the response. Self-checking reduces drift and aids review.
- Don't override rules in prompts; update the rule file instead. Keeps the single source of truth in version control, not ephemeral chats.
- When uncertain about a tool, version, or convention, read the project's actual config files and defer to them. Project configs are the source of truth.
- Prefer no change over unsafe change when safety or correctness is unclear. Conservatism avoids incidents.
```