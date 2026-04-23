## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Give every workflow, job, and step an explicit name. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Pin third-party actions to immutable references (SHA or version), not floating refs like @main/@master. | Safety | ✓ | | ✓ | ✓ | ✓ | ✓ | 5 |
| Declare top-level permissions with least privilege. | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | | 5 |
| Cache dependencies to speed up workflows. | Performance | ✓ | ✓ | | ✓ | ✓ | ✓ | 5 |
| Never hardcode secrets; use the secrets context. | Safety | | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| Use strict bash (set -euo pipefail) in multi-line run steps. | Correctness | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Extract reusable logic into reusable workflows / composite actions to avoid duplication. | Maintainability | ✓ | | ✓ | | ✓ | ✓ | 4 |
| Use continue-on-error sparingly, only for non-critical steps. | Error Handling | ✓ | ✓ | | ✓ | ✓ | | 4 |
| Scope triggers narrowly with paths/branches filters. | Performance | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Set timeout-minutes on jobs to prevent runaway runs. | Correctness | ✓ | | ✓ | ✓ | | | 3 |
| Use a concurrency group (with cancel-in-progress) for PR/branch workflows. | Performance | ✓ | | ✓ | ✓ | | | 3 |
| Avoid pull_request_target (or use with extreme care) to prevent privilege escalation from forks. | Safety | ✓ | | ✓ | ✓ | ✓ | | 3 |
| Do not log or echo secrets. | Safety | ✓ | | ✓ | ✓ | | | 3 |
| Restrict secret access for PRs from forks. | Safety | ✓ | | ✓ | ✓ | | | 3 |
| Extract long inline run scripts into checked-in script files. | Structure | ✓ | | ✓ | | ✓ | ✓ | 4 |
| Set defaults.run.shell to bash at the workflow level. | Structure | ✓ | | ✓ | | ✓ | | 3 |
| Pin runner images to a specific version rather than *-latest. | Correctness | ✓ | | ✓ | | | | 2 |
| Use GitHub Environments with required reviewers for production deployments. | Safety | ✓ | | ✓ | ✓ | | | 3 |
| Set explicit retention-days on uploaded artifacts. | Artifacts | ✓ | | | ✓ | | | 2 |
| Avoid Docker latest tags; pin container images. | Safety | ✓ | | | | | | 1 |
| Don't use deprecated workflow commands (::set-output, ::add-path, ::set-env). | Deprecated | ✓ | | | | | | 1 |
| Include lockfile hash in actions/cache keys. | Performance | ✓ | | | | | | 1 |
| Set explicit fetch-depth on actions/checkout. | Performance | ✓ | | | | | | 1 |
| Randomize scheduled cron minutes; don't run at minute 0. | Triggers | ✓ | | | | | | 1 |
| Add harden-runner as the first step of every job. | Safety | ✓ | | | | | | 1 |
| For self-hosted runners, require specific labels beyond "self-hosted". | Runners | ✓ | | | | | | 1 |
| Prefer pull_request over push for CI to avoid duplicate runs. | Triggers | ✓ | | | | | | 1 |
| Define env at the narrowest scope; avoid secrets in workflow-level env. | Structure | ✓ | | ✓ | ✓ | | | 3 |
| Do not use self-hosted runners for PR workflows on public repos. | Safety | | | ✓ | | | ✓ | 2 |
| Set persist-credentials: false on actions/checkout unless pushing. | Safety | | | ✓ | | | | 1 |
| Avoid YAML anchors in workflows. | Style | | | ✓ | | | | 1 |
| Use lowercase kebab-case for job/step IDs. | Style | | | ✓ | | | ✓ | 2 |
| Never interpolate user-controlled github.event.* directly into run scripts (script injection). | Safety | | | ✓ | ✓ | | | 2 |
| Prefer OIDC / short-lived credentials over static cloud secrets. | Safety | | | ✓ | ✓ | | | 2 |
| Use explicit if: conditions (e.g., always()/needs.*.result) for post-failure jobs. | Error Handling | | | ✓ | ✓ | ✓ | ✓ | 4 |
| Quote ${{ }} expressions used as strings. | Correctness | | | ✓ | | | | 1 |
| Keep env blocks close to where they are used (narrowest scope). | Style | | | ✓ | ✓ | | | 2 |
| Order keys within a job consistently. | Style | | | ✓ | | | | 1 |
| Prefer GitHub-authored/first-party actions over third-party where available. | Safety | | | | ✓ | | | 1 |
| Use Dependabot / regularly audit action dependencies. | Maintainability | | | | ✓ | | | 1 |
| Document exceptions to pinning rules inline. | Safety | | | | ✓ | | | 1 |
| For workflow_dispatch, define typed inputs with descriptions. | Triggers | | | | ✓ | | | 1 |
| Include both opened and synchronize for pull_request workflows. | Triggers | | | | ✓ | | | 1 |
| Run independent jobs in parallel / use matrix strategies. | Performance | | ✓ | | ✓ | ✓ | ✓ | 4 |
| Fail fast: run quick checks before slow ones. | Performance | | | | ✓ | | | 1 |
| Prefer small base container images. | Performance | | | | ✓ | | | 1 |
| Use deterministic test ordering. | Testing | | | | ✓ | | | 1 |
| Enforce a minimum code coverage threshold. | Testing | | | | ✓ | | | 1 |
| Run security scanning on push/PR. | Testing | | | | ✓ | | | 1 |
| Capture/upload test reports as artifacts. | Artifacts | | | | ✓ | | | 1 |
| Never upload secrets/sensitive data in artifacts. | Artifacts | | | | ✓ | | | 1 |
| Use structured logging and include workflow context. | Artifacts | | | | ✓ | | | 1 |
| Include a rollback or smoke test step after critical deployments. | Deployment | | | | ✓ | | | 1 |
| Use a deployment tracking system (Deployments API). | Deployment | | | | ✓ | | | 1 |
| Add comments explaining non-obvious conditional logic / decisions. | Maintainability | | ✓ | | ✓ | ✓ | ✓ | 4 |
| Maintain a workflows README / changelog for complex workflows. | Maintainability | | | | ✓ | | ✓ | 2 |
| Add retry logic for flaky external dependencies. | Error Handling | | | | ✓ | | | 1 |
| Log intermediate state / context generously before risky operations. | Error Handling | | | | ✓ | | | 1 |
| Validate input parameters before use. | Safety | | ✓ | | ✓ | | | 2 |
| Don't deploy directly from arbitrary branches; use protected branches. | Safety | | ✓ | | | | | 1 |
| Use explicit needs dependencies between jobs. | Correctness | | ✓ | | | ✓ | ✓ | 3 |
| Don't ignore exit codes from scripts. | Error Handling | | ✓ | | | | | 1 |
| Use a YAML linter / follow YAML best practices (consistent indentation, no tabs). | Style | | ✓ | | | | ✓ | 2 |
| Keep workflows single-purpose (one workflow per file / process). | Structure | ✓ | ✓ | ✓ | | ✓ | ✓ | 5 |
| Run shellcheck against non-trivial shell scripts. | Correctness | | | | | ✓ | | 1 |
| One workflow file per major process (CI, CD, etc.). | Structure | ✓ | | ✓ | | | ✓ | 3 |
| Pin actions/checkout to v4 (or SHA). | Safety | ✓ | | | | | | 1 |

