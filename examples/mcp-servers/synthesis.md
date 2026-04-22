# Synthesis of MCP Server Best Practices

## 1. Consensus Rules

### Structure & Architecture

- **Separate transport/protocol handling from domain logic.** Thin adapters make business logic testable and transport-agnostic. *(substantively similar but differently worded across GPT-5, Claude Opus, Gemini, Grok)*
- **Keep tools small, focused, and single-purpose.** Narrow scope reduces selection ambiguity and simplifies reasoning. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Name tools with verb-noun patterns in snake_case (e.g., `create_ticket`, `search_users`).** Predictable naming improves model tool selection. *(near-identical across GPT-5, Claude Opus, Claude Haiku)*

### Tool & Resource Design

- **Define strict input/output schemas (JSON Schema, Zod, Pydantic) for every tool and validate at runtime.** Schemas are the contract with a probabilistic client that will invent parameters. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Write tool descriptions as prompts — include purpose, units, constraints, side effects, and examples.** Descriptions are read by the model far more than code is read by humans. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Return structured data with a stable shape; use `null` for missing fields rather than omission.** Shape stability lets the model parse reliably. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Paginate list results and cap default page sizes.** Unbounded lists overflow context and silently degrade reasoning. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Truncate or handle-ify large payloads; do not dump megabytes inline.** Large outputs poison context windows. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Keep `get_*`, `list_*`, `search_*` tools strictly read-only and idempotent.** Violating this breaks the model's ability to plan safely. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Error Handling

- **Return structured, specific errors with stable codes/types and remediation hints.** The model uses error text to self-correct; vague errors cause retry loops. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Never return raw stack traces or internal paths to the client.** They leak internals, waste tokens, and create security risk. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Distinguish retryable (transient) from non-retryable (bad input) errors.** Prevents infinite retry loops and enables correct client behavior. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Safety & Security

- **Run the server with least-privilege credentials scoped to what the exposed tools need.** Minimizing privilege limits blast radius. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Treat all model-supplied arguments as untrusted/adversarial input (prompt injection is real).** The LLM is a confused deputy acting on potentially injected instructions. *(substantively similar across Claude Opus, Claude Haiku, Gemini)*
- **Validate, sanitize, and parameterize all inputs used in queries, paths, or commands.** Prevents SQL injection, path traversal, command injection, SSRF. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Require explicit confirmation, dry-run, or opt-in for destructive operations.** Models will invoke delete/write tools based on injected instructions otherwise. *(substantively similar across GPT-5, Claude Opus)*
- **Never log or return secrets, credentials, or PII.** Leakage is irreversible and outputs re-enter prompts. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Enforce hard timeouts, size caps, and resource limits on tools and upstream calls.** Hard limits prevent resource exhaustion and stranded sessions. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Performance

- **Target sub-second latency for common tool calls; each call blocks the model's reasoning loop.** Latency directly degrades the assistant experience. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Use asynchronous/non-blocking I/O throughout.** A single slow synchronous tool blocks the server. *(substantively similar across GPT-5, Gemini, Grok)*
- **Cache idempotent reads with bounded TTLs.** Models repeat identical calls within a session. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

### Observability

- **Emit structured (JSON) logs with tool name, arguments summary, caller, outcome, duration, and correlation ID.** Structured logs are queryable; unstructured logs are noise. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Expose metrics (latency p50/p95, error rates, QPS) per tool.** You cannot tune what you do not measure. *(substantively similar across GPT-5, Claude Opus, Gemini)*

### Testing

- **Write unit/contract tests against tool schemas and domain functions independently of the MCP runtime.** Schema drift is the most common regression. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*
- **Fuzz tool inputs with malformed, oversized, and adversarial values.** The LLM is effectively a fuzzer — pre-empt it. *(substantively similar across GPT-5, Claude Opus)*
- **Include end-to-end tests over the real transport.** stdio framing and cancellation bugs only appear end-to-end. *(substantively similar across GPT-5, Claude Opus)*

### Versioning & Compatibility

- **Version servers and schemas explicitly; never silently repurpose a tool name.** Name stability prevents silent breakage in clients and saved contexts. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

## 2. Strong Minority Rules

