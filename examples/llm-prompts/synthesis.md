# Synthesis of LLM Prompt Best-Practices

## 1. Consensus Rules

### Structure & Organization

- **Organize prompts into explicit, named sections (goal, constraints, context, examples, output format).** *(substantively similar but differently worded across all 5 models)*
  Rationale: Explicit structure aids both human maintainers and model parsing.

- **Use delimiters (XML tags, markdown headers, or triple backticks) to separate instructions from data/context.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
  Rationale: Prevents format bleed and ambiguity between roles of content.

- **Use named placeholders (e.g., `{user_query}`, `{{variable_name}}`) for dynamic content rather than string concatenation.** *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
  Rationale: Clearly separates instructions from data and prevents injection.

- **Place primary instructions/goal at the start; restate critical constraints at the end.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
  Rationale: Models attend most to the beginning and end of prompts.

### Output Specification

- **Specify output format with a concrete schema or literal example, not prose descriptions.** *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
  Rationale: Natural-language format descriptions drift; literal schemas don't.

- **Prefer JSON / structured output / function calling when the consumer is code.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
  Rationale: Structured I/O is more reliable and reduces parsing errors.

- **Define an explicit failure/uncertainty output (e.g., "unknown", error object, refusal).** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
  Rationale: Overrides the model's default tendency to guess or fabricate.

- **Enumerate edge cases explicitly (empty input, ambiguous input, out-of-scope requests).** *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
  Rationale: The dominant failure mode is underspecification of edge behavior.

### Clarity & Instructions

- **Use direct, imperative, unambiguous language; avoid vague exhortations.** *(substantively similar across all 5 models)*
  Rationale: Specific constraints change behavior; vague ones ("be careful", "be thorough") do not.

- **Avoid contradictory instructions (e.g., "concise AND exhaustive").** *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
  Rationale: Models silently resolve contradictions in unpredictable ways.

### Safety & Input Handling

- **Treat all user input, retrieved docs, and tool outputs as untrusted data, not instructions.** *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
  Rationale: Prompt injection is the default threat model, not an edge case.

- **Explicitly tell the model that delimited user/retrieved content is data to be ignored if it contains instructions.** *(substantively similar across GPT-5, Claude Opus, Gemini)*
  Rationale: Defense in depth against injection.

- **Define refusal behavior and unsafe-content boundaries explicitly.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
  Rationale: Consistent, detectable refusals enable graceful downstream handling.

- **Never embed secrets, API keys, or PII in prompts.** *(near-identical across GPT-5, Claude Opus)*
  Rationale: Prompts leak through logs, traces, and outputs.

### Versioning & Maintainability

- **Store prompts in version control and treat them as code subject to review.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*
  Rationale: Prompts drift with model updates; they need diffs, rollback, and review.

- **Attach an evaluation/test suite to every production prompt.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
  Rationale: Prompts regress; without tests, changes are guesswork.

- **Pin the model version / decoding parameters alongside the prompt.** *(substantively similar across GPT-5, Claude Opus)*
  Rationale: Same prompt behaves differently across model versions; reproducibility requires pinning.

### Performance

- **Remove redundancy and boilerplate, but never sacrifice clarity for brevity.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
  Rationale: Tokens cost money and dilute attention, but reliability matters more than raw cost.

- **Cap output length with an explicit hard limit (tokens, words, or characters).** *(substantively similar across GPT-5, Claude Haiku)*
  Rationale: Vague "be concise" guidance doesn't constrain output reliably.

### Examples (Few-Shot)

- **Ensure examples exactly match the expected output format.** *(substantively similar across Claude Opus, Claude Haiku, Gemini)*
  Rationale: The model follows examples over instructions when they conflict.

### RAG / Context Handling

- **Label retrieved chunks with source/provenance metadata and require citation.** *(substantively similar across GPT-5, Claude Opus)*
  Rationale: Enables attribution, verification, and graceful "insufficient context" behavior.

- **Cap retrieved context to a small top-k ranked by relevance.** *(substantively similar across GPT-5, Claude Opus)*
  Rationale: More tokens dilute attention rather than adding signal.

