# Synthesis of Agent Rule Files Guidance

## 1. Consensus Rules

### Structure & Scoping

- **Include a `paths:` glob in YAML frontmatter at the top of every rule file.** — Conditional loading is the core mechanism; missing or misconfigured paths defeats the purpose. (substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Scope `paths:` globs as narrowly as the rule's actual domain.** — Overbroad globs pollute unrelated edits and erode trust. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)
- **Group rules under thematic headings (e.g., Structure, Safety, Style).** — Flat, predictable organization aids scanning by humans and parsers. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Keep one concern per file and split unrelated topics.** — Focused files are easier to scope, review, and update. (substantively similar across GPT-5, Claude Opus, Gemini)

### Content & Style

- **Write each rule as a single imperative sentence followed by a one-line rationale.** — Uniform, scannable format reduces ambiguity for both humans and AI. (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini; Grok echoes)
- **State rules as commands or prohibitions; avoid hedging words like "should," "try," "consider," "maybe."** — LLMs mirror hedging and treat softened language as optional. (near-identical wording across GPT-5, Claude Opus, Claude Haiku — suggests shared training signal)
- **Use bullet lists rather than long prose.** — Lists are more parseable and scannable than paragraphs. (substantively similar across Claude Haiku, Gemini, Grok)
- **Fence code blocks with a language tag.** — Language hints enable syntax-aware tooling and safer rendering. (substantively similar across GPT-5, Claude Opus)
- **Keep code examples minimal or omit them entirely.** — Examples are token-expensive and go stale; use only when prose is insufficient. (substantively similar across GPT-5, Claude Opus, Gemini, Grok)

### Safety

- **Never commit real secrets, tokens, credentials, or private hostnames; use obvious placeholders.** — Rule files are version-controlled and widely readable. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)
- **State rules governing destructive or security-sensitive operations with no hedging.** — Soft language on dangerous operations is the worst place for ambiguity. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)

### Performance

- **Keep rule files small (roughly under 2KB–16KB or under ~200–300 lines).** — Every token competes with code and prompt for context budget. (substantively similar but with varying thresholds across GPT-5, Claude Opus, Gemini, Grok)
- **Do not duplicate rules across files; extract shared rules to a single scoped file.** — Duplication guarantees drift. (substantively similar across GPT-5, Claude Opus, Grok)

### Maintenance

- **Declare an owner and a last-reviewed date (or equivalent lifecycle metadata).** — Clear accountability prevents stale-rule rot. (substantively similar across GPT-5, Claude Haiku)
- **Delete or archive rules when the underlying convention changes; do not layer contradictions.** — Stale rules poison every future edit under their scope. (substantively similar across GPT-5, Claude Opus, Claude Haiku)

## 2. Strong Minority Rules

- **Place the most load-bearing rules first within each section.** (Claude Opus) — Context windows truncate from the end under pressure; ordering becomes a real lever at scale. Kept because it reflects a real mechanism of LLM context handling.
- **Reference project-specific names, modules, and APIs by exact identifier rather than generic advice.** (Claude Opus) — The base model already knows generic style; specificity is what the tokens are buying. This is the most under-represented insight across the inputs and arguably the highest-value one.
- **Reference external sources of truth (linters, formatters, configs) instead of restating their rules.** (Gemini, Claude Haiku) — Rule files drift; configs are canonical. Avoids the rules-file-as-linter-config anti-pattern.
- **Never let two rule files with overlapping `paths:` state contradictory rules.** (Claude Opus) — Resolution order is implementation-defined across agents; invisible bugs until they matter. Essential at scale.
- **Name exceptions inline when a rule has common ones.** (Claude Haiku) — Prevents rule-lawyering and over-application without requiring an ADR lookup.
- **Set a priority (integer) and define tie-break rules.** (GPT-5) — Only GPT-5 raised this, but it's the one deterministic mechanism for handling conflicts between overlapping files.
- **Do not instruct the agent to run destructive shell commands like `rm -rf` or `dd`.** (Gemini, GPT-5) — Rules guide generation; they should not push execution of dangerous operations.
- **Use concrete, falsifiable criteria (specific thresholds, named patterns) instead of subjective qualifiers like "clean," "elegant," or "reasonable."** (Claude Opus, Claude Haiku) — Unfalsifiable rules are noise.

## 3. Divergences

### File size / length thresholds
- **GPT-5:** under 16KB and 300 lines.
- **Claude Opus:** under 200 lines, under 2,000 tokens.
- **Gemini:** under 2KB.
- **Grok:** under 10KB, under 500 lines.
- **Claude Haiku:** ~40 rules or fewer (one printed page).

**Recommendation:** Adopt Claude Opus's token-based threshold (~2,000 tokens) as the primary metric because tokens are what actually compete for context, with a line-count fallback (~200 lines) for quick checks. Byte limits are a weaker proxy. The exact number matters less than having *some* enforced ceiling.

