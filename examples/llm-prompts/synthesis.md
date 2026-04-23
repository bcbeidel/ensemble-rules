# Synthesis of LLM Prompt Best Practices

## 1. Consensus Rules

### Structure & Organization

- **Store prompts as version-controlled files, not inline strings or database rows.** Enables review, diffing, rollback, and treats prompts as durable engineering artifacts. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Use consistent, ordered sections (Role/Goal, Context, Constraints, Output Format, Examples).** Predictable structure makes prompts scannable and maintainable. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **State an explicit goal/task as the first content in the prompt.** A stated goal is the reference point for all downstream decisions. *(substantively similar across GPT-5, Claude Haiku, Gemini, Grok)*

- **Isolate variable/user content with explicit delimiters and a consistent placeholder syntax.** Reduces injection risk and clarifies substitution. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Use a real templating engine (Jinja, Handlebars, etc.) rather than string concatenation or f-strings.** String concatenation produces injection bugs and malformed prompts. *(raised by Claude Opus and Gemini; substantively similar)*

### Output Contract

- **Specify the output format with a concrete schema, grammar, or literal example — never prose alone.** Prose-only format specs fail unpredictably and cause parsing errors downstream. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Use the provider's native structured-output / JSON-mode / tool-calling feature when available.** More reliable than instructing the model in English. *(raised by GPT-5 and Claude Opus, substantively similar)*

- **Instruct the model to return only the specified output, with no conversational filler or markdown fences.** Simplifies downstream parsing. *(substantively similar across GPT-5, Claude Opus, Gemini)*

- **Define an explicit error/refusal/abstention path with a fixed shape.** Standardizes failure modes and prevents hallucinated answers when inputs are insufficient. *(substantively similar across GPT-5, Claude Haiku, Grok)*

### Style

- **Write instructions in short, imperative, active-voice sentences.** Matches instruction-tuned model training and reduces ambiguity. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*

- **Delete filler, politeness, and narrative preamble ("please," "kindly," "you are a world-class expert").** Tokens cost money and filler has negligible measurable effect on frontier models. *(substantively similar across Claude Opus, Claude Haiku, Grok; flagged contested by Claude Opus)*

- **Use consistent terminology for the same entity throughout a prompt.** Terminology drift confuses models and increases hallucination. *(substantively similar across GPT-5, Claude Haiku)*

### Safety

- **Treat all retrieved context, tool outputs, and user input as untrusted data, not instructions.** The system prompt is not a security boundary; injection is not solved by prompting alone. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Never embed secrets, API keys, or credentials in prompt templates.** Prompts are logged, cached, and sometimes leaked in error traces. *(substantively similar across Claude Opus, Claude Haiku, Gemini, Grok)*

- **Include an explicit refusal/safety policy for the task's sensitive categories.** Defense-in-depth; enables auditing and compliance. *(substantively similar across GPT-5, Claude Haiku, Gemini, Grok)*

### RAG

- **Separate retrieved context from instructions using explicit delimiters; require abstention when evidence is absent.** Prevents injection and hallucination. *(substantively similar across GPT-5, Claude Haiku, Gemini)*

- **Require citations with stable source identifiers for any sourced claim.** Enables auditability. *(raised by GPT-5 and Claude Haiku)*

### Performance & Cost

- **Set explicit length budgets (max_tokens, item counts, or token limits).** Runaway generations are a cost and latency bug. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*

- **Be as concise as possible without sacrificing clarity or necessary constraints.** Reduces token cost and latency; each instruction must earn its place. *(substantively similar across GPT-5, Claude Opus, Gemini, Grok)*

- **Use few-shot examples sparingly — only when format is non-obvious or empirically justified.** Examples inflate cost, bias content, and don't always help on frontier models. *(substantively similar across GPT-5, Claude Opus, Claude Haiku; all flag contested)*

### Testing & Versioning

- **Maintain a fixed evaluation set (golden cases) checked into the repo and run it on every change.** Without an eval set, every change is vibes-based. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

