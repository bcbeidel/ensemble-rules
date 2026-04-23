## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Provide a description for every variable and output. | Inputs & Outputs | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use snake_case for variable, local, and output names. | Style & Naming | ✓ | ✓ | ✓ |  | ✓ | ✓ | 5 |
| Declare explicit types for all variables; avoid `any`. | Inputs & Outputs | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Mark secret/sensitive outputs (and inputs) as `sensitive = true`. | Safety | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Provide a standard file layout (main.tf, variables.tf, outputs.tf, etc.). | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Provide a README documenting purpose, inputs, outputs, and examples. | Documentation | ✓ | ✓ | ✓ | ✓ |  | ✓ | 5 |
| Run `terraform fmt` (enforced in CI) for consistent formatting. | Style / CI | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Pin required provider versions with bounded constraints. | Versioning | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Prefer `for_each` over `count` for resource collections. | Style / Resources | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use variable `validation` blocks to enforce constraints. | Error Handling | ✓ | ✓ |  | ✓ | ✓ |  | 4 |
| Do not declare provider blocks inside reusable modules. | Structure / Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Use semantic versioning with tagged releases for modules. | Versioning | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Pin module source versions when consuming modules. | Versioning | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Run `terraform plan` on PRs; apply only from protected/CI pipelines. | CI/CD | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Run `terraform validate` / `tflint` / security scanning in CI. | CI/CD | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Provide runnable examples under `examples/`. | Structure / Docs | ✓ |  | ✓ | ✓ |  |  | 3 |
| Keep outputs minimal / only export what callers need. | Inputs & Outputs | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use `moved {}` blocks when renaming/refactoring resources. | State | ✓ |  | ✓ |  |  |  | 2 |
| Use `ignore_changes` sparingly and only with justification. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Do not use `terraform.workspace` to drive environment behavior. | Safety | ✓ |  |  |  | ✓ |  | 2 |
| Avoid `depends_on` unless strictly necessary. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Require a minimum Terraform version (`required_version`). | Versioning | ✓ |  | ✓ |  |  |  | 2 |
| Don't pass secrets via `-var`/`TF_VAR` or hardcode them in modules. | Safety | ✓ | ✓ |  | ✓ |  |  | 3 |
| Use a remote backend with state locking. | State | ✓ |  |  |  |  | ✓ | 2 |
| Keep state granular / split by blast radius & environment. | State | ✓ |  | ✓ |  |  |  | 2 |
| Use precondition/postcondition blocks for critical guarantees. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Maintain a CHANGELOG for module releases. | Versioning | ✓ |  | ✓ | ✓ |  |  | 3 |
| Keep modules focused on a single cohesive purpose (avoid god modules). | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Name booleans with a positive `enable_`/`create_` prefix. | Style | ✓ |  | ✓ |  |  |  | 2 |
| Auto-generate inputs/outputs docs (e.g., terraform-docs). | Documentation | ✓ |  | ✓ | ✓ |  |  | 3 |
| Order resource arguments predictably. | Style | ✓ |  |  | ✓ |  |  | 2 |
| Do not embed environment names/values in module logic. | Anti-patterns | ✓ |  | ✓ |  | ✓ |  | 3 |
| Avoid reading `terraform_remote_state` / data sources for caller-known values inside modules. | Anti-patterns | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use `prevent_destroy` on critical stateful resources. | Safety |  |  | ✓ |  | ✓ |  | 2 |
| Do not use `type = any` for variables. | Inputs & Outputs | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Avoid overly dynamic / heavy data source usage. | Performance | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Limit module nesting depth. | Structure |  |  |  | ✓ |  | ✓ | 2 |
| Avoid obscure/abbreviated variable names. | Style |  | ✓ |  |  |  | ✓ | 2 |
| Apply consistent tagging (e.g., Environment, Project, ManagedBy). | Style / Safety |  |  |  | ✓ | ✓ |  | 2 |
| Provide terraform test / example-based tests. | Testing | ✓ |  |  | ✓ |  | ✓ | 3 |
| Limit line length (e.g., 80 chars). | Style |  |  |  |  |  | ✓ | 1 |
| Use pessimistic version constraints (`~>`). | Versioning |  |  | ✓ |  | ✓ |  | 2 |
| Pass aliased providers explicitly to resources/modules. | State & Dependencies |  |  |  |  | ✓ |  | 1 |
| Name resources with a stable convention (e.g., `this` prefix, deterministic names). | Style | ✓ |  |  |  | ✓ |  | 2 |
| Avoid complex business logic in `locals`. | Style |  |  |  | ✓ | ✓ |  | 2 |
| Run drift detection on a schedule. | CI/CD | ✓ |  |  |  |  |  | 1 |
| Store/apply reviewed plan artifacts (don't replan during apply). | CI/CD | ✓ |  |  |  |  |  | 1 |
| Avoid `count`/`for_each` over very large collections. | Performance |  |  |  | ✓ |  |  | 1 |
| Use `file()`/`filebase64()` rather than inline keys/certs. | Safety |  |  |  | ✓ |  |  | 1 |
| Avoid unknown-at-plan-time values in `count`/`for_each`. | Resources |  |  | ✓ | ✓ |  |  | 2 |
| Use `dynamic` blocks sparingly. | Style |  |  | ✓ |  |  |  | 1 |
| Treat I/O contract changes as major-version bumps. | Versioning | ✓ |  | ✓ | ✓ |  |  | 3 |

## Notes on clustering decisions

- "Mark secrets sensitive" was merged across inputs even though some models wrote it only for outputs, others for both inputs and outputs; I considered these a single semantic rule since the intent (prevent secret disclosure) is identical.
- "Pin required provider versions" and "Use pessimistic `~>` constraints" were kept as two rows because some models only require *a* version constraint while others specifically mandate the `~>` operator — a regex matcher would likely conflate them.
- "Standard file layout" was clustered broadly: some models list exactly `main.tf/variables.tf/outputs.tf/versions.tf`, others add `README.md`, others just say "distinct folders." Treated as one rule since the spirit (predictable layout) matches; fine-grained differences (e.g., `versions.tf` presence) are lost.
- "Keep modules focused / single responsibility / avoid god modules" rolls up several phrasings: "one thing well," "cohesive unit," "don't mix resource types." Arguably gpt-4o-mini's "don't mix resource types in a single module" is narrower than Claude's "avoid god modules," but I clustered them.
- "Pin module sources" vs "Use semantic versioning for releases" are related but distinct (consumer vs producer side) — kept as separate rows.
- "Run terraform plan in CI on PRs" and "Apply only from protected branches / with approvals" appear together in most sources; I merged them into a single row since no model treated them as fully independent, though gpt-5 arguably splits them.
- gpt-4o-mini's "validate all input variables using type restrictions and default values" was counted toward both "declare types" and "use validation blocks" clusters, which is a judgment call.
- "Don't use `type = any`" was separated from "declare explicit types" because several models called it out specifically; a regex matcher would likely miss this nuance.
- xai/grok-3-mini's "prefix module outputs with module name" appears in no other response; kept as its own singleton rather than forced into the naming cluster.
- "Treat I/O contract changes as major-version bumps" was clustered from gpt-5's "Do not change output shapes without major version bump," Claude Opus's "MAJOR version bump" rule, and Haiku's "Mark breaking changes ... major version bump" — phrasings differ enough that fuzzy matching would likely miss.
- "Avoid overly dynamic / heavy data source usage" merges gpt-5's "bound data source usage," Haiku's "minimize data sources," grok's "avoid unnecessary API calls," and gemini's implicit performance guidance — these are close in intent but phrased very differently.