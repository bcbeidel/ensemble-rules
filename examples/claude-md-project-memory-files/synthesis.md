# Synthesis of CLAUDE.md Best Practices

## 1. Consensus Rules

### Structure & Placement

- **Place the file at the repository root.** (substantively similar across Gemini, Haiku, GPT-5) — AI assistants auto-load it from there; any other location requires explicit configuration.
- **Use Markdown headings with a predictable section order.** (substantively similar across all models) — Headings enable both humans and AI to navigate by skimming.
- **Use bulleted lists, not prose paragraphs.** (substantively similar across Opus, Haiku, Gemini, Grok, GPT-4o-mini) — Lists are scannable and more machine-parseable than prose.
- **Enforce a hard length cap (roughly 200 lines / under 2000 tokens).** (near-identical wording between Opus and Gemini at "under 200 lines"; Haiku says "under 2000 lines" — see Divergences) — Every token is paid for on every request; brevity forces prioritization.

### Content Priorities

- **Document only what is specific to *this* project; don't repeat generic best practices.** (substantively similar across Opus, Haiku, Gemini) — Generic advice is noise that displaces project-specific signal.
- **Link to source-of-truth files (configs, ADRs, package.json) rather than duplicating their content.** (substantively similar across GPT-5, Opus, Haiku, Gemini) — Duplication guarantees drift.
- **Include exact, canonical commands for setup, test, lint, and build.** (substantively similar across GPT-5, Opus, Haiku) — Agents will invent plausible-but-wrong commands when left to guess.
- **Use exact file paths and identifiers in backticks, not descriptions.** (substantively similar across Opus and Gemini) — Paths are unambiguous; descriptions drift.
- **Enumerate non-obvious invariants and architectural constraints.** (substantively similar across GPT-5, Opus, Haiku) — Models are literal; unstated constraints will be violated.

### Style & Tone

- **Write in imperative voice ("Do X" / "Don't Y"), not hedged or preference-based language.** (near-identical wording across Opus, Haiku, Gemini, Grok) — Models weight imperative language more reliably than "we prefer" or "consider."
- **Document ground truth, not aspiration.** (near-identical wording across Opus, Haiku, Gemini) — Aspirational rules produce code inconsistent with the actual codebase; if a rule isn't enforced, enforce it or delete it.
- **One rule per bullet; avoid compound rules.** (substantively similar across Opus and Haiku) — Compound rules get partially followed.

### Safety

- **Explicitly enumerate files and directories the AI must not modify.** (substantively similar across GPT-5, Opus, Haiku, Gemini) — Generated code, vendored deps, and migrations are common footguns.
- **Never commit secrets, internal hostnames, or customer data to the file.** (substantively similar across GPT-5 and Opus) — Memory files are routinely shared, indexed, and pasted into prompts.
- **State destructive-command and approval policies explicitly (migrations, deploys, new dependencies).** (substantively similar across GPT-5, Opus, Haiku) — Defaults are not safe; models need unambiguous guardrails.
- **Document security-critical conventions (input sanitization, auth, SQL usage).** (substantively similar across Haiku and Gemini) — Codifies secure-by-default code generation.

### Maintainability

- **Assign a single owner (e.g., CODEOWNERS entry) for the file.** (substantively similar across GPT-5 and Opus) — Shared ownership means no ownership.
- **Update the file in the same PR that changes the things it describes.** (substantively similar across GPT-5, Opus, Haiku, Gemini) — Staleness is the dominant failure mode; co-change prevents drift.
- **Include a last-updated date or version stamp.** (substantively similar across GPT-5, Haiku, Grok) — Visible currency builds trust and triggers reviews.
- **Delete rules that aren't actually enforced.** (substantively similar across Opus and Haiku) — Stale rules are worse than no rules.

## 2. Strong Minority Rules

- **Pair prohibitions with positive alternatives** (Opus only) — Kept because "Don't use X" without "Use Y instead" leaves the model to guess, which often reproduces the anti-pattern.
- **Start with a one-paragraph project summary / TL;DR** (GPT-5, Opus) — Kept because models need to know what the repo *is* before reading rules; fast orientation prevents early mistakes.
- **Don't rely on screenshots, images, or decorative emoji** (GPT-5, Opus, Grok) — Kept because these add tokens without behavioral signal and don't survive diffs/terminals.
- **Don't restate what the linter, formatter, or type-checker already enforces** (Opus, Haiku) — Kept because tooling is the source of truth for mechanical rules; duplication creates conflict.
- **Follow each rule with a one-line rationale** (Haiku explicit, implied by GPT-5/Opus) — Kept because brief rationales help humans and AI know when it's safe to break the rule.
- **Include short code examples showing ✓ preferred and ✗ anti-pattern forms** (Haiku) — Kept because concrete examples disambiguate style rules that prose cannot, *if kept short*.
- **Provide subdirectory CLAUDE.md files for domain-specific rules** (Opus, GPT-5) — Kept because it keeps the root lean and loads context only when relevant; marked contested (tool support varies).
- **Include a CI check that validates commands and links in the file** (GPT-5) — Kept because automation is the only scalable defense against staleness.
- **State an "Ask-before" checklist for high-risk changes** (GPT-5, Opus) — Kept because human-in-the-loop is the ultimate guardrail for irreversible operations.

