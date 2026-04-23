# Makefile Best Practices: Multi-Model Synthesis

## 1. Consensus Rules

### Structure & Default Behavior

- **Declare all non-file targets as `.PHONY`.** Prevents targets from being silently skipped when a file of the same name exists. *(substantively similar but differently worded across GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok — strong convergence)*

- **Provide a self-documenting `help` target that lists available targets and descriptions.** Onboarding and discovery without reading the whole file. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini; also in GPT-4o-mini and Grok)*

- **Make `help` the default goal (via `.DEFAULT_GOAL := help` or by ordering).** Bare `make` should be informative, never destructive. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Group related targets with comments or blank lines.** Aids scanning and comprehension. *(substantively similar across GPT-4o-mini, Claude Haiku, Gemini, Grok)*

### Variables

- **Define configurable variables at the top of the file.** Single location for customization and overrides. *(substantively similar across GPT-5, Claude Haiku, Gemini, Grok)*

- **Prefer `:=` (immediate) over `=` (deferred) for simple assignment; use `?=` for overridable defaults.** Deterministic assignment prevents surprising re-evaluation and environment leaks. *(near-identical framing across GPT-5, Claude Opus, Gemini; also present in Claude Haiku)*

- **Extract repeated commands/flags into named variables.** Prevents drift when one copy is updated and another is not. *(substantively similar across GPT-4o-mini, Claude Haiku, Grok)*

### Shell & Recipe Safety

- **Set a strict shell: `SHELL := bash` with `.SHELLFLAGS := -eu -o pipefail -c` (or equivalent `set -e`/`set -o pipefail`).** Default `/bin/sh` varies; without `pipefail` a failure inside a pipeline is silently swallowed. *(near-identical wording across GPT-5, Claude Opus, Gemini; same substance in Claude Haiku and Grok)*

- **Keep recipes short; move logic longer than ~5–10 lines into scripts under `scripts/`.** Make is a poor scripting language; complex logic belongs in testable shell files. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Use `$(MAKE)` instead of literal `make` for recursive invocations.** Propagates flags and job counts. *(substantively similar across GPT-5, Claude Haiku)*

### Safety

- **Never write unguarded `rm -rf $(VAR)`; validate variables and scope cleanup to known build dirs.** An unset or mistyped variable turns cleanup into catastrophic deletion. *(substantively similar across GPT-5, GPT-4o-mini, Claude Opus, Gemini, Grok)*

- **Do not use `sudo`, install tools globally, or pipe remote scripts to shell in recipes.** Dev workflows must not mutate the user's machine or introduce supply-chain risk. *(substantively similar across GPT-5 and Claude Opus)*

### Style

- **Indent recipes with real tabs, not spaces.** Non-negotiable Make syntax. *(substantively similar across GPT-5, GPT-4o-mini [inverted], Claude Opus, Claude Haiku, Grok)* — note GPT-4o-mini got this backwards (see Divergences).

- **Use lowercase, hyphenated, verb-like target names (`build`, `test`, `lint`, `fmt`, `run`, `clean`, `deploy`).** Consistent, shell-friendly, muscle-memory-compatible across repos. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Document each public target with a `## description` comment that drives `make help`.** Keeps documentation and code in sync. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Performance & Portability

- **Disable built-in implicit rules (`MAKEFLAGS += --no-builtin-rules` and/or `.SUFFIXES:`).** Prevents surprising legacy inference rules and speeds up no-op runs. *(substantively similar across GPT-5, Claude Opus)*

- **Use sentinel files for expensive idempotent setup (e.g., `.venv/.installed`).** Avoids re-running slow installs on every invocation. *(substantively similar across Claude Opus, Claude Haiku, Gemini)*

- **Don't call expensive `$(shell ...)` at parse time.** Top-level shells run on every `make` invocation, including `make help`. *(substantively similar across Claude Opus, Claude Haiku)*

### Single Source of Truth

- **CI should invoke the same `make` targets developers run locally (provide a `ci` target).** If the Makefile isn't the source of truth, it's a lie. *(substantively similar across GPT-5, Claude Opus)*

