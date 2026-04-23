# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Provide a description for every variable and output | Section 2: Rules File | ✓ |  | ✓ |  | ✓ |  | 3 |
| **Mark outputs containing secrets, credentials, or PII as `sensitive = true`.** | Outputs and Output Contracts |  |  |  | ✓ | ✓ |  | 2 |
| Do use snake_case for variable names | Style |  | ✓ |  |  |  | ✓ | 2 |
| **Add a `type` constraint to every variable; avoid `any` unless absolutely necessary.** | Interface (Variables & Outputs) |  |  |  |  | ✓ |  | 1 |
| **Add a `validation` block for any constraint that is not captured by the variable type.** | Error Handling and Validation |  |  |  | ✓ |  |  | 1 |
| **Add a `validation` block for variables with interdependent or complex constraints.** | Interface (Variables & Outputs) |  |  |  |  | ✓ |  | 1 |
| **Assign `default = null` for optional variables and validate that null values are handled correctly.** | Variables and Input Contracts |  |  |  | ✓ |  |  | 1 |
| **Avoid comments that repeat what the code says; instead, explain the *why* (e.g., "must use a data source because the AMI ID changes weekly").** | Code Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Avoid complex data transformations and business logic in `locals`.** | Style & Logic |  |  |  |  | ✓ |  | 1 |
| **Avoid exporting dynamic or computed values that depend on external state (e.g., a data source lookup).** | Outputs and Output Contracts |  |  |  | ✓ |  |  | 1 |
| **Avoid hard-coded references to external state files or data sources.** | State Management and Dependencies |  |  |  | ✓ |  |  | 1 |
| **Avoid nesting modules more than one level deep.** | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Avoid using `for_each` or `count` to iterate over a large number of items (100+).** | Performance and Scale |  |  |  | ✓ |  |  | 1 |
| **Avoid using `random_*` resources for anything other than resource naming or non-critical values.** | Safety and Secrets |  |  |  | ✓ |  |  | 1 |
| **Create a `variables.tf`, `outputs.tf`, `main.tf`, and `README.md` for every module.** | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Declare required provider versions in a `versions.tf` file using pessimistic constraints.** | State & Dependencies |  |  |  |  | ✓ |  | 1 |
| **Design modules to manage a single, cohesive set of resources.** | Structure & Naming |  |  |  |  | ✓ |  | 1 |
| **Do not create implicit or circular dependencies between resources or modules.** | State Management and Dependencies |  |  |  | ✓ |  |  | 1 |
| **Do not define `provider` blocks inside a reusable module | State & Dependencies |  |  |  |  | ✓ |  | 1 |
| **Do not expose credentials, private keys, or secrets as module inputs.** | Variables and Input Contracts |  |  |  | ✓ |  |  | 1 |
| **Do not hardcode environment-specific values (e.g., 'prod', 'us-east-1').** | Interface (Variables & Outputs) |  |  |  |  | ✓ |  | 1 |
| **Do not output values that are only useful for debugging or internal use.** | Outputs and Output Contracts |  |  |  | ✓ |  |  | 1 |
| **Do not use `terraform.workspace` to alter resource behavior or naming | Style & Logic |  |  |  |  | ✓ |  | 1 |
| **Document all error messages that a module might produce.** | Error Handling and Validation |  |  |  | ✓ |  |  | 1 |
| **Document any assumptions about AWS regions, account setup, permissions, or external dependencies.** | Documentation and README |  |  |  | ✓ |  |  | 1 |
| **Document the cost and performance implications of the module.** | Documentation and README |  |  |  | ✓ |  |  | 1 |
| **Document the expected plan and apply times for the module and any scaling limits.** | Performance and Scale |  |  |  | ✓ |  |  | 1 |
| **Document the module purpose, inputs, and outputs in a `README.md` at the module root.** | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Enable `terraform fmt` and `terraform validate` checks in CI/CD; fail the build if they do not pass.** | CI/CD and Testing |  |  |  | ✓ |  |  | 1 |
| **Export all resource properties needed by downstream consumers as outputs.** | Interface (Variables & Outputs) |  |  |  |  | ✓ |  | 1 |
| **Export outputs that downstream modules and root modules need; do not export everything.** | Outputs and Output Contracts |  |  |  | ✓ |  |  | 1 |
| **For non-breaking releases (minor or patch), provide upgrade notes if any action is required from consumers.** | Versioning and Release Management |  |  |  | ✓ |  |  | 1 |
| **Format all `.tf` files with `terraform fmt -recursive`.** | Style & Logic |  |  |  |  | ✓ |  | 1 |
| **If the module is complex or widely used, write integration tests that apply the module in a test account and verify resource outputs.** | CI/CD and Testing |  |  |  | ✓ |  |  | 1 |
| **Include a working example in `examples/` subdirectory or in the README.** | Documentation and README |  |  |  | ✓ |  |  | 1 |
| **Keep one reusable module per repository.** | Structure & Naming |  |  |  |  | ✓ |  | 1 |
| **Keep resource arguments in a predictable order: `count`/`for_each`, required arguments, optional arguments, then `tags` and `depends_on`.** | Code Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Keep the number of data sources per module to a minimum.** | Performance and Scale |  |  |  | ✓ |  |  | 1 |
| **Limit a single module to a cohesive unit of infrastructure; avoid god modules.** | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Lint the module with `tflint` and enforce rules in CI/CD.** | CI/CD and Testing |  |  |  | ✓ |  |  | 1 |
| **Mark breaking changes clearly in the CHANGELOG and use a major version bump.** | Versioning and Release Management |  |  |  | ✓ |  |  | 1 |
| **Mark outputs and variables containing secrets, passwords, or PII with `sensitive = true`.** | Safety and Secrets |  |  |  | ✓ |  |  | 1 |
| **Minimize the number of resources per module; keep state size manageable.** | State Management and Dependencies |  |  |  | ✓ |  |  | 1 |
| **Name outputs clearly and document their contents with `description`.** | Outputs and Output Contracts |  |  |  | ✓ |  |  | 1 |
| **Name resources with a `this_` prefix (e.g., `aws_instance.this`).** | Structure & Naming |  |  |  |  | ✓ |  | 1 |
| **Name variables descriptively; avoid abbreviations.** | Variables and Input Contracts |  |  |  | ✓ |  |  | 1 |
| **Name variables, locals, and outputs using `snake_case`.** | Structure & Naming |  |  |  |  | ✓ |  | 1 |
| **Never embed credentials, API keys, or secrets in code or comments.** | Safety and Secrets |  |  |  | ✓ |  |  | 1 |
| **Pass aliased providers explicitly to resources and modules.** | State & Dependencies |  |  |  |  | ✓ |  | 1 |
| **Pin all module sources to a specific version tag in calling code (e.g., `version = "v1.2.3"`).** | Safety & Versioning |  |  |  |  | ✓ |  | 1 |
| **Prefer `for_each` over `count` for creating multiple resources from a list.** | State & Dependencies |  |  |  |  | ✓ |  | 1 |
| **Run `terraform plan` in a CI job for every pull request and merge to the main branch.** | Safety & Versioning |  |  |  |  | ✓ |  | 1 |
| **Run a `terraform plan` in a ephemeral or dedicated test account before merging.** | CI/CD and Testing |  |  |  | ✓ |  |  | 1 |
| **Set `description` and `type` on every variable; never use `type = any`.** | Variables and Input Contracts |  |  |  | ✓ |  |  | 1 |
| **Tag all taggable resources with at least `Environment`, `Project`, and `ManagedBy = "Terraform"`.** | Resource Naming and Tagging |  |  |  | ✓ |  |  | 1 |
| **Tag all taggable resources with identifying module metadata.** | Safety & Versioning |  |  |  |  | ✓ |  | 1 |
| **Tag releases with semantic versioning (e.g., `v1.2.3`) and include a CHANGELOG.md.** | Versioning and Release Management |  |  |  | ✓ |  |  | 1 |
| **Use `can()` and `try()` to handle unexpected input shapes gracefully; fail with a clear error message.** | Error Handling and Validation |  |  |  | ✓ |  |  | 1 |
| **Use `depends_on` only when a reference attribute is insufficient.** | Performance and Scale |  |  |  | ✓ |  |  | 1 |
| **Use `filebase64()` or `file()` to load certificates or keys from external files; do not paste them inline.** | Safety and Secrets |  |  |  | ✓ |  |  | 1 |
| **Use `for_each` to create multiple similar resources when the set is known at module invocation time.** | Resource Naming and Tagging |  |  |  | ✓ |  |  | 1 |
| **Use `ignore_changes` sparingly and only for attributes that are legitimately managed outside Terraform.** | State Management and Dependencies |  |  |  | ✓ |  |  | 1 |
| **Use `locals` to define a consistent naming scheme for all resources (e.g., `${var.environment}-${var.project}-<resource>`), and apply it systematically.** | Resource Naming and Tagging |  |  |  | ✓ |  |  | 1 |
| **Use `locals` to extract computed values and large blocks of logic.** | Code Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Use `validation` blocks to enforce non-trivial constraints (e.g., CIDR validity, enum membership).** | Variables and Input Contracts |  |  |  | ✓ |  |  | 1 |
| **Use `variables.tf` for all input variables; do not scatter them across `main.tf` or other files.** | Variables and Input Contracts |  |  |  | ✓ |  |  | 1 |
| **Use consistent indentation (2 spaces) and formatting.** | Code Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Use explicit `source` blocks with version constraints; never use `branch = "main"` or unversioned git URLs.** | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Use standard filenames: `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`.** | Structure & Naming |  |  |  |  | ✓ |  | 1 |
| **Use the `prevent_destroy` lifecycle block for critical, stateful resources (e.g., databases) | Safety & Versioning |  |  |  |  | ✓ |  | 1 |
| **Use version constraints in child module calls (e.g., `version = "~> 2.0"`) and document the rationale for the constraint.** | Versioning and Release Management |  |  |  | ✓ |  |  | 1 |
| **Validate that required inputs are not null and that optional inputs are handled explicitly.** | Error Handling and Validation |  |  |  | ✓ |  |  | 1 |
| **Write a README.md that includes: module purpose, usage example, input variables table, output values table, and any prerequisites or side effects.** | Documentation and README |  |  |  | ✓ |  |  | 1 |
| **Write comments for non-obvious logic, especially around dynamic resource creation or conditional branching.** | Code Style and Clarity |  |  |  | ✓ |  |  | 1 |
| Add a `validation` block for any constraint expressible in HCL (ranges, regexes, enum membership) | Variables |  |  | ✓ |  |  |  | 1 |
| Audience: Engineers and AI assistants authoring or reviewing Terraform modules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Auto-generate inputs/outputs tables (e.g., terraform-docs) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid Terraform workspaces for environments | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid `terraform_remote_state` inside reusable modules; accept IDs as variables instead | Style |  |  | ✓ |  |  |  | 1 |
| Avoid depends_on on modules and resources unless strictly necessary | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid giant modules and monolithic states; split when plans consistently exceed minutes or exceed provider rate limits | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid try() swallowing errors without logging a reason | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Bound data source usage and avoid overly-dynamic queries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare an explicit `type` on every variable; never use `any` | Variables |  |  | ✓ |  |  |  | 1 |
| Declare explicit types for all variables | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do adopt semantic versioning (e.g., 1.2.3) for modules | Versioning Strategy |  |  |  |  |  | ✓ | 1 |
| Do avoid hardcoding sensitive information within modules | Safety |  | ✓ |  |  |  |  | 1 |
| Do configure remote state backends like S3 or Terraform Cloud for all modules | State Layout |  |  |  |  |  | ✓ | 1 |
| Do define all outputs explicitly in `outputs.tf` with descriptions | Output Contracts |  |  |  |  |  | ✓ | 1 |
| Do define input variables and output values in separate files (`variables.tf` and `outputs.tf`) | Structure |  | ✓ |  |  |  |  | 1 |
| Do document all public variables and outputs in module README files | Style |  | ✓ |  |  |  |  | 1 |
| Do enforce a linter like `terraform fmt` for consistent formatting | Style |  |  |  |  |  | ✓ | 1 |
| Do ensure outputs are typed and include sensitive markings where applicable | Output Contracts |  |  |  |  |  | ✓ | 1 |
| Do implement CI pipelines that run `terraform plan` on every pull request | CI-Driven Workflows |  |  |  |  |  | ✓ | 1 |
| Do include input validation using `validation` blocks in variables | Safety |  |  |  |  |  | ✓ | 1 |
| Do limit line length to 80 characters | Style |  |  |  |  |  | ✓ | 1 |
| Do minimize the number of resources created within a single apply | Performance |  | ✓ |  |  |  |  | 1 |
| Do not change output shapes or semantics without a major version bump | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not configure any provider in modules, including minor ones | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not declare `provider` blocks inside modules; only `required_providers` in `versions.tf` | Structure |  |  | ✓ |  |  |  | 1 |
| Do not embed environment names (`"prod"`, `"dev"`) in module logic | Anti-patterns |  |  | ✓ |  |  |  | 1 |
| Do not generate resource names via `random_*` inside a module without exposing the result as an output | Anti-patterns |  |  | ✓ |  |  |  | 1 |
| Do not include provider blocks for major cloud providers in modules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not pass secrets via -var or TF_VAR in CI; use secure variable stores and sensitive inputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not read `data` sources inside a module for values the caller already knows (account ID, region, VPC ID) | Anti-patterns |  |  | ✓ |  |  |  | 1 |
| Do not share one state across unrelated systems | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use `depends_on` at the module block level unless you've proven an implicit dependency is missing | Resources & Safety |  |  | ✓ |  |  |  | 1 |
| Do not use `dynamic` blocks unless the nested block is genuinely variable in arity | Style |  |  | ✓ |  |  |  | 1 |
| Do not use lifecycle ignore_changes except for narrowly-justified attributes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use terraform.workspace to branch behavior for environments | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do optimize data sources and resources to avoid unnecessary API calls | Performance |  |  |  |  |  | ✓ | 1 |
| Do organize Terraform modules into distinct folders for clarity | Structure |  | ✓ |  |  |  |  | 1 |
| Do organize modules into a root module with submodules for distinct concerns, such as networking and compute | Structure |  |  |  |  |  | ✓ | 1 |
| Do prefix module outputs with the module name, e.g., `my_module_output` | Naming Conventions |  |  |  |  |  | ✓ | 1 |
| Do require automated tests, such as `terraform validate` and integration tests, before merging | CI-Driven Workflows |  |  |  |  |  | ✓ | 1 |
| Do tag releases in the module repository | Versioning Strategy |  |  |  |  |  | ✓ | 1 |
| Do use `count` or `for_each` cautiously to avoid unexpected resource creation | Safety |  |  |  |  |  | ✓ | 1 |
| Do use a consistent directory layout with files like `main.tf`, `variables.tf`, `outputs.tf`, and `README.md` | Structure |  |  |  |  |  | ✓ | 1 |
| Do use modules that support variable resource sizing based on inputs | Performance |  |  |  |  |  | ✓ | 1 |
| Do use workspace-specific state configurations | State Layout |  |  |  |  |  | ✓ | 1 |
| Do validate all input variables using type restrictions and default values | Error Handling |  | ✓ |  |  |  |  | 1 |
| Document deprecations and provide at least one minor release with warnings before removing inputs/outputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't allow direct `terraform apply` in production; enforce approval gates | CI-Driven Workflows |  |  |  |  |  | ✓ | 1 |
| Don't create data sources unnecessarily | Performance |  | ✓ |  |  |  |  | 1 |
| Don't expose unnecessary details in outputs; keep them minimal and focused on essential data | Output Contracts |  |  |  |  |  | ✓ | 1 |
| Don't hardcode state file paths; use variables or remote backends | State Layout |  |  |  |  |  | ✓ | 1 |
| Don't ignore errors during provisioning | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don't include debug outputs in production modules | Performance |  |  |  |  |  | ✓ | 1 |
| Don't mix different resource types in a single module | Structure |  | ✓ |  |  |  |  | 1 |
| Don't nest modules deeper than three levels | Structure |  |  |  |  |  | ✓ | 1 |
| Don't output sensitive information inadvertently | Safety |  | ✓ |  |  |  |  | 1 |
| Don't release modules without a changelog | Versioning Strategy |  |  |  |  |  | ✓ | 1 |
| Don't skip `terraform plan` reviews in CI; always diff outputs | Safety |  |  |  |  |  | ✓ | 1 |
| Don't use acronyms in variable names unless they are widely understood, e.g., avoid "ec2_inst" in favor of "ec2_instance" | Naming Conventions |  |  |  |  |  | ✓ | 1 |
| Don't use inline comments for critical logic; prefer descriptive variable names | Style |  |  |  |  |  | ✓ | 1 |
| Don't use obscure or abbreviated variable names | Style |  | ✓ |  |  |  |  | 1 |
| Exclude terraform.lock.hcl from published library modules; commit it for root modules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Export only what callers need: IDs, ARNs, endpoints, names | Outputs |  |  | ✓ |  |  |  | 1 |
| Generate and post a plan on PRs; apply only from protected branches with approvals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Group related functionality into a single module; do not create one-module-per-resource | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include `moved {}` blocks when renaming or restructuring resources | Resources & Safety |  |  | ✓ |  |  |  | 1 |
| Include an `examples/` directory with at least one runnable example per major use case | Structure |  |  | ✓ |  |  |  | 1 |
| Keep interpolation expressions short; extract complex logic into `locals` | Style |  |  | ✓ |  |  |  | 1 |
| Keep outputs minimal and avoid exposing secrets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep state granular by blast radius (e.g., per service or tier) and per environment | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Maintain a README with: module purpose, inputs/outputs table, examples, version compatibility, and breaking change policy | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Maintain a `CHANGELOG.md` updated in the same PR as the change | Versioning & Distribution |  |  | ✓ |  |  |  | 1 |
| Mark any output derived from a secret as `sensitive = true` | Outputs |  |  | ✓ |  |  |  | 1 |
| Mark secret inputs as sensitive and do not set defaults for secrets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name booleans with a positive `enable_`/`create_` prefix, not `disable_` | Variables |  |  | ✓ |  |  |  | 1 |
| Name resources predictably and deterministically; avoid random suffixes unless required | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never output secrets in plaintext; avoid printing them in logs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never output values that can change across applies without a stable identity (e.g., timestamps) | Outputs |  |  | ✓ |  |  |  | 1 |
| Never pass a value unknown at plan time to `for_each` or `count` | Resources & Safety |  |  | ✓ |  |  |  | 1 |
| Only set a `default` when the default is safe in every environment; otherwise require the caller to supply it | Variables |  |  | ✓ |  |  |  | 1 |
| Order arguments predictably: required first, optional next, computed last | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin `required_version` and every entry in `required_providers` to a `~>` constraint | Structure |  |  | ✓ |  |  |  | 1 |
| Pin module sources: use version = for registry modules or ref= tags for git sources | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin required_providers with compatible ranges (>= X.Y, < X+1.0) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place code in `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf` at minimum | Structure |  |  | ✓ |  |  |  | 1 |
| Prefer `object({...})` over `map(any)` for structured inputs | Variables |  |  | ✓ |  |  |  | 1 |
| Prefer data pre-computation in locals and keep expressions simple | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer for_each over count for resources and modules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer optional() types over default = null for complex objects | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a minimal, predictable file layout: main.tf, variables.tf, outputs.tf, versions.tf, README.md, examples/ | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide at least one runnable example under examples/ (minimal and/or complete) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide terraform test or example-based tests that init/plan successfully | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put `lifecycle { prevent_destroy = true }` on stateful resources (databases, stateful volumes) | Resources & Safety |  |  | ✓ |  |  |  | 1 |
| Put only module-local resources in a module; keep environment wiring in root modules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require a minimum Terraform version in versions.tf | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run `terraform apply` only from CI on the protected branch, against a locked remote backend | CI/CD |  |  | ✓ |  |  |  | 1 |
| Run `terraform fmt -check -recursive`, `terraform validate`, `tflint`, and a security scanner (tfsec, checkov, or trivy) on every PR | CI/CD |  |  | ✓ |  |  |  | 1 |
| Run `terraform plan` in CI on PR and post output as a comment | CI/CD |  |  | ✓ |  |  |  | 1 |
| Run drift detection on a schedule and surface differences | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run terraform fmt, validate, tflint, and security scanning (tfsec or checkov) in CI on every PR | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run terraform fmt; do not commit unformatted files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Reusable Terraform modules that define cloud infrastructure and are consumed by root modules across environments | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ship a `README.md` with usage example, inputs, outputs, and requirements, generated by `terraform-docs` | Structure |  |  | ✓ |  |  |  | 1 |
| Split `main.tf` by resource domain (e.g., `iam.tf`, `network.tf`) once it exceeds ~200 lines | Structure |  |  | ✓ |  |  |  | 1 |
| Store plan artifacts; do not re-plan silently during apply | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Tag module releases with SemVer (`vMAJOR.MINOR.PATCH`) | Versioning & Distribution |  |  | ✓ |  |  |  | 1 |
| Treat any change to variable names, variable types without a default, output names, or minimum provider versions as a MAJOR version bump | Versioning & Distribution |  |  | ✓ |  |  |  | 1 |
| Use `for_each` with a string-keyed map, not `count`, for collections of non-identical resources | Resources & Safety |  |  | ✓ |  |  |  | 1 |
| Use `lifecycle { ignore_changes = [...] }` only for fields genuinely managed outside Terraform, and comment why | Resources & Safety |  |  | ✓ |  |  |  | 1 |
| Use `snake_case` for all variable, output, local, and resource names | Variables |  |  | ✓ |  |  |  | 1 |
| Use a remote backend with locking for all real environments | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use moved blocks to refactor addresses instead of recreating resources | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use one state per environment per blast-radius slice (e.g., `prod/network`, `prod/apps`) | CI/CD |  |  | ✓ |  |  |  | 1 |
| Use precondition and postcondition blocks on resources/outputs for critical guarantees | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use snake_case for variable, local, and output names | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use tflint with provider-specific rulesets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use validation blocks on variables to enforce allowed values and formats | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use variable validation and preconditions for non-trivial invariants | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate custom conditions with pre/postconditions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Version modules with SemVer and publish tags; treat inputs/outputs as the API | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.

- **Provide a description for every variable and output** — avg similarity 65 (substantively similar but differently worded — genuine convergence)
  - `openai/gpt-5`: Provide a description for every variable and output. Descriptions are the end-user docstring.
  - `anthropic/claude-opus-4-7`: Provide a `description` for every variable. Reviewers and `terraform-docs` both depend on it.
  - `vertex_ai/gemini-2.5-pro`: **Provide a non-empty `description` for every variable and output.**
- ****Mark outputs containing secrets, credentials, or PII as `sensitive = true`.**** — avg similarity 85 (substantively similar but differently worded — genuine convergence)
  - `anthropic/claude-haiku-4-5`: **Mark outputs containing secrets, credentials, or PII as `sensitive = true`.**
  - `vertex_ai/gemini-2.5-pro`: **Mark outputs containing secrets as `sensitive = true`.**
- **Do use snake_case for variable names** — avg similarity 79 (substantively similar but differently worded — genuine convergence)
  - `openai/gpt-4o-mini`: Do use snake_case for variable names. This increases readability and aligns with community standards.
  - `xai/grok-3-mini`: Do use snake_case for all variable names. This improves readability and aligns with Terraform's conventions.

## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

