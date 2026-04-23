# MCP Servers: Synthesized Best-Practices Guidance

## 1. Consensus Rules

### Transport & I/O Protocol

- **Never write non-protocol output to stdout on stdio transports; logs go to stderr or a file.** Stray writes corrupt the JSON-RPC frame and break clients. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini; present in all four detailed responses)*
- **Use the official MCP SDK rather than hand-rolling the protocol.** SDKs encode subtle framing, timeout, and lifecycle requirements that are easy to miss. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Schemas & Input Validation

- **Define every tool with an explicit, strict input schema (JSON Schema / Zod / Pydantic).** The schema is the contract the LLM reads on every invocation; lying or omitting it propagates into agent behavior. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Set `additionalProperties: false` (or equivalent strictness) on object schemas.** Unknown fields are usually model hallucinations; reject them loudly. *(near-identical wording across GPT-5 and Claude Opus; also raised by Claude Haiku)*
- **Validate inputs before the handler does any work and return structured validation errors naming the field.** Catches typos and misuse early and lets the model self-correct. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Tool Design & Naming

- **Write tool names and descriptions for the model: stable `verb_noun` snake_case names and short, purposeful descriptions.** The tool surface is the LLM's UI; ambiguity produces misuse. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Declare side effects and idempotency in each tool's description; default to read-only.** Enables safe retries and scoped approval UX. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Error Handling

- **Return structured errors with a stable code, a human-readable message, and actionable detail — never a bare string or silent empty result.** Silent failures cause infinite retry loops and wrong-data propagation. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Distinguish transient from permanent errors so clients know whether to retry.** Prevents retry storms on permanent failures and gives up too easily on transient ones. *(substantively similar across GPT-5, Claude Haiku)*
- **Set an explicit, configurable timeout on every outbound I/O call.** Unbounded calls hang the agent loop. *(near-identical wording across GPT-5 and Claude Opus; also raised by Claude Haiku, Gemini)*

### Safety & Security

- **Scope credentials to the minimum required; treat the server as a confused deputy.** The server's token defines the blast radius. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Never interpolate tool input into shell commands, SQL, or `eval`-like constructs; use parameterized APIs.** This is the dominant injection vector. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Enforce allowlists for filesystem paths and network egress; reject `..` and traversal.** Allowlists fail closed; denylists don't. *(substantively similar across GPT-5, Claude Haiku, Gemini)*
- **Never hard-code secrets; never log them.** Use env vars or a secrets manager and redact at log-emission time. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Response Size & Performance

- **Paginate or truncate anything that can return a large list, and mark truncation explicitly.** Unbounded responses burn context, money, and memory. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Cap response sizes and enforce per-request resource limits (memory, wall-clock).** Prevents OOMs and token overflow. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Observability

- **Log every tool invocation with name, arguments (redacted), duration, and outcome in structured form.** Audit trails are the first thing you need when something goes wrong. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Emit structured JSON logs to stderr with timestamps and correlation IDs.** Makes production triage tractable. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Testing

- **Write tests covering success, invalid input, boundary, and error paths for every tool.** A tool without a malformed-input test hasn't proven its validation works. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Documentation

- **Provide a README documenting purpose, tools, required env vars, and setup.** Operators can't run what they can't configure. *(substantively similar across GPT-5, Claude Haiku, Gemini)*

### Versioning

- **Include a semantic version in server metadata; pin the MCP SDK to a specific version.** The ecosystem is young and churning; floating versions produce silent behavior shifts. *(substantively similar across GPT-5, Claude Opus)*

## 2. Strong Minority Rules

