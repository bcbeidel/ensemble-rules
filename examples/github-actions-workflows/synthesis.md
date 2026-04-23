# Synthesis of GitHub Actions Workflow Best Practices

## 1. Consensus Rules

### Structure & Naming

- **Give every workflow, job, and (multi-line) step an explicit `name`.** Named entities make logs, the Checks UI, and required-check configuration readable. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)*
- **Keep workflows single-purpose; split unrelated concerns into separate files.** Smaller DAGs are easier to reason about, debug, and modify. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Extract shared logic into reusable workflows (`workflow_call`) or composite actions.** Reduces duplication and drift across pipelines. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Extract non-trivial inline scripts (≳10–20 lines) into checked-in script files.** Enables shellcheck, testing, and review; YAML is a poor place for real code. *(substantively similar across GPT-5, Claude Opus, Gemini)*

### Triggers

- **Scope triggers with `paths`, `branches`, and `types` filters.** Avoids duplicate runs and wasted minutes on irrelevant changes. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Avoid `pull_request_target` for untrusted PRs; never check out PR code when using it.** This trigger runs with write permissions and secrets and is the vector behind most Actions CVEs. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Safety & Permissions

- **Declare top-level `permissions:` with least privilege; elevate per-job only when needed.** The default `GITHUB_TOKEN` scope is too broad. *(near-identical phrasing across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok — strong convergence, likely shared source material)*
- **Never hardcode or echo secrets; reference only via the `secrets` context.** Prevents credential leakage in logs, artifacts, and source. *(near-identical across all six models)*
- **Do not expose secrets to workflows triggered by untrusted forks.** Fork PRs can't safely receive secrets; split workflows or gate on PR source. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Gate production deployments behind GitHub Environments with required reviewers.** Environment protection rules are the only reliable human gate on deploys. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Dependency Pinning

- **Pin third-party actions to a full 40-character commit SHA.** Tags are mutable; a compromised tag is a supply-chain incident. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Pin first-party (`actions/*`, `github/*`) actions to at least a major version tag (`@v4`).** Balances safety inside the GitHub trust boundary against maintenance churn. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)* — explicitly marked contested by GPT-5 and Claude Opus.
- **Do not use `@main`, `@master`, or floating tags for actions.** Mutable refs are unreproducible and unsafe. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

### Correctness & Error Handling

- **Set `timeout-minutes` on every job.** The default 360 minutes silently burns compute on hung jobs. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Use strict Bash (`set -euo pipefail`) at the top of every multi-line `run:` block.** Bash defaults silently swallow pipeline failures and unset variables. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Set `defaults.run.shell: bash` at the workflow level.** Avoids OS-dependent shell surprises. *(substantively similar across GPT-5, Claude Opus)*
- **Use `continue-on-error` sparingly and only for explicitly non-blocking steps.** Silent failures erode trust in CI. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)* — marked contested by several.

### Performance & Concurrency

