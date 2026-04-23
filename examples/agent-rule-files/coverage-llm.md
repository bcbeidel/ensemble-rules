## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Require YAML frontmatter with a `paths` scoping glob. | Structure/Scoping | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Write each rule as a short imperative sentence followed by a one-line rationale. | Content/Style | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Group rules under clear thematic headings. | Structure | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Avoid hedging language ("should", "try", "consider"); use plain imperatives. | Content/Style | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Keep rule files small/concise to conserve context budget. | Performance | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Never include secrets, tokens, or real credentials in rule files. | Safety | ✓ | ✓ | ✓ |  |  |  | 3 |
| Avoid overly broad globs like `**/*` that apply rules everywhere. | Scoping | ✓ |  | ✓ |  | ✓ |  | 3 |
| Limit or constrain code-block examples (length/count). | Performance/Content | ✓ |  | ✓ |  | ✓ |  | 3 |
| Keep one focused concern per rule file; split by subsystem. | Maintenance | ✓ |  | ✓ |  | ✓ |  | 3 |
| Forbid or guard destructive shell commands in examples. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Use language-tagged fenced code blocks for code snippets. | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Record ownership / last-reviewed metadata for each rule file. | Maintenance | ✓ |  |  | ✓ |  |  | 2 |
| Remove or archive obsolete/deprecated rules rather than leaving them stale. | Maintenance | ✓ |  | ✓ |  |  |  | 2 |
| Validate frontmatter and globs in CI before merge. | Correctness/Testing | ✓ |  | ✓ |  |  |  | 2 |
| Do not duplicate the same rule across multiple files. | Maintenance | ✓ |  | ✓ |  |  |  | 2 |
| Provide a fallback / precedence mechanism for conflicting rules. | Error Handling | ✓ |  | ✓ |  |  |  | 2 |
| State rules in falsifiable, concrete terms (avoid vague qualifiers). | Content/Clarity | ✓ |  |  | ✓ |  |  | 2 |
| Mark contested rules explicitly as (contested). | Content | ✓ |  |  | ✓ |  |  | 2 |
| Use kebab-case / descriptive filenames for rule files. | Structure | ✓ |  |  |  | ✓ |  | 2 |
| Cap line length for readability. | Style | ✓ |  |  |  |  | ✓ | 2 |
| Include a short preamble stating scope/audience/purpose. | Structure | ✓ |  |  | ✓ |  |  | 2 |
| Use bullet lists (rather than long prose) for rules. | Style |  |  |  | ✓ | ✓ |  | 2 |
| Version rules (semver) and include an ISO-8601 updated date. | Maintenance | ✓ |  |  |  |  |  | 1 |
| Declare capability frontmatter (allow_tools/deny_tools/network). | Safety | ✓ |  |  |  |  |  | 1 |
| Use UTF-8 encoding and LF line endings. | Structure | ✓ |  |  |  |  |  | 1 |
| Limit the combined number of include/exclude globs. | Performance | ✓ |  |  |  |  |  | 1 |
| Require a resolvable owner (email or team slug). | Maintenance | ✓ |  |  |  |  |  | 1 |
| Date or version rules tied to migrations/deprecations. | Maintenance |  |  | ✓ |  |  |  | 1 |
| Place load-bearing rules first within each section. | Structure |  |  | ✓ |  |  |  | 1 |
| Reference project-specific names/APIs by exact identifier. | Content |  |  | ✓ |  |  |  | 1 |
| Omit rules that describe universal programming hygiene. | Content |  |  | ✓ |  |  |  | 1 |
| Keep rationales falsifiable (not "because it's cleaner"). | Maintenance |  |  | ✓ |  |  |  | 1 |
| Write in second-person/bare imperative (avoid "we"). | Style |  |  | ✓ |  |  |  | 1 |
| Keep intro prose under two lines. | Style |  |  | ✓ |  |  |  | 1 |
| Limit heading depth to two levels. | Structure |  |  | ✓ |  |  |  | 1 |
| Prefer positive framing ("Use X") over negative ("Don't Y") when clearer. | Content |  |  |  | ✓ |  |  | 1 |
| Name common exceptions explicitly in the rule itself. | Content |  |  |  | ✓ |  |  | 1 |
| Security/stability rules must be unhedged and cite consequences. | Safety |  |  |  | ✓ |  |  | 1 |
| Do not use rule files to hide proprietary/sensitive methods. | Safety |  |  |  | ✓ |  |  | 1 |
| Avoid rules that cause the AI to silently override user intent. | Safety |  |  |  | ✓ |  |  | 1 |
| Update rules only via version-controlled PRs, not ad-hoc. | Maintenance |  |  |  | ✓ |  |  | 1 |
| Do not duplicate linter/formatter configs; reference them. | Content |  |  |  | ✓ |  |  | 1 |
| Use inline code for identifiers, keywords, and file paths. | Style |  |  |  | ✓ |  |  | 1 |
| Reference other rule files by relative path/link. | Structure |  |  |  | ✓ |  |  | 1 |
| Use at most two heading levels (## and ###). | Structure |  |  | ✓ |  |  |  | 1 |
| Keep file under a hard line/token budget (e.g., 200 lines / 2k tokens). | Performance |  |  | ✓ |  |  |  | 1 |
| Don't ignore error returns in functions. | Error Handling |  | ✓ |  |  |  |  | 1 |
| Document error-handling behavior for all functions. | Error Handling |  | ✓ |  |  |  |  | 1 |
| Adopt a consistent naming convention. | Style |  | ✓ |  |  |  |  | 1 |
| Avoid excessive abbreviations in identifiers. | Style |  | ✓ |  |  |  |  | 1 |
| Include descriptive comments for complex code sections. | Style |  | ✓ |  |  |  |  | 1 |
| Avoid deprecated APIs. | Safety |  | ✓ |  |  |  |  | 1 |
| Minimize use of global variables. | Performance |  | ✓ |  |  |  |  | 1 |
| Avoid unnecessary calculations inside loops. | Performance |  | ✓ |  |  |  |  | 1 |
| Don't nest rules more than three levels deep. | Structure |  | ✓ |  |  |  |  | 1 |
| Reference an external source of truth (linter/tests) when possible. | Correctness |  |  |  |  | ✓ |  | 1 |
| Prefer guiding code generation over abstract principles. | Correctness |  |  |  |  | ✓ |  | 1 |
| Remove redundant/obvious instructions. | Performance |  |  |  |  | ✓ |  | 1 |
| Include a safety disclaimer in the preamble for high-risk rules. | Safety |  |  |  |  |  | ✓ | 1 |
| Prioritize essential rules over optional ones. | Performance |  |  |  |  |  | ✓ | 1 |
| Don't mix tabs and spaces; use spaces exclusively. | Style |  |  |  |  |  | ✓ | 1 |

## Notes on clustering decisions

- **"Require YAML frontmatter with paths"**: I merged gpt-5's broader "start with YAML frontmatter bounded by ---" and "provide keys title/paths/owner/..." with the narrower "must have `paths:`" from Opus, Haiku, Gemini, and Grok. gpt-4o-mini did not mention frontmatter at all. A stricter clustering would split "frontmatter at all" from "paths key specifically."
- **"Keep files small/concise"**: gpt-5 (16 KB / 300 lines), Opus (200 lines / 2k tokens), Gemini (2 KB), and Grok (10 KB, <500 lines) all gave different numeric budgets. I clustered them as one rule since the intent is the same; a stricter matcher would separate byte-size, line-count, and token-count variants.
- **"Group under thematic headings"**: Grok's "organize content into clear thematic headings" and Haiku's "group rules by theme with second-level headings" and gpt-4o-mini's "use clear and consistent headings" were clustered together. Opus's separate "use at most two heading levels" is kept distinct because it's a depth constraint, not a grouping directive.
- **Imperative phrasing vs. avoiding hedges**: I kept "write as imperative + rationale" separate from "avoid should/try/consider." They often co-occur but are mechanically distinct (one is a format rule, one is a vocabulary ban). gpt-4o-mini arguably implies imperative style but doesn't state it, so I left it blank.
- **Destructive-command safety**: gpt-5's "prefix destructive examples with echo/DANGEROUS", Opus's "spell out destructive prohibitions", and Gemini's "don't suggest rm -rf/dd" were clustered as one safety rule about destructive shell content. A stricter reading would split "don't include them" from "mark them if you do."
- **Scoping narrowly / avoid broad globs**: gpt-5 ("no `**/*`"), Opus ("write paths as narrowly as the domain" + "don't load for every file"), and Gemini (implicit via "narrowly defined paths glob" in reasoning but also the rules stress scoping) clustered. Grok's "don't allow wildcard paths; specify exact patterns" also fits; I included it.
- **"One concept per file" vs. "don't duplicate rules"**: These are related but distinct. I kept "one focused concern per file" (gpt-5, Opus, Gemini) separate from "don't duplicate a rule across files" (gpt-5, Opus).
- **gpt-4o-mini's rules about code quality** (naming conventions, avoiding globals, loop calculations, deprecated APIs, etc.) are about *application code*, not about *agent rule files*. I listed them as singletons rather than forcing them into clusters with meta-rules from other models, because they're addressing the wrong target audience. A regex matcher might mis-cluster "avoid deprecated APIs" with "remove obsolete rules."
- **Haiku's "reference other rule files by relative path"** is adjacent to gpt-5's linking conventions but specific enough that I kept it a singleton.
- **"Contested" marking**: gpt-5 and Haiku both explicitly prescribe marking contested rules; I clustered those. Other models use "(contested)" tags themselves but don't state it as a rule.