### Use of RFC 2119 keywords (MUST / SHOULD / MAY)
- **Claude Opus:** Explicitly recommends against them — "plain imperatives are equally binding to an LLM."
- **Other models:** Do not raise this; implicitly accept plain imperatives.

**Recommendation:** Follow Claude Opus. Plain imperatives are shorter and no less binding to an LLM. RFC 2119 language is a human-spec convention with no added value here.

### Rationale format (inline dash vs. brackets vs. sub-bullet)
- **GPT-5:** `— rationale` on the same line after an em-dash.
- **Claude Haiku:** `[rationale]` in square brackets.
- **Gemini / Claude Opus:** One-line rationale immediately following; format flexible.

**Recommendation:** Pick one convention per project and enforce it with a linter. The em-dash form is most common across inputs and reads cleanly in rendered markdown.

### Strictness of imperative phrasing
- **GPT-5 / Claude Opus / Claude Haiku:** Ban "should," "try," "maybe," "consider."
- **Claude Haiku own reasoning:** Notes rules phrased as absolutes can cause over-rigid AI behavior.

**Recommendation:** Default to unhedged imperatives, but allow named exceptions inline ("except when…") as the pressure valve. This reconciles the two positions: strong phrasing + explicit exception clauses beats softened phrasing.

### Granularity (many small files vs. fewer larger ones)
- **Claude Opus, Gemini:** Many small, concept-scoped files.
- **Grok:** Notes this is genuinely contested; some prefer consolidation.

**Recommendation:** Many small files, scoped by subsystem or concern. This aligns with path-based conditional loading and reduces merge conflicts. A monolithic file defeats the core mechanism.

## 4. Notable Omissions

- **GPT-4o-mini omitted nearly everything specific to Agent Rule Files.** Its output reads as generic "good code" advice (naming conventions, error handling in code, avoid globals) rather than rules for authoring rule files. This is the signal: the model did not understand the meta-level of the task. Its output should be heavily discounted.
- **Gemini omitted explicit ownership/lifecycle metadata** (owner, last-reviewed date) that GPT-5, Claude Opus, and Claude Haiku all called out. Significant because stale rules are a named top failure mode elsewhere.
- **Grok omitted the imperative/no-hedging rule** that three other models converged on. Surprising given how central it is to making rules actionable for LLMs.
- **Grok and Gemini omitted conflict-resolution mechanics** (priority, tie-breaking, detecting overlapping paths) that GPT-5 and Claude Opus raised. At scale, this becomes a real bug source.
- **Claude Haiku omitted explicit file-size or token-budget thresholds,** though it mentioned "one page." The other four all set numeric limits. Performance guidance without a number is advisory only.
- **GPT-5 omitted the "reference external sources of truth" rule** (defer to linter configs rather than duplicate them) that Gemini and Claude Haiku raised. Meaningful because it's the cleanest way to prevent drift.

## 5. Shared Deterministic Checks

### Shared (multi-model) checks

- **Check** — File begins with valid YAML frontmatter delimited by `---` markers and contains a non-empty `paths` key (array of strings).
  - **Signal** — Raw source file; parsed YAML frontmatter.
  - **Tool candidate** — Ad-hoc (YAML parser + key presence assertion; no off-the-shelf tool specifically for this).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — GPT-5 requires a larger set of keys (title, owner, version, updated, priority, status); Claude Opus requires `paths` + `description`; others require only `paths`. Substance agrees on `paths`; the broader metadata set is project-specific.

- **Check** — File size or line count is below a configured ceiling.
  - **Signal** — File byte size, line count, or token count via tokenizer.
  - **Tool candidate** — `wc -l`, `stat`, or `tiktoken` for token count; ad-hoc threshold.
  - **Raised by** — GPT-5, Claude Opus, Gemini, Grok.
  - **Variance** — Thresholds vary widely (2KB / 10KB / 16KB; 200 / 300 / 500 lines; 2,000 tokens). The check is identical in shape; only the constant differs. Token count is the most semantically meaningful signal.

- **Check** — No real secrets, API keys, tokens, or credentials appear anywhere in the file.
  - **Signal** — Raw source text.
  - **Tool candidate** — `gitleaks`, `trufflehog`, or `detect-secrets` with default rulesets.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Substance agrees. GPT-5 additionally suggests project-specific regexes for internal token shapes; others rely on stock scanners.

- **Check** — All fenced code blocks carry a language tag.
  - **Signal** — Markdown AST; fenced code block nodes.
  - **Tool candidate** — `markdownlint` rule `MD040`.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — None of substance. GPT-5 allows `text` as a fallback for pseudo-code.