### Agentic Workflows

- **Give agents an explicit termination condition; never allow unbounded loops.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
  Rationale: Prevents runaway cost and infinite recursion.

## 2. Strong Minority Rules

- **Exploit prompt caching by placing stable content first, volatile content last.** (Claude Opus only)
  Kept because: This is a concrete, measurable performance win on modern APIs (Anthropic, OpenAI) that the other models missed.

- **Chain multiple simple prompts instead of one mega-prompt for multi-step tasks.** (Gemini; implicit in Claude Opus)
  Kept because: Modularity and debuggability are real production concerns; this is a well-reasoned architectural principle.

- **Include a metadata header on each prompt (name, version, owner, model targets).** (GPT-5 only)
  Kept because: Concrete operational discipline that supports the consensus "prompts are code" principle.

- **Require agents to state their plan before destructive operations.** (Claude Opus only)
  Kept because: Cheap, high-leverage safety mechanism specific to agentic workflows.

- **Log every prompt, tool call, and output for agentic systems.** (Claude Opus only)
  Kept because: Non-reproducible agent failures are a well-known operational pain point.

- **Use second person ("you") for addressing the model, not third person.** (Claude Opus only)
  Kept because: Low-cost stylistic clarity rule with no apparent downside.

- **Don't use prompts to fix problems that belong in application code (parsing, validation, retries).** (Claude Opus only)
  Kept because: A critical architectural principle — overloading prompts is a common anti-pattern.

- **Review prompt diffs like code diffs; a one-word change can flip behavior on 10% of inputs.** (Claude Opus; implicit in Claude Haiku)
  Kept because: Captures the non-obvious fragility of prompt changes.

## 3. Divergences

### Persona / Role-Play Preambles ("You are an expert...")
- **Pro:** Gemini explicitly endorses role-play as low-cost context-setting.
- **Con:** GPT-5 and Claude Opus call generic personas "cargo culting" or "fluff."
- **Nuanced:** Claude Haiku says use only when persona directly shapes output.
- **Synthesis:** Skip generic "helpful assistant" framing; use concrete roles only when they demonstrably shape style/expertise in evals. The burden of proof is on the persona.

### Chain-of-Thought Reasoning
- **Skeptical:** GPT-5, Claude Opus, Claude Haiku — costly, leaks reasoning, measure before adding.
- **Neutral:** Grok mentions it improves reasoning but notes latency cost.
- **Synthesis:** Default off. Enable only when evals show a measurable accuracy lift that justifies the latency/cost.

### Few-Shot Examples: Default or Last Resort?
- **Always use examples:** Claude Haiku ("one example is almost always better than none"), Gemini ("worth a thousand words"), Grok.
- **Use sparingly:** GPT-5, Claude Opus ("use few-shot only when instructions alone fail your evals").
- **Synthesis:** Start with clear instructions + schema; add examples when (a) the task is structurally tricky, (b) evals show instruction-only prompts fail, or (c) tone/style is hard to describe. Examples are powerful but costly and anchor flaws.

### Negative Examples (showing what *not* to do)
- **Against:** Claude Haiku warns negatives can confuse the model into doing the forbidden thing.
- **For:** Gemini says "state constraints and prohibitions explicitly and negatively" works well.
- **Synthesis:** Use negative *constraints* ("Do not invent sources") freely; use negative *examples* (showing a bad output) sparingly and only for common, specific failure modes.

### Markdown vs. XML Tags
- **XML-leaning:** Claude Opus, Claude Haiku (Anthropic-native convention).
- **Markdown-leaning:** Gemini.
- **Agnostic:** GPT-5, Grok.
- **Synthesis:** Pick one and apply consistently within a prompt. Model-dependent; test both if it matters.

### Temperature / Decoding Parameters in the Prompt
- **In config:** Claude Haiku says decoding belongs in config, not prompt text.
- **Pinned with prompt:** GPT-5 says pin decoding params per version for reproducibility.
- **Synthesis:** Store decoding params in prompt *metadata* (version-pinned), not in prompt *body*. Both views are compatible.

