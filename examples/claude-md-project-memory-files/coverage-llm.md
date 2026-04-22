## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Use clear Markdown headings and bullet lists for structure. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Write rules as imperatives, not preferences or aspirations. | Style | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Keep the file short/under a line cap to preserve signal and context. | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Link to source-of-truth docs/files instead of duplicating content. | Maintainability | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Review and update the memory file alongside related code changes. | Maintainability | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Never commit secrets, tokens, or sensitive data in the file. | Safety | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Document project-specific security/safety conventions explicitly. | Safety | ✓ | ✓ |  | ✓ | ✓ | ✓ | 5 |
| Assign a clear owner (e.g., CODEOWNERS) for the file. | Maintainability | ✓ |  | ✓ |  | ✓ |  | 3 |
| Enumerate "do not edit" files/directories (generated code, vendored deps, migrations). | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Require human approval before high-risk/destructive actions (migrations, deps, prod). | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Provide canonical/exact commands for setup, test, lint, build, run. | Content | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Include a last-updated date or version stamp. | Maintainability | ✓ | ✓ |  | ✓ |  | ✓ | 4 |
| State architectural invariants and constraints the type system can't enforce. | Content | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Place the file at the repository root. | Structure | ✓ |  |  | ✓ | ✓ |  | 3 |
| Use a fixed/predictable section order and group related rules thematically. | Structure | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Begin with a brief project overview/TL;DR/preamble. | Structure | ✓ | ✓ | ✓ | ✓ |  |  | 4 |
| Document toolchain/language/package-manager versions and assumptions. | Content | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use repo-relative paths and backtick identifiers for unambiguous references. | Style | ✓ |  | ✓ |  | ✓ |  | 3 |
| Don't document the obvious or duplicate linter/formatter/type-checker rules. | Content |  |  | ✓ | ✓ | ✓ |  | 3 |
| Describe ground truth, not aspirations; ensure rules match enforced reality. | Correctness |  |  | ✓ | ✓ | ✓ |  | 3 |
| Provide a CI or automated check to validate commands/links/examples. | Maintainability | ✓ |  |  | ✓ |  |  | 2 |
| Document deprecated patterns and forbid them in new code. | Content |  |  | ✓ | ✓ |  | ✓ | 3 |
| Define a "Definition of Done" (tests pass, lint clean, docs updated). | Correctness | ✓ |  |  |  |  |  | 1 |
| Declare SLOs/performance budgets and identify hot paths. | Performance | ✓ |  |  | ✓ |  |  | 2 |
| Specify testing framework, patterns, and coverage expectations. | Testing | ✓ |  |  | ✓ |  |  | 2 |
| State error-handling policy (retries, fail-fast, error shape). | Error Handling | ✓ |  |  | ✓ |  | ✓ | 3 |
| Include a glossary of project-specific terminology. | Content |  |  |  |  | ✓ | ✓ | 2 |
| Specify commit/PR/branch conventions. | Content | ✓ |  | ✓ |  |  |  | 2 |
| Provide short inline rationales for each rule. | Style |  |  |  | ✓ | ✓ | ✓ | 3 |
| Include rollback/migration/incident-recovery procedures and contacts. | Safety | ✓ |  |  |  |  |  | 1 |
| Pair ✓/✗ examples or anti-examples to illustrate rules. | Style |  |  |  | ✓ |  |  | 1 |
| Prefer vendor-neutral AGENTS.md naming (with CLAUDE.md as alias). | Structure | ✓ |  | ✓ |  | ✓ |  | 3 |
| Include machine-readable frontmatter/metadata for tools. | Automation | ✓ |  |  |  |  |  | 1 |
| Support nested CLAUDE.md files in subdirectories for domain-specific rules. | Structure |  |  | ✓ |  |  |  | 1 |
| Keep examples short, minimal, and executable. | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| List files/actions the AI must not modify or perform without approval. | Safety |  |  | ✓ | ✓ | ✓ |  | 3 |
| List required environment variables and their handling. | Content | ✓ |  |  | ✓ |  |  | 2 |
| Solicit team feedback on the documentation to surface issues. | Maintainability |  | ✓ |  |  |  |  | 1 |
| Declare explicit non-goals or out-of-scope items. | Content | ✓ |  |  |  |  |  | 1 |
| Specify logging conventions and what must never be logged. | Error Handling | ✓ |  |  | ✓ |  |  | 2 |
| Avoid deep heading nesting (≤2–3 levels). | Structure | ✓ |  | ✓ | ✓ |  |  | 3 |
| Include a table of contents for long files. | Structure |  |  |  | ✓ |  | ✓ | 2 |
| One rule per bullet/sentence; avoid compound rules. | Style |  |  | ✓ | ✓ |  |  | 2 |
| Use consistent terminology across sections. | Style | ✓ |  |  | ✓ |  |  | 2 |
| Avoid decorative elements (emoji, images, screenshots). | Style | ✓ |  | ✓ |  |  | ✓ | 3 |
| Define naming conventions for files, folders, and identifiers. | Style |  |  |  | ✓ |  |  | 1 |
| Define a repo map highlighting key paths. | Structure | ✓ |  |  | ✓ |  | ✓ | 3 |
| Validate that code examples/snippets in the file actually run. | Correctness |  |  |  | ✓ |  |  | 1 |
| Use plain language and define jargon on first use. | Readability |  | ✓ |  | ✓ |  | ✓ | 3 |
| Include an architectural decision log or link to ADRs. | Content | ✓ |  |  |  |  |  | 1 |
| Prefer positive phrasing over negative-only prohibitions. | Style |  |  | ✓ |  |  |  | 1 |

