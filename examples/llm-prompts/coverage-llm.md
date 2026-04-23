## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Specify output format explicitly with a schema or concrete example. | Output Format | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Include explicit safety constraints, refusal triggers, or content policy guardrails. | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Isolate/delimit untrusted input and retrieved context; treat them as data, not instructions. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Keep prompts concise / set explicit length budgets. | Performance | ✓ | ✓ | ✓ |  |  | ✓ | 4 |
| Version-control prompt files with semantic versioning and/or a changelog. | Tooling/Maintenance | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Organize prompt with a consistent section structure (Goal, Constraints, Output Format, etc.). | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| State the goal/task explicitly and up front. | Structure | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Use short, imperative, direct instructions (no filler/politeness). | Style | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Use explicit, typed template variables / delimited placeholders for interpolation. | Structure | ✓ |  | ✓ |  | ✓ |  | 3 |
| Define an explicit error/refusal shape and failure path. | Error Handling | ✓ | ✓ |  | ✓ |  |  | 3 |
| Maintain a test/eval set and run it on prompt changes. | Evaluation/Testing | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use YAML/structured frontmatter declaring metadata (id, owner, model, purpose, etc.). | Structure | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use few-shot examples sparingly / only when justified (contested). | Examples | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use consistent terminology and style throughout the prompt. | Style |  | ✓ |  | ✓ | ✓ |  | 3 |
| Do not request/leak chain-of-thought in user-visible output; isolate reasoning. | Reasoning | ✓ |  | ✓ |  |  |  | 2 |
| Forbid embedding secrets, credentials, or PII in prompt templates. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Instruct abstention when evidence/context is insufficient (RAG fallback). | RAG/Error Handling | ✓ |  |  | ✓ |  |  | 2 |
| Use provider structured-output / tool-calling features for structured outputs. | Output Format |  |  | ✓ | ✓ |  |  | 2 |
| Declare tools/allowed actions with explicit schemas and bounded tool-call limits. | Agentic/Tool Use | ✓ |  |  | ✓ |  |  | 2 |
| Define explicit termination/state conditions for multi-turn or agentic loops. | Agentic/Tool Use | ✓ |  |  | ✓ |  |  | 2 |
| Prefer positive instructions over negative ones. | Style |  |  | ✓ |  | ✓ |  | 2 |
| Assign a clear role/persona and goal to prime the model. | Content |  |  |  |  | ✓ | ✓ | 2 |
| Place static content first and variable content last (for caching / attention). | Performance | ✓ |  | ✓ |  |  |  | 2 |
| Set explicit generation parameters (temperature, max_tokens) appropriate to the task. | Performance |  |  | ✓ |  |  |  | 1 |
| State explicit Non-Goals to prevent scope creep. | Structure | ✓ |  |  |  |  |  | 1 |
| Require citations with stable source identifiers for sourced claims. | RAG | ✓ |  |  |  |  |  | 1 |
| Keep one responsibility per prompt (single-responsibility). | Structure | ✓ |  |  |  |  |  | 1 |
| Log full prompt, parameters, and output on every invocation. | Observability |  |  |  | ✓ |  |  | 1 |
| Do not assume the LLM will correctly infer unstated user intent. | Error Handling |  | ✓ |  |  |  |  | 1 |
| State explicit assumptions / required background knowledge. | Content |  |  |  | ✓ |  |  | 1 |
| Document expected token count and latency characteristics. | Performance |  |  |  | ✓ |  |  | 1 |
| Use RFC 2119 keywords (MUST/SHOULD/MAY) for normative constraints (contested). | Style | ✓ |  |  |  |  |  | 1 |
| Keep sentences short (under ~20 words) (contested). | Style | ✓ |  |  | ✓ |  |  | 2 |
| Wrap final output in explicit begin/end markers. | Output Format | ✓ |  |  |  |  |  | 1 |
| Prohibit markdown formatting inside JSON values unless allowed. | Output Format | ✓ |  |  |  |  |  | 1 |
| Pin model name and version when recording results. | Evaluation | | | ✓ | | | | 1 |
| Use comments for human-readable notes ignored by the LLM. | Structure |  |  |  |  | ✓ |  | 1 |
| Adopt consistent file naming convention (e.g., `.prompt.md` suffix). | Tooling/Maintenance |  |  |  |  | ✓ |  | 1 |
| Sanitize untrusted input in application code before injecting into prompt. | Safety |  |  |  |  | ✓ |  | 1 |
| Instruct the model to return raw output only (no conversational filler / code fences). | Output Format |  |  |  |  | ✓ |  | 1 |
| State the instruction before large blocks of context/data. | Content |  |  |  |  | ✓ |  | 1 |
| Pin a single output format — do not offer the model a choice. | Output Format |  |  | ✓ |  |  |  | 1 |
| Use chain-of-thought for complex reasoning tasks (contested). | Reasoning |  |  |  |  | ✓ |  | 1 |
| Prefer the system prompt for enduring instructions/persona (contested). | Structure |  |  |  |  | ✓ |  | 1 |
| Test prompts for performance and response time. | Performance |  | ✓ |  |  |  |  | 1 |
| Ask at most N clarifying questions if inputs are insufficient (contested). | Error Handling | ✓ |  |  |  |  |  | 1 |