- **Give destructive tools distinct name prefixes (`delete_*`, `drop_*`, `force_*`).** (Claude Opus) — Name-level signaling is the only safety cue some clients surface to the end user; cheap to adopt and mechanically checkable.
- **Never expose generic `execute_sql`, `run_shell`, or `eval` tools in production.** (Claude Opus, echoed in spirit by Claude Haiku and Gemini) — Collapses the entire safety model into one prompt injection; worth stating explicitly.
- **Require a confirmation token (or dry-run mode) for irreversible operations.** (Claude Opus, Claude Haiku) — Forces the model to surface intent to the user before destructive action.
- **Treat all tool output as untrusted data — never as instructions.** (Claude Opus) — Prompt injection via returned content (tickets, emails, web pages) is a routine attack vector that most guidance omits.
- **Keep tool handlers short (~50 lines) and avoid module-level mutable state.** (Claude Opus) — Mutable module state breaks HTTP/multi-tenant deployments in subtle ways; worth keeping.
- **Snapshot the full tool list and schemas; diff on every PR.** (Claude Opus) — Accidental schema changes break deployed clients silently; cheap insurance.
- **Implement graceful shutdown on SIGTERM/SIGINT and drain in-flight work.** (GPT-5) — Enables safe deploys and autoscaling; commonly overlooked.
- **Provide `/health` and `/ready` endpoints for HTTP transport.** (GPT-5, Claude Haiku) — Required for any orchestrated deployment.
- **Prefer `async` handlers uniformly; do not mix sync and async.** (Claude Opus) — Mixed execution models cause subtle deadlocks under load.
- **Pin base images by digest and include a `.dockerignore` and `HEALTHCHECK`.** (GPT-5) — Reproducibility and container hygiene that tend to be forgotten.
- **Sandbox tool execution (containers, limited user accounts).** (Gemini) — The strongest defense against malicious tool behavior; worth surfacing as a design option.

## 3. Divergences

- **Server granularity: one server per integration vs. split at ~20 tools vs. split at 40+.**
  - GPT-5: one server per operational responsibility (contested).
  - Claude Opus: tool-count bloat starts hurting model selection at ~40+.
  - Claude Haiku: 5–15 tools is ideal; split beyond 20.
  - **Recommendation:** Prefer one server per logical domain; split when it exceeds ~20 tools *or* spans unrelated capabilities. The number is heuristic; the principle (contain blast radius, clarify ownership, keep the tool menu legible to the model) is what matters.

- **Stateless vs. stateful servers.**
  - Gemini: stateless, explicitly (contested).
  - Claude Opus: avoid module-level mutable state (similar stance).
  - Others: quiet.
  - **Recommendation:** Default to stateless. Server-side state creates a second coordination problem on top of the client's; externalize it when possible.

- **Reject unknown properties (`additionalProperties: false`) vs. tolerate for forward compatibility.**
  - GPT-5 and Claude Opus: reject. GPT-5 flags it as contested.
  - Others silent.
  - **Recommendation:** Reject by default. Forward compatibility for MCP tools is better served by adding optional fields than by tolerating unknowns — because the "unknown" is usually an LLM hallucination, not a future client.

- **Egress allowlists — hard enforcement vs. observe-and-alert.**
  - GPT-5: enforce in production (contested).
  - Others: mostly silent except Gemini's general allowlist stance.
  - **Recommendation:** Enforce for any server that handles user data or proprietary systems; observe-only is acceptable for dev/experimentation.

- **Tool granularity: many narrow tools vs. multiplex with a `mode` parameter.**
  - Claude Opus: one tool per distinct operation (contested).
  - Claude Haiku: lean narrow but cap at 20.
  - GPT-5: doesn't take a strong stance.
  - **Recommendation:** Prefer narrow tools. Multiplexing confuses tool selection and muddles permission boundaries. Accept the tool-count growth and split servers when it gets unwieldy.

- **Base-image digest pinning.**
  - GPT-5: pin by digest (contested).
  - Others silent.
  - **Recommendation:** Pin in production images; for local dev or internal-only servers this is overkill. The rule carries real cost (update overhead) and should be adopted deliberately.

## 4. Notable Omissions

