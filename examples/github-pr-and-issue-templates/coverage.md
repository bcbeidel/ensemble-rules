# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **Assign a single maintainer as the owner of template content.** When templates fail, someone should own the fix | Governance |  |  |  | ✓ |  |  | 1 |
| **Do not ask for sensitive information (passwords, API keys, personal data) in templates.** Remind contributors that issues are public | Safety and Compliance |  |  |  | ✓ |  |  | 1 |
| **Do not encode secrets or examples containing credentials in the template itself.** Even if the example looks fake, it trains contributors to use the template as a reference and increases the risk of accidental leaks | Safety and Compliance |  |  |  | ✓ |  |  | 1 |
| **Do not require a checklist of "I have run tests," "I have updated docs," etc., unless your CI cannot enforce it.** (contested) Checklists without enforcement create false confidence | Required Sections for Pull Request Templates |  |  |  | ✓ |  |  | 1 |
| **Do not use GitHub-flavored Markdown features that are poorly supported on mobile or in email (complex tables, collapsible sections).** Mobile users make up a significant fraction of contributors | Formatting and Content |  |  |  | ✓ |  |  | 1 |
| **Do** create a `.github/PULL_REQUEST_TEMPLATE.md` file for pull requests | Structure and Content |  |  |  |  | ✓ |  | 1 |
| **Do** explicitly warn users not to post sensitive data like passwords, API keys, or PII | Safety |  |  |  |  | ✓ |  | 1 |
| **Do** include a checklist in PR templates for critical, self-reviewable items | Structure and Content |  |  |  |  | ✓ |  | 1 |
| **Do** instruct users on the preferred method for sharing large logs or files | Safety |  |  |  |  | ✓ |  | 1 |
| **Do** place all issue templates inside the `.github/ISSUE_TEMPLATE/` directory | Structure and Content |  |  |  |  | ✓ |  | 1 |
| **Do** prefer specific questions over general prompts | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| **Do** provide stable links to core project documentation like `CONTRIBUTING.md` | Maintainability |  |  |  |  | ✓ |  | 1 |
| **Do** use HTML comments (`<!-- | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| **Do** use Markdown headings (`##` or `###`) to create distinct, scannable sections | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| **Do** use YAML frontmatter in issue templates to configure the template chooser | Structure and Content |  |  |  |  | ✓ |  | 1 |
| **Do** wrap non-essential or lengthy instructional text in `<details>` tags | Structure and Content |  |  |  |  | ✓ |  | 1 |
| **Document the template in your CONTRIBUTING.md or README, explaining the purpose of each section and what makes a good submission.** The template itself cannot cover everything | Governance |  |  |  | ✓ |  |  | 1 |
| **Don't ask for information the maintainers will not read.** Every unused field is pure contributor tax | Content — Issue Templates |  |  | ✓ |  |  |  | 1 |
| **Don't auto-assign issues to individuals from the template.** Creates bus-factor pressure and bypasses rotation | Safety |  |  | ✓ |  |  |  | 1 |
| **Don't include items the contributor cannot verify themselves** (e.g., "reviewed by security team") | Content — PR Templates |  |  | ✓ |  |  |  | 1 |
| **Don't use emoji in template filenames or `name:` fields.** (contested) Breaks CLI tooling and screen readers; decorative value is low | Style |  |  | ✓ |  |  |  | 1 |
| **Don't** ask contributors for information they cannot reasonably know | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| **Don't** let templates become a dumping ground for every possible edge case | Maintainability |  |  |  |  | ✓ |  | 1 |
| **Ensure every section title is a single, clear question or imperative.** Use "What problem does this solve?" not "Problem Description" or "Rationale for changes." | Structure |  |  |  | ✓ |  |  | 1 |
| **For bug reports, include "Environment" (language version, OS, relevant dependencies) to the extent it's material.** Many bugs are environmental | Required Sections for Issue Templates |  |  |  | ✓ |  |  | 1 |
| **For bug reports, include a "Steps to reproduce" or "Minimal example" section.** Vague bug reports are useless | Required Sections for Issue Templates |  |  |  | ✓ |  |  | 1 |
| **For feature requests, include a "Motivation and use case" section.** Not every feature is worth building | Required Sections for Issue Templates |  |  |  | ✓ |  |  | 1 |
| **For security-relevant projects, route vulnerability reports out of the issue tracker via `config.yml` `contact_links` to a private channel.** Public issue trackers are not a responsible disclosure venue | Safety |  |  | ✓ |  |  |  | 1 |
| **Give each template a distinct `name` and `description` visible in the chooser.** Contributors pick by these; ambiguity guarantees misfiling | Structure |  |  | ✓ |  |  |  | 1 |
| **If your project has a Code of Conduct, link to it once in the top guidance section, not in every template.** Repetition reduces impact | Safety and Compliance |  |  |  | ✓ |  |  | 1 |
| **Include a "Describe the problem or feature request" section as the first editable field.** This is the core of the issue | Required Sections for Issue Templates |  |  |  | ✓ |  |  | 1 |
| **Include a "Does this break anything?" or "Breaking changes" section.** This surfaces risk | Required Sections for Pull Request Templates |  |  |  | ✓ |  |  | 1 |
| **Include a "How was this tested?" section for PRs that touch behavior or code paths.** Reviewers need to know whether the change was actually tested and how | Required Sections for Pull Request Templates |  |  |  | ✓ |  |  | 1 |
| **Include a "What does this PR do?" or "Summary" section as the first editable field.** This is the most important field | Required Sections for Pull Request Templates |  |  |  | ✓ |  |  | 1 |
| **Include a "Why are we making this change?" section.** Link to an issue, explain the motivation, or describe the context | Required Sections for Pull Request Templates |  |  |  | ✓ |  |  | 1 |
| **Include a checklist of at most six items, each actionable by the contributor before review.** (contested) Longer checklists are ticked without being read | Content — PR Templates |  |  | ✓ |  |  |  | 1 |
| **Include a pre-submission checklist that requires searching existing issues.** Cheapest duplicate-reduction mechanism available | Content — Issue Templates |  |  | ✓ |  |  |  | 1 |
| **Include an "Alternatives you've considered" section for feature requests.** This forces contributors to think critically and prevents duplicates by surfacing existing workarounds | Required Sections for Issue Templates |  |  |  | ✓ |  |  | 1 |
| **Include an `.github/ISSUE_TEMPLATE/config.yml` that disables blank issues and links to support channels.** Forces contributors into a triageable path and routes questions away from the issue tracker | Structure |  |  | ✓ |  |  |  | 1 |
| **Include an explicit warning against pasting secrets, tokens, or PII in any field that accepts logs or stack traces.** Contributors will paste `.env` contents; tell them not to | Safety |  |  | ✓ |  |  |  | 1 |
| **Keep a single source of truth: link from templates to CONTRIBUTING.md, don't copy content.** Duplication guarantees divergence | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Keep descriptions concise (one sentence per bullet or field).** Long prose in a template is not read | Formatting and Content |  |  |  | ✓ |  |  | 1 |
| **Keep each template under 60 lines of rendered content.** Longer templates get skimmed, not read | Structure |  |  | ✓ |  |  |  | 1 |
| **Limit each template to 8–12 sections maximum.** Longer templates are skipped | Structure |  |  |  | ✓ |  |  | 1 |
| **Link to your CONTRIBUTING.md or relevant docs in the top guidance section, not inline in every field.** Readers should know where to find reference material; don't repeat it in the template | Formatting and Content |  |  |  | ✓ |  |  | 1 |
| **Mark a field `required: true` only if triage genuinely cannot proceed without it.** Over-requiring blocks legitimate reports from users who lack the information | Content — Issue Templates |  |  | ✓ |  |  |  | 1 |
| **Order sections by importance, not by logical grouping.** The first section reviewers care about (problem statement, change summary) should appear first, before boilerplate or rationale | Structure |  |  |  | ✓ |  |  | 1 |
| **Order sections from most to least important: summary, reproduction/context, environment, extras.** Reviewers stop reading partway; put the critical fields first | Structure |  |  | ✓ |  |  |  | 1 |
| **Place templates in `.github/`, not the repo root.** Keeps contributor-facing metadata in one predictable directory | Structure |  |  | ✓ |  |  |  | 1 |
| **Provide a one-line explanation below each section header, in italic text, stating what belongs there and why.** This surfaces intent without requiring contributors to infer it | Structure |  |  |  | ✓ |  |  | 1 |
| **Provide at minimum a bug report and a feature request template.** These cover the two dominant intents; anything else is opt-in | Structure |  |  | ✓ |  |  |  | 1 |
| **Provide multiple PR templates via `.github/PULL_REQUEST_TEMPLATE/` only when you have distinct, high-volume change types** (e.g., docs-only, dependency bump) | Content — PR Templates |  |  | ✓ |  |  |  | 1 |
| **Put contributor instructions in `description:` fields (YAML) or visible prose, never in HTML comments alone.** Comments are invisible on GitHub mobile and routinely submitted verbatim | Style |  |  | ✓ |  |  |  | 1 |
| **Remove fields that haven't been meaningfully used in the last 50 issues/PRs.** Evidence beats speculation about what's useful | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Require a "How tested" section.** Test plans in the PR are the primary artifact reviewers use to decide if CI coverage is adequate | Content — PR Templates |  |  | ✓ |  |  |  | 1 |
| **Require a "What" and "Why" section.** Diff shows what changed mechanically; the template must capture intent | Content — PR Templates |  |  | ✓ |  |  |  | 1 |
| **Require a linked issue using a closing keyword (`Closes #123`).** Enables automatic issue closure and bidirectional traceability | Content — PR Templates |  |  | ✓ |  |  |  | 1 |
| **Require a reproduction section for bug reports with fields for expected vs | Content — Issue Templates |  |  | ✓ |  |  |  | 1 |
| **Require version/environment fields as `input` or `dropdown` types, not free text.** Structured input enables filtering and prevents "latest" as an answer | Content — Issue Templates |  |  | ✓ |  |  |  | 1 |
| **Review and update templates at least annually, or when contributor feedback indicates sections are confusing or ignored.** Templates drift | Governance |  |  |  | ✓ |  |  | 1 |
| **Review templates whenever CONTRIBUTING.md, CI, or the supported-version matrix changes.** Templates go stale silently; nothing fails when they do | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Start with a brief, genuine welcome statement (1–2 lines max).** Contributors are often anxious | Structure |  |  |  | ✓ |  |  | 1 |
| **Use H2 headers (##) for top-level sections and no deeper than H3.** This creates a scannable outline | Structure |  |  |  | ✓ |  |  | 1 |
| **Use YAML issue forms (`.yml`) for issue templates, not markdown.** Forms enforce structure, required fields, and input types; markdown does not | Structure |  |  | ✓ |  |  |  | 1 |
| **Use `dropdown` for enumerable values (OS, severity, component) and pin the allowed list.** Free text produces 47 spellings of "macOS" | Content — Issue Templates |  |  | ✓ |  |  |  | 1 |
| **Use a "Additional context" section sparingly, if at all.** This is a catch-all that discourages thought | Required Sections for Issue Templates |  |  |  | ✓ |  |  | 1 |
| **Use a explicit separator (e.g., `---`) between template boilerplate and the form itself.** The form section is what contributors edit | Structure |  |  |  | ✓ |  |  | 1 |
| **Use examples liberally, but place them outside the template as visible guidance text or in linked docs.** Do not embed lengthy examples in the template; they inflate file size | Formatting and Content |  |  |  | ✓ |  |  | 1 |
| **Use inline code formatting (backticks) for command names, file paths, and class names.** This improves clarity and is parseable by bots | Formatting and Content |  |  |  | ✓ |  |  | 1 |
| **Use sentence case for field headers, not Title Case.** Sentence case is more readable and is the convention for natural language | Formatting and Content |  |  |  | ✓ |  |  | 1 |
| **Use sentence case for headings and field labels.** Consistent with GitHub's own UI | Style |  |  | ✓ |  |  |  | 1 |
| **Use separate templates for PRs and Issues, and separate Issue Templates for bugs, features, and docs.** Each template type has different information needs; unified templates create ambiguity and encourage skipping sections | Structure |  |  |  | ✓ |  |  | 1 |
| **Validate YAML issue forms in CI.** An invalid form silently falls back to a blank issue on GitHub | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Version your templates implicitly by dating them or linking them to a CHANGELOG entry if you make significant changes.** This helps you track what changed and why | Governance |  |  |  | ✓ |  |  | 1 |
| **Write prompts as questions or imperatives, not labels.** "What did you expect to happen?" beats "Expected behavior" | Style |  |  | ✓ |  |  |  | 1 |
| *Rationale:* "What version of Node.js are you using?" elicits better data than "Describe your environment." | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* A clear structure helps both the author fill out the template and the reviewer parse the information | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Asking a user to identify the specific line of code causing a bug is unproductive and frustrating | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Automating categorization and assignment saves maintainer time | Structure and Content |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Overly complex templates are ignored or filled out incorrectly; they should serve the 80% case well | Maintainability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This connects the template to the wider project context and avoids duplicating information | Maintainability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This enables the user to select the most relevant template from a menu | Structure and Content |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This ensures a consistent structure for every pull request, aiding reviewers | Structure and Content |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This forces contributors to confirm they have completed necessary steps like writing tests or updating docs | Structure and Content |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This helps prevent accidental secret exposure in a public forum | Safety |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This keeps the initial template view clean and less intimidating | Structure and Content |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This prevents unmanageably large issues and points users toward safe practices like using Gists or `<details>` blocks | Safety |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This provides a clear `name` and `about` description for users selecting a template | Structure and Content |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This provides guidance to the author without cluttering the final submission for the reader | Clarity and Usability |  |  |  |  | ✓ |  | 1 |
| Apply default labels via front matter: “bug” on bug reports and “enhancement” on feature requests | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ask for a reproducible scope (commit SHA or version) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ask for success criteria and a rollout/flag plan | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Consider whether to include detailed step-by-step instructions | Contested |  | ✓ |  |  |  |  | 1 |
| Do add a reminder to check for accessibility in UI-related issues | Safety and Best Practices |  |  |  |  |  | ✓ | 1 |
| Do include a checklist for potentially breaking changes | Safety |  | ✓ |  |  |  |  | 1 |
| Do include a security checklist in PR templates for code changes | Safety and Best Practices |  |  |  |  |  | ✓ | 1 |
| Do include examples where applicable | Structure |  | ✓ |  |  |  |  | 1 |
| Do include mandatory fields like "Description," "Steps to Reproduce," and "Expected/Actual Behavior" in issue templates | Content Requirements |  |  |  |  |  | ✓ | 1 |
| Do keep template files under 500 lines | Performance |  |  |  |  |  | ✓ | 1 |
| Do keep templates concise | Performance |  | ✓ |  |  |  |  | 1 |
| Do limit the template to 5-10 sections to avoid overwhelming contributors | Structure |  |  |  |  |  | ✓ | 1 |
| Do not ask reporters to paste entire raw logs by default; ask for minimal, sanitized snippets inside a collapsible block | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not rename required section headings without updating downstream automation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do prompt for issue/PR type | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do require a "Summary of Changes" and "Testing Performed" in PR templates | Content Requirements |  |  |  |  |  | ✓ | 1 |
| Do use a consistent YAML front matter or Markdown headings to organize sections | Structure |  |  |  |  |  | ✓ | 1 |
| Do use bullet points or numbered lists for checklists | Style and Formatting |  |  |  |  |  | ✓ | 1 |
| Do use clear headings | Structure |  | ✓ |  |  |  |  | 1 |
| Do write in a consistent tone | Style |  | ✓ |  |  |  |  | 1 |
| Do write in clear, imperative language (e.g., "Provide details here") | Style and Formatting |  |  |  |  |  | ✓ | 1 |
| Don't allow optional fields to be truly optional without defaults | Content Requirements |  |  |  |  |  | ✓ | 1 |
| Don't include unnecessary examples or fluff | Performance |  |  |  |  |  | ✓ | 1 |
| Don't nest sections deeper than two levels | Structure |  |  |  |  |  | ✓ | 1 |
| Don't permit placeholders like "TODO" in final templates | Safety and Best Practices |  |  |  |  |  | ✓ | 1 |
| Don't use jargon or project-specific terms without explanation | Style and Formatting |  |  |  |  |  | ✓ | 1 |
| Don’t assume contributors will know what info is necessary | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t limit templates to just the mandatory fields without offering room for additional context | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t overload templates with irrelevant information | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t skip templates for critical areas like security vulnerabilities | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t use jargon or overly technical language | Style |  | ✓ |  |  |  |  | 1 |
| Each Markdown issue template must start with YAML front matter defining name, about, title, and labels | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In “Breaking Changes,” require “None” if none | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In “Docs,” require “Updated” or “N/A” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In “Linked Issues,” instruct to use “Fixes #<id>” or “Closes #<id>” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In “Security and Privacy,” ask for data impact, permissions, and threat-model changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| In “Testing,” request commands/steps and evidence (logs, screenshots) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a checklist item confirming no secrets/PII are included | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a security contact path (SECURITY.md or a contact link) in templates or config | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include an HTML comment “Last updated: YYYY-MM-DD” at the top of each template | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include at least five unchecked checklist items in the PR template | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include links to CONTRIBUTING.md and CODE_OF_CONDUCT.md in an HTML comment at the top of each template | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include these H2 sections: Summary, Motivation, Proposed Solution, Alternatives Considered, Out of Scope, Additional Context | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include these H2 sections: Summary, Steps to Reproduce, Expected Behavior, Actual Behavior, Environment, Logs (collapsible), Additional Context | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include these PR sections with exact H2 headings: Summary, Changes, Motivation, Testing, Security and Privacy, Breaking Changes, Docs, Linked Issues, Checklist | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include these checklist items exactly once each: tests added/updated; docs updated; security review requested if sensitive; breaking changes called out; self-review completed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep all guidance text inside HTML comments so rendered output stays clean | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep prompts short and specific; avoid paragraphs; prefer bullets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the PR template under 200 non-blank lines and 10 KB; keep each issue template under 250 non-blank lines and 10 KB | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place a single PR template at .github/PULL_REQUEST_TEMPLATE.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place fields most reviewers care about first: Summary, Changes, Motivation, then Testing | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer multiple smaller PRs over one large PR; include a checklist item acknowledging you split where reasonable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefix issue titles via front matter: “[Bug]” for bugs and “[Feature]” for features | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prominently instruct users not to include secrets, tokens, passwords, or personal data and to redact logs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide .github/ISSUE_TEMPLATE/config.yml with blank_issues_enabled: false and contact_links for security and support | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide at least bug_report.md and feature_request.md under .github/ISSUE_TEMPLATE/ | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put the “## Checklist” section at the end of the PR template | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start each template with a short HTML comment explaining how to use it | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Under “Logs,” use a collapsible <details> block and instruct to redact sensitive data | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use H2 headings (##) for all section headers across templates | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use HTML comments for guidance/examples; avoid visible placeholder text | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use Markdown Issue Templates, not YAML Issue Forms | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use consistent, exact section titles across repos to keep automation stable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use imperative prompts (“Describe X.”, “List Y.”), not questions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| `(contested)` **Do** use `labels` and `assignees` in issue template frontmatter for auto-triage | Structure and Content |  |  |  |  | ✓ |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

