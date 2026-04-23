# Synthesized Best Practices: Pre-Commit Hooks

## 1. Consensus Rules

### Framework & Structure

- **Use the `pre-commit` framework rather than hand-rolled `.git/hooks/` scripts.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Provides portable, shareable, versioned configuration with per-language environment caching.
- **Maintain a single `.pre-commit-config.yaml` at the repo root, checked into version control.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Single source of truth for what runs on commit.
- **Pin every hook `rev` to an immutable tag or SHA; never use floating refs (`main`, `master`, `HEAD`, `latest`).** *(near-identical wording across GPT-5, Claude Opus, Gemini, Grok; similar in Claude Haiku)* — Ensures reproducible behavior across machines and over time.
- **Keep custom hook logic in version-controlled scripts (e.g., `scripts/hooks/`) rather than inline shell in YAML.** *(substantively similar across GPT-5, Claude Opus, Gemini)* — Inline shell is unreviewable, untestable, and hides complexity.

### Scope & Correctness

- **Scope hooks to staged/changed files, not the whole repo.** *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Keeps per-commit work proportional to diff size and avoids reporting pre-existing issues.
- **Declare `files:` or `types:` for each hook to limit what it processes.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku)* — Prevents irrelevant matches and speeds up runs.
- **Exit non-zero on any failure; do not silently swallow errors with `|| true`, `--exit-zero`, or `set +e`.** *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Silent pass-through defeats the hook's purpose.
- **Hooks must be deterministic and idempotent.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)* — Same input must produce the same result; avoids flakiness and trust erosion.

### Safety

- **Do not perform network I/O in pre-commit hooks (no `curl`, `wget`, `pip install`, `npm install`, etc.).** *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)* — Breaks offline work, slows commits, and introduces flakiness.
- **Do not require sudo, elevated privileges, or password prompts.** *(substantively similar across Claude Opus, Claude Haiku, Grok)* — Hooks must run as the normal developer user.
- **Do not mutate files outside the staged set, auto-`git add`, or rewrite git history from a hook.** *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)* — Surprising side effects destroy developer trust.

### Error Handling

- **Shell hooks must start with a shebang and `set -euo pipefail`.** *(near-identical across GPT-5, Claude Opus, Gemini)* — Default shell semantics hide failures; strict mode surfaces them.
- **Failure messages must be actionable: name the file, line, and how to fix.** *(substantively similar across Claude Opus, Claude Haiku, Grok, Gemini)* — "Lint failed" is useless; `app/x.py:42: unused import 'os'` is actionable.

### Performance

- **Keep total hook runtime fast (~2–5 seconds on a typical commit).** *(substantively similar across Claude Opus, Claude Haiku, Gemini, Grok; GPT-5 expresses it indirectly)* — Slow hooks get bypassed with `--no-verify`, which is worse than no hook.
- **Do not run full test suites or whole-repo type checking in pre-commit; move those to pre-push or CI.** *(substantively similar across Claude Opus, Claude Haiku, Gemini, Grok; GPT-5 agrees)* — Tests and type checks are too slow and noisy for commit-time.
- **Run formatters before linters.** *(substantively similar across GPT-5, Claude Haiku)* — Linters should not report issues a formatter would fix.

### Developer Experience

- **Mirror pre-commit enforcement in CI (e.g., `pre-commit run --all-files`).** *(substantively similar across GPT-5, Claude Opus, Claude Haiku)* — Ensures divergence between local and CI can't produce unreproducible failures.
- **Document bootstrap (`pre-commit install`) in the repo README or automate via setup script.** *(substantively similar across Claude Opus, Claude Haiku, Grok)* — Discoverability determines whether hooks are actually enforced.

---

## 2. Strong Minority Rules