### Single Prompt vs. Chained Prompts
- **Chaining:** Gemini favors it for complex workflows (single-responsibility principle).
- **Not discussed:** Others.
- **Synthesis:** Prefer chaining for multi-step tasks; it improves testability at the cost of latency.

## 4. Notable Omissions

- **GPT-4o-mini omits nearly everything concrete:** no prompt injection handling, no output-schema specification details, no RAG guidance, no agentic workflow rules, no model-version pinning, no eval-set requirement, no prompt caching, no templating discipline. Its rules file reads as generic platitudes ("be specific", "be concise") without the operational detail the other four models converge on. The absence is the signal: this model produced a weaker output than its peers.

- **Grok omits prompt injection as a threat model.** It mentions safety generally but does not treat untrusted-input handling or delimiting as a core discipline — a significant gap given how strongly the other four converge on it.

- **Gemini omits explicit testing/eval infrastructure rules** beyond "iterate and test." Claude Opus, Claude Haiku, GPT-5, and Grok all call out attaching eval suites as non-negotiable.

- **Claude Haiku and Grok omit prompt caching / cache-friendly ordering** — a concrete performance lever Claude Opus highlights.

- **GPT-4o-mini and Grok omit model-version pinning** — a maintainability point GPT-5 and Claude Opus treat as essential.

- **Grok omits structured output / JSON mode preference** — the other four all recommend it when the consumer is code.

---

## 5. Final Rules File

# LLM Prompt Rules

**Scope.** Durable, version-controlled prompts for coding assistants, content generation, RAG pipelines, and agentic workflows.
**Audience.** Engineers and AI coding assistants authoring or modifying production prompts.
**Principle.** Prompts are source code. Version, review, test, document, and measure them like code.

## Structure

- **Open with a one-sentence goal.** Models attend most to the start; state what must be produced up front.
- **Organize prompts into explicit, named sections** (Goal, Constraints, Context, Input Format, Output Format, Examples). Use headings or XML-style tags (`<context>`, `<user_input>`).
- **Pick one delimiter style (markdown OR XML) and apply it consistently.** Mixing confuses readers and occasionally models.
- **Place primary instructions first; restate critical constraints at the end.** Middle tokens receive the least attention.
- **Put stable content first, volatile content last.** Enables prompt caching and stable diffs.
- **Use named placeholders (`{user_query}`, `{{document}}`) for all dynamic content.** Never string-concatenate user data into instruction text.
- **Keep prompts under one screen where possible.** Long prompts hide contradictions; chain simpler prompts for multi-step tasks.

## Output Specification

- **Specify output format with a literal example or schema, not prose.** "A list of items" is ambiguous; `{"items": string[]}` is not.
- **Prefer structured output / JSON mode / function calling when the consumer is code.** Don't parse free text you could have constrained.
- **Define an explicit failure/uncertainty output** (e.g., `{"error": "...", "reason": "..."}` or a designated refusal string).
- **Enumerate edge cases explicitly**: empty input, ambiguous input, out-of-scope requests.
- **Cap output length with a hard limit** (tokens, words, or characters). Vague "be concise" does not constrain behavior.
- **Forbid hedging and conversational filler** when output is for code or UI.

## Instructions

- **Use direct, imperative language.** "Return JSON with fields X and Y" beats "It would be ideal if you could provide..."
- **Address the model in the second person** ("you"), not the third.
- **Never give contradictory instructions.** "Concise and comprehensive" resolves to whichever the model prefers today.
- **Write negative constraints, not just positive ones.** "Do not invent sources" prevents a failure mode "cite sources" does not.
- **Don't ask the model to "be careful" or "think hard."** Vague exhortations don't change behavior; specific constraints do.
- **Use chain-of-thought only when evals prove a measurable lift.** It inflates latency and cost.

## Context and RAG

