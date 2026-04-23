# Synthesis: CLAUDE.md Project Memory File Best Practices

## 1. Consensus Rules

### Structure & Placement

- **Place a single project memory file at the repository root.** (substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini) — Assistants look for it there; nested files are for subprojects.
- **Use hierarchical Markdown headings (H1 title, H2 sections) to organize content.** (substantively similar across all five models) — Predictable structure enables both human scanning and AI parsing.
- **Enforce a size/length limit to stay within AI context budgets.** (substantively similar but differently worded; thresholds vary — see Divergences) — Every token loads each session; bloat displaces useful context.

### Content Essentials

- **List exact build, test, lint, and run commands in copy-pastable code blocks.** (substantively similar across GPT-5, Claude Opus, Claude Haiku) — These are the highest-frequency assistant lookups.
- **Document project layout: where source, tests, and config live.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — A map prevents blind grepping.
- **State primary language(s), runtime version(s), and key frameworks explicitly.** (substantively similar across GPT-5, Claude Haiku, Gemini) — Prevents environment mismatches.
- **Link to canonical sources (ADRs, CONTRIBUTING.md, linter configs) rather than duplicating content.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Duplication guarantees drift.
- **Document prohibitions and destructive-command guardrails explicitly as imperative negatives.** (substantively similar across GPT-5, Claude Opus, Claude Haiku) — Prohibitions are the highest-ROI content.

### Style

- **Write in concise imperative bullets, not prose paragraphs.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok) — Scannability improves reliability for humans and LLMs.
- **Use consistent Markdown syntax (ATX headings, standard bullet markers, fenced code blocks with language tags).** (substantively similar across GPT-5, GPT-4o-mini, Claude Opus, Grok) — Uniformity improves parsing.
- **Use repository-relative paths for intra-repo references.** (substantively similar across GPT-5, Gemini) — Relative links work in forks, IDEs, and clones.

### Safety

- **Do not include secrets, tokens, credentials, PII, or private/production endpoints.** (substantively similar across GPT-5, Claude Haiku, Gemini, GPT-4o-mini) — The file is committed to source control and loaded into AI context.
- **Document security-relevant conventions and safe patterns explicitly.** (substantively similar across GPT-5, GPT-4o-mini, Claude Haiku, Gemini, Grok) — Guides the AI toward approved patterns for auth, PII, and sensitive data.

### Maintenance

- **Assign an owner or responsible team for the file.** (substantively similar across GPT-5, Claude Haiku, Gemini) — Without ownership, the file rots.
- **Delete aspirational, outdated, or unverifiable content aggressively; document current reality only.** (substantively similar across Claude Opus, Claude Haiku, Gemini) — Stale guidance is worse than missing guidance because it actively misleads.
- **Track freshness with a last-updated date or include the file in PR review for relevant changes.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok) — Drift is the default mode; review is the fix.

## 2. Strong Minority Rules

- **Symlink `AGENTS.md` to `CLAUDE.md` (or maintain byte-identical copies) for tool-agnosticism.** (Claude Opus, Gemini) — The ecosystem is converging on `AGENTS.md` as a vendor-neutral name; dual-file setups fail predictably. Worth including because it solves a real portability problem.
- **Include commands for running a single test, not just the full suite.** (Claude Opus) — Targeted reruns are the dominant iteration loop; a specific, high-value content rule.
- **State where generated/vendored code lives and mark it as non-hand-editable.** (Claude Opus, Claude Haiku) — Prevents the single most common class of destructive edits.
- **Mark unknowns explicitly with "Unknown as of YYYY-MM-DD" rather than omitting or guessing.** (GPT-5) — Explicit unknowns avert AI guesswork and invite updates.
- **Define project-specific terminology and acronyms in a glossary.** (Gemini, Claude Haiku) — AIs lack the team's cultural context and will otherwise invent meanings.
- **Call out non-obvious architectural boundaries (e.g., "packages/core must not import from packages/web").** (Claude Opus) — Import rules are invisible to a reader of the directory tree.
- **Include a bold warning not to paste secrets or production data into prompts.** (GPT-5) — Habitual guardrails at the point of use prevent leaks.

