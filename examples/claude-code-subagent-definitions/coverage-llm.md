## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Grant only the minimum tools required (least privilege). | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Declare tool allowlist explicitly; no wildcards or "all". | Tooling | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Cap the system prompt length for efficiency/determinism. | Performance | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Mandate an explicit, structured/machine-parsable output format. | Error Handling | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Keep each subagent to a single, well-defined responsibility. | Structure |  | ✓ | ✓ | ✓ | ✓ |  | 4 |
| Require YAML frontmatter with required metadata keys. | Structure | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Write a concise, routing-oriented description. | Description |  | ✓ | ✓ | ✓ | ✓ |  | 4 |
| Constrain/scope shell (Bash) use or restrict dangerous tools. | Safety | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Place subagent files in `.claude/agents/` with `.md` extension. | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use an agreed filename convention (kebab-case / descriptive). | Naming | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Include at least one concrete input/output example. | Testing |  | ✓ | ✓ | ✓ |  |  | 3 |
| Provide explicit refusal/failure/escalation behavior. | Error Handling | ✓ |  |  | ✓ | ✓ |  | 3 |
| Do not embed secrets or credentials in the definition. | Safety | ✓ | ✓ |  | ✓ |  |  | 3 |
| Version subagents and document changes in a changelog. | Versioning | ✓ |  |  | ✓ |  | ✓ | 3 |
| Constrain filesystem scope via path allowlist/denylist. | Safety | ✓ |  |  | ✓ |  |  | 2 |
| Use consistent section headings / standard template. | Structure | ✓ |  |  |  | ✓ |  | 2 |
| Require an explicit owner / stewardship for each subagent. | Ownership | ✓ |  |  |  |  |  | 1 |
| Set bounded timeouts for execution. | Performance | ✓ |  |  |  |  |  | 1 |
| Cap max_output_tokens. | Performance | ✓ |  |  |  |  |  | 1 |
| Require dry-run / commit-preview before writes. | Safety | ✓ |  |  |  |  |  | 1 |
| Default network access off; require allowed_domains when on. | Safety | ✓ |  |  |  |  |  | 1 |
| Validate tool allowlist against a central approved list in CI. | Testing | ✓ |  |  |  |  |  | 1 |
| Define an explicit escalate_to target (handoff). | Error Handling | ✓ |  |  |  |  |  | 1 |
| Stop after N failed attempts and escalate. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Use kebab-case id matching filename stem. | Naming | ✓ |  | ✓ |  |  |  | 2 |
| Regularly review and iterate on definitions. | Maintainability |  | ✓ |  |  |  |  | 1 |
| Include trigger phrases (e.g., PROACTIVELY / MUST BE USED) in description. | Description |  |  | ✓ |  |  |  | 1 |
| Avoid duplicated/overlapping trigger vocabulary across agents. | Description |  |  | ✓ |  |  | ✓ | 2 |
| Open the system prompt with a one-line role statement / primary goal. | Prompt |  |  | ✓ | ✓ |  |  | 2 |
| Structure the system prompt with markdown headings. | Prompt |  |  | ✓ |  |  |  | 1 |
| Do not reference prior conversation state in the system prompt. | Prompt |  |  | ✓ |  |  |  | 1 |
| End system prompt with a self-check / success criteria. | Prompt |  |  | ✓ |  |  |  | 1 |
| Choose the model tier intentionally (haiku/sonnet/opus). | Model Selection |  |  | ✓ |  |  |  | 1 |
| Write prompt instructions in imperative mood. | Style |  |  | ✓ |  | ✓ |  | 2 |
| Avoid hedging/apology language in the system prompt. | Style |  |  | ✓ |  |  |  | 1 |
| Commit project subagents to version control. | Repo Hygiene |  |  | ✓ |  |  |  | 1 |
| Don't commit personal subagents to project repo. | Repo Hygiene |  |  | ✓ |  |  |  | 1 |
| Document non-obvious subagents in the README. | Repo Hygiene |  |  | ✓ |  |  |  | 1 |
| Include a Scope & Constraints / out-of-scope section. | Structure | ✓ |  |  | ✓ |  |  | 2 |
| Do not interpolate untrusted user input into the prompt (injection). | Safety |  |  |  | ✓ |  | ✓ | 2 |
| Do not include instructions that contradict the tool allowlist. | Correctness |  |  |  | ✓ |  |  | 1 |
| Use consistent terminology/tone across agents. | Style |  |  |  | ✓ |  | ✓ | 2 |
| Document project/runtime assumptions explicitly. | Documentation |  |  |  | ✓ |  |  | 1 |
| Require review/confirmation step for sensitive-file edits. | Safety |  |  |  | ✓ |  |  | 1 |
| Explicitly forbid destructive operations in the prompt. | Safety |  |  |  | ✓ |  |  | 1 |
| Mark subagents deprecated rather than deleting them. | Versioning |  |  |  | ✓ |  |  | 1 |
| Include a "Related Subagents" section when applicable. | Documentation |  |  |  | ✓ |  |  | 1 |
| Use CamelCase/PascalCase for the `name` field. | Naming |  |  |  | ✓ |  |  | 1 |
| Enclose dynamic placeholders in `<context>` tags. | Prompt |  |  |  |  | ✓ |  | 1 |
| Keep the section order Description → Tools → System prompt. | Structure |  |  |  |  | ✓ |  | 1 |
| Don't exceed three levels of headings in the file. | Style |  |  |  |  |  | ✓ | 1 |
| Don't leave placeholder/TODO text in final definitions. | Style |  |  |  |  |  | ✓ | 1 |