- **Set `minimum_pre_commit_version` and pin `language_version` for language-specific hooks.** *(GPT-5)* — Specific, implementable, and closes real portability gaps that other models hand-waved.
- **Serialize file-mutating hooks with `require_serial: true`.** *(GPT-5)* — Concrete guidance that prevents a real race-condition class others did not name.
- **Exclude generated and vendored directories (`node_modules`, `dist`, `build`, `target`, `.venv`, `vendor`) globally or per-hook.** *(GPT-5, Claude Haiku)* — Practical and checkable; reduces real-world noise.
- **Make fixer hooks fail the commit when they modify files, so the developer re-stages and reviews.** *(Claude Opus)* — A well-reasoned position on a contested area; preserves developer awareness of automated changes.
- **Leave `--no-verify` working; never try to defeat the bypass.** *(Claude Opus, Claude Haiku)* — Important cultural/safety rule: the escape hatch is a feature, not a bug.
- **Do not duplicate hooks already provided by `pre-commit-hooks` (trailing whitespace, EOF fixer, merge-conflict markers, large-file check).** *(Claude Opus)* — Prevents pure tech debt from reinvented-wheel hooks.
- **Run `pre-commit autoupdate` on a schedule, reviewing changes in a dedicated PR.** *(GPT-5, Claude Opus)* — Keeps pins current without letting them rot.
- **Validate custom shell hook scripts with `shellcheck`.** *(Gemini)* — Concrete, tool-backed validation for a real bug class in custom hooks.
- **Give every hook an explicit `name` (in addition to `id`) for readable failure output.** *(Claude Opus)* — Small but meaningful readability improvement.
- **Document why each linter rule disable exists (e.g., `# noqa: E501 — long URLs OK`).** *(Claude Haiku)* — Prevents silent rule-disable drift.

---

## 3. Divergences

### Auto-fix vs. reject behavior for formatters

- **Apply-and-restage (GPT-5, Grok-ish, Gemini):** Configure formatters with `--fix`/`--write` so the commit contains the fixed output.
- **Fail-and-require-review (Claude Opus, Claude Haiku):** Fixers should fail the commit when they modify files, forcing the developer to inspect and re-stage.

**Synthesis:** Both are defensible; the choice depends on team culture. The pre-commit framework's default behavior is already "fail if files modified, let developer re-stage" — which aligns with Claude's position. **Recommendation:** Treat auto-fixing-and-committing as the friendly default for pure formatters (Black, Prettier, gofmt) where the transformation is boring and reviewed in the editor, but require fail-and-review for autofix linters (Ruff `--fix`, ESLint `--fix`) where changes can be semantic.

### Running tests/type checking in pre-commit

- **Never (Claude Opus, Claude Haiku, Gemini, Grok):** Tests and type checks belong in CI or pre-push.
- **Allowed with narrow scoping (GPT-5 implied):** Repo-wide slow checks should default to CI, but doesn't explicitly forbid them.
- **Must run tests (GPT-4o-mini):** "Do run automated tests on committed code."

**Synthesis:** The strong majority is right. GPT-4o-mini is outlier and its rule would cause hooks to be bypassed. **Recommendation:** Do not run full test suites or whole-repo type checkers in pre-commit. Move to `pre-push` or CI.

### `pass_filenames: false`

- **Avoid it (GPT-5):** Only use when the tool inherently requires repo-wide scanning.
- **Acceptable for repo-wide invariants (Claude Opus, Claude Haiku):** Use deliberately with comment/justification.

**Synthesis:** Agreement in substance — default to `pass_filenames: true`, allow exceptions with justification.

### Line length / specific style thresholds

- **GPT-4o-mini** proposes a hard 120-character line limit as a hook rule.
- All other models treat specific thresholds as tool-configuration concerns, not pre-commit policy.

**Synthesis:** Line-length is a lint config detail, not a pre-commit meta-rule. Omit from the rules file.

### Hook ordering by speed (fastest first) vs. formatters-before-linters

- **Claude Haiku:** Order fastest → slowest for fail-fast.
- **GPT-5, Claude Haiku:** Order formatters → linters so linters see formatted code.

**Synthesis:** These don't actually conflict in practice (formatters tend to be fast). **Recommendation:** Primary rule is "formatters before linters"; secondary heuristic is "fastest first within a tier."

### Alphabetical ordering of hooks

- **Grok:** Sort hooks alphabetically.
- Everyone else: Order by dependency (formatters → linters → validators).

**Synthesis:** Dependency order is more meaningful than alphabetical. Drop Grok's rule.

---

## 4. Notable Omissions