## 3. Divergences

### File size / length limit

- **Positions:** GPT-5 says ≤50 KB and ≤1,200 lines; Claude Opus says ≤200 lines; Claude Haiku says ≤60 lines per section (~1 screen); Grok says ≤500 lines; Gemini says ≤32 KB. GPT-4o-mini has no limit.
- **Synthesis:** The direction of agreement is clear (shorter is better), but numbers span an order of magnitude. The variance reflects different assumed use cases — a small app vs. a complex monorepo. **Recommendation:** set a soft warning at ~200 lines and a hard limit around 32 KB / 1,000 lines, with per-section caps (~60 lines) as a second line of defense. Treat the number as a configurable threshold, not a universal law.

### Prescribed section ordering

- **Positions:** GPT-5 mandates 16 sections in exact order; Claude Opus mandates 5 fixed headings (Overview, Commands, Architecture, Conventions, Do Not) with order not enforced; Claude Haiku suggests themes without strict order; Gemini, Grok, GPT-4o-mini give no mandatory list.
- **Synthesis:** GPT-5's 16-section schema is too heavy for the median repo and tips into the "encyclopedia" failure mode all models warned about. Claude Opus's minimal fixed set hits the right target. **Recommendation:** require a small set of named sections (Commands, Architecture, Do Not, plus an Overview/summary), allow additions, and do not enforce order.

### File naming (`CLAUDE.md` vs. `AGENTS.md`)

- **Positions:** Gemini recommends `AGENTS.md` as the vendor-neutral standard and would rename `CLAUDE.md`. GPT-5 accepts either but bans having both. Claude Opus suggests symlinking the two. Others don't address it.
- **Synthesis:** The community is genuinely in transition. **Recommendation:** accept either, prohibit unsynchronized duplicates, and prefer `AGENTS.md` for new projects while supporting `CLAUDE.md` for ecosystem compatibility.

### Images, diagrams, and raw HTML

- **Positions:** GPT-5 bans them outright (parser fragility, token cost). Others don't prohibit them.
- **Synthesis:** The ban is reasonable but aggressive. **Recommendation:** discourage inline images and raw HTML; allow links to diagrams stored elsewhere. Mark as an opinionated, contested rule.

### Code examples

- **Positions:** Claude Opus bans code blocks >15 lines; Claude Haiku caps at 3 lines; Grok at 5 lines; Gemini prefers descriptions over snippets; GPT-5 caps at 120 lines per block.
- **Synthesis:** All agree long examples don't belong; thresholds differ. **Recommendation:** keep illustrative snippets short (≤15 lines) and link to a live file for anything larger.

### Table of Contents

- **Positions:** GPT-4o-mini and Claude Haiku require one; Claude Opus explicitly bans one ("at this length it's noise").
- **Synthesis:** At the file sizes the majority endorses (under ~200 lines), a TOC is overhead. **Recommendation:** no TOC; rely on stable H2 headings for navigation.

## 4. Notable Omissions

- **GPT-4o-mini omits nearly all consensus rules** — no file placement, no commands section, no size limit, no architectural content, no ownership, no freshness tracking, no secrets ban. Its output is a generic documentation-quality template that misses what makes project memory files distinct from ordinary docs. The absence is the signal: treat this model's output as low-weight in the synthesis.
- **Grok omits the secrets/safety ban**, the most universally agreed safety rule across the other four models. Also omits ownership, file placement, and architectural content guidance.
- **Grok omits the "link, don't duplicate" principle** that four of five other models surface as central to maintainability.
- **Gemini omits explicit guidance on listing commands and prohibitions**, which Claude Opus and Claude Haiku identify as the highest-ROI content. Gemini's file is strong on meta-principles, weaker on concrete content prescriptions.
- **GPT-5 omits the "delete aspirational content" rule** that Claude Opus, Claude Haiku, and Gemini each call out as a primary failure mode — interesting given GPT-5's otherwise thorough coverage.
- **No model except Claude Opus mentions single-test commands**, though this is arguably the most-used assistant operation during iteration.

