## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Require explicit confirmation before destructive or irreversible actions. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Keep each skill focused on a single workflow or outcome. | Structure |  |  | ✓ | ✓ | ✓ | ✓ | 4 |
| Include a validation/verification step with a pass/fail signal. | Correctness |  |  | ✓ | ✓ | ✓ | ✓ | 4 |
| Never embed secrets or credentials in skill text; reference them by handle. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| List preconditions, required permissions, and environment explicitly. | Preconditions | ✓ |  | ✓ | ✓ |  |  | 3 |
| Write steps as numbered, imperative, atomic actions. | Steps | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Include explicit error handling and recovery paths for each fallible step. | Error Handling | ✓ | ✓ |  | ✓ |  | ✓ | 4 |
| Specify concrete trigger phrases / when-to-use patterns. | Triggers | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Include a "when NOT to use" / negative-trigger section. | Triggers | ✓ |  | ✓ |  |  |  | 2 |
| Cap skill file length / keep it concise to preserve context budget. | Performance | ✓ |  | ✓ |  |  | ✓ | 3 |
| Use consistent section ordering / standard template. | Structure | ✓ | ✓ |  | ✓ |  | ✓ | 4 |
| Assign an owner / maintainer for each skill. | Maintainability | ✓ |  |  | ✓ |  |  | 2 |
| Record a "last verified" / last-reviewed date and tested versions. | Maintainability | ✓ |  | ✓ | ✓ |  |  | 3 |
| Version skills and maintain a changelog. | Maintainability | ✓ |  | ✓ |  |  |  | 2 |
| Make steps idempotent (or declare when not). | Correctness | ✓ |  | ✓ |  | ✓ |  | 3 |
| Fail fast on missing prerequisites / invalid state. | Error Handling | ✓ |  |  |  | ✓ | ✓ | 3 |
| Prefer exact commands / structured outputs over vague descriptions or stdout parsing. | Steps | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Validate inputs / define input types and formats. | Inputs | ✓ | ✓ |  |  | ✓ | ✓ | 4 |
| Define outputs with a schema or success criteria. | Outputs | ✓ |  | ✓ |  |  |  | 2 |
| Bound retries / don't embed complex retry logic in the skill. | Error Handling | ✓ |  |  | ✓ | ✓ |  | 3 |
| Apply least-privilege / minimum required permissions. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Provide a dry-run or simulation mode for writes. | Safety | ✓ |  |  | ✓ | ✓ |  | 3 |
| Sanitize untrusted input to prevent injection. | Safety | ✓ |  |  |  | ✓ |  | 2 |
| Include at most one minimal inline example; link out for longer ones. | Content | ✓ |  | ✓ |  |  | ✓ | 3 |
| Use active voice / clear, plain language with short sentences. | Style | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Forbid hedging / vague language ("maybe", "try to", "usually"). | Style |  |  | ✓ | ✓ |  | ✓ | 3 |
| Use a consistent naming convention (verb-noun, kebab-case). | Structure |  | ✓ | ✓ | ✓ | ✓ |  | 4 |
| Require testing / executable test scenarios before release. | Testing | ✓ |  |  |  |  | ✓ | 2 |
| Emit structured logs/telemetry for steps and errors. | Observability | ✓ | ✓ |  |  |  |  | 2 |
| Pin tool/API versions to prevent drift. | Tool Usage | ✓ |  | ✓ |  |  |  | 2 |
| Use progressive disclosure / link to external reference material. | Performance | ✓ |  | ✓ |  |  | ✓ | 3 |
| Prohibit chain-of-thought in final user-visible outputs. | Safety | ✓ |  |  |  |  |  | 1 |
| Declare overlapping sibling skills and their boundaries. | Triggers | ✓ |  | ✓ |  |  |  | 2 |
| Clean up temp state / artifacts after execution. | Steps |  |  |  |  | ✓ |  | 1 |
| Do not ask for user input mid-execution. | Steps |  |  |  |  | ✓ |  | 1 |
| Delete or archive unused/deprecated skills. | Maintainability | ✓ |  | ✓ |  |  |  | 2 |
| Require security or owner review before merge/release. | Governance | ✓ |  | ✓ |  |  |  | 2 |
| Document expected durations for known-slow steps. | Performance |  |  |  | ✓ |  |  | 1 |
| Parameterize timeouts rather than hardcoding them. | Performance |  |  |  | ✓ |  |  | 1 |
| Keep lines of code under 80 characters. | Style |  | ✓ |  |  |  |  | 1 |
| Use lazy loading for non-essential modules. | Performance |  | ✓ |  |  |  |  | 1 |
| Include minimum model capability requirements. | Compatibility | ✓ |  |  |  |  |  | 1 |
| Parallelize independent tool calls where safe. | Performance | ✓ |  |  |  |  |  | 1 |
| Cache stable lookups to reduce repeated work. | Performance | ✓ |  |  |  |  |  | 1 |
| Use canonical units/encodings (UTC, ISO-8601). | Inputs | ✓ |  |  |  |  |  | 1 |
| Store skills in version control alongside the code they operate on. | Maintainability |  |  | ✓ |  |  |  | 1 |
| Forbid self-modifying skills (no editing other skills or system prompt). | Safety |  |  | ✓ |  |  |  | 1 |
| Prefer composition via sub-skills for multi-intent tasks. | Structure | ✓ |  |  |  | ✓ |  | 2 |
| Do not use skills as incident/debugging runbooks. | Maintainability |  |  |  | ✓ |  |  | 1 |
| Clarify partial-success vs all-or-nothing semantics. | Error Handling |  |  |  | ✓ |  |  | 1 |
| Use YAML frontmatter for metadata at the top of the file. | Structure | ✓ |  | ✓ |  |  | ✓ | 3 |
| Write the description from the agent's perspective, starting with a verb. | Description |  |  |  |  | ✓ |  | 1 |
| Include the skill's description length/specificity as selection-decidable. | Triggers |  |  | ✓ |  |  |  | 1 |
| Specify scale limits / performance cliffs for iterative steps. | Performance |  |  |  | ✓ |  |  | 1 |
| Include rollback steps for failed operations. | Error Handling | ✓ |  |  | ✓ |  |  | 2 |
| Do not use sudo/root or escalate privileges. | Safety |  |  |  |  | ✓ |  | 1 |
| Short-circuit / fail early when prerequisites fail. | Performance | ✓ |  |  |  | ✓ |  | 2 |
| Provide both happy-path and edge-case examples. | Content | ✓ |  |  |  |  |  | 1 |
| Use code blocks (not prose) for commands and configuration. | Style |  |  |  | ✓ |  | ✓ | 2 |
| Include a glossary / stable terminology for key entities. | Style | ✓ |  |  |  |  |  | 1 |
| Re-review skills on a cadence (e.g., quarterly or on API change). | Maintainability | ✓ |  | ✓ |  |  |  | 2 |