- **Check** — No rule bullet uses hedging words ("should," "try," "consider," "maybe," "may") in the imperative clause.
  - **Signal** — Markdown AST list items; text before the rationale delimiter; excluding inline code spans.
  - **Tool candidate** — Ad-hoc (regex over list-item text, excluding fenced/inline code).
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — GPT-5 is stricter (blocklists "should | try | maybe | consider"); Claude Haiku flags modal auxiliaries and passive voice more broadly but acknowledges higher false-positive rate.

- **Check** — Every rule bullet is followed by a rationale of adequate length in the project's chosen format (em-dash, brackets, or sub-bullet).
  - **Signal** — Markdown AST list-item structure.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Format convention differs (em-dash vs. brackets vs. child bullet); each model picks one. Substance agrees: rationale must be present, non-empty, and one line.

- **Check** — `paths:` globs do not use unrestricted catch-alls like `**/*` or `*` unless the file is explicitly marked universal.
  - **Signal** — Parsed frontmatter; optionally expanded against the repo file tree.
  - **Tool candidate** — Ad-hoc (glob string inspection + optional minimatch expansion).
  - **Raised by** — GPT-5, Claude Opus, Grok.
  - **Variance** — GPT-5 checks against a list of disallowed literal patterns; Claude Opus additionally expands globs and flags matches covering >50% of tracked files; Grok simply forbids wildcards. The glob-expansion check (Opus) is the strongest.

- **Check** — Destructive shell commands (`rm -rf`, `dd`, `mkfs`, `drop database`) do not appear unguarded in fenced code blocks.
  - **Signal** — Fenced code blocks tagged as shell.
  - **Tool candidate** — Ad-hoc (regex over shell code-block content against a blocklist).
  - **Raised by** — GPT-5, Gemini.
  - **Variance** — GPT-5 requires either an `echo ` prefix or a `# DANGEROUS:` warning comment; Gemini straight-up forbids them. Blocklists agree in substance.

### Singleton checks

- **Check** — `paths:` globs expand to at least one file that actually exists in the repo at authoring time.
  - **Signal** — Parsed frontmatter + repo file listing.
  - **Tool candidate** — Ad-hoc (minimatch / pathlib glob expansion).
  - **Raised by** — GPT-5.

- **Check** — Pairs of rule files whose `paths:` globs overlap are surfaced for human review of contradictions.
  - **Signal** — All rule-file frontmatter + glob expansion.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Bullets containing deprecation or migration keywords ("deprecated," "legacy," "temporary," "until") are accompanied by a date (ISO format) or issue reference.
  - **Signal** — Raw source text.
  - **Tool candidate** — Ad-hoc (keyword + regex proximity).
  - **Raised by** — Claude Opus.

- **Check** — Rule bullets near near-duplicate text across multiple files (flagged via Levenshtein or embedding similarity above a threshold).
  - **Signal** — All rule-file bullet text.
  - **Tool candidate** — Ad-hoc (`rapidfuzz`, embedding cosine similarity).
  - **Raised by** — Claude Opus.

- **Check** — Filenames under the rules directory match kebab-case `^[a-z0-9]+(-[a-z0-9]+)*\.md$`.
  - **Signal** — File path.
  - **Tool candidate** — Ad-hoc (regex).
  - **Raised by** — GPT-5.

- **Check** — Indentation uses spaces only; no tab characters in indentation.
  - **Signal** — Raw source file.
  - **Tool candidate** — `markdownlint` rule `MD010`.
  - **Raised by** — Grok.

- **Check** — No line exceeds 80 (or 100) characters.
  - **Signal** — Raw source file; line lengths.
  - **Tool candidate** — `markdownlint` rule `MD013`.
  - **Raised by** — GPT-5 (100), Grok (80).

- **Check** — Rule bullets touching security-sensitive keywords (`auth`, `crypto`, `PII`, `secret`, `password`, `token`, `GDPR`) contain no hedging words and include a consequence-stating rationale.
  - **Signal** — Raw source text; keyword scan + hedge-word scan on the same bullet.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Haiku.

- **Check** — Prose preamble before the first `##` heading does not exceed two non-blank lines.
  - **Signal** — Markdown AST; nodes between frontmatter and first heading.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Relative markdown links to other files resolve to files that exist on disk.
  - **Signal** — Parsed markdown links + filesystem lookup.
  - **Tool candidate** — `markdown-link-check` or `lychee`.
  - **Raised by** — Claude Haiku.

- **Check** — Heading depth does not exceed `###` (level 3).
  - **Signal** — Markdown AST heading nodes.
  - **Tool candidate** — `markdownlint` rule `MD001`/`MD025` variants; ad-hoc depth check.
  - **Raised by** — Claude Opus.

---

## 6. Final Rules File