- **Cache dependencies, keyed by a lockfile hash.** Lockfile-based keys produce correct, stable caches that actually hit. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)*
- **Define a `concurrency` group with `cancel-in-progress: true` for PR and branch-push workflows.** Prevents queue pile-up from force-pushes and superseded runs. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Do not cancel in-progress runs for deploy/release workflows.** Cancelling mid-deploy leaves systems inconsistent. *(raised by Claude Opus, echoed in spirit by GPT-5's concurrency discussion)* — kept as consensus because it's the necessary corollary of the concurrency rule.

### Injection & Input Safety

- **Never interpolate `${{ github.event.* }}`, `github.head_ref`, or similar attacker-controlled context directly into `run:` scripts; pass through `env:`.** Direct interpolation is script injection and is actively exploited. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Deprecated Commands

- **Do not use deprecated workflow commands (`::set-output`, `::set-env`, `::add-path`).** Use `$GITHUB_OUTPUT`, `$GITHUB_ENV`, `$GITHUB_PATH`. *(raised by GPT-5 only in rule form but implied by Claude Opus/Gemini via "avoid deprecated patterns")* — kept as consensus on substantive alignment.

---

## 2. Strong Minority Rules

- **Add `step-security/harden-runner` as the first step of every job.** *(GPT-5 only.)* Provides egress auditing/blocking, a concrete defense-in-depth measure that's cheap to adopt. Kept because it's a real, auditable control, not generic advice.
- **Set `persist-credentials: false` on `actions/checkout` unless the workflow needs to push back.** *(Claude Opus only.)* The checkout default leaves a usable token on disk for the job's lifetime; this is a specific, frequently-overlooked hardening step.
- **Randomize scheduled cron minutes; avoid minute 0.** *(GPT-5 only.)* Real operational lesson — top-of-hour scheduling causes runner contention and rate-limit storms.
- **Do not use self-hosted runners for public-repo `pull_request` workflows.** *(Claude Opus only.)* PR code would execute on your infrastructure; a severe, commonly-missed vulnerability.
- **Prefer OIDC (federated cloud credentials) over long-lived static cloud secrets.** *(Claude Opus, Claude Haiku.)* Substantially reduces blast radius of leaked credentials; worth elevating despite partial coverage.
- **Pin runner images to a specific version (`ubuntu-24.04`) for release/deploy workflows.** *(GPT-5, Claude Opus.)* Explicitly contested — CI can tolerate `-latest` drift, deploys generally cannot.
- **Configure Dependabot for the `github-actions` ecosystem.** *(Claude Haiku only.)* Operationalizes the SHA-pinning rule; without it, pinned SHAs silently accumulate vulnerabilities.
- **Set explicit `fetch-depth` on `actions/checkout` (usually `1`).** *(GPT-5 only.)* Small but real performance win, and makes history-dependent workflows fail loudly instead of silently.

---

## 3. Divergences

### Action pinning granularity

- **Positions:** GPT-5, Claude Opus, Claude Haiku, Gemini, Grok all prescribe SHA-pinning for third-party actions. Gemini and Grok accept major-tag pinning (`@v3`) as a pragmatic default even for third-party; Claude Opus and Claude Haiku explicitly split first-party vs third-party (tag vs SHA). GPT-5 flags the whole question as contested.
- **Recommendation:** SHA-pin third-party; tag-pin first-party (`actions/*`, `github/*`). This is the majority view, balances security and maintenance realistically, and depends on a clear trust boundary. Pair with Dependabot so SHAs don't rot.

### Runner pinning (`ubuntu-latest` vs `ubuntu-22.04`)

- **Positions:** GPT-5 and Claude Opus recommend pinning for release/deploy workflows but accept `-latest` for general CI, explicitly contested. Other models don't raise it.
- **Recommendation:** Adopt the differentiated rule — pin release/deploy runners; tolerate `-latest` for CI. The failure mode (deploy pipeline breaking on image rollover) is real.

### One large workflow vs many small workflows

- **Positions:** Gemini and Grok explicitly recommend "single workflow per major process" or even "single workflow file per concern." Claude Opus recommends "one workflow per file named after purpose." GPT-4o-mini notes reasonable disagreement. No model defends monolithic workflows.
- **Recommendation:** Prefer focused, single-purpose workflows. The disagreement is really about granularity within that principle, not the principle itself.

### `continue-on-error`

- **Positions:** All models distrust it. Claude Haiku, GPT-5, Gemini suggest it's acceptable only for explicitly non-blocking steps. Grok permits it more readily. GPT-4o-mini is ambivalent.
- **Recommendation:** Allow only for clearly-labeled non-critical steps (e.g., coverage uploads, optional linters). Never for tests, builds, deploys, or security checks. Require an inline comment justifying use.

### Coverage of deprecated workflow commands

- **Positions:** Only GPT-5 raises `::set-output`, `::set-env`, `::add-path` explicitly. Others omit. No model defends their use.
- **Recommendation:** Include as consensus — the silence from other models reads as "assumed obvious," not disagreement.

### Matrix strategy

- **Positions:** Claude Haiku and Grok treat aggressive matrices as a maintainability concern. Gemini and GPT-4o-mini recommend them for parallelization. Claude Opus notes matrices are "cheap to add, expensive to remove."
- **Recommendation:** Use matrices, but start small and set `fail-fast` explicitly. Past 2–3 dimensions, readability suffers.

---

## 4. Notable Omissions

- **GPT-4o-mini omits** nearly all safety-critical rules the other five models converged on: SHA pinning, `pull_request_target` warnings, script injection via `github.event.*`, explicit `permissions:`, environments for deploys, and concurrency. The response reads as generic CI advice rather than Actions-specific; treat it as low-signal for this domain.
- **Grok omits** the script-injection rule around `${{ github.event.* }}` in `run:` blocks — a top-tier Actions security concern that five of six models raised.
- **Gemini omits** explicit timeout rules (`timeout-minutes`) and workflow-level concurrency groups. Both are near-universal elsewhere.
- **Claude Haiku omits** `defaults.run.shell: bash` and the specific `pull_request_target` danger (covers fork-PR secret exposure instead).
- **GPT-5 omits** OIDC for cloud credentials and Dependabot for action updates. Both are operational mainstays raised by the Claude models.
- **Grok and GPT-4o-mini omit** the strict-Bash (`set -euo pipefail`) rule — a correctness staple the rest converge on.
- **Grok and GPT-4o-mini omit** concurrency groups entirely.

---

## 5. Shared Deterministic Checks

### Converged checks

- **Check** — Every workflow, job, and (optionally) step has a non-empty `name` field.
  - **Signal** — Parsed YAML AST.
  - **Tool candidate** — `actionlint` (partial); otherwise ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, GPT-4o-mini, Grok.
  - **Variance** — Models differ on step-level strictness: some require `name` only on `run:` steps (letting `uses:` steps go nameless), others require it universally. Grok additionally enforces kebab-case on identifiers.

- **Check** — `uses:` references for third-party actions resolve to a 40-char hex SHA; first-party (`actions/*`, `github/*`) may use `@vN`; mutable refs (`@main`, `@master`, semver wildcards) are rejected.
  - **Signal** — Parsed YAML; `uses:` string.
  - **Tool candidate** — `zizmor` (`unpinned-uses`), `actionlint` (partial).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — First-party allowlist varies (some include the repo's own org). Claude Haiku requires a documentation comment next to non-SHA refs; others don't.

- **Check** — A top-level `permissions:` block exists and is not `write-all`.
  - **Signal** — Parsed YAML root.
  - **Tool candidate** — `zizmor` (`excessive-permissions`); `actionlint` partial.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — GPT-5 additionally requires all values be `read`/`none`; others only require presence. None can verify "actually minimum."

- **Check** — No hardcoded secret-looking values in workflow source.
  - **Signal** — Raw file text.
  - **Tool candidate** — `gitleaks` or `trufflehog`.
  - **Raised by** — Claude Opus, Claude Haiku, Gemini, GPT-4o-mini, Grok.
  - **Variance** — All describe equivalent entropy/regex scanning; agreement on substance.

- **Check** — Every job declares `timeout-minutes` as a positive integer.
  - **Signal** — Parsed YAML, per job.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Claude Opus suggests a configurable ceiling (e.g., 60); GPT-5 accepts any positive integer.

- **Check** — Multi-line bash `run:` blocks begin with `set -euo pipefail` (or equivalent).
  - **Signal** — Raw text of `run:` string where effective shell is bash.
  - **Tool candidate** — ad-hoc; pairs with `shellcheck` on the extracted script.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Threshold for "multi-line" differs (Claude Opus: >1 non-blank line; GPT-5: any newline). All accept variants like `-euxo pipefail`.

- **Check** — `pull_request_target` triggers are flagged; when present, `actions/checkout` with `ref: ${{ github.event.pull_request.head.* }}` is a hard violation.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — `zizmor` (`dangerous-triggers`).
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — GPT-5 flags any `pull_request_target` use; Claude Opus warns but only hard-fails on the dangerous combination.

- **Check** — No `${{ github.event.* }}`, `github.head_ref`, `inputs.*`, or similar user-controlled expressions interpolated directly into `run:` block text.
  - **Signal** — Raw text of each `run:` string.
  - **Tool candidate** — `zizmor` (`template-injection`), `actionlint` partial.
  - **Raised by** — Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Allowlist of safe contexts (`github.sha`, `github.run_id`) varies.

- **Check** — Workflow-level `concurrency.group` is defined and includes `github.workflow` + `github.ref` for PR/push workflows; `cancel-in-progress: true`.
  - **Signal** — Parsed YAML root.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Claude Opus excludes deploy/release workflows from the `cancel-in-progress` requirement; GPT-5 enforces workflow-level uniformly.

- **Check** — `uses: actions/cache@*` entries have a `with.key` containing `hashFiles(...)`.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Haiku, Grok, GPT-4o-mini.
  - **Variance** — Claude Haiku checks inferentially (install-step present but no cache step); GPT-5 checks structural correctness of the key.

- **Check** — No `::set-output`, `::set-env`, or `::add-path` strings appear in any `run:` block.
  - **Signal** — Raw source text.
  - **Tool candidate** — `actionlint` (deprecated-commands).
  - **Raised by** — GPT-5.
  - **Variance** — Single-model but well-specified.

- **Check** — YAML is syntactically valid and passes style linting.
  - **Signal** — Raw file text.
  - **Tool candidate** — `yamllint`, `actionlint`.
  - **Raised by** — Gemini, GPT-4o-mini, Grok.
  - **Variance** — Grok additionally enforces four-space indentation and kebab-case identifiers; others accept any consistent style.

### Singleton checks worth keeping

- **Check** — `step-security/harden-runner` is the first step of every job, with `mode: audit` or `mode: block`.
  - **Signal** — Parsed YAML; `jobs.*.steps[0]`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Scheduled cron expressions do not use minute `0` (or `00`).
  - **Signal** — Parsed YAML; `on.schedule[*].cron`.
  - **Tool candidate** — ad-hoc (any cron parser).
  - **Raised by** — GPT-5.

- **Check** — `actions/checkout` steps specify `with.persist-credentials: false` unless the job contains a subsequent `git push` or push-shaped action.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — In public repos, `pull_request` workflows do not use self-hosted runners.
  - **Signal** — Parsed YAML + repo visibility from GitHub API.
  - **Tool candidate** — `zizmor` (`self-hosted-runner`).
  - **Raised by** — Claude Opus.

- **Check** — `actions/checkout` has an explicit `with.fetch-depth`.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — `actions/upload-artifact` steps specify both `name` and `retention-days`.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Haiku.

- **Check** — Release/deploy workflows (classified by filename like `deploy*.yml`, `release*.yml`, or explicit tag) don't use `*-latest` runner images.
  - **Signal** — Parsed YAML + filename.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus.

- **Check** — Jobs classified as deployments reference an `environment:` key.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.

- **Check** — Extracted `run:` scripts pass `shellcheck` (at least SC2086, SC2154).
  - **Signal** — `run:` string content piped to `shellcheck`.
  - **Tool candidate** — `shellcheck`.
  - **Raised by** — Gemini.

- **Check** — Job IDs and step IDs match `^[a-z][a-z0-9-]*$` (kebab-case).
  - **Signal** — Parsed YAML keys.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Grok.

- **Check** — Docker image references (`uses: docker://...`, `jobs.*.container.image`) include an explicit non-`latest` tag or `@sha256:` digest.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Top-level `env:` does not contain any `${{ secrets.* }}` references.
  - **Signal** — Parsed YAML root.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Workflows triggered by `pull_request` do not reference `${{ secrets.* }}` without a source-gating `if:` condition.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Haiku.

- **Check** — No YAML anchors (`&foo`, `*foo`) in non-string positions.
  - **Signal** — Raw file text or AST.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — `run:` blocks longer than ~20 non-blank lines are flagged for extraction.
  - **Signal** — Line count of `run:` string.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

---

## 6. Final Rules File

# GitHub Actions Workflow Rules

**Scope:** YAML files under `.github/workflows/` and composite actions under `.github/actions/`. Applies to workflows on both GitHub-hosted and self-hosted runners; public-repo rules are stricter where noted.

**Audience:** Engineers authoring or reviewing workflow changes; AI assistants generating workflow YAML.

**Goal:** Safe-by-default, predictable, fast, maintainable pipelines.

---

## Structure & Naming

- **Give every workflow, every job, and every multi-line `run:` step an explicit `name`.** Named entities make the Checks UI, logs, and required-check configuration legible.
- **Keep workflows single-purpose and name the file after its intent** (`ci.yml`, `release.yml`, `deploy-prod.yml`). Omnibus workflows are harder to reason about, debug, and modify.
- **Extract shared logic into reusable workflows (`workflow_call`) for whole-job reuse, or composite actions for step sequences.** Don't copy-paste job bodies across files.
- **Extract any `run:` block longer than ~20 lines into a checked-in script** under `.github/scripts/` or `scripts/`. Inline YAML is a poor place for real code; scripts can be shellchecked and tested.
- **Use lowercase kebab-case for job IDs and step IDs** (`build-and-test`, not `BuildAndTest`). Job IDs appear in URLs and required-check names.
- **Avoid YAML anchors (`&`, `*`) in workflows.** Supported but hurt readability and aren't uniform across all contexts.
- **Scope `env:` blocks to the narrowest level possible** (step > job > workflow). Reduces surprise and blast radius.

## Triggers

- **Scope triggers with `paths`, `branches`, and `types` filters.** Don't run the full CI suite on docs-only changes; don't run on tags you didn't mean to.
- **Do not use `pull_request_target` for untrusted PRs,** and **never check out PR code (`ref: github.event.pull_request.head.*`) when you do.** This trigger runs with write permissions and secrets against the base repo and is the vector behind most Actions CVEs.
- **Randomize scheduled cron minutes; do not run at minute 0.** Avoids thundering-herd contention on GitHub's runner pool and upstream rate limits.
- **Scope `workflow_dispatch` inputs with `type: choice` where possible** and document each input. Self-documents the workflow and prevents misuse.

## Safety & Permissions

- **Declare `permissions:` at the workflow level with minimum scopes** (start from `contents: read`); elevate per-job only where needed. The default `GITHUB_TOKEN` is too broad.
- **Never interpolate user-controlled context (`${{ github.event.* }}`, `github.head_ref`, `github.ref_name`, `inputs.*`) directly into `run:` scripts.** Pass through `env:` and reference as `"$VAR"`. Direct interpolation is script injection and is actively exploited.
- **Never echo secrets or enable `set -x` in steps that use them.** Masking catches known values, not transformations; length leaks still reveal structure.
- **Do not reference `${{ secrets.* }}` in workflows triggered by `pull_request` from forks,** or gate on `github.event.pull_request.head.repo.full_name == github.repository`. Fork PRs can't safely receive secrets.
- **Split workflows by trust level:** one on `pull_request` (no secrets, runs tests), one on merge or label (has secrets, runs deploys).
- **Do not store secrets in workflow-level `env:`, artifacts, or caches.** All of those have wider access than the step that needs them.
- **Set `persist-credentials: false` on `actions/checkout`** unless the workflow needs to push back. The default leaves a usable token on disk for the rest of the job.
- **Do not use self-hosted runners for `pull_request` workflows on public repositories.** PR code would execute on your infrastructure.
- **Add `step-security/harden-runner` as the first step of every job** (audit mode at minimum). Provides egress auditing and supply-chain tamper detection.
- **Gate production deployments behind a GitHub `environment:` with required reviewers.** Environment protection rules are the only reliable human gate on deploys.
- **Prefer OIDC-based federated credentials (`id-token: write`) over long-lived static cloud access keys** where the provider supports it. Static keys are the largest-blast-radius credentials most teams hold.

## Dependency Pinning

- **Pin third-party actions (anything outside `actions/`, `github/`, or your own org) to a full 40-character commit SHA.** Tags are mutable; a compromised tag is a supply-chain incident.
- **Pin first-party actions (`actions/*`, `github/*`) to a major version tag (`@v4`).** *(contested)* SHA-pinning inside the GitHub trust boundary creates maintenance noise without proportional security benefit.
- **Do not use `@main`, `@master`, or floating semver wildcards (`@v3.1.x`) for any action.** Unreproducible and unsafe.
- **Do not use Docker `:latest` or untagged images.** Use explicit tags or `@sha256:` digests.
- **Configure Dependabot (`.github/dependabot.yml`) for the `github-actions` ecosystem.** Without it, pinned SHAs silently rot and accumulate vulnerabilities.

## Runners

- **Pin runner images (`ubuntu-24.04`, not `ubuntu-latest`) for release and deploy workflows.** *(contested)* Image drift has broken production pipelines; CI can tolerate `-latest`, releases should not.
- **For self-hosted runners, require a specific label beyond `self-hosted`** and target it explicitly. Protects against wrong-machine selection.

## Correctness & Error Handling

- **Set `timeout-minutes` on every job** (60 is a reasonable default ceiling). The runner default is 360 minutes; runaway jobs are expensive and hide hangs.
- **Set `defaults.run.shell: bash` at the workflow level.** Avoids OS-dependent shell differences.
- **Start every multi-line bash `run:` block with `set -euo pipefail`.** Bash's defaults silently swallow pipeline failures and unset variables.
- **Do not use deprecated workflow commands** (`::set-output`, `::set-env`, `::add-path`). Use `$GITHUB_OUTPUT`, `$GITHUB_ENV`, `$GITHUB_PATH`.
- **Use `continue-on-error: true` only for explicitly non-blocking steps** (optional linters, coverage uploads). Never for tests, builds, deploys, or security checks. Add a comment justifying each use.
- **When a job should run after failure, use explicit `if:` conditions** (`if: always() && needs.x.result == 'failure'`). `if: failure()` alone is brittle across `needs:` chains.
- **Quote all `${{ }}` expressions used as strings in `if:` and `run:` contexts.** Unquoted expressions containing spaces or special characters misparse silently.
- **Declare explicit `needs:` dependencies between jobs.** Prevents race conditions and makes the DAG legible.
- **Set `fail-fast: false` on matrices only when you genuinely want all shards to run.** The default saves minutes and surfaces the first failure faster.

## Performance & Concurrency

- **Define a workflow-level `concurrency` group including `github.workflow` and `github.ref`, with `cancel-in-progress: true`** for PR and branch-push workflows. Prevents queue pile-up on force-pushes.
- **Do not set `cancel-in-progress: true` on deployment or release workflows.** Cancelling mid-deploy leaves systems inconsistent.
- **Cache dependencies keyed by a lockfile hash** (`hashFiles('**/package-lock.json')`). Prefer the caching built into `setup-node`, `setup-python`, `setup-java`; their keys are correct by default.
- **Set explicit `fetch-depth` on `actions/checkout`** (use `1` unless full history is required). Shallow clones are faster and cheaper.
- **Gate costly jobs with `paths:` filters or conditional `if:`.** Skip what you can.

## Artifacts & Logs

- **Set `name` and `retention-days` explicitly on every `actions/upload-artifact`.** The default 90-day retention is often too long.
- **Never upload secrets, credentials, or sensitive logs as artifacts.** Audit artifact contents before uploading.
- **Log workflow context (branch, commit SHA, run ID) near the start of each job.** Dramatically aids post-mortem debugging.

## Style & Review

- **Comment the *why*, not the *what*.** YAML describes what it does; comments explain non-obvious intent — especially in complex `if:` expressions.
- **Order keys within a job consistently:** `name`, `runs-on`, `needs`, `if`, `permissions`, `timeout-minutes`, `strategy`, `env`, `defaults`, `steps`.

---

## Appendix: Deterministic Checks

The following rules in this file admit mechanical verification. Recommended tooling: [`actionlint`](https://github.com/rhysd/actionlint), [`zizmor`](https://github.com/woodruffw/zizmor), [`shellcheck`](https://www.shellcheck.net/), [`yamllint`](https://github.com/adrienverge/yamllint), and secret scanners (`gitleaks`, `trufflehog`).

- Presence of `name` at workflow, job, and step level
- `uses:` refs: SHA-pinned for third-party, `@vN` or SHA for first-party, no `@main`/`@master`/wildcard
- Top-level `permissions:` present and not `write-all`
- No hardcoded secrets (entropy/regex scan)
- Every job has `timeout-minutes`
- Multi-line bash `run:` blocks start with `set -euo pipefail`
- `pull_request_target` + checkout of PR ref combination
- User-controlled expressions interpolated into `run:` text
- Workflow-level `concurrency.group` with `github.workflow` + `github.ref` + `cancel-in-progress: true` (excluding deploy workflows)
- `actions/cache` `with.key` includes `hashFiles(...)`
- No `::set-output` / `::set-env` / `::add-path` in any `run:` block
- `actions/checkout` has `persist-credentials: false` (unless pushing) and explicit `fetch-depth`
- `actions/upload-artifact` has `name` and `retention-days`
- Docker images specify a non-`latest` tag or `@sha256:` digest
- Deployment jobs reference an `environment:` key
- Public-repo `pull_request` workflows use only GitHub-hosted runners
- Job/step IDs match `^[a-z][a-z0-9-]*$`
- YAML passes `yamllint`; workflow passes `actionlint`
- `shellcheck` passes on extracted `run:` script content