## Notes on clustering decisions

- "Give every workflow, job, and step an explicit name" merges rules that variously required names only on workflows, only on jobs, or on all three (gpt-4o-mini only explicitly required job names; grok only mentioned job/step identifiers). I clustered them because all are about the "name things explicitly" concern; a strict reader might want these split by scope.
- "Pin third-party actions to immutable references" aggregates a spectrum: gpt-5 and claude-opus distinguish SHA-for-third-party vs tag-for-first-party; gemini and grok accept major-version tags; haiku requires SHAs. I treated these as the same rule because the deterministic violation ("@main/@master/floating") is shared, but the pinning-granularity disagreement is real.
- "Don't use floating refs (@main/@master)" was folded into the pinning rule above rather than split out, since every model that stated one stated the other.
- "Use strict bash / set -euo pipefail" and "Set defaults.run.shell: bash" were kept as separate clusters — they address different failure modes (shell strictness vs shell selection) even though they often co-occur.
- "Use concurrency group with cancel-in-progress" and "Use concurrency for deployments (without cancel)" were kept as one row; only claude-opus explicitly noted the deploy-exception, but the core rule is the same.
- gemini's "extract scripts > 10 lines" and claude-opus's "> 20 lines" were clustered into one "extract long inline scripts" rule despite the differing thresholds.
- Claude-haiku's many narrow rules (deterministic test order, coverage threshold, security scanning, structured logging, rollback steps) did not appear in other models' outputs and are shown as Count=1. A more aggressive clusterer might merge "run security scanning" with general "safety" rules; I kept it distinct.
- "Use GitHub Environments with required reviewers" appears under both Safety and Deployment headings across models; clustered as one rule.
- "Never log/echo secrets" vs "Never hardcode secrets" were kept distinct — they're different failure modes (runtime leak vs source-controlled leak).
- Grok's "final job runs on failure (if: failure())" was clustered with claude-opus/haiku/gemini's "use explicit if: conditions for post-failure jobs" as they address the same concern, though grok's phrasing is narrower.
- "Keep workflows single-purpose" absorbed gpt-4o-mini's "separate concerns with distinct jobs" even though that rule is technically about jobs within a workflow rather than splitting files; the underlying principle (single-responsibility) is the same and no model articulated both separately.
- xai/grok's "don't allow write access in workflows triggered by forks" was clustered with the broader "least-privilege permissions" rule rather than with "restrict secrets for fork PRs", since it's phrased as a permissions concern.