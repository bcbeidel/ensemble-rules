# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Design each subagent to perform a single, well-defined verb.** | System Prompt (`## System prompt`) |  |  |  |  | ✓ |  | 1 |
| **(contested) If a subagent reads from external APIs (e.g., GitHub, third-party linters), explicitly include those tool names and document rate limits or authentication assumptions.** | Tool Allowlists |  |  |  | ✓ |  |  | 1 |
| **Add a "Related Subagents" section if this subagent is designed to work with others (e.g., "complements PythonTestRunner").** | Documentation and Comments |  |  |  | ✓ |  |  | 1 |
| **Adopt a neutral, professional tone in descriptions and prompts; avoid sales language or excessive enthusiasm.** | Style and Tone |  |  |  | ✓ |  |  | 1 |
| **Avoid second-person meta-commentary about being an AI.** It wastes tokens and degrades output | Style |  |  | ✓ |  |  |  | 1 |
| **Commit project subagents to version control under `.claude/agents/`.** Team subagents are shared infrastructure | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Declare the `tools` field explicitly; never rely on the default.** Omitting it grants all tools, violating least privilege | Tools and Safety |  |  | ✓ |  |  |  | 1 |
| **Do define clear tool allowlists.** Only include tools that the subagent is intended to use to ensure safety and correctness | Structure |  | ✓ |  |  |  |  | 1 |
| **Do handle potential errors gracefully in prompts.** Unhandled errors may lead to agent failures in production | Error Handling |  | ✓ |  |  |  |  | 1 |
| **Do include versioning in file names.** This aids in tracking changes and maintaining a history of subagent definitions | Structure |  | ✓ |  |  |  |  | 1 |
| **Do limit the scope of actions subagents can perform to that specified in the allowlist.** This prevents accidental or malicious use of tools | Safety |  | ✓ |  |  |  |  | 1 |
| **Do not delete a subagent file; instead, mark it as deprecated in the YAML (e.g., `deprecated: true`, `replacement: "new-agent-name"`) and leave it in place for at least one release cycle.** | Versioning and Deprecation |  |  |  | ✓ |  |  | 1 |
| **Do not exceed two sentences in the description.** | Description (`## Description`) |  |  |  |  | ✓ |  | 1 |
| **Do not grant API credentials or secrets to subagent prompts; instead, document how the main agent should inject them at invocation time.** | Safety and Permissions |  |  |  | ✓ |  |  | 1 |
| **Do not include instructions that contradict the tool allowlist (e.g., "run the project's build script" if `bash` is not in `tools`).** | System Prompts |  |  |  | ✓ |  |  | 1 |
| **Do not include shell execution (`bash`, `sh`) unless the subagent's primary purpose requires it (e.g., build orchestration, environment setup).** | Tool Allowlists |  |  |  | ✓ |  |  | 1 |
| **Do not instruct the subagent to "try alternative approaches" if the primary tool is unavailable; instead, report the blocker clearly.** | Error Handling |  |  |  | ✓ |  |  | 1 |
| **Do not interpolate user input or context variables directly into the system prompt without escaping or sandboxing.** | System Prompts |  |  |  | ✓ |  |  | 1 |
| **Do not use generic filenames like `agent.md` or `test.md`.** | Naming and Location |  |  |  |  | ✓ |  | 1 |
| **Do optimize prompts to focus on specific tasks.** This improves the agent's efficiency and reduces unnecessary processing | Performance |  | ✓ |  |  |  |  | 1 |
| **Do provide a clear, concise description of the subagent.** This enhances understanding of the agent's functionality | Structure |  | ✓ |  |  |  |  | 1 |
| **Do review and iterate on definitions regularly.** Regular reviews help maintain relevance and correctness in a rapidly evolving environment | Common Pitfalls |  | ✓ |  |  |  |  | 1 |
| **Do use consistent naming conventions across all definitions.** Consistency aids readability and reduces cognitive load | Style |  | ✓ |  |  |  |  | 1 |
| **Document any non-obvious tool interactions in the system prompt (e.g., "after editing a file, always run format_check before reporting").** | Documentation and Comments |  |  |  | ✓ |  |  | 1 |
| **Document non-obvious subagents in the project README.** Discoverability matters when routing is implicit | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Don't allow ambiguous tool usage in the allowlist.** Ambiguity can lead to incorrect tool deployment and unexpected behavior | Error Handling |  | ✓ |  |  |  |  | 1 |
| **Don't apologize or hedge in the system prompt.** "Try your best" licenses mediocre output | Style |  |  | ✓ |  |  |  | 1 |
| **Don't commit personal subagents (`~/.claude/agents/`) to the project repo.** Scope matters | Repository Hygiene |  |  | ✓ |  |  |  | 1 |
| **Don't duplicate trigger vocabulary across subagents.** Overlapping triggers produce non-deterministic delegation | Description Field |  |  | ✓ |  |  |  | 1 |
| **Don't grant `Bash` unless the subagent's core job requires shell execution.** Bash is the widest attack surface | Tools and Safety |  |  | ✓ |  |  |  | 1 |
| **Don't grant `Write` or `Edit` to review, analysis, or reporting subagents.** Read-only intent requires read-only tools | Tools and Safety |  |  | ✓ |  |  |  | 1 |
| **Don't hardcode sensitive information within the definitions.** Hardcoding can lead to security vulnerabilities if exposed | Safety |  | ✓ |  |  |  |  | 1 |
| **Don't neglect documentation on usage and examples.** Well-documented agents are easier to adopt and integrate | Common Pitfalls |  | ✓ |  |  |  |  | 1 |
| **Don't overload a single subagent with disparate tasks.** Each agent should have a clear, singular purpose to ensure focus and efficiency | Performance |  | ✓ |  |  |  |  | 1 |
| **Don't reference prior conversation state.** Subagents run in fresh contexts; "continue what we were doing" has no referent | System Prompt Body |  |  | ✓ |  |  |  | 1 |
| **Don't use overly complex language in descriptions.** Clear and straightforward language promotes better understanding among engineers | Style |  | ✓ |  |  |  |  | 1 |
| **Enclose placeholders for dynamic information within `<context>` tags.** | System Prompt (`## System prompt`) |  |  |  |  | ✓ |  | 1 |
| **End with a checklist or success criteria the subagent should verify before returning.** Self-check reduces sloppy outputs | System Prompt Body |  |  | ✓ |  |  |  | 1 |
| **Enumerate the `tools` allowlist explicitly; do not use wildcards or "all tools" unless the subagent is a general-purpose fallback.** | Structure |  |  |  | ✓ |  |  | 1 |
| **Explicitly forbid destructive operations in the system prompt if the tool allows them (e.g., "Never delete files; only edit or create").** | Safety and Permissions |  |  |  | ✓ |  |  | 1 |
| **For file operations, declare intended directories or path patterns in the tools list where the tool supports it (e.g., `file_edit: {paths: ["src/**/*.ts", "tests/**/*.ts"]}`).** | Tool Allowlists |  |  |  | ✓ |  |  | 1 |
| **Grant only the tools the subagent actually uses.** A reviewer needs `Read`, `Grep`, `Glob` — not `Write` or `Bash` | Tools and Safety |  |  | ✓ |  |  |  | 1 |
| **Grant the minimum set of tools required for the task.** | Tool Allowlist (`## Tools`) |  |  |  |  | ✓ |  | 1 |
| **If a subagent can modify sensitive files (config, secrets, deployment scripts), include a review step in the prompt (e.g., "describe the change and request confirmation before writing").** | Safety and Permissions |  |  |  | ✓ |  |  | 1 |
| **If granting `Bash`, constrain commands in the system prompt.** Enumerate allowed commands; forbid `rm`, `curl \| sh`, credential access | Tools and Safety |  |  | ✓ |  |  |  | 1 |
| **If shell is included, document the exact use cases in the "Scope & Constraints" section (e.g., "only for running npm test, not for deployment").** | Tool Allowlists |  |  |  | ✓ |  |  | 1 |
| **If you revise a subagent significantly (tool additions, scope changes), bump a version in the YAML (e.g., `version: "1.1"`) and document breaking changes in a "Changelog" section.** | Versioning and Deprecation |  |  |  | ✓ |  |  | 1 |
| **In the system prompt, define how the subagent should behave when it cannot access a required tool or encounters a permission error (e.g., "Report the missing file path and stop; do not attempt workarounds").** | Error Handling |  |  |  | ✓ |  |  | 1 |
| **Include `name` and `description` in frontmatter; both are mandatory.** Missing either breaks discovery or routing | Structure |  |  | ✓ |  |  |  | 1 |
| **Include a "Context & Assumptions" block if the subagent assumes project structure, language versions, or runtime environments.** | Documentation and Comments |  |  |  | ✓ |  |  | 1 |
| **Include a "Scope & Constraints" section after the front matter, stating what the subagent *does not* do and any implicit dependencies (e.g., "assumes a Python 3.9+ repo").** | Structure |  |  |  | ✓ |  |  | 1 |
| **Include at least one concrete example of input and expected output.** Few-shot examples outperform abstract instructions | System Prompt Body |  |  | ✓ |  |  |  | 1 |
| **Include explicit trigger conditions in the description.** Phrases like "Use when…", "MUST BE USED for…", "after editing Python files" make routing deterministic | Description Field |  |  | ✓ |  |  |  | 1 |
| **Include one minimal example (input and output) in the system prompt if the task is ambiguous; link to detailed examples in external docs.** | System Prompts |  |  |  | ✓ |  |  | 1 |
| **Include only tools necessary to accomplish the declared task; omit tools "just in case".** | Tool Allowlists |  |  |  | ✓ |  |  | 1 |
| **Keep `description` under ~400 characters.** Longer descriptions dilute the routing signal | Description Field |  |  | ✓ |  |  |  | 1 |
| **Keep descriptions under 100 words and action-oriented ("finds and fixes X"; avoid "helps with" or "assists in").** | Structure |  |  |  | ✓ |  |  | 1 |
| **Keep each subagent to a single responsibility.** Overlapping subagents cause unpredictable routing | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep system prompts under 2 KB; prioritize clarity over exhaustiveness.** | System Prompts |  |  |  | ✓ |  |  | 1 |
| **Keep the section order: Description, then Tools, then System prompt.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Keep the system prompt under ~1500 tokens unless justified.** Longer prompts eat the subagent's own context budget | System Prompt Body |  |  | ✓ |  |  |  | 1 |
| **List each tool on its own line without any prefixes.** | Tool Allowlist (`## Tools`) |  |  |  |  | ✓ |  | 1 |
| **Make `name` match the filename stem.** Mismatches confuse humans diffing the repo | Structure |  |  | ✓ |  |  |  | 1 |
| **Mandate a specific, machine-parsable output format.** | System Prompt (`## System prompt`) |  |  |  |  | ✓ |  | 1 |
| **Name each subagent file with a lowercase, hyphenated descriptor matching its primary role (e.g., `typescript-linter.md`, `pull-request-summarizer.md`).** | Naming |  |  |  | ✓ |  |  | 1 |
| **Name the agent file to reflect its specific capability (e.g., `lint_fixer.md`).** | Naming and Location |  |  |  |  | ✓ |  | 1 |
| **Omit the `model` field to inherit the session default.** Explicit overrides should be intentional, not cargo-culted | Model Selection |  |  | ✓ |  |  |  | 1 |
| **Open the system prompt with a one-line role statement.** "You are a …" anchors the model's persona before instructions | System Prompt Body |  |  | ✓ |  |  |  | 1 |
| **Place agent definitions in `.claude/agents/`.** | Naming and Location |  |  |  |  | ✓ |  | 1 |
| **Place subagent files in `.claude/agents/` with a `.md` extension.** Claude Code only discovers subagents in these locations | Structure |  |  | ✓ |  |  |  | 1 |
| **Place the system prompt in a clearly delimited `system_prompt` field (not inline prose).** | Structure |  |  |  | ✓ |  |  | 1 |
| **Provide explicit instructions on how to behave on failure or ambiguity.** | System Prompt (`## System prompt`) |  |  |  |  | ✓ |  | 1 |
| **Put the system prompt in the markdown body, not in frontmatter.** Frontmatter is for metadata | Structure |  |  | ✓ |  |  |  | 1 |
| **Reserve `model: opus` for subagents doing genuinely hard reasoning.** Default-to-opus wastes budget | Model Selection |  |  | ✓ |  |  |  | 1 |
| **Specify the output format explicitly.** The caller parses the response; unstructured prose breaks downstream agents | System Prompt Body |  |  | ✓ |  |  |  | 1 |
| **Start each subagent definition with a YAML front matter block declaring `name`, `description`, `tools`, and `model` fields.** | Structure |  |  |  | ✓ |  |  | 1 |
| **Start the description with a verb phrase stating the agent's core capability.** | Description (`## Description`) |  |  |  |  | ✓ |  | 1 |
| **Start the file with a YAML frontmatter block delimited by `---`.** Without frontmatter, the file is not a valid subagent | Structure |  |  | ✓ |  |  |  | 1 |
| **State the subagent's **single primary goal** at the top of the system prompt in one sentence (e.g., "Find and report TypeScript type mismatches in this repository").** | System Prompts |  |  |  | ✓ |  |  | 1 |
| **Structure the prompt with markdown headings (Responsibilities, Process, Output Format, Constraints).** Headings improve retrieval during long tasks | System Prompt Body |  |  | ✓ |  |  |  | 1 |
| **Use `CamelCase` for the `name` field in YAML to match Claude's naming style (e.g., `TypeScriptLinter`).** | Naming |  |  |  | ✓ |  |  | 1 |
| **Use `PROACTIVELY` or `MUST BE USED` when the subagent should self-invoke.** Without these keywords, Claude only delegates on explicit request | Description Field |  |  | ✓ |  |  |  | 1 |
| **Use `kebab-case` for the `name` field.** Matches Claude Code's convention and avoids quoting issues | Structure |  |  | ✓ |  |  |  | 1 |
| **Use `model: haiku` for mechanical, high-volume subagents.** Linters, formatters, and simple extractors don't need Sonnet | Model Selection |  |  | ✓ |  |  |  | 1 |
| **Use a direct, imperative tone in the system prompt.** | System Prompt (`## System prompt`) |  |  |  |  | ✓ |  | 1 |
| **Use consistent terminology across all subagent definitions (e.g., always say "file" not "document"; always say "directory" not "folder").** | Style and Tone |  |  |  | ✓ |  |  | 1 |
| **Use imperative mood ("Find X", "Report Y") rather than permissive ("You may find X", "You can report Y").** | System Prompts |  |  |  | ✓ |  |  | 1 |
| **Use present tense and active voice throughout.** Consistent with prompt-engineering norms | Style |  |  | ✓ |  |  |  | 1 |
| **Use the standard three-section markdown structure.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Write instructions in the imperative mood.** "Run the tests" not "You should probably run the tests." | Style |  |  | ✓ |  |  |  | 1 |
| **Write the `description` for the router, not for humans.** It's the primary routing signal; treat it as a classifier prompt | Description Field |  |  | ✓ |  |  |  | 1 |
| **Write the description for the main agent, not a human.** | Description (`## Description`) |  |  |  |  | ✓ |  | 1 |
| Audience: Engineers and AI prompt/tooling authors who create, review, or maintain subagents used by a main Claude Code agent | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid duplicated guidance across agents; extract shared text into a referenced include (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default network_access to false and only enable with allowed_domains present | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define a minimal, structured Output contract for success and for refusal/escalation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define files_allowlist and files_denylist in frontmatter whenever the agent can write or edit files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Describe in-scope tasks, out-of-scope tasks, and expected output formats precisely | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do include a detailed description section that clearly outlines the subagent's role and boundaries, to ensure correct delegation and avoid ambiguity | Content Requirements |  |  |  |  |  | ✓ | 1 |
| Do incorporate guardrails in the system prompt, such as explicit instructions to reject unsafe inputs, to prevent misuse and protect against attacks | Safety |  |  |  |  |  | ✓ | 1 |
| Do keep the system prompt under 500 tokens to minimize latency and resource usage during execution | Performance |  |  |  |  |  | ✓ | 1 |
| Do name files descriptively, such as `subagent-task-specific.md`, to reflect the agent's purpose and aid in discovery (contested) | Structure |  |  |  |  |  | ✓ | 1 |
| Do not embed secrets, API keys, or tokens in the file | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do specify a tool allowlist as an explicit list (e.g., bullet points) with justifications, to enforce least-privilege access and promote correctness | Content Requirements |  |  |  |  |  | ✓ | 1 |
| Do structure the file with dedicated sections for description, tool allowlist, and system prompt, using Markdown headings (e.g., ## Description), to make navigation intuitive and consistent | Structure |  |  |  |  |  | ✓ | 1 |
| Do use a YAML front matter at the top of each file to define metadata like agent name and version, as it provides a standardized way to organize essential details | Structure |  |  |  |  |  | ✓ | 1 |
| Do use consistent, professional language throughout the file, avoiding slang or ambiguity, to enhance readability and maintainability | Style |  |  |  |  |  | ✓ | 1 |
| Do validate inputs and outputs in the prompt where possible, to maintain safety without overly complicating the definition (contested) | Safety |  |  |  |  |  | ✓ | 1 |
| Document a short Changelog section at the end of the file with date, author, and summary | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't exceed three levels of headings in the file, as deeper nesting complicates readability and maintenance | Structure |  |  |  |  |  | ✓ | 1 |
| Don't grant access to sensitive tools (e.g., file system access) without explicit justification in the description, as this heightens security risks | Safety |  |  |  |  |  | ✓ | 1 |
| Don't include placeholder text (e.g., "TODO") in final definitions, as it indicates incompleteness and reduces trust in the system | Style |  |  |  |  |  | ✓ | 1 |
| Don't include redundant or verbose elements in the description or prompt, as they degrade performance by increasing processing time | Performance |  |  |  |  |  | ✓ | 1 |
| Don't reference undefined or external tools in the allowlist, as this leads to runtime errors and undermines reliability | Content Requirements |  |  |  |  |  | ✓ | 1 |
| Ensure escalate_to references at least one other subagent id | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For files_allowlist, prohibit bare "*" or "**/*" | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Grant the minimum tools needed for the task | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If network_access is true, define allowed_domains | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a files_denylist with at least one pattern whenever writes are allowed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include body sections with H2 headings: Scope, Out of scope, Input contract, Output contract, Handoff criteria, and Examples | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Instruct the agent to stop after N failed attempts (default 2) and escalate | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep description to one sentence ≤ 160 characters | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the system prompt under 3000 characters (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the system_prompt in frontmatter as a single YAML string block | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| List only approved tool names in tools_allowlist; never use "*" or "all" | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make id kebab-case and match the filename stem | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make name Title Case and ≤ 40 characters | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Narrow context via files_allowlist to task-relevant paths | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prohibit allowed_domains of "*" or ".*" | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide at least one concrete Example that maps an input to the expected output format | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put each subagent in .claude/agents/<id>.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require commit_preview_required: true when any write-capable tool is allowed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require dry_run_required: true when using terminal, git, or filesystem.write | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: This rules file governs Claude Code custom subagent definition files located at .claude/agents/*.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set max_output_tokens ≤ 4096 (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set owner to a resolvable team or email | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set timeout_seconds between 5 and 900 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify concrete Handoff criteria that trigger escalate_to | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start each file with YAML frontmatter containing id, name, description, owner, model, tools_allowlist, system_prompt, escalate_to, timeout_seconds | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State explicit refusal criteria in the system prompt (e.g., when to stop and escalate) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Update owner and escalate_to on ownership changes before merging | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use the exact H2 headings defined in Structure and keep sections concise | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate tools_allowlist against a central approved tools list in CI | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