## Notes on clustering decisions

- **"Grant only the minimum tools (least privilege)"** merges gpt-5's "Grant the minimum tools needed", gpt-4o-mini's "limit scope of actions to the allowlist", opus's "grant only tools actually used", haiku's "include only tools necessary", gemini's "grant the minimum set of tools", and grok's justification-per-tool rule. These are phrased quite differently but all express least privilege; a regex matcher would likely miss some.
- **"Declare tool allowlist explicitly; no wildcards"** groups "never use `*`/`all`" (gpt-5, opus, grok-implicit via enumeration), gpt-4o-mini's "no ambiguous entries", and haiku's "no wildcards unless fallback". Grok's "explicit list with bullet points" was treated as the same rule as "enumerate explicitly".
- **"Cap system prompt length"** merges specific numeric thresholds that differ across models (gpt-5: 3000 chars; opus: ~1500 tokens; haiku: 2 KB; grok: 500 tokens). A fuzzy matcher would likely separate these by number; I clustered on intent.
- **"Mandate structured output format"** merges gpt-5's "Output contract", opus's "specify output format explicitly", haiku's output-format requirements, and gemini's "machine-parsable output". gpt-4o-mini has no clear analog.
- **"Single responsibility"** clusters gpt-4o-mini's "don't overload a subagent", opus's "single responsibility", haiku's "single-purpose", and gemini's "one primary verb". Arguably distinct from "don't duplicate trigger vocabulary" (kept separate).
- **"Constrain/scope dangerous tools (Bash)"** merges gpt-5's write-capable-tool guards (dry-run/preview), opus's Bash-specific caution, haiku's shell caution, and grok's sensitive-tool caveat. I debated splitting Bash-specific from general destructive-tool rules; I kept them together because all are about extra scrutiny for high-risk tools. gpt-5's specific `dry_run_required`/`commit_preview_required` rules were split out as their own more-specific mechanisms.
- **Naming rules** are fragmented across models (kebab-case filename, kebab-case id, CamelCase `name`, PascalCase `name`, descriptive filename). I clustered "filename convention" loosely but kept "kebab-case id matches filename stem" and "CamelCase/PascalCase name field" separate because they make mutually incompatible claims about the `name` field.
- **"Open with role/primary goal statement"** merges opus's "one-line role statement" with haiku's "state single primary goal at top". Could arguably be two rules; I merged on shared intent.
- **"Use consistent terminology/tone"** merges haiku's two style rules (neutral tone; consistent terminology) with grok's "consistent professional language". Split finely these are 2–3 rules.
- **gpt-5 safety sub-rules** (dry-run, commit-preview, network default off, allowed_domains, deny wildcard domains, files_denylist) are unique to gpt-5 and kept as separate rows rather than collapsed into one "safety hardening" megarule, because they're mechanically distinct checks.
- **"Include examples"** merges gpt-4o-mini's "documentation on usage and examples", opus's "at least one concrete example", and haiku's "one minimal example". gemini gestures at few-shot examples in reasoning but doesn't state a rule, so not counted.
- **"Versioning/changelog"** merges gpt-5's Changelog section, haiku's version-bump rule, and grok's "version in filenames". The deprecation rule (haiku) is kept separate since it's a distinct mechanism.