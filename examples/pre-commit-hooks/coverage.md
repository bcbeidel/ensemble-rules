# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **Always allow `git commit --no-verify` to bypass hooks.** This is a git built-in and should never be disabled; it is the safety valve | Escape Hatches & Exceptions |  |  |  | ✓ |  |  | 1 |
| **Avoid multi-purpose hooks.** A hook that formats code, lints, checks secrets, and validates YAML is hard to debug and slow to run; split it into separate hooks | Structure & Configuration |  |  |  | ✓ |  |  | 1 |
| **Cache tool outputs or metadata across hook runs if the tool supports it.** (e.g., eslint's `--cache` flag); this can reduce runtime by 50%+ on no-change commits | Performance |  |  |  | ✓ |  |  | 1 |
| **Commit a `.pre-commit-config.yaml` at the repo root and document bootstrap (`pre-commit install`) in the README.** Discoverability is the difference between enforced and ignored | Structure |  |  | ✓ |  |  |  | 1 |
| **Declare `files:` or `types:` for every hook so it only runs on relevant files.** Broad matching wastes time and produces irrelevant failures | Structure |  |  | ✓ |  |  |  | 1 |
| **Declare each hook's purpose in a comment or documentation string.** A future maintainer should understand why the hook exists without reading its implementation | Structure & Configuration |  |  |  | ✓ |  |  | 1 |
| **Define hooks in a single, root `.pre-commit-config.yaml` file.** | Framework & Structure |  |  |  |  | ✓ |  | 1 |
| **Design hooks to complete in under 5 seconds on a typical commit.** If a hook takes >10 seconds, developers will bypass it or disable it | Performance |  |  |  | ✓ |  |  | 1 |
| **Do not check for commit message formatting in a `pre-commit` hook.** | Behavior |  |  |  |  | ✓ |  | 1 |
| **Do not duplicate hooks already provided by `pre-commit-hooks` (trailing whitespace, EOF, merge conflict markers, large file check).** Reinventing them is pure tech debt | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Do not invoke hooks on generated files, build artifacts, or vendored code.** Use `.gitignore` or explicit path patterns in hook configuration to exclude them | Scope & Safety |  |  |  | ✓ |  |  | 1 |
| **Do not make network calls unless absolutely required (e.g., license checker querying a license database).** Hooks must be runnable offline and must not fail due to transient network issues | Scope & Safety |  |  |  | ✓ |  |  | 1 |
| **Do not make network calls within a hook.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Do not modify files outside the staged set.** Surprising side effects destroy trust | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not perform network I/O in a commit-time hook.** Breaks offline work and slows every commit | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not require developers to install hooks manually.** Use `pre-commit install` (framework) or a setup script that runs automatically (e.g., via `husky install` in `postinstall`) | Documentation & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Do not require root, sudo, or global package installation.** Hooks must run in the developer's normal shell with the repo's declared toolchain | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not rewrite commit history, push, tag, or mutate refs from a pre-commit hook.** Commit-time is the wrong layer for those operations | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not run `git add` inside a hook.** Auto-staging hides changes from the developer | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not run application tests in pre-commit hooks.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Do not run full test suites in pre-commit; move them to pre-push or CI.** (contested) Tests are too slow and too noisy for commit-time | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not run whole-repo type checking in pre-commit; run it in CI or pre-push.** (contested) Incremental type checkers exist but are fragile; the bypass rate isn't worth it | Performance |  |  | ✓ |  |  |  | 1 |
| **Do not suppress warnings or errors; fail visibly if the hook detects any issue.** A hook that warns and passes is a hook developers will ignore | Error Handling & Messages |  |  |  | ✓ |  |  | 1 |
| **Do not use complex shell logic inside the `.pre-commit-config.yaml` `entry`.** | Framework & Structure |  |  |  |  | ✓ |  | 1 |
| **Document the purpose of each hook and any non-obvious configuration** in a markdown file at the repo root or in the hook configuration file itself | Documentation & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Emit actionable error messages that name the file, line, and fix.** "Lint failed" is useless; "app/x.py:42: unused import `os`" is actionable | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Enable `require_serial: true` only when a hook genuinely cannot run in parallel.** Serial hooks stall the whole run | Performance |  |  | ✓ |  |  |  | 1 |
| **Ensure that any auto-formatting hook is idempotent.** | Behavior |  |  |  |  | ✓ |  | 1 |
| **Ensure the entire hook suite completes in under 5 seconds on a typical commit.** | Performance |  |  |  |  | ✓ |  | 1 |
| **Error messages must include the offending file name and line number (if applicable).** A developer should not have to search the output to find which file failed | Error Handling & Messages |  |  |  | ✓ |  |  | 1 |
| **Every hook that fails must output a clear, actionable error message to stderr.** "Linting failed" is not actionable; "Line 15 in src/main.py: unused import `json` | Error Handling & Messages |  |  |  | ✓ |  |  | 1 |
| **Exit non-zero on any error, including tool crashes and unexpected conditions.** Silent pass-through destroys the hook's value | Correctness |  |  | ✓ |  |  |  | 1 |
| **Fail fast: order hooks from fastest to slowest.** If a quick syntax check fails, skip expensive linting; save CI for comprehensive checks | Structure & Configuration |  |  |  | ✓ |  |  | 1 |
| **Failure messages must be clear, concise, and actionable.** | Safety & Error Handling |  |  |  |  | ✓ |  | 1 |
| **For formatters (e.g., `prettier`, `black`, `gofmt`), run them as a gate before linters.** Linters should not complain about formatting; formatters should not complain about logic | Style & Language-Specific Rules |  |  |  | ✓ |  |  | 1 |
| **For large repositories, use incremental or diff-only checks.** Only lint the files that changed in the current commit, not the entire codebase | Performance |  |  |  | ✓ |  |  | 1 |
| **For linters, enable only rules that the team has consciously adopted.** A linter with 500 rules enabled and 50 disabled creates confusion; start with a minimal set and add rules explicitly | Style & Language-Specific Rules |  |  |  | ✓ |  |  | 1 |
| **Give every hook an explicit `id` and `name` that describes what it checks.** Defaults are opaque in failure output | Structure |  |  | ✓ |  |  |  | 1 |
| **Hooks must be deterministic: the same input must always produce the same output.** Non-determinism (random IDs, timestamps, nondeterministic tool output) breaks developer trust | Scope & Safety |  |  |  | ✓ |  |  | 1 |
| **Hooks must exit with a non-zero status code on failure.** | Safety & Error Handling |  |  |  |  | ✓ |  | 1 |
| **If a hook can auto-fix the issue, mention that in the error message and do not auto-fix.** (contested) Let the developer run the fix command; this preserves visibility of what changed | Error Handling & Messages |  |  |  | ✓ |  |  | 1 |
| **If a hook is too strict or produces false positives, fix the hook rather than asking developers to use `--no-verify`.** A hook that is regularly bypassed should be revised or removed | Escape Hatches & Exceptions |  |  |  | ✓ |  |  | 1 |
| **If a hook requires manual intervention (e.g., a merge conflict marker), explain the steps to resolve it in the error message.** Do not assume the developer will know what to do | Error Handling & Messages |  |  |  | ✓ |  |  | 1 |
| **If a linter rule is disabled, document why in a comment near the disable directive.** (e.g., `# noqa: E501 — long URLs are OK in comments`) | Style & Language-Specific Rules |  |  |  | ✓ |  |  | 1 |
| **Keep custom hook logic in `scripts/hooks/` as standalone executables referenced by `entry:`, not as inline shell in YAML.** Inline shell is unreviewable and untestable | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep total hook runtime under 2 seconds on a typical commit.** Slower hooks get bypassed, which is worse than no hook | Performance |  |  | ✓ |  |  |  | 1 |
| **Leave `--no-verify` working; never try to defeat it.** Bypass is a legitimate escape hatch; teams enforce via server-side checks or CI | Safety |  |  | ✓ |  |  |  | 1 |
| **Maintain a shared, version-controlled hook configuration.** (e.g., `.pre-commit-config.yaml`, `.husky/` directory, or `scripts/hooks/`) | Documentation & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Make fixers fail the commit when they modify files.** Forces the developer to re-stage and review the change | Correctness |  |  | ✓ |  |  |  | 1 |
| **Never auto-mutate files in the working directory without explicit developer action.** (contested) If a hook auto-formats, do so only in a stage-in-place mode that updates the index and working tree after developer approval, or not at all | Scope & Safety |  |  |  | ✓ |  |  | 1 |
| **Never require sudo, a password, or elevated privileges to run a hook.** Hooks should run with the developer's normal user permissions | Scope & Safety |  |  |  | ✓ |  |  | 1 |
| **Operate on staged content only, via the framework's file list or `git diff --cached --name-only --diff-filter=ACMR`.** Reading the working tree lints unstaged changes and misses the actual commit contents | Correctness |  |  | ✓ |  |  |  | 1 |
| **Pin every hook to an explicit `rev` (tag or SHA), never to a branch.** Unpinned versions break reproducibility across machines and time | Structure |  |  | ✓ |  |  |  | 1 |
| **Pin hook versions to a specific, immutable revision (a tag or full commit SHA).** | Framework & Structure |  |  |  |  | ✓ |  | 1 |
| **Prefer auto-formatters that modify files over linters that only report style issues.** `(contested)` | Behavior |  |  |  |  | ✓ |  | 1 |
| **Provide a README or wiki entry that explains how to run hooks locally and how to bypass them.** Include the command to invoke the hook manually and when use of `--no-verify` is acceptable | Structure & Configuration |  |  |  | ✓ |  |  | 1 |
| **Provide a clear, documented process for temporarily disabling a hook.** (e.g., commenting out a line in `.pre-commit-config.yaml`) | Escape Hatches & Exceptions |  |  |  | ✓ |  |  | 1 |
| **Respect the framework-provided `$PRE_COMMIT` environment and argv file list; do not re-discover files with `find` or `git ls-files`.** Re-discovery bypasses the staging isolation the framework provides | Correctness |  |  | ✓ |  |  |  | 1 |
| **Run hooks in parallel where independent.** (e.g., format Python and check YAML at the same time) | Performance |  |  |  | ✓ |  |  | 1 |
| **Run hooks only on staged changes, not on the entire repository.** This keeps hook runtime acceptable and avoids reporting pre-existing issues as blocking current commits | Structure & Configuration |  |  |  | ✓ |  |  | 1 |
| **Run the same hook versions in CI (via `pre-commit run --all-files` or `pre-commit.ci`).** Divergence between local and CI produces unreproducible failures | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Scope every hook to changed files, not the whole repo.** Per-commit work should be proportional to the commit's size | Performance |  |  | ✓ |  |  |  | 1 |
| **Scope hooks to run only on the files staged for the current commit.** | Behavior |  |  |  |  | ✓ |  | 1 |
| **Set `pass_filenames: true` (the default) and let the framework batch; only use `pass_filenames: false` for repo-wide invariants.** Per-file invocation parallelizes cleanly | Performance |  |  | ✓ |  |  |  | 1 |
| **Test hooks locally before committing them to the repository.** A hook that breaks in CI after it has been merged is a productivity loss | Documentation & Maintainability |  |  |  | ✓ |  |  | 1 |
| **Update hook revs on a schedule (e.g., monthly via `pre-commit autoupdate`) and commit the result as a standalone change.** Stale pins rot; batched updates are reviewable | Hygiene |  |  | ✓ |  |  |  | 1 |
| **Use `fail_fast: true` for CI runs to get quicker feedback.** | Safety & Error Handling |  |  |  |  | ✓ |  | 1 |
| **Use `set -euo pipefail` at the top of every shell hook.** Default shell behavior hides failures | Correctness |  |  | ✓ |  |  |  | 1 |
| **Use language-specific hook tools native to each ecosystem.** (e.g., `ruff` for Python, `eslint` for JavaScript, `golangci-lint` for Go) | Structure & Configuration |  |  |  | ✓ |  |  | 1 |
| **Use opinionated formatters (e.g., `black`, `gofmt`, `prettier` with minimal config) over configurable ones.** Less configuration means fewer team arguments and easier onboarding | Style & Language-Specific Rules |  |  |  | ✓ |  |  | 1 |
| **Use the `pre-commit` framework for managing hooks.** | Framework & Structure |  |  |  |  | ✓ |  | 1 |
| **Use the `pre-commit` framework rather than hand-rolled `.git/hooks/pre-commit` scripts.** Framework handles staging isolation, per-language environments, and caching correctly; hand-rolled scripts almost never do | Structure |  |  | ✓ |  |  |  | 1 |
| **Validate any custom hook shell scripts with `shellcheck`.** | Safety & Error Handling |  |  |  |  | ✓ |  | 1 |
| **Version all hook tools explicitly in a lockfile or manifest.** (e.g., `.pre-commit-hooks.yaml` with `rev:` pinned, or `package-lock.json`, `requirements.txt`, `go.mod`) | Structure & Configuration |  |  |  | ✓ |  |  | 1 |
| Audience: Engineers and AI coding assistants authoring or reviewing pre-commit configurations and local hook scripts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Configure formatters to apply changes in place (e.g., --fix/--write/-w) so pre-commit can re-stage them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do configure hooks to run only on staged files, not the entire repository | Execution |  |  |  |  |  | ✓ | 1 |
| Do enforce a coding style guide (e.g., Prettier for JavaScript, Black for Python) | Style |  | ✓ |  |  |  |  | 1 |
| Do exit with a non-zero status on failure | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do implement logging or output from hooks to clearly explain failures | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do include language-specific linters (e.g., eslint for JavaScript, flake8 for Python) that target common errors and style issues | Hook Selection |  |  |  |  |  | ✓ | 1 |
| Do limit hooks to run only on staged files to avoid unnecessary processing of unchanged files | Structure |  | ✓ |  |  |  |  | 1 |
| Do limit the scope of checks based on the file type | Performance |  | ✓ |  |  |  |  | 1 |
| Do limit the total execution time of all hooks to under 5 seconds per commit | Performance |  |  |  |  |  | ✓ | 1 |
| Do not include destructive commands (git reset --hard, git clean -fdx, rm -rf, docker prune) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not pass repo-wide flags like --all or --all-files in local pre-commit hooks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not run network or package-manager commands in hooks (curl, wget, pip install, npm install, apt-get, brew, go get, gem install) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not set pass_filenames: false unless the tool inherently requires a repo-wide scan | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize hook configurations alphabetically or by category in the config file | Style and Maintainability |  |  |  |  |  | ✓ | 1 |
| Do prioritize auto-formatting hooks (e.g., black for Python) over manual style checks | Hook Selection |  |  |  |  |  | ✓ | 1 |
| Do run automated tests on committed code | Safety |  | ✓ |  |  |  |  | 1 |
| Do set hooks to fail the commit on any non-zero exit code from tools | Execution |  |  |  |  |  | ✓ | 1 |
| Do specify exact versions for all hooks and their dependencies in the configuration file | Configuration |  |  |  |  |  | ✓ | 1 |
| Do test new hooks in a isolated branch or staging environment before enabling them globally | Safety |  |  |  |  |  | ✓ | 1 |
| Do use a single entry point for configuring hooks | Structure |  | ✓ |  |  |  |  | 1 |
| Do use the pre-commit framework (e.g., via .pre-commit-config.yaml) instead of raw .git/hooks scripts for easier management and versioning | Configuration |  |  |  |  |  | ✓ | 1 |
| Don't add unnecessary hooks; limit to those directly relevant to the project's tech stack | Hook Selection |  |  |  |  |  | ✓ | 1 |
| Don't allow hooks to modify files outside the staged area or commit changes automatically | Execution |  |  |  |  |  | ✓ | 1 |
| Don't hardcode absolute paths in hook configurations; use relative paths or hooks that detect the project root | Configuration |  |  |  |  |  | ✓ | 1 |
| Don't include hooks that perform deep scans or require installing large tools | Performance |  |  |  |  |  | ✓ | 1 |
| Don't suppress errors or warnings in hook scripts; always propagate them | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't use custom scripts for standard tasks; rely on pre-built hooks from reputable sources | Style and Maintainability |  |  |  |  |  | ✓ | 1 |
| Don't use hooks that require elevated permissions or external network access | Safety |  |  |  |  |  | ✓ | 1 |
| Don’t allow code files that exceed a specific line length (e.g., 120 characters) | Style |  | ✓ |  |  |  |  | 1 |
| Don’t allow commits without relevant documentation (e.g., comments, README updates) where necessary | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t ignore error messages from executables used in hooks | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t introduce hooks that take longer than a set threshold (e.g., 500ms) to execute | Performance |  | ✓ |  |  |  |  | 1 |
| Ensure hooks operate only on staged content; do not read or modify unstaged files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Exclude generated and vendored directories (e.g., node_modules, dist, build, target, .venv, vendor, third_party) at top-level or per-hook | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Exit non-zero on any failure; do not silence errors with \|\| true | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fail the commit on linter findings; do not use exit-zero to hide issues | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For Python hooks, pin language_version (or set default_language_version.python) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For repo: local hooks, specify files or types to limit scope | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep a single .pre-commit-config.yaml at the repository root | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep hook output quiet on success and actionable on failure | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep slow, repo-wide analyses in CI or manual stages, not on every commit | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make hooks idempotent and deterministic given the same inputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mirror critical hooks in CI with pre-commit run -a | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Order formatters before linters and analyzers | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin every hook rev to an immutable tag or commit; never use floating branches like master, main, HEAD, latest, or stable | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer native language hooks over Docker for local development when possible | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide an onboarding command (e.g., make setup) that installs pre-commit and runs pre-commit install | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Regularly run pre-commit autoupdate and review changes in a dedicated PR | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Git pre-commit hooks defined via the pre-commit framework or repo-local scripts invoked by it, focused on formatters, linters, and validators for staged changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Serialize any hook that modifies files with require_serial: true | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set minimum_pre_commit_version to a specific version you test in CI | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start all shell hooks with a shebang and set -Eeuo pipefail and a safe IFS | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use files/types/types_or and excludes to minimize matcher work on large repositories | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use repo: local for in-repo hooks and point entry to versioned scripts under the repository | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use the pre-commit framework instead of custom .git/hooks scripts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