- **Version prompts with semver and maintain a changelog.** Downstream systems depend on specific versions; rollback and debugging require history. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

- **Pin model name and version in frontmatter and in recorded eval results.** Floating aliases change behavior; results are meaningless without a pinned model. *(raised by Claude Opus; GPT-5 implies via `model_targets`)*

## 2. Strong Minority Rules

- **Place static content first and variable content last to maximize prefix-cache hit rates.** *(Claude Opus only.)* Kept because it is a concrete, provider-supported optimization with measurable (~90%) cost impact on cached tokens — a specific, actionable mechanism that the other models gesture at only vaguely.

- **Set temperature to 0 for extraction, classification, and structured-output tasks.** *(Claude Opus only.)* Kept because determinism is a common source of flaky evals and the rule is crisp and mechanically checkable.

- **Do not add "think step by step" to prompts targeting reasoning-tuned models (o1, o3, R1, Claude extended thinking).** *(Claude Opus only.)* Kept because it is a specific, current correction to cargo-culted CoT advice and avoids a real regression on modern models.

- **Declare every template variable with a type and description in frontmatter.** *(Claude Opus; partially GPT-5 and Gemini.)* Kept because it enables the variable-AST check below and catches silent breakage at the template-call boundary.

- **Put the primary instruction before large context blocks.** *(Gemini, Claude Opus implied via "lost in the middle.")* Kept because it maps to a measurable model behavior (attention at start/end) and is cheap to apply.

- **Cover edge cases in few-shot examples, not the happy path.** *(Claude Opus only.)* Kept because models infer happy paths; this refines the generic "use few-shot sparingly" consensus.

- **Document inputs, outputs, and known failure modes in frontmatter or an adjacent README.** *(Claude Opus, Claude Haiku, GPT-5.)* Kept because presence-of-documentation is checkable and the artifact is often the only context the next engineer will have.

## 3. Divergences

### Prompt length limits
- **GPT-5:** Set explicit length budgets; no absolute number.
- **Claude Opus:** Recommends <500 tokens unless evidence justifies more (flagged contested).
- **Grok:** Prescribes <500 tokens as a hard rule.
- **Others:** Silent or "concise."
- **Synthesis:** Require an explicit length budget (consensus), but make absolute thresholds project-configurable. A hardcoded 500-token limit is too aggressive for legitimate RAG/agentic prompts. Recommend budget + waiver pattern from Claude Opus.

### Markup style: XML vs Markdown
- **Gemini:** Advocates XML-style tags for rigidity and parse clarity.
- **Claude Opus:** Either works on Claude 3.5+; pick one per project and be consistent.
- **Claude Haiku, GPT-5, Grok:** Agnostic; emphasize consistency.
- **Synthesis:** Adopt Claude Opus's position — pick one style per project and enforce consistency. XML has a slight edge for untrusted-input isolation because tag names are less likely to collide with content.

### Chain-of-thought prompting
- **Gemini:** Use CoT for complex reasoning tasks (flagged contested).
- **Claude Opus:** Never on reasoning-tuned models; for others, isolate in a delimited region.
- **GPT-5:** Prefer not in user-facing output; structured rationale field if needed.
- **Synthesis:** Default to no CoT on reasoning-tuned models; for non-reasoning models, use a dedicated `<thinking>` block or separate `rationale` field distinct from the final answer. Do not mix reasoning into user-visible output.

### Negative vs positive instructions
- **Gemini:** Prefer positive ("Do X") over negative ("Don't Y") as a general rule.
- **Claude Opus:** Use negative constraints only for observed failures — speculative prohibitions can prime the forbidden behavior.
- **Synthesis:** Claude Opus's position is more precise and better reasoned. Keep negative instructions but require they be tied to a documented failure mode.

