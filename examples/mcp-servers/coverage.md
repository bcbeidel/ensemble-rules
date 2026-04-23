# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

**Errored models** (excluded from matrix): xai/grok-3-mini

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | Count |
|---|---|---|---|---|---|---|---|
| **(contested) For I/O-bound tools, use async/await or threading to avoid blocking concurrent calls.** This is a performance win but adds complexity; acceptable if your runtime supports it | Concurrency & State |  |  |  | ✓ |  | 1 |
| **Avoid dynamic code generation or `eval`-like constructs; never interpolate tool input into code or queries.** This is a vector for injection attacks | Code & Implementation Quality |  |  |  | ✓ |  | 1 |
| **Avoid module-level mutable state.** Breaks the moment the server runs in HTTP mode with concurrent requests | Style |  |  | ✓ |  |  | 1 |
| **Cache expensive results (e.g., API responses, database queries) if safe; document cache TTL and invalidation strategy.** But never cache sensitive data (tokens, secrets) or mutable state | Performance |  |  |  | ✓ |  | 1 |
| **Check input length and cardinality limits upfront; reject requests that exceed documented bounds.** A tool that accepts "list of IDs" should enforce a maximum (e.g., 1000) to prevent DoS | Input Validation |  |  |  | ✓ |  | 1 |
| **Declare one tool per distinct operation; do not multiplex with a `mode` parameter.** (contested) Multiplexed tools confuse model tool-selection and obscure permissions | Structure |  |  | ✓ |  |  | 1 |
| **Default every tool to read-only; require explicit opt-in for mutation.** Most MCP damage comes from the model calling write tools it thought were queries | Safety |  |  | ✓ |  |  | 1 |
| **Define every tool's input with a strict schema (Zod, Pydantic, or JSON Schema).** Unvalidated input means the LLM's mistakes become your bugs | Schemas & Validation |  |  | ✓ |  |  | 1 |
| **Define every tool's name, description, and input schema explicitly and upfront.** This is your API contract; AI assistants and humans rely on it for correctness | Structure & Declaration |  |  |  | ✓ |  | 1 |
| **Disallow or restrict operations that consume unbounded resources (infinite loops, large list returns, bulk operations).** A tool that lists 1 million objects will hang the AI | Safety & Capability Bounds |  |  |  | ✓ |  | 1 |
| **Distinguish retryable from non-retryable failures in the error code.** Rate limits and outages should be retried; bad input should not | Error Handling |  |  | ✓ |  |  | 1 |
| **Distinguish transient errors (timeout, network glitch) from permanent ones (auth failure, resource not found) in the error type.** This lets the AI decide whether to retry without guessing | Error Handling & Reporting |  |  |  | ✓ |  | 1 |
| **Do not assume stdio or HTTP transport guarantees ordering or atomicity.** Tool calls can arrive out of order; responses may be retried | Concurrency & State |  |  |  | ✓ |  | 1 |
| **Do not perform nested lookups or privilege checks after the initial request; validate all constraints upfront.** A tool that resolves symlinks after an allowlist check might bypass the check | Safety & Capability Bounds |  |  |  | ✓ |  | 1 |
| **Do not suppress or silently log errors; always return them to the caller.** A tool that catches an exception and returns `{ "status": "ok" }` is deceptive | Error Handling & Reporting |  |  |  | ✓ |  | 1 |
| **Document any side effects and latency assumptions (e.g., "creates a resource in S3; takes 2–5 seconds").** The AI needs to know what will happen | Documentation & Discoverability |  |  |  | ✓ |  | 1 |
| **Document every tool parameter, allowed values, and constraints in the schema and in code comments.** Do not require reverse-engineering from examples | Documentation & Discoverability |  |  |  | ✓ |  | 1 |
| **Emit a structured `startup` log line with server name, version, and tool count.** Makes client misconfiguration diagnosable in one grep | Observability |  |  | ✓ |  |  | 1 |
| **Enforce strict type validation: parse integers as integers, booleans as booleans, reject type mismatches.** Implicit coercion (e.g., "true" → true) is a source of subtle bugs | Input Validation |  |  |  | ✓ |  | 1 |
| **Expose a `/_health` endpoint (HTTP) or equivalent (stdio) for liveness checks; it should confirm the server is responsive, not just alive.** "Server is running but all tools time out" is a failure mode the health check should catch | Transport & Runtime |  |  |  | ✓ |  | 1 |
| **Flush or `await` all writes before process exit.** Truncated final messages look like server crashes to clients | Transport & I/O |  |  | ✓ |  |  | 1 |
| **For HTTP transport, require authentication on every request; do not trust session cookies alone.** MCP servers are often proxied; assume the network is hostile | Transport & I/O |  |  | ✓ |  |  | 1 |
| **For path or filename inputs, validate against an explicit allowlist of directories or patterns; reject `..` and absolute paths outside the allowlist.** Directory traversal attacks are real and trivial to miss | Input Validation |  |  |  | ✓ |  | 1 |
| **For string inputs, check encoding (UTF-8) and reject null bytes and other control characters unless explicitly allowed.** Null bytes hide attacks; control characters break logs | Input Validation |  |  |  | ✓ |  | 1 |
| **For tools that return lists or large data, implement pagination or size limits (e.g., "returns up to 1000 items").** Unbounded responses will hang the AI and waste bandwidth | Performance |  |  |  | ✓ |  | 1 |
| **Give destructive tools distinct names (`delete_*`, `drop_*`, `force_*`).** Name-level signals are the only safety layer some clients surface to users | Safety |  |  | ✓ |  |  | 1 |
| **Group related tools into a single MCP Server; split when a server exceeds 20 tools or serves disjoint capabilities.** One server per logical domain (e.g., "database" or "file operations") | Structure & Declaration |  |  |  | ✓ |  | 1 |
| **Handle EOF and connection drops gracefully; do not assume the client will always read your output.** The AI might kill the connection or timeout; your code should not crash or leak resources | Transport & Runtime |  |  |  | ✓ |  | 1 |
| **If a tool mutates state (write, delete, modify), require an explicit confirmation token or enforce a dry-run mode.** This prevents accidental damage when an AI assistant misunderstands the user's intent | Safety & Capability Bounds |  |  |  | ✓ |  | 1 |
| **If a tool times out, return immediately with a `timeout` error; do not wait for the operation to finish.** Timeouts are hard stops, not suggestions | Error Handling & Reporting |  |  |  | ✓ |  | 1 |
| **If your server accepts a configuration file, validate it strictly and fail at startup if it is invalid.** Silent config errors are invisible time bombs | Secrets & Configuration |  |  |  | ✓ |  | 1 |
| **If your server handles multiple concurrent tool calls, use explicit locking or a concurrency-safe data structure to protect shared state.** Race conditions are silent and devastating | Concurrency & State |  |  |  | ✓ |  | 1 |
| **If your server maintains in-memory state (caches, sessions), document its lifetime and scope.** State in a stateless function is a footgun | Concurrency & State |  |  |  | ✓ |  | 1 |
| **Implement allowlist-based access control: if a tool accepts a resource identifier (path, table name, API endpoint), validate it against a hard-coded or user-configured allowlist.** Allowlists are safer than denylists because they fail secure | Safety & Capability Bounds |  |  |  | ✓ |  | 1 |
| **Import and use established libraries for cryptography, hashing, and data validation; do not roll your own.** Cryptography is easy to get subtly wrong | Code & Implementation Quality |  |  |  | ✓ |  | 1 |
| **Include a "smoke test" that invokes all tools and confirms they return valid schemas.** This catches schema drift and unexpected errors at deployment time | Testing |  |  |  | ✓ |  | 1 |
| **Include a README explaining what the server does, which tools it exposes, and any setup required (env vars, auth, dependencies).** Deployers need to know what they're running | Documentation & Discoverability |  |  |  | ✓ |  | 1 |
| **Include a one-sentence summary and a one-paragraph description for each tool.** The summary appears in AI context windows; the paragraph aids debugging and auditing | Structure & Declaration |  |  |  | ✓ |  | 1 |
| **Include a test with deliberately malformed input for each tool.** Confirms validation actually rejects what it should | Testing |  |  | ✓ |  |  | 1 |
| **Include one or two example tool invocations and responses in the README.** Examples are the fastest way to understand a tool | Documentation & Discoverability |  |  |  | ✓ |  | 1 |
| **Include the offending argument name and value in validation errors.** The model fixes what it can see | Error Handling |  |  | ✓ |  |  | 1 |
| **Keep each tool's schema, handler, and tests in one file.** Co-location makes the contract visible; hunting across files hides schema bugs | Structure |  |  | ✓ |  |  | 1 |
| **Keep tool handlers under 50 lines; extract helpers.** Long handlers hide the request/response shape that matters for model behavior | Style |  |  | ✓ |  |  | 1 |
| **List any rate limits, quotas, or resource constraints on the server or individual tools.** Otherwise the AI will discover them the hard way | Documentation & Discoverability |  |  |  | ✓ |  | 1 |
| **Log enough context to trace tool calls in production without logging secrets.** Include request IDs, parameters (except passwords), response size, and latency | Secrets & Configuration |  |  |  | ✓ |  | 1 |
| **Log every mutating operation (who, what, when, where); include the operation input and result.** Humans need audit trails to detect misuse and triage damage | Safety & Capability Bounds |  |  |  | ✓ |  | 1 |
| **Log every tool invocation with name, arguments, duration, and outcome.** You will need this the first time something goes wrong in production | Observability |  |  | ✓ |  |  | 1 |
| **Mark optional parameters optional; do not fake it with "" or -1 sentinels.** The model respects the schema; lying in the schema corrupts its planning | Schemas & Validation |  |  | ✓ |  |  | 1 |
| **Monitor and alert on latency, error rate, and resource usage (CPU, memory, file descriptors).** Silent degradation will wreck the AI's experience | Performance |  |  |  | ✓ |  | 1 |
| **Name tools `verb_noun` in snake_case.** Consistent naming helps the model select the right tool; e.g., `list_users`, `delete_issue` | Structure |  |  | ✓ |  |  | 1 |
| **Never expose a generic `execute_sql`, `run_shell`, or `eval` tool in production.** (contested) These collapse the entire safety model into one prompt-injection away from disaster | Safety |  |  | ✓ |  |  | 1 |
| **Never expose a tool that can escalate privileges, read secrets, or write to sensitive system paths without explicit documentation and user consent.** If your tool can read `$HOME/.ssh`, say so prominently | Safety & Capability Bounds |  |  |  | ✓ |  | 1 |
| **Never hard-code secrets (API keys, passwords, tokens) in source code or configuration files.** Use environment variables, a secrets manager, or command-line flags | Secrets & Configuration |  |  |  | ✓ |  | 1 |
| **Never swallow an exception and return an empty result.** Silent failure causes infinite retry loops and silent data loss | Error Handling |  |  | ✓ |  |  | 1 |
| **Never write to stdout from a stdio-transport server except via the SDK.** Stray `print`/`console.log` corrupts the JSON-RPC frame | Transport & I/O |  |  | ✓ |  |  | 1 |
| **On error, return a structured response including error type (e.g., `validation_error`, `timeout`, `permission_denied`), a human-readable message, and the raw error detail.** The AI needs to know what happened so it can decide whether to retry or ask the user | Error Handling & Reporting |  |  |  | ✓ |  | 1 |
| **Paginate any tool that can return more than ~50 items.** Unbounded lists burn the model's context and money | Response Size & Performance |  |  | ✓ |  |  | 1 |
| **Pin the MCP SDK to an exact version.** The protocol and SDKs are unstable; floating versions cause silent behavior changes | Structure |  |  | ✓ |  |  | 1 |
| **Prefer `async` handlers uniformly; do not mix sync and async.** Mixed execution models cause subtle deadlocks under load | Style |  |  | ✓ |  |  | 1 |
| **Prefer explicit over implicit | Code & Implementation Quality |  |  |  | ✓ |  | 1 |
| **Profile your tools under realistic load before production; document the latency percentiles (p50, p95, p99) and throughput.** "It's fast" is not acceptable; "p95 latency 200 ms, 100 req/s" is | Performance |  |  |  | ✓ |  | 1 |
| **Redact secrets and PII in logs by field name, not pattern matching.** Pattern matching misses; allowlists don't | Observability |  |  | ✓ |  |  | 1 |
| **Require a confirmation token argument for irreversible operations.** Forces the model to surface intent to the user before acting | Safety |  |  | ✓ |  |  | 1 |
| **Return IDs and summaries by default; provide a separate `get_*` tool for full detail.** Lets the model fetch only what it needs | Response Size & Performance |  |  | ✓ |  |  | 1 |
| **Return errors as structured MCP errors with a stable `code` and actionable `message`.** The model uses the message to self-correct; stack traces teach it nothing useful | Error Handling |  |  | ✓ |  |  | 1 |
| **Rotate credentials regularly and detect rotation in tests (e.g., confirm a rotated key fails).** Stale credentials will surface in production at the worst time | Secrets & Configuration |  |  |  | ✓ |  | 1 |
| **Rule:** Choose the transport protocol (stdio vs | Performance |  |  |  |  | ✓ | 1 |
| **Rule:** Clearly document and aim for idempotency in tool actions where possible | Tool Definition |  |  |  |  | ✓ | 1 |
| **Rule:** Define tools declaratively in a well-known, machine-readable format | Tool Definition |  |  |  |  | ✓ | 1 |
| **Rule:** Design the server to be stateless | Structure |  |  |  |  | ✓ | 1 |
| **Rule:** Do not execute shell commands constructed from LLM-provided input | Safety |  |  |  |  | ✓ | 1 |
| **Rule:** Encode all string data as UTF-8 | Protocol & Communication |  |  |  |  | ✓ | 1 |
| **Rule:** Expose all logic through a single, main executable | Structure |  |  |  |  | ✓ | 1 |
| **Rule:** For HTTP servers, follow standard RESTful practices for resources and verbs | Protocol & Communication |  |  |  |  | ✓ | 1 |
| **Rule:** For HTTP servers, provide an OpenAPI specification for all endpoints | Protocol & Communication |  |  |  |  | ✓ | 1 |
| **Rule:** Implement and enforce a timeout for every tool execution | Performance |  |  |  |  | ✓ | 1 |
| **Rule:** Isolate tool execution from the host system using sandboxing techniques | Safety |  |  |  |  | ✓ | 1 |
| **Rule:** Log internal errors and diagnostics to `stderr` or a dedicated log file | Error Handling |  |  |  |  | ✓ | 1 |
| **Rule:** Minimize external dependencies | Structure |  |  |  |  | ✓ | 1 |
| **Rule:** Never write logs or other unstructured debug output to `stdout` | Error Handling |  |  |  |  | ✓ | 1 |
| **Rule:** Prefer allow-lists over block-lists for all operations | Safety |  |  |  |  | ✓ | 1 |
| **Rule:** Prevent tool outputs from leaking sensitive environment or user data | Safety |  |  |  |  | ✓ | 1 |
| **Rule:** Return structured errors in the response body | Error Handling |  |  |  |  | ✓ | 1 |
| **Rule:** Separate protocol handling, tool dispatch, and tool implementation into distinct modules | Structure |  |  |  |  | ✓ | 1 |
| **Rule:** Support streaming for tool inputs or outputs that may be large | Performance |  |  |  |  | ✓ | 1 |
| **Rule:** Use JSON Schema to define tool parameters | Tool Definition |  |  |  |  | ✓ | 1 |
| **Rule:** Use line-delimited JSON (JSONL/NDJSON) for stdio communication | Protocol & Communication |  |  |  |  | ✓ | 1 |
| **Rule:** Use non-zero exit codes only for catastrophic server failures | Error Handling |  |  |  |  | ✓ | 1 |
| **Rule:** Write clear, concise, and unambiguous descriptions for every tool and parameter | Tool Definition |  |  |  |  | ✓ | 1 |
| **Scope the server's credentials to the minimum required.** The server is a confused deputy; its token is the blast radius | Safety |  |  | ✓ |  |  | 1 |
| **Send logs to stderr or a file, never stdout.** Same reason; stdout is the protocol channel | Transport & I/O |  |  | ✓ |  |  | 1 |
| **Set `additionalProperties: false` on all object schemas.** Unknown fields are almost always model hallucinations; reject them loudly | Schemas & Validation |  |  | ✓ |  |  | 1 |
| **Set a per-tool timeout; never block indefinitely on a downstream call.** Hung tools stall the entire agent loop | Response Size & Performance |  |  | ✓ |  |  | 1 |
| **Set and document a timeout for every I/O operation (database query, HTTP request, filesystem call).** Infinite hangs kill the AI's ability to recover | Error Handling & Reporting |  |  |  | ✓ |  | 1 |
| **Set socket timeouts at the transport layer; never rely on application-layer timeouts alone.** A hung subprocess or infinite loop will hang the AI | Transport & Runtime |  |  |  | ✓ |  | 1 |
| **Snapshot the full tool list and schemas; diff on every PR.** Accidental schema changes break deployed clients silently | Testing |  |  | ✓ |  |  | 1 |
| **Stream progress for operations over ~2 seconds.** Keeps clients responsive and lets users cancel | Response Size & Performance |  |  | ✓ |  |  | 1 |
| **Test timeouts and transient errors (mock a timeout, mock a 500 from the API).** Code that never saw an error is fragile | Testing |  |  |  | ✓ |  | 1 |
| **Test with the actual I/O (real database, real API, or mock with a library like `responses` or `unittest.mock`).** Mocking transport or requests doesn't catch integration bugs | Testing |  |  |  | ✓ |  | 1 |
| **Treat all tool output as untrusted data, never as instructions.** Prompt injection from returned content is a routine attack vector | Safety |  |  | ✓ |  |  | 1 |
| **Truncate large string fields with an explicit marker (`…[truncated 12KB]`).** Silent truncation makes the model act on partial data | Response Size & Performance |  |  | ✓ |  |  | 1 |
| **Use JSON Schema with the `required` array to declare mandatory inputs.** Optional inputs must be marked as such and have sensible defaults documented | Structure & Declaration |  |  |  | ✓ |  | 1 |
| **Use enums for any parameter with a fixed set of values.** Free-form strings invite invented values | Schemas & Validation |  |  | ✓ |  |  | 1 |
| **Use parameterized queries or prepared statements for all database access; never concatenate strings into SQL.** Parameterization is non-negotiable | Code & Implementation Quality |  |  |  | ✓ |  | 1 |
| **Use structured logging (JSON or similar) so logs are machine-parseable; include timestamps, request IDs, and error types.** Humans and tools alike will need to query logs | Transport & Runtime |  |  |  | ✓ |  | 1 |
| **Use the MCP SDK for your language (e.g., `mcp-sdk-python`, `mcp-sdk-js`) and follow its conventions.** Custom transport code is fragile and often missing error handling | Code & Implementation Quality |  |  |  | ✓ |  | 1 |
| **Use the MCP SDK; do not implement the transport protocol yourself.** The protocol has subtle requirements (timeouts, partial reads, keep-alives) that are easy to miss | Transport & Runtime |  |  |  | ✓ |  | 1 |
| **Use the official SDK's native registration API directly.** Wrapping it adds indirection that obscures the schema the model actually sees | Structure |  |  | ✓ |  |  | 1 |
| **Validate API keys, tokens, and credentials synchronously at tool invocation time, not lazily.** Fail immediately if auth is invalid, don't pass it to a downstream service and wait for rejection | Input Validation |  |  |  | ✓ |  | 1 |
| **Validate all tool inputs against the schema before processing; reject invalid inputs with a structured error message naming the field and violation.** A malformed request should fail in 10 ms with a clear message, not hang or corrupt state | Input Validation |  |  |  | ✓ |  | 1 |
| **Validate output schemas in tests, not at runtime.** Runtime output validation adds cost without catching model-facing bugs the schema already prevents | Schemas & Validation |  |  | ✓ |  |  | 1 |
| **Write a test that invokes each tool through the MCP protocol, not by calling the handler directly.** Direct-call tests miss schema and transport bugs | Testing |  |  | ✓ |  |  | 1 |
| **Write code for readability, not conciseness | Code & Implementation Quality |  |  |  | ✓ |  | 1 |
| **Write tests for every tool; cover success cases, invalid inputs, boundary conditions, and error cases.** A tool with no tests is untested in production | Testing |  |  |  | ✓ |  | 1 |
| **Write tool descriptions for the model, not humans.** Include when to use it, when not to, and what it returns in 1–3 sentences | Structure |  |  | ✓ |  |  | 1 |
| *Rationale:* A single entry point simplifies deployment, discovery, and execution by the AI orchestrator | Structure |  |  |  |  | ✓ | 1 |
| *Rationale:* A single, universal encoding prevents a wide class of errors when dealing with international text | Protocol & Communication |  |  |  |  | ✓ | 1 |
| *Rationale:* Adhering to web standards makes the server more predictable and easier to integrate with standard tooling | Protocol & Communication |  |  |  |  | ✓ | 1 |
| *Rationale:* Allow-lists for file paths, network hosts, and permissions provide a much stronger security posture than trying to block known-bad patterns | Safety |  |  |  |  | ✓ | 1 |
| *Rationale:* Declarative definitions serve as a single source of truth for validation, help text, and invocation | Tool Definition |  |  |  |  | ✓ | 1 |
| *Rationale:* Fewer dependencies reduce attack surface, decrease binary size, and simplify dependency management | Structure |  |  |  |  | ✓ | 1 |
| *Rationale:* Idempotent tools can be safely retried by the client on transient failures | Tool Definition |  |  |  |  | ✓ | 1 |
| *Rationale:* JSON Schema is a powerful and standard way to describe data structures, enabling automatic validation and type checking | Tool Definition |  |  |  |  | ✓ | 1 |
| *Rationale:* Sandboxing (e.g., containers, limited user accounts, `chroot`) is the strongest defense against malicious tool behavior | Safety |  |  |  |  | ✓ | 1 |
| *Rationale:* Stateless servers are easier to test, scale, and reason about; state should be managed by the client | Structure |  |  |  |  | ✓ | 1 |
| *Rationale:* Streaming avoids high memory usage and allows for processing data larger than available RAM | Performance |  |  |  |  | ✓ | 1 |
| *Rationale:* Structured errors (e.g., a JSON object with `code` and `message` fields) allow clients to handle failures programmatically | Error Handling |  |  |  |  | ✓ | 1 |
| *Rationale:* The LLM uses these descriptions to decide which tool to use and how to use it; clarity is paramount | Tool Definition |  |  |  |  | ✓ | 1 |
| *Rationale:* This is the primary vector for command injection attacks; use language-specific libraries for system interaction | Safety |  |  |  |  | ✓ | 1 |
| *Rationale:* This provides a robust, widely-supported, and easy-to-parse streaming message format | Protocol & Communication |  |  |  |  | ✓ | 1 |
| *Rationale:* This provides machine-readable documentation for discovery, testing, and client generation | Protocol & Communication |  |  |  |  | ✓ | 1 |
| *Rationale:* This separates diagnostic information from the primary data channel, aiding in debugging without disrupting operation | Error Handling |  |  |  |  | ✓ | 1 |
| *Rationale:* This separation of concerns makes the server easier to maintain and extend with new tools | Structure |  |  |  |  | ✓ | 1 |
| *Rationale:* Timeouts prevent a single hanging tool from making the entire server unresponsive | Performance |  |  |  |  | ✓ | 1 |
| *Rationale:* Tool execution errors are predictable and should be reported as structured data in the response, not by crashing the server | Error Handling |  |  |  |  | ✓ | 1 |
| *Rationale:* Tools must sanitize their output to avoid exposing API keys, internal IP addresses, or PII to the LLM | Safety |  |  |  |  | ✓ | 1 |
| *Rationale:* Use stdio for low-latency local communication; use HTTP for network-accessible or distributed services | Performance |  |  |  |  | ✓ | 1 |
| *Rationale:* `stdout` is the data channel for protocol messages; any other output will corrupt the stream and break the client | Error Handling |  |  |  |  | ✓ | 1 |
| Add a HEALTHCHECK to container images | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Add contract tests covering initialize and listing of tools/resources/prompts | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Apply backpressure when streaming to match consumer speed | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Audience: Engineers building production-grade MCP Servers; AI coding assistants generating or modifying servers | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Authenticate HTTP servers (token/mTLS) and never expose unauthenticated endpoints to the public internet | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Batch or pipeline backend calls to avoid N+1 patterns | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Bind to localhost by default; require explicit config to listen externally | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Build minimal, non-root container images and set USER explicitly | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Cap response sizes and stream or paginate large outputs | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Declare side effects and idempotency clearly in tool descriptions | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Default resource list pagination to a sane size (≤ 1000); support cursors | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Describe side effects, idempotency, and rollback for mutating tools | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Do catch and log exceptions adequately | Error Handling |  | ✓ |  |  |  | 1 |
| Do implement caching for frequent requests | Performance |  | ✓ |  |  |  | 1 |
| Do not write anything except protocol frames to stdout on stdio; write all logs to stderr | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Do sanitize all incoming data | Safety |  | ✓ |  |  |  | 1 |
| Do use a modular design to separate concerns | Structure |  | ✓ |  |  |  | 1 |
| Do use consistent naming conventions for variables and functions | Style |  | ✓ |  |  |  | 1 |
| Do use external libraries for common functionalities where possible | Contestable Areas |  | ✓ |  |  |  | 1 |
| Document required environment variables and configuration in README | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Don't allow blocking operations in main threads | Performance |  | ✓ |  |  |  | 1 |
| Don't exceed a single responsibility for a module | Structure |  | ✓ |  |  |  | 1 |
| Don't hard-code secrets in the codebase | Safety |  | ✓ |  |  |  | 1 |
| Don't ignore error responses from external systems | Error Handling |  | ✓ |  |  |  | 1 |
| Don't optimize prematurely | Contestable Areas |  | ✓ |  |  |  | 1 |
| Don't use abbreviations that may not be universally understood | Style |  | ✓ |  |  |  | 1 |
| Emit structured JSON logs to stderr with time, level, request_id, tool, duration, and outcome | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Enforce an allowlist for outbound hosts/ports for HTTP/DNS egress in production | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Enforce formatting and linting in CI | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Enforce per-request wall-clock timeouts and memory ceilings; fail fast when exceeded | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Export metrics: requests, errors, latency, retries, and timeouts at minimum | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Expose tools/resources/prompts with stable, lowercase snake_case names | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Fail fast on missing required environment variables at startup | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Goal: Specific, opinionated rules that improve correctness, safety, operability, and performance | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Implement graceful shutdown on SIGTERM/SIGINT and drain in-flight work | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Include a .dockerignore to keep images small | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Include an mcp.json manifest at the repo root for local discovery | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Include golden tests for common tool calls and for error paths | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Keep names stable; never reuse a name for different behavior—version instead | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Keep one server per operational responsibility or integration | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Maintain a CHANGELOG and follow semver for breaking changes | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Map backend failures to stable, machine-parseable error codes with a clear message and structured data | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Never crash the process on bad input; return an error and continue serving | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Never include environment variables, tokens, or keys in error messages | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Never interpolate user input into shell commands; use parameterized APIs or safe exec variants | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Pin base images by digest and dependencies to exact versions | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Pin dependencies and scan for vulnerabilities in CI | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Propagate and log a correlation/request ID across all backend calls | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Provide /health (liveness) and /ready (readiness) endpoints for HTTP servers | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Provide a semantic version in server metadata and bump on changes | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Provide concise, high-signal descriptions with at least one minimal example per tool | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Record auditable tool invocations (names, parameter hashes, duration) with PII minimization | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Redact secrets and PII in logs and tool outputs unless explicitly required | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Require TLS for HTTP transport and backend calls in production | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Restrict filesystem access to explicit allowlisted roots and block path traversal | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Retry only idempotent operations with exponential backoff and jitter | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Return partial results with an explicit incomplete indicator instead of silently truncating | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Reuse connections (HTTP/DB pooling) instead of reconnecting per call | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Run static secret-scans and dependency audits in CI | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Run with least-privilege credentials scoped to required resources only | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Scope: Model Context Protocol servers that expose tools, resources, or prompts to AI assistants over stdio or HTTP | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Set explicit timeouts on every outbound network or storage call and make them configurable | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Support cancellation/abort if the SDK provides it, and promptly stop work when cancelled | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Surface validation errors listing exactly which fields are invalid and why | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Test against multiple client versions/implementations when feasible | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Use the official MCP SDK for your language, not ad-hoc JSON-RPC plumbing | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Validate all tool inputs with JSON Schema and reject unknown properties | Section 2: Rules File | ✓ |  |  |  |  | 1 |
| Write short, imperative descriptions with one minimal example per tool | Section 2: Rules File | ✓ |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

