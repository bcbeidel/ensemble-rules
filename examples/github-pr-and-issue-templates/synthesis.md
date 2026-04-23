# Consensus Synthesis: GitHub PR and Issue Templates

## 1. Consensus Rules

### File Location & Organization
- **Place templates in `.github/` with issue templates in `.github/ISSUE_TEMPLATE/` and a single PR template at `.github/PULL_REQUEST_TEMPLATE.md`.** Establishes predictable, GitHub-native discovery. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini; near-identical path specifications)*
- **Provide at minimum separate templates for bug reports and feature requests.** Different intents need different fields; unified templates force awkward compromises. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Structure & Hierarchy
- **Use H2 (`##`) as the primary heading level for sections and avoid deeper than H3.** Creates a scannable, consistent outline that supports tooling. *(substantively similar across GPT-5, Claude Haiku, Grok)*
- **Keep templates short — target well under 100 lines of rendered content.** Long templates get skipped or skimmed; thresholds vary (Claude Opus: 60 lines; GPT-5: 200; Grok: 500). *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*
- **Limit templates to a bounded number of sections (roughly 8–12 max).** Section sprawl signals the template is doing too much. *(substantively similar across Claude Haiku, Grok)*

### PR Template Content
- **Require a "Summary/What" section capturing intent, not just a mechanical change list.** The diff shows what changed; the template must capture why. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Require a "Motivation/Why" section, ideally linking the related issue.** Reviewers need context to make trade-off decisions. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Require a "How tested" / "Testing" section.** Test evidence is the primary artifact reviewers use to assess risk. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*
- **Include a short, actionable PR checklist — contested at the margins but majority-endorsed.** Drives self-review; keep items to things contributors can genuinely verify. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok; disagreement on length — see Divergences)*
- **Instruct linking with a closing keyword (`Closes #N` / `Fixes #N`).** Enables automatic issue closure and traceability. *(substantively similar across GPT-5, Claude Opus)*

### Bug Report Content
- **Require structured reproduction: steps, expected behavior, actual behavior.** Without these, every triage starts with the same clarifying questions. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Require environment/version fields (OS, language version, relevant deps).** Most bugs are environmental; omitting this forces follow-up. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Feature Request Content
- **Require a motivation/use-case section.** Separates genuine needs from nice-to-haves. *(substantively similar across GPT-5, Claude Haiku)*
- **Request alternatives considered.** Forces critical thought and surfaces existing workarounds. *(substantively similar across GPT-5, Claude Haiku)*

### Style & Language
- **Use clear, imperative prompts or direct questions, not vague labels.** "What did you expect to happen?" beats "Expected behavior." *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*
- **Avoid jargon; write for first-time contributors.** Templates should not assume project-specific domain knowledge. *(substantively similar across Claude Haiku, Grok)*

### Safety & Privacy
- **Explicitly warn against pasting secrets, tokens, passwords, or PII in any free-text field.** Issue trackers are public; users will paste `.env` contents unless told not to. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Route vulnerability reports away from the public issue tracker (SECURITY.md or `config.yml` contact link).** Public trackers are not a responsible disclosure venue. *(substantively similar across GPT-5, Claude Opus, Gemini)*
- **Provide a collapsible `<details>` block or equivalent for pasting logs, with a redaction reminder.** Limits accidental exposure and UI noise. *(substantively similar across GPT-5, Claude Opus, Gemini)*

### Metadata & Triage Automation
- **Use YAML front matter on Markdown issue templates (name, about, title, labels).** Powers the template chooser UI and auto-triage. *(substantively similar across GPT-5, Gemini)*
- **Provide `.github/ISSUE_TEMPLATE/config.yml` with `blank_issues_enabled: false` and `contact_links`.** Channels contributors into triageable paths. *(substantively similar across GPT-5, Claude Opus)*