- **On stdio transport, write nothing to stdout except protocol messages; logs go to stderr.** *(Claude Opus)* — A notoriously common bug that corrupts sessions silently. High-signal, low-cost rule worth keeping.
- **Flush stdio promptly and handle SIGPIPE/EOF cleanly.** *(GPT-5, Claude Opus)* — Concrete failure mode that silently hangs clients.
- **For HTTP transport, require authentication and bind to localhost by default.** *(Claude Opus)* — An unauthenticated MCP server on `0.0.0.0` is effectively RCE; critical default.
- **Block SSRF explicitly: reject private IP ranges, metadata endpoints (`169.254.169.254`), and non-allowlisted hosts in any fetch tool.** *(Claude Opus, Gemini)* — LLMs will happily be instructed to fetch cloud metadata services.
- **Include a machine-readable status plus a separate human summary field.** *(GPT-5, Claude Opus)* — Prevents mixing prose into structured data while keeping the model oriented.
- **Return long-running work as operation handles with polling/progress rather than blocking.** *(GPT-5, Claude Opus via pagination/truncation)* — Essential for work that cannot fit in a single turn.
- **Snapshot-test tool descriptions.** *(Claude Opus)* — Descriptions are prompts; treat regressions as code regressions.
- **Provide a `/health` or health-check tool without side effects.** *(Claude Haiku, Gemini)* — Standard ops hook; cheap and essential.
- **Reject unknown input properties (`additionalProperties: false`).** *(Claude Opus)* — Catches hallucinated parameters early.
- **Fail fast at startup on missing required configuration.** *(Claude Opus)* — Silent misconfiguration surfaces later as confusing tool errors.
- **Prefer coarse-grained tools that complete a task over N chatty tools the model must chain.** *(Claude Opus)* — Round trips dominate latency; counterbalances the "small tools" rule (see Divergences).
- **Expose stable, indexable data as resources; use tools for actions and computed/filtered data.** *(Claude Opus, Claude Haiku)* — Provides a useful design heuristic absent from other inputs.

## 3. Divergences

### Tool granularity: fine-grained vs. coarse-grained

- **Fine-grained / micro-tools:** GPT-5 (with caveat), Gemini — improves selection accuracy, reduces attack surface.
- **Coarse-grained / task-complete:** Claude Opus — fewer tools reason better, round trips dominate latency.
- **Synthesis:** Both sides agree on *single-purpose* (not Swiss-army) but disagree on *how much work one tool does*. Recommended rule: **prefer task-complete tools over chatty chains, but keep each tool single-purpose with a narrow, well-named scope.** Measure tool count — if the model is repeatedly chaining N calls to accomplish one user intent, collapse them.

### Transport: stdio vs. HTTP

- **stdio preferred for local/desktop:** GPT-5, Claude Opus.
- **HTTP preferred for production:** Gemini, GPT-5 (for distributed).
- **Synthesis:** This is a deployment-context question, not a best practice. Recommended rule: **use stdio for local/co-located integrations, HTTP(S) with auth for networked/multi-tenant deployments.** Both sides agree when scoped to their context.

### Output format: pure JSON vs. JSON + human summary

- **Pure structured JSON:** Gemini implicitly, GPT-5 (leaning).
- **JSON with a `summary` human-readable field:** Claude Opus, GPT-5 (contested tag).
- **Synthesis:** The summary field is low-cost and measurably improves model behavior. Recommended: **return structured data as the primary payload; include a short `summary` field when the model benefits from a human-quotable description.** Keep prose out of data fields either way.

### Business-rule validation at the server

- **Validate schema only; let backend decide business rules:** Claude Haiku.
- **Validate aggressively including business constraints:** GPT-5, Gemini.
- **Synthesis:** Validate schema always; validate business rules only when the server owns the authority or when failing fast saves significant cost. Avoid duplicating authorization logic that lives elsewhere.

### Internal retry on transient errors

- **Retry internally with backoff:** Grok, GPT-5 (for idempotent ops).
- **Fail fast; let the caller retry:** Claude Haiku.
- **Synthesis:** **Retry only idempotent upstream calls with bounded attempts and jitter; surface exhaustion as a retryable error to the client.** Never retry mutations without idempotency keys.

## 4. Notable Omissions