### RFC 2119 keywords (MUST/SHOULD/MAY)
- **GPT-5:** Recommends, flagged contested.
- **Others:** Silent.
- **Synthesis:** Optional project-level convention; do not elevate to universal rule. The underlying intent (unambiguous priority) is served by the consensus "imperative voice" rule.

### Clarifying questions
- **GPT-5:** At most 2 clarifying questions before answering (flagged contested).
- **Others:** Silent or prefer explicit error path.
- **Synthesis:** Prefer the error/refusal path (consensus) over clarifying questions for non-conversational prompts. Clarifying questions are appropriate for interactive assistants; make this a conditional, not universal, rule.

## 4. Notable Omissions

- **GPT-4o-mini omits nearly all consensus rules.** Its output is substantially less specific than the other four responses — no versioning, no structured output schemas, no eval sets, no delimiter isolation, no templating, no RAG-specific guidance. The response reads as generic advice rather than engineering practice. Weight its signal accordingly.

- **Gemini omits versioning, changelog, and eval-set rules** that appear in GPT-5, Claude Opus, and Claude Haiku. Surprising given its "prompts as code" framing — the logical extension to test suites and semver is missing.

- **Grok omits prompt injection / untrusted-input isolation as a safety boundary concept.** It mentions "prompt injection risks" in passing but does not articulate the core rule that system prompts are not security boundaries.

- **GPT-4o-mini and Grok both omit the structured-output / JSON-mode feature recommendation.** This is a concrete, high-impact rule the stronger responses converged on.

- **GPT-5, Gemini, and Grok omit `max_tokens` enforcement at the call site** that Claude Opus flags. Given its concrete cost/latency impact, this is a notable gap.

- **Only Claude Opus addresses prefix caching.** Given it's supported across Anthropic, OpenAI, and Gemini and cuts costs ~90% on cached tokens, the omission by Gemini is particularly conspicuous.

## 5. Shared Deterministic Checks

### Shared Checks (Multiple Models)

- **Check** — Verify the prompt file contains an explicit, labeled goal/task statement near the top.
  - **Signal** — Raw prompt source file.
  - **Tool candidate** — ad-hoc (regex over first N lines for `^(Goal|Task|Objective|Purpose):` or imperative action verbs).
  - **Raised by** — Claude Haiku, Grok, GPT-5 (via required section ordering).
  - **Variance** — Claude Haiku adds a sentence-length cap (≤20 words, single sentence); Grok uses action-verb regex on the first sentence; GPT-5 requires a named section. Substance agrees: "a goal exists and is at the top."

- **Check** — Verify required sections are present and appear in the canonical order (Role/Goal, Context, Constraints, Output Format, Examples).
  - **Signal** — Raw source file; extracted Markdown headings or XML tags.
  - **Tool candidate** — ad-hoc markdown AST parser (e.g., `remark`, `markdown-it`).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5's canonical list is longer (includes Non-Goals, Safety, Tests); Claude Opus treats missing sections as allowed but reordering as a violation; Claude Haiku checks specific section labels exist when certain keywords appear in the body. Converge on "order is enforced, presence is section-specific."

- **Check** — Verify template variables use a consistent placeholder syntax and every referenced variable is declared.
  - **Signal** — Raw source file + frontmatter + template AST.
  - **Tool candidate** — Jinja2 / Handlebars parser for variable extraction; regex for syntax conformance.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — GPT-5 requires `{{UPPER_SNAKE}}` and an allowlist; Gemini requires uppercase snake_case via regex; Claude Opus requires declared `type` and `description` for each variable. Agree on substance; differ on declaration strictness.

- **Check** — Verify the output-format section contains a schema or fenced code-block example, not prose only.
  - **Signal** — Raw source file; fenced code-block detection; optional JSON Schema validation.
  - **Tool candidate** — `ajv` / `jsonschema` for schema validation of any JSON example against the declared schema.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 requires both a schema and a compliant example and validates one against the other; Claude Opus and Claude Haiku require at least one of schema/example. GPT-5's check is stricter.

