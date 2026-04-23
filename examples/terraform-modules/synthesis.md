# Synthesis of Terraform Module Best Practices

## 1. Consensus Rules

### Structure & File Layout

- **Use a standard file layout (`main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, `README.md`).** Predictable structure aids navigation and onboarding. (substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok; GPT-4o-mini partial)
- **Keep modules focused on a single cohesive purpose; avoid "god modules."** Single-responsibility modules are more reusable, testable, and have smaller blast radius. (substantively similar wording across all six models)
- **Include at least one runnable example under `examples/`.** Examples serve as documentation and double as integration tests. (substantively similar across GPT-5, Claude Opus, Claude Haiku)

### Provider Configuration

- **Do not declare `provider` blocks inside reusable modules; only `required_providers` in `versions.tf`.** Provider configuration belongs to the root module so modules can be reused across accounts/regions. (substantively similar across GPT-5, Claude Opus, Gemini)
- **Pin `required_providers` with bounded version constraints (e.g., `~>`).** Floating versions cause silent drift and surprise breakage. (near-identical wording across GPT-5, Claude Opus, Gemini; supported by Claude Haiku, Grok)
- **Declare `required_version` for Terraform itself in `versions.tf`.** New language features need known baselines. (GPT-5, Claude Opus)

### Variables (Inputs)

- **Declare an explicit `type` on every variable; avoid `any`.** Types are the module's contract and catch errors at plan time. (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)
- **Provide a non-empty `description` on every variable.** Descriptions are the end-user documentation consumed by `terraform-docs` and reviewers. (near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Use `snake_case` for variables, locals, outputs, and resource names.** Matches HCL community conventions and improves tooling support. (near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)
- **Add `validation` blocks for non-trivial input constraints.** Fail fast at plan time rather than during apply. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Do not accept credentials/secrets as plain inputs without `sensitive = true`; never set defaults for secrets.** Prevents secrets from leaking into logs, state diffs, and version control. (substantively similar across GPT-5, Claude Opus, Claude Haiku, GPT-4o-mini, Gemini)

### Outputs

- **Provide a `description` on every output.** Outputs form a public contract; descriptions document it. (near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)
- **Mark outputs derived from secrets as `sensitive = true`.** Unmarked secrets appear in plans, CI logs, and state. (near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, GPT-4o-mini)
- **Keep outputs minimal—expose only what consumers actually need.** Smaller contracts reduce coupling to internals and ease refactoring. (substantively similar across GPT-5, Claude Opus, Claude Haiku)

### Resources & Lifecycle

- **Prefer `for_each` with a string-keyed map over `count` for collections.** `for_each` keeps addresses stable when items are added, removed, or reordered. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)
- **Use `lifecycle { ignore_changes }` sparingly and only for fields genuinely managed outside Terraform, with a comment explaining why.** Broad ignores silently hide drift. (substantively similar across GPT-5, Claude Opus, Claude Haiku)
- **Use `depends_on` on modules/resources only when implicit dependencies are insufficient.** Over-use serializes plans and masks design smells. (substantively similar across GPT-5, Claude Opus, Claude Haiku)
- **Use `moved {}` blocks when renaming/restructuring resources rather than forcing recreation.** Preserves state across refactors. (substantively similar across GPT-5, Claude Opus)

### Versioning & Distribution

- **Tag module releases with Semantic Versioning (`vMAJOR.MINOR.PATCH`).** Enables safe, intentional upgrades by consumers. (near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Pin module `source` references in calling code to a specific version tag or `ref=`.** Prevents silent breakage from upstream changes. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Maintain a `CHANGELOG.md` updated in the same PR as the change.** Release notes written later are wrong. (substantively similar across Claude Opus, Claude Haiku, Grok)
- **Treat input/output renames, type changes, or removals as breaking (MAJOR) changes.** Outputs and inputs are a public API. (substantively similar across GPT-5, Claude Opus, Claude Haiku)

### Documentation

- **Maintain a `README.md` covering purpose, usage example, inputs, outputs, and requirements (ideally auto-generated via `terraform-docs`).** Stale docs are worse than no docs. (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, GPT-4o-mini)

### CI/CD & Workflow

- **Run `terraform fmt -check`, `terraform validate`, `tflint`, and a security scanner (tfsec/checkov/trivy) on every PR.** Automated quality gate catches issues before review. (near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)
- **Run `terraform plan` on PRs and surface the output for review; apply only from protected branches via CI.** Review-before-apply prevents accidents; laptop applies cause drift. (substantively similar across GPT-5, Claude Opus, Gemini, Grok)

### Style

- **Format all `.tf` files with `terraform fmt`.** Consistent formatting standardizes diffs. (near-identical across GPT-5, Claude Haiku, Gemini, Grok)

## 2. Strong Minority Rules

- **Use `precondition`/`postcondition` blocks for critical guarantees on resources and outputs.** (GPT-5) — Kept because Terraform ≥1.2 has strong support for these, they catch provider drift early, and complement `validation` blocks.
- **Name boolean variables with a positive prefix (`enable_`, `create_`), not `disable_`.** (Claude Opus, GPT-5 mentioned) — Kept because double negatives cause real bugs and this is mechanically checkable.
- **Do not embed environment names (`prod`, `dev`, `staging`) in module logic.** (Claude Opus) — Kept because environment-branching inside modules is a common and damaging anti-pattern.
- **Avoid `terraform_remote_state` inside reusable modules; accept IDs as inputs.** (Claude Opus, Claude Haiku) — Kept because it couples modules to a specific state layout and breaks reusability.
- **Tag all taggable resources with identifying metadata (`Environment`, `Project`, `ManagedBy`).** (Claude Haiku, Gemini) — Kept because it enables cost allocation and operational inventory and is widely expected.
- **Use `prevent_destroy` on critical stateful resources (databases, KMS keys).** (Claude Opus, Gemini) — Kept as a narrowly-applied safety measure; flagged `(contested)`.
- **Store plan artifacts in CI; do not re-plan silently during apply.** (GPT-5) — Kept because it closes a real loophole where apply drifts from reviewed plan.
- **Do not pass secrets via `-var` or `TF_VAR_*` in CI; use secure stores.** (GPT-5) — Kept because command-line secrets leak into process lists and CI logs.
- **Keep state granular by environment and blast-radius slice (e.g., `prod/network`, `prod/apps`).** (GPT-5, Claude Opus) — Kept as architectural guidance even though it belongs to root configs more than modules.

## 3. Divergences

### Terraform Workspaces for Environments
- **Against**: GPT-5 and Claude Opus explicitly discourage `terraform.workspace` for environment branching.
- **Neutral/Not mentioned**: Other models.
- **Synthesis**: Adopt the "against" position. Workspaces are a weak environment boundary; per-environment state is safer. Mark as `(contested)` since small orgs use them successfully.

### Default Values
- **Claude Opus**: "Only set a `default` when the default is safe in every environment; otherwise require the caller to supply it."
- **Claude Haiku**: "Assign `default = null` for optional variables… explicit nullability is clearer."
- **GPT-5**: Recommends `optional()` object attributes over `default = null` in modern Terraform.
- **Synthesis**: Prefer `optional()` types for structured inputs (Terraform ≥1.3); use `default = null` where interop requires it; never default required unsafe inputs. Mark `(contested)`.

### Module Granularity (Thin vs. Thick)
- **Claude Opus**: Thin for libraries, thick for platform modules.
- **Gemini**: Prefer smaller, focused, composable modules.
- **Claude Haiku**: Avoid god modules; composable building blocks.
- **Synthesis**: Bias toward smaller, focused modules; accept opinionated "thick" modules for internal platform use. This is taste-driven and not mechanically checkable.

### Resource Naming Convention
- **Gemini**: Use `this_` prefix (e.g., `aws_instance.this`).
- **Others**: No specific prefix convention; just `snake_case`.
- **Synthesis**: Recommend `this` as the primary resource label when a module manages a single primary resource, but do not enforce. Not a consensus rule.

### Line Length Limits
- **Grok**: 80-character limit.
- **Others**: Not mentioned.
- **Synthesis**: Reject as a hard rule — `terraform fmt` doesn't enforce line length and HCL often exceeds 80 chars naturally. Keep only as a soft style preference.

### Lock File (`.terraform.lock.hcl`) for Published Modules
- **GPT-5**: Exclude lock file from published library modules; commit for root modules.
- **Others**: Not addressed.
- **Synthesis**: Follow HashiCorp's guidance: commit in root modules, exclude from published library modules. Mark `(contested)`.

### Number of Resources per Module
- **GPT-4o-mini**: Suggests a hard cap (~20).
- **Claude Haiku**: Warn at 100+.
- **Others**: Qualitative guidance only.
- **Synthesis**: Avoid a hard numeric limit; use plan time as the practical signal. A count threshold creates false failures on legitimately large modules.

## 4. Notable Omissions

- **`for_each` over `count`**: Omitted by Grok and GPT-4o-mini despite being a near-universal Terraform recommendation. This is a conspicuous gap.
- **Provider blocks not in modules**: Absent from Claude Haiku, GPT-4o-mini, and Grok. This is one of the most consequential mistakes for reusable modules; its omission is notable.
- **`moved {}` blocks for refactoring**: Only GPT-5 and Claude Opus raise it. Given Terraform ≥1.1 support, this should be more widespread.
- **Sensitive output marking**: GPT-4o-mini and Grok give weaker treatment than the other four. Grok omits output-level sensitivity handling entirely.
- **Variable `validation` blocks**: Grok and GPT-4o-mini do not emphasize them.
- **`terraform-docs` for README generation**: Absent from Grok and GPT-4o-mini.
- **Security scanner (tfsec/checkov) in CI**: Absent from GPT-4o-mini and Gemini; this is a widespread industry norm.
- **Semantic Versioning**: Omitted by GPT-4o-mini despite being a near-universal practice.

## 5. Shared Deterministic Checks

### Checks Multiple Models Converged On

- **Check** — Required module files (`main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, `README.md`) exist at module root.
  - **Signal**: Directory listing.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance**: GPT-5 and Claude Opus additionally require `examples/` subdirectory; Gemini permits alternative filenames if content is equivalent.