---

## 2. Strong Minority Rules

- **Add `.DELETE_ON_ERROR:`.** *(GPT-5 only.)* Prevents Make from leaving corrupted partial outputs on failure. Cheap, universally beneficial, no real downsides — worth including.

- **Set `MAKEFLAGS += --warn-undefined-variables`.** *(Claude Opus only.)* Catches typos like `$(BULID_DIR)` that would otherwise expand to empty and turn `rm -rf $(BUILD_DIR)/` into `rm -rf /`. High-value safety rule.

- **Guard destructive targets (`deploy`, `publish`, `release`) with an explicit confirmation variable (e.g., `CONFIRM=1`).** *(Claude Opus.)* Accidental deploys are expensive; the cost of typing `CONFIRM=1` is trivial.

- **Prefix internal/helper targets with `_` and omit the `##` comment.** *(Claude Opus, Claude Haiku.)* Cleanly distinguishes public API from implementation details and keeps `make help` output clean.

- **Don't use `@` to silence commands except for `echo`/`printf`.** *(Claude Opus, Gemini.)* Hiding commands obscures failures during debugging; prefer `make -s` when quiet output is desired.

- **Avoid `|| true` to swallow failures unless explicitly commented.** *(Claude Opus, Claude Haiku.)* Silent error suppression is how bad builds ship.

- **Support developer overrides via `-include .env.mk` (or similar).** *(GPT-5 only.)* Lets contributors tweak without editing the tracked file.

- **Use order-only prerequisites for directory creation (`target: | $(BUILD_DIR)`).** *(GPT-5, Grok.)* Creates dirs once without retriggering work; a well-known Make idiom worth codifying.

- **Avoid recursive Make (`$(MAKE) -C subdir`) for workflow orchestration; prefer a flat target graph.** *(Claude Opus, Claude Haiku.)* Recursive Make breaks parallelism and dependency tracking.

- **Pin tool invocations to project-local versions (`./node_modules/.bin/eslint`, `.venv/bin/pytest`).** *(Claude Opus.)* Prevents CI/local drift from global tool versions.

- **Don't embed secrets in the Makefile; use `include .env` with `.env` gitignored.** *(Claude Opus.)* Obvious in retrospect, but worth writing down.

---

## 3. Divergences

### Tabs vs. spaces for recipe indentation
- **GPT-5, Claude Opus, Claude Haiku, Gemini, Grok:** Use tabs (Make syntax requires it).
- **GPT-4o-mini:** "Don't use tab characters. Always use spaces for consistent indentation."
- **Recommendation:** Use tabs. GPT-4o-mini is simply wrong — Make fundamentally requires a tab to start a recipe line (unless `.RECIPEPREFIX` is changed, which is itself discouraged). This is not a matter of taste.