## 3. Divergences

### Length Cap
- **~200 lines:** Opus, Gemini, Grok
- **~300 lines:** GPT-5
- **~2000 lines:** Haiku
- **No specific cap:** GPT-4o-mini

**Recommendation:** 200 lines as a soft target, 300 as a hard cap. The majority position (4 of 5 with explicit caps) clusters near 200. Haiku's 2000 is an outlier that conflicts with the shared rationale that every token costs attention on every request.

### Filename: CLAUDE.md vs AGENTS.md
- **AGENTS.md preferred for vendor neutrality:** GPT-5 (strongly)
- **Either acceptable, pick one:** Opus, Haiku, Gemini
- **CLAUDE.md as primary:** Grok, GPT-4o-mini (implicitly)

**Recommendation:** Use `AGENTS.md` as the canonical file with `CLAUDE.md` as a symlink or one-line pointer. This captures GPT-5's portability argument without breaking Claude's auto-load. Don't maintain two copies.

### Inclusion of Rationales vs Pure Imperatives
- **Rationales belong inline (brief):** Haiku (required), GPT-5, Gemini
- **Rationales are bloat:** Opus (implicit; favors pure imperatives with context-window concern)

**Recommendation:** Include one-line rationales for non-obvious rules only. They guide when-to-break decisions for humans and AI, but mechanical rules ("use camelCase") don't need them.

### Structured Metadata / Frontmatter
- **Useful for AI parsing:** GPT-5 (marks contested), Grok
- **Unnecessary coupling:** Opus, Haiku, Gemini (by omission)

**Recommendation:** Skip frontmatter unless you have tooling that consumes it. Majority view is that plain markdown is sufficient.

### Including Commands vs Linking to package.json
- **Include canonical commands inline:** GPT-5, Opus, Haiku
- **Only 1–3 most critical; link to package.json/Makefile:** Gemini, Grok

**Recommendation:** Include the small set of commands an agent will actually need (test, lint, build, run, format). These are high-value even if duplicative because agents fabricate them otherwise.

## 4. Notable Omissions

- **GPT-4o-mini omitted nearly every concrete rule** that other models converged on: no length cap, no imperative-voice rule, no "link don't duplicate," no explicit file-paths-in-backticks rule, no specific commands-to-include list, no "do-not-touch" section. Its output reads as generic documentation advice, not CLAUDE.md-specific guidance. Treat its signal as low.
- **Grok omitted the "document ground truth, not aspiration" rule** that Opus, Haiku, and Gemini all emphasized as critical. This is a significant omission because aspirational rules are a dominant failure mode.
- **Gemini omitted explicit rules about "do-not-edit" files and destructive-command policy.** GPT-5, Opus, and Haiku all treat these as first-order safety rules.
- **Haiku omitted the "write for AI, not as a README" framing** that Opus and Gemini both stress. Haiku's file is the most verbose and reads closer to README-style guidance — consistent with its much higher line-count tolerance.
- **Opus omitted explicit CI-validation of commands** that GPT-5 raised. Given Opus's emphasis on staleness as the dominant failure mode, this is a noteworthy gap.
- **GPT-5 and Opus both omitted the "define project terminology/glossary" rule** raised by Gemini and Haiku. Useful for domain-heavy codebases.

---

## 5. Final Rules File

