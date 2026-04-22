# Synthesis of Agent Skills Best Practices

## 1. Consensus Rules

### Structure & Metadata

- **Include explicit frontmatter/metadata with name, description, and when-to-use triggers at the top of every SKILL.md.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Metadata drives skill selection; if selection fails, nothing else matters.
- **Enforce a consistent section ordering across all skills (name, trigger, preconditions, steps, validation, etc.).** *(substantively similar across GPT-5, Claude Haiku, Grok, GPT-4o-mini)* — Consistency reduces cognitive load for both humans and parsers.
- **Use a clear, action-oriented naming convention (verb-noun, kebab-case).** *(substantively similar across Claude Opus, Gemini, GPT-5)* — Communicates action and outcome at a glance; aids predictable resolution.

### Scope & Granularity

- **One skill = one workflow/outcome; split composite workflows into separate skills.** *(substantively similar across Claude Opus, Claude Haiku, Gemini, GPT-5)* — Composite skills degrade selection accuracy, bloat context, and harm reusability.

### Triggering & Selection

- **Write "when to use" with concrete, specific trigger phrases — not vague domain labels.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Vague descriptions cause mis-selection or over-triggering.
- **Include an explicit "when NOT to use" section with negative triggers.** *(substantively similar across GPT-5, Claude Opus)* — Prevents over-firing on adjacent tasks.

### Preconditions & Inputs

- **State all preconditions, required tools, permissions, and inputs explicitly upfront.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)* — Models do not reliably infer context; missing preconditions are a top cause of silent failure.
- **Validate prerequisites in the earliest possible step (fail fast).** *(substantively similar across GPT-5, Claude Haiku, Gemini)* — Avoids wasted work and degraded user trust.

### Steps & Instructions

- **Write steps as numbered, atomic, imperative actions — one action per step.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Atomic imperatives enable precise failure diagnosis and are executed rather than ignored.
- **Prefer exact commands and parameters over descriptions of commands.** *(substantively similar across Claude Opus, Claude Haiku, Gemini)* — `pytest -q` beats "run the tests"; specificity prevents improvisation.
- **Forbid hedging/vague language ("maybe", "try", "use best judgment").** *(substantively similar across Claude Opus, Claude Haiku, Gemini, Grok)* — Ambiguity compounds across steps; agents execute, they don't improvise.

### Validation & Correctness

- **End every skill with an explicit, machine-checkable validation step.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)* — Without one, models over-report success on no-ops.
- **Declare expected postconditions/success criteria (exit codes, files, HTTP status).** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)* — Gives the agent an objective target.
- **Prefer idempotent steps; explicitly flag any that are not.** *(substantively similar across GPT-5, Claude Opus, Gemini)* — Retries are common; non-idempotency causes duplication or wedged state.

### Error Handling

- **Every step touching external systems must declare error detection and recovery behavior.** *(substantively similar across GPT-5, Claude Haiku, Gemini, Grok, GPT-4o-mini)* — Silent failures are the dominant cascading-error source.
- **Fail loudly and surface errors rather than silently continuing with invalid state.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)* — Improvised recovery masks real failures.

### Safety

- **Never embed secrets, credentials, or tokens in skill text; reference them by handle/env var.** *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)* — Skills are shared, mirrored, and logged.
- **Require an explicit confirmation/dry-run step before any destructive or irreversible action.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — The latency is cheap; irreversible mistakes are not.
- **Apply principle of least privilege; state minimum required permissions.** *(substantively similar across GPT-5, Claude Opus, Gemini)* — Limits blast radius of a faulty skill.
- **Enumerate destructive operations in a dedicated Danger/Safety section.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku)* — Makes guardrails visible at selection and review time.

### Maintainability

- **Assign an explicit owner/maintainer and include a "last verified" date with tested versions.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)* — Skills rot as tool APIs change; staleness must be legible.
- **Store skills in version control alongside the code they operate on.** *(substantively similar across GPT-5, Claude Opus)* — Drift between code and skill is the dominant decay mode.
- **Document known limitations, edge cases, and incompatibilities.** *(substantively similar across Claude Haiku, Claude Opus, Gemini)* — Sets realistic expectations.