## 5. Shared Deterministic Checks

### Multi-model checks

- **Check** — Verifies the project memory file exists at the repository root under a recognized name (`CLAUDE.md` or `AGENTS.md`).
  - **Signal** — Filesystem listing of the repo root.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — GPT-5 requires exactly one of the two names (fails if both exist); Claude Opus accepts either or both if symlinked/identical; Gemini prefers `AGENTS.md` and flags `CLAUDE.md` without an accompanying `AGENTS.md`. Substantively they agree on "exactly one source of truth at the root."

- **Check** — Verifies the file is under a maximum size or line count.
  - **Signal** — File size in bytes and/or line count.
  - **Tool candidate** — `wc -l`, `stat`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — Thresholds span 200 lines (Opus) to 1,200 lines / 50 KB (GPT-5). Haiku applies a per-section cap instead of a whole-file cap. All agree a limit should exist; set the number per project.

- **Check** — Verifies H2 headings exist and include required sections.
  - **Signal** — Parsed Markdown AST (or regex over `^## `).
  - **Tool candidate** — `remark`, `markdown-it`, or regex; `markdownlint`.
  - **Raised by** — GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Grok.
  - **Variance** — GPT-5 requires 16 sections in exact order; Opus requires a minimum set including `Commands` and `Do Not`; Haiku requires at least some H2s; Grok requires at least three specific names; GPT-4o-mini requires two H2s minimum. Substance converges on "enforce a minimum set of H2 headings"; strictness varies.

- **Check** — Verifies consistent Markdown formatting (heading style, bullets, fenced code blocks).
  - **Signal** — Raw source text parsed as Markdown.
  - **Tool candidate** — `markdownlint` (rules MD003, MD004, MD040, MD048).
  - **Raised by** — GPT-5, GPT-4o-mini, Claude Opus, Grok.
  - **Variance** — GPT-5 restricts code fence language tags to an allow-list (bash/sh/pwsh/json/yaml/ini); others just require consistency. Grok names `markdownlint` explicitly.

- **Check** — Verifies the file contains no secrets, credentials, or tokens.
  - **Signal** — Raw source text run through a secret scanner.
  - **Tool candidate** — `gitleaks`, `trufflehog`.
  - **Raised by** — GPT-5, Gemini.
  - **Variance** — GPT-5 additionally flags production URL patterns and internal TLDs; Gemini relies on the scanner's entropy/pattern rules alone. Both agree the scanner output is the primary signal.

- **Check** — Verifies a last-updated date or freshness marker is present near the top.
  - **Signal** — Raw source text (regex over first N lines or frontmatter parse).
  - **Tool candidate** — ad-hoc regex; optionally cross-check against `git log` on the file.
  - **Raised by** — GPT-5, Claude Haiku, Grok.
  - **Variance** — GPT-5 requires strict ISO 8601 and exact casing; Haiku accepts HTML comments and per-section timestamps; Grok accepts version strings or dates. Collapse to: require at least one ISO-8601 date or explicit "Last updated:" line within the first ~30 lines.

- **Check** — Verifies a Commands section contains at least one fenced code block with build/test/lint invocations.
  - **Signal** — Parsed Markdown; section under `## Commands` (or synonym).
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Opus requires coverage of specific command categories (build, test, lint, typecheck, run) and cross-checks the declared package manager against lockfiles on disk; GPT-5 only requires at least one code block per section.

- **Check** — Verifies internal references use relative paths, not absolute paths or full URLs to the same repo.
  - **Signal** — Markdown links extracted from source.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Gemini.
  - **Variance** — GPT-5 focuses on flagging `github.com/<this-repo>/blob/...` URLs; Gemini focuses on root-absolute paths (`/src/...`). Both miss cases the other catches; combine them.