## Notes on clustering decisions

- **"Keep each skill focused on a single workflow"** combines gpt-5's "composition by calling sub-skills," opus's "one skill = one workflow," haiku's "exactly one outcome," gemini's "single, clear responsibility," and grok's "single, focused workflow." These are phrased very differently but all express the atomicity principle. A regex matcher would likely miss this grouping.
- **"Specify concrete trigger phrases"** spans "When to Use" (gpt-5), `when_to_use` frontmatter (opus), Trigger section under 2 sentences (haiku), "when-to-use" triggers (gemini), and "when-to-use trigger language" (grok). I treated these as one cluster even though the level of specificity varies.
- **"Validation step with a pass/fail signal"** merges opus's "verification step," haiku's "Validation section," gemini's "explicit exit codes/output signals," and grok's "validation steps for inputs and outputs." Grok's is arguably more about input validation — borderline case, but kept here because it also covers outputs.
- **"Prefer exact commands over vague descriptions"** conflates opus's `pytest -q` example, haiku's "avoid 'use best judgment'," gemini's "prefer structured commands over parsing stdout," grok's "actionable verbs" and "avoid vague terms," and gpt-5's "strong verb, testable steps." These touch adjacent concerns (exactness vs. structured I/O vs. imperative verbs) that could be split into 2–3 clusters; I kept them together as "make steps unambiguous and machine-parseable."
- **"Use active voice / clear, plain language"** absorbs multiple style rules (short sentences, imperative voice, plain language). Arguably "imperative voice" deserves its own row, but every model that raised imperatives also raised plain/clear language, so I merged.
- **"Include error handling and recovery paths"** vs. **"Bound retries / don't embed complex retry logic"** — kept separate because gemini and opus explicitly argue retry logic belongs in the agent, not the skill, which is a distinct (and contested) position.
- **"Record last-verified date"** and **"Version skills / changelog"** kept separate: the former is about staleness signaling, the latter about change tracking. Some models did both, some only one.
- **"YAML frontmatter for metadata"** — gpt-5 says "Name, Summary, Owner, Version, Last-Reviewed" at top, opus says "frontmatter," grok says "YAML front matter." Treated as same cluster though gpt-5 doesn't explicitly say YAML.
- **gpt-4o-mini's rules are mostly generic software-engineering advice** (80-char lines, lazy loading, camelCase) that didn't overlap much with the skill-specific rules raised by the other models. This shows up as many single-model rows for that column.
- **"Clean up temp state"** (gemini) and **"Record partial progress and safe rollback steps"** (gpt-5) are related but distinct (cleanup vs. rollback); kept separate.
- **"Progressive disclosure / link out"** (gpt-5, opus, grok) was clustered even though gpt-5 frames it as "link out for deep references," opus as "progressive disclosure," and grok as "don't embed large code snippets." All three express the same mechanism.