- **Prompt injection / untrusted-input treatment:** Absent from GPT-4o-mini and Grok. This is arguably the defining security concern for MCP servers — its omission is significant.
- **stdio stdout contamination rule:** Only Claude Opus raises this specifically. Given how often this bug occurs in practice, its absence from GPT-5, Gemini, Haiku, and Grok is notable.
- **Tool descriptions as prompts / description quality:** Absent from GPT-4o-mini and Grok. These models treated MCP servers as generic services, missing that the description *is* the interface for the model.
- **Destructive-operation confirmation/dry-run:** Only GPT-5 and Claude Opus raise this explicitly. A critical safety pattern missing from Haiku, Gemini, and Grok.
- **Pagination and payload truncation:** Absent from GPT-4o-mini and Grok. Consensus among the more detailed responses; its absence correlates with less MCP-specific reasoning.
- **Schema-first validation with named libraries:** GPT-4o-mini and Grok speak only generically about "input validation" without naming schemas as the contract.
- **Read-only idempotency of `get_*`/`list_*` tools:** Only Claude Opus and Claude Haiku raise this explicitly, though it's a foundational property.
- **GPT-4o-mini and Grok overall:** Both produced generic "good software" advice with little MCP-specific content. Their outputs carry less independent signal on MCP-specific questions.

---

## 5. Final Rules File

# MCP Server Best Practices

**Scope:** Building Model Context Protocol servers (stdio or HTTP) that expose tools, resources, and prompts to AI assistants.
**Audience:** Engineers and AI coding assistants authoring, reviewing, or operating MCP servers.

---

## Architecture & Structure

- **Separate transport, protocol, and domain layers.** Tool handlers should be thin wrappers over pure domain functions so logic is testable without the MCP runtime.
- **Register tools, resources, and prompts declaratively in one place.** Central registration makes capabilities auditable and discoverable.
- **Co-locate each tool's schema, validator, and implementation.** Proximity keeps contract and code in sync.
- **Keep each tool single-purpose with a narrow, well-named scope.** Narrow scope reduces selection ambiguity.
- **Prefer task-complete tools over chatty chains the model must sequence.** Round trips dominate latency inside the model's reasoning loop.
- **Expose stable, indexable data as resources; use tools for actions and computed results.** Resources are cacheable and discoverable; tools are for effects.

## Naming & Descriptions

- **Name tools with `verb_object` in snake_case** (e.g., `create_ticket`, `search_users`). Predictable naming improves model tool selection.
- **Namespace related tools with a shared prefix** (e.g., `db_query`, `db_migrate`). Grouping clarifies intent in large servers.
- **Write tool descriptions as prompts, not docstrings.** Include purpose, when to use (and not use) the tool, units, constraints, side effects, and a minimal example.
- **State side effects explicitly** ("writes to disk", "sends email"). The model uses this to decide whether to ask the user first.
- **Snapshot-test tool descriptions.** Descriptions are prompts; regressions silently degrade model behavior.

## Schemas & Validation

- **Define strict JSON Schema (or Zod/Pydantic) for every tool input and output.** Schemas are your contract with a probabilistic client.
- **Reject unknown properties (`additionalProperties: false`).** Silent acceptance hides hallucinated parameters and masks bugs.
- **Use enums, ranges, and formats for constrained fields.** Tight constraints prevent garbage-in.
- **Validate both inputs and outputs at runtime.** Never trust model-supplied shapes; never emit outputs that violate your own schema.
- **Version schemas and server capabilities explicitly; never silently repurpose a tool name.** Deprecate with a clear path; add new tools rather than mutating semantics.

## Tool & Resource Design

- **Return structured JSON with a stable shape.** Use `null` for missing fields, never omission.
- **Include a short human-readable `summary` field alongside structured data.** Gives the model something to quote without re-serializing.
- **Make all `get_*`, `list_*`, `search_*` tools strictly read-only and idempotent.** Violating this breaks the model's ability to plan safely.
- **Paginate every list endpoint with sensible default caps (a few dozen items).** Unbounded lists overflow context and silently truncate reasoning.
- **Truncate large string fields and return a `truncated: true` flag plus a fetch handle.** Dumping megabytes degrades model performance.
- **Use links or operation handles for large blobs and binaries; never base64 inline.**
- **Return operation handles with progress/polling for long-running work instead of blocking.** Handles enable streaming, cancellation, and retry.
- **Include enough context in returned data to act on it later** (IDs, paths, timestamps), not just display strings.

## Error Handling

- **Return structured errors with a stable machine-readable type/code and a human message.** Example: `{ type: "ValidationError", message: "expected YYYY-MM-DD, got 'next Tuesday'", field: "due_date" }`.
- **Write error messages that tell the model how to fix the call.** Include the offending field, expected format, and an example.
- **Never return stack traces, internal paths, or library versions to the client.** Log them server-side with a correlation ID.
- **Distinguish retryable (transient) from non-retryable (bad input) errors, and include `retry_after` hints when applicable.** Prevents infinite retry loops and thundering herds.
- **Retry only idempotent upstream calls internally, with bounded attempts and jitter.** Surface exhaustion as a retryable error.
- **Fail closed on ambiguity.** If intent cannot be determined safely, return an error asking for clarification rather than guessing.