```markdown
# CLAUDE.md / AGENTS.md Authoring Rules

**Scope:** Top-level project memory files (`CLAUDE.md` or `AGENTS.md`) that
AI coding assistants auto-load at the start of every session.

**Audience:** Engineers who write and review these files, and AI agents
generating or updating them.

---

## Structure

- **Place the file at the repository root.** AI assistants auto-load it from there.
- **Use `AGENTS.md` as the canonical file with `CLAUDE.md` as a symlink or one-line pointer.** Vendor-neutral naming preserves portability without breaking Claude's auto-load. Don't maintain two copies. *(contested)*
- **Keep the file under 200 lines; hard cap at 300.** Every token is paid on every request and displaces attention from the user's task.
- **Open with a one-paragraph project summary.** The model needs to know what the repo *is* before it reads rules.
- **Use a fixed section order:** Overview → Commands → Architecture → Conventions → Safety / Do-Not-Touch → Gotchas. Critical safety rules must precede stylistic ones.
- **Use H2 headings for top-level sections; avoid nesting beyond H3.** Deep nesting hurts skimmability for both humans and models.
- **Use bulleted lists, not prose paragraphs.** Lists are scannable and parseable.
- **One rule per bullet; no compound rules joined by "and."** Compound rules get partially followed.

## Content

- **Document only what is specific to *this* project.** Generic best practices ("write tests," "avoid null") are noise.
- **Document only what a competent engineer would get wrong by default.** Obvious things waste context; non-obvious things prevent bugs.
- **Link to source-of-truth files (configs, ADRs, `package.json`) instead of duplicating their content.** Duplication guarantees drift.
- **Don't restate what the linter, formatter, or type-checker already enforces.** Tooling is the source of truth for mechanical rules.
- **Include exact, copy-pasteable commands for setup, test, lint, build, and run.** Agents fabricate plausible-but-wrong commands when left to guess.
- **Name the package manager, language version, and OS assumptions explicitly.** `npm` vs `pnpm` vs `yarn` produces silently broken installs.
- **Reference files and identifiers by repo-relative path in backticks (`src/api/router.ts`).** Paths are unambiguous; descriptions drift.
- **Enumerate non-obvious architectural invariants** (e.g., "all API routes must call `requireAuth()`"). These are the rules the type system can't enforce.
- **List anti-patterns the team has explicitly rejected.** Prevents assistants from re-introducing solutions that were tried and failed.
- **Define project-specific terminology on first use.** Gives the AI a glossary for domain language.
- **Consider subdirectory `CLAUDE.md` files for domain-specific rules in large repos.** Keeps the root lean; tool support varies. *(contested)*

## Style & Tone

- **Write in imperative voice ("Do X." / "Never Y.").** Models weight imperatives more reliably than "we prefer" or "consider."
- **Document ground truth, not aspiration.** If a rule isn't enforced, either enforce it or delete it. Aspirational rules produce code inconsistent with the codebase.
- **Use present tense and active voice.** "The API returns JSON" beats "JSON will be returned by the API."
- **Follow non-obvious rules with a one-line rationale.** Helps humans and agents decide when it's safe to break a rule. Skip rationales for mechanical rules.
- **Pair prohibitions with positive alternatives.** "Don't use `var`; use `const` by default, `let` for loop counters." Bare prohibitions leave the model to guess.
- **Omit marketing language, mission statements, team values, and decorative emoji.** Zero behavioral impact; pure context-window tax.
- **Include short ✓ / ✗ code examples only for rules prose cannot make concrete.** Keep examples under 10 lines.

## Safety

- **Enumerate files and directories that must never be edited without approval.** Generated code, vendored deps, migrations, and CI config are common footguns.
- **State destructive-command policy explicitly** (migrations, `rm -rf`, force-push, prod deploys, dependency additions). Defaults are not safe.
- **Provide an "ask before" checklist for high-risk changes** (schema changes, public API changes, cross-boundary refactors, new dependencies). Human-in-the-loop is the ultimate guardrail.
- **Never commit secrets, tokens, internal hostnames, or customer data to this file.** It is routinely shared, indexed, and pasted into prompts.
- **State security-critical conventions** (e.g., "use `db.query()` prepared statements," "sanitize input via `src/utils/sanitize.ts`"). Codifies secure-by-default generation.
- **Specify data-handling and PII rules** with links to the full policy. Clear data rules reduce compliance risk.

## Maintainability

- **Assign a single owner via CODEOWNERS.** Shared ownership means no ownership.
- **Update this file in the same PR that changes what it describes.** Co-change policy is the primary defense against staleness.
- **Delete rules that aren't actually enforced.** A stale "we use Jest" rule three months after migrating to Vitest is worse than no file at all.
- **Add a CI check that runs the canonical commands and validates links.** Automation is the only scalable defense against drift.
- **Include a "Last Updated" date at the top.** Visible currency triggers reviews and builds trust.
- **Audit the file quarterly and on major version bumps.** Scheduled review catches drift that PR review misses.

## Anti-Patterns

- **Don't paste the README into this file.** READMEs target new humans; this file targets agents mid-task. Different jobs.
- **Don't duplicate full guides, API references, or ADRs.** Link to them.
- **Don't document the obvious** ("this is a TypeScript project"). The model can see `tsconfig.json`.
- **Don't use vague verbs** like "run the app" or "write clean code." Specify exact commands and concrete rules.
- **Don't bury "Do not edit" warnings.** Prominent guards are respected.
- **Don't rely on screenshots or images for critical steps.** Text survives terminals and diffs.
```