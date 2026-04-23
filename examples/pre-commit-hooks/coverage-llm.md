## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Pin every hook to an explicit, immutable version; never use floating branches. | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Scope hooks to staged/changed files only, not the entire repository. | Performance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Exit non-zero on failure; do not silence or suppress errors. | Error Handling | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use the pre-commit framework rather than raw .git/hooks scripts. | Structure | ✓ | ✓ | ✓ |  | ✓ | ✓ | 5 |
| Do not perform network I/O in pre-commit hooks. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Keep hooks fast (under a small time budget) to avoid being bypassed. | Performance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Emit clear, actionable error messages including file/line info. | Error Handling / DX |  | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| Use files/types selectors and exclude generated/vendored directories. | Performance / Structure | ✓ |  | ✓ | ✓ |  |  | 3 |
| Do not run full test suites in pre-commit hooks. | Performance | ✓ | ✓ | ✓ |  | ✓ |  | 4 |
| Keep a single .pre-commit-config.yaml at the repo root under version control. | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Start shell hooks with set -Eeuo pipefail (and safe IFS). | Error Handling | ✓ |  | ✓ |  |  |  | 2 |
| Do not require sudo or elevated privileges. | Safety |  |  | ✓ | ✓ |  | ✓ | 3 |
| Hooks must be deterministic and idempotent. | Correctness | ✓ |  |  | ✓ | ✓ |  | 3 |
| Keep custom hook logic in version-controlled scripts, not inline shell in YAML. | Structure | ✓ |  | ✓ |  | ✓ |  | 3 |
| Run formatters before linters. | Structure | ✓ |  |  | ✓ |  |  | 2 |
| Mirror/enforce the same hooks in CI. | DX | ✓ |  | ✓ |  |  |  | 2 |
| Do not auto-`git add` or silently mutate files without developer action. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Do not rewrite history, push, or mutate refs from a pre-commit hook. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Serialize hooks that modify files (require_serial) to avoid races. | Safety | ✓ |  |  |  |  |  | 1 |
| Set minimum_pre_commit_version to a tested value. | Structure | ✓ |  |  |  |  |  | 1 |
| Pin language_version for Python (or default_language_version.python). | Structure | ✓ |  |  |  |  |  | 1 |
| Configure formatters to apply in-place fixes so pre-commit can re-stage. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Make fixers fail the commit when they modify files. | Correctness |  |  | ✓ |  |  |  | 1 |
| Provide an onboarding/setup command (e.g., make setup, pre-commit install). | DX | ✓ |  |  | ✓ |  |  | 2 |
| Regularly run pre-commit autoupdate and review in a dedicated PR. | DX | ✓ |  | ✓ |  |  |  | 2 |
| Keep hook output quiet on success and actionable on failure. | DX | ✓ |  |  |  |  |  | 1 |
| Do not include destructive commands (rm -rf, git reset --hard, etc.). | Safety | ✓ |  |  |  |  |  | 1 |
| Do not use pass_filenames: false unless repo-wide scan is genuinely required. | Safety / Performance | ✓ |  | ✓ |  |  |  | 2 |
| Prefer native language hooks over Docker where possible. | Performance | ✓ |  |  |  |  |  | 1 |
| Do not pass repo-wide flags like --all/--all-files in local hooks. | Performance | ✓ |  |  |  |  |  | 1 |
| Give every hook an explicit id and descriptive name. | Structure |  |  | ✓ |  |  |  | 1 |
| Do not duplicate hooks already provided by pre-commit-hooks. | Hygiene |  |  | ✓ |  |  |  | 1 |
| Leave `--no-verify` working as an escape hatch. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Document the purpose/intent of each hook. | Maintainability |  |  |  | ✓ |  |  | 1 |
| Avoid multi-purpose hooks; keep each single-purpose. | Structure |  |  |  | ✓ |  |  | 1 |
| Prefer opinionated formatters with minimal config. | Style |  |  |  | ✓ |  |  | 1 |
| Document rationale when disabling a linter rule. | Style |  |  |  | ✓ |  |  | 1 |
| Enforce line-length limits on source files. | Style |  | ✓ |  |  |  |  | 1 |
| Require documentation/comments with code changes where needed. | Safety |  | ✓ |  |  |  |  | 1 |
| Run automated tests as part of pre-commit. | Safety |  | ✓ |  |  |  |  | 1 |
| Cache tool outputs across hook runs where supported. | Performance |  |  |  | ✓ |  |  | 1 |
| Run independent hooks in parallel. | Performance |  |  |  | ✓ |  |  | 1 |
| Order hooks fastest to slowest for fail-fast behavior. | Performance |  |  |  | ✓ | ✓ |  | 2 |
| Do not auto-install hooks manually; automate install (husky install, pre-commit install). | DX |  |  |  | ✓ |  |  | 1 |
| Prefer auto-formatters over style-only linters. | Style |  |  |  |  | ✓ |  | 1 |
| Do not check commit message formatting in a pre-commit hook (use commit-msg). | Behavior |  |  |  |  | ✓ |  | 1 |
| Validate custom shell hook scripts with shellcheck. | Safety |  |  |  |  | ✓ |  | 1 |
| Use fail_fast in CI runs. | Safety |  |  |  |  | ✓ |  | 1 |
| Organize hook configurations alphabetically or by category. | Style |  |  |  |  |  | ✓ | 1 |
| Avoid hardcoded absolute paths in hook configurations. | Configuration |  |  |  |  |  | ✓ | 1 |
| Respect framework-provided file list; do not re-discover files with find/git ls-files. | Correctness |  |  | ✓ |  |  |  | 1 |
| Test new hooks before enabling them repo-wide. | Safety |  |  |  | ✓ |  | ✓ | 2 |
| Do not invoke hooks on generated/vendored files. | Safety | ✓ |  |  | ✓ |  |  | 2 |

