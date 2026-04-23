## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | Count |
|---|---|---|---|---|---|---|---|
| Never write logs or debug output to stdout on stdio transports; use stderr. | Transport/Protocol | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Set explicit timeouts on every I/O or tool execution call. | Error Handling/Performance | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Validate all tool inputs against a strict schema before processing. | Input Validation | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Do not hard-code secrets; use env vars or a secrets manager. | Safety | ✓ | ✓ |  | ✓ | ✓ | 4 |
| Return structured errors with stable codes and actionable messages. | Error Handling | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Paginate, cap, or stream large tool outputs to avoid unbounded responses. | Performance | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Never interpolate user/LLM input into shell commands or code (no eval/injection). | Safety | ✓ |  |  | ✓ | ✓ | 3 |
| Use parameterized queries/prepared statements for database access. | Safety | ✓ | ✓ |  | ✓ |  | 3 |
| Use the official MCP SDK instead of hand-rolling protocol code. | Structure/Protocol | ✓ |  | ✓ | ✓ |  | 3 |
| Enforce allowlists for filesystem paths / network egress / resources. | Safety | ✓ |  |  | ✓ | ✓ | 3 |
| Reject unknown/additional properties in input schemas. | Schemas/Validation | ✓ |  | ✓ | ✓ |  | 3 |
| Log every tool invocation with name, arguments, duration, and outcome. | Observability | ✓ |  | ✓ | ✓ |  | 3 |
| Redact secrets/PII in logs and tool outputs. | Safety/Observability | ✓ |  | ✓ | ✓ |  | 3 |
| Keep each server focused on a single responsibility/domain. | Structure | ✓ | ✓ |  | ✓ |  | 3 |
| Document required env vars, setup, and configuration in a README. | Documentation | ✓ |  |  | ✓ | ✓ | 3 |
| Provide clear, model-facing descriptions for each tool. | Tool Definition | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Use consistent, stable, predictable tool names (e.g., snake_case/verb_noun). | Structure | ✓ |  | ✓ |  |  | 2 |
| Declare and document side effects / idempotency for tools. | Tool Definition | ✓ |  |  |  | ✓ | 2 |
| Write tests covering success, invalid inputs, and error paths for each tool. | Testing | ✓ |  | ✓ | ✓ |  | 3 |
| Run with least-privilege credentials scoped to needed resources. | Safety | ✓ |  | ✓ |  |  | 2 |
| Provide /health (and /ready) endpoints for HTTP servers. | Observability/Ops | ✓ |  |  | ✓ |  | 2 |
| Implement graceful shutdown and drain in-flight work on SIGTERM/SIGINT. | Ops | ✓ |  |  | ✓ |  | 2 |
| Pin dependencies (and MCP SDK) to exact versions. | Deployment/Structure | ✓ |  | ✓ |  |  | 2 |
| Emit structured (JSON) logs with timestamps, request IDs, and context. | Observability | ✓ |  |  | ✓ |  | 2 |
| Require authentication (token/mTLS) for HTTP transport. | Safety | ✓ |  | ✓ |  |  | 2 |
| Distinguish transient vs permanent errors; retry only idempotent ops. | Error Handling | ✓ |  | ✓ | ✓ |  | 3 |
| Use enums / fixed value sets in schemas for constrained parameters. | Schemas | ✓ |  | ✓ |  |  | 2 |
| Support cancellation and stop work promptly when cancelled. | Protocol | ✓ |  |  |  |  | 1 |
| Maintain a CHANGELOG and follow semantic versioning. | Style/Deployment | ✓ |  |  |  |  | 1 |
| Include an mcp.json manifest at the repo root. | Structure | ✓ |  |  |  |  | 1 |
| Build minimal, non-root container images with explicit USER. | Deployment | ✓ |  |  |  |  | 1 |
| Pin container base images by digest. | Deployment | ✓ |  |  |  |  | 1 |
| Add a HEALTHCHECK to container images. | Deployment | ✓ |  |  |  |  | 1 |
| Include a .dockerignore file. | Deployment | ✓ |  |  |  |  | 1 |
| Fail fast on missing required env vars at startup. | Deployment | ✓ |  |  | ✓ |  | 2 |
| Bind to localhost by default; require explicit config to listen externally. | Deployment | ✓ |  |  |  |  | 1 |
| Reuse connections (HTTP/DB pooling) rather than reconnecting per call. | Performance | ✓ |  |  |  |  | 1 |
| Batch or pipeline backend calls to avoid N+1 patterns. | Performance | ✓ |  |  |  |  | 1 |
| Apply backpressure when streaming to match consumer speed. | Performance | ✓ |  |  |  |  | 1 |
| Export metrics (requests, errors, latency, retries, timeouts). | Observability | ✓ |  |  | ✓ |  | 2 |
| Propagate and log a correlation/request ID across backend calls. | Observability | ✓ |  |  |  |  | 1 |
| Add contract/snapshot tests for tool list and schemas. | Testing | ✓ |  | ✓ |  |  | 2 |
| Test against multiple client versions/implementations. | Testing | ✓ |  |  |  |  | 1 |
| Enforce formatting and linting in CI. | Style | ✓ |  |  |  |  | 1 |
| Never crash the process on bad input; return an error and continue. | Error Handling | ✓ |  |  |  |  | 1 |
| Run static secret scans and dependency audits in CI. | Testing/Safety | ✓ |  |  |  |  | 1 |
| Require TLS for HTTP transport and backend calls in production. | Safety | ✓ |  |  |  |  | 1 |
| Prefer async/non-blocking I/O for I/O-bound tools. | Performance | ✓ | ✓ | ✓ | ✓ |  | 4 |
| Implement caching for frequent/expensive requests. | Performance |  | ✓ |  | ✓ |  | 2 |
| Use consistent naming conventions for variables/functions. | Style |  | ✓ |  |  |  | 1 |
| Avoid unclear abbreviations; prioritize clarity over brevity. | Style |  | ✓ |  |  |  | 1 |
| Don't optimize prematurely; prioritize clarity/correctness. | Style |  | ✓ |  |  |  | 1 |
| Prefer external libraries for common functionality. | Style |  | ✓ |  |  |  | 1 |
| Default tools to read-only; require opt-in for mutations. | Safety |  |  | ✓ | ✓ |  | 2 |
| Give destructive tools distinct, explicit names (delete_*, drop_*). | Safety |  |  | ✓ |  |  | 1 |
| Never expose generic execute_sql/run_shell/eval tools. | Safety |  |  | ✓ |  |  | 1 |
| Treat tool output as untrusted data, never as instructions (prompt-injection). | Safety |  |  | ✓ |  |  | 1 |
| Require a confirmation token / dry-run for irreversible operations. | Safety |  |  | ✓ | ✓ |  | 2 |
| Mark optional parameters optional; don't use sentinel values. | Schemas |  |  | ✓ |  |  | 1 |
| Co-locate tool schema, handler, and tests in one file. | Structure |  |  | ✓ |  |  | 1 |
| One tool per distinct operation; do not multiplex via mode params. | Structure |  |  | ✓ |  |  | 1 |
| Keep tool handlers short (~under 50 lines); extract helpers. | Style |  |  | ✓ |  |  | 1 |
| Avoid module-level mutable state. | Style |  |  | ✓ |  |  | 1 |
| Use async handlers uniformly; do not mix sync and async. | Style |  |  | ✓ |  |  | 1 |
| Truncate large string fields with an explicit marker. | Performance |  |  | ✓ |  |  | 1 |
| Return IDs/summaries by default; provide separate get_* for details. | Performance |  |  | ✓ |  |  | 1 |
| Stream progress for operations over ~2 seconds. | Performance |  |  | ✓ |  |  | 1 |
| Flush/await all writes before process exit. | Transport |  |  | ✓ |  |  | 1 |
| Emit a structured startup log line with name/version/tool count. | Observability |  |  | ✓ |  |  | 1 |
| Validate API keys/credentials synchronously at tool invocation. | Input Validation |  |  |  | ✓ |  | 1 |
| Validate path inputs; reject `..` and paths outside the allowlist. | Safety |  |  |  | ✓ |  | 1 |
| Check/reject input encoding issues (UTF-8, null bytes, control chars). | Input Validation |  |  |  | ✓ |  | 1 |
| Profile tools under realistic load and document latency percentiles. | Performance |  |  |  | ✓ |  | 1 |
| Rotate credentials regularly; test that rotation actually invalidates old keys. | Safety |  |  |  | ✓ |  | 1 |
| Validate configuration at startup and fail fast on invalid config. | Deployment |  |  |  | ✓ |  | 1 |
| Handle EOF and connection drops gracefully. | Transport |  |  |  | ✓ |  | 1 |
| Use locking / concurrency-safe structures for shared state. | Concurrency |  |  |  | ✓ |  | 1 |
| Document in-memory state lifetime and scope. | Concurrency |  |  |  | ✓ |  | 1 |
| Design the server to be stateless. | Structure |  |  |  |  | ✓ | 1 |
| Minimize external dependencies. | Structure |  |  |  |  | ✓ | 1 |
| Encode all string data as UTF-8. | Protocol |  |  |  |  | ✓ | 1 |
| Use line-delimited JSON (JSONL) for stdio communication. | Protocol |  |  |  |  | ✓ | 1 |
| Follow RESTful practices for HTTP endpoints. | Protocol |  |  |  |  | ✓ | 1 |
| Provide an OpenAPI specification for HTTP endpoints. | Documentation |  |  |  |  | ✓ | 1 |
| Use non-zero exit codes only for catastrophic failures. | Error Handling |  |  |  |  | ✓ | 1 |
| Isolate/sandbox tool execution from the host system. | Safety |  |  |  |  | ✓ | 1 |
| Choose transport (stdio vs HTTP) deliberately per deployment needs. | Performance/Protocol |  |  |  |  | ✓ | 1 |
| Write code for readability; favor clear names and explicit control flow. | Style |  | ✓ |  | ✓ |  | 2 |
| Use established crypto/validation libraries; don't roll your own. | Safety |  |  |  | ✓ |  | 1 |
| Catch and log exceptions adequately; don't ignore errors. | Error Handling |  | ✓ |  | ✓ |  | 2 |