### Maintenance
- **Link to `CONTRIBUTING.md` rather than duplicating policy inline.** Duplication guarantees drift. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Don't bury instructions in HTML comments alone — contributors on mobile and new users won't see them.** Comments disappear on render and get submitted verbatim. *(substantively similar across Claude Opus, Claude Haiku; directly contradicted by GPT-5 and Gemini — see Divergences)*

---

## 2. Strong Minority Rules

- **Validate YAML issue forms against GitHub's schema in CI.** *(Claude Opus only.)* Kept because an invalid form silently falls back to a blank issue — a genuine silent-failure mode worth catching.
- **Prefer YAML issue forms (`.yml`) over Markdown issue templates.** *(Claude Opus; directly opposed by GPT-5.)* Kept because Opus's reasoning — required fields, typed inputs, dropdown enumeration, built-in validation — is materially stronger than "Markdown is git-diffable," and matches GitHub's own direction of travel. Flagged as contested.
- **Use `dropdown` for enumerable values with a pinned option list.** *(Claude Opus only.)* Kept because free-text "OS" fields producing 47 spellings of "macOS" is a concrete, common pathology.
- **Only mark a field `required: true` if triage genuinely cannot proceed without it.** *(Claude Opus only.)* Kept because over-requiring is the dominant failure mode of strict issue forms and specifically excludes non-native-English contributors.
- **Don't include PR checklist items the contributor cannot self-verify** (e.g., "security team approved"). *(Claude Opus only.)* Kept because it's a sharp, generalizable principle: self-attestation only works for things the author actually controls.
- **Remove fields that haven't been meaningfully used in the last ~50 issues/PRs.** *(Claude Opus only.)* Kept because it inverts the usual "add a field" bias with evidence-based pruning.
- **Include a pre-submission "I searched existing issues" checkbox.** *(Claude Opus only.)* Kept because it's the cheapest duplicate-reduction mechanism available.
- **Assign a single maintainer as owner of template content.** *(Claude Haiku only.)* Kept because collective ownership of config artifacts reliably produces drift.
- **Include a "Last updated: YYYY-MM-DD" comment at the top of each template.** *(GPT-5 only.)* Kept as a lightweight, mechanical way to surface staleness.
- **Include a "Breaking Changes" section with explicit "None" when N/A.** *(GPT-5 only.)* Kept because implicit "no breaking changes" is a common source of post-merge surprise.

---

## 3. Divergences

### Markdown vs. YAML Issue Forms
- **GPT-5**: Prefer Markdown — git-native, diffable, portable, simpler.
- **Claude Opus**: Prefer YAML forms — enforced structure, required fields, typed inputs; markdown "masquerading as a form" is a named failure mode.
- **Gemini, Claude Haiku, Grok**: Assume Markdown without strong argument either way.
- **Synthesis**: YAML forms are materially better for bug reports on projects of any meaningful size — the structural validation and dropdown enumeration solve real problems Markdown cannot. GPT-5's "git-diffable" argument applies equally to YAML. **Recommend YAML forms for issue templates on repos with more than trivial traffic; allow Markdown for small/hobby projects.**

### Instructions in HTML Comments
- **GPT-5**: Put guidance in HTML comments; keep rendered output clean.
- **Gemini**: Use HTML comments for instructions so they disappear from submissions.
- **Claude Opus**: Never rely on HTML comments alone — they're invisible on mobile and submitted verbatim by new users.
- **Claude Haiku**: Use visible italic sub-headers for intent; comments are a trap.
- **Synthesis**: Claude's position has stronger evidence (mobile UX, verbatim submission is a well-documented pathology). **Recommend: use YAML `description:` fields where possible; for Markdown, put critical guidance visibly (e.g., italicized one-liners under headings) and reserve HTML comments for examples/advanced notes only.**

### PR Checklist Length
- **GPT-5**: Require at least 5 checklist items.
- **Claude Opus**: At most 6 items — longer checklists are theater.
- **Claude Haiku**: Make checklists advisory, not gating; warn against reflexive checking.
- **Grok**: Use checklists liberally.
- **Synthesis**: The convergence is **3–6 items, each genuinely consequential, positioned at the end, and none that the contributor cannot self-verify.** GPT-5's floor of 5 and Opus's ceiling of 6 overlap at 5–6, which is the defensible sweet spot.

