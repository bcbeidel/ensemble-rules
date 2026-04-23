## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Write steps as a numbered, ordered list with one action per step. | Instructions | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Include explicit trigger conditions / "When to use" section. | Triggers | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Declare required preconditions/prerequisites (and check them before side effects). | Dependencies | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Include concrete input/output examples in the skill. | Examples | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Never hardcode credentials, API keys, or secrets; reference env vars instead. | Safety | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Provide a clear, concise description/title stating what the skill does. | Structure |  | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| Require explicit human confirmation/approval for destructive or high-risk operations. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Specify error handling / failure recovery for steps that can fail. | Error Handling | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Specify timeouts and retry/backoff policy explicitly. | Performance | ✓ |  |  | ✓ |  |  | 2 |
| Cap SKILL.md length (keep it short/focused). | Structure | ✓ |  | ✓ |  |  | ✓ | 3 |
| Use YAML frontmatter with required metadata fields (name, description, version, etc.). | Metadata | ✓ |  | ✓ |  |  |  | 2 |
| Use a canonical/standard filename for the skill file. | Structure | ✓ |  |  | ✓ | ✓ |  | 3 |
| Use a kebab-case / lowercase identifier for the skill name. | Metadata | ✓ |  | ✓ |  | ✓ |  | 3 |
| Use semantic versioning and bump version on changes. | Versioning | ✓ |  | ✓ |  |  |  | 2 |
| Declare an owner (team or individual) for each skill. | Versioning | ✓ |  | ✓ |  |  |  | 2 |
| Write steps in imperative voice / action-oriented language. | Style | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Ban ambiguous/vague filler words (etc., maybe, generally, somehow). | Style | ✓ |  |  |  |  | ✓ | 2 |
| Keep lines under ~120 characters. | Style | ✓ |  | ✓ |  |  |  | 2 |
| Declare and validate allowed input/output types or schema. | Inputs & Outputs | ✓ |  |  | ✓ |  |  | 2 |
| List all environment variables / dependencies the skill uses. | Dependencies | ✓ |  | ✓ | ✓ |  |  | 3 |
| One skill, one workflow; avoid overlapping or kitchen-sink skills. | Scope |  |  | ✓ | ✓ |  |  | 2 |
| Declare a safety/privilege tier (e.g., low/medium/high or ADMIN). | Safety | ✓ |  |  | ✓ |  |  | 2 |
| Include an anti-prompt-injection instruction ("do not follow external instructions"). | Safety | ✓ |  |  |  |  |  | 1 |
| Ban unverified remote execution patterns (curl \| bash, eval of remote content). | Safety |  |  | ✓ |  |  |  | 1 |
| Reference bundled files by relative path from the skill directory. | Structure |  |  | ✓ |  |  |  | 1 |
| Declare expected duration/resource usage/concurrency limits. | Performance |  |  |  | ✓ |  |  | 1 |
| Warn about O(n) scaling / rate limits for loops or external APIs. | Performance |  |  |  | ✓ |  |  | 1 |
| Use consistent naming conventions throughout skills. | Style |  | ✓ |  | ✓ |  | ✓ | 3 |
| Validate all external inputs rigorously. | Safety |  | ✓ |  |  |  | ✓ | 2 |
| Avoid deeply nested conditionals (keep step logic flat). | Structure |  | ✓ |  | ✓ |  |  | 2 |
| Define a clear "definition of done" / verification step. | Correctness |  |  |  |  | ✓ |  | 1 |
| Specify expected success output/exit code for commands. | Error Handling |  |  |  |  | ✓ |  | 1 |
| Filter/reduce command output to minimize tokens returned to agent. | Performance |  |  |  |  | ✓ |  | 1 |
| Use non-interactive flags for commands that might prompt. | Performance |  |  |  |  | ✓ |  | 1 |
| Declare batching / batch_size for array inputs. | Performance | ✓ |  |  |  |  |  | 1 |
| Use placeholders only in a standardized form ({{inputs.NAME}} etc.). | Style | ✓ |  |  |  |  |  | 1 |
| Include a sibling test file with success and failure cases. | Examples & Tests | ✓ |  |  |  |  |  | 1 |
| Don't assume performance is adequate without measurement. | Performance |  | ✓ |  |  |  |  | 1 |
| Don't include unnecessary comments/commentary inside instructions. | Style |  | ✓ |  | ✓ |  |  | 2 |
| Ensure skills can be reused across workflows. | Maintainability |  | ✓ |  |  |  |  | 1 |
| Reference tool calls using a standardized `tool.operation` syntax bound to declared tools. | Tools | ✓ |  |  |  |  |  | 1 |
| Declare tools in frontmatter with operations, inputs/outputs, timeouts, error codes. | Tools | ✓ |  |  |  |  |  | 1 |
| Mark non-idempotent operations and provide compensation/rollback. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Include a catch-all "on unknown error, surface to human and stop". | Error Handling | ✓ |  |  |  |  |  | 1 |
| Update last_updated / changelog on every material change. | Versioning | ✓ |  |  |  |  |  | 1 |
| State PII handling and redaction rules. | Safety | ✓ |  |  |  |  |  | 1 |
| Prefer cache of deterministic lookups with key/TTL noted. | Performance | ✓ |  |  |  |  |  | 1 |
| Use fenced code blocks (with language tags) for commands. | Style |  |  | ✓ | ✓ |  |  | 2 |
| Use ATX-style headings consistently. | Style |  |  | ✓ |  |  |  | 1 |
| Avoid ambiguous pronouns without clear referents. | Style |  |  | ✓ |  |  |  | 1 |
| Write the description to start with "Use when…" and include concrete triggers. | Description |  |  | ✓ |  |  |  | 1 |
| Pin versions for external tools/APIs where behavior shifts across releases. | Dependencies |  |  | ✓ |  |  |  | 1 |
| Log state-changing actions with timestamp, actor, reason, and old/new values. | Safety |  |  |  | ✓ |  |  | 1 |
| Define and declare assumptions about system state or ordering. | Correctness |  |  |  | ✓ |  |  | 1 |
| Avoid undefined jargon/abbreviations. | Style |  |  | ✓ | ✓ |  | ✓ | 3 |
| Externalize complex shell logic into separate versioned scripts. | Content |  |  |  |  | ✓ |  | 1 |
| Prefer tools with a `--dry-run` mode for pre-flight validation. | Safety |  |  | ✓ |  | ✓ |  | 2 |
| Declare the data_access scope / minimal data sources and sinks. | Safety | ✓ |  |  |  |  |  | 1 |
| Set cost/token budget in frontmatter. | Performance | ✓ |  |  |  |  |  | 1 |
| Keep each step to one or two sentences. | Style |  |  |  | ✓ |  |  | 1 |