## Notes on clustering decisions

- **"Never write logs to stdout"** — merged openai/gpt-5's "keep stdout pristine for protocol frames", claude-opus's "never write to stdout from stdio-transport server", claude-haiku's transport guidance (implicit via SDK), and gemini's "never write logs to stdout" as the same rule. Haiku's is weaker; marked based on the SDK rule implying the concern.
- **"Use the official MCP SDK"** — gpt-5, claude-opus, and claude-haiku all raise this; gemini raises SDK-adjacent rules (JSONL, protocol framing) but not "use the SDK" specifically, so not credited.
- **"Validate inputs with a strict schema"** vs **"Reject unknown/additional properties"** — kept as two separate clusters even though they often appear together, because several models raise strict validation without explicitly addressing unknown-property rejection (e.g., gemini, haiku partial).
- **"Paginate/cap/stream large outputs"** — merged several closely related ideas: response-size caps, pagination, and streaming. Claude-opus splits these into three rules; I clustered them under one "bound output size" rule since they address the same failure mode. A stricter clusterer could split.
- **"Document side effects / idempotency"** appears in gpt-5 under tool descriptions and in gemini under tool definitions. Could arguably merge with "return structured errors that distinguish retryable" but I kept separate because idempotency is about tool semantics, retryability about error classification.
- **"Prefer async/non-blocking I/O"** — gpt-4o-mini's "don't block main threads", claude-opus's "async handlers uniformly", and claude-haiku's contested async rule all clustered here. Gpt-5 raises backpressure/streaming but not async specifically; not credited. Actually credited gpt-5 because of its "Apply backpressure when streaming" and overall async posture — borderline; a stricter reading would drop it.
- **"Default to read-only / require confirmation for mutations"** — kept as two separate rules (read-only default vs confirmation token) even though they're related, because claude-opus and claude-haiku treat them distinctly.
- **"Log every tool invocation"** and **"Log mutating operations with audit trail"** — merged; claude-haiku's audit-log rule and gpt-5's auditable invocations rule and claude-opus's invocation log are the same substance.
- **"Write code for readability"** vs **"Consistent naming conventions"** — kept separate; gpt-4o-mini raises both as distinct rules, so treated as distinct clusters.
- **"Fail fast on missing env vars"** (gpt-5) vs **"Validate config at startup"** (claude-haiku) — could be merged; I kept them separate because haiku's is broader (config file validation) while gpt-5's is specifically env-var presence. A looser clusterer would collapse.
- **"Document parameters / schemas"** in haiku overlaps with gpt-5's "concise descriptions with examples" and gemini's "clear descriptions"; clustered under "Provide clear model-facing tool descriptions."
- Claude-haiku's "include README" and gpt-5's "document env vars in README" and gemini's README-ish content were clustered as one documentation rule.