## Notes on clustering decisions

- **"Keep the file short"** merged hard line caps (200/300/2,000 lines) and general brevity advice into one cluster; the specific caps differ substantially (Haiku's 2,000 is ~10× others') but the intent is the same.
- **"Link to source of truth"** clusters a range of related rules: linking to ADRs (gpt-5, grok), linking to config files (opus, haiku, gemini), and avoiding duplication generally. A stricter reading could split "link to ADRs" from "link to configs."
- **"Write rules as imperatives"** groups opus's "imperative not hedged," haiku's "active imperative voice," gemini's "direct imperative sentences," grok's "do/don't" format, and gpt-4o-mini's similar guidance. Different wording, same substance.
- **"Use Markdown headings/bullets"** bundles separate rules some models stated as two or three bullets (headings, bullets, code fences). A more granular matrix would split these.
- **"State ground truth, not aspirations"** (opus, haiku, gemini) could arguably merge with **"Describe what is enforced"** — I kept them as one cluster since all three models frame it the same way.
- **"Provide canonical commands"** merges rules ranging from "exact test/lint/build commands" (opus, haiku) to "canonical verbs for setup/run/test/..." (gpt-5) to "limit to 1–3 critical commands" (gemini). Gemini's is arguably the inverse, but all agree commands should appear and be exact.
- **"Assign an owner"** and **"Review in PRs"** were kept separate because some models raise one without the other (gpt-4o-mini mentions review but not ownership).
- **"Avoid decorative elements"** merges gpt-5's "no screenshots/images," opus's "no emoji/decoration," and grok's "no images/non-MD elements."
- **"AI guardrails / don't modify X"** (opus, haiku, gemini) overlaps with **"Enumerate do-not-edit files"** (gpt-5, opus, haiku). I kept them as two clusters because the first is about AI-behavioral constraints broadly and the second about specific generated/vendored directories — but a looser matcher would collapse them.
- **"Short rationales inline"** (haiku, gemini, grok) is distinct from "link to ADRs for full rationale" (gpt-5); both appear as separate clusters.
- Haiku's extensive domain-specific sections (Testing, Naming, Type Safety, Performance/Scalability) were mostly matched only where another model raised a comparable rule; the many unique rules in that response appear as count-1 entries or are omitted for brevity.