- **Label every retrieved chunk with source, URL, and date metadata.** The model cannot reason about provenance it cannot see.
- **Cap retrieval to a small, relevance-ranked top-k.** More tokens dilute attention.
- **Place retrieved context after instructions and before the user query.** Keeps instructions cache-stable.
- **Instruct the model to refuse or emit "insufficient_context" when sources don't support an answer.** Override the default tendency to guess.
- **Require citation IDs for factual claims.**

## Examples (Few-Shot)

- **Start with clear instructions + schema; add examples when evals show instructions alone fail.** Examples are expensive and anchor behavior, including their flaws.
- **Make examples cover hard and boundary cases, not obvious ones.**
- **Keep example format byte-identical to the expected output.** The model follows examples over instructions on conflict.
- **Prefer positive examples over negative ones.** Use a negative example only for a common, specific failure mode.

## Safety

- **Treat all user input, retrieved docs, and tool outputs as untrusted data.** Prompt injection is the default, not the exception.
- **Delimit untrusted content and explicitly tell the model it is data, not instructions.**
- **Never rely on prompting alone for security boundaries.** Enforce tool permissions, output validation, and allowlists in code.
- **Never embed secrets, API keys, or PII in prompts.** They leak through logs, traces, and outputs.
- **Define refusal behavior explicitly** — what the model says and returns when asked to violate constraints.
- **Declare unsafe-content boundaries explicitly** (e.g., prohibit malware, unverified medical advice); use conservative examples rather than exhaustive rule lists.

## Agentic Workflows

- **Give every agent an explicit termination condition** (step limit, success criterion, or halt signal).
- **Constrain tool use with explicit allow/deny lists, input schemas, and side-effect annotations.**
- **Require the agent to state its plan before destructive operations.** Cheap insurance against confident mistakes.
- **Log every prompt, tool call, and output.** Agents fail in ways you cannot reproduce without traces.
- **On tool errors, allow bounded retries, then return a structured error.** No unbounded loops.

## Performance

- **Remove redundancy and boilerplate** — but never sacrifice clarity for brevity. A 500-token prompt that works beats a 200-token prompt that fails.
- **Exploit prompt caching: freeze the prefix; reorder so the cached portion is byte-stable.**
- **Prefer structure (JSON, function calls) over prose** — reduces decoding entropy, tokens, and latency.
- **Prefer smaller models with tighter prompts over larger models with loose ones** when evals permit.
- **Store decoding parameters (temperature, top_p) in prompt metadata, not in the prompt body.**

## Maintainability & Versioning

- **Store every production prompt in version control.** No prompts in config UIs, notebooks, or Slack.
- **Attach an eval set to every prompt.** A prompt without evals is unreviewable and unshippable.
- **Pin the model version in prompt metadata.** "Works on gpt-4o-2024-08-06" ≠ "works on gpt-4o."
- **Include a metadata header** (name, version, owner, model targets, decoding params, tool inventory).
- **Use semantic versioning and a change log.** Bump MAJOR for breaking schema/output changes.
- **Review prompt diffs like code diffs.** A one-word change can flip behavior on 10% of inputs.
- **Comment non-obvious constraints** with the *why* (e.g., `<!-- 100-word cap: mobile UI -->`).
- **Don't use prompts to fix problems that belong in application code** (parsing, validation, retries).

## Anti-Patterns

- **Don't bury the task in the middle of the prompt.**
- **Don't mix narrative output with structured output.** If both are needed, use separate fields in one top-level object.
- **Don't let user or retrieved text redefine the output schema.**
- **Don't rely on hidden model memory.** Restate necessary constraints every request.
- **Don't ship a prompt without running it on adversarial input.** If you didn't try to break it, a user will.
- **Don't use generic persona theater ("You are a world-class expert").** Use concrete roles only when evals show they shape output.

## Contested (apply with judgment)

- **Role/persona preambles:** Skip generic framing; use concrete roles only with eval support.
- **Few-shot defaults:** Opinions split between "always include an example" and "only when instructions fail." Let your evals decide.
- **Markdown vs. XML tags:** Model-dependent. Pick one per prompt and be consistent.
- **Chain-of-thought in output:** Can improve accuracy, leaks reasoning, costs tokens. Default off; enable only with evidence.