- **Pin every `rev` to an immutable tag/SHA** — missed by GPT-4o-mini. The single most-cited rule in the corpus; omitting it is a meaningful gap.
- **Scope hooks to staged files, not the whole repo** — GPT-4o-mini mentions "staged files only" but does not emphasize scoping per-hook via `files:`/`types:`.
- **Do not run network I/O in hooks** — missed by GPT-4o-mini. A core safety rule four other models converged on.
- **`set -euo pipefail` for shell hooks** — missed by Claude Haiku, GPT-4o-mini, Grok. Three models converged on this; its absence elsewhere is a drafting gap, not a substantive disagreement.
- **Performance budget (<2–5 seconds)** — missed by GPT-5 and GPT-4o-mini (well, GPT-4o-mini says <500ms which is unrealistic). Four models agree a concrete budget matters.
- **Do not make hooks run full test suites** — missed by GPT-5 (implicit only) and actively contradicted by GPT-4o-mini. Majority view is strong.
- **Use the `pre-commit` framework** — GPT-4o-mini never explicitly endorses this; its guidance is framework-agnostic in a way that reads as unaware of the ecosystem.

GPT-4o-mini's omissions are systemic and suggest the model didn't engage with the actual pre-commit ecosystem. Its response should be weighted accordingly.

---

## 5. Shared Deterministic Checks

### Shared checks (multiple models converged)

- **Check** — `.pre-commit-config.yaml` exists at the repo root and parses as valid YAML with a top-level `repos:` key.
  - **Signal** — Filesystem listing + YAML parse of repo root.
  - **Tool candidate** — ad-hoc (YAML parser + file-existence check).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Claude Opus additionally requires the top-level `repos:` key; others check only existence. Monorepo exception (per-package configs) noted by GPT-5 only.

- **Check** — Every non-local hook `rev` is an immutable reference, not a floating branch name (`main`, `master`, `HEAD`, `develop`, `latest`, `stable`).
  - **Signal** — Parsed YAML of `.pre-commit-config.yaml`, iterating `repos[].rev`.
  - **Tool candidate** — ad-hoc (regex: semver-like tag or 7/40-char hex SHA).
  - **Raised by** — GPT-5, Claude Opus, Gemini, Grok.
  - **Variance** — GPT-5 and Claude Opus suggest stricter shape checks (semver or 40-hex); Gemini and Grok match by banned-name blacklist. Stricter form catches more, but produces false positives for date-based tags.

- **Check** — Every hook has `files:`, `types:`, `types_or:`, or an equivalent scoping directive.
  - **Signal** — Parsed YAML of `.pre-commit-config.yaml` per hook entry.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — GPT-5 applies to `repo: local` hooks only; Claude Opus applies broadly but notes upstream hooks often set `types` themselves, producing false positives.

- **Check** — No hook entry or referenced script contains network-fetch patterns (`curl`, `wget`, `pip install`, `npm install`, `apt-get install`, `brew install`, `gem install`, `go get`).
  - **Signal** — Entry/args strings in YAML plus contents of referenced shell scripts.
  - **Tool candidate** — ad-hoc (regex grep).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok (implied).
  - **Variance** — Claude Opus also flags bare `http://`/`https://` URLs; GPT-5 adds package-manager breadth; all agree on heuristic nature with false positives for comments/docstrings.

- **Check** — Every shell hook script has a shebang and `set -euo pipefail` (or equivalents) within the first ~20 lines.
  - **Signal** — Raw source of custom hook scripts.
  - **Tool candidate** — ad-hoc (text scan); `shellcheck` catches related issues.
  - **Raised by** — GPT-5, Claude Opus, Gemini (via shellcheck).
  - **Variance** — GPT-5 also requires a safe `IFS`; Claude Opus relaxes `pipefail` for POSIX `/bin/sh`.

- **Check** — No hook entry or script contains destructive or history-mutating git commands (`git add`, `git push`, `git commit`, `git reset --hard`, `git clean -fdx`, `rm -rf`, `git rebase`, `git tag`).
  - **Signal** — Entry/args strings in YAML plus contents of referenced scripts.
  - **Tool candidate** — ad-hoc (regex grep).
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — GPT-5 focuses on destructive shell commands; Claude Opus focuses on git-mutation commands. Union of both is the useful superset.