- **Check** — Verify an error/refusal path exists in the schema and is referenced in an Error Handling section.
  - **Signal** — Raw source file + parsed output schema.
  - **Tool candidate** — JSON Schema validator + ad-hoc regex on section headings.
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — GPT-5 specifies acceptable shapes (`oneOf` branch with `error`, or `error` object with `code`/`message`); Claude Haiku only checks for a Safety/Constraints section when refusal verbs appear. Substance agrees on "refusal path must exist and be documented."

- **Check** — Verify untrusted-input variables are wrapped in explicit delimiters.
  - **Signal** — Raw source file; allowlist of variable names treated as untrusted.
  - **Tool candidate** — ad-hoc regex; requires project-config allowlist.
  - **Raised by** — Claude Haiku, Gemini.
  - **Variance** — Claude Haiku checks for any delimiter pattern (`<USER_INPUT>`, `[USER_INPUT]`, `{{USER_INPUT}}`); Gemini specifically requires XML-style encapsulation (`<query>{{VAR}}</query>`). Gemini is stricter.

- **Check** — Scan prompt files for leaked secrets (API keys, tokens, private keys).
  - **Signal** — Raw source file.
  - **Tool candidate** — `gitleaks`, `trufflehog`, or `detect-secrets`.
  - **Raised by** — Claude Opus, Claude Haiku.
  - **Variance** — None substantive. Both name industry-standard scanners and acknowledge false positives via pragma comments.

- **Check** — Verify prompt length is under a configured token budget.
  - **Signal** — Rendered prompt text piped through a tokenizer.
  - **Tool candidate** — `tiktoken` (OpenAI), provider SDK tokenizers, or a shared tokenizer library.
  - **Raised by** — Claude Opus, Grok.
  - **Variance** — Grok hard-codes 500; Claude Opus makes it configurable with a `size_waiver` escape hatch. Opus's version is more usable.