- **Check** — Every `variable` block has both a `type` and a non-empty `description`, and `type` is not `any`.
  - **Signal**: Parsed HCL AST of `variable` blocks.
  - **Tool candidate**: `tflint` (`terraform_typed_variables`, `terraform_documented_variables`).
  - **Raised by**: GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance**: Claude Opus and Claude Haiku additionally flag `map(any)`/`list(any)`; Gemini allows `any` with suppression.

- **Check** — Every `output` block has a non-empty `description`.
  - **Signal**: Parsed HCL AST of `output` blocks.
  - **Tool candidate**: `tflint` (`terraform_documented_outputs`).
  - **Raised by**: GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance**: Agreement on substance.

- **Check** — Outputs whose names or values suggest secrets have `sensitive = true`.
  - **Signal**: Parsed HCL AST plus regex on output names (`password|secret|token|key|credential|pem|private`).
  - **Tool candidate**: ad-hoc (partially covered by `terraform validate` when source is already `sensitive`).
  - **Raised by**: GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance**: Claude Opus uses data-flow from known secret-producing resources; others use name heuristics. Heuristics carry false-positive/negative risk.

- **Check** — All identifiers (variables, outputs, locals, resources) use `snake_case` matching `^[a-z][a-z0-9_]*$`.
  - **Signal**: Parsed HCL AST identifiers.
  - **Tool candidate**: `tflint` (`terraform_naming_convention`).
  - **Raised by**: GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance**: Agreement on substance.

