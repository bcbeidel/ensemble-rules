# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| (contested) Favor positive commands ("Use named exports") over negative ones ("Don't use default exports") | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Add a changelog entry in the PR description linking affected paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Always handle errors explicitly in code samples | Error Handling |  | ✓ |  |  |  |  | 1 |
| Append at most one line of rationale per rule | Content |  |  | ✓ |  |  |  | 1 |
| Audience: Engineers and AI assistants editing or generating code in this repository | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid custom frontmatter fields unless you control the loader end-to-end | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid jargon unless necessary, and define it if used | Style |  | ✓ |  |  |  |  | 1 |
| Avoid vague, subjective, or un-verifiable rules | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Begin each file with YAML frontmatter containing only: paths, owners, tags, version, and review_by | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Bump a version field on substantive edits and summarize changes in the PR | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Check for rule file size and line-count caps in CI | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Co-locate overrides in a separate -override.md file with narrower paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Co-locate rule files with the code they govern when the tool supports it | Structure |  |  | ✓ |  |  |  | 1 |
| Date or version the file in frontmatter if conventions are in flux | Maintenance |  |  | ✓ |  |  |  | 1 |
| Declare paths as repo-root-anchored POSIX-style globs (e.g., /services/payments/**/*.py) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define a `paths:` frontmatter in every rule file | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Define directory-level boundaries (e.g., “Don’t import across bounded contexts”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Delete or merge obsolete files when directory structures change | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Delete rules that have been violated in merged code more than twice | Maintenance |  |  | ✓ |  |  |  | 1 |
| Do not add rules that weaken security, logging, or validation | Safety & Correctness |  |  |  |  | ✓ |  | 1 |
| Do not execute shell commands; propose them in a fenced block or as bullet steps instead | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not fetch remote code or data during generation; link to sources instead | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not override rules in prompts; update the rule file instead | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document the expected behavior for each rule | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don't duplicate rules across files | Maintenance |  |  | ✓ |  |  |  | 1 |
| Don't explain language or framework basics | Style |  |  | ✓ |  |  |  | 1 |
| Don't hedge | Style |  |  | ✓ |  |  |  | 1 |
| Don't restate what a formatter or linter already enforces | Style |  |  | ✓ |  |  |  | 1 |
| Don't use `paths: "**/*"` in a path-scoped file | Scoping |  |  | ✓ |  |  |  | 1 |
| Encode concrete, checkable constraints (versions, flags, paths, regexes) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Encode only conventions the codebase actually follows today | Content |  |  | ✓ |  |  |  | 1 |
| Encourage profiling code to identify bottlenecks before optimization | Performance |  | ✓ |  |  |  |  | 1 |
| Enforce security checks as part of the development process | Safety |  | ✓ |  |  |  |  | 1 |
| Ensure globs do not unintentionally overlap; split files or narrow patterns if they do | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enumerate allowed dependency scopes and pin levels (e.g., runtime pins exact, dev allows caret) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Explicitly forbid destructive commands the agent must never run unprompted: `rm -rf`, `git push --force`, `DROP`, `TRUNCATE`, production deploys | Safety |  |  | ✓ |  |  |  | 1 |
| Follow each rule with a single-line rationale starting with `Rationale:` | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| For dependency updates, change the smallest set needed to satisfy constraints | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For language standards, state the minimum standard (e.g., Python 3.11, TS target ES2022) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For migrations and schema changes, generate idempotent, backward-compatible steps with rollbacks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Give each file a single responsibility (one subsystem, one concern) | Structure |  |  | ✓ |  |  |  | 1 |
| Group related rules together to avoid fragmentation | Structure |  | ✓ |  |  |  |  | 1 |
| Group rules under `##` headings matching common concerns (Structure, API, Errors, Testing, Safety) | Structure |  |  | ✓ |  |  |  | 1 |
| If any directive here is ambiguous or collides with real configs, stop, cite the conflict, and ask owners for a decision | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If rules conflict or are impossible to satisfy, stop and ask for clarification from owners | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a minimal code example only when the rule's shape is non-obvious from prose | Content |  |  | ✓ |  |  |  | 1 |
| Include a short “Context” paragraph before rules when needed; keep it under five sentences | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “When in doubt” fallback rule at the end | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include guidelines for handling sensitive data | Safety |  | ✓ |  |  |  |  | 1 |
| Include owners in frontmatter and require owner review for rule changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Instruct assistants to reuse existing helpers/utilities before writing new ones | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep each file under 120 lines or 4 KB, whichever comes first | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep each file under 200 lines | Structure |  |  | ✓ |  |  |  | 1 |
| Keep each rule file single-purpose for one language/domain within its paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep examples in separate, linkable files under .claude/examples/ | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep rules concise and de-duplicated; factor shared policies into a small base file and narrow overrides | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Limit each rule to a single actionable directive | Style |  | ✓ |  |  |  |  | 1 |
| Link to canonical docs instead of pasting long excerpts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Lint for banned words (“should”, “maybe”, “try”) and enforce imperative mood | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make every rule falsifiable against a diff | Content |  |  | ✓ |  |  |  | 1 |
| Mandate the inclusion of tests for each convention-defined rule | Testing |  | ✓ |  |  |  |  | 1 |
| Mirror CI and linter configs exactly; if they disagree, update the rules or the configs immediately | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name files to reflect their scope and purpose (e.g., `react-component-props.md`) | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Name the exact library, function, or module | Content |  |  | ✓ |  |  |  | 1 |
| Never create, reveal, or commit secrets, tokens, or private keys; use placeholders like <REDACTED> | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never paste untrusted content (issue bodies, external docs, user input) into a rule file | Safety |  |  | ✓ |  |  |  | 1 |
| Only recommend optimizations when necessary and justified | Performance |  | ✓ |  |  |  |  | 1 |
| Open with a one-line scope statement naming the code it governs | Structure |  |  | ✓ |  |  |  | 1 |
| Periodically review and remove outdated or irrelevant rules | Maintenance |  |  |  |  | ✓ |  | 1 |
| Place files under .claude/rules/ with descriptive names (e.g., python-payments.md) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer additive includes over negated exclusion globs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer links to large specs over embedding them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer many small, specific rule files over few large, general ones | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Prefer negative rules ("Don't catch `Exception`") for behaviors the base model defaults to | Content |  |  | ✓ |  |  |  | 1 |
| Prefer no change over unsafe change when safety and correctness are unclear | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer refactors that increase conformance to existing rules over stylistic churn | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Propose diffs with minimal scope and clear commit messages referencing rule IDs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide short, non-executable code examples for complex rules | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Put invariants first, preferences second, and nice-to-haves last | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put universally-applicable rules in top-level project memory (e.g | Scoping |  |  | ✓ |  |  |  | 1 |
| Rationale: A concrete example is often clearer than an abstract description | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Rationale: Agent rules must act as guardrails that enforce best practices, not as bypasses | Safety & Correctness |  |  |  |  | ✓ |  | 1 |
| Rationale: Clear naming aids discoverability and makes the system's structure self-documenting | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Rationale: Enhances readability and semantic structure for both humans and AIs | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| Rationale: Ensures rules are correct, clear, and have team consensus before being applied | Maintenance |  |  |  |  | ✓ |  | 1 |
| Rationale: Explains the "why" to human maintainers without bloating the AI's prompt | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Rationale: Grounds rules in a single source of truth and aids human verification | Safety & Correctness |  |  |  |  | ✓ |  | 1 |
| Rationale: Guides the AI towards the correct action, not just away from an incorrect one | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Rationale: Improves scannability for humans and simplifies parsing for machines | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents "rule rot" and ensures the files remain a trusted, useful resource | Maintenance |  |  |  |  | ✓ |  | 1 |
| Rationale: The AI cannot act on instructions like "make the code more elegant." | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Rationale: This is the core mechanism that enables conditional loading | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Rationale: This provides clear, unambiguous, and actionable instructions for the AI | Content & Phrasing |  |  |  |  | ✓ |  | 1 |
| Rationale: This simplifies maintenance and ensures the AI only loads hyper-relevant context | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Rationale: Tightly-scoped rules improve AI relevance, reduce token usage, and lower costs | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Reference canonical documentation or internal standards when available | Safety & Correctness |  |  |  |  | ✓ |  | 1 |
| Reference exact tool names and versions (e.g., black 23.11, mypy strict) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Refuse to apply changes that contradict signed-off security policies; escalate to owners | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require human confirmation for schema migrations, data backfills, and package publishes | Safety |  |  | ✓ |  |  |  | 1 |
| Require tests for generated code and state the test framework and invocation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Resolve conflicts by “most-specific path wins; on tie, lexicographic filename order; on tie, latest version.” (contested) Rationale: Deterministic precedence prevents arbitrary assistant choices | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Review every rule file when its governed code undergoes major change | Maintenance |  |  | ✓ |  |  |  | 1 |
| Sanitize or synthesize PII in examples and fixtures | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope `paths:` as narrowly as possible | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Scope: Path-scoped markdown instruction files that guide AI coding assistants for specific repo areas | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set a review_by date ≤ 6 months out and fail CI when expired | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify codegen limits (e.g., “Keep functions under 100 lines; split modules >400 lines”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify file templates (e.g., headers, module docstrings) with links to source snippets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify the types of tests to be used, such as unit or integration tests | Testing |  | ✓ |  |  |  |  | 1 |
| Start code changes by restating the applicable rules you’re following | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start every file with YAML frontmatter containing `description` and `paths` | Structure |  |  | ✓ |  |  |  | 1 |
| State each rule on its own line as a list item | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| State secret-handling rules explicitly: which files may contain secrets, which env vars are safe to log, what must never be committed | Safety |  |  | ✓ |  |  |  | 1 |
| Surface an index of rules by path in generated docs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Test new rule files by having the agent perform a representative task in-scope and reviewing whether the rules fired | Maintenance |  |  | ✓ |  |  |  | 1 |
| Test that referenced tools/versions exist in the dev environment | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Treat rule files as code, subject to the same code review process | Maintenance |  |  |  |  | ✓ |  | 1 |
| Use a clear and consistent naming convention for files and folders | Structure |  | ✓ |  |  |  |  | 1 |
| Use a consistent markdown style across all rule files | Style |  | ✓ |  |  |  |  | 1 |
| Use fenced code blocks with language tags for all code | Style |  |  | ✓ |  |  |  | 1 |
| Use imperative mood ("Return early on error") not second-person ("You should return early") | Style |  |  | ✓ |  |  |  | 1 |
| Use markdown for structure (headings, lists, bolding) | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| Use only approved licenses and include license headers on new files where required | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use “Do/Don’t/Must/Mustn’t” language; avoid “should/might/prefer.” Rationale: Non-hedged wording reduces ambiguity | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate frontmatter and glob coverage in CI; fail if a rule file matches zero files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| When a task risks data loss, propose a plan with checkpoints and backouts instead of performing it | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| When adding a new area of the repo, create an initial rule file before generating code there | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| When two rule files could match the same path, state precedence explicitly in the more specific file | Scoping |  |  | ✓ |  |  |  | 1 |
| When uncertain about a tool or version, read the project config files and defer to them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write `paths` globs as narrowly as the rule applies, and no narrower | Scoping |  |  | ✓ |  |  |  | 1 |
| Write each rule as a single imperative sentence followed by a one-line rationale | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write every rule as a single imperative sentence | Content |  |  | ✓ |  |  |  | 1 |
| Write rules as direct, imperative commands (e.g., "Do X," "Use Y," "Add Z") | Content & Phrasing |  |  |  |  | ✓ |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