- **Check** — Verifies a "Do Not" / prohibitions section exists and contains at least one imperative negative bullet.
  - **Signal** — Parsed Markdown; text of the designated section.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.
  - **Variance** — Opus requires a section named `Do Not` or synonym; Haiku searches keywords across the file without requiring a dedicated section.

### Singleton checks worth keeping

- **Check** — Verifies no fenced code block exceeds a line threshold (e.g., 15 lines).
  - **Signal** — Parsed Markdown; length of each fenced block.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verifies every top-level repo directory (excluding standard ignores) is mentioned in the Architecture section.
  - **Signal** — Directory listing cross-referenced with section text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verifies that when a lockfile is present on disk, the corresponding package manager is named explicitly in the Commands section (and generic phrasing like "your package manager" is flagged).
  - **Signal** — Filesystem (lockfile presence) + section text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verifies a CODEOWNERS entry exists for the project memory file.
  - **Signal** — `.github/CODEOWNERS` or `CODEOWNERS` at repo root.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Warns when a PR modifies `package.json` scripts, `Makefile`, dependency manifests, or top-level directory structure without touching the memory file.
  - **Signal** — Git diff of the PR.
  - **Tool candidate** — ad-hoc CI check.
  - **Raised by** — Claude Opus.

- **Check** — Verifies generated code paths (detected via `.gitattributes linguist-generated` or `generated/` directories) are mentioned in the file alongside a "do not edit" phrase.
  - **Signal** — `.gitattributes` + filesystem + section text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verifies a Changelog section contains bullets prefixed with ISO dates in non-increasing order.
  - **Signal** — Parsed Changelog section.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5.

- **Check** — Flags hedging language ("should", "try to", "might", "consider") in directive sections; expects >80% of bullets to use imperative or prohibitive forms.
  - **Signal** — Raw source; per-section bullet analysis.
  - **Tool candidate** — `vale`, `diction`.
  - **Raised by** — Claude Haiku.

- **Check** — Verifies bullets in directive sections use active voice, not passive (flags "should be run", "is deployed by").
  - **Signal** — Raw source; per-bullet analysis.
  - **Tool candidate** — `vale`.
  - **Raised by** — Claude Haiku.

---

## 6. Final Rules File

# Project Memory File (`CLAUDE.md` / `AGENTS.md`) — Authoring Rules

**Scope.** Top-level project memory file loaded automatically by AI coding assistants at session start, at the root of a repository or well-scoped subproject.

**Audience.** Engineers and AI assistants authoring, reviewing, or consuming the file.

---

## Naming and Placement

- **Place the file at the repository root.** Assistants look there first; nested files are reserved for subprojects.
- **Use `AGENTS.md` for new projects; accept `CLAUDE.md` for ecosystem compatibility. Do not maintain both as separate content.** If both filenames exist, symlink one to the other or keep their contents byte-identical. Two independently-edited files drift.

## Structure

- **Open with an H1 title and a one-sentence summary of what the repo is and its primary stack.** Fast orientation cuts time-to-first-correct-action.
- **Organize content under stable H2 headings.** At minimum include: Overview, Commands, Architecture, Conventions, and Do Not (or a clear synonym for each). Predictable structure speeds parsing and diffs.
- **Keep the file short.** Aim for under ~200 lines and under ~32 KB; treat ~1,000 lines as a hard ceiling. Every token loads on every session.
- **Keep individual sections under roughly one screen (~60 lines).** If a section grows, link out rather than expand inline.
- **Do not include a table of contents.** At this length it is noise.

## Commands

- **List exact commands for build, test, lint, typecheck, and run in fenced code blocks, one command per line.** These are the assistant's most frequent lookups.
- **Specify the package manager explicitly (e.g., `pnpm`, not "your package manager").** Mixed package managers corrupt lockfiles.
- **Include a command for running a single test, not just the full suite.** Targeted reruns are the common iteration case.
- **Reference `package.json` scripts or `Makefile` targets; do not duplicate their contents.** Duplication guarantees drift.

## Architecture