- **Check** — No top-level `provider` block for major cloud providers inside a module directory.
  - **Signal**: Parsed HCL AST; allowlist/denylist of provider names.
  - **Tool candidate**: `tflint` (`terraform_module_provider_declaration`).
  - **Raised by**: GPT-5, Claude Opus, Gemini.
  - **Variance**: GPT-5 restricts to major cloud providers; Claude Opus and Gemini apply universally.

- **Check** — `required_providers` entries have bounded version constraints (presence of `~>` or both `>=` and `<`).
  - **Signal**: Parsed `terraform { required_providers {} }` block.
  - **Tool candidate**: `tflint` (`terraform_required_providers`, `terraform_required_version`).
  - **Raised by**: GPT-5, Claude Opus, Gemini, Grok (indirectly).
  - **Variance**: Claude Opus requires `~>` specifically; GPT-5 accepts any bounded range.

- **Check** — `module` blocks that reference remote sources include a `version` attribute or a pinned `ref=` query parameter, and no branch names (`main`, `master`).
  - **Signal**: Parsed HCL AST of `module` blocks; URL parsing on `source`.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance**: Claude Haiku additionally rejects `version = "*"` and overly permissive ranges.

- **Check** — All `.tf` files pass `terraform fmt -check -recursive`.
  - **Signal**: Exit code of `terraform fmt -check`.
  - **Tool candidate**: `terraform fmt`.
  - **Raised by**: GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance**: None.

