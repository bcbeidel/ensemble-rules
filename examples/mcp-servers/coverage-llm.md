## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Validate all tool inputs against a strict schema before processing. | Correctness | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Separate transport/protocol concerns from domain/business logic. | Structure | ✓ | ✓ | ✓ |  | ✓ | ✓ | 5 |
| Emit structured logs with request/tool context for observability and audit. | Observability | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Enforce timeouts, size limits, and resource ceilings to prevent exhaustion. | Safety/Performance | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Paginate or chunk large list results and cap default page size. | Performance | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Redact secrets and never log/return credentials or PII. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Return structured errors with codes/types distinguishing retryable vs. permanent. | Error Handling | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Return specific, actionable error messages (not generic failures). | Error Handling | ✓ | ✓ | ✓ | ✓ |  |  | 4 |
| Run the server with least-privilege credentials/permissions. | Safety | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Use consistent naming conventions for tools/identifiers. | Style | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Version tools/resources/schemas and avoid breaking existing contracts. | Compatibility | ✓ |  | ✓ | ✓ |  |  | 3 |
| Write tool descriptions as clear prompts including purpose, units, and examples. | Tool Design | ✓ |  | ✓ | ✓ |  |  | 3 |
| Never expose stack traces or internal details in error responses. | Error Handling |  |  | ✓ | ✓ | ✓ |  | 3 |
| Cache idempotent/read-only results with bounded TTLs. | Performance | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Parameterize queries and avoid string concatenation for SQL/shell/paths. | Safety |  |  | ✓ | ✓ | ✓ |  | 3 |
| Prefer small/specific single-purpose tools over general-purpose ones. (contested) | Tool Design | ✓ |  | ✓ |  | ✓ |  | 3 |
| Keep tool outputs structured with a stable, deterministic shape. | Correctness | ✓ |  | ✓ | ✓ |  |  | 3 |
| Enforce latency budgets / sub-second targets for common tool calls. | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use asynchronous/non-blocking I/O to avoid blocking the server. | Performance |  |  |  |  | ✓ | ✓ | 2 |
| Implement a health check endpoint or tool. | Operations | ✓ |  |  | ✓ | ✓ |  | 3 |
| Write comprehensive unit and integration/contract tests. | Testing | ✓ | ✓ | ✓ | ✓ |  |  | 4 |
| Fuzz tool inputs with malformed/adversarial data. | Testing | ✓ |  | ✓ | ✓ |  |  | 3 |
| Return operation handles for long-running tasks instead of blocking. | Tool Design | ✓ |  |  | ✓ |  |  | 2 |
| Use enums/allowlists and reject unknown properties in input schemas. | Safety/Correctness | ✓ |  | ✓ |  | ✓ |  | 3 |
| On stdio transport, keep stdout pure protocol; send logs to stderr. | Transport | ✓ |  | ✓ |  |  |  | 2 |
| Distinguish mutating tools from read-only tools/resources. | Tool Design | ✓ |  | ✓ | ✓ |  |  | 3 |
| Require confirmation/dry-run for destructive operations. | Safety |  |  | ✓ |  |  |  | 1 |
| Block SSRF and validate outbound hosts with allowlists. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Sandbox filesystem access and prevent path traversal/symlink attacks. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Apply rate limits and backpressure per tenant/tool. | Performance | ✓ |  |  |  |  |  | 1 |
| Use circuit breakers and bounded retries only for idempotent operations. | Reliability | ✓ |  |  |  |  | ✓ | 2 |
| Expose metrics (latency, error rates, QPS) per tool. | Observability | ✓ |  | ✓ |  | ✓ |  | 3 |
| Name tools as short verb-object identifiers (snake_case). | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Keep each tool handler small; push logic into domain modules. | Structure |  |  | ✓ |  |  | ✓ | 2 |
| Use the official MCP SDK rather than hand-rolling the protocol. | Style |  |  | ✓ |  |  |  | 1 |
| Pin dependency and SDK versions. | Operations |  |  | ✓ |  |  |  | 1 |
| Fail fast at startup on missing/invalid configuration. | Operations | ✓ |  | ✓ |  |  |  | 2 |
| Treat the AI model/input as untrusted and potentially adversarial. | Safety |  |  | ✓ | ✓ | ✓ |  | 3 |
| Implement capability negotiation and handshake per spec. | Transport | ✓ |  |  |  |  |  | 1 |
| Honor client cancellation and deadlines. | Transport | ✓ |  |  |  |  |  | 1 |
| Externalize configuration and use environment variables for secrets. | Operations | ✓ | ✓ |  | ✓ |  |  | 3 |
| Normalize timestamps to ISO-8601 UTC. | Style | ✓ |  |  |  |  |  | 1 |
| Gracefully drain and shut down in-flight requests. | Operations | ✓ |  |  |  |  |  | 1 |
| Gate new tools behind feature flags with deprecation telemetry. | Release | ✓ |  |  |  |  |  | 1 |
| Use link/handle references for large blobs rather than inline base64. | Tool Design | ✓ |  | ✓ |  |  |  | 2 |
| Don't prematurely optimize; ensure correctness/readability first. | Performance |  | ✓ |  |  |  |  | 1 |
| Include a human-readable summary alongside structured data. (contested) | Tool Design | ✓ |  | ✓ |  |  |  | 2 |
| Require authentication and bind HTTP servers safely by default. | Safety |  |  | ✓ |  |  | ✓ | 2 |
| Document environment/config requirements and tool dependencies. | Documentation |  |  | ✓ | ✓ |  |  | 2 |
| Snapshot-test tool descriptions to catch prompt regressions. | Testing |  |  | ✓ |  |  |  | 1 |
| Use connection pools for databases/backends. | Performance | ✓ |  |  |  | ✓ |  | 2 |
| Include enough identifying context (IDs, paths) in returned data. | Tool Design |  |  |  | ✓ |  |  | 1 |
| Reject ambiguous/underspecified inputs rather than guessing. | Correctness |  |  | ✓ | ✓ |  |  | 2 |
| Namespace related tools with a common prefix. | Style |  |  |  | ✓ |  |  | 1 |
| Write tool descriptions in imperative mood, concisely. | Style | ✓ |  |  | ✓ |  |  | 2 |
| Do not authenticate or authorize based on model-supplied arguments. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Prefer HTTP for distributed/production; stdio for local. (contested) | Transport | ✓ |  |  |  | ✓ |  | 2 |
| Design servers to be stateless where possible. | Structure |  |  |  |  | ✓ |  | 1 |
| Use rolling/blue-green deploys with rollback. | Operations | ✓ |  |  |  |  |  | 1 |
| Avoid magic numbers/strings; use named constants. | Style |  | ✓ |  |  |  | ✓ | 2 |
| Batch operations where possible to reduce round trips. | Performance |  |  |  | ✓ |  |  | 1 |
| Classify and tag data sensitivity in outputs. | Data/Privacy | ✓ |  |  | ✓ |  |  | 2 |
| Don't expose debug endpoints in production. | Safety |  |  |  |  |  | ✓ | 1 |