- **Check** — No hook suppresses errors via `|| true`, `--exit-zero`, or a toggled `set +e`.
  - **Signal** — Entry/args strings in YAML plus contents of referenced scripts.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Grok (implied), Claude Haiku (implied).
  - **Variance** — GPT-5 is most specific; others state the principle without an explicit check.

- **Check** — No hook entry contains shell-chaining metacharacters (`;`, `&&`, `||`, `|`, `$(...)`, backticks) or exceeds a length threshold (~80 chars).
  - **Signal** — Parsed YAML `entry:` values.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Gemini.
  - **Variance** — Gemini allows any shell metacharacters to trigger; Claude Opus combines metacharacter and length heuristics.

- **Check** — Hooks matching known test runners (`pytest`, `go test`, `cargo test`, `npm test`, `jest`) or whole-repo type checkers (`mypy`, `pyright`, `tsc`) with `pass_filenames: false` are flagged.
  - **Signal** — Parsed YAML of `.pre-commit-config.yaml`.
  - **Tool candidate** — ad-hoc (id/entry match against curated list).
  - **Raised by** — Claude Opus, Claude Haiku (implied), Gemini (implied).
  - **Variance** — Treated as warning by Claude Opus (contested rule); others treat as hard rule.

### Singleton checks (one model, but generally useful)

- **Check** — Top-level `minimum_pre_commit_version` is set and matches `^\d+\.\d+\.\d+$`.
  - **Signal** — Parsed YAML of `.pre-commit-config.yaml`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Any hook with `language: python` has `language_version` set, or top-level `default_language_version.python` is set.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Hooks identified as file-mutating formatters (Black, isort, Ruff+`--fix`, Prettier, ESLint+`--fix`, gofmt, rustfmt, shfmt, clang-format, `terraform fmt`) declare `require_serial: true`.
  - **Signal** — Parsed YAML; id/args heuristics.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Local hooks have a non-empty `name:` field.
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Present vendor/generated directories (`node_modules`, `dist`, `build`, `target`, `.venv`, `vendor`, `third_party`) are excluded either globally or per-hook.
  - **Signal** — Filesystem listing + parsed YAML `exclude` patterns.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Custom shell scripts referenced by local hooks pass `shellcheck` with no errors.
  - **Signal** — Local hook script files.
  - **Tool candidate** — `shellcheck` (or `shellcheck-py` wrapper).
  - **Raised by** — Gemini.

- **Check** — Local hook entries matching file-mutating formatters include an in-place write flag (`--fix`, `--write`, `-w`, `-i`).
  - **Signal** — Parsed YAML.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — CI configuration files contain a step that runs `pre-commit run --all-files` (or equivalent `pre-commit.ci` integration).
  - **Signal** — CI config files (`.github/workflows/*.yml`, `.gitlab-ci.yml`, etc.).
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — GPT-5.

- **Check** — No hook script contains `sudo` or `su -c`.
  - **Signal** — Raw source of hook scripts and `entry:` values.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — Claude Opus.

- **Check** — Local hooks that reimplement built-in `pre-commit-hooks` checks (trailing-whitespace, end-of-file-fixer, merge-conflict markers, large-file check) are flagged.
  - **Signal** — Parsed YAML `id:` fields plus heuristic entry inspection.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

---

## 6. Final Rules File

# Pre-Commit Hooks: Rules

**Scope:** Git pre-commit hooks configured via the `pre-commit` framework or as local scripts invoked by it. Applies to formatters, linters, validators, and structural checks that run on `git commit`.

**Audience:** Engineers authoring or reviewing pre-commit configurations, and AI coding assistants generating hook configurations.

## Framework & Structure

- **Use the `pre-commit` framework** rather than hand-rolled `.git/hooks/` scripts. The framework handles staging isolation, per-language environments, and caching correctly.
- **Commit a single `.pre-commit-config.yaml` at the repository root.** This is the discoverable source of truth for what runs on commit.
- **Pin every hook `rev` to an immutable tag or full commit SHA.** Never use floating references (`main`, `master`, `HEAD`, `develop`, `latest`, `stable`).
- **Set `minimum_pre_commit_version`** to a version you test in CI, so incompatibilities surface immediately.
- **Pin `language_version`** (or `default_language_version.python`) for language-specific hooks — do not rely on a machine's default interpreter.
- **Keep custom hook logic in version-controlled scripts** (e.g., `scripts/hooks/`) referenced by `entry:`. Do not embed complex shell logic (with `&&`, `||`, `|`, `;`, `$(...)`) inline in YAML.
- **Give every hook an explicit `id` and a human-readable `name`.** Failure output is only as clear as the hook names.
- **Do not duplicate hooks already provided by `pre-commit-hooks`** (trailing whitespace, EOF fixer, merge-conflict markers, large-file check).