### Template Length Thresholds
- **Claude Opus**: 60 lines
- **Claude Haiku**: 8–12 sections
- **GPT-5**: 200 lines / 10 KB for PR; 250 / 10 KB for issues
- **Grok**: 500 lines
- **Synthesis**: Numbers are opinion, not science. **Use soft limits: warn above ~80 rendered lines, fail above ~250.** Thresholds should be project-configurable.

### Prescription vs. Flexibility
- **Grok**: Explicitly argues for opinionated, prescriptive templates.
- **Claude Haiku**: Explicitly argues for escape hatches and flexibility.
- **Synthesis**: Both are right in context — prescriptive for high-volume open-source, flexible for small teams. The rules file should default to prescriptive (it's the safer failure mode) but call this out as context-dependent.

### Emoji in Template Names
- **Claude Opus** (contested): Ban them — breaks CLI tooling and screen readers.
- Everyone else: Silent.
- **Synthesis**: Minority position, but the accessibility argument is real. **Keep as a soft rule / opt-in check.**

---

## 4. Notable Omissions

- **GPT-4o-mini omits nearly everything.** Its rules file is so generic ("Do use clear headings," "Do keep templates concise") that it skips every substantive consensus rule — no mention of reproduction steps, no linked-issue convention, no safety/PII warning, no front matter, no config.yml, no bug-vs-feature split. Signal: this response carries almost no independent weight.
- **Grok omits safety-side PII/secret warnings** despite these appearing in all four other substantive responses. Notable gap.
- **Grok omits the bug-vs-feature template split**, treating templates as generic.
- **Gemini omits the PR checklist item-count guidance** that GPT-5, Opus, and Haiku all discuss.
- **GPT-4o-mini and Grok both omit any mention of `config.yml`, `contact_links`, or SECURITY.md** — core GitHub-specific plumbing that the other three models all address.
- **Gemini and Grok omit the "link don't duplicate CONTRIBUTING.md" rule** that Opus, Haiku, and GPT-5 all raise.
- **Claude Haiku omits YAML front matter guidance for issue templates** — notable because it otherwise discusses template metadata extensively.
- **GPT-5 omits the "don't bury guidance in HTML comments" concern**, going in the opposite direction and actively recommending comments. This is the cleanest cross-model contradiction.

---

## 5. Shared Deterministic Checks

### Multi-model checks

- **Check** — Verify a PR template file exists at the canonical path `.github/PULL_REQUEST_TEMPLATE.md`.
  - **Signal** — File system listing.
  - **Tool candidate** — ad-hoc (trivial path existence).
  - **Raised by** — GPT-5, Gemini, Claude Opus (implicitly via scope).
  - **Variance** — GPT-5 additionally forbids the multi-template directory variant; Opus allows it; Gemini is neutral. Substance aligns on the single-template case.

- **Check** — Verify both a bug-report and a feature-request issue template exist under `.github/ISSUE_TEMPLATE/`.
  - **Signal** — Directory listing + filename/name-field regex.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 expects exact filenames (`bug_report.md`, `feature_request.md`); Opus matches by regex on filename or `name` field (more robust); Haiku uses path-substring heuristic. Opus's approach is the most tolerant.

- **Check** — Parse template markdown and verify heading levels are consistent (H2 primary, no deeper than H3).
  - **Signal** — Parsed Markdown AST, excluding fenced code blocks.
  - **Tool candidate** — `remark` / `markdownlint` (rule MD001/MD025).
  - **Raised by** — GPT-5, Claude Haiku, Grok.
  - **Variance** — GPT-5 is strictest (exactly H2 only); Haiku allows H3 sub-sections; Grok forbids H4+. Convergence on "no H4 or deeper"; disagreement on whether H3 is allowed.

- **Check** — Verify the PR template contains sections matching required headings (Summary, Motivation/Why, Testing).
  - **Signal** — Parsed Markdown AST + regex on heading text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — GPT-5 requires exact heading strings from a fixed list; Opus/Haiku use case-insensitive regex (`/what/i`, `/why|motivation/i`, `/test/i`) — more robust. GPT-5's strictness is over-fitted to one team's taxonomy.

- **Check** — Verify the PR template contains at least one Markdown checkbox, with a bounded count (minimum ~3–5, maximum ~6–10).
  - **Signal** — Raw markdown; regex `^- \[ \]` or `^\* \[ \]`.
  - **Tool candidate** — ad-hoc (trivial regex count).
  - **Raised by** — GPT-5 (≥5), Claude Opus (≤6), Gemini (≥1), Claude Haiku (advisory), Grok.
  - **Variance** — Models disagree on bounds; converge on "count is checkable."

- **Check** — Verify the bug-report template prompts for reproduction steps and expected/actual behavior.
  - **Signal** — Markdown AST (for `.md`) or parsed YAML `body` labels (for YAML forms).
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Opus checks YAML `attributes.label`; others do header regex on markdown. Substance aligns.

- **Check** — Verify a warning about secrets/tokens/PII appears near any field that accepts logs or stack traces.
  - **Signal** — Raw markdown or YAML `description`; keyword regex (`/secret|token|password|credential|PII|redact/i`).
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Opus scopes the check to textareas whose label matches `/log|trace|output|error/i`; others check document-wide. Opus's approach has far fewer false positives.

- **Check** — Verify `.github/ISSUE_TEMPLATE/config.yml` exists, disables blank issues, and declares at least one `contact_link` (preferably one matching `/security|vulnerab/i`).
  - **Signal** — Parsed YAML of `config.yml`.
  - **Tool candidate** — ad-hoc (yaml parse + key assertion).
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Agree on substance.

- **Check** — Verify issue template files begin with valid YAML front matter containing `name`, `about`, (and ideally `title`, `labels`).
  - **Signal** — Front-matter parse of each `.md` in `.github/ISSUE_TEMPLATE/`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Gemini.
  - **Variance** — GPT-5 also requires `title` and `labels`; Gemini only checks structural presence. Escalation path: presence → completeness.

- **Check** — Verify total template line count / byte size is below a threshold.
  - **Signal** — File `wc -l` / file size.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5 (200/250 lines), Claude Opus (60), Claude Haiku (8–12 sections), Grok (500), GPT-4o-mini (300 words).
  - **Variance** — Wide disagreement on the threshold; agreement that "there should be one." Make configurable.

- **Check** — Verify credential-looking strings and common dummy tokens (`sk-`, `ghp_`, `API_KEY=...`) don't appear inside the template itself.
  - **Signal** — Raw markdown; regex against known credential prefixes.
  - **Tool candidate** — `gitleaks`, `trufflehog`, or `detect-secrets` (would catch template contents along with repo contents).
  - **Raised by** — Claude Haiku, implicit in GPT-5 and Gemini safety rules.
  - **Variance** — Substantively equivalent.

### Singleton checks worth generalizing

- **Check** — Validate YAML issue forms against GitHub's issue-form schema (or at least against required keys `name`, `description`, `body`, and per-item `type`/`attributes`).
  - **Signal** — Parsed YAML of each `.github/ISSUE_TEMPLATE/*.yml`.
  - **Tool candidate** — community JSON Schemas for GitHub issue forms; SchemaStore.
  - **Raised by** — Claude Opus.

- **Check** — For any issue-form `body` entry of type `dropdown`, verify `attributes.options` exists and contains at least two entries.
  - **Signal** — Parsed YAML body array.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — For any issue-form `body` entry whose label matches `/version|environment|OS|platform|browser/i`, verify `type` is `input` or `dropdown` rather than `textarea`.
  - **Signal** — Parsed YAML body.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — For any issue template, verify the presence of a `checkboxes` body item that includes a "searched existing issues" option (regex `/search(ed)?|existing|duplicate/i`).
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — For each template, verify a `Last updated: YYYY-MM-DD` marker exists in a top-of-file HTML comment.
  - **Signal** — Raw markdown regex `/Last updated:\s*\d{4}-\d{2}-\d{2}/`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — For each PR template, verify that the `## Checklist` section, if present, is the last section.
  - **Signal** — Markdown AST; index of "Checklist" heading vs. subsequent headings.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — For bug-report issue templates, verify presence of a `<details>...</details>` block wrapping log-paste areas.
  - **Signal** — Raw markdown substring check.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — For any filename or YAML `name:` field, flag presence of characters matching Unicode `\p{Extended_Pictographic}` (emoji).
  - **Signal** — File names + parsed YAML.
  - **Tool candidate** — `emoji-regex`.
  - **Raised by** — Claude Opus.

- **Check** — For any non-boilerplate Markdown paragraph, flag visible placeholder patterns (`TODO`, `Describe here`, `[enter...]`, `<enter...>`) outside of HTML comments.
  - **Signal** — Raw markdown with comment regions masked.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Verify `SECURITY.md` exists at the repo root or `.github/`, OR `config.yml` lists a contact link with name matching `/security|vulnerab/i`.
  - **Signal** — File system + parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

---

## 6. Final Rules File

# GitHub PR and Issue Templates — Rules

**Scope:** `.github/PULL_REQUEST_TEMPLATE.md`, `.github/PULL_REQUEST_TEMPLATE/*.md`, `.github/ISSUE_TEMPLATE/*.md`, `.github/ISSUE_TEMPLATE/*.yml`, and `.github/ISSUE_TEMPLATE/config.yml` in any GitHub-hosted repository.

**Audience:** Engineers, maintainers, and AI assistants creating or modifying these templates.

---

## File Location and Organization

- Place all templates under `.github/`. Put a single PR template at `.github/PULL_REQUEST_TEMPLATE.md`; put issue templates under `.github/ISSUE_TEMPLATE/`. Keeps contributor-facing config in one predictable location.
- Provide at minimum a bug-report template and a feature-request template as separate files. Different intents need different fields; unified templates force awkward compromises.
- Provide `.github/ISSUE_TEMPLATE/config.yml` with `blank_issues_enabled: false` and a `contact_links` list including a security/disclosure channel. Channels contributors into triageable paths and keeps vulnerability reports out of the public tracker.
- Prefer YAML issue forms (`.yml`) over Markdown (`.md`) for bug reports and feature requests on projects with more than hobby-level traffic. Typed inputs, required fields, and dropdowns prevent classes of bad data that Markdown cannot. (contested — use Markdown for very small projects if simplicity matters more than structure.)

## Structure

- Use H2 (`##`) as the primary heading level for sections; do not nest deeper than H3. Creates a scannable, consistent outline.
- Keep each template focused: aim for ≤80 rendered lines and ≤12 top-level sections. Longer templates get skipped or skimmed.
- Order sections from highest reviewer priority to lowest: Summary first, then reproduction/context, then environment, then extras. Reviewers stop reading partway; put the critical fields first.
- Give each issue template a distinct `name` and `description`. Contributors choose by these; ambiguity guarantees misfiling.

## PR Template Content

- Include a "Summary" / "What does this PR do?" section as the first editable field. The diff shows the mechanical change; the template must capture intent.
- Include a "Motivation" / "Why" section, and instruct contributors to link the related issue with a closing keyword (`Closes #N`, `Fixes #N`). Enables automatic issue closure and bidirectional traceability.
- Include a "How was this tested?" section. Test evidence is the primary artifact reviewers use to assess risk.
- Include a "Breaking Changes" section with an explicit "None" if not applicable. Explicit "None" prevents ambiguity and post-merge surprise.
- Include a PR checklist of 3–6 actionable items, placed at the end of the template. (contested — some teams consider checklists theater.)
- Every checklist item must be something the contributor can self-verify (e.g., "tests added", "docs updated", "no secrets in diff"). Items like "security team approved" belong in CODEOWNERS or branch protection, not a checkbox.
- Include exactly one checklist item reminding the author they have confirmed no secrets/PII are included. A visible reminder reduces accidents.

## Bug Report Content

- Require structured fields for: steps to reproduce, expected behavior, actual behavior, environment (OS, language/runtime version, relevant dependency versions). Without these, every triage starts with the same clarifying questions.
- Model enumerable values (OS, severity, affected component) as `dropdown` fields with a pinned option list. Free text produces 47 spellings of "macOS."
- Wrap log-paste fields in a collapsible `<details>` block (Markdown) or a `textarea` with a `render:` language hint (YAML forms). Ask for minimal, sanitized snippets, not full logs. Limits exposure and UI noise.
- Include a pre-submission checkbox asking the user to confirm they searched for existing issues. Cheapest duplicate-reduction mechanism available.

## Feature Request Content

- Require a "Motivation / use case" section. Separates genuine needs from nice-to-haves.
- Require an "Alternatives considered" section. Forces critical thought and surfaces existing workarounds.

## Style and Language

- Write prompts as direct questions or imperatives, not vague labels. "What did you expect to happen?" beats "Expected behavior."
- Put contributor-facing instructions in YAML `description:` fields or visible italic prose. Do not hide critical guidance in HTML comments alone — comments are invisible on mobile and routinely submitted verbatim by new users.
- Use sentence case for headings and field labels. Consistent with GitHub's own UI.
- Avoid project-specific jargon or assumed domain knowledge. Templates should work for first-time contributors.
- Do not use emoji in template filenames or `name:` fields. (contested — many projects embrace this.) Breaks some CLI tooling and screen readers; decorative value is low.

## Safety and Privacy

- Explicitly warn contributors not to paste secrets, tokens, passwords, credentials, or PII in any free-text field, and instruct them to redact logs before submitting. Issue trackers are public; users will paste `.env` contents unless told not to.
- Do not include example strings that look like real credentials (e.g., `sk-...`, `ghp_...`, `API_KEY=...`) in the template itself. Trains contributors to paste similar patterns and risks false-positive secret scanning.
- Route vulnerability disclosures away from the public issue tracker — provide a `SECURITY.md` at the repo root and/or a security `contact_link` in `config.yml`. Public trackers are not a responsible disclosure venue.

## Metadata and Automation

- For Markdown issue templates, include YAML front matter with `name`, `about`, `title`, and `labels`. Powers the template chooser and auto-triage.
- Apply default labels via front matter or YAML form `labels:` — `bug` on bug reports, `enhancement` on feature requests. Auto-labeling speeds triage.
- Prefix issue titles via front matter (`[Bug]`, `[Feature]`) to aid inbox scanning.
- Do not auto-assign issues to individuals from the template. Creates bus-factor pressure and bypasses rotation; apply labels instead.
- Mark a YAML form field `required: true` only if triage genuinely cannot proceed without it. Over-requiring blocks legitimate reports, especially from non-native English speakers and first-time contributors.

## Maintainability

- Link from templates to `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`; do not copy their contents inline. Duplication guarantees divergence.
- Include a `<!-- Last updated: YYYY-MM-DD -->` marker at the top of each template. Visible freshness encourages upkeep.
- Assign a single maintainer as the owner of template content. Collective ownership of config artifacts reliably produces drift.
- Review templates when CONTRIBUTING, CI, or the supported-version matrix changes, and prune fields that have not been meaningfully used in the last ~50 submissions. Evidence beats speculation about what's useful.
- Validate YAML issue forms in CI against GitHub's form schema. An invalid form silently falls back to a blank issue on GitHub.
- Do not rename required section headings without updating downstream automation. Consistency protects bots and scripts.