### `.ONESHELL:` directive
- **GPT-5, Gemini:** Prefer `.ONESHELL:` — avoids per-line subshell footguns (lost `cd`, lost state).
- **Claude Opus:** Explicitly don't use it — it changes semantics readers expect.
- **Others:** Silent.
- **Recommendation:** Contested. Default to **not using it** (Claude Opus's position) because the traditional per-line shell model is what reviewers expect, and the fix — use `&& \` or move logic to a script — aligns with the broader "keep recipes short" rule. Teams that prefer `.ONESHELL` should adopt it uniformly and document it.

### Hiding commands with `@`
- **GPT-5, Claude Opus, Gemini:** Don't hide by default; visibility aids debugging. Use `@` only for `echo`/`printf`, or gate silence behind a `Q`/`VERBOSE` variable.
- **Claude Haiku:** Use `@` to suppress echoing of self-documenting commands (inverted framing — same conclusion).
- **Recommendation:** Don't use `@` except on `echo`/`printf`/`:`. Users who want quiet output can run `make -s`.

### POSIX `sh` vs bash
- **Claude Opus, GPT-5, Gemini:** Pin bash explicitly and require GNU Make ≥ 4. Modern productivity outweighs POSIX purity.
- **Claude Haiku, Grok:** Default to POSIX `sh`; document any bash-isms.
- **Recommendation:** For developer-workflow Makefiles in a typical repo, pin bash and state the requirement. POSIX strictness is only worth the cost for broadly distributed tooling.

### Variable assignment strictness
- **Claude Opus, GPT-5, Gemini, Claude Haiku:** Default to `:=`; `=` only for intentional deferral.
- **Grok:** Use `$(shell ...)` sparingly (adjacent concern, no direct disagreement).
- **Recommendation:** Default to `:=` and `?=`; treat `=` as requiring an explanatory comment.

### Line-length limits
- **Grok:** Limit to 80 characters with `\` continuation.
- **Others:** No opinion.
- **Recommendation:** Not a Makefile-specific rule; defer to repo-wide style. Don't invent a Makefile-specific limit.

---

## 4. Notable Omissions

- **`.PHONY` declarations** — universally agreed as essential, but **GPT-4o-mini** buried it as "use phony targets" without explaining what that means or how to declare them. The single most important correctness rule in Makefiles deserves more than a sentence.

- **Strict shell flags (`set -e`, `pipefail`)** — consensus across 5 of 6 models, but **GPT-4o-mini** omits this entirely, instead suggesting "check command exit statuses with conditional statements" — a much weaker and more error-prone practice.

- **Tab indentation** — **Gemini** omits this, presumably treating it as obvious; however given that GPT-4o-mini got it backwards, making it explicit is worthwhile.

- **`$(MAKE)` for recursive invocation** — mentioned by GPT-5 and Claude Haiku only; absent from Claude Opus, Gemini, GPT-4o-mini, Grok. Claude Opus actively recommends avoiding recursive Make, which partly explains its omission — but when recursion is needed, `$(MAKE)` is non-negotiable.

- **Disable built-in rules** — only GPT-5 and Claude Opus call this out; absent from Gemini, Claude Haiku, GPT-4o-mini, Grok. This is a legitimate oversight — built-in implicit rules are a real source of surprise.

- **Sentinel files for expensive setup** — mentioned by Claude Opus, Claude Haiku, Gemini. Absent from GPT-5, GPT-4o-mini, Grok. A well-known idiom that belongs in any serious Makefile guide.

- **CI/local parity** — Claude Opus and GPT-5 are explicit; others don't state it. This is arguably *the* reason to have a Makefile at all.

---

## 5. Shared Deterministic Checks

### Multi-model shared checks

- **Check** — Every non-file target defined in the Makefile is listed in a `.PHONY` declaration.
  - **Signal** — Parsed Makefile target list and `.PHONY` prerequisite list.
  - **Tool candidate** — `checkmake` (partial); otherwise ad-hoc regex/parser.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — GPT-5 and Grok scope the check to a known set of public targets; Claude Opus and Gemini check all targets and require a filesystem probe or allowlist to exclude legitimate file-producing ones. Claude Haiku notes the false-positive risk explicitly.

- **Check** — The Makefile contains `.DEFAULT_GOAL := help` (or equivalent ordering that makes `help` the first target).
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — GPT-5 and Claude Opus check for the explicit `.DEFAULT_GOAL` assignment; Gemini checks that `help` is the first-defined target. Either satisfies the intent; a combined check is more robust.

- **Check** — A `help` target is defined and its recipe parses `##`-annotated comments from the Makefile.
  - **Signal** — Raw source text (target definition + recipe body).
  - **Tool candidate** — ad-hoc grep for `help:` + `$(MAKEFILE_LIST)` + `##` tokens.
  - **Raised by** — GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — GPT-5 and Claude Opus require the recipe to reference `$(MAKEFILE_LIST)` and `##`; GPT-4o-mini and Claude Haiku only require the target to exist; Gemini notes the self-documentation check is brittle.

- **Check** — `SHELL` is set to bash and `.SHELLFLAGS` includes `-e`, `-u` (optionally), `-o pipefail`, and `-c`.
  - **Signal** — Raw source text (final `SHELL` and `.SHELLFLAGS` assignments).
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — GPT-5 and Claude Opus require `-eu -o pipefail -c`; Gemini requires `-e` and `-o pipefail` (not `-u`); Claude Haiku accepts either the shell flag or an in-recipe `set -e`.

- **Check** — Every public target has a `## description` comment on its definition line.
  - **Signal** — Raw source text, per-target line.
  - **Tool candidate** — ad-hoc regex `^<name>:.*##\s+.+$`.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Agreed on substance. Both note that description quality cannot be validated mechanically.

- **Check** — All target definitions use tab indentation for recipe lines.
  - **Signal** — Raw bytes of recipe lines.
  - **Tool candidate** — Make itself rejects space-indented recipes with "missing separator"; `.editorconfig` validation via editorconfig-checker.
  - **Raised by** — GPT-5, Claude Opus, Grok.
  - **Variance** — Agreed on substance.

- **Check** — `rm -rf` in recipes must be followed by a non-empty guard variable, reference a known build-dir variable, or contain a literal safe path.
  - **Signal** — Recipe text; optional allowlist of safe path prefixes.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus, GPT-4o-mini, Grok.
  - **Variance** — GPT-5 scopes to the `clean:` target; Claude Opus checks every recipe for `rm -rf $(VAR)` with no guard; Grok checks wildcard `rm` patterns. Union of all three is appropriate.

- **Check** — Bare `make` (not `$(MAKE)`) does not appear as a command token in recipe lines.
  - **Signal** — Recipe text.
  - **Tool candidate** — ad-hoc regex with word boundaries.
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — GPT-5 gives explicit regex guidance; Claude Haiku states the rule without validation detail.

- **Check** — Top-level variable assignments use `:=` or `?=`, not bare `=`, unless annotated with an explanatory comment.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — All three acknowledge the rule is contested; Claude Opus requires an inline `deferred`/`recursive` comment to opt out.

- **Check** — Bash-specific syntax in recipes (`[[`, `<(…)`, arrays, `{1..n}`) is only permitted when `SHELL` is explicitly set to bash.
  - **Signal** — Recipe text + `SHELL` assignment; optionally `shellcheck --shell=sh` on extracted recipes.
  - **Tool candidate** — `shellcheck` (requires extracting recipe bodies into shell files first).
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — Both acknowledge the extraction is imperfect.

### Singleton checks worth preserving

- **Check** — `.DELETE_ON_ERROR:` is present in the Makefile.
  - **Signal** — Raw source text grep.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — GPT-5.

- **Check** — `MAKEFLAGS += --warn-undefined-variables` is present.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — Claude Opus.

- **Check** — `MAKEFLAGS += --no-builtin-rules` and/or `.SUFFIXES:` (with no suffixes) are present.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — GPT-5, Claude Opus.

- **Check** — No `.SILENT:` directive and no `-s`/`--silent` in `MAKEFLAGS`.
  - **Signal** — Raw source text.
  - **Tool candidate** — ad-hoc grep.
  - **Raised by** — GPT-5.

- **Check** — Recipes do not invoke `sudo`, `npm install -g`, unscoped `pip install`, or `curl | sh`/`curl | bash`.
  - **Signal** — Recipe text.
  - **Tool candidate** — ad-hoc regex; `shellcheck` on extracted recipes catches some.
  - **Raised by** — GPT-5, Claude Opus.

- **Check** — Each recipe exceeding ~5–10 tab-indented lines is flagged for extraction into `scripts/`.
  - **Signal** — Recipe line counts per target.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.

- **Check** — Targets named `deploy`, `publish`, `release`, or `prod-*` begin their recipe with a confirmation-variable guard.
  - **Signal** — Target name + first recipe line.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — `@`-prefixed recipe lines begin only with `echo`, `printf`, or `:`.
  - **Signal** — Recipe text.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — Claude Opus.

- **Check** — `|| true` in recipe lines requires an adjacent explanatory comment.
  - **Signal** — Recipe text + surrounding comment lines.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.

- **Check** — No `$(shell ...)` appears outside recipe bodies (or only against an allowlist of cheap commands like `git rev-parse`, `uname`).
  - **Signal** — Parsed Makefile; classification of lines as top-level vs recipe.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Public target names match `^[a-z][a-z0-9-]*$`.
  - **Signal** — Parsed target list.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus.

- **Check** — Secret-like assignments (`TOKEN|SECRET|KEY|PASSWORD` holding high-entropy values) are not present.
  - **Signal** — Raw source text.
  - **Tool candidate** — `gitleaks`, `trufflehog`.
  - **Raised by** — Claude Opus.

- **Check** — Recipe line count per target does not exceed a configurable threshold (5–10).
  - **Signal** — Recipe text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.

---

## 6. Final Rules File

# Makefile Rules: Developer Workflow Orchestration

**Scope.** Top-level `Makefile` that orchestrates developer workflows (build, test, lint, format, run, deploy, clean) for a single repository. Not for compiling C/C++ source trees or large multi-module builds.

**Audience.** Engineers writing or reviewing Makefiles; AI assistants generating or modifying them.

**Assumed environment.** GNU Make ≥ 4.0, `bash` available at `/usr/bin/env bash`. State this assumption in a comment at the top of the Makefile.

---

## Structure

- **Put variable definitions at the top of the file, before any target.** Readers should see configuration before behavior.
- **Group related targets by lifecycle (setup → build → test → lint/format → run → deploy → clean) with section comments.** Predictable order aids scanning.
- **Make `help` the default goal via `.DEFAULT_GOAL := help` and define it as the first target.** Bare `make` must never build, deploy, or delete.
- **Provide a `help` target that parses `## description` comments from target lines and prints them aligned.** Hand-maintained help rots; generated help stays honest.
- **Declare `.PHONY:` for every target that is not a real file.** Without this, a stray file named `test` silently breaks `make test`.
- **Keep recipes to ~5 lines or fewer; move longer logic into `scripts/` and invoke from the target.** Make is not a scripting language.
- **Avoid recursive Make (`$(MAKE) -C subdir`) for workflow orchestration; prefer a flat target graph.** Recursive Make breaks parallelism and dependency tracking.
- **When recursion is genuinely needed, invoke it as `$(MAKE)`, not literal `make`.** Propagates flags and job counts.
- **Name public targets as lowercase, hyphenated verbs: `build`, `test`, `lint`, `fmt`, `run`, `deploy`, `clean`.** Consistency across repos lowers cognitive load.
- **Prefix internal/helper targets with `_` and omit the `##` description.** Makes the public surface obvious.

## Shell & Recipe Safety

- **Set `SHELL := bash` and `.SHELLFLAGS := -eu -o pipefail -c`.** Default `/bin/sh` varies; without `pipefail` failures inside pipelines are silently swallowed.
- **Set `MAKEFLAGS += --warn-undefined-variables`.** Catches typos that would otherwise expand to empty strings (`rm -rf $(BULID_DIR)/` → `rm -rf /`).
- **Set `MAKEFLAGS += --no-builtin-rules` and add a bare `.SUFFIXES:` line.** Disables decades of legacy C/Fortran inference rules that cause surprising behavior.
- **Add `.DELETE_ON_ERROR:`.** Prevents partial or corrupted outputs from lingering after a failed recipe.
- **Indent recipe lines with real tabs, not spaces.** Non-negotiable Make syntax; configure `.editorconfig` with `[Makefile] indent_style = tab` to enforce.
- **Write one logical shell command per recipe line; use `\` continuations for multi-line commands.** Each recipe line runs in a fresh shell — `cd foo` on line 1 has no effect on line 2.
- **Escape literal `$` in recipes as `$$` to defer expansion to the shell.** Single `$` expands at Make parse time.

## Variables

- **Define user-configurable variables at the top using `?=` for overridable defaults (`PYTHON ?= python3`, `BUILD_DIR ?= build`).** Respects environment and CI overrides.
- **Use `:=` for simple immediate assignment; use bare `=` only when deferred expansion is deliberate and documented with a comment.** Recursive assignment re-evaluates on every reference and causes surprising performance and ordering bugs.
- **Extract any command or flag string repeated across targets into a named variable.** Prevents drift when one copy is updated and another is not.
- **Quote all variable expansions in recipes (`"$(VAR)"` not `$(VAR)`).** Unquoted paths with spaces or empty variables silently corrupt commands.
- **Support developer overrides via `-include .env.mk` (or `include .env`); keep the override file `.gitignore`d.** Local tweaks without repo-wide impact.
- **Never call expensive commands via `$(shell …)` at the top level.** Top-level shells run on every `make` invocation, including `make help`. Cheap invocations like `git rev-parse` are acceptable.

## Safety

- **Scope `clean` to `$(BUILD_DIR)` and an explicit allowlist of artifacts; never use unscoped `rm -rf`.** A typo or unset variable can turn cleanup into `rm -rf /`.
- **Guard destructive targets (`deploy`, `publish`, `release`) with an explicit confirmation such as `CONFIRM=1`.** Accidental deploys are expensive.
- **Do not use `sudo`, `npm install -g`, or unscoped `pip install` in recipes.** Dev workflows must not mutate the user's machine; use venvs or local `node_modules`.
- **Do not execute remote scripts via `curl | sh` or `curl | bash`.** Supply-chain risk; require explicit, versioned installation steps.
- **Do not embed secrets, tokens, or environment-specific URLs in the Makefile.** Use `.env` loaded via `-include .env`, with `.env` gitignored.
- **Pin tool invocations to project-local versions (`./node_modules/.bin/eslint`, `.venv/bin/pytest`, `poetry run`, `uv run`) rather than relying on `$PATH`.** Global tool versions drift and make CI diverge from local.

## Style & Self-Documentation

- **Annotate every public target with a `## description` comment on its definition line.** Powers `make help` and documents the public API.
- **Do not use `@` to silence commands except for `echo`, `printf`, or `:`.** Hiding commands obscures failures during debugging; users who want quiet output can run `make -s`.
- **Do not use `.ONESHELL:`.** It changes the per-line-shell semantics every Make reader expects. (Contested: teams that adopt `.ONESHELL` uniformly and document it may ignore this rule.)
- **Do not catch errors with `|| true` unless accompanied by a comment explaining why.** Swallowing failures is how bad builds ship.

## Correctness & Performance

- **Make CI invoke the same `make` targets developers run locally; provide a `ci` target that is the single source of truth.** If the Makefile isn't the source of truth, it's a lie.
- **Use order-only prerequisites for directory creation (`target: | $(BUILD_DIR)`).** Creates directories once without retriggering work.
- **Use sentinel files (e.g., `.venv/.installed`, `.stamp-deps`) for expensive idempotent setup steps.** Avoids re-running slow installs on every invocation.
- **Declare file-producing targets against their actual output files, not phony names.** Lets Make skip work correctly when inputs haven't changed.
- **Do not hardcode `-j1`; allow parallelism. Use `.NOTPARALLEL` per-target only when strict ordering is required.** Honor the user's available cores.
- **Do not redefine built-in variables (`MAKE`, `CURDIR`, etc.) except `SHELL` and `.SHELLFLAGS` as specified.** Surprising to readers and tools.

## Size & Modularity

- **Keep the top-level Makefile under ~300 lines; split details into included `*.mk` files.** Improves navigation and reuse.

---

### Contested rules (adopt or reject per team, but be consistent)

- `.ONESHELL:` — off by default here; some teams prefer it to avoid `&& \` continuations.
- Bash vs POSIX `sh` — this file pins bash; broadly distributed tooling may require strict POSIX instead.
- Line-length limits — not enforced here; defer to repo-wide style.
- Default to `:=` over `=` — strongly recommended but not universal.