### Performance & Brevity

- **Cap SKILL.md length (target ~100–300 lines; hard ceiling ~500) and use progressive disclosure for reference material.** *(substantively similar across GPT-5, Claude Opus, Grok)* — Every loaded skill competes with task context for tokens.
- **Reference external scripts, schemas, and long examples rather than embedding them inline.** *(substantively similar across GPT-5, Claude Opus, Grok)* — Lazy loading is the core performance lever.
- **Do not duplicate content already in system prompts or tool descriptions.** *(raised by GPT-5, Claude Opus)* — Duplication wastes context and creates contradictions.

### Style

- **Use clear, active, simple language with consistent terminology; avoid synonyms for key entities.** *(substantively similar across GPT-5, Claude Haiku, Grok, GPT-4o-mini)* — Stable terms reduce confusion for both audiences.
- **Use code blocks for commands and configuration; don't embed code in prose.** *(raised by Claude Haiku, Gemini)* — Improves scannability and copy-paste fidelity.

---

## 2. Strong Minority Rules

- **Include 3–7 concrete trigger phrases in `when_to_use`, and re-test selection when the description changes.** *(Claude Opus)* — Models match on surface form more than intent; small wording shifts materially change routing behavior. Kept because it operationalizes the "specific triggers" consensus with a testable heuristic.
- **List overlapping sibling skills by name and explain the boundary.** *(Claude Opus)* — Prevents silent mis-selection between near-neighbors. Closely related to GPT-5's "mutually exclusive relationships" point and worth including.
- **Provide an offline/mocked test mode and gate release on passing routing tests.** *(GPT-5)* — Testing discipline is underdeveloped in most inputs but is essential for skill reliability at scale.
- **Emit structured telemetry (start, step transitions, retries, exit) with a correlation ID.** *(GPT-5)* — Observability is largely absent from other responses but critical for debugging agent workflows in production.
- **Isolate skill work in a temporary directory and clean up artifacts in the final step.** *(Gemini, GPT-4o-mini)* — State contamination between skills is a real and under-discussed failure mode.
- **Prefer structured command outputs (JSON, exit codes, flags) over parsing stdout.** *(Gemini)* — Brittle screen-scraping is a top cause of skill decay; worth explicit callout.
- **Sanitize parameter substitution to prevent command injection.** *(Gemini)* — Security concern that goes beyond generic "safety" rules.
- **Delete or archive skills that haven't been invoked in ~90 days.** *(Claude Opus, GPT-5)* — Dead skills pollute selection; explicit pruning guidance is rare but valuable.
- **Sanitize untrusted retrieved content before it enters prompts or tool calls.** *(GPT-5)* — Prompt injection via RAG content is a serious threat underrepresented in other responses.
- **Do not make skills interactive mid-execution; gather all inputs up front.** *(Gemini)* — Important operational constraint that prevents common hang scenarios.

---

## 3. Divergences

### Divergence 1: Where should error handling and retry logic live?

- **Skill-side** (Claude Haiku, Grok, GPT-4o-mini): Skills should include timeout, retry, and recovery logic for resilience.
- **Agent-side** (Gemini, Claude Opus): Skills should fail fast and report specific errors; the agent's planner decides whether to retry, substitute, or escalate. Gemini explicitly argues skills are "hands," the agent is "brain."
- **Hybrid** (GPT-5): Bounded retries with backoff per step, but fail closed on ambiguity and surface errors for agent escalation.

**Recommendation:** Adopt the hybrid position. Skills should declare *classification* of errors (transient vs. permanent), set *bounded* retry caps with backoff for clearly transient conditions (e.g., network blips), and otherwise fail fast with structured error output for the agent to handle. Embedding complex recovery logic inside skills reduces reusability and makes them harder to reason about, but zero retry guidance causes avoidable flakiness.