- **stdout/stderr discipline** — GPT-4o-mini doesn't mention this, despite it being the single most common MCP-specific footgun and appearing in all other responses. The absence reflects that GPT-4o-mini's response is generic "good engineering" advice without MCP-specific content.
- **Schema strictness and `additionalProperties: false`** — Missing from GPT-4o-mini and Claude Haiku (partially); this is a near-universal recommendation elsewhere.
- **Use the official MCP SDK** — GPT-4o-mini omits; Gemini omits. Strong consensus elsewhere that hand-rolling the protocol is a mistake.
- **Pagination / response-size caps** — GPT-4o-mini and Gemini both omit concrete pagination guidance, despite token budgets being the dominant performance constraint in agent contexts.
- **Structured error responses with codes** — GPT-4o-mini mentions logging errors but not returning structured error objects with stable codes — a recommendation made by the three other detailed responses.
- **Tool invocation audit logging** — GPT-4o-mini omits; near-universal elsewhere. This is the single most important observability rule for MCP servers because mutating tools can cause real damage.
- **Prompt injection via tool output** — Only Claude Opus raises this explicitly; a notable omission across the others given how widespread the risk is.
- **Timeouts on I/O calls** — GPT-4o-mini omits despite this being table stakes.

GPT-4o-mini's response is conspicuously generic throughout — most of its rules apply to any service, not specifically to MCP servers. Treat its omissions as low signal individually but high signal collectively: the response likely did not engage with MCP specifics.

## 5. Shared Deterministic Checks

### Multi-model checks

- **Check:** Verify that no code path outside the SDK's protocol writer emits to stdout in a stdio-transport server.
  - **Signal:** Source AST (language-specific: `console.log`, `process.stdout.write`, `print(` without `file=sys.stderr`, `sys.stdout.write`).
  - **Tool candidate:** ESLint `no-console` (scoped), ruff/flake8 custom rule; otherwise ad-hoc.
  - **Raised by:** GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance:** GPT-5 and Claude Opus require a suppression pragma allowlist for the legitimate SDK writer; Gemini frames it as linting with exemptions; Claude Haiku treats it as part of logger-config validation. All agree the check is a heuristic, not a proof.

- **Check:** Verify every tool registration includes a non-empty input schema, and that every object schema has `additionalProperties: false` (or language equivalent: Zod `.strict()`, Pydantic `extra="forbid"`).
  - **Signal:** AST of tool registration calls, or compiled JSON Schema.
  - **Tool candidate:** ad-hoc; Zod→`zod-to-json-schema`, Pydantic→`model_json_schema()`.
  - **Raised by:** GPT-5, Claude Opus, Claude Haiku.
  - **Variance:** Claude Opus requires whitelisting legitimate metadata bags via inline comment; GPT-5 and Haiku are stricter. Substance agrees.

- **Check:** Verify every outbound I/O call (HTTP, DB, subprocess) passes an explicit timeout argument.
  - **Signal:** Source AST.
  - **Tool candidate:** ad-hoc; partial coverage via `bandit`, `semgrep`, custom lint rules.
  - **Raised by:** GPT-5, Claude Opus, Claude Haiku.
  - **Variance:** Claude Opus recognizes client-level default timeouts as acceptable; GPT-5 and Haiku are more literal and may false-positive on wrapped clients.

- **Check:** Verify no shell-injection-prone patterns exist: `shell=True` in Python subprocess, `exec`/`execSync` in Node, string interpolation into SQL.
  - **Signal:** Source AST.
  - **Tool candidate:** `bandit` (Python), `semgrep`, `gosec`, ESLint security plugin.
  - **Raised by:** GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance:** Gemini requires taint analysis to confirm user input reaches the sink; others use simpler pattern matching. Taint analysis has fewer false positives but requires heavier tooling.

- **Check:** Verify the MCP SDK dependency is pinned to an exact version (or a lockfile is committed).
  - **Signal:** `package.json`, `requirements.txt`, `pyproject.toml`, lockfiles.
  - **Tool candidate:** ad-hoc dependency-manifest parser.
  - **Raised by:** GPT-5 (general dependency pinning), Claude Opus (specifically the MCP SDK).
  - **Variance:** GPT-5 applies to all deps; Opus applies specifically to the SDK. A lockfile can satisfy both.