## Safety & Security

- **Treat every model-supplied argument as untrusted and adversarial.** Prompt injection can originate from any document the model has seen.
- **Run the server as a non-root user with least-privilege credentials scoped to the exposed tools.** A read-only tool gets read-only DB creds.
- **Never authenticate based on tool arguments.** The server's identity is fixed; arguments are model-supplied.
- **Parameterize all database queries, shell invocations, and path operations.** Never string-concatenate untrusted input.
- **Require `confirm: true` or a dry-run → execute flow for destructive operations.** Models will invoke delete/write tools based on injected instructions otherwise.
- **Sandbox filesystem tools to an explicit root allowlist; resolve symlinks before checks.** Path traversal via `..` and symlinks is the most common MCP exploit.
- **Block SSRF: reject private IP ranges, cloud metadata endpoints (`169.254.169.254`), and non-allowlisted hosts in any fetch tool.**
- **Never echo or log secrets, credentials, or PII.** Outputs re-enter prompts; logs are read.
- **Log every tool invocation with tool name, caller, sanitized arguments, outcome, and correlation ID.** Auditability is non-negotiable for agent-driven systems.

## Transport

- **Use stdio for local/co-located integrations; use HTTP(S) with authentication for networked or multi-tenant deployments.**
- **On stdio, write nothing to stdout except protocol messages.** Logs go to stderr; a stray `print` corrupts the session.
- **Flush stdout after every message; handle SIGPIPE and EOF cleanly.** Hanging servers strand clients.
- **For HTTP, require authentication and bind to localhost by default.** An unauthenticated MCP server on `0.0.0.0` is an RCE primitive.
- **Set explicit timeouts on every outbound call** (DB, HTTP, subprocess). A hung tool hangs the entire assistant turn.
- **Implement capability negotiation and graceful shutdown correctly per spec.**

## Performance

- **Target sub-second latency for common tool calls.** Each call blocks the model's reasoning loop.
- **Use asynchronous, non-blocking I/O throughout.** One slow synchronous tool blocks the server.
- **Cache idempotent reads with short, bounded TTLs keyed by arguments.** Models repeat identical calls within a session.
- **Use connection pools and exponential backoff with jitter for upstream calls.**
- **Apply per-tool concurrency limits and backpressure.** Protects the server and its dependencies.
- **Enforce per-tool latency budgets and payload size caps.** Hard limits prevent tail-latency regressions and resource exhaustion.

## Observability

- **Emit structured (JSON) logs with timestamp, correlation ID, tool, caller, duration, size, and outcome.**
- **Expose metrics for QPS, p50/p95 latency, error rate, and queue depth per tool.** You cannot tune what you do not measure.
- **Add tracing spans around each tool call and upstream dependency.**
- **Provide a health/readiness check without side effects.** Standard ops hook for orchestrators and load balancers.
- **Fail fast at startup on missing required configuration or unreachable dependencies.** Silent misconfiguration surfaces later as confusing tool errors.

## Testing

- **Write contract tests against tool schemas and unit tests against domain functions.** Schema drift is the most common regression.
- **Fuzz tool inputs with malformed, oversized, and adversarial strings.** The LLM is effectively a fuzzer.
- **Include end-to-end tests over the real transport.** stdio framing, cancellation, and backpressure bugs only surface end-to-end.
- **Test limits explicitly:** timeouts, size caps, pagination, rate limits, and error paths.

## Style & Operations

- **Use the official SDK (TypeScript, Python) rather than hand-rolling the protocol.** The spec evolves; SDKs track it.
- **Pin SDK and dependency versions.** Protocol-level breakage is hard to diagnose from the model's side.
- **Keep tool handlers thin (~50 lines): validate, call, format, return.** Push logic into domain modules.
- **Normalize timestamps to ISO-8601 UTC.** Consistent time simplifies reasoning and joins.
- **Write tool descriptions in imperative mood** ("Create a new ticket") and keep them concise.
- **Document required environment variables, dependencies, and typical latencies per tool.**
- **Gate new tools behind feature flags; measure usage before removing deprecated ones.**