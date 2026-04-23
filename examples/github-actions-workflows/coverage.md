# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Do not trigger workflows on `push` to main without also gating on protected branches.** Pair `push` triggers with explicit branch filters (`branches: [main]`) and ensure the branch is protected | Triggers & Event Filtering |  |  |  | ✓ |  |  | 1 |
| **(contested) For blue-green or canary deployments, implement them in the workflow or a called reusable workflow.** Some teams prefer delegating this to infrastructure-as-code tools (Terraform, Helm) | Deployment Safety |  |  |  | ✓ |  |  | 1 |
| **(contested) Use `continue-on-error: true` sparingly and only for non-critical steps.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Add comments explaining non-obvious conditional logic, especially in `if:` conditions.** Rationale: future readers and maintainers won't have to reverse-engineer intent | Maintainability & Documentation |  |  |  | ✓ |  |  | 1 |
| **Avoid YAML anchors (`&`, `*`) in workflows.** GitHub supports them but they hurt readability and aren't supported uniformly across all contexts | Style |  |  | ✓ |  |  |  | 1 |
| **Avoid downloading large unnecessary artifacts.** Use `actions/download-artifact` only for artifacts you use; clean up large temporary artifacts after use | Performance |  |  |  | ✓ |  |  | 1 |
| **Avoid the `pull_request_target` trigger unless you fully understand its security implications.** | Safety and Security |  |  |  |  | ✓ |  | 1 |
| **Cache dependencies and build outputs between jobs.** | Performance and Cost |  |  |  |  | ✓ |  | 1 |
| **Capture and upload test reports (JUnit XML, coverage, etc.) as artifacts for post-workflow analysis.** Use `actions/upload-artifact` with a clear `name` | Testing & Verification |  |  |  | ✓ |  |  | 1 |
| **Comment the `why`, not the `what`.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Declare `on:` triggers explicitly with filters (`branches`, `paths`, `types`).** Unfiltered `on: push` burns minutes and triggers on tags you didn't mean | Structure |  |  | ✓ |  |  |  | 1 |
| **Declare `permissions:` at the workflow level with the minimum scopes; override per-job only to elevate.** The default `GITHUB_TOKEN` is too broad; start from `contents: read` | Safety |  |  | ✓ |  |  |  | 1 |
| **Define a `name` field for each workflow.** Use a human-readable string that matches the filename intent | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Define explicit `needs` dependencies between jobs.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Define the most restrictive `permissions` possible at the top level.** | Safety and Security |  |  |  |  | ✓ |  | 1 |
| **Do cache dependencies where appropriate.** This reduces build times and speeds up CI/CD cycles | Performance |  | ✓ |  |  |  |  | 1 |
| **Do comment complex or non-obvious steps.** Clear explanations help others understand your reasoning | Style |  | ✓ |  |  |  |  | 1 |
| **Do follow YAML best practices.** Consistent formatting reduces confusion and parsing issues | Style |  | ✓ |  |  |  |  | 1 |
| **Do implement failure checks.** Identify failed jobs early to prevent cascading errors | Error Handling |  | ✓ |  |  |  |  | 1 |
| **Do limit permissions for tokens.** Always apply the principle of least privilege to avoid potential security vulnerabilities | Safety |  | ✓ |  |  |  |  | 1 |
| **Do not pin actions to a mutable reference like a branch name (`@main`).** | Safety and Security |  |  |  |  | ✓ |  | 1 |
| **Do not run untrusted code with access to secrets.** Split workflows: one on `pull_request` (no secrets, runs tests), one on merge or label (has secrets, runs deploys) | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not set `cancel-in-progress: true` on deployment or release workflows.** Cancelling mid-deploy leaves systems in inconsistent states | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not use `pull_request_target` unless you have a specific reason, and never check out the PR's code when you do.** It runs with write permissions and secrets against the base repo | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not use self-hosted runners for workflows triggered by public-repo `pull_request` events.** PR code would execute on your infrastructure | Safety |  |  | ✓ |  |  |  | 1 |
| **Do separate concerns with distinct jobs.** This isolates failures and aids debugging | Structure |  | ✓ |  |  |  |  | 1 |
| **Do use `continue-on-error` judiciously.** This prevents critical failures from halting workflows unnecessarily | Error Handling |  | ✓ |  |  |  |  | 1 |
| **Do use matrix builds judiciously.** They can drastically reduce testing time across multiple configurations but may increase resource usage | Performance |  | ✓ |  |  |  |  | 1 |
| **Do use meaningful job names.** Clear job names enhance workflow readability | Structure |  | ✓ |  |  |  |  | 1 |
| **Do validate input parameters.** Ensure the correctness of inputs before proceeding with critical tasks | Safety |  | ✓ |  |  |  |  | 1 |
| **Document exceptions to pinning rules in the workflow file itself.** E.g., `# intentionally unpinned: used to auto-update Python in dev environments only` | Action Selection & Pinning |  |  |  | ✓ |  |  | 1 |
| **Don’t deploy directly from any branch.** Use protected branches to manage releases | Safety |  | ✓ |  |  |  |  | 1 |
| **Don’t hard-code secrets in workflow files.** Always use GitHub secrets to protect sensitive information | Style |  | ✓ |  |  |  |  | 1 |
| **Don’t ignore exit codes from scripts.** Ignoring non-zero exit codes can lead to undetected failures | Error Handling |  | ✓ |  |  |  |  | 1 |
| **Don’t nest conditions unnecessarily.** Simple structures improve clarity and maintainability | Structure |  | ✓ |  |  |  |  | 1 |
| **Don’t run jobs serially unless necessary.** Favor parallel execution to optimize execution time | Performance |  | ✓ |  |  |  |  | 1 |
| **Explicitly declare all events that trigger the workflow.** Use `on:` with a list of events, not `on: [push]` shorthand alone | Triggers & Event Filtering |  |  |  | ✓ |  |  | 1 |
| **Explicitly set `permissions:` at the workflow level.** Use `permissions: read-all` for read-only workflows (CI, linting); use minimal write scopes for workflows that modify state | Secrets & Permissions |  |  |  | ✓ |  |  | 1 |
| **Explicitly set shell to `bash` with `set -e` in all Bash script steps.** Include the preamble: `shell: bash` and `run: \|` with `set -euo pipefail` for multiline scripts | Error Handling & Resilience |  |  |  | ✓ |  |  | 1 |
| **Extract any `run:` block over 20 lines into a checked-in script** under `.github/scripts/` or a repo `scripts/` directory | Structure |  |  | ✓ |  |  |  | 1 |
| **Extract repeated jobs or steps into reusable workflows or composite actions.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Fail fast: use early linting and type checks before slow test suites.** Order jobs so quick checks run first; skip later stages if early ones fail | Performance |  |  |  | ✓ |  |  | 1 |
| **For `pull_request` workflows, explicitly include both `opened` and `synchronize` events if you want them to run on new commits.** Rationale: `synchronize` (new commits pushed) is easy to forget and is required to enforce branch protection rules reliably | Triggers & Event Filtering |  |  |  | ✓ |  |  | 1 |
| **For code coverage, enforce a minimum threshold and fail if coverage drops.** Rationale: prevents incremental erosion of test quality | Testing & Verification |  |  |  | ✓ |  |  | 1 |
| **For complex workflows, add a README in `.github/workflows/README.md` explaining triggers, dependencies, and failure modes.** Rationale: new team members and reviewers have a reference; scales to multiple workflows | Maintainability & Documentation |  |  |  | ✓ |  |  | 1 |
| **For container images, use the smallest base image appropriate for the workload** (e.g., `alpine`, `distroless`) | Performance |  |  |  | ✓ |  |  | 1 |
| **For deployments, use GitHub Environments with required reviewers and/or status checks.** Never auto-deploy to production without human approval | Deployment Safety |  |  |  | ✓ |  |  | 1 |
| **For first-party (organizationally-owned) actions, pin to a major version tag (e.g., `v3`) if the action is stable and well-maintained; otherwise pin to commit hash.** Rationale: balances maintainability (fewer Dependabot PRs) with safety; assumes organizational control and testing discipline | Action Selection & Pinning |  |  |  | ✓ |  |  | 1 |
| **For flaky external dependencies (e.g., API calls, downloads), use explicit retry logic or built-in retry mechanisms.** E.g., `actions/upload-artifact` has `retry-count` | Error Handling & Resilience |  |  |  | ✓ |  |  | 1 |
| **For private or fork-based actions, use deploy keys or GitHub App tokens with minimal scopes, not `GITHUB_TOKEN` directly.** Rationale: limits blast radius if the action is compromised | Action Selection & Pinning |  |  |  | ✓ |  |  | 1 |
| **For pull requests from forks, restrict access to secrets.** E.g., do not pass secrets to actions running on `pull_request` from external contributors; use `pull_request_target` sparingly and with caution, or gate with `github.event.pull_request.head.repo.full_name == github.repository` | Input Validation & Safety |  |  |  | ✓ |  |  | 1 |
| **For sensitive operations (deployments, publishing), use GitHub Environments with required reviewers and deployment branches.** Rationale: adds human-in-the-loop control; enforces audit trail | Secrets & Permissions |  |  |  | ✓ |  |  | 1 |
| **For workflow dispatch (`workflow_dispatch`), define input parameters with descriptions.** Use `type: choice` for enums; avoid free text where constrained options exist | Triggers & Event Filtering |  |  |  | ✓ |  |  | 1 |
| **Give every workflow, job, and step an explicit `name`.** Default names are derived from `run` content and make logs and the Checks UI unreadable | Structure |  |  | ✓ |  |  |  | 1 |
| **Group related steps into few, well-named jobs rather than one monolithic job.** Aim for 3–8 steps per job; if a job exceeds 15 steps, break it into parallel subjobs | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Include a rollback or smoke test step after critical deployments.** Log the previous and new version | Deployment Safety |  |  |  | ✓ |  |  | 1 |
| **Include workflow context in logs: branch, commit, run ID, timestamp.** Rationale: aids correlation and debugging when logs are aggregated | Artifacts & Logging |  |  |  | ✓ |  |  | 1 |
| **Keep individual workflow files focused on a single responsibility.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Log intermediate state generously, especially before risky operations.** E.g., log the commit SHA, branch, environment variables (non-secrets), dependency versions | Error Handling & Resilience |  |  |  | ✓ |  |  | 1 |
| **Never echo secrets, even masked.** `echo "$TOKEN"` with a masked value still leaks length and can leak content if the masker misses a transformation | Safety |  |  | ✓ |  |  |  | 1 |
| **Never hardcode secrets or tokens in the workflow file.** | Safety and Security |  |  |  |  | ✓ |  | 1 |
| **Never interpolate `${{ github.event.* }}`, `${{ github.head_ref }}`, or other user-controlled context directly into `run:` scripts.** Pass them through `env:` and reference as `"$VAR"` | Safety |  |  | ✓ |  |  |  | 1 |
| **Never log, print, or output secrets.** Use `::add-mask::` or GitHub's built-in redaction (e.g., secrets are automatically masked in logs) | Secrets & Permissions |  |  |  | ✓ |  |  | 1 |
| **Never upload secrets, credentials, or sensitive data in artifacts.** Audit artifact contents before uploading | Artifacts & Logging |  |  |  | ✓ |  |  | 1 |
| **Order keys within a job consistently:** `name`, `runs-on`, `needs`, `if`, `permissions`, `timeout-minutes`, `strategy`, `env`, `defaults`, `steps` | Style |  |  | ✓ |  |  |  | 1 |
| **Organize jobs in dependency order, with explicit `needs:` relationships.** Do not rely on implicit ordering or alphabetic sequence | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Pass secrets only to steps and actions that need them.** Do not set secrets as environment variables for entire jobs if only one step uses them | Secrets & Permissions |  |  |  | ✓ |  |  | 1 |
| **Pin actions to a major version tag (e.g., `actions/checkout@v3`).** | Safety and Security |  |  |  |  | ✓ |  | 1 |
| **Pin all third-party actions to a specific commit hash (e.g., `uses: actions/checkout@a81bbbf8298c0fa03ea29cdc473d45aa81f7f7f3`).** Do not use `latest`, `main`, or floating major version tags without documented, narrowly-scoped exceptions | Action Selection & Pinning |  |  |  | ✓ |  |  | 1 |
| **Pin first-party actions (`actions/*`, `github/*`) to a major version tag (`@v4`).** (contested) SHA-pinning every action creates maintenance noise without proportional security benefit inside the GitHub org trust boundary | Safety |  |  | ✓ |  |  |  | 1 |
| **Pin runner images to a specific version (`ubuntu-24.04`) rather than `-latest` for release and deploy workflows.** (contested) `-latest` drift has broken production pipelines; CI can tolerate it, releases cannot | Correctness |  |  | ✓ |  |  |  | 1 |
| **Pin third-party actions (anything not under `actions/`, `github/`, or your own org) to a full 40-character commit SHA.** Tags are mutable; a compromised tag is a supply-chain incident | Safety |  |  | ✓ |  |  |  | 1 |
| **Place one workflow per file and name the file after its purpose** (e.g., `ci.yml`, `release.yml`, `deploy-prod.yml`) | Structure |  |  | ✓ |  |  |  | 1 |
| **Place scripts longer than 10 lines into a separate, executable file.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Prefer GitHub-authored actions (in `actions/` namespace) over third-party equivalents when both exist.** E.g., `actions/checkout`, `actions/cache`, `actions/upload-artifact` | Action Selection & Pinning |  |  |  | ✓ |  |  | 1 |
| **Prefer short-lived credentials (OIDC tokens, temporary AWS credentials) over static secrets.** If using OIDC, trust only your repository and organization (not `actor == 'dependabot'` alone) | Secrets & Permissions |  |  |  | ✓ |  |  | 1 |
| **Put `env:` blocks close to where the variables are used (step-level over job-level over workflow-level) unless the value is genuinely global.** Scoping reduces surprises | Style |  |  | ✓ |  |  |  | 1 |
| **Put production deployment jobs behind a GitHub `environment:` with required reviewers.** Environment protection rules are the only reliable gate on deploy workflows | Secrets & Environments |  |  | ✓ |  |  |  | 1 |
| **Quote all `${{ }}` expressions used as strings in `if:` and `run:` contexts.** Unquoted expressions containing spaces or special characters misparse silently | Correctness |  |  | ✓ |  |  |  | 1 |
| **Reference secrets through `secrets.` or environment-scoped secrets; never hard-code, never read from a file committed to the repo.** Obvious, still violated | Secrets & Environments |  |  | ✓ |  |  |  | 1 |
| **Regularly audit and update action dependencies.** Use Dependabot for GitHub Actions; review and merge version bumps monthly | Maintainability & Documentation |  |  |  | ✓ |  |  | 1 |
| **Run independent jobs in parallel using the matrix strategy, not sequentially.** Rationale: reduces total workflow runtime; better resource utilization | Performance |  |  |  | ✓ |  |  | 1 |
| **Run security scanning (SAST, dependency scanning, container scanning) on every push to main and on pull requests.** Do not gate these behind manual approval | Testing & Verification |  |  |  | ✓ |  |  | 1 |
| **Run tests in a deterministic order, not in random or parallel order, unless the test suite explicitly supports it.** Rationale: ensures reproducibility; makes failures easier to diagnose | Testing & Verification |  |  |  | ✓ |  |  | 1 |
| **Scope triggers as narrowly as possible using `paths` or `types`.** | Performance and Cost |  |  |  |  | ✓ |  | 1 |
| **Scope workflow triggers with `paths:` filters when the workflow only cares about a subset of the repo.** Don't run the docs build on backend-only changes | Performance |  |  | ✓ |  |  |  | 1 |
| **Set `defaults.run.shell: bash` at the workflow level.** Don't rely on runner-default shells; they differ across OSes | Structure |  |  | ✓ |  |  |  | 1 |
| **Set `fail-fast: false` on matrices only when you genuinely want all shards to run.** The default (`true`) saves minutes and surfaces the first failure faster | Performance |  |  | ✓ |  |  |  | 1 |
| **Set `persist-credentials: false` on `actions/checkout` unless the workflow needs to push back to the repo.** The default leaves a usable token on disk for the rest of the job | Safety |  |  | ✓ |  |  |  | 1 |
| **Set `set -euo pipefail` at the top of every multi-line bash `run:` block.** Bash's defaults silently swallow failures in pipelines and unset variables | Correctness |  |  | ✓ |  |  |  | 1 |
| **Set `timeout-minutes` on every job.** The default is 360 minutes; a runaway job is expensive and hides hangs | Correctness |  |  | ✓ |  |  |  | 1 |
| **Set a `concurrency` group with `cancel-in-progress: true` for PR and branch-push workflows.** Prevents queue pile-up when someone force-pushes | Performance |  |  | ✓ |  |  |  | 1 |
| **Set explicit retention for artifacts based on use case.** E.g., 7 days for CI logs, 30 days for release builds, 1 day for pull request artifacts | Artifacts & Logging |  |  |  | ✓ |  |  | 1 |
| **Set explicit timeouts for long-running steps.** E.g., `timeout-minutes: 30` at the job level or per step | Error Handling & Resilience |  |  |  | ✓ |  |  | 1 |
| **Treat all external input (GitHub event context, workflow dispatch inputs, pull request data) as untrusted.** Do not interpolate user input directly into shell commands without quoting | Input Validation & Safety |  |  |  | ✓ |  |  | 1 |
| **Use GitHub Actions expressions (`${{ }}`) for variable substitution, not shell variable expansion, where possible.** Rationale: expressions are evaluated in a safer context; less prone to injection | Input Validation & Safety |  |  |  | ✓ |  |  | 1 |
| **Use OIDC (`id-token: write` + cloud-provider federated credentials) instead of long-lived cloud access keys where the provider supports it.** Static keys in secrets are the largest blast-radius credential you own | Secrets & Environments |  |  | ✓ |  |  |  | 1 |
| **Use `actions/cache` to cache build artifacts, dependencies, and container images.** Key cache paths by dependency file content hash (e.g., `package-lock.json`, `go.sum`) | Performance |  |  |  | ✓ |  |  | 1 |
| **Use `concurrency` groups for deployment jobs.** | Performance and Cost |  |  |  |  | ✓ |  | 1 |
| **Use `continue-on-error: true` only for non-blocking checks** (e.g., code style, optional linting) | Error Handling & Resilience |  |  |  | ✓ |  |  | 1 |
| **Use `env:` at the job level, not global, for job-specific configuration.** Keep top-level `env:` for truly universal settings | Maintainability & Documentation |  |  |  | ✓ |  |  | 1 |
| **Use `if: failure()` to add cleanup or rollback steps, not `continue-on-error` as a band-aid.** Rationale: explicit error recovery is clearer than suppressing errors; documents intent | Error Handling & Resilience |  |  |  | ✓ |  |  | 1 |
| **Use `name` attributes for workflows, jobs, and steps.** | Structure and Style |  |  |  |  | ✓ |  | 1 |
| **Use `secrets` context (`${{ secrets.MY_SECRET }}`) to pass credentials.** | Safety and Security |  |  |  |  | ✓ |  | 1 |
| **Use `shell: bash {0}` at the job or workflow level to enforce fail-fast behavior.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Use `shellcheck` to validate all non-trivial shell scripts.** | Correctness and Error Handling |  |  |  |  | ✓ |  | 1 |
| **Use a Concurrency key for workflows that should not run in parallel.** E.g., deployments to the same environment | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Use a deployment tracking system (e.g., GitHub Deployments API, manual logs) to track what was deployed where and when.** Rationale: enables quick rollback identification and audit compliance | Deployment Safety |  |  |  | ✓ |  |  | 1 |
| **Use branch and path filters to avoid redundant runs.** E.g., don't run the full CI suite on every `push` to documentation files | Triggers & Event Filtering |  |  |  | ✓ |  |  | 1 |
| **Use descriptive `name:` fields for all jobs and steps.** Avoid generic names like "Run tests"; use "Run unit tests (Python 3.9)" or "Build Docker image for staging" | Maintainability & Documentation |  |  |  | ✓ |  |  | 1 |
| **Use explicit `if:` conditions with `always()` or `needs.<job>.result` when a job should run after a failure.** `if: failure()` alone is brittle across `needs:` chains | Correctness |  |  | ✓ |  |  |  | 1 |
| **Use lowercase kebab-case for job IDs and step IDs** (`build-and-test`, not `BuildAndTest`) | Style |  |  | ✓ |  |  |  | 1 |
| **Use matrix strategies to test across different versions or platforms.** | Performance and Cost |  |  |  |  | ✓ |  | 1 |
| **Use reusable workflows (`workflow_call`) for whole-job reuse and composite actions for step sequences.** Don't copy-paste identical job bodies across files | Structure |  |  | ✓ |  |  |  | 1 |
| **Use semantic names for workflows and jobs.** Name workflows by their high-level purpose (e.g., `ci.yml`, `deploy-staging.yml`), not `build.yml` or `test.yml` if there are multiple testing phases | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Use structured logging (JSON, key=value) for programmatic log analysis.** Rationale: enables log aggregation tools and automated alerting | Artifacts & Logging |  |  |  | ✓ |  |  | 1 |
| **Use the caching built into `setup-node`, `setup-python`, `setup-java`, etc., rather than hand-rolling `actions/cache`.** The built-in keys are correct; hand-rolled ones frequently cache-miss or cache-poison | Performance |  |  | ✓ |  |  |  | 1 |
| **Use top-level environment variables for shared, non-sensitive configuration.** Define once at the workflow root, inherit in all jobs | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Vet all third-party actions before use.** | Safety and Security |  |  |  |  | ✓ |  | 1 |
| Add step-security/harden-runner as the first step of every job (audit or block) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid running the same heavy job on both push and pull_request to the same branch | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare top-level permissions with least privilege (read-all or equivalent) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define a workflow-level concurrency group that includes workflow and ref, with cancel-in-progress: true | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define env at the narrowest scope; don’t put secrets in workflow-level env | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t reference secrets in workflows triggered by pull_request | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t store secrets in artifacts or cache | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t use @main, @master, or floating ranges (e.g., @v3.1.x) for actions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t use Docker latest tags or omit image tags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t use continue-on-error except for explicitly allowed failures | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t use deprecated workflow commands (::set-output, ::add-path, ::set-env) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t use pull_request_target for untrusted PRs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For self-hosted, use specific labels beyond self-hosted and target them explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Gate costly jobs with paths filters or conditional if: | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Give steps descriptive names; avoid generic “Run script” labels | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Grant job-level write permissions only where strictly required | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If you use actions/cache, include a lockfile hash in the key (e.g., hashFiles('**/package-lock.json')) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep artifacts small; compress and avoid redundant contents | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep run steps short; prefer scripts checked into the repo for complex logic | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep workflows single-purpose; split unrelated concerns into separate files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name artifacts clearly and set retention-days to the minimum needed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name every workflow and every job explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never echo secrets or enable set -x in steps that use secrets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin Ubuntu runner by major version (e.g., ubuntu-22.04) instead of ubuntu-latest for critical workflows (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin third-party actions by full commit SHA; pin GitHub-owned actions by major version or SHA (contested) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer GitHub-hosted runners unless you need privileged workloads or custom hardware | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer pull_request for CI and reserve push for release branches/tags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer reusable workflows (workflow_call) for shared logic | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Randomize scheduled cron minutes; do not run at minute 0 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Remove add-path and set-env; use PATH via $GITHUB_PATH and env via $GITHUB_ENV | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Remove set-output; write to $GITHUB_OUTPUT | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope triggers with paths/paths-ignore for heavy workflows | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set defaults.run.shell: bash | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set explicit fetch-depth in actions/checkout; use 1 unless full history is required | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set timeout-minutes on every job | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use actions/checkout@v4 (or SHA) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use protected environments with required reviewers for deployments | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use strict Bash in multi-line run steps: set -euo pipefail | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