- **Check:** Run a secret scanner over the repo and fail on high-confidence findings.
  - **Signal:** Full repo tree.
  - **Tool candidate:** `gitleaks`, `trufflehog`, `detect-secrets`.
  - **Raised by:** GPT-5, Claude Haiku.
  - **Variance:** Agree on substance; Haiku adds a log-statement scan for live secret leakage.

- **Check:** Verify a README exists at the repo root and documents environment/configuration.
  - **Signal:** `README.md` contents.
  - **Tool candidate:** ad-hoc (keyword/heading search).
  - **Raised by:** GPT-5, Claude Haiku.
  - **Variance:** Haiku checks for a tool list and setup instructions; GPT-5 only checks for env/config keywords. Haiku is stricter.

- **Check:** Verify list-returning tools declare a pagination parameter (`limit`, `cursor`, `offset`, `page`, `page_size`) or enforce `maxItems`.
  - **Signal:** Input schema + handler AST.
  - **Tool candidate:** ad-hoc.
  - **Raised by:** Claude Opus, Claude Haiku.
  - **Variance:** Opus infers list-return from handler AST (`findAll()`, `SELECT` without `LIMIT`); Haiku checks schema `maxItems` and hand-rolled limits. Complementary.

- **Check:** Verify a tool test suite exists and invokes each registered tool.
  - **Signal:** Test files + tool registry.
  - **Tool candidate:** ad-hoc; coverage tools as secondary signal.
  - **Raised by:** Claude Opus (snapshot diff), Claude Haiku (per-tool tests + smoke test).
  - **Variance:** Opus emphasizes schema-snapshot diffing in CI; Haiku emphasizes coverage-based per-tool tests. Different primary targets but both want automated tool-surface verification.

### Singleton checks

- **Check:** Verify tool names match `^[a-z][a-z0-9]*(_[a-z0-9]+)+$` and start with a known verb prefix.
  - **Signal:** Tool registration AST.
  - **Tool candidate:** ad-hoc.
  - **Raised by:** Claude Opus.

- **Check:** Verify tools whose handlers invoke destructive operations (SQL `DELETE`, `fs.unlink`, HTTP `DELETE`) carry a destructive name prefix.
  - **Signal:** Tool registration AST + handler AST.
  - **Tool candidate:** ad-hoc.
  - **Raised by:** Claude Opus.

- **Check:** Verify no tool is registered under the names `execute_sql`, `run_shell`, `eval`, `exec`, etc.
  - **Signal:** Tool registration AST.
  - **Tool candidate:** ad-hoc (regex match).
  - **Raised by:** Claude Opus.

- **Check:** Verify tool-handler functions are under ~50 non-blank, non-comment lines.
  - **Signal:** Handler AST.
  - **Tool candidate:** ad-hoc; existing complexity/length linters.
  - **Raised by:** Claude Opus.

- **Check:** Verify no module-level `let`/`var` or Python module-level names are reassigned after first bind.
  - **Signal:** Module-scope AST.
  - **Tool candidate:** ad-hoc; partial via ESLint `prefer-const`.
  - **Raised by:** Claude Opus.

- **Check:** Verify tool handlers are uniformly async (or uniformly sync).
  - **Signal:** Handler registration AST.
  - **Tool candidate:** ad-hoc.
  - **Raised by:** Claude Opus.

- **Check:** Verify signal handlers for SIGTERM/SIGINT exist and call a server shutdown method.
  - **Signal:** Source AST.
  - **Tool candidate:** ad-hoc.
  - **Raised by:** GPT-5.

- **Check:** Verify an HTTP server registers `/health` and `/ready` routes.
  - **Signal:** Source AST (framework-specific route registration).
  - **Tool candidate:** ad-hoc.
  - **Raised by:** GPT-5, Claude Haiku (similar but less strict).

- **Check:** Verify a `Dockerfile` contains a non-root `USER` instruction, a `HEALTHCHECK`, and pins `FROM` by digest.
  - **Signal:** Dockerfile.
  - **Tool candidate:** `hadolint` (partial coverage).
  - **Raised by:** GPT-5.

