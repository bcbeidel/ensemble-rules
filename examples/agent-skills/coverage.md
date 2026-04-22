# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Do not implement complex retry logic within a skill.** | **Error Handling & State** |  |  |  |  | ✓ |  | 1 |
| **(contested)** For destructive operations (delete, overwrite, deploy to production), include an explicit confirmation or approval step before the action | Error Handling & Recovery |  |  |  | ✓ |  |  | 1 |
| **A fresh agent can execute the skill end-to-end with no outside context.** Skills must be self-contained against their stated preconditions | Review Checklist (block merge if any fails) |  |  | ✓ |  |  |  | 1 |
| **Add a "Last verified" date and the runtime/model it was tested against.** Makes staleness legible | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Add a "When to Update This Skill" section if the underlying tool or service changes frequently.** (Signals decay risk.) | Maintenance & Ownership |  |  |  | ✓ |  |  | 1 |
| **Address the procedure, not the model ("Run the migration"), not ("You should run the migration").** (contested) Reads identically to humans and models and avoids anthropomorphic drift | Writing Style |  |  | ✓ |  |  |  | 1 |
| **Assign an owner (person or team) and contact info; list them in Maintenance Notes.** (Ensures someone is responsible for updates and bug fixes.) | Maintenance & Ownership |  |  |  | ✓ |  |  | 1 |
| **Avoid "nice to have" or optional steps; if it's optional, remove it or move it to a separate variant Skill.** (Clarity about what *must* happen.) | Style & Language |  |  |  | ✓ |  |  | 1 |
| **Avoid "try several approaches" or "use best judgment"; specify the exact sequence.** (Agents execute, they don't improvise.) | Steps |  |  |  | ✓ |  |  | 1 |
| **Avoid embedding large JSON/YAML schemas inline; link to them.** Schemas compress poorly in attention | Performance |  |  | ✓ |  |  |  | 1 |
| **Cap `SKILL.md` at ~500 lines; target 100–200.** Tokens spent on the skill are tokens not spent on the task | Structure |  |  | ✓ |  |  |  | 1 |
| **Clean up any created artifacts (temp files, environment variables) in the final step.** | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| **Define all required inputs as parameters at the start of the skill.** | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| **Delete skills that haven't been invoked in 90 days.** Dead skills pollute selection | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Destructive actions are gated and reversible or confirmed.** Non-negotiable | Review Checklist (block merge if any fails) |  |  | ✓ |  |  |  | 1 |
| **Do not ask for user input in the middle of a skill's steps.** | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| **Do not describe implementation details in the description.** | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| **Do not duplicate content already in the system prompt or tool descriptions.** Duplication wastes context and causes contradictions | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not use Skill files as incident or debugging runbooks; create those separately and link to them.** (Keeps Skills focused on happy-path automation; runbooks handle failure modes.) | Maintenance & Ownership |  |  |  | ✓ |  |  | 1 |
| **Do not use commands that require `sudo` or root privileges.** | **Safety** |  |  |  |  | ✓ |  | 1 |
| **Document any known limitations, edge cases, or incompatibilities.** (Sets realistic expectations; prevents support requests about unsupported scenarios.) | Maintenance & Ownership |  |  |  | ✓ |  |  | 1 |
| **Document any permissions or privileges required; if elevated access is needed, state it explicitly.** (Prevents privilege escalation surprises.) | Safety & Security |  |  |  | ✓ |  |  | 1 |
| **Don't assume any external system is available; always include timeout and retry logic.** (Networks fail; code that doesn't account for it will fail mysteriously.) | Error Handling & Recovery |  |  |  | ✓ |  |  | 1 |
| **Don't hardcode timeouts; parameterize them and document defaults.** (Allows tuning without editing the Skill.) | Performance & Scalability |  |  |  | ✓ |  |  | 1 |
| **Each step must be a single atomic action; don't combine conditionals, loops, or multiple commands into one step.** (Enables precise failure diagnosis and branching.) | Steps |  |  |  | ✓ |  |  | 1 |
| **End every skill with an explicit verification step with a pass/fail signal.** Models over-report success without one | Correctness |  |  | ✓ |  |  |  | 1 |
| **Ensure the skill is idempotent.** | **Error Handling & State** |  |  |  |  | ✓ |  | 1 |
| **Enumerate destructive operations (file deletion, force-push, DB writes, network calls) in a "Danger" section.** Makes guardrails visible at selection time | Safety |  |  | ✓ |  |  |  | 1 |
| **Every Skill must have exactly one outcome.** A Skill succeeds when it achieves that outcome; anything else is a separate Skill | Structure |  |  |  | ✓ |  |  | 1 |
| **Every Skill must include a final Validation section that checks whether the outcome was achieved.** (Prevents false success.) | Validation |  |  |  | ✓ |  |  | 1 |
| **Every step has a verifiable outcome.** No step should be "and then it works." | Review Checklist (block merge if any fails) |  |  | ✓ |  |  |  | 1 |
| **Every step that touches external systems (API calls, file ops, network requests) must include error detection and recovery.** State "If [condition], then [recovery action]" explicitly | Steps |  |  |  | ✓ |  |  | 1 |
| **Fail fast on unexpected outcomes or invalid state.** | **Error Handling & State** |  |  |  |  | ✓ |  | 1 |
| **Fetch data in bulk once rather than in a loop.** | **Performance** |  |  |  |  | ✓ |  | 1 |
| **For Skill steps that iterate over a collection (files, API results, etc.), specify the expected scale and any known performance cliffs.** State "Works for up to 1000 items; above that, use [alternative]." (Prevents runaway execution and timeouts.) | Performance & Scalability |  |  |  | ✓ |  |  | 1 |
| **Forbid hedging words: "maybe", "try to", "usually".** Ambiguity compounds across steps | Writing Style |  |  | ✓ |  |  |  | 1 |
| **Forbid skills from modifying other skills or the agent's system prompt.** Self-modifying skills are unreviewable | Safety |  |  | ✓ |  |  |  | 1 |
| **Give each skill a single, clear responsibility.** | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| **If a Skill can fail partially (some targets succeed, some fail), clarify whether partial success is acceptable or if the entire operation must rollback.** (Prevents inconsistent state.) | Safety & Security |  |  |  | ✓ |  |  | 1 |
| **If a Skill operates on sensitive data or makes production changes, include a dry-run or simulation step before the real action.** (Catches bugs before damage.) | Safety & Security |  |  |  | ✓ |  |  | 1 |
| **If a Skill requires authentication or credentials, explicitly name the auth mechanism and where credentials come from.** (Agents cannot guess or improvise.) | Preconditions & Context |  |  |  | ✓ |  |  | 1 |
| **If a step cannot be recovered automatically (e.g., permission denied, data loss risk), fail loudly and document the manual recovery path.** (Prevents accidental data loss and unsupervised damage.) | Error Handling & Recovery |  |  |  | ✓ |  |  | 1 |
| **If a step is intentionally slow (> 10 seconds expected), document the expected duration.** (Prevents agents from timing out or retrying prematurely.) | Steps |  |  |  | ✓ |  |  | 1 |
| **If validation fails, the Skill must clearly state whether to retry or escalate.** (Prevents infinite loops and silent hangs.) | Validation |  |  |  | ✓ |  |  | 1 |
| **Include 3–7 concrete trigger phrases or task patterns in `when_to_use`.** Models match on surface form more than intent | Triggering and Selection |  |  | ✓ |  |  |  | 1 |
| **Include a "last verified on" date and the tool/service versions tested against.** (Signals decay and incompatibility risk.) | Preconditions & Context |  |  |  | ✓ |  |  | 1 |
| **Include an explicit "When NOT to use" section.** Prevents over-triggering on adjacent tasks | Structure |  |  | ✓ |  |  |  | 1 |
| **Include at most one minimal inline example; move longer examples to a referenced file.** (contested) Long examples drift and crowd context | Writing Style |  |  | ✓ |  |  |  | 1 |
| **Instruct the agent to stop and surface errors rather than improvise recovery.** (contested) Improvised recovery masks real failures and corrupts state | Safety |  |  | ✓ |  |  |  | 1 |
| **Isolate a skill's work in a temporary directory.** | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| **Keep `description` to one or two sentences naming the task, trigger patterns, and output.** Vague descriptions cause mis-selection | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep the Trigger section under 2 sentences and use "when" language ("When you need to…").** (Agents must instantly recognize whether the Skill applies.) | Structure |  |  |  | ✓ |  |  | 1 |
| **Link to reference docs for domain concepts, but don't replicate them in the Skill itself.** (Keeps Skills scannable; documents stay single-source-of-truth.) | Preconditions & Context |  |  |  | ✓ |  |  | 1 |
| **List overlapping sibling skills by name and explain the boundary.** Prevents silent mis-selection between near-neighbors | Triggering and Selection |  |  | ✓ |  |  |  | 1 |
| **List required tools, permissions, and environment preconditions explicitly.** The model will not infer them reliably | Structure |  |  | ✓ |  |  |  | 1 |
| **Measure skill token cost; treat >2k tokens as a code smell.** Every loaded skill competes with task context | Performance |  |  | ✓ |  |  |  | 1 |
| **Minimize the number of steps and external network calls.** | **Performance** |  |  |  |  | ✓ |  | 1 |
| **Name the Skill with a verb-noun phrase ("Deploy Service," not "Service Deployment").** (Clarifies action and outcome.) | Structure |  |  |  | ✓ |  |  | 1 |
| **Name the skill directory and `name` field identically, in kebab-case.** Predictable resolution avoids loader bugs | Structure |  |  | ✓ |  |  |  | 1 |
| **Never embed secrets, tokens, or credentials in skill text or assets.** Skills are frequently shared, mirrored, and logged | Safety |  |  | ✓ |  |  |  | 1 |
| **Never write a skill whose trigger is "any coding task" or similarly broad.** Such skills always misfire | Triggering and Selection |  |  | ✓ |  |  |  | 1 |
| **No step requires the model to guess a command, path, or value.** Guessing is where incidents originate | Review Checklist (block merge if any fails) |  |  | ✓ |  |  |  | 1 |
| **Number all steps sequentially starting from 1.** | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| **Number steps sequentially; use nested numbering (1.1, 1.2) only for conditional sub-steps.** (Supports clear reference and execution order.) | Steps |  |  |  | ✓ |  |  | 1 |
| **One skill = one workflow.** Composite skills degrade selection accuracy and bloat context | Structure |  |  | ✓ |  |  |  | 1 |
| **Pin versions of tools, schemas, and external references where behavior depends on them.** Unpinned references rot silently | Correctness |  |  | ✓ |  |  |  | 1 |
| **Preconditions are mandatory; list every assumption about state, tooling, permissions, and access required.** (Prevents silent failures from unmet prerequisites.) | Preconditions & Context |  |  |  | ✓ |  |  | 1 |
| **Prefer exact commands over descriptions of commands.** `pytest -q tests/unit` beats "run the unit tests." | Writing Style |  |  | ✓ |  |  |  | 1 |
| **Prefer idempotent steps; if a step is not idempotent, say so.** Retries are common; non-idempotent steps cause duplication | Correctness |  |  | ✓ |  |  |  | 1 |
| **Prefer structured commands (e.g., JSON RPC, dedicated CLI flags) over parsing `stdout`.** | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| **Provide a "dry run" mode where possible.** | **Safety** |  |  |  |  | ✓ |  | 1 |
| **Put `name`, `description`, and `when_to_use` in frontmatter at the top.** These drive skill selection; nothing else matters if selection fails | Structure |  |  | ✓ |  |  |  | 1 |
| **Re-test skill selection whenever you edit the description.** Small wording changes materially change selection behavior | Triggering and Selection |  |  | ✓ |  |  |  | 1 |
| **Reference scripts and data files by path; instruct the agent to read them only when needed.** Lazy loading is the core performance lever | Performance |  |  | ✓ |  |  |  | 1 |
| **Require an explicit confirmation step before any irreversible action.** The marginal latency is cheap; a wrong `rm -rf` is not | Safety |  |  | ✓ |  |  |  | 1 |
| **Require an explicit confirmation step for any destructive action.** | **Safety** |  |  |  |  | ✓ |  | 1 |
| **Review skills on the same cadence as the APIs they wrap.** Skill rot tracks dependency rot | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Scrutinize and sanitize any command that includes parameter substitution.** | **Safety** |  |  |  |  | ✓ |  | 1 |
| **Secrets, API keys, and credentials must never appear in the Skill file; always reference them by variable name or external store (e.g., `$API_KEY`, `env:GITHUB_TOKEN`).** (Prevents credential leaks.) | Safety & Security |  |  |  | ✓ |  |  | 1 |
| **Specify required inputs and their formats before the first step.** Missing preconditions are the top cause of silent failure | Correctness |  |  | ✓ |  |  |  | 1 |
| **Start the description with a verb.** | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| **State the expected postcondition (files changed, services running, exit codes).** Gives the agent something to check against | Correctness |  |  | ✓ |  |  |  | 1 |
| **State the minimum required permissions; refuse to escalate.** Principle of least privilege applies to skills as to humans | Safety |  |  | ✓ |  |  |  | 1 |
| **Store skills in version control alongside the code they operate on.** Drift between code and skill is the dominant decay mode | Maintainability |  |  | ✓ |  |  |  | 1 |
| **The description alone makes selection decidable.** If a reviewer can't tell when it fires, neither can the model | Review Checklist (block merge if any fails) |  |  | ✓ |  |  |  | 1 |
| **Use `kebab-case` for file names.** | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| **Use `verb-noun` for skill names.** | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| **Use a mandatory template with sections in this order: Name, Trigger, Preconditions, Steps, Validation, Rollback (if applicable), Maintenance Notes.** (Enables predictable parsing by humans and machines.) | Structure |  |  |  | ✓ |  |  | 1 |
| **Use code blocks for commands and configuration; don't embed code in prose.** (Improves scannability and allows copy-paste.) | Style & Language |  |  |  | ✓ |  |  | 1 |
| **Use explicit exit codes or output signals for step success or failure.** | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| **Use imperative voice ("Run `git status`," not "Running `git status`").** (Clarity and brevity.) | Steps |  |  |  | ✓ |  |  | 1 |
| **Use plain, direct language; assume the reader (human or AI) has domain knowledge but not context-specific knowledge.** (Balances clarity with brevity.) | Style & Language |  |  |  | ✓ |  |  | 1 |
| **Use progressive disclosure: link to sibling files for reference material, schemas, and long examples.** Keeps the hot path small | Structure |  |  | ✓ |  |  |  | 1 |
| **Use second-person only for safety warnings and confirmations.** Reserves that voice for where attention matters | Writing Style |  |  | ✓ |  |  |  | 1 |
| **Use specific, unambiguous trigger phrases in the "when-to-use" section.** | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| **Validate all prerequisites in the earliest possible step.** | **Performance** |  |  |  |  | ✓ |  | 1 |
| **Validation must be executable by the agent without requiring human judgment.** Use testable conditions: "File exists," "HTTP 200 response," not "Looks good." (Enables reliable automation.) | Validation |  |  |  | ✓ |  |  | 1 |
| **Version published/shared skills with SemVer; repo-local skills may rely on git history.** (contested) Shared consumers need stability guarantees; local consumers don't | Maintainability |  |  | ✓ |  |  |  | 1 |
| **Write steps as numbered imperatives ("Run X.", "Verify Y.").** Suggestions get ignored; commands get executed | Writing Style |  |  | ✓ |  |  |  | 1 |
| **Write the description from the agent's perspective.** | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| A good name communicates the skill's purpose at a glance | Structure |  | ✓ |  |  |  |  | 1 |
| Abort on repeated low-confidence reasoning signals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add Error Handling, Safety, and Observability sections | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add a local/offline test mode with mocked tools | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add a second-person confirmation step for high-risk operations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Always include a failsafe mechanism for critical operations | Safety |  | ✓ |  |  |  |  | 1 |
| Archive unused skills after deprecation windows | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Assign an accountable Owner and backup reviewer | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers, prompt authors, and tool owners responsible for safe, reliable agent workflows | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid model-specific quirks; keep instructions model-agnostic where possible | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid reliance on global state | Safety |  | ✓ |  |  |  |  | 1 |
| Avoid synonyms for key entities; define a glossary if needed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cache stable lookups and reuse context across steps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Clarity promotes understanding among different users and stakeholders | Style |  | ✓ |  |  |  |  | 1 |
| Clear triggers improve the skill's usability and effectiveness | Structure |  | ✓ |  |  |  |  | 1 |
| Co-locate related sub-skills in a directory with an index | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Conclude with explicit Completion Criteria and Follow-ups | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Consistency aids in quick comprehension and reduces cognitive load | Structure |  | ✓ |  |  |  |  | 1 |
| Consistency in naming helps with code maintenance and collaboration | Style |  | ✓ |  |  |  |  | 1 |
| DRY shared policies by reference, not copy-paste | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare a When Not to Use section with negative triggers and escalation paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare a When to Use section with positive trigger phrases and concrete examples | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare minimum model capabilities and any special formatting assumptions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare sensitive input fields and masking rules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default to Dry-Run for any write until explicitly confirmed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define Inputs with types, required/optional flags, and defaults | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define Outputs with a strict schema or shape and success criteria | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define trigger language explicitly | Structure |  | ✓ |  |  |  |  | 1 |
| Deprecate with dates and migration paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Detailed logs facilitate issue resolution and skill improvement | Error Handling |  | ✓ |  |  |  |  | 1 |
| Distinguish transient errors (retry) from permanent errors (abort) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document jurisdictional restrictions and audit requirements | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Emit structured events for start, step transitions, tool calls, retries, and exit | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| End with Examples (happy-path and edge cases) and a Changelog | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce strict JSON output for all skills, including human-facing ones | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Escalate to a human when policy or data conflicts arise | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fail closed on ambiguous or missing critical inputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Failsafes protect against process failures and maintain system integrity | Safety |  | ✓ |  |  |  |  | 1 |
| Fewer dependencies simplify maintenance and reduce potential failure points | Performance |  | ✓ |  |  |  |  | 1 |
| Follow a consistent naming convention (e.g., camelCase or snake_case) | Style |  | ✓ |  |  |  |  | 1 |
| For code or shell tools, require sandbox or read-only first, then promote on confirmation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For external APIs, include expected status codes and error classes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For human-facing results, specify a concise answer style and forbid chain-of-thought in outputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For long-running jobs, require a poll-and-timeout pattern with cancellation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For multi-intent tasks, prefer composition by calling sub-skills explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For search/retrieval, define corpus, filters, and chunking rules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Gate destructive actions behind Confirm or Dry-Run steps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Gate release on passing tests and owner review | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Highlight MUST/SHOULD with explicit wording, not formatting | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Implement robust error handling for all workflows | Error Handling |  | ✓ |  |  |  |  | 1 |
| Include Tooling with exact tool names, versions, scopes, and parameter rules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a clear and descriptive name for each skill | Structure |  | ✓ |  |  |  |  | 1 |
| Include a stable correlation ID and idempotency key per run | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “What this skill does NOT do” note | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include an Output Validation step that checks schema and business invariants | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include at least three high-signal positive trigger examples and three negative examples | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include golden outputs matching the declared schema | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Input validation prevents runtime errors and enhances safety | Error Handling |  | ✓ |  |  |  |  | 1 |
| Keep SKILL.md under 300 lines; link out for deep references | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep examples inside SKILL.md rather than external docs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep lines of code under 80 characters | Style |  | ✓ |  |  |  |  | 1 |
| Limit retrieval to the smallest necessary scope and depth | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| List explicit Preconditions and Required Permissions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Log all errors with context for easier debugging | Error Handling |  | ✓ |  |  |  |  | 1 |
| Log structured error details without secrets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Logical flow helps users understand the process and minimizes errors | Structure |  | ✓ |  |  |  |  | 1 |
| Make steps idempotent and include idempotency keys for external writes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Minimize data access to the least privilege required | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Minimize dependencies to essential libraries only | Performance |  | ✓ |  |  |  |  | 1 |
| Mutable global state can lead to unpredictable behavior across different workflows | Safety |  | ✓ |  |  |  |  | 1 |
| Never print or echo secrets; reference them by handle or vault ID | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| On validation failures, request specific clarifications once, then abort | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Optimize for performance after ensuring readability and maintainability | Performance |  | ✓ |  |  |  |  | 1 |
| Parallelize independent tool calls where safe and reorder to front-load blockers | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Performance enhancements should be secondary to clarity and ease of modification | Performance |  | ✓ |  |  |  |  | 1 |
| Prefer many small, composable skills over a few large ones | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer summaries over raw dumps; cap list sizes with pagination | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Present step-by-step instructions logically | Structure |  | ✓ |  |  |  |  | 1 |
| Prohibit chain-of-thought or hidden deliberations in final user-visible outputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Proper error management ensures the skill can recover from unexpected issues | Error Handling |  | ✓ |  |  |  |  | 1 |
| Provide a detailed description of what the skill does | Structure |  | ✓ |  |  |  |  | 1 |
| Provide a tie-break rule when triggers overlap | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide at least three executable test scenarios: happy path, edge, and failure | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide exact parameter shapes and allowed enums | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide numbered, imperative Steps with one action per step | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide one minimal example invocation and one complex example | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Rationale: Allows the agent or a human supervisor to preview a skill's effects before committing them | **Safety** |  |  |  |  | ✓ |  | 1 |
| Rationale: Allows the agent to safely retry the skill after an interruption without creating duplicate side effects | **Error Handling & State** |  |  |  |  | ✓ |  | 1 |
| Rationale: Avoids wasted work and compute time if the skill cannot possibly succeed | **Performance** |  |  |  |  | ✓ |  | 1 |
| Rationale: Clearly communicates the primary action of the skill (e.g., "Creates a new file...") | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| Rationale: Creates a clear contract and allows for early validation | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| Rationale: Defers recovery strategy to the agent's more capable reasoning-and-planning loop | **Error Handling & State** |  |  |  |  | ✓ |  | 1 |
| Rationale: Each step and call adds latency and is a potential point of failure | **Performance** |  |  |  |  | ✓ |  | 1 |
| Rationale: Enforces a clear, action-oriented naming convention (e.g., `create-user`, `get-file-content`) | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| Rationale: Enforces the principle of least privilege and contains the blast radius of a faulty skill | **Safety** |  |  |  |  | ✓ |  | 1 |
| Rationale: Ensures file system compatibility and consistency across operating systems | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| Rationale: Ensures the skill is stateless and leaves the environment clean for the next task | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| Rationale: Helps the agent understand what *it* can achieve by using the skill | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| Rationale: Improves reusability, testability, and makes the skill easier to maintain | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents accidental data loss or irreversible changes by the agent | **Safety** |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents command injection vulnerabilities from user-controlled or agent-generated inputs | **Safety** |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents silent failures where a step fails but execution continues | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents state contamination between skills and simplifies cleanup | **Structure & Naming** |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents the agent from incorrectly invoking the skill in ambiguous situations | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents the skill from continuing with corrupt data, which can lead to worse errors | **Error Handling & State** |  |  |  |  | ✓ |  | 1 |
| Rationale: Provides a clear, unambiguous execution path for the agent | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| Rationale: Reduces brittleness by decoupling the skill from cosmetic changes in command output | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| Rationale: Reduces the overhead of multiple network round-trips | **Performance** |  |  |  |  | ✓ |  | 1 |
| Rationale: Skills must be non-interactive; all inputs should be gathered before execution | **Instructions (Steps)** |  |  |  |  | ✓ |  | 1 |
| Rationale: The description is the "what," not the "how"; implementation details are brittle and irrelevant to the agent's planning | **Description & Triggers** |  |  |  |  | ✓ |  | 1 |
| Re-review skills at least quarterly or on upstream API changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Re-validate time-of-check assumptions right before apply | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Record durations and token usage per step | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Record partial progress and safe rollback steps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Redact PII in telemetry and enforce data retention limits | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Refer to tools by canonical names and pinned versions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Reference external tool schemas instead of embedding large copies | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require a machine-checkable output schema (JSON) for programmatic skills | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require explicit user consent for irreversible or cross-tenant actions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require post-action verification against source of truth | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require security review for skills with destructive or privileged actions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run a linter or checklist on PR to enforce these rules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Sanitize or neutralize untrusted content before using it in prompts or tools | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Authoring SKILL.md files that define reusable, model-invocable capabilities agents can load on demand | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set a token budget and context window allocation per skill | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Short-circuit early when prerequisites fail | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Show both success and failure outputs exactly as declared | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify maximum retries, backoff, and abort conditions per step | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify required scopes, rate limits, and timeouts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start each step with a strong verb and make it testable (“Validate X,” “Fetch Y,” “Update Z”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start every SKILL.md with Name, Summary, Owner, Version, Last-Reviewed, and Status | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State mutually exclusive relationships with other skills | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Surface human-readable remediation hints on abort | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Tag logs with skill version and environment | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| This can improve startup times and overall responsiveness | Performance |  | ✓ |  |  |  |  | 1 |
| This enhances clarity and understanding of the skill's functionality | Structure |  | ✓ |  |  |  |  | 1 |
| This file is subject to updates as best practices evolve; adhere to the latest guidelines for optimal results | Note |  | ✓ |  |  |  |  | 1 |
| This improves readability, especially in wide editor views | Style |  | ✓ |  |  |  |  | 1 |
| Timeouts can prevent long-running tasks from freezing systems or causing performance issues | Safety |  | ✓ |  |  |  |  | 1 |
| Track incidents and tie remediations to specific rule updates | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use a consistent format for SKILL.md files | Structure |  | ✓ |  |  |  |  | 1 |
| Use canonical units, encodings, and timezones (UTC, ISO-8601) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use clear and precise language throughout | Style |  | ✓ |  |  |  |  | 1 |
| Use consistent section headings and ordering across all skills | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use explicit decision points (“If A, do B; else, escalate”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use lazy loading for non-essential modules | Performance |  | ✓ |  |  |  |  | 1 |
| Use timeout thresholds where applicable | Safety |  | ✓ |  |  |  |  | 1 |
| Validate inputs before processing | Error Handling |  | ✓ |  |  |  |  | 1 |
| Validate triggers with a routing test set to detect overlaps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Version every change and document it in a Changelog | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write in clear, active voice with short sentences | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write triggers as concrete, model-matchable patterns (e.g., “create Jira issue,” not “project management”) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