- **Check** — CI configuration (GitHub Actions, GitLab CI, etc.) invokes `terraform fmt -check`, `terraform validate`, `tflint`, and a security scanner (tfsec/checkov/trivy) on PRs.
  - **Signal**: YAML workflow files or CI run logs.
  - **Tool candidate**: ad-hoc parsing of workflow YAML.
  - **Raised by**: GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance**: Scanner choice varies (tfsec, checkov, trivy); match any member of the set.

- **Check** — Repository has at least one git tag matching SemVer pattern `^v?\d+\.\d+\.\d+(-[\w.]+)?$`.
  - **Signal**: Git tag listing.
  - **Tool candidate**: ad-hoc regex on `git tag` output.
  - **Raised by**: Claude Opus, Claude Haiku, Grok.
  - **Variance**: Grok omits `v` prefix.

- **Check** — `count` on resources is flagged unless expression is a boolean toggle (`? 1 : 0`).
  - **Signal**: Parsed HCL AST of resource blocks.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: GPT-5, Claude Opus, Claude Haiku.
  - **Variance**: Treated as warning vs. hard failure varies. False positives expected.

### Singleton Checks

- **Check** — Boolean variables use positive prefixes (`enable_`, `create_`, `is_`, `allow_`, `has_`); reject `disable_`, `skip_`, `no_`, `deny_`.
  - **Signal**: AST of `variable` blocks with `type = bool`.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: Claude Opus.

- **Check** — No `data "terraform_remote_state"` block inside a module directory (excluding root configs).
  - **Signal**: AST or grep of `.tf` files.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: Claude Opus.

- **Check** — Environment names (`"prod"`, `"dev"`, `"staging"`, `"qa"`) do not appear as string literals in conditional expressions inside module `.tf` files.
  - **Signal**: AST or grep of `.tf` files.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: Claude Opus.

- **Check** — `CHANGELOG.md` is updated in any PR that modifies `.tf` files.
  - **Signal**: Git diff for the PR.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: Claude Opus.

- **Check** — No inline PEM/certificate content (e.g., `-----BEGIN ...-----`) in `.tf` files; require `file()`/`filebase64()`.
  - **Signal**: Regex on raw source.
  - **Tool candidate**: `gitleaks`, `detect-secrets`, or ad-hoc regex.
  - **Raised by**: Claude Haiku.

- **Check** — `README.md` contains `terraform-docs` marker comments and generated content matches source.
  - **Signal**: `terraform-docs --output-check`.
  - **Tool candidate**: `terraform-docs`.
  - **Raised by**: Claude Opus.

- **Check** — `terraform` block with a remote `backend` declaration exists (for root configs/examples, not library modules).
  - **Signal**: AST of `terraform {}` block.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: GPT-5, Grok.

- **Check** — Taggable cloud resources include `Environment`, `Project`, and `ManagedBy` tags.
  - **Signal**: AST of resource blocks; type registry of taggable resources.
  - **Tool candidate**: `tflint` with provider plugins.
  - **Raised by**: Claude Haiku, Gemini.

- **Check** — No references to `terraform.workspace` in module source.
  - **Signal**: Grep or AST of identifiers.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: GPT-5.

- **Check** — No `TF_VAR_*` environment variables or `-var` flags carrying secrets in CI config.
  - **Signal**: Grep on CI YAML.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: GPT-5.

- **Check** — Resource/module renames in a PR diff are accompanied by corresponding `moved {}` blocks.
  - **Signal**: Git diff of block headers plus AST of `moved` blocks.
  - **Tool candidate**: ad-hoc.
  - **Raised by**: GPT-5, Claude Opus.

