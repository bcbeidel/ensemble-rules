## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Include a checklist in PR templates for contributor self-review items. | Content — PR | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Keep templates concise and bounded in length. | Performance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use clear, consistent section headings to organize templates. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Include a testing / "how was this tested" section in PR templates. | Content — PR | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Require steps to reproduce / minimal example in bug report templates. | Content — Issues | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Warn contributors not to include secrets, tokens, or PII. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Require a summary / "what" section as the first PR field. | Content — PR | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Provide separate issue templates for distinct intents (bug, feature, etc.). | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Require environment / version details in bug reports. | Content — Issues | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Require a motivation / "why" section in PR templates. | Content — PR | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use imperative, specific prompts rather than vague labels. | Style | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Place templates in the `.github/` directory. | Structure | ✓ |  | ✓ |  | ✓ |  | 3 |
| Provide a PR template at `.github/PULL_REQUEST_TEMPLATE.md`. | Structure | ✓ |  | ✓ |  | ✓ |  | 3 |
| Use YAML front matter / form configuration on issue templates. | Metadata | ✓ |  | ✓ |  | ✓ |  | 3 |
| Provide a `config.yml` with `blank_issues_enabled: false` and contact links. | Metadata | ✓ |  | ✓ |  |  |  | 2 |
| Route security/vulnerability reports to a private channel. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Link to CONTRIBUTING.md / project docs from templates. | Metadata | ✓ |  |  | ✓ | ✓ |  | 3 |
| Include a "breaking changes" section or callout in PR templates. | Content — PR | ✓ |  |  | ✓ |  |  | 2 |
| Require an "alternatives considered" section in feature requests. | Content — Issues | ✓ |  |  | ✓ |  |  | 2 |
| Include a pre-submission checklist to search for duplicate issues. | Content — Issues |  |  | ✓ |  |  |  | 1 |
| Require linked issue with closing keyword (Fixes/Closes #N) in PR. | Content — PR | ✓ |  | ✓ |  |  |  | 2 |
| Use HTML comments for guidance so rendered output stays clean. | Style | ✓ |  |  |  | ✓ |  | 2 |
| Do not rely solely on HTML comments for contributor-facing instructions. | Style |  |  | ✓ | ✓ |  |  | 2 |
| Use `<details>` / collapsible blocks for long logs or guidance. | Safety / Style | ✓ |  |  |  | ✓ |  | 2 |
| Guide users on how to share large logs safely (Gist, details block, sanitized snippet). | Safety | ✓ |  |  |  | ✓ |  | 2 |
| Use dropdown/input field types for enumerable values, not free text. | Content — Issues |  |  | ✓ |  |  |  | 1 |
| Mark fields required only when triage truly needs them. | Content — Issues |  |  | ✓ |  |  |  | 1 |
| Give each template a distinct name and description in the chooser. | Metadata |  |  | ✓ |  |  |  | 1 |
| Validate YAML issue forms in CI. | Maintainability |  |  | ✓ |  |  |  | 1 |
| Review/update templates periodically to avoid drift. | Maintainability |  |  | ✓ | ✓ |  |  | 2 |
| Assign a single maintainer as owner of templates. | Maintainability |  |  |  | ✓ |  |  | 1 |
| Include a "Last updated: YYYY-MM-DD" marker in templates. | Maintainability | ✓ |  |  |  |  |  | 1 |
| Order sections by reviewer priority (most important first). | Structure | ✓ |  | ✓ | ✓ |  |  | 3 |
| Don't include checklist items the contributor can't self-verify. | Content — PR |  |  | ✓ |  |  |  | 1 |
| Prefer multiple smaller PRs over one large PR. | Performance | ✓ |  |  |  |  |  | 1 |
| Apply default labels via issue template front matter. | Metadata | ✓ |  |  |  | ✓ |  | 2 |
| Prefix issue titles via front matter (e.g., `[Bug]`, `[Feature]`). | Metadata | ✓ |  |  |  |  |  | 1 |
| Don't auto-assign issues to individuals from templates. | Safety |  |  | ✓ |  |  |  | 1 |
| Use sentence case for headings/field labels. | Style |  |  | ✓ | ✓ |  |  | 2 |
| Don't use emoji in template filenames or names. | Style |  |  | ✓ |  |  |  | 1 |
| Avoid GitHub-flavored Markdown that renders poorly on mobile. | Style |  |  |  | ✓ |  |  | 1 |
| Use inline code formatting for commands, paths, and class names. | Style |  |  |  | ✓ |  |  | 1 |
| Avoid visible placeholder text like "Describe here". | Style | ✓ |  |  |  |  |  | 1 |
| Write in a consistent tone throughout templates. | Style |  | ✓ |  |  |  |  | 1 |
| Avoid jargon or project-specific terms without explanation. | Style |  |  |  |  |  | ✓ | 1 |
| Don't overload templates with irrelevant fields / information. | Structure |  | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| Include examples to clarify contributor expectations. | Structure |  | ✓ |  |  |  |  | 1 |
| Prompt for issue/PR type to aid triage categorization. | Error Handling |  | ✓ |  |  |  |  | 1 |
| Link to Code of Conduct in top guidance (not in every template). | Safety |  |  |  | ✓ |  |  | 1 |
| Include a "no secrets/PII" item in the PR checklist. | Safety | ✓ |  |  |  |  |  | 1 |
| Don't embed example credentials or secret-like strings in templates. | Safety |  |  |  | ✓ |  |  | 1 |
| Include accessibility considerations for UI-related issues. | Safety |  |  |  |  |  | ✓ | 1 |
| Don't allow "TODO" or unfilled placeholders in final templates. | Safety |  |  |  |  |  | ✓ | 1 |
| Provide multiple PR templates only for distinct, high-volume change types. | Structure |  |  | ✓ |  |  |  | 1 |
| Don't nest template sections deeper than two heading levels. | Structure |  |  |  | ✓ |  | ✓ | 2 |
| Use a separator between boilerplate/guidance and the editable form. | Structure |  |  |  | ✓ |  |  | 1 |
| Ask for a reproducible scope (commit SHA or version) in bug reports. | Content — Issues | ✓ |  |  |  |  |  | 1 |
| Include an "out of scope" section in feature request templates. | Content — Issues | ✓ |  |  |  |  |  | 1 |
| Ask for success criteria / rollout plan in feature requests. | Content — Issues | ✓ |  |  |  |  |  | 1 |
| Include a "docs updated" item/section in PR templates. | Content — PR | ✓ |  |  |  |  |  | 1 |
| Include a "security and privacy" section in PR templates. | Content — PR | ✓ |  |  |  |  |  | 1 |
| Use "Additional context" sparingly or not at all. | Content — Issues |  |  |  | ✓ |  |  | 1 |
| Don't ask contributors for information they cannot know. | Content — Issues |  |  |  |  | ✓ |  | 1 |
| Remove fields that go unused based on evidence. | Maintainability |  |  | ✓ | ✓ |  |  | 2 |

## Notes on clustering decisions

- **"Checklist in PR templates"** — I clustered gpt-4o-mini's "checklist for potentially breaking changes" with the general PR-checklist rule since it's the only checklist guidance that model gave; a stricter reading could put it under "breaking changes callout" only.
- **"Keep templates concise / bounded length"** — Merged a wide range of numeric thresholds (200 lines, 60 lines, 8–12 sections, 500 lines, 300 words, "concise") into one cluster. A stricter clusterer might split size-in-lines vs. size-in-sections vs. word-count.
- **"Use clear, consistent section headings"** — Merged gpt-5's "H2 for all sections", haiku's "H2 only, no deeper than H3", grok's "YAML front matter or headings", and gemini's "use `##`/`###`" because they all enforce heading-based scannable structure. Splitting by heading-depth prescription would separate these.
- **"Imperative/specific prompts vs vague labels"** — Combined gpt-5's "imperatives not questions", opus's "questions or imperatives, not labels", haiku's "single clear question or imperative", gemini's "specific over general prompts", and grok's "imperative language". Note the internal tension (gpt-5 says not questions; opus says questions are fine) — I still clustered them as "specific actionable prompts".
- **"Don't overload templates with irrelevant info"** — Bundled gpt-4o-mini's "don't overload", opus's "don't ask for info maintainers won't read" / "wishlist template" warning, haiku's "section cap" + "additional context sparingly", gemini's "don't become a dumping ground", and grok's "no fluff". These overlap heavily but could be split into "no unused fields" vs "no fluff".
- **"Don't rely solely on HTML comments for instructions"** (opus, haiku) vs **"Use HTML comments for guidance"** (gpt-5, gemini) — kept as two separate rows because they are in direct tension, not the same rule.
- **"Order sections by reviewer priority"** — gpt-5's "reviewer-first ordering (Summary → Changes → Motivation → Testing)", opus's "most to least important", and haiku's "order by importance" clustered together despite differing specificity.
- **"Warn about secrets/PII"** vs **"Include a no-secrets checklist item"** vs **"Don't embed example credentials"** — kept as three separate rows; they are related safety rules but mechanically distinct (instructional warning vs. PR checkbox vs. prohibition on template content).
- **"Provide separate issue templates for distinct intents"** — gemini's "multiple focused templates in ISSUE_TEMPLATE/" and opus's "at minimum bug + feature" and gpt-5's "at least bug_report.md and feature_request.md" all cluster here; I did not separate the "minimum two" subcase.
- **"Review/update templates"** (opus's "review when CONTRIBUTING changes", haiku's "annually") merged despite different triggers.
- **"Remove unused fields based on evidence"** — opus's "remove fields not used in last 50 PRs" and haiku's "remove sections ignored by contributors" clustered; the evidence thresholds differ but the principle is the same.
- gpt-4o-mini's rules are mostly high-level and map onto multiple clusters; I resisted double-counting it across clusters where the text was too generic to confidently attribute (e.g., "prompt for issue/PR type" was kept as its own row rather than folded into "separate templates").