### Divergence 2: Inline examples vs. external references

- **Minimal or zero inline** (Claude Opus, GPT-5, Grok): Examples bloat context and drift; keep one minimal example, move the rest out.
- **Inline encouraged** (GPT-4o-mini, Claude Haiku, Gemini): Examples anchor intent and improve adoption.

**Recommendation:** At most one minimal inline example demonstrating the happy path; longer/edge-case examples live in sibling files the skill instructs the agent to read on demand. This balances context economy against the real pedagogical value of examples.

### Divergence 3: Strict output schemas for all skills

- **Pro** (GPT-5): Machine-checkable JSON schemas enable validation, composition, and testing.
- **Con/contextual** (Claude Opus, Claude Haiku): Strict schemas for human-facing skills reduce readability; apply selectively.

**Recommendation:** Require strict output schemas for programmatic skills whose output feeds other skills or tools. For human-facing skills, specify a concise output *style* rather than a rigid schema.

### Divergence 4: Voice — imperative procedure vs. second-person to the model

- **Neutral imperative** (Claude Opus, Gemini): "Run the migration" reads the same to humans and models; avoids anthropomorphic drift.
- **Second-person to model** (GPT-5, Grok, implied by several others): "You will…" is acceptable or expected.

**Recommendation:** Default to neutral imperative for procedure steps; reserve second person ("You must confirm…") for safety warnings and confirmations where attention matters. This is genuinely contested; either is defensible if consistent within a team.

### Divergence 5: Skill length cap

- Claude Opus: ~500 lines max, target 100–200.
- GPT-5: under 300 lines.
- Grok: under ~500 words.
- Others: no explicit cap.

**Recommendation:** Target 100–300 lines; treat >500 lines or >2k tokens as a code smell warranting a split. The specific number matters less than the discipline of measuring and justifying size.

### Divergence 6: Versioning requirements

- **SemVer for shared skills, git history for repo-local** (Claude Opus): Context-dependent.
- **Version every change with a changelog** (GPT-5): Universal.
- Others: largely silent.

**Recommendation:** Follow Claude Opus's graduated approach. Published/shared skills need SemVer and a changelog; repo-local skills can rely on git history plus a "last verified" date.

---

## 4. Notable Omissions

- **GPT-4o-mini omits nearly all skill-specific guidance.** Its rules read as generic code-style advice (line length, camelCase, lazy loading) and miss the defining features of skills: triggers, when-to-use, when-NOT-to-use, validation steps, selection precision, and progressive disclosure. This is the most conspicuous omission in the set and suggests the model didn't engage with the Agent Skills format specifically.
- **Grok omits validation/verification as a required final step** — a point raised by every other model. Its treatment of correctness is abstract rather than operational.
- **GPT-4o-mini and Grok omit any "when NOT to use" guidance**, despite its importance for selection precision (raised by Claude Opus, GPT-5).
- **Claude Haiku omits explicit guidance on token budget / skill length**, though it emphasizes conciseness qualitatively.
- **Gemini omits explicit telemetry/observability guidance.** Given its otherwise operational framing, the absence is notable.
- **Only GPT-5 addresses prompt injection and untrusted content sanitization.** Given the security significance, this is a meaningful omission from the other four.
- **Only GPT-5 and Claude Opus address reviewing skills on upstream API change cadence.** Maintenance discipline is underweighted elsewhere.
- **Only Claude Opus explicitly forbids skills that modify other skills or the agent's system prompt.** A real governance concern absent elsewhere.

---

## 5. Final Rules File

# Agent Skills — Rules and Conventions

**Scope.** Rules for authoring `SKILL.md` files and their supporting assets: model-invocable, on-demand capability definitions consumed by AI agents.
**Audience.** Engineers authoring skills, reviewers approving them, and AI assistants generating or editing them.
**Principle.** A skill is a privileged, model-readable procedure. Write it so both a junior engineer and a competent LLM execute it identically on the first try.