---

## 6. Final Rules File

# Terraform Module Rules

**Scope:** Reusable Terraform modules that define cloud infrastructure and are consumed by root modules or other modules.
**Audience:** Engineers and AI coding assistants authoring, reviewing, or publishing Terraform modules.
**Assumptions:** Terraform ≥ 1.3 (OpenTofu compatible), remote state, CI/CD-gated applies.

Rules marked `(contested)` reflect genuine practitioner disagreement; follow them unless your context provides a documented exception.

---

## Structure & Organization

- **Provide a standard file layout: `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, `README.md`.** Predictable structure aids navigation.
- **Split `main.tf` by resource domain (`iam.tf`, `network.tf`) once it grows beyond ~200 lines.** Keeps files focused.
- **Design each module to manage a single cohesive set of resources; avoid "god modules."** Smaller modules are more reusable, testable, and have smaller blast radius.
- **Include at least one runnable example under `examples/`.** Examples document usage and double as integration tests.
- **Avoid nesting modules more than one level deep.** Deep nesting obscures dependencies and hinders testing.

## Provider Configuration

- **Do not declare `provider` blocks inside reusable modules; only `required_providers` in `versions.tf`.** Provider configuration belongs to the root module so modules can be reused across accounts, regions, and aliases.
- **Declare `required_version` for Terraform in `versions.tf`.** Pins the language baseline.
- **Pin every `required_providers` entry with a bounded constraint (`~>` or `>= x, < y`).** Floating versions cause silent drift.
- **Pass aliased providers explicitly to child modules.** Makes cross-region/cross-account dependencies visible.

## Variables (Inputs)

- **Declare an explicit `type` on every variable; never use `any` (including `map(any)`, `list(any)`).** Types are the module's contract.
- **Prefer `object({...})` over loose `map` types for structured inputs.** Catches typos at plan time.
- **Provide a non-empty `description` on every variable.** The description is the consumer-facing docstring.
- **Set a `default` only when it is safe in every environment; otherwise require the caller to supply it.** Defaults hide intent.
- **Prefer `optional()` attributes on object types for optional fields over `default = null` where Terraform version permits.** More precise than null sentinels. `(contested)`
- **Add `validation` blocks for constraints not expressible via type alone (enums, regex, ranges).** Fail fast at plan.
- **Name booleans with a positive prefix (`enable_`, `create_`, `is_`, `allow_`, `has_`); avoid `disable_`, `skip_`, `no_`.** Double negatives cause bugs.
- **Use `snake_case` for all variable, output, local, and resource names.** Matches HCL convention.
- **Do not accept secrets as plain variables without `sensitive = true`, and never set defaults for secret inputs.** Prevents leakage into logs and state.

## Outputs

- **Expose only what downstream consumers need (IDs, ARNs, endpoints); do not export raw resource objects.** Minimizes coupling to internals.
- **Provide a non-empty `description` on every output.** Outputs are a public API.
- **Mark outputs derived from secrets as `sensitive = true`.** Unmarked secrets land in CI logs and state diffs.
- **Treat output renames, removals, or shape changes as MAJOR breaking changes.** Outputs are a versioned contract.
- **Avoid outputs whose values change every apply without a stable identity (e.g., timestamps).** Causes spurious downstream diffs.

## Resources, Lifecycle & State

- **Prefer `for_each` with a string-keyed map over `count` for collections of non-identical resources.** Addresses survive reordering and removal.
- **Use `count` only for simple boolean toggles (`count = var.create ? 1 : 0`).** Linear indexing over lists is fragile.
- **Never pass values unknown at plan time to `for_each` or `count`.** Forces `-target` workarounds.
- **Use `lifecycle { ignore_changes = [...] }` only for fields genuinely managed outside Terraform, with a comment explaining why.** Otherwise silently hides drift.
- **Use `lifecycle { prevent_destroy = true }` on critical stateful resources (databases, KMS keys, stateful volumes).** Cheap insurance against accidental destruction. `(contested)`
- **Add `moved {}` blocks when renaming or restructuring resources.** Preserves state across refactors.
- **Use `depends_on` only when an implicit dependency is demonstrably missing.** Over-use serializes plans.
- **Do not use `terraform_remote_state` data sources inside reusable modules; accept IDs as inputs instead.** Couples modules to a specific state layout.
- **Do not embed environment names (`"prod"`, `"dev"`, `"staging"`) in module logic.** Modules must be environment-agnostic; callers supply context.
- **Do not use `terraform.workspace` to branch behavior for environments.** Workspaces are not an environment boundary. `(contested)`
- **Keep state granular per environment and blast-radius slice (e.g., `prod/network`, `prod/apps`).** Smaller states unlock faster and refactor more safely. `(contested)`

## Tagging

- **Tag all taggable resources with at least `Environment`, `Project`, and `ManagedBy = "Terraform"`, using a `local.common_tags` + `merge()` pattern.** Enables cost allocation, operational inventory, and policy enforcement.

## Versioning & Distribution

- **Tag module releases with Semantic Versioning (`vMAJOR.MINOR.PATCH`).** Enables safe upgrades.
- **Pin `source` references in calling code with `version = "..."` (registry) or `?ref=vX.Y.Z` (git).** Prevents silent upstream breakage. Never use `main`/`master` or unversioned URLs.
- **Treat input renames, type changes (without a safe default), output renames/removals, or minimum-provider bumps as MAJOR changes.** Breaking the contract silently destroys trust.
- **Maintain a `CHANGELOG.md` updated in the same PR as the change.** Notes written later are wrong.

## Documentation

- **Maintain a `README.md` with purpose, usage example, inputs table, outputs table, and requirements.** Ideally auto-generated with `terraform-docs` markers.
- **Document assumptions about accounts, regions, IAM permissions, and external dependencies.** Reduces misuse.
- **Document meaningful cost/performance trade-offs (e.g., multi-AZ pricing).** Helps consumers make informed choices.

## Safety & Secrets

- **Never embed credentials, API keys, or secrets in code or comments.** Use secret managers (AWS Secrets Manager, Vault) or CI secret stores.
- **Load certificates/keys via `file()` or `filebase64()` from external files, not inline heredocs.** Keeps secrets out of source history.
- **Do not pass secrets via `-var` or `TF_VAR_*` in CI; use secure variable stores and sensitive inputs.** CLI/env vars leak in logs.

## CI/CD & Workflow

- **Run `terraform fmt -check -recursive`, `terraform validate`, `tflint`, and a security scanner (tfsec, checkov, or trivy) on every PR.** Non-negotiable quality gate.
- **Run `terraform plan` in CI on PRs and post the output for reviewers.** Reviewers must see the plan before approval.
- **Run `terraform apply` only from CI on protected branches, against a locked remote backend, and consuming the previously-generated plan artifact.** Laptop applies and re-plans during apply cause drift.
- **Use `tflint` with provider-specific rulesets.** Catches deprecated arguments and provider misuse.
- **Run drift detection on a schedule.** Surfaces out-of-band changes early.

## Error Handling

- **Use variable `validation` blocks to enforce allowed values, formats, and ranges.** Early errors beat late failures.
- **Use `precondition`/`postcondition` on resources and outputs for critical guarantees.** Preconditions catch invalid inputs; postconditions catch provider drift.
- **Use `try()` and `can()` only where input shape variability is legitimate; do not swallow errors silently.** Hidden failures produce brittle modules.

## Style

- **Format all `.tf` files with `terraform fmt` and enforce `-check` in CI.** Standardizes diffs.
- **Order resource arguments predictably: `count`/`for_each`, required, optional, then `tags`, `lifecycle`, `depends_on`.** Aids scanning.
- **Extract complex expressions into `locals`; keep inline interpolation short.** Single-use locals can stay inline.
- **Avoid complex business logic or data transformations inside `locals`.** HCL is not a general-purpose language; such logic is hard to test.
- **Use `dynamic` blocks only when the nested block's arity is genuinely variable.** Dynamic blocks obscure intent.

## Anti-patterns

- **Do not read `data` sources inside a module for values the caller already knows (account ID, region, VPC ID).** Pass them as inputs.
- **Do not generate resource names via `random_*` inside a module without exposing the result as an output.** Callers lose the ability to reference them.
- **Do not create hundreds of resources in a single module invocation.** Plan time degrades; split into multiple modules or pipelines.