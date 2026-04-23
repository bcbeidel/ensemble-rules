# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| (contested) Avoid including large code blocks as examples | Content & Style |  |  |  |  | ✓ |  | 1 |
| (contested) Do enforce a maximum line length of 80 characters | Common Areas of Disagreement |  | ✓ |  |  |  |  | 1 |
| **Begin every rule file with YAML frontmatter containing `paths:` and `description:`.** Without `paths:`, the file either never loads or always loads — both are bugs | Structure |  |  | ✓ |  |  |  | 1 |
| **Date or version rules tied to migrations or deprecations (e.g., `// until 2025-Q2`).** Time-boxed rules must announce their own expiry | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Delete rules when the underlying convention changes; do not add a contradicting rule.** Stale rules poison every future edit under their path | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Do not create a rule file that loads for every file in the repo unless its rules are genuinely universal.** Universal-looking files accrete subsystem-specific rules and become unreadable | Scoping |  |  | ✓ |  |  |  | 1 |
| **Do not duplicate a rule across multiple files; extract shared rules to a single file with appropriate `paths:`.** Duplication guarantees drift | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not use RFC 2119 keywords (MUST, SHOULD, MAY).** (contested) Plain imperatives are equally binding to an LLM and cheaper to read | Content |  |  | ✓ |  |  |  | 1 |
| **Do not wrap rule files in prose introductions longer than two lines.** Preambles are skimmed; the rules are what matter | Style |  |  | ✓ |  |  |  | 1 |
| **Follow each rule with exactly one line of rationale.** More than one line is an essay; zero lines leaves the model guessing intent | Structure |  |  | ✓ |  |  |  | 1 |
| **Forbid specific anti-patterns by name when they have bitten this codebase.** Named prohibitions are more effective than positive framing | Content |  |  | ✓ |  |  |  | 1 |
| **Include a code example only when the rule is non-obvious from prose, and keep it under 10 lines.** Examples are expensive; use them surgically | Content |  |  | ✓ |  |  |  | 1 |
| **Keep each rule file under 200 lines.** Beyond this, split by subsystem; long files get truncated or ignored in context | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep rationales falsifiable.** "Because it's cleaner" is not a rationale; "because `FooClient` is not thread-safe" is | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Never let two rule files whose `paths:` overlap state contradictory rules.** The model's resolution is undefined; you will not notice until it matters | Scoping |  |  | ✓ |  |  |  | 1 |
| **Never put secrets, tokens, or real hostnames in rule files.** Rule files are checked in and indexed; treat them as public | Safety |  |  | ✓ |  |  |  | 1 |
| **Omit rules that describe universal programming hygiene.** "Handle errors" wastes the budget; "wrap `db.Exec` calls in `withRetry`" earns it | Content |  |  | ✓ |  |  |  | 1 |
| **Place the most load-bearing rules first within each section.** Context windows truncate from the end when budget is tight | Structure |  |  | ✓ |  |  |  | 1 |
| **Put one rule per bullet, phrased as a single imperative sentence.** Multi-clause rules hide violations and are harder to cite | Structure |  |  | ✓ |  |  |  | 1 |
| **Put repo-wide conventions in the top-level memory file (e.g., `CLAUDE.md`), not in a rule file with `paths: "**/*"`.** The top-level file has a defined role; a catch-all rule file duplicates it | Scoping |  |  | ✓ |  |  |  | 1 |
| **Reference project-specific names, modules, and APIs by exact identifier.** Generic advice is already in the base model; specificity is what you're paying tokens for | Content |  |  | ✓ |  |  |  | 1 |
| **Review rule files whenever their `paths:` glob's code undergoes major refactor.** Rules survive refactors they shouldn't; audits catch this | Maintenance |  |  | ✓ |  |  |  | 1 |
| **Spell out destructive-operation prohibitions explicitly (force-push, drop table, rm -rf, prod credentials).** Destructive defaults are the one place redundancy is worth the tokens | Safety |  |  | ✓ |  |  |  | 1 |
| **State required pre-conditions for risky commands (dry-run, staging-first, confirmation flag).** Conditions buried in prose get skipped; list them | Safety |  |  | ✓ |  |  |  | 1 |
| **State rules as prohibitions or commands, never as suggestions.** "Consider X" and "prefer Y" read as optional; LLMs mirror the hedging | Content |  |  | ✓ |  |  |  | 1 |
| **Target under 2,000 tokens per rule file.** Beyond this, loading cost exceeds benefit for most edits | Performance |  |  | ✓ |  |  |  | 1 |
| **Use at most two heading levels (`##` and `###`).** Deeper nesting confuses parsers and adds no information | Structure |  |  | ✓ |  |  |  | 1 |
| **Use fenced code blocks with language tags for all code snippets.** Untagged fences defeat syntax-aware tooling and occasionally get reflowed | Style |  |  | ✓ |  |  |  | 1 |
| **Write `paths:` globs as narrowly as the rule's domain.** Overbroad globs pollute unrelated edits with irrelevant instructions | Scoping |  |  | ✓ |  |  |  | 1 |
| **Write in second-person imperative or bare imperative; avoid first-person plural ("we").** "We prefer" is weaker than "Use" | Style |  |  | ✓ |  |  |  | 1 |
| Audience: Engineers authoring/reviewing rule files and maintainers of assistant runtimes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid first-person, apologies, or pleasantries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Break ties after priority by choosing the rule whose matching glob has the longest fixed prefix | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare capabilities in frontmatter: allow_tools (string[]), deny_tools (string[]), and network: off\|allowlist\|on | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define a `paths` glob in the YAML frontmatter | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Define scoping with a required paths (include) array and optional exclude_paths array of repo-relative globs that do not start with '/' | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do adopt a consistent naming convention | Style |  | ✓ |  |  |  |  | 1 |
| Do avoid using deprecated APIs | Safety |  | ✓ |  |  |  |  | 1 |
| Do explicitly document error handling behavior for all functions | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do explicitly forbid rules that could cause data loss, like file deletions | Safety |  |  |  |  |  | ✓ | 1 |
| Do include a 'paths' frontmatter at the top of the file to define the scope | Structure |  |  |  |  |  | ✓ | 1 |
| Do include a safety disclaimer in the preamble for high-risk rules | Safety |  |  |  |  |  | ✓ | 1 |
| Do include descriptive comments for complex code sections | Style |  | ✓ |  |  |  |  | 1 |
| Do keep the file size under 10KB | Performance |  |  |  |  |  | ✓ | 1 |
| Do limit line lengths to 80 characters | Style |  |  |  |  |  | ✓ | 1 |
| Do minimize the use of global variables | Performance |  | ✓ |  |  |  |  | 1 |
| Do not include real secrets, tokens, keys, or endpoints; use obvious placeholders like '<TOKEN>' or '<ORG_URL>' | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not instruct network or shell execution unless allowed by frontmatter | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not suggest raw, destructive shell commands (e.g., `rm -rf`, `dd`) | Correctness & Safety |  |  |  |  | ✓ |  | 1 |
| Do not use overscoped globs like '**/*' or '*' alone | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize content into clear, thematic headings (e.g., Structure, Safety) | Structure |  |  |  |  |  | ✓ | 1 |
| Do prioritize essential rules over optional ones | Performance |  |  |  |  |  | ✓ | 1 |
| Do use clear and consistent headings | Structure |  | ✓ |  |  |  |  | 1 |
| Do use consistent markdown formatting, such as bullet points for rules | Style |  |  |  |  |  | ✓ | 1 |
| Do use precise, unambiguous language in rules | Content |  |  |  |  |  | ✓ | 1 |
| Do write each rule as a single imperative sentence followed by a one-line rationale | Content |  |  |  |  |  | ✓ | 1 |
| Don't allow wildcard paths in frontmatter; specify exact patterns | Safety |  |  |  |  |  | ✓ | 1 |
| Don't exceed 500 lines per file (contested) | Structure |  |  |  |  |  | ✓ | 1 |
| Don't include examples longer than one line in the main body | Content |  |  |  |  |  | ✓ | 1 |
| Don't include redundant or duplicate rules across files | Performance |  |  |  |  |  | ✓ | 1 |
| Don't mix tabs and spaces for indentation; use spaces exclusively | Style |  |  |  |  |  | ✓ | 1 |
| Don't reference external documentation without a direct link | Content |  |  |  |  |  | ✓ | 1 |
| Don't use bold or italics excessively (contested) | Style |  |  |  |  |  | ✓ | 1 |
| Don't use nested frontmatter structures; keep them flat and simple | Structure |  |  |  |  |  | ✓ | 1 |
| Don’t hard-code sensitive information directly in the code | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t ignore error returns in functions | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t nest rules more than three levels deep | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t perform unnecessary calculations in loops | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t use excessive abbreviations in identifiers | Style |  | ✓ |  |  |  |  | 1 |
| Ensure at least one include glob matches a file in the repository at authoring time | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fence all code with language-tagged triple backticks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Follow each rule with a short rationale | Content & Style |  |  |  |  | ✓ |  | 1 |
| Group rules under H2 theme headings (Structure, Scoping & Precedence, Content Style, Safety, Performance, Correctness & Testing, Maintenance & Governance, Error Handling & Conflicts) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If an example is necessary, keep it minimal and targeted to the specific point | Content & Style |  |  |  |  | ✓ |  | 1 |
| Increment version (semver) on behavior changes and update the ISO 8601 updated date | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep all lines to 100 characters or fewer | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep each code block to at most 50 lines and use no more than 3 code blocks per file | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep each rule file under 16 KB and 300 lines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep one focused concern per file and split unrelated topics | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep rule files concise and under 2kb | Performance |  |  |  |  | ✓ |  | 1 |
| Limit the combined length of paths and exclude_paths to 20 entries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place only one core concept in each rule file | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Place rule files under .claude/rules/ using kebab-case filenames ending in .md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer guiding code generation over describing abstract principles | Correctness & Safety |  |  |  |  | ✓ |  | 1 |
| Prefer specific include globs over many excludes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefix destructive shell examples with 'echo ' or a preceding '# DANGEROUS: example only' comment | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a resolvable owner (email or team slug) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide frontmatter keys: title, paths, owner, version, updated, priority, status | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Reference an external source of truth when possible | Correctness & Safety |  |  |  |  | ✓ |  | 1 |
| Remove redundant or obvious instructions | Performance |  |  |  |  | ✓ |  | 1 |
| Scope: Rules for writing and maintaining Agent Rule Files (path-scoped markdown in .claude/rules/*.md) consumed by AI coding assistants | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set priority as an integer 1–5 where higher wins conflicts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set status to one of: draft, active, deprecated; archive deprecated files instead of deleting | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start rules with strong verbs and avoid “should”, “try”, “maybe”, or “consider” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start the file with valid YAML frontmatter bounded by '---' lines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State a fallback behavior for conflicts or missing context (e.g., “ask the user” or “defer to higher-priority file”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Structure the file with markdown headers for logical grouping | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Use UTF-8 encoding and LF line endings | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use a descriptive, kebab-case filename for the rule file | Structure & Scoping |  |  |  |  | ✓ |  | 1 |
| Use lists for rules instead of long prose | Content & Style |  |  |  |  | ✓ |  | 1 |
| Use repository-specific examples only when they clarify behavior and keep them minimal | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate frontmatter and globs in CI before merge | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write each rule as a single bullet with an imperative sentence ending in a period, then ' — ' and a one-line rationale | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write rules as imperative commands (e.g., "Use...", "Do not...", "Always...") | Content & Style |  |  |  |  | ✓ |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