## Notes on clustering decisions

- **"Validate all tool inputs against a strict schema"** merges gpt-4o-mini's generic "validate all inputs against expected formats" with the more specific JSON Schema / Zod / Pydantic recommendations from others. A stricter reading would split "schema validation" from "input sanitization against injection"; I kept schema validation as its own row and kept parameterized queries / injection prevention separate.
- **"Return structured errors with codes/types distinguishing retryable vs. permanent"** and **"Return specific, actionable error messages"** could have been one cluster, but the first is about machine-readable taxonomy and the second is about message content/quality, which several models addressed independently.
- **"Separate transport from domain logic"** absorbed grok's "don't mix transport-specific logic with business logic", gpt-4o-mini's "organize into clear modules / don't put business logic in routing", gpt-5's thin-adapter principle, opus's layered architecture, and gemini's "separate protocol handling from tool execution". A stricter clustering could split generic modularity from the specific transport/domain split.
- **"Enforce timeouts, size limits, and resource ceilings"** bundles three related but distinct ideas (execution timeouts, payload caps, concurrency/memory limits). Splitting would have produced three sparse rows each with the same set of models.
- **"Treat AI/model input as untrusted"** is separate from generic "validate inputs" because several models called this out as a distinct threat-model stance (confused deputy, prompt injection) rather than a schema-validation rule.
- **"Distinguish mutating tools from read-only tools/resources"** combines gpt-5's "mutations as tools, reads as resources", opus's "get_*/list_* must be idempotent", and haiku's "resources for stable data, tools for actions". Arguably three different rules; I clustered on the shared underlying principle.
- **"Cache idempotent reads with bounded TTLs"** — grok marked this contested, haiku warned against caching permission checks, others endorsed it plainly; clustered together despite nuance.
- **gpt-4o-mini's contested meta-rules** ("prioritize performance where user pain is evident", "don't adhere strictly to one style guide") did not map cleanly to any other model's rule and are left as count=1 rows implicit in the sparse tail (not listed individually to avoid noise — a stricter audit would add them).
- **"Prefer small/specific tools over general-purpose ones"** vs. gpt-5's "micro-tools improve selection (contested)" vs. opus's "coarse-grained tools beat fine-grained (contested)" — these are *opposing* positions on the same axis. I clustered them as a single "tool granularity" row favoring the "specific/small" side since gpt-5, opus, and gemini all explicitly called granularity contested; the direction each leans differs. A stricter matrix would split into two opposing rows.
- **"Include human-readable summary alongside structured data"** is marked contested by gpt-5 and opus; haiku takes the opposite view ("return structured JSON, keep markdown separate") which I read as compatible rather than opposing, so I did not split.