## Scope & Correctness

- **Scope hooks to changed files, not the whole repository.** Per-commit work should be proportional to commit size.
- **Declare `files:`, `types:`, or `types_or:` on every hook** to constrain what it runs on.
- **Exclude generated and vendored directories** (`node_modules`, `dist`, `build`, `target`, `.venv`, `vendor`, `third_party`) at the top level or per-hook.
- **Default to `pass_filenames: true`.** Only use `pass_filenames: false` for genuinely repo-wide invariants, and justify it with a comment.
- **Operate on staged content only.** In custom scripts, use `git diff --cached --name-only --diff-filter=ACMR`; do not re-discover files with `find` or bare `git ls-files`.
- **Order formatters before linters** so linters see formatted code. Within a tier, prefer fastest-first for fail-fast feedback.
- **Hooks must be deterministic and idempotent.** Same input → same result; running twice should produce no additional changes.

## Safety

- **Do not perform network I/O in a pre-commit hook.** No `curl`, `wget`, `pip install`, `npm install`, `apt-get`, `brew`, `gem install`, `go get`. Hooks must work offline.
- **Do not require `sudo`, a password, or elevated privileges.**
- **Do not modify files outside the staged set.**
- **Do not run `git add` inside a hook.** Auto-staging hides changes from the developer.
- **Do not rewrite history, push, tag, or mutate refs** from a pre-commit hook (`git push`, `git commit`, `git reset --hard`, `git clean -fdx`, `git rebase`, `git tag`, `git update-ref`).
- **Do not use destructive shell commands** (`rm -rf`, `docker system prune`, `terraform destroy`).
- **Leave `git commit --no-verify` working.** Bypass is a legitimate escape hatch; enforce via CI instead.
- **Serialize file-mutating hooks** (Black, Prettier, gofmt, rustfmt, Ruff+`--fix`, ESLint+`--fix`, etc.) with `require_serial: true` to prevent race conditions.

## Error Handling

- **Shell hooks must start with `#!/usr/bin/env bash` (or appropriate shebang) followed by `set -euo pipefail`** and a safe `IFS`. (Relax `pipefail` for portable `/bin/sh` scripts.)
- **Exit non-zero on any failure.** Do not silence errors with `|| true`, `--exit-zero`, `exit 0` traps, or toggled `set +e`.
- **Failure messages must be actionable.** Include filename, line number, the specific issue, and — when applicable — the command to fix. "Lint failed" is useless; `app/x.py:42: unused import 'os' (run 'ruff check --fix')` is actionable.
- **Document every linter-rule disable** with a comment explaining why (e.g., `# noqa: E501 — long URLs are OK in comments`).

## Performance

- **Target total hook runtime under ~2–5 seconds on a typical commit.** Slower hooks get bypassed, which is worse than no hook.
- **Do not run full test suites in pre-commit.** Move them to `pre-push` or CI.
- **Do not run whole-repo type checking in pre-commit.** Move `mypy`, `pyright`, `tsc` to `pre-push` or CI.
- **Use tool caches** where supported (e.g., ESLint `--cache`) to speed up no-change runs.

## Developer Experience

- **Mirror pre-commit enforcement in CI** via `pre-commit run --all-files` (or `pre-commit.ci`). Divergence between local and CI produces unreproducible failures.
- **Document bootstrap in the repo README** — minimally, the command `pre-commit install` — or automate it via a setup script (`make setup`, `husky install` in `postinstall`, etc.).
- **Run `pre-commit autoupdate` on a regular cadence** (e.g., monthly), committing the result as a dedicated, reviewable PR.
- **Validate custom shell hook scripts with `shellcheck`** as a meta-hook or CI step.
- **If a hook is regularly bypassed, fix the hook** — revise the rule, scope it better, or remove it. Chronic `--no-verify` usage is a design signal, not a discipline problem.