- **Name top-level directories and what lives in each, in two lines or fewer per directory.** Provides a map without blind grepping.
- **Call out non-obvious boundaries and import rules (e.g., "`packages/core` must not import from `packages/web`").** Import rules are invisible to a reader of the tree.
- **State where generated, vendored, or codegen output lives, and mark it as non-hand-editable.** Prevents the most common class of destructive edits.
- **Link to an ADR index or authoritative architecture doc rather than restating rationale inline.** CLAUDE.md is *what*, not *why*.

## Conventions

- **State conventions only where they deviate from ecosystem defaults or are enforced in this repo.** The assistant already knows standard idioms.
- **Defer style and formatting rules to the linter/formatter config; name the tool and config file (`.eslintrc`, `.prettierrc`, `ruff.toml`, etc.).** The config is the source of truth.
- **Specify the test framework and test file-naming pattern.** Disambiguates `*.test.ts` vs. `*.spec.ts` vs. `__tests__/`.
- **Define project-specific terminology and acronyms in a short glossary.** Assistants lack the team's implicit vocabulary.

## Do Not (Prohibitions & Safety)

- **Write prohibitions as imperative negatives ("Do not run `prisma migrate` against production").** Prohibitions are the highest-ROI lines in the file.
- **Name destructive commands and environments that require confirmation (e.g., `db:reset`, `deploy:prod`, `main` branch).** The assistant cannot infer destructiveness from a command name.
- **Include a bold warning not to paste secrets or production data into AI prompts.** Habitual guardrails prevent leaks at the point of use.
- **Do not state prohibitions the assistant already infers (e.g., "don't commit secrets").** Wastes context.
- **Document the project's security-critical areas and preferred secure patterns (auth flow, PII handling, approved libraries).** Guides the AI toward approved patterns.

## Safety (File Contents)

- **Do not include secrets, tokens, credentials, PII, private endpoints, or production URLs.** The file is committed to source control and loaded into AI context.
- **Link to `SECURITY.md` and name the secrets-management system (vault path, env var loader) without values.** Directs readers to the right place without creating exposure.

## Content Hygiene

- **Link to canonical sources (ADRs, `CONTRIBUTING.md`, linter configs, runbooks) rather than duplicating them.** Duplication guarantees drift.
- **Document current reality, not aspirations.** "We use TDD" when the codebase doesn't is worse than silence.
- **Delete any claim you cannot point to a file or command to verify.** Unverifiable content is noise at best, actively misleading at worst.
- **Do not include onboarding prose, team history, motivational statements, or dated roadmap items.** Wrong audience, wrong file.
- **Mark unknowns explicitly as "Unknown as of YYYY-MM-DD" rather than omitting or guessing.** Explicit unknowns avert AI guesswork.

## Style

- **Write in concise, imperative bullets; avoid prose paragraphs.** Scannability improves reliability for humans and LLMs.
- **Use present tense and active voice.** "Tests run on every PR", not "Tests should be run".
- **Use consistent Markdown: ATX headings (`#`, `##`), `-` for bullets, fenced code blocks with language tags.** Uniformity aids parsing.
- **Use repository-relative paths for intra-repo references; reserve full URLs for external resources.** Relative paths work in forks, IDEs, and clones.
- **Keep code examples short (≤15 lines).** Link to a live file for anything larger.
- **Avoid inline images, diagrams, and raw HTML; link to assets instead.** They hinder parsing and inflate token cost.

## Maintenance and Freshness

- **Include a "Last updated: YYYY-MM-DD" line near the top, or per-section timestamps for longer files.** Visibility encourages upkeep.
- **Assign an owner or team for the file and add it to `CODEOWNERS`.** Without ownership, the file rots.
- **Review the memory file in any PR that changes commands, directory layout, dependencies, or architecture.** Drift is the default; review is the fix.
- **Keep H2 heading names stable across revisions.** Stability enables robust assistant anchoring and clean diffs.

---

*This rules file is opinionated. Thresholds (line limits, section names) are defaults; adjust per project but keep the shape.*