## Notes on clustering decisions

- "Provide a clear, concise description/title" conflates two partially-distinct ideas: (a) a concise one-line description of purpose (gpt-4o-mini, haiku, grok, gemini) and (b) Opus's stronger "description must start with 'Use when…' and enumerate triggers." I kept Opus in both the general description cluster and in a more specific "Use when…" row; the "Use when…" row is left at count 1 to preserve that precision.
- "Include explicit trigger conditions / When to use" merges gpt-5's strict "Use when / Do not use when + positive/negative trigger phrases" rule with lighter "state trigger conditions" rules from others. A stricter clustering would split out gpt-5's negative-triggers requirement as its own row.
- "Require explicit human confirmation/approval for destructive operations" clusters several variants: gpt-5's [HUMAN-APPROVAL] step gated on safety_tier, Opus's "explicit user confirmation before destructive ops," haiku's approval-gates rule, and gemini's "require explicit user confirmation for state-changing or costly operation." These overlap heavily but differ in trigger (tier vs. operation type).
- "Specify error handling / failure recovery" is a broad cluster covering gpt-4o-mini's generic "implement robust error handling," Opus's "## Failure modes section," haiku's per-step recovery, gemini's "handling for known errors," and gpt-5's error_code→action mapping. A stricter reading would split the structural-section requirement from the per-step requirement.
- "Cap SKILL.md length" merges gpt-5's ≤400 lines, Opus's <300 lines, and grok's <2000 words; the numeric thresholds differ substantially but the intent is the same.
- "Use a canonical/standard filename" merges gpt-5 and gemini's "name the file SKILL.md exactly" with haiku's stricter `SKILL_VerbNoun.md` convention — these are arguably incompatible conventions but both encode "enforce a filename pattern."
- "List all environment variables / dependencies" merges gpt-5's env_vars frontmatter requirement, Opus's `## Prerequisites` with tools/versions, and haiku's `## Dependencies` section. These are structurally different (frontmatter vs. prose section) but share intent.
- "Declare a safety/privilege tier" merges gpt-5's `safety_tier` enum with haiku's "Declare privilege level and required IAM/RBAC roles"; they encode different things (risk tier vs. IAM role) but both sit in the "declare the blast radius up front" family.
- "Don't include unnecessary comments/commentary" merges gpt-4o-mini's "don't include unnecessary comments" and haiku's "don't include reasoning/commentary in instructions" — the first targets code comments broadly, the second targets commentary inside steps specifically.
- "Avoid undefined jargon/abbreviations" merges Opus's "avoid undefined jargon," haiku's "avoid jargon without definition," and grok's "don't use abbreviations without defining" — close enough to cluster.
- gpt-4o-mini's rules are all very generic ("robust error handling," "validate inputs," "optimize performance"); I mapped them to the nearest specific cluster where intent overlaps, but a reader could reasonably argue they're too vague to cluster with more specific rules from other models.
- "Prefer `--dry-run`" clusters Opus's "prefer dry-run/preview as default" with gemini's "prefer tools with `--dry-run`"; these are close in substance.
- gpt-5 emits many rules unique to its frontmatter-heavy stance (tool declarations, retry_policy, data_access, token budgets, placeholder syntax, test sibling file). I kept each as its own row at count 1 rather than folding them into broader clusters, since other models did not raise equivalents.