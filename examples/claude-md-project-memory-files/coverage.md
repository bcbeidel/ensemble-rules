# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested)** Link to pull requests or commits that exemplify the rule (e.g., "See PR #1234 for a well-structured service class") | Examples and Anti-Examples |  |  |  | ✓ |  |  | 1 |
| **Aggressively prune low-value or outdated information.** (contested) | **Maintenance** |  |  |  |  | ✓ |  | 1 |
| **Appoint an owner or group responsible for the file's accuracy.** | **Maintenance** |  |  |  |  | ✓ |  | 1 |
| **Assign a single owner (CODEOWNERS entry) for the file.** Shared ownership means no ownership | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Audit the file quarterly and on major version bumps.** Scheduled review catches drift that PR review misses | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Avoid example code blocks longer than 10 lines.** (contested) Short examples clarify; long ones bloat context and go stale | Style |  |  | ✓ |  |  |  | 1 |
| **Avoid jargon specific to one person's mental model.** If the team uses terms like "thin client" or "the event loop," define them on first use | Clarity and Tone |  |  |  | ✓ |  |  | 1 |
| **Call out any SQL, shell, or template injection risks specific to the project's architecture.** | Safety and Security |  |  |  | ✓ |  |  | 1 |
| **Call out any mocking or stubbing conventions** (e.g., "Mock external APIs using msw or nock; do not hardcode mock responses in test files") | Testing |  |  |  | ✓ |  |  | 1 |
| **Call out high-leverage architectural decisions** (e.g., how state is managed, how the system handles concurrency, multi-tenancy approach) even if they seem obvious to current team members | Content and Specificity |  |  |  | ✓ |  |  | 1 |
| **Call out performance-critical paths and their constraints** (e.g., "Initial page load must complete in <3s; the recommendation engine must respond in <500ms") | Performance and Scalability |  |  |  | ✓ |  |  | 1 |
| **Co-locate subdirectory `CLAUDE.md` files for domain-specific rules.** (contested) Keeps root lean; not all tools support nested loading | Structure |  |  | ✓ |  |  |  | 1 |
| **Cross-check with actual code in the repository.** If CLAUDE.md forbids a pattern but that pattern exists in core files, flag it during review and either update the rule or refactor the code | Correctness |  |  |  | ✓ |  |  | 1 |
| **Date or version CLAUDE.md updates** in a footer comment so reviewers know how fresh the guidance is | Structure |  |  |  | ✓ |  |  | 1 |
| **Date or version major architectural claims when they're likely to change.** Lets future readers detect stale assumptions | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Define any review or approval gates** (e.g., "Security-sensitive changes require manual review before merge; database schema changes require approval from @db-team") | AI Constraints and Guardrails |  |  |  | ✓ |  |  | 1 |
| **Define limits on data fetching** (e.g., "Pagination defaults to 20 items per page; API calls are cached for 5 minutes; never fetch more than 1000 records at once") | Performance and Scalability |  |  |  | ✓ |  |  | 1 |
| **Define project-specific terminology and acronyms.** | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| **Define the minimum test coverage threshold** if one is enforced (e.g., "80% line coverage for src/ directory, 50% for scripts/") | Testing |  |  |  | ✓ |  |  | 1 |
| **Define the process for handling secrets and environment variables** (e.g., "All secrets go in .env.local; never commit them; use process.env to access") | Safety and Security |  |  |  | ✓ |  |  | 1 |
| **Define the rule for null vs | Type Safety and Language Features |  |  |  | ✓ |  |  | 1 |
| **Define variable and function naming conventions** (e.g., "Use camelCase for variables and functions; use UPPER_SNAKE_CASE for constants; prefix private methods with _") | Naming and Conventions |  |  |  | ✓ |  |  | 1 |
| **Define what "good" looks like concretely**: "Function signatures should fit on one 80-char line; if they exceed it, use object destructuring." beats "Keep function signatures short." | Content and Specificity |  |  |  | ✓ |  |  | 1 |
| **Delete rules that aren't actually enforced.** Aspirational rules train models to produce code inconsistent with the codebase | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Describe the architecture in 5–10 bullets, not paragraphs.** Bullets survive skimming; paragraphs get truncated mentally | Content |  |  | ✓ |  |  |  | 1 |
| **Do not document aspiration; document ground truth.** If you want all functions to have JSDoc comments but your CI doesn't enforce it, either enforce it or don't list it as a rule | Correctness |  |  |  | ✓ |  |  | 1 |
| **Do not document or encourage bypassing security mechanisms.** | **Safety** |  |  |  |  | ✓ |  | 1 |
| **Do not include long code snippets.** | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| **Document non-obvious invariants (e.g., "all API routes must call `requireAuth()`").** These are the rules the type system can't enforce | Content |  |  | ✓ |  |  |  | 1 |
| **Document only what a competent engineer would get wrong by default.** Obvious things waste context; non-obvious things prevent bugs | Content |  |  | ✓ |  |  |  | 1 |
| **Don't document the obvious ("this is a TypeScript project").** The model can see `tsconfig.json` | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Don't include marketing language, mission statements, or team values.** Zero behavioral impact; pure context-window tax | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Don't paste the README into CLAUDE.md.** READMEs target new humans; CLAUDE.md targets agents mid-task | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Don't restate what the linter, formatter, or type-checker already enforces.** Tooling is the source of truth for mechanical rules | Style |  |  | ✓ |  |  |  | 1 |
| **Don't use emoji or decorative formatting to signal importance.** Position and imperative phrasing do the work; decoration adds tokens | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Don't write rules in the negative only ("don't use var").** Pair prohibitions with the positive alternative | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Enclose all file paths, function names, and identifiers in backticks (`).** | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| **Ensure rules are consistent with linter, formatter, and type-checker configs.** If `.eslintrc.json` says `semi: false` but CLAUDE.md says "always add semicolons," update CLAUDE.md or the linter | Correctness |  |  |  | ✓ |  |  | 1 |
| **Enumerate files and directories that must never be edited without explicit approval.** Generated code, vendored deps, and migrations are common footguns | Safety |  |  | ✓ |  |  |  | 1 |
| **Explicitly state security-critical conventions.** | **Safety** |  |  |  |  | ✓ |  | 1 |
| **Focus on stable architectural patterns, not volatile implementation details.** | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| **Follow each rule with a one-line rationale in square brackets.** The rationale should explain *why* or *when*, not restate the rule | Clarity and Tone |  |  |  | ✓ |  |  | 1 |
| **Group content in this order: Overview → Commands → Architecture → Conventions → Gotchas → Do-Not-Touch.** Readers scan top-down; critical safety rules must precede stylistic ones | Structure |  |  | ✓ |  |  |  | 1 |
| **Group rules into 4–8 thematic sections** (e.g., Structure, Naming, Testing, Security, Performance, AI Constraints) | Structure |  |  |  | ✓ |  |  | 1 |
| **Identify the location of core authentication and authorization logic.** | **Safety** |  |  |  |  | ✓ |  | 1 |
| **Include a code example for any rule about style or structure.** Show both the preferred form and the anti-pattern (labeled ✓ and ✗) | Examples and Anti-Examples |  |  |  | ✓ |  |  | 1 |
| **Include a last-updated date** in ISO 8601 format (YYYY-MM-DD) | Footer |  |  |  | ✓ |  |  | 1 |
| **Include file-structure diagrams or trees** if the layout is non-standard or has been a source of confusion in code review | Content and Specificity |  |  |  | ✓ |  |  | 1 |
| **Include only rules specific to this project.** Generic advice ("write tests," "avoid null") belongs in team guidelines, not here | Content and Specificity |  |  |  | ✓ |  |  | 1 |
| **Include the exact test, lint, build, and run commands.** Agents routinely invent wrong commands when left to guess | Content |  |  | ✓ |  |  |  | 1 |
| **Keep CLAUDE.md under 2,000 lines.** Longer files are not read thoroughly; split architectural deep-dives into separate ADR or ARCHITECTURE.md documents and link to them | Structure |  |  |  | ✓ |  |  | 1 |
| **Keep examples short** (3–5 lines) | Examples and Anti-Examples |  |  |  | ✓ |  |  | 1 |
| **Keep the file under 200 lines.** | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| **Keep the file under 200 lines.** Every token is paid for on every request; brevity forces prioritization | Structure |  |  | ✓ |  |  |  | 1 |
| **Lead with a one-paragraph project summary.** The model needs to know what the repo *is* before it reads rules | Structure |  |  | ✓ |  |  |  | 1 |
| **Limit command examples to the 1-3 most critical setup/test commands.** (contested) | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| **Link to authoritative sources** (linter configs, package.json, CI definitions) rather than restating their rules in prose | Structure |  |  |  | ✓ |  |  | 1 |
| **Link to relevant documents** (architecture ADRs, style guide, security policy) in a "See Also" section | Footer |  |  |  | ✓ |  |  | 1 |
| **List TypeScript compiler options that are non-standard or disabled** (e.g., "strict: true is enabled; noImplicitAny is enforced; skipLibCheck is true for build speed") | Type Safety and Language Features |  |  |  | ✓ |  |  | 1 |
| **List any files or directories the AI must not create or modify** (e.g., "Do not modify .github/workflows/; do not create new migration files; ask for approval before editing schema.ts") | AI Constraints and Guardrails |  |  |  | ✓ |  |  | 1 |
| **List any files or patterns that AI must not modify** (e.g., "Do not edit migration files after they are merged to main," "Do not remove feature flags") | Safety and Security |  |  |  | ✓ |  |  | 1 |
| **List dependencies and frameworks with versions only when the major version matters.** Pinning in prose duplicates `package.json` and goes stale | Content |  |  | ✓ |  |  |  | 1 |
| **List known anti-patterns the team has explicitly rejected.** Prevents assistants from re-introducing solutions that were tried and failed | Content |  |  | ✓ |  |  |  | 1 |
| **Mark deprecated patterns clearly** (e.g., "Deprecated: class components | Content and Specificity |  |  |  | ✓ |  |  | 1 |
| **Name the package manager, Node/Python/etc | Content |  |  | ✓ |  |  |  | 1 |
| **Never commit secrets, internal hostnames, or customer data to CLAUDE.md.** The file is routinely shared, indexed, and pasted into prompts | Safety |  |  | ✓ |  |  |  | 1 |
| **Omit conversational filler, project history, and welcomes.** | **Style & Tone** |  |  |  |  | ✓ |  | 1 |
| **One rule per bullet; no compound rules joined by "and."** Compound rules get partially followed | Style |  |  | ✓ |  |  |  | 1 |
| **Open with a brief preamble** (2–3 sentences) stating the project name, primary language(s), and the file's purpose | Structure |  |  |  | ✓ |  |  | 1 |
| **Place CLAUDE.md at the repository root.** AI assistants load it by default; placing it elsewhere requires explicit configuration and reduces adoption | Structure |  |  |  | ✓ |  |  | 1 |
| **Prefer linking to source-of-truth files over restating their content.** `See tsconfig.json for compiler options` beats duplicating the config | Style |  |  | ✓ |  |  |  | 1 |
| **Prioritize pointers to the "source of truth" over duplicating content.** | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| **Provide a point of contact** or team for questions or updates (e.g., "@engineering-team") | Footer |  |  |  | ✓ |  |  | 1 |
| **Put commands in fenced code blocks with the exact invocation.** Copy-pasteable commands prevent guessing | Structure |  |  | ✓ |  |  |  | 1 |
| **Reference files by repo-relative path (`src/api/router.ts`), not by description.** Paths are unambiguous; descriptions drift | Structure |  |  | ✓ |  |  |  | 1 |
| **Require confirmation before adding new dependencies.** Silent dependency sprawl is a top source of supply-chain and bloat issues | Safety |  |  | ✓ |  |  |  | 1 |
| **Review CLAUDE.md during architectural changes.** When a major refactor occurs (e.g., migration from Redux to Context), update affected rules immediately; do not let rules describe obsolete patterns | Correctness |  |  |  | ✓ |  |  | 1 |
| **Review CLAUDE.md in every PR that changes the things it describes.** Staleness is the dominant failure mode; treat it as code | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Review `CLAUDE.md` changes as part of every relevant pull request.** | **Maintenance** |  |  |  |  | ✓ |  | 1 |
| **Specify any code-generation or refactoring tasks the AI must not attempt unilaterally** (e.g., "Do not rename more than 5 files in a single response; do not refactor more than one major subsystem per session") | AI Constraints and Guardrails |  |  |  | ✓ |  |  | 1 |
| **Specify any database query or index constraints** (e.g., "Always include EXPLAIN ANALYZE in PR descriptions for schema changes; indexes are mandatory for columns used in WHERE clauses") | Performance and Scalability |  |  |  | ✓ |  |  | 1 |
| **Specify any prefixes or suffixes for special constructs** (e.g., "React hooks are named useX; custom middleware is named withX; selectors are named selectX") | Naming and Conventions |  |  |  | ✓ |  |  | 1 |
| **Specify async test patterns:** "All async operations in tests must have explicit timeout guards; default is 5000ms | Testing |  |  |  | ✓ |  |  | 1 |
| **Specify file and folder naming rules** (e.g., "React components go in src/components/ and are PascalCase; utilities go in src/utils/ and are camelCase") | Naming and Conventions |  |  |  | ✓ |  |  | 1 |
| **Specify rules for error handling:** "All async functions must handle errors; use try/catch for promises or .catch() for chains; never ignore rejected promises." | Type Safety and Language Features |  |  |  | ✓ |  |  | 1 |
| **Specify the branching and PR workflow (branch naming, commit style, who merges).** Agents otherwise invent plausible-but-wrong conventions | Safety |  |  | ✓ |  |  |  | 1 |
| **Specify the testing framework(s) and conventions** (e.g., "Jest for unit tests, Cypress for E2E; test files live in __tests__ folders; use describe/it syntax") | Testing |  |  |  | ✓ |  |  | 1 |
| **Specify timeout, rate-limit, and resource constraints** that the codebase enforces and that code generation must respect | Safety and Security |  |  |  | ✓ |  |  | 1 |
| **State all data-sensitivity or compliance constraints explicitly** (e.g., "PII must never be logged," "all network requests require auth tokens") | Safety and Security |  |  |  | ✓ |  |  | 1 |
| **State constraints on AI behavior explicitly** if they exist (e.g., "Do not modify .env files," "Do not create migrations without manual approval") | Content and Specificity |  |  |  | ✓ |  |  | 1 |
| **State destructive-command policy explicitly (migrations, `rm -rf`, force-push, prod deploys).** Defaults are not safe; make the rule unambiguous | Safety |  |  | ✓ |  |  |  | 1 |
| **State facts and conventions, not aspirations.** | **Style & Tone** |  |  |  |  | ✓ |  | 1 |
| **State rules about re-renders, memoization, or caching** if the project has learned lessons (e.g., "Memoize components that receive object props; use useCallback for event handlers passed to children") | Performance and Scalability |  |  |  | ✓ |  |  | 1 |
| **State rules as imperatives ("Use X." / "Never Y."), not preferences.** Models weight imperative language more reliably than hedged prose | Content |  |  | ✓ |  |  |  | 1 |
| **State rules for naming async/promise-returning functions** if not obvious (e.g., "Use verb phrases for async functions: fetchUser, loadData, submitForm") | Naming and Conventions |  |  |  | ✓ |  |  | 1 |
| **State whether tests are run in CI and which failures block merges.** | Testing |  |  |  | ✓ |  |  | 1 |
| **State whether the AI should seek clarification or make assumptions** when faced with ambiguity (e.g., "If a rule is unclear, ask; do not guess") | AI Constraints and Guardrails |  |  |  | ✓ |  |  | 1 |
| **State which JavaScript features are forbidden or required** (e.g., "No var; use const by default, let only for loop counters; avoid eval and Function constructor") | Type Safety and Language Features |  |  |  | ✓ |  |  | 1 |
| **Use H2 headings for top-level sections and H3 sparingly.** Headings are how both humans and models navigate; deep nesting hurts both | Structure |  |  | ✓ |  |  |  | 1 |
| **Use Markdown headings (`##`, `###`) to structure major sections.** | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| **Use `CLAUDE.md` if your team standardizes on Claude; use `AGENTS.md` for cross-tool portability.** (contested) Pick one and symlink if needed; don't maintain two copies | Filename |  |  | ✓ |  |  |  | 1 |
| **Use a table of contents if CLAUDE.md exceeds 500 lines.** AI assistants and humans both benefit from a scannable index | Structure |  |  |  | ✓ |  |  | 1 |
| **Use bulleted lists for discrete points and rules.** | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| **Use consistent terminology.** If you say "component" in one section and "module" in another for the same concept, you will confuse readers and AI assistants | Clarity and Tone |  |  |  | ✓ |  |  | 1 |
| **Use imperative, active voice** ("Do X" / "Don't Y") rather than passive or conditional ("X is preferred," "consider doing X") | Clarity and Tone |  |  |  | ✓ |  |  | 1 |
| **Use present tense and active voice.** "The API returns JSON" beats "JSON will be returned by the API." | Style |  |  | ✓ |  |  |  | 1 |
| **Use real patterns from the codebase as examples.** Synthetic examples can misrepresent the actual challenge | Examples and Anti-Examples |  |  |  | ✓ |  |  | 1 |
| **Use the filename `CLAUDE.md` or `AGENTS.md`.** (contested) | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| **Validate that code examples in CLAUDE.md actually run.** A rule with a broken code snippet undermines trust in all rules | Correctness |  |  |  | ✓ |  |  | 1 |
| **Write all file paths relative to the project root.** | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| **Write in direct, imperative sentences ("Do X," "Use Y").** | **Style & Tone** |  |  |  |  | ✓ |  | 1 |
| **Write in second-person imperative or bare imperative; avoid "we" and "you should."** Rules, not suggestions | Style |  |  | ✓ |  |  |  | 1 |
| **Write one rule per sentence.** If a rule has multiple conditions or exceptions, break it into separate, numbered rules or a short list | Clarity and Tone |  |  |  | ✓ |  |  | 1 |
| *Rationale:* An outdated rule is more harmful than no rule at all; conciseness is a key feature | **Maintenance** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Avoids duplicating the `package.json` or `Makefile`, which is the source of truth for commands | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Clearly delineates code and file system artifacts from descriptive text, reducing ambiguity | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Creates a parsable document structure that is easy for both humans and machines to scan | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Enforces conciseness, which improves maintainability and ensures a high signal-to-noise ratio | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Ensures clear accountability for maintaining this crucial piece of project documentation | **Maintenance** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Establishes a predictable, root-level location for AI assistants to find project context | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Every token is valuable; this is a technical specification for an agent, not a `README` for a human | **Style & Tone** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Guides the AI to generate secure-by-default code (e.g., "Use `db.query()` for all database access to prevent SQL injection") | **Safety** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Helps the AI understand how to correctly apply security controls when modifying protected resources | **Safety** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Linking to ADRs, schemas, or documentation (`docs/API_STYLE_GUIDE.md`) prevents the file from becoming stale | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Lists are easily parsed by AIs and prevent long, hard-to-read paragraphs | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Prevents the AI from learning or propagating unsafe development practices, even for local testing | **Safety** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Provides a consistent, unambiguous frame of reference for file locations | **Structure & Formatting** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Provides clear, unambiguous instructions that are easily interpreted as rules by the AI | **Style & Tone** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Provides the AI with a glossary to understand the domain-specific language used in the codebase | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* The AI can read source files directly; this file's purpose is to provide high-level guidance and pointers | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* The file should describe the "how" and "why" of the project, which changes less frequently than specific code | **Content & Scope** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Treats the file as a critical project artifact, ensuring it remains accurate and up-to-date | **Maintenance** |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Use "All API routes are defined in `src/pages/api`" instead of "We are trying to move API routes to `src/pages/api`." | **Style & Tone** |  |  |  |  | ✓ |  | 1 |
| Add a CI check that runs all canonical commands and flags stale links | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Assign clear ownership (CODEOWNERS line) for the memory file | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid marketing, fluff, and jokes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Call out concurrency/threading model and shared-state invariants | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare SLOs/perf budgets for hot paths and endpoints | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare explicit non-goals/out-of-scope | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define a “Definition of Done” (tests passing, lint/format clean, docs updated, perf within budget) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define retry/backoff/jitter defaults and when to surface vs suppress | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define the preferred refactor policy (local-first; avoid cross-module unless approved) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do document performance-critical areas and any architectural decisions that impact efficiency | Performance |  | ✓ |  |  |  |  | 1 |
| Do encourage feedback on the document to identify areas of improvement | Common Pitfalls |  | ✓ |  |  |  |  | 1 |
| Do ensure that all documented practices accurately represent the project’s enforced conventions and practices | Correctness |  | ✓ |  |  |  |  | 1 |
| Do include guidelines on security practices and error handling | Safety |  | ✓ |  |  |  |  | 1 |
| Do include version control notes to track changes to the document | Maintainability |  | ✓ |  |  |  |  | 1 |
| Do schedule regular reviews of the project memory file, ideally alongside major code updates or sprints | Maintainability |  | ✓ |  |  |  |  | 1 |
| Do start with an overview section that summarizes key project goals and conventions | Structure |  | ✓ |  |  |  |  | 1 |
| Do structure the document with clear headings and subheadings | Structure |  | ✓ |  |  |  |  | 1 |
| Do use plain language and avoid jargon unless well-defined within the document | Readability |  | ✓ |  |  |  |  | 1 |
| Document PII handling, redaction, and retention policies with links | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document caching/TTL policies, timeouts, and backpressure behavior | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document rollback and recovery steps for deploys and migrations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document schema evolution policy and migration ordering | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document toolchain versions (language, runtime, package manager) and pinning strategy | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't assume prior knowledge of the project | Readability |  | ✓ |  |  |  |  | 1 |
| Don't document optional practices as mandatory without clear justification | Correctness |  | ✓ |  |  |  |  | 1 |
| Don't include large blocks of text without breaks or bullet points | Structure |  | ✓ |  |  |  |  | 1 |
| Don't let the project memory file become stale; this leads to its decreased effectiveness | Common Pitfalls |  | ✓ |  |  |  |  | 1 |
| Don't overlook the impact of practices on performance without explanation | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t bury “Do not edit” warnings; place them where assistants will see them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t duplicate full guides, API references, or ADRs; link to them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t ignore the documentation of edge cases in error handling | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t include secrets, tokens, or private endpoints | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t rely on screenshots or external images for critical steps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t use ambiguous verbs like “run the app”; specify exact commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce a hard 200–300 line cap for the file | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enumerate key architectural invariants (e.g., layering, IO boundaries, threading model, event schemas) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Forbid editing generated files and vendored code | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Forbid storing secrets, tokens, or sample private data in CLAUDE.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Generate CLAUDE.md from small maintained fragments if the repo is large | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Identify hot code paths and known bottlenecks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include YAML/JSON frontmatter with commands/envs for tool parsing | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a docs:validate or equivalent that checks examples and commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “Repo Map” with only key paths and “do not edit” areas | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Instruct assistants to run tests/linters and paste summaries before proposing merges | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Intended audience: Repository maintainers, platform/enablement teams, and AI assistant integrators creating and enforcing CLAUDE.md content | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep decisions brief in-file and link to full ADRs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep examples minimal and executable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the file ≤300 lines; link to deeper docs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Link to ADRs/architecture docs; include one-line summaries in-place | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Link to golden tests/fixtures and sample datasets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| List canonical commands: setup, run, test, format, lint, typecheck, generate, migrate, seed, profile, package, release | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| List primary context files to open for tasks (e.g., X for models, Y for handlers) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| List required environment variables with type, default, and whether secret | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mark all generated code and “DO NOT EDIT” directories and patterns | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name the vendor-neutral file AGENTS.md and add CLAUDE.md as a one-line pointer to it | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Offer machine-readable frontmatter for key fields (commands, owners, anchors) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place the memory file at repo root | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer AGENTS.md with CLAUDE.md as a shim to remain vendor-neutral | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer bullets over paragraphs; avoid nested bullets >2 levels deep | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer links to scripts checked into the repo over inline script blobs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a deterministic seed/reset command for local dev | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a make task or script to regenerate the Repo Map snippet | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a minimal, deterministic test command to validate changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a standard error shape/contract for APIs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide an “Ask-before” checklist for high-risk changes (migrations, dependency bumps, cross-boundary refactors, public API changes, infra/CI edits) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide incident and security contacts (email/alias) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide migration and rollback procedures | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide profiling/tracing commands and how to capture a baseline | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide stable, unique H2/H3 anchors for each section | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require explicit human approval before running destructive scripts or data changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require performance checks on PRs touching hot paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require updating CLAUDE.md in the same PR as any change to commands, structure, or invariants | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: This ruleset defines what “good” looks like for top-level CLAUDE.md/AGENTS.md project-memory files that AI coding assistants auto-load each session | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify commit message and PR conventions (scope, type, references) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify logging and metrics expectations for new code paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify logging levels and what must never be logged (PII, secrets) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify repository layout and module boundaries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify third-party service boundaries and credentials acquisition flow | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Stamp the file with version and Last-Reviewed date at the top | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start with TL;DR and Quickstart commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State dependency and license policies (allowlist/denylist; review process) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State error-handling policy (e.g., fail fast on invariant breach; degrade gracefully on upstream failures) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State files assistants must read before editing (e.g., CONTRIBUTING, STYLE, ADR index) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use a fixed section order: Purpose, TL;DR, Repo Map, Canonical Commands, Invariants, Environments, Safety, Testing, Release, Observability, AI Guardrails, Decision Log (summary), Changelog | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use consistent terminology for commands and directories | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use relative links within the repo | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write imperative, second-person, one-sentence rules and bullets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