- **Check** — Verify each prompt file has a valid semver version, either in the filename or frontmatter.
  - **Signal** — Filename; YAML frontmatter.
  - **Tool candidate** — semver regex (standard: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)`); YAML parser.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 requires it in YAML frontmatter only; Claude Opus accepts filename-embedded version; Claude Haiku accepts either git tags or frontmatter. Opus/Haiku are more flexible.

- **Check** — Verify each prompt has a matching eval/test file with a minimum number of cases.
  - **Signal** — Repository file layout; eval file contents.
  - **Tool candidate** — ad-hoc directory convention; JSONL/YAML parser.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 requires at least one golden case; Claude Opus requires ≥20; Claude Haiku requires 5–10. Adopt a configurable minimum; the concept is unanimous.

- **Check** — Verify material edits to a prompt are accompanied by a version bump and a changelog entry.
  - **Signal** — Git diff + frontmatter `version` + changelog file.
  - **Tool candidate** — ad-hoc pre-commit hook.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — All three agree on substance. Differ on whether the check lives in CI or pre-commit.

### Singleton Checks (Generally Useful)

- **Check** — Verify prompts targeting reasoning-tuned models do not contain "think step by step" or equivalent CoT phrases.
  - **Signal** — Frontmatter `model` field + body regex.
  - **Tool candidate** — ad-hoc regex with maintained model allowlist.
  - **Raised by** — Claude Opus.

- **Check** — Verify call sites passing structured-output prompts use the provider's JSON-schema / tool-calling response_format.
  - **Signal** — Source code AST at LLM call sites + prompt frontmatter `output_type`.
  - **Tool candidate** — language-specific AST linter (e.g., `ruff` custom rule, ESLint plugin).
  - **Raised by** — Claude Opus.

- **Check** — Verify every LLM client call has an explicit `max_tokens` / `max_output_tokens` argument.
  - **Signal** — Source code AST at LLM call sites.
  - **Tool candidate** — language-specific AST linter.
  - **Raised by** — Claude Opus.

- **Check** — Verify eval result artifacts record pinned, dated model IDs rather than floating aliases.
  - **Signal** — Eval result JSON/JSONL.
  - **Tool candidate** — ad-hoc JSON schema validator + regex (reject `gpt-4o`, `claude-3-5-sonnet-latest`; require dated suffix).
  - **Raised by** — Claude Opus.

- **Check** — Verify prompts declaring agentic/tool use include a declared `MAX_TOOL_CALLS` cap and per-tool JSON Schema.
  - **Signal** — Raw source file; fenced JSON tool definitions.
  - **Tool candidate** — JSON Schema validator + regex.
  - **Raised by** — GPT-5.

- **Check** — Verify prompts mixing Markdown and XML section headers violate a project-declared style.
  - **Signal** — Raw source file + project config.
  - **Tool candidate** — ad-hoc regex (ignoring content inside fenced code blocks).
  - **Raised by** — Claude Opus.

- **Check** — Verify prompts do not contain filler phrases from a configurable denylist ("please," "kindly," "world-class expert").
  - **Signal** — Raw source file.
  - **Tool candidate** — ad-hoc regex denylist.
  - **Raised by** — Claude Opus (flagged contested).

- **Check** — Verify average/max sentence length in the instruction body stays under configured thresholds.
  - **Signal** — Sentence-tokenized prompt body.
  - **Tool candidate** — ad-hoc (NLTK/spaCy sentence tokenizer + word count).
  - **Raised by** — Claude Haiku, GPT-5. (Borderline shared; listed as singleton because thresholds differ significantly: Haiku 20 avg / 40 max, GPT-5 20 avg / 30 max.)

---

## 6. Final Rules File

# LLM Prompt Rules

**Scope:** User-facing prompts in production systems — coding assistants, content generation, RAG, and agentic workflows. Prompts are treated as version-controlled code.
**Audience:** Engineers and AI coding assistants authoring, reviewing, or modifying prompts.

## Structure & Organization

- **Store every production prompt as a file in version control.** Prompts edited via admin UIs cannot be reviewed, diffed, or rolled back.
- **Give each prompt a stable ID and semantic version in filename or YAML frontmatter.** Enables pinning, A/B testing, and rollback.
- **State an explicit goal as the first content in the file.** A stated goal is the reference point for all downstream decisions.
- **Organize the body in a consistent order: Role, Context, Task, Constraints, Output Format, Examples.** Sections may be omitted; reordering is not allowed.
- **Place the primary instruction before large context blocks.** Models attend better to the start and end of a prompt; buried instructions are ignored.
- **Place static content first and variable content last.** Maximizes provider prefix-cache hit rates (~90% cost reduction on cached tokens).
- **Use a real templating engine (Jinja2, Handlebars, or equivalent) for variable interpolation.** String concatenation and f-strings cause injection bugs and malformed prompts.
- **Use a consistent `{{UPPER_SNAKE_CASE}}` placeholder syntax.** Clearly separates static instructions from dynamic, injected data.
- **Declare every template variable in frontmatter with a type and description.** Undocumented variables cause silent breakage when callers change.

## Output Contract

- **Specify the output format as a JSON Schema, grammar, or literal fenced example — never prose alone.** Prose-only specs fail unpredictably.
- **Use the provider's structured-output, JSON-mode, or tool-calling feature when output is structured.** Format enforcement is more reliable than English instruction-following.
- **Pin a single output format per prompt; do not offer the model a choice.** Branching output shapes double downstream parsing complexity.
- **Instruct the model to return only the specified output, with no conversational filler or markdown fences.** Simplifies downstream parsing.
- **Define an explicit error/refusal/abstention path with a fixed shape** (e.g., `{ "error": { "code": "...", "message": "..." } }` or a `oneOf` discriminator). Standardizes failure and prevents hallucinated answers.

## Style

- **Write instructions as short, imperative, active-voice sentences.** Matches instruction-tuned model training and reduces ambiguity.
- **Use consistent terminology throughout a prompt.** Referring to the same entity as both "document" and "text" confuses the model.
- **Delete filler and narrative preamble.** "Please," "kindly," and "you are a world-class expert" cost tokens without measurable benefit on frontier models.
- **Use Markdown or XML section headers consistently within a project; do not mix.** Either works; inconsistency wastes reader attention.
- **Use negative constraints ("do NOT do X") only for observed failure modes.** Speculative prohibitions waste tokens and sometimes prime the forbidden behavior.

## Safety

- **Treat all retrieved documents, tool outputs, and user input as untrusted.** The system prompt is a behavioral hint, not a security boundary. Prompt injection is not solved by prompting.
- **Wrap untrusted input in explicit delimiters** (e.g., `<user_query>{{USER_QUERY}}</user_query>`) and label it as untrusted in the surrounding instructions.
- **Enforce authorization, PII redaction, and data scoping outside the model.** The model cannot reliably gatekeep what it can see.
- **Never embed secrets, API keys, or internal URLs in prompt templates.** Prompts get logged, cached, and leaked in error traces.
- **Include a task-specific safety/refusal policy enumerating disallowed content.** Explicit documentation enables auditing and compliance.

## RAG

- **Separate retrieved context from instructions using explicit delimiters** (e.g., `<context>...</context>`), placed after the instruction body.
- **Instruct the model to abstain ("insufficient evidence") when sources do not support an answer,** returning the error/refusal shape.
- **Require citations with stable source identifiers and spans for any sourced claim.** Enables auditability.
- **Forbid following instructions found inside retrieved documents.** Injection resistance.

## Reasoning & Chain-of-Thought

- **Do not add "think step by step" to prompts targeting reasoning-tuned models** (o1, o3, DeepSeek-R1, Claude extended thinking). Redundant at best, harmful at worst.
- **When eliciting reasoning on non-reasoning models, isolate it in a delimited region or a separate schema field** distinct from the final answer. Prevents reasoning from leaking into parsed output.

## Performance & Cost

- **Set an explicit length budget** (token or item count) in the prompt, with a project-configurable maximum and a waiver mechanism for justified exceptions.
- **Be as concise as possible without sacrificing clarity or constraints.** Each instruction must earn its token cost.
- **Use few-shot examples sparingly** — only when output format is non-obvious, the task is narrow, or examples are empirically justified against an eval set. 0–2 examples is the default; cover edge cases, not the happy path.
- **Set `max_tokens` (or provider equivalent) explicitly on every call.** Runaway generations are a cost and latency bug.
- **Set temperature to 0 for extraction, classification, structured-output, and code-generation tasks.** Non-zero temperature on deterministic tasks produces flaky evals and flaky production.

## Agentic & Tool Use

- **Declare each allowed tool with name, description, and a JSON Schema for parameters.** Disallow tools not listed.
- **Set a `MAX_TOOL_CALLS` cap per turn and stop with an error if exceeded.** Bounds cost and prevents loops.
- **Define state-transition logic and termination conditions explicitly** for multi-step or agentic workflows. Implicit loops are hard to debug.

## Testing & Versioning

- **Maintain a fixed evaluation set (at least ~20 cases per prompt, threshold configurable) checked into the repo.** Without an eval set, every change is vibes-based.
- **Re-run the eval on every prompt change; block merges on regressions.** Prompts regress silently; CI is the only defense.
- **Pin model name and dated version** (e.g., `gpt-4o-2024-11-20`, not `gpt-4o`) in frontmatter and in recorded eval results. Floating aliases make results meaningless.
- **Use semantic versioning** (major on output-format or goal change; minor on instruction clarification; patch on typos).
- **Require a changelog entry for every material change to a prompt.** Rationale matters more than the text diff.

## Documentation

- **Document purpose, inputs, outputs, and known failure modes in frontmatter or an adjacent README.** The next engineer needs this; so do you in six months.