```markdown
---
title: Agent Rule Files — Authoring Conventions
paths: [".claude/rules/*.md", ".cursor/rules/*.mdc", ".github/.ai/rules/*.md"]
description: Conventions for authoring path-scoped markdown rule files loaded by AI coding assistants.
owner: <team-slug-or-email>
updated: 2025-01-15
status: active
---

# Agent Rule Files — Authoring Conventions

**Scope.** This document governs path-scoped markdown rule files loaded conditionally
by AI coding assistants based on the files being edited.

**Audience.** Engineers authoring and reviewing rule files.

**Principle.** Rule files are a finite, token-budgeted instruction channel to a
non-human reader. They are valuable only when scoped, specific, and unhedged.

## Structure & Scoping

- Begin every rule file with YAML frontmatter containing at minimum `paths:` and `description:`. — Without `paths:` a file either never loads or always loads; both are bugs.
- Scope `paths:` globs as narrowly as the rule's actual domain. — Overbroad globs pollute unrelated edits and erode trust in the whole system.
- Never use unrestricted catch-alls like `**/*` or `*` except in a file explicitly marked as universal. — Catch-alls defeat the conditional-loading mechanism entirely.
- Put one focused concern per file; split unrelated topics. — Narrow scope limits conflict, reduces merge friction, and enables precise path matching.
- Group rules under `##` thematic headings and stay within three heading levels. — Flat, predictable layout aids scanning by humans and parsers.
- Never let two rule files whose `paths:` globs overlap state contradictory rules. — Resolution order is implementation-defined; invisible bugs until they matter.
- Set a `priority` integer in frontmatter when overlap is unavoidable, and break further ties by longest fixed glob prefix. — Deterministic resolution beats hidden behavior.

## Content & Style

- Write each rule as a single imperative sentence followed by ` — ` and a one-line rationale. — Uniform bullets are scannable and lintable.
- State rules as commands or prohibitions; do not use "should," "try," "consider," "maybe," or "may" in the imperative clause. — LLMs mirror hedging and treat softened language as optional.
- Name common exceptions inline within the rule ("…except when X"). — Prevents over-application and rule-lawyering without forcing an ADR lookup.
- Reference project-specific names, modules, and APIs by exact identifier. — Generic advice is already in the base model; specificity is what the tokens are buying.
- Omit rules that describe universal programming hygiene. — "Handle errors" is noise; "wrap `db.Exec` in `withRetry`" earns its tokens.
- Use bullet lists rather than prose paragraphs. — Lists parse cleanly and read in any order.
- Keep rationales falsifiable; avoid words like "clean," "elegant," "reasonable," "appropriate." — Unfalsifiable rules cannot be reviewed or enforced.
- Include a code example only when the rule is non-obvious from prose, and keep it under 10 lines. — Examples cost tokens and go stale; use them surgically.
- Fence all code blocks with a language tag. — Language tags enable syntax-aware tooling and safer rendering.
- Reference external sources of truth (linter configs, formatters, CI checks) rather than restating them. — Configs are canonical; rule-file duplicates drift.

## Safety

- Never commit real secrets, tokens, credentials, or private hostnames; use obvious placeholders like `<TOKEN>`. — Rule files are version-controlled and widely readable.
- State rules governing destructive or security-sensitive operations with no hedging, and include a brief note on the consequence. — Soft language on dangerous operations is the worst place for ambiguity.
- Do not include raw destructive shell commands (`rm -rf`, `dd`, `mkfs`, `drop database`) in examples unless prefixed with `echo ` or preceded by a `# DANGEROUS: example only` comment. — Prevents unsafe copy-paste from examples.
- Guide code generation rather than instruct command execution. — Rule files should not be a vector for running destructive operations.

## Performance

- Target under ~2,000 tokens (roughly 200 lines) per rule file. — Every token competes with the user's prompt, the code, and the response.
- Do not duplicate rules across files; extract shared rules to a single file with appropriate `paths:`. — Duplication guarantees drift.
- Place the most load-bearing rules first within each section. — Context windows truncate from the end under pressure.

## Maintenance

- Declare an `owner` and `updated` date in frontmatter. — Clear accountability prevents stale-rule rot.
- Mark lifecycle with `status: draft | active | deprecated`; move deprecated files to an archive subpath rather than deleting. — Discoverability during migrations beats silent removal.
- Delete rules when the underlying convention changes; do not add a contradicting rule on top. — Layered contradictions poison every future edit under the scope.
- Date or link a tracking issue on any rule marked deprecated, legacy, temporary, or tied to a migration. — Time-boxed rules must announce their own expiry.
- Review rule files when the code matching their `paths:` undergoes major refactor. — Rules survive refactors they shouldn't; audits catch this.

## Error Handling & Conflicts

- Define a fallback when rules conflict or context is missing (e.g., "ask the user" or "defer to higher-priority file"). — Explicit fallbacks prevent agent dead-ends and non-deterministic behavior.
```