## Notes on clustering decisions

- **"Specify output format explicitly"** is a broad cluster: gpt-5, opus, haiku, and gemini all call for JSON Schema or concrete example, while 4o-mini and grok call for "specify output format" more generically. I grouped them because the substance (declare an explicit format) matches, even though rigor differs.
- **"Include explicit safety constraints"** aggregates several distinct-looking rules: gpt-5's "Safety section enumerating disallowed content," 4o-mini's "incorporate safety measures," opus's "enforce authorization externally," haiku's "document content policy," gemini's "forbid harmful content," and grok's "refusal mechanism." These could plausibly split into (a) have a safety section, (b) refusal policy, (c) external enforcement — I kept them together since each model raised at least one piece of a shared concern.
- **"Isolate/delimit untrusted input"** merges prompt-injection defense rules from gpt-5 (treat retrieved context as data), opus (delimit untrusted inputs), haiku (isolate user input in marked sections), gemini (XML tags around untrusted input), and grok (checks on tool access). Grok's is the weakest match; borderline include.
- **"Use short, imperative, direct instructions"** combines opus's "delete filler like please/kindly," haiku's "imperative mood" + "avoid narrative preamble," gpt-5's "directive voice without hedging," and grok's "active voice." Could have been split into "imperative voice" vs "no filler," but they travel together in the source material.
- **"Keep sentences short"** — I kept as a separate cluster from "short imperative" because gpt-5 and haiku explicitly quantify sentence length, whereas other "concise" rules target prompt-level length.
- **"Version-control with semver/changelog"** merges opus's "stable ID + semver + changelog," haiku's "semver tag releases + post-mortem," gemini's "version-control prompt files," and gpt-5's "version bump + CHANGELOG." 4o-mini mentions "version control principles" only in reasoning, not rules, so excluded.
- **"Organize prompt with consistent section structure"** — models disagree on the exact sections (gpt-5: Goal/Non-Goals/Inputs/...; opus: Role/Context/Task/...; haiku: Task/Context/Constraints/...; gemini: XML-tagged sections). Clustered as one rule because the substance is "use a canonical section structure," not the specific sections.
- **"Frontmatter with metadata"** is separate from "section structure" because frontmatter is machine-readable metadata (id, version, owner) rather than prompt body organization.
- **"Few-shot sparingly"** — all three (gpt-5, opus, haiku) flag this as contested and agree on "use when justified, keep small." Gemini's separate rule recommending few-shot for complex tasks is *not* included in this cluster because it pushes the opposite direction; I left it as a single-model rule under Content instead, though one could argue for merging into a contested cluster.
- **Gemini's "use chain-of-thought for complex reasoning"** and **opus's "do not add 'think step by step' to reasoning-tuned models"** are listed separately rather than as a contested cluster because they address different model classes — opus carves out reasoning-tuned models specifically while gemini speaks generally.
- **"State the goal up front"** (gpt-5, haiku, gemini, grok) vs **"Assign a role/persona"** (gemini, grok) — kept separate since role-assignment is a distinct prompt technique from stating a task goal, though they often co-locate at the top of a prompt.
- **"Error/refusal shape"** merges gpt-5's "Cannot comply path with fixed error object," 4o-mini's "explicit instructions for handling errors," and haiku's "fallback behavior if context missing." Borderline — 4o-mini's version is vaguer.
- **4o-mini's rules** are quite generic ("do use consistent tone," "don't overlook biases"); I mapped them to the nearest substantive cluster but several are thin matches.