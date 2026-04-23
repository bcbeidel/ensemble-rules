# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Prefer concise descriptions over large code snippets.** | Content and Style |  |  |  |  | ✓ |  | 1 |
| **Assign a file owner or team in a "Metadata" section.** | Safety and Maintenance |  |  |  |  | ✓ |  | 1 |
| **Call out any non-obvious boundaries (e.g., "`packages/core` must not import from `packages/web`").** Import rules are invisible to a reader of the tree | Architecture |  |  | ✓ |  |  |  | 1 |
| **Defer style and formatting rules to the linter/formatter config; name the tool and config file.** The config is the source of truth; the prose will drift | Conventions |  |  | ✓ |  |  |  | 1 |
| **Define project-specific terminology and acronyms.** | Content and Style |  |  |  |  | ✓ |  | 1 |
| **Delete any claim you cannot point to a file or command to verify.** Unverifiable content is noise at best, misleading at worst | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Do not duplicate commands already trivially discoverable in `package.json` scripts or a `Makefile`; reference them instead.** Duplication guarantees drift | Commands |  |  | ✓ |  |  |  | 1 |
| **Do not embed large code examples.** The assistant can read the file; link to it by path | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Do not explain generic patterns (MVC, clean architecture) by name without pointing to the concrete files that embody them.** Names without referents are decorative | Architecture |  |  | ✓ |  |  |  | 1 |
| **Do not include a table of contents.** At this length it's noise | Structure |  |  | ✓ |  |  |  | 1 |
| **Do not include dated roadmap items, migration plans, or "we're moving to X" statements.** These are never deleted when completed | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Do not include onboarding prose aimed at humans (team rituals, hiring context, history).** Wrong audience | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Do not include prohibitions the assistant already infers (e.g., "don't commit secrets") | Do Not |  |  | ✓ |  |  |  | 1 |
| **Do not include secrets, keys, or any other sensitive credentials.** | Safety and Maintenance |  |  |  |  | ✓ |  | 1 |
| **Document which commands are destructive and require confirmation (e.g., `db:reset`, `deploy:prod`).** The assistant cannot tell from the name alone | Safety |  |  | ✓ |  |  |  | 1 |
| **Explain the "why" behind a convention, not just the "what".** | Content and Style |  |  |  |  | ✓ |  | 1 |
| **Group content under fixed top-level headings: Overview, Commands, Architecture, Conventions, Do Not.** Predictable structure is faster to parse and easier to diff | Structure |  |  | ✓ |  |  |  | 1 |
| **Group related file paths under a common heading.** | Structure and Size |  |  |  |  | ✓ |  | 1 |
| **Highlight security-critical areas and preferred secure patterns.** | Safety and Maintenance |  |  |  |  | ✓ |  | 1 |
| **Include commands for running a single test, not just the full suite.** Targeted reruns are the common case during iteration | Commands |  |  | ✓ |  |  |  | 1 |
| **Keep the file under 200 lines.** Every line loads on every session; context is scarce | Structure |  |  | ✓ |  |  |  | 1 |
| **Limit the file size to a maximum of 32KB.** | Structure and Size |  |  |  |  | ✓ |  | 1 |
| **Link to sources of truth; do not duplicate their content.** | Content and Style |  |  |  |  | ✓ |  | 1 |
| **List explicit prohibitions as imperative negatives ("Do not run `prisma migrate` against production").** Prohibitions are the highest-value lines in the file | Do Not |  |  | ✓ |  |  |  | 1 |
| **List the exact commands for build, test, lint, typecheck, and run — one per line in a code block.** These are the assistant's most frequent lookups | Commands |  |  | ✓ |  |  |  | 1 |
| **Name branches, environments, or files that are off-limits for modification.** Eliminates a class of destructive mistakes | Do Not |  |  | ✓ |  |  |  | 1 |
| **Name the files or paths that are generated, vendored, or otherwise not hand-editable.** Prevents silent corruption of build outputs | Safety |  |  | ✓ |  |  |  | 1 |
| **Name the top-level directories and what lives in each, in two lines or fewer per directory.** Gives the assistant a map without it grepping blindly | Architecture |  |  | ✓ |  |  |  | 1 |
| **Open with a one-paragraph project summary naming what the repo is and its primary language/framework.** Orients the assistant before it reads anything else | Structure |  |  | ✓ |  |  |  | 1 |
| **Place the `AGENTS.md` file in the repository root.** | Naming and Location |  |  |  |  | ✓ |  | 1 |
| **Place the file at the repository root as `CLAUDE.md`.** Assistants look there first; nested memory files are for subprojects only | Structure |  |  | ✓ |  |  |  | 1 |
| **Review `CLAUDE.md` in any PR that changes commands, directory layout, or dependencies.** Drift is the default; review is the fix | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Review and update the file as part of the pull request process for major features.** | Safety and Maintenance |  |  |  |  | ✓ |  | 1 |
| **Specify the package manager explicitly (`pnpm`, not "your package manager").** Mixed package managers corrupt lockfiles | Commands |  |  | ✓ |  |  |  | 1 |
| **Specify the test framework and the file-naming pattern for tests.** Disambiguates `*.test.ts` vs | Conventions |  |  | ✓ |  |  |  | 1 |
| **State conventions only when they're enforced in this repo and deviate from ecosystem defaults.** The assistant already knows standard idioms | Conventions |  |  | ✓ |  |  |  | 1 |
| **State where generated code lives and that it must not be edited by hand.** Prevents the single most common destructive edit | Architecture |  |  | ✓ |  |  |  | 1 |
| **Symlink `AGENTS.md` to `CLAUDE.md` (or vice versa).** Keeps one source of truth across tools | Structure |  |  | ✓ |  |  |  | 1 |
| **Use Markdown with hierarchical headings (##, ###).** | Structure and Size |  |  |  |  | ✓ |  | 1 |
| **Use repository-relative paths for all internal links and file references.** | Content and Style |  |  |  |  | ✓ |  | 1 |
| **Use the filename `AGENTS.md`.** | Naming and Location |  |  |  |  | ✓ |  | 1 |
| Add CODEOWNERS coverage for CLAUDE.md/AGENTS.md to require review by a responsible team | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add a “Last updated: YYYY-MM-DD” line near the top | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers, maintainers, and technical writers responsible for repository ergonomics | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid HTML comments and nonstandard metadata blocks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid images, diagrams, and raw HTML in this file; link to assets instead | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Begin content with an H1 heading naming the repo and “Project Memory.” Stable anchors help assistants | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare required environment variables without values and show safe placeholders for usage | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do adhere to a consistent Markdown syntax throughout the file | Style |  | ✓ |  |  |  |  | 1 |
| Do avoid unnecessary verbosity by omitting examples unless they clarify a rule | Performance |  |  |  |  |  | ✓ | 1 |
| Do document security best practices relevant to the project | Safety |  | ✓ |  |  |  |  | 1 |
| Do enforce consistent Markdown formatting, such as using `#` for headings and `-` for bullets | Style |  |  |  |  |  | ✓ | 1 |
| Do explicitly state security best practices, like "Always validate inputs before processing." | Safety |  |  |  |  |  | ✓ | 1 |
| Do highlight any performance-related conventions or metrics | Performance |  | ✓ |  |  |  |  | 1 |
| Do include a table of contents at the beginning of the file | Structure |  | ✓ |  |  |  |  | 1 |
| Do include a version number or date at the top to track updates | Structure |  |  |  |  |  | ✓ | 1 |
| Do limit each section to bullet points or numbered lists for key information | Content Guidelines |  |  |  |  |  | ✓ | 1 |
| Do not include secrets, tokens, credentials, private endpoints, or production URLs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize the file into clearly defined sections | Structure |  | ✓ |  |  |  |  | 1 |
| Do require regular reviews of the file during project milestones | Maintainability |  |  |  |  |  | ✓ | 1 |
| Do specify error handling guidelines for critical operations | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do use a hierarchical structure with headings and subheadings for sections like "Conventions," "Decisions," and "File Locations" to organize content logically | Structure |  |  |  |  |  | ✓ | 1 |
| Do write all instructions in clear, imperative language using active voice | Content Guidelines |  |  |  |  |  | ✓ | 1 |
| Document data classification and PII-handling expectations with links to policy | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't allow unchecked additions; require peer review for updates | Maintainability |  |  |  |  |  | ✓ | 1 |
| Don't exceed 500 lines in the file to keep it concise and load quickly | Structure |  |  |  |  |  | ✓ | 1 |
| Don't include code snippets longer than 5 lines without linking to the actual file | Style |  |  |  |  |  | ✓ | 1 |
| Don't include dynamic content like scripts or external references | Performance |  |  |  |  |  | ✓ | 1 |
| Don't overlook the importance of code reviews in the context of security | Safety |  | ✓ |  |  |  |  | 1 |
| Don't recommend experimental or deprecated tools without warnings | Safety |  |  |  |  |  | ✓ | 1 |
| Don't use jargon or overly complex language | Style |  | ✓ |  |  |  |  | 1 |
| Don't use undefined jargon or acronyms without immediate explanation | Content Guidelines |  |  |  |  |  | ✓ | 1 |
| Engineers and AI coding assistants reviewing or authoring CLAUDE.md files | Section 2: Rules File |  |  |  | ✓ |  |  | 1 |
| Enumerate naming, branching, and code-style conventions with links to authoritative docs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a bold warning not to paste secrets or production data into prompts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include known pitfalls and sharp edges with workarounds | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep all intra-repo paths relative to the repo root | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep headings and section names stable across revisions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the file under 50 KB and under 1,200 lines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Land changes via PRs reviewed by owners | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Link to SECURITY.md and describe where secrets live (e.g., vault paths) without values | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Link to an ADR index or list top architectural decisions with links | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| List exact setup, build, test, and run commands as copy-pastable code blocks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Maintain a reverse-chronological Changelog section with YYYY-MM-DD bullets for major changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mark deprecated guidance with “Deprecated:” and link to replacements | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mark unknowns explicitly with “Unknown as of YYYY-MM-DD.” Explicit unknowns avert guesswork | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Move volatile details (version pins, rotating endpoints) behind single-source-of-truth links | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name owners with emails or GitHub handles and provide escalation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place a single CLAUDE.md or AGENTS.md at the repository root; do not use both | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer links to large documents, logs, and ADRs instead of inlining | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer relative links for intra-repo references; reserve absolute links for external resources | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide H2 sections in this exact order: Overview; Goals and Non-Goals; How to Work Here; Repository Layout; Conventions; Build and Run; Testing; Architecture and Decisions; Safety and Secrets; Tooling and AI; CI/CD; Performance; Troubleshooting and Pitfalls; Ownership and Contacts; Glossary; Changelog | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put a one-sentence Summary under the H1 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Rules for authoring and maintaining a single top-level CLAUDE.md (or AGENTS.md) project-memory file that AI assistants load automatically | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Show key repository paths and their purposes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start the file with an optional YAML front matter block containing type: project-memory, schema: 1, audience: ai+human, and last_updated: YYYY-MM-DD | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State forbidden actions for assistants (e.g., never run destructive commands without confirmation) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State supported languages, frameworks, and runtime versions explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Teams establishing repository conventions and governance | Section 2: Rules File |  |  |  | ✓ |  |  | 1 |
| Update the last_updated/front matter date on substantive changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use fenced code blocks labeled bash, sh, pwsh, json, yaml, or ini only | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use inline links; avoid reference-style link definitions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use placeholders in ALL_CAPS or <angle-brackets>; never include real values | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use plain GitHub-Flavored Markdown; avoid custom directives and footnotes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| When guidance conflicts with code, state “Code is authoritative” and link to the source; open an issue to reconcile | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Wrap lines at 100 characters | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write in concise bullets and imperative sentences; avoid walls of text | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

