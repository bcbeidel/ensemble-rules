## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Do not include secrets, credentials, or sensitive data in the file. | Safety | ✓ | | | ✓ | ✓ | | 3 |
| Include a last-updated date or timestamp to track freshness. | Maintenance | ✓ | | | ✓ | | ✓ | 3 |
| Keep the file concise and under a defined size/line limit. | Performance | ✓ | | ✓ | | ✓ | ✓ | 4 |
| Link to canonical sources rather than duplicating their content. | Maintenance | ✓ | | ✓ | ✓ | ✓ | | 4 |
| List exact build/test/run commands as copy-pastable code blocks. | Content | ✓ | | ✓ | ✓ | | | 3 |
| Organize content under clear hierarchical headings/sections. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Place the memory file at the repository root. | Structure | ✓ | | ✓ | | ✓ | | 3 |
| Use concise bullets and imperative language over prose. | Style | ✓ | | ✓ | ✓ | | ✓ | 4 |
| Use consistent Markdown formatting/syntax. | Style | ✓ | ✓ | | | ✓ | ✓ | 4 |
| Assign clear ownership (owner/team/CODEOWNERS) for the file. | Maintenance | ✓ | | | ✓ | ✓ | | 3 |
| Document architectural decisions, layout, or boundaries (link to ADRs). | Content | ✓ | | ✓ | ✓ | | | 3 |
| Document environment variables/secrets location with placeholders, not values. | Safety | ✓ | | | ✓ | | | 2 |
| Document project directory layout / where code lives. | Content | ✓ | | ✓ | ✓ | | | 3 |
| Document testing framework, coverage, and how to run tests. | Content | ✓ | | ✓ | ✓ | | | 3 |
| Explicitly list prohibitions / "Do Not" items for assistants. | Safety | ✓ | | ✓ | ✓ | | | 3 |
| Include a changelog or review history for the file. | Maintenance | ✓ | | | | | | 1 |
| Include a table of contents / elevator pitch at the top. | Structure | | ✓ | | ✓ | | | 2 |
| Include an H1/summary naming the project at the top. | Structure | ✓ | | ✓ | | | | 2 |
| Include security best practices / guide toward secure patterns. | Safety | | ✓ | | ✓ | ✓ | ✓ | 4 |
| Keep only one canonical memory file (CLAUDE.md or AGENTS.md, not both). | Structure | ✓ | | ✓ | | ✓ | | 3 |
| Link to linter/formatter configs rather than restating style rules. | Style | | | ✓ | ✓ | | | 2 |
| Maintain a changelog section with dated entries. | Maintenance | ✓ | | | | | | 1 |
| Name linters, formatters, and pre-commit hooks used. | Content | | | | ✓ | | | 1 |
| Prefer relative links for intra-repo references. | Style | ✓ | | | | ✓ | | 2 |
| Require PR review / CODEOWNERS enforcement for changes to the file. | Maintenance | ✓ | | ✓ | ✓ | ✓ | ✓ | 5 |
| Restrict or limit embedded code examples in length. | Style | | | ✓ | ✓ | ✓ | ✓ | 4 |
| Specify branching strategy and CI/CD expectations. | Content | | | | ✓ | | | 1 |
| Specify the package manager and runtime versions explicitly. | Content | ✓ | | ✓ | ✓ | | | 3 |
| State conventions only where they deviate from ecosystem defaults. | Content | | | ✓ | ✓ | | | 2 |
| State forbidden/destructive actions requiring confirmation. | Safety | ✓ | | ✓ | | | | 2 |
| State goals and non-goals / scope explicitly. | Content | ✓ | | | | | | 1 |
| State what's internal/private/off-limits in the codebase. | Safety | | | ✓ | ✓ | | | 2 |
| Use a glossary / define project-specific terminology. | Content | ✓ | | | | ✓ | | 2 |
| Use fixed/predictable section names and stable headings. | Structure | ✓ | | ✓ | | | | 2 |
| Use plain GitHub-Flavored Markdown; avoid custom directives/HTML. | Interoperability | ✓ | | | | | | 1 |
| Use present tense / active voice. | Style | | | | ✓ | | ✓ | 2 |
| Warn users not to paste secrets/production data into prompts. | Safety | ✓ | | | | | | 1 |
| Warn about repo-specific anti-patterns and gotchas. | Safety | ✓ | | ✓ | ✓ | | | 3 |
| Write in a clear style avoiding jargon / define acronyms. | Style | | ✓ | | | ✓ | ✓ | 3 |

## Notes on clustering decisions

- "Organize content under clear hierarchical headings" was clustered aggressively: gpt-5's exact-ordered H2 list, opus's "fixed top-level headings", haiku's "single-level hierarchy", gemini's "hierarchical headings", grok's "hierarchical structure", and 4o-mini's "clearly defined sections" were all treated as the same rule despite very different levels of prescriptiveness. A stricter matcher would split these.
- "Keep the file concise and under a defined size/line limit" collapses wildly different thresholds (gpt-5: 50KB/1200 lines; opus: 200 lines; gemini: 32KB; grok: 500 lines). Clustered because the underlying rule — bound file size for context economy — is identical.
- "Require PR review / CODEOWNERS enforcement" merges gpt-5's CODEOWNERS rule, opus's "review in PR that changes commands", haiku's "assign owner + review yearly", gemini's "review in PR process", and grok's "require peer review for updates". These could plausibly split into "ownership" vs. "review workflow" clusters; I kept them together since all target the same drift-prevention mechanism. I also kept a separate "Assign clear ownership" row for rules that focus on naming an owner rather than the review process — borderline overlap with the review row.
- "Link to canonical sources rather than duplicating" merges gpt-5's "link to SSoT", opus's "don't duplicate package.json scripts", haiku's "link to CONTRIBUTING.md", and gemini's "link, don't duplicate". Close call vs. the separate "link to linter config" rule, which I kept distinct because opus and haiku specifically called it out as a style-deferral rule.
- "Restrict embedded code examples" merges opus's "no blocks >15 lines", haiku's "≤3 lines", gemini's "prefer descriptions over snippets", and grok's "≤5 lines with link". All share the same intent.
- "Include security best practices" groups 4o-mini's generic "document security best practices", haiku's error-handling/secrets conventions, gemini's "highlight security-critical areas", and grok's "state security best practices". Arguably gemini's rule is closer to "warn about anti-patterns"; kept here because its framing is about promoting secure patterns.
- "Use concise bullets / imperative language" and "Write in a clear style avoiding jargon" are adjacent and could be merged. Kept separate because the first is about form (bullets, imperatives) and the second about vocabulary (jargon, acronym definitions).
- gpt-5's many interoperability rules (inline links, no reference-style links, no HTML comments, etc.) were mostly left as single-model rows rather than force-merged, since no other model addressed them.
- opus's "Symlink AGENTS.md to CLAUDE.md" and gemini's "Use the filename AGENTS.md" both touch file-name choice but take opposite positions; I did not cluster them. gpt-5's "use one, not both" is closer to opus and was clustered with it under "Keep only one canonical memory file".
- 4o-mini is sparse; many rows show blank for it not because it disagreed but because it didn't raise the topic.