- **Check:** Verify CI configuration runs at least one linter, one secret scanner, and one dependency auditor.
  - **Signal:** CI workflow YAML.
  - **Tool candidate:** ad-hoc.
  - **Raised by:** GPT-5.

- **Check:** Verify server `stdout` on a test request yields valid line-delimited JSON.
  - **Signal:** Live process stdout given a known input.
  - **Tool candidate:** ad-hoc runtime harness.
  - **Raised by:** Gemini.

- **Check:** Verify the tool-parameter schema validates against the JSON Schema meta-schema.
  - **Signal:** Tool manifest file.
  - **Tool candidate:** JSON Schema validator against `draft-2020-12` meta-schema.
  - **Raised by:** Gemini.

- **Check:** Verify path-accepting tool handlers call a normalization + allowlist check before filesystem access.
  - **Signal:** Handler AST.
  - **Tool candidate:** ad-hoc; `semgrep` rules.
  - **Raised by:** Claude Haiku.

- **Check:** Verify handlers for mutating tools require a `confirm_token` or `dry_run` parameter before performing the mutation.
  - **Signal:** Schema + handler AST.
  - **Tool candidate:** ad-hoc.
  - **Raised by:** Claude Haiku.

---

## 6. Final Rules File

# MCP Server Best-Practices Rules

**Scope.** Servers implementing the Model Context Protocol over stdio or HTTP, exposing tools, resources, or prompts to LLM clients.

**Audience.** Engineers and AI coding assistants building or modifying such servers.

**Philosophy.** The tool surface is the LLM's UI. Be strict about contracts, safe by default, transparent when things fail, and bounded in resource use. Correctness before performance.

## Structure & Project Layout

- Use the official MCP SDK for your language rather than hand-rolling JSON-RPC or stdio framing.
- Pin the MCP SDK to an exact version (or commit a lockfile).
- Keep one server per logical domain; split when a server exceeds ~20 tools or mixes unrelated capabilities.
- Separate protocol handling, tool dispatch, and tool implementation into distinct modules.
- Co-locate each tool's schema, handler, and tests in one file.
- Default to a stateless server design; externalize session state to clients or a shared store. *(contested)*
- Avoid module-level mutable state; it breaks under concurrent HTTP or multi-tenant deployment.
- Minimize external dependencies; each one is maintenance and attack surface.

## Tool Design & Naming

- Name tools `verb_noun` in snake_case, using a consistent set of verbs (`list_`, `get_`, `create_`, `update_`, `delete_`, `search_`, etc.).
- Write tool descriptions for the model, not the human: one to three sentences covering purpose, when to use it, when not to, and what it returns.
- Declare one tool per distinct operation; do not multiplex with a `mode` parameter.
- Default every tool to read-only; require explicit opt-in for mutation.
- Give destructive tools distinct name prefixes (`delete_`, `drop_`, `force_`).
- Never expose generic `execute_sql`, `run_shell`, `exec`, or `eval` tools in production.
- Declare side effects, idempotency, and rollback semantics in the tool description.
- Require a confirmation token or dry-run mode for irreversible operations.

## Schemas & Input Validation

- Define every tool's input with a strict schema (Zod, Pydantic, or JSON Schema). Never register a tool without one.
- Set `additionalProperties: false` (or Zod `.strict()` / Pydantic `extra="forbid"`) on all object schemas. Allow exceptions only with an explicit annotation.
- Validate inputs before the handler does any work; return structured validation errors naming the offending field and violation.
- Mark optional parameters optional; do not encode optionality with sentinel values like `""` or `-1`.
- Use enums for any parameter with a fixed set of values.
- Enforce length, cardinality, and range limits in the schema (`maxLength`, `maxItems`, `minimum`, `maximum`).
- For path inputs, validate against an explicit allowlist and reject `..` and absolute paths outside that list. Resolve symlinks before re-validating.

## Safety & Security

- Scope the server's credentials to the minimum required; assume the server is a confused deputy.
- Never interpolate tool input into shell commands, SQL, or `eval`-like constructs. Use parameterized queries and safe exec variants only.
- Enforce allowlists over denylists for filesystem paths and outbound network hosts.
- Sandbox tool execution (containers, isolated users) for servers handling untrusted or sensitive data.
- Treat all tool output as untrusted data — never as instructions. Do not auto-chain tools based on string patterns in other tools' output.
- Require TLS and authentication on every HTTP endpoint; never expose unauthenticated HTTP to untrusted networks.
- Never hard-code secrets. Read them from environment variables or a secrets manager, validated at startup.
- Redact secrets and PII from logs and error messages by field name, not by pattern matching.
- Pin dependencies and scan for vulnerabilities in CI.

## Error Handling

- Return structured errors with a stable `code`, an actionable `message`, and a `detail` field — never bare strings, stack traces, or silent empty results.
- Distinguish transient errors (`timeout`, `rate_limited`, `service_unavailable`) from permanent ones (`validation_error`, `permission_denied`, `not_found`).
- Include the offending argument name and value in validation errors.
- Set an explicit, configurable timeout on every outbound I/O call (HTTP, DB, subprocess, filesystem).
- On timeout, return immediately with a `timeout` error — do not wait for the operation to finish.
- Retry only idempotent operations, with exponential backoff and jitter.
- Never crash the process on bad input.

## Transport & I/O

- On stdio transport, never write to stdout except via the SDK's protocol writer. All `console.log`, `print`, and direct stdout writes are protocol-corruption bugs.
- Send logs to stderr (or a file) in structured JSON form with timestamp, level, tool name, request ID, duration, and outcome.
- Flush or await all writes before process exit.
- For HTTP transport, require authentication on every request and never rely on session cookies alone.
- Handle connection drops and EOF gracefully; clean up resources.

## Response Size & Performance

- Paginate any tool that can return more than ~50 items. Declare `limit`, `cursor`, or `page_size` in the schema.
- Truncate large string fields with an explicit marker (e.g., `...[truncated 12KB]`). Never truncate silently.
- Return summaries by default; provide separate `get_*` tools for full detail.
- Cap response sizes and enforce per-request memory and wall-clock limits.
- Reuse connections (HTTP keepalive, DB pools) instead of reconnecting per call.
- Stream progress or return a handle plus a `get_status` tool for operations over ~2 seconds.
- Prefer async I/O uniformly; do not mix sync and async handlers in the same server.

## Observability

- Log every tool invocation with name, redacted arguments, duration, and outcome.
- Log mutating operations with enough context to audit what changed, when, and by whom.
- Emit a structured startup log line with server name, version, and tool count.
- Propagate and log correlation/request IDs across downstream calls.
- For HTTP transport, expose `/health` (liveness) and `/ready` (readiness) endpoints that validate critical dependencies.
- Implement graceful shutdown on SIGTERM/SIGINT; drain in-flight requests.

## Testing

- Write tests for every tool covering success, invalid input, boundary conditions, and error paths.
- Invoke tools through the MCP protocol in at least one test, not only by calling handlers directly.
- Include a smoke test that invokes every tool with a minimal valid input and verifies schema compliance.
- Snapshot the full tool list and schemas; diff on every PR to catch accidental contract changes.
- Validate output schemas in tests rather than at runtime.

## Documentation

- Provide a README covering purpose, exposed tools, required environment variables, and setup.
- Document every parameter with a description, allowed values, and constraints — in the schema, not just in prose.
- Document side effects, rate limits, and latency expectations for each tool.
- Maintain a CHANGELOG and follow semantic versioning; never reuse a tool name for different behavior — version instead.

## Deployment

- Include a semantic version in server metadata and bump it on every change.
- For container images: use a minimal base, set a non-root `USER`, pin the base by digest, include a `HEALTHCHECK`, and commit a `.dockerignore`.
- Fail fast on missing required environment variables at startup.
- Bind to localhost by default for local servers; require explicit configuration to listen externally.
- In CI, run formatters, linters, secret scanners, and dependency auditors; fail the build on any violation.