## Notes on clustering decisions

- **"Scope hooks to staged/changed files only"** merges gpt-5's "don't use --all-files", gpt-4o-mini's "limit hooks to staged files", opus's "operate on staged content only", haiku's rule 2, gemini's "scope hooks to staged files", and grok's "run only on staged files". These are phrased quite differently (some about flags, some about git diff --cached, some about framework file lists) but share the same substance.
- **"Keep hooks fast"** clusters thresholds of 500ms (gpt-4o-mini), 2s (opus), 5s (haiku, gemini, grok), and gpt-5's more general "optimize for the common path". Numeric thresholds differ but the rule is the same.
- **"Exit non-zero on failure; do not silence errors"** merges gpt-5's "do not use || true", gpt-4o-mini's "exit with non-zero", opus's "exit non-zero on any error", haiku's "do not suppress warnings", gemini's "exit non-zero on failure", and grok's "fail commit on non-zero exit".
- **"Emit clear, actionable error messages"** — opus, haiku, gemini, grok, and gpt-4o-mini all raised this but with different emphases (file/line info vs. remediation path vs. just "actionable"). Clustered together despite differences in specificity.
- **"Do not auto-`git add` or silently mutate files"** — opus's explicit "no git add" and haiku's "never auto-mutate without developer action" are close enough to cluster; gpt-5's "do not modify unstaged files" is related but more about scope, so kept separate.
- **"Do not run full test suites"** — I kept this separate from the broader "keep hooks fast" since several models called it out as a specific anti-pattern with its own rationale.
- **"Use the pre-commit framework"** — grok's framing is somewhat softer ("do use…") but substantively matches the others.
- **"Pin every hook to an explicit version"** — grok's rule is phrased as "specify exact versions for hooks and their dependencies" which is broader than floating-branch prohibition, but I clustered it since the core substance overlaps.
- **gpt-4o-mini's "run automated tests on commits"** directly contradicts opus/haiku/gemini's "do not run tests in pre-commit." I kept these as separate rules (rather than negating one) since they are genuinely opposing positions.
- **"Do not invoke hooks on generated/vendored files"** (haiku) vs. **"Exclude generated and vendored directories"** (gpt-5) — these are nearly identical in substance; clustered.
- **"Order hooks fastest to slowest"** (haiku) and **"Run formatters before linters"** (gpt-5, haiku) are related but distinct ordering rules; kept separate.
- **Opus's "Do not require sudo"** and haiku's "Never require sudo" and grok's "hooks shouldn't require elevated permissions" clustered together; grok also mentions network access in the same rule but I attributed the network portion to the separate network-I/O cluster.