---

## Structure & Metadata

- **Put `name`, `description`, and `when_to_use` in frontmatter at the top.** Metadata drives skill selection; if selection fails, nothing else matters.
- **Keep the `description` to one or two sentences naming the task, trigger patterns, and output.** Vague descriptions cause mis-selection.
- **Use a consistent section ordering across all skills: Name → Description → When to Use → When NOT to Use → Preconditions → Inputs → Steps → Validation → Rollback → Safety/Danger → Maintenance Notes.** Consistency reduces cognitive load for humans and parsers alike.
- **Name skills as `verb-noun` in kebab-case; match the directory name to the `name` field.** Clear action orientation and predictable resolution.
- **One skill = one workflow with one outcome.** Composite skills degrade selection accuracy and bloat context. Split multi-workflow skills.

## Triggering & Selection

- **List 3–7 concrete trigger phrases or task patterns in `when_to_use`.** Models match on surface form more than intent.
- **Include an explicit "When NOT to use" section with negative triggers.** Prevents over-firing on adjacent tasks.
- **List overlapping sibling skills by name and explain the boundary.** Prevents silent mis-selection between near-neighbors.
- **Never write a skill whose trigger is "any coding task" or similarly broad.** Such skills always misfire.
- **Re-test skill selection whenever you edit the description.** Small wording changes materially change selection behavior.

## Preconditions & Inputs

- **State every precondition, required tool, required permission, and environment assumption explicitly and upfront.** Missing preconditions are the top cause of silent failure.
- **Define required inputs with types, formats, required/optional flags, and defaults.** Strong typing reduces parsing errors.
- **Validate all prerequisites in the earliest possible step (fail fast).** Avoids wasted work and compute time.
- **Gather all required inputs before execution; do not prompt for user input mid-skill.** Skills must be non-interactive.

## Steps & Instructions

- **Write steps as numbered, atomic, imperative actions — one action per step.** "Run `pytest -q`." beats "run the unit tests." Atomic imperatives are executed; suggestions are ignored.
- **Prefer exact commands, paths, and parameters over descriptions of commands.** Specificity prevents improvisation.
- **Forbid hedging language: "maybe", "try to", "usually", "use best judgment".** Ambiguity compounds across steps.
- **Prefer idempotent steps; flag any non-idempotent step explicitly.** Retries are common; non-idempotency causes duplication or wedged state.
- **Prefer structured command outputs (JSON, exit codes, typed flags) over parsing stdout.** Screen-scraping is brittle and a top cause of skill decay.
- **Isolate skill work in a temporary directory and clean up artifacts in the final step.** Prevents state contamination between skills.
- **Document expected durations for steps known to exceed ~10 seconds.** Prevents premature timeouts and erroneous retries.

## Validation & Correctness

- **End every skill with an explicit, machine-checkable validation step with a pass/fail signal.** Without one, models over-report success on no-ops.
- **State the expected postcondition (files changed, services running, exit codes, HTTP status).** Gives the agent an objective target to verify.
- **Pin versions of tools, schemas, and external references where behavior depends on them.** Unpinned references rot silently.
- **Require strict output schemas (JSON) for programmatic skills whose outputs feed other skills.** Schemas enable validation, composition, and testing.

## Error Handling

- **Every step that touches external systems must specify how failure is detected and what to do on failure.** Silent failures cause cascades.
- **Fail loudly on ambiguous or invalid state rather than improvising recovery.** Improvised recovery masks real failures and corrupts state.
- **Classify errors as transient (bounded retry with backoff) or permanent (abort and surface).** Correct classification saves time without hiding real bugs.
- **On validation failure, request a specific clarification at most once, then abort.** Bounded clarification prevents loops.
- **Log structured error details without secrets; include remediation hints on abort.** Aids triage without leakage.

## Safety

- **Never embed secrets, tokens, or credentials in skill text or assets; reference them by environment variable or vault handle.** Skills are shared, mirrored, and logged.
- **Enumerate destructive operations (file deletion, force-push, DB writes, production calls) in a dedicated Danger/Safety section.** Makes guardrails visible at review and selection time.
- **Require an explicit confirmation step or dry-run before any irreversible action.** Marginal latency is cheap; a wrong `rm -rf` is not.
- **State the minimum required permissions; never use `sudo` or escalate privileges.** Least privilege limits blast radius.
- **Sanitize and parameterize any command containing variable substitution.** Prevents command injection from agent-generated or user inputs.
- **Sanitize untrusted retrieved content before it enters prompts or tool calls.** Mitigates prompt injection via RAG.
- **Forbid skills from modifying other skills or the agent's system prompt.** Self-modifying skills are unreviewable.
- **For skills touching sensitive data or production, provide a dry-run/simulation mode.** Catches bugs before damage.

## Maintainability

- **Store skills in version control alongside the code they operate on.** Drift between code and skill is the dominant decay mode.
- **Assign an accountable owner and list contact info in Maintenance Notes.** Someone must be responsible for updates.
- **Record a "last verified" date and the runtime/tool versions tested against.** Makes staleness legible.
- **Version published/shared skills with SemVer and a changelog; repo-local skills may rely on git history.** Graduated stability matching consumer expectations.
- **Review skills on the same cadence as the APIs they wrap; re-review at least quarterly.** Skill rot tracks dependency rot.
- **Archive or delete skills not invoked in ~90 days.** Dead skills pollute selection.
- **Document known limitations, edge cases, and incompatibilities.** Sets realistic expectations.
- **Do not use SKILL.md files as incident runbooks; link to separate runbooks instead.** Keeps skills focused on happy-path automation.

## Performance & Brevity

- **Target 100–300 lines per SKILL.md; treat >500 lines or >2k tokens as a code smell.** Every loaded skill competes with task context for tokens.
- **Use progressive disclosure: reference scripts, schemas, and long examples by path, and instruct the agent to read them only when needed.** Lazy loading is the core performance lever.
- **Do not duplicate content already in the system prompt or tool descriptions.** Duplication wastes context and creates contradictions.
- **Avoid embedding large JSON/YAML schemas inline; link to them.** Schemas compress poorly in attention and drift quickly.
- **Minimize network round-trips; fetch data in bulk rather than in loops where possible.** Reduces latency and failure surface.

## Style

- **Use clear, active, simple language with short sentences.** Improves adherence for both humans and models.
- **Use consistent terminology for key entities; avoid synonyms.** Stable terms reduce confusion.
- **Write procedures in neutral imperative voice ("Run the migration"); reserve second person for safety warnings and confirmations.** Reads the same to humans and models; emphasis where it matters.
- **Use code blocks for all commands and configuration; do not embed code in prose.** Improves scannability and copy-paste fidelity.
- **Include at most one minimal inline example on the happy path; move additional examples to referenced files.** Balances pedagogy against context cost.

## Testing & Observability

- **Provide at least three executable test scenarios: happy path, edge case, and failure.** Coverage catches regressions.
- **Provide an offline/mocked test mode for CI.** Enables fast iteration without hitting real systems.
- **Validate triggers against a routing test set to detect overlaps with sibling skills.** Routing tests prevent collisions.
- **Emit structured telemetry for start, step transitions, tool calls, retries, and exit, tagged with skill name and version.** Enables tracing and cohort analysis.
- **Include a stable correlation ID per run.** Simplifies cross-system debugging.

## Review Checklist (block merge if any fails)

- The `description` alone makes selection decidable. If a reviewer can't tell when it fires, neither can the model.
- A fresh agent can execute the skill end-to-end given only the stated preconditions.
- Every step has a verifiable, pass/fail outcome.
- No step requires the model to guess a command, path, or value.
- Destructive actions are gated, reversible, or explicitly confirmed.
- No secrets, credentials, or tokens appear anywhere in the skill or its assets.
- The final validation step would catch a silent no-op.