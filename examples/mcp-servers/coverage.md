# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| (contested) Do prioritize performance optimizations where user pain points are evident | Controversial |  | ✓ |  |  |  |  | 1 |
| (contested) Don’t adhere strictly to a single style guide | Controversial |  | ✓ |  |  |  |  | 1 |
| **Block SSRF: reject private IP ranges, metadata endpoints, and non-allowlisted hosts in any fetch tool.** LLMs will happily be told to fetch `169.254.169.254` | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Cache idempotent reads with short TTLs keyed by arguments.** Models repeat identical calls within a session | Performance |  |  | ✓ |  |  |  | 1 |
| **Declare a JSON Schema for every tool input and validate before dispatch.** Models invent parameters; unvalidated input is a vulnerability | Structure & Architecture |  |  | ✓ |  |  |  | 1 |
| **Distinguish retryable (transient) from non-retryable (bad input) errors in the message.** Prevents infinite retry loops | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Do not authenticate based on tool arguments.** The server's identity is fixed; arguments are model-supplied and untrusted | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Document required environment variables and fail fast at startup if any are missing.** Silent misconfiguration surfaces as confusing tool errors later | Style |  |  | ✓ |  |  |  | 1 |
| **Expose long-lived data as resources, not tools.** Resources are cacheable and discoverable; tools are for actions | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Fail closed on ambiguity.** If you can't determine intent safely, return an error asking for clarification rather than guessing | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Flush stdout after every message and handle SIGPIPE/EOF cleanly.** Hanging servers strand clients | Transport |  |  | ✓ |  |  |  | 1 |
| **For HTTP transport, require authentication and bind to localhost by default.** An unauthenticated MCP server on `0.0.0.0` is a remote code execution primitive | Transport |  |  | ✓ |  |  |  | 1 |
| **Fuzz tool inputs with malformed, oversized, and adversarial strings.** The LLM is a fuzzer; pre-empt it | Testing |  |  | ✓ |  |  |  | 1 |
| **Include a short human-readable `summary` field alongside structured data.** Gives the model something to quote without re-serializing | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Include an end-to-end test that runs the server over its real transport.** stdio framing bugs only appear end-to-end | Testing |  |  | ✓ |  |  |  | 1 |
| **Keep each tool handler under ~50 lines; push logic into domain modules.** Handlers should validate, call, format, return | Style |  |  | ✓ |  |  |  | 1 |
| **Keep the tool surface small and coarse-grained.** Fewer, task-complete tools outperform many fine-grained ones because models reason better over small toolsets | Structure & Architecture |  |  | ✓ |  |  |  | 1 |
| **Log every tool invocation with arguments, caller, and result status.** Auditability is non-negotiable for agent-driven systems | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Make all `get_*`, `list_*`, `search_*` tools strictly read-only and idempotent.** Violating this breaks the model's ability to plan safely | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Measure and expose p50/p95 latency per tool.** You cannot tune what you do not measure | Performance |  |  | ✓ |  |  |  | 1 |
| **Name tools as `verb_object` in snake_case.** Predictable naming improves model tool selection | Structure & Architecture |  |  | ✓ |  |  |  | 1 |
| **Never return stack traces or internal paths to the model.** They leak internals and waste tokens; log them server-side with a correlation ID | Error Handling |  |  | ✓ |  |  |  | 1 |
| **On stdio transport, write nothing to stdout except protocol messages.** Logs go to stderr; a stray `print` corrupts the session | Transport |  |  | ✓ |  |  |  | 1 |
| **Paginate any list endpoint and cap default page size at a few dozen items.** Unbounded lists overflow context and silently truncate reasoning | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Parameterize all database queries and shell invocations; never string-concatenate.** Standard injection defenses apply doubly here | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Pin SDK and dependency versions.** Protocol-level breakage is hard to diagnose from the model's side | Style |  |  | ✓ |  |  |  | 1 |
| **Prefer one coarse tool that returns joined data over N chatty tools the model must chain.** Round trips dominate latency | Performance |  |  | ✓ |  |  |  | 1 |
| **Redact secrets from logs and from tool outputs.** Assume logs will be read and outputs will be echoed back into prompts | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Reject unknown properties in input schemas (`additionalProperties: false`).** Silent acceptance hides model mistakes and masks bugs | Structure & Architecture |  |  | ✓ |  |  |  | 1 |
| **Require an explicit `confirm: true` or dry-run-then-execute flow for destructive operations.** Models will call delete tools based on injected instructions otherwise | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Return errors as structured results with `isError: true`, not by throwing over the wire.** The protocol requires it and the model can recover from structured errors | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Return structured JSON with a stable shape; use `null`, not omission, for missing fields.** Shape stability lets the model parse reliably across calls | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Run the server with least-privilege credentials scoped to the tools exposed.** A read-only tool gets read-only DB creds, not the app's primary role | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Sandbox filesystem tools to an explicit allowlist of roots and resolve symlinks before checks.** Path traversal via `..` and symlinks is the most common MCP exploit | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Separate protocol, domain, and transport layers.** Tool handlers should be thin wrappers over pure domain functions so logic is testable without the MCP runtime | Structure & Architecture |  |  | ✓ |  |  |  | 1 |
| **Set explicit timeouts on all outbound calls (DB, HTTP, subprocess).** A hung tool hangs the entire assistant turn | Transport |  |  | ✓ |  |  |  | 1 |
| **Snapshot-test tool descriptions.** Prompt regressions silently degrade model behavior; treat descriptions as code | Testing |  |  | ✓ |  |  |  | 1 |
| **State side effects explicitly in the description ("This writes to disk", "This sends email").** The model uses this to decide whether to ask the user first | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Stream results when the protocol and tool semantics allow.** Reduces time-to-first-token for the assistant's next step | Performance |  |  | ✓ |  |  |  | 1 |
| **Target sub-second latency for common tool calls.** Each call blocks the model's reasoning loop | Performance |  |  | ✓ |  |  |  | 1 |
| **Treat every string argument as untrusted and potentially adversarial.** Prompt injection can originate from any document the model has seen | Safety & Security |  |  | ✓ |  |  |  | 1 |
| **Truncate large string fields and return a `truncated: true` flag plus a fetch handle.** Dumping megabytes into context degrades model performance | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Use the official SDK for your language (TypeScript, Python) rather than hand-rolling the protocol.** The spec evolves; SDKs track it | Style |  |  | ✓ |  |  |  | 1 |
| **Version your server and advertise it in `serverInfo`.** Clients and logs need to distinguish incompatible behaviors | Structure & Architecture |  |  | ✓ |  |  |  | 1 |
| **Write error messages that tell the model how to fix the call.** Include the offending field, the expected format, and an example | Error Handling |  |  | ✓ |  |  |  | 1 |
| **Write tool descriptions as prompts, not docstrings.** Include purpose, when to use it, when *not* to use it, units, and an example call | Tool & Resource Design |  |  | ✓ |  |  |  | 1 |
| **Write unit tests against domain functions and contract tests against tool schemas.** Schema drift is the most common regression | Testing |  |  | ✓ |  |  |  | 1 |
| Add golden tests for deterministic outputs and ordering | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add tracing spans around each tool call and upstream dependency | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Allow resume/retry via idempotency keys or operation IDs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Announce capability changes during initialization and keep a changelog | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Apply concurrency limits and backpressure per tool | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Apply least privilege to system, network, and data access | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers and AI coding assistants implementing, reviewing, or operating MCP Servers for production use | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Bias toward deterministic, compact outputs with explicit next steps | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cache hot, immutable lookups with bounded TTLs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Classify data and tag outputs with sensitivity levels | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Co-locate each tool/resource schema, validator, and implementation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Create contract tests that validate schema, examples, and round-trip behavior | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default resources to read-only and non-recursive | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default-deny filesystem writes and outbound network egress | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define each tool with a unique name, a clear description, and explicit input/output schemas | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Define every tool input and output with strict JSON Schema | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define tool schemas using a strict, code-native validation library (e.g., Pydantic, Zod) | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Design servers to be stateless | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Distinguish user errors (4xx-like), server errors (5xx-like), and rate limits distinctly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do enforce input validation and sanitization for all incoming requests | Safety |  |  |  |  |  | ✓ | 1 |
| Do follow consistent naming conventions, such as camelCase for variables and PascalCase for classes | Style |  |  |  |  |  | ✓ | 1 |
| Do handle all potential errors, including network failures and invalid inputs, with informative responses | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do implement caching for frequently accessed resources (contested) | Performance |  |  |  |  |  | ✓ | 1 |
| Do implement retry mechanisms for transient errors like HTTP timeouts (contested) | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do implement structured error responses that clearly indicate the type of error | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do implement unit and integration tests for all critical components | Testing |  | ✓ |  |  |  |  | 1 |
| Do include inline comments for complex logic, but keep them concise | Style |  |  |  |  |  | ✓ | 1 |
| Do not expose raw stack traces or internal exceptions in API responses | Error Handling |  |  |  |  | ✓ |  | 1 |
| Do not log secrets, API keys, or personally identifiable information (PII) | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Do not return partial success as success; use explicit partial flags or separate streams | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize code into clear modules | Structure |  | ✓ |  |  |  |  | 1 |
| Do organize code into modular components, separating concerns like transport handling, request processing, and error management | Structure |  |  |  |  |  | ✓ | 1 |
| Do profile and optimize critical paths, such as request parsing and external API calls | Performance |  |  |  |  |  | ✓ | 1 |
| Do profile your application to identify bottlenecks regularly | Performance |  | ✓ |  |  |  |  | 1 |
| Do require authentication and authorization for access to sensitive resources | Safety |  |  |  |  |  | ✓ | 1 |
| Do use a standardized protocol schema for all interactions | Structure |  |  |  |  |  | ✓ | 1 |
| Do use consistent naming conventions throughout your code | Style |  | ✓ |  |  |  |  | 1 |
| Do validate all inputs against expected formats and types | Safety |  | ✓ |  |  |  |  | 1 |
| Document limits, side effects, and typical latencies per tool | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Document the purpose and parameters of each tool in the model-facing description | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Don't expose debug endpoints in production builds | Safety |  |  |  |  |  | ✓ | 1 |
| Don't mix transport-specific logic (e.g., stdio vs | Structure |  |  |  |  |  | ✓ | 1 |
| Don't propagate exceptions without logging and context | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't use magic numbers or strings; define them as constants instead | Style |  |  |  |  |  | ✓ | 1 |
| Don't use synchronous I/O for operations that could block the server | Performance |  |  |  |  |  | ✓ | 1 |
| Don’t allow business logic inside routing layers | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t hard-code sensitive information in your source code | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t optimize prematurely | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t rely solely on manual testing | Testing |  | ✓ |  |  |  |  | 1 |
| Don’t suppress exceptions without logging them | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t use magic numbers or strings in your codebase | Style |  | ✓ |  |  |  |  | 1 |
| Emit structured logs with request IDs, tool names, durations, sizes, and outcomes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce hard limits on the amount of data a tool can return | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Enforce per-tenant and global rate limits with clear error signals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce strict, short timeouts on all tool executions and external API calls | Performance |  |  |  |  | ✓ |  | 1 |
| Enforce timeouts, memory limits, and max payload sizes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Export metrics for request latency, error rates, and tool execution duration | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Expose metrics for QPS, p50/p95 latency, error rates, rate limits, and queue depth | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Expose mutations as tools and reads as resources by default | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fail fast with specific, stable error codes and messages | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Flush stdio writes promptly and avoid blocking reads | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fuzz tool inputs within schema bounds | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Gate new tools and capabilities behind feature flags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Gracefully drain on shutdown and complete in-flight work or cancel cleanly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Honor cancellation and deadlines from the client | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Implement a `/health` endpoint for automated health checks | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Implement all I/O-bound tool operations asynchronously | Performance |  |  |  |  | ✓ |  | 1 |
| Implement caching for frequently called, deterministic tools | Performance |  |  |  |  | ✓ |  | 1 |
| Implement capability negotiation and initialization exactly per spec | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Implement retries only for idempotent operations with bounded attempts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a machine-readable status and a human summary field separately | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include clear remediation tips in user-facing error summaries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include end-to-end tests with a reference MCP client | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include retryable=true/false and retry_after hints on errors | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep configuration externalized and immutable at runtime | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep each tool single-purpose and side-effect scoped | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep individual messages under a strict size cap; split or reference when larger | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep results deterministic and order-stable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Log every tool invocation with its unique ID, tool name, sanitized parameters, and outcome | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Log security-relevant events to an immutable audit sink | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Maintain allowlists for external hosts and protocols; block SSRF patterns | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make tool inputs small and outputs structured with explicit fields | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Map transport errors to protocol errors consistently and log both IDs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mark all required fields and use enums/ranges for constrained values | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Minimize data returned; send only what is necessary | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name tools with short verb-noun identifiers (snake_case) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never echo credentials or secrets back to the client | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never repurpose a tool name; deprecate and add a new one | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never use `eval`, `exec`, or shell command execution with direct model-provided input | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Normalize timestamps to ISO-8601 UTC | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Offload multi-minute tasks to a job model with progress updates | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer HTTP over stdio for all non-local deployments | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Prefer code generation from schemas for server types (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer returning handles and follow-up instructions over dumping huge data | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer small, composable tools over giant ones for typical flows (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer specific, single-purpose tools over general-purpose ones (e.g., `get_user` over `run_query`) | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Prefer stdio for local/desktop integrations; prefer HTTP for distributed, multi-tenant services (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer token-bucket or leaky-bucket with jittered retry guidance | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a deprecation path and telemetry on usage before removal | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a one-sentence description and one minimal example per tool | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide deletion/retention policies and enforce them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide pagination and filters for list-like results | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put examples under an examples field or docs block, not in prose descriptions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Rationale: Allows programmatic handling by the assistant while providing debug context | Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: Allows the model to self-correct malformed requests | Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: Denying by default is the only secure posture against a creative actor | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Rationale: Enables monitoring, alerting, and performance profiling | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Rationale: Enables standard networking, load balancing, health checks, and observability | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: Improves response time and reduces load on downstream systems | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Improves testability and makes it easier to support multiple protocols in the future | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: Leaking implementation details creates an unnecessary security risk | Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: Limits the blast radius in the event of a successful exploit | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Rationale: Makes logs machine-parseable for aggregation and automated analysis | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents a single slow tool from blocking the entire server process | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents ambiguity between a missing tool and a failing one | Error Handling |  |  |  |  | ✓ |  | 1 |
| Rationale: Prevents injection attacks, path traversals, and other input-based vulnerabilities | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Rationale: Protects sensitive data and complies with privacy regulations | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Rationale: Protects the server and the model from resource exhaustion attacks | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Rationale: Protects the server and upstream systems from resource exhaustion and cascading failures | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Provides a standard mechanism for load balancers and orchestrators to manage server lifecycle | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: Provides an essential audit trail for debugging and security analysis | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Rationale: Provides static analysis, IDE support, and robust runtime data validation | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Rationale: Reduces latency by reusing expensive-to-create connections | Performance |  |  |  |  | ✓ |  | 1 |
| Rationale: Reduces the attack surface and minimizes the potential for misuse | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Rationale: Simplifies scaling, reliability, and reasoning about behavior | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: The quality of the tool description directly impacts the model's ability to use it correctly | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Rationale: This is the foundational principle of MCP server security | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Rationale: This is the primary vector for remote code execution vulnerabilities | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Rationale: This manifest is the source of truth for the AI's capabilities and for runtime validation | Tool Definition |  |  |  |  | ✓ |  | 1 |
| Redact secrets from error messages and stack traces | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Register tools/resources declaratively in one place | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return a distinct error when an input fails schema validation | Error Handling |  |  |  |  | ✓ |  | 1 |
| Return an explicit error for unknown or disabled tools | Error Handling |  |  |  |  | ✓ |  | 1 |
| Return machine data as JSON fields and keep markdown in a separate summary field (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return operation handles for long-running work instead of blocking | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Return structured errors with a stable error code and a human-readable message | Error Handling |  |  |  |  | ✓ |  | 1 |
| Rotate credentials and validate at startup | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run the server as a non-root, least-privilege user with minimal capabilities | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run the server process with the minimum necessary operating system permissions | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Sample payloads safely and never log PII/secrets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Sanitize, validate, and type-check all input parameters before any processing | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Scope: Best practices for building Model Context Protocol (MCP) Servers that expose tools, resources, and prompts over stdio or HTTP | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Separate transport adapters from domain logic | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set per-tool latency budgets and enforce them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Stream or chunk results larger than a few hundred KB (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Structure the server logic to clearly separate protocol handling from tool execution | Protocol & Structure |  |  |  |  | ✓ |  | 1 |
| Support dual versions during migrations where feasible | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Surface health and readiness endpoints or checks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Test limits: timeouts, size caps, pagination, and rate limits | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Treat the AI model as an untrusted, potentially malicious actor | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Use circuit breakers around flaky upstreams | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use connection pools and exponential backoff with jitter for upstream calls | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use connection pools for databases and other backend services | Performance |  |  |  |  | ✓ |  | 1 |
| Use consistent casing: snake_case for tool names, camelCase for JSON fields (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use links/handles for large blobs and binary data, not inline base64 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use rolling or blue/green deploys with fast rollback | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use stable identifiers for tools, resources, and prompts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use strict allow-lists for all operations, parameters, and file paths | Safety & Security |  |  |  |  | ✓ |  | 1 |
| Use structured logging (e.g., JSON) for all log output | Logging & Observability |  |  |  |  | ✓ |  | 1 |
| Validate all inputs and outputs at runtime | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate and normalize file paths; block traversal and symlinks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Version schemas and never change semantics in place | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write tool descriptions as imperative, single-sentence summaries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

