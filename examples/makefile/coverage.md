# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Do not hide commands with the `@` prefix.** | Shell Commands |  |  |  |  | ✓ |  | 1 |
| **(contested) Use immediately-expanded variables (`:=`) over deferred variables (`=`).** | Variables |  |  |  |  | ✓ |  | 1 |
| **Annotate every public target with a `## description` comment on the target line.** Targets without a description are invisible to `help` and should not exist as public entry points | Self-Documentation |  |  | ✓ |  |  |  | 1 |
| **Assign user-configurable variables near the top of the file (e.g., `PYTHON := python3`, `COVERAGE_THRESHOLD := 80`).** Signals intent and allows overrides via command line (`make test PYTHON=python3.11`) | Variables & DRY |  |  |  | ✓ |  |  | 1 |
| **Assume POSIX shell (`/bin/sh`) by default; document any GNU make extensions or bash-specific syntax.** Improves portability across Linux distributions, macOS, and containers | Portability |  |  |  | ✓ |  |  | 1 |
| **Avoid calling external programs (e.g., `$(shell git rev-parse HEAD)`) in top-level variable assignments if the value will be used rarely.** Slows down every `make` invocation; defer to recipe-time if possible | Performance & Efficiency |  |  |  | ✓ |  |  | 1 |
| **Avoid using `cd` in recipes; use `$(MAKE) -C dir` or path-qualified commands instead.** Prevents accidental directory switches that affect subsequent recipes or confuse readers | Shell & Recipe Safety |  |  |  | ✓ |  |  | 1 |
| **Avoid using shell globbing (e.g., `*.py`) in recipes; use explicit file lists or tool-driven discovery instead.** Globbing at Makefile parse time is fragile and non-incremental | Safety & Correctness |  |  |  | ✓ |  |  | 1 |
| **Declare `.PHONY:` for every target that is not a real file.** Without this, a stray file named `test` silently breaks `make test` | Structure |  |  | ✓ |  |  |  | 1 |
| **Declare all non-file targets as `.PHONY`.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Declare all phony targets with `.PHONY` at the top of the file.** Prevents accidental conflicts between target names and file names | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Declare file-producing targets against their actual output files, not phony names.** Lets Make skip work correctly when inputs haven't changed | Correctness |  |  | ✓ |  |  |  | 1 |
| **Define a `.help` or `help` target that lists and describes all user-facing targets.** New contributors should be able to run `make help` and understand what's available without reading the file | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Define a default target (`.DEFAULT_GOAL`), or ensure the first non-hidden target is the most common action (usually `help`).** Running `make` with no arguments should be safe and informative, never destructive | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Define a self-documenting `help` target as the first target.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Define common tool paths as variables (e.g., `PYTHON := python3`, `DOCKER := docker`) to allow overrides.** Accommodates environments where tools are in non-standard locations or named differently | Portability |  |  |  | ✓ |  |  | 1 |
| **Define repeated commands or flags as named variables, and reference them consistently throughout.** Prevents command drift when a test flag or linter configuration must change | Variables & DRY |  |  |  | ✓ |  |  | 1 |
| **Define user-configurable variables at the top of the file.** | Variables |  |  |  |  | ✓ |  | 1 |
| **Do not suppress errors with `\|\| true` unless there is an explicit, documented reason (e.g., a cleanup target that should not fail the build).** Silent error suppression hides real problems | Shell & Recipe Safety |  |  |  | ✓ |  |  | 1 |
| **Document non-obvious variable requirements or assumptions in comments.** (e.g., `# Requires DEPLOY_ENV to be set (staging\|prod)`, `# Assumes Docker is running`) | Safety & Correctness |  |  |  | ✓ |  |  | 1 |
| **Don't catch errors with `\|\| true` unless the failure is genuinely acceptable and commented.** Swallowing failures is how bad builds ship | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Don't embed secrets, tokens, or environment-specific URLs in the Makefile.** Use `.env` files loaded via `include .env` with `.env` gitignored | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Don't redefine built-in variables like `MAKE`, `SHELL` (except as specified above), or `CURDIR`.** Surprising to readers and tools | Correctness |  |  | ✓ |  |  |  | 1 |
| **Don't run `$(shell ...)` for expensive commands at the top level; defer to recipes.** Top-level `$(shell)` runs on every `make` invocation, including `make help` | Performance |  |  | ✓ |  |  |  | 1 |
| **Don't use `.ONESHELL:`.** (contested) It hides the per-line shell semantics that every Make reader already expects and surprises reviewers | Style |  |  | ✓ |  |  |  | 1 |
| **Don't use `@` to silence commands except for `echo` and `printf`.** Hiding the command obscures failures during debugging | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| **Ensure `clean` targets only remove files from the project directory.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Ensure all scripts invoked by the Makefile have a shebang line and are executable, or invoke them explicitly (e.g., `bash scripts/deploy.sh` not `./scripts/deploy.sh`).** Reduces platform-specific failures and makes dependencies clear | Safety & Correctness |  |  |  | ✓ |  |  | 1 |
| **Escape literal `$$` in recipes to produce a single `$` in the shell.** Distinguishes between Makefile variable expansion (single `$`) and shell variable expansion (double `$$`) | Shell & Recipe Safety |  |  |  | ✓ |  |  | 1 |
| **For slow operations (e.g., container builds, database migrations), provide both an incremental target (depends on a `.built` marker file) and a `--force` override.** Balances speed and correctness | Performance & Efficiency |  |  |  | ✓ |  |  | 1 |
| **For targets that mutate external state (e.g., `deploy`, `publish`), require an explicit confirmation or flag.** (contested) Prevents accidental destructive operations; e.g., `make deploy CONFIRM=yes` | Safety & Correctness |  |  |  | ✓ |  |  | 1 |
| **Group related targets logically using comments and blank lines (e.g., "# Build targets", "# Test targets").** Reduces cognitive load when scanning the file | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Group related targets together.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Group targets by lifecycle: setup, build, test, lint/format, run, deploy, clean.** Predictable order aids scanning | Structure |  |  | ✓ |  |  |  | 1 |
| **Guard destructive targets (`deploy`, `publish`, `release`) with an explicit confirmation or `CONFIRM=1` env var.** Accidental deploys are expensive | Safety |  |  | ✓ |  |  |  | 1 |
| **If a target is meant to always run (e.g., `make fmt` reformats code in place), mark it `.PHONY` and document why.** Clarifies intention and prevents accidental caching | Error Handling & Robustness |  |  |  | ✓ |  |  | 1 |
| **Implement `make help` that parses `target: ## description` comments and prints them aligned.** Hand-maintained help text always rots; generated help stays honest | Self-Documentation |  |  | ✓ |  |  |  | 1 |
| **Keep recipes short and task-focused; shell scripts longer than ~10 lines belong in a dedicated shell script file in `scripts/`.** Avoids turning the Makefile into an unmaintainable monolith | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Keep recipes to 5 lines or fewer; move longer logic into `scripts/`.** Make is not a scripting language; shell-in-recipes is unreadable and untestable | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep target names to a single verb and object where possible (e.g., `format-py`, not `run-the-python-formatter`).** Brevity aids discoverability and muscle memory | Style & Readability |  |  |  | ✓ |  |  | 1 |
| **Keep targets focused on a single logical action.** | Targets |  |  |  |  | ✓ |  | 1 |
| **Make CI invoke the same `make` targets a developer runs locally.** If the Makefile is not the source of truth, it is a lie | Correctness |  |  | ✓ |  |  |  | 1 |
| **Make `help` the default target via `.DEFAULT_GOAL := help`.** Bare `make` must never build, deploy, or delete | Structure |  |  | ✓ |  |  |  | 1 |
| **Make file-producing targets depend on their prerequisites, and use `.PHONY` only for targets that have no output file.** Enables correct incremental builds and prevents spurious re-runs | Error Handling & Robustness |  |  |  | ✓ |  |  | 1 |
| **Move complex logic into dedicated scripts.** | Shell Commands |  |  |  |  | ✓ |  | 1 |
| **Name targets as lowercase verbs: `build`, `test`, `lint`, `fmt`, `run`, `deploy`, `clean`.** Consistent naming across repos lowers cognitive load | Structure |  |  | ✓ |  |  |  | 1 |
| **Never mutate global state in recipes (no `pip install` outside a venv, no `npm install -g`, no `sudo`).** Dev workflow must not alter the user's machine | Safety |  |  | ✓ |  |  |  | 1 |
| **Never write `rm -rf $(VAR)` without validating `VAR` is non-empty and inside the repo.** A typo or override turns cleanup into `rm -rf /` | Safety |  |  | ✓ |  |  |  | 1 |
| **Only mark independent targets as parallel-safe; document which targets support `-j`.** Most dev workflows have hidden ordering dependencies through shared state (ports, files) | Performance |  |  | ✓ |  |  |  | 1 |
| **Pin tool invocations to project-local versions (`./node_modules/.bin/eslint`, `.venv/bin/pytest`, `go run tool@version`).** Global tool versions drift and make CI diverge from local | Correctness |  |  | ✓ |  |  |  | 1 |
| **Prefix helper/internal targets with an underscore (e.g., `_check-env`, `_build-deps`) to signal they are not meant for direct user invocation.** Distinguishes public API from implementation details | Style & Readability |  |  |  | ✓ |  |  | 1 |
| **Prefix internal/helper targets with `_` and omit the `##` comment.** Makes the public surface obvious | Self-Documentation |  |  | ✓ |  |  |  | 1 |
| **Prefix shell recipes with `set -e` (or `.SHELLFLAGS := -e`) to stop on first error.** Prevents silent failures when an intermediate command fails but the script continues | Shell & Recipe Safety |  |  |  | ✓ |  |  | 1 |
| **Protect destructive commands like `rm`.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Provide a `.PRECIOUS` rule for intermediate files that should not be auto-deleted (e.g., generated code that users may inspect).** Respects the principle of least surprise | Error Handling & Robustness |  |  |  | ✓ |  |  | 1 |
| **Put each prerequisite on its own line for targets with more than two prerequisites.** Diffs stay clean and readable | Style |  |  | ✓ |  |  |  | 1 |
| **Put variable definitions at the top, before any target.** Readers should see configuration before behavior | Structure |  |  | ✓ |  |  |  | 1 |
| **Quote all variable expansions in recipes: `"$(VAR)"` not `$(VAR)`.** Unquoted paths with spaces or empty variables silently corrupt commands | Safety |  |  | ✓ |  |  |  | 1 |
| **Quote variable references to handle spaces and special characters: use `"$(VAR)"` in shell contexts.** Prevents word-splitting bugs in file paths or arguments containing spaces | Variables & DRY |  |  |  | ✓ |  |  | 1 |
| **Set `MAKEFLAGS += --no-builtin-rules` and `.SUFFIXES:`.** Disables decades of legacy C/Fortran inference rules that cause surprising behavior | Safety |  |  | ✓ |  |  |  | 1 |
| **Set `MAKEFLAGS += --warn-undefined-variables`.** Catches typos that would otherwise expand to empty strings | Safety |  |  | ✓ |  |  |  | 1 |
| **Set `SHELL := bash` and `.SHELLFLAGS := -eu -o pipefail -c`.** Default `/bin/sh` varies; without `pipefail` a failure in a pipeline is silently swallowed | Safety |  |  | ✓ |  |  |  | 1 |
| **Set a strict `SHELL` environment.** | Shell Commands |  |  |  |  | ✓ |  | 1 |
| **Set the default goal to `help`.** | Structure |  |  |  |  | ✓ |  | 1 |
| **Use `##` comments above a target to generate `help` output; parse and display these comments in the help target.** Keeps documentation and code in sync | Style & Readability |  |  |  | ✓ |  |  | 1 |
| **Use `$(MAKE)` instead of literal `make` when invoking make recursively.** Respects environment variables and flags passed to the parent make | Portability |  |  |  | ✓ |  |  | 1 |
| **Use `.ONESHELL` to enable multi-line recipes.** | Shell Commands |  |  |  |  | ✓ |  | 1 |
| **Use `.PHONY` targets for commands that don't produce files, and use file-based targets (with real outputs) for build products.** Ensures make's incremental semantics work correctly | Performance & Efficiency |  |  |  | ✓ |  |  | 1 |
| **Use `.PHONY` targets that are lowercase, hyphenated, and descriptive: `test-unit`, `lint-python`, `deploy-staging`.** Aligns with shell command conventions and clarifies intent | Style & Readability |  |  |  | ✓ |  |  | 1 |
| **Use `.SHELL := /bin/bash` if you rely on bash-isms (e.g., `set -o pipefail`, `[[` conditionals); otherwise default to `/bin/sh` for portability.** Declares assumptions explicitly and fails obviously on systems lacking bash | Shell & Recipe Safety |  |  |  | ✓ |  |  | 1 |
| **Use `:=` for simple variables; use `=` only when deferred expansion is deliberate.** Recursive assignment (`=`) re-evaluates on every reference and causes surprising performance and ordering bugs | Style |  |  | ✓ |  |  |  | 1 |
| **Use `?=` (conditional assignment) for variables that might already be set by the environment.** Respects shell environment and CI overrides | Variables & DRY |  |  |  | ✓ |  |  | 1 |
| **Use `@` to suppress echoing of recipes that are self-documenting (e.g., `@echo "Running tests…"`); otherwise let recipes echo by default.** Aids debugging and shows what's actually being run | Error Handling & Robustness |  |  |  | ✓ |  |  | 1 |
| **Use `set -o pipefail` in recipes that chain commands with pipes.** Ensures that a failure in a piped command is caught (e.g., `grep foo \| awk` won't hide a grep failure) | Shell & Recipe Safety |  |  |  | ✓ |  |  | 1 |
| **Use a consistent variable naming convention (e.g., `UPPER_CASE` for configuration, `lower_case` for computed values).** Reduces confusion about what is user-configurable vs | Structure & Organization |  |  |  | ✓ |  |  | 1 |
| **Use a flat target graph; avoid recursive `$(MAKE) -C subdir` for workflow orchestration.** Recursive Make breaks parallelism and dependency tracking | Structure |  |  | ✓ |  |  |  | 1 |
| **Use a standard set of target names.** | Targets |  |  |  |  | ✓ |  | 1 |
| **Use sentinel files (e.g., `.venv/.installed`) for expensive idempotent setup steps.** (contested) Avoids re-running slow installs on every invocation | Correctness |  |  | ✓ |  |  |  | 1 |
| **Use sentinel files for expensive one-time setup.** | Targets |  |  |  |  | ✓ |  | 1 |
| **Use tabs (not spaces) for recipe indentation, and configure `.editorconfig` to enforce it.** Non-negotiable Make syntax; editors silently break this | Style |  |  | ✓ |  |  |  | 1 |
| **Use variables for all tools, flags, and important paths.** | Variables |  |  |  |  | ✓ |  | 1 |
| **Write one logical command per recipe line; do not chain with `&&` across multiple physical lines without a trailing `\`.** Each recipe line is a fresh shell — `cd foo` on line 1 has no effect on line 2 | Style |  |  | ✓ |  |  |  | 1 |
| Add “.DELETE_ON_ERROR:” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid non-portable shell features unless you explicitly set SHELL accordingly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare all convenience targets (including the public ones) as .PHONY | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define MKDIR_P ?= mkdir -p and use $(RM) and $(MKDIR_P) in recipes, not raw rm/mkdir | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define at least these public targets: build, test, lint, fmt, run, clean, help, and ci | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Disable built-in implicit rules: add “.SUFFIXES:” and/or “MAKEFLAGS += -rR” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do cache results where possible, such as with Make's .SECONDARY special target | Performance |  |  |  |  |  | ✓ | 1 |
| Do choose between using shell commands directly or relying on built-in Makefile functions based on your team's context and preference | Contested |  | ✓ |  |  |  |  | 1 |
| Do clearly define targets that remove files (e.g., `clean`) | Safety |  | ✓ |  |  |  |  | 1 |
| Do declare all dependencies explicitly to prevent race conditions in parallel builds | Safety |  |  |  |  |  | ✓ | 1 |
| Do define a "help" target that lists all available targets and their descriptions to make the Makefile self-documenting | Structure |  |  |  |  |  | ✓ | 1 |
| Do ensure every target has a clear, descriptive name (e.g., "format-code" instead of "fmt") | Targets |  |  |  |  |  | ✓ | 1 |
| Do explicitly check command exit statuses with conditional statements | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do include a "clean" target that prompts for confirmation before deleting files | Safety |  |  |  |  |  | ✓ | 1 |
| Do include error checks in recipes, such as setting `set -e` in Bash to exit on failure | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do indent recipes with tabs, not spaces | Style |  |  |  |  |  | ✓ | 1 |
| Do limit lines to 80 characters and use line continuations (\) for long commands | Style |  |  |  |  |  | ✓ | 1 |
| Do mark non-file-producing targets as .PHONY (e.g., build, test) | Targets |  |  |  |  |  | ✓ | 1 |
| Do not execute remote scripts via “curl \| sh” (or bash) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use .SILENT or -s globally; show commands by default and gate silence behind a Q/VERBOSE toggle | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use sudo in recipes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize targets logically, grouping related ones (e.g., build-related first) and using comments to separate sections | Structure |  |  |  |  |  | ✓ | 1 |
| Do organize the Makefile into clearly defined sections for each target | Structure |  | ✓ |  |  |  |  | 1 |
| Do prefix recipes with a specific shell (e.g., /bin/bash) if portability is a concern | Commands |  |  |  |  |  | ✓ | 1 |
| Do provide a `make help` target that lists all available commands | Style |  | ✓ |  |  |  |  | 1 |
| Do use Make's error directives (e.g., `-` prefix for ignoring errors) only when absolutely necessary | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do use `$(shell ...)` sparingly for external commands; prefer Make's built-in functions | Commands |  |  |  |  |  | ✓ | 1 |
| Do use order-only prerequisites for files that don't affect build outcomes (e.g., directories) | Performance |  |  |  |  |  | ✓ | 1 |
| Do use phony targets to avoid conflict with actual files | Structure |  | ✓ |  |  |  |  | 1 |
| Do use variables for paths, commands, and flags to avoid hard-coded values | Structure |  |  |  |  |  | ✓ | 1 |
| Do utilize variables for frequently used commands and flags | Performance |  | ✓ |  |  |  |  | 1 |
| Document every public target with a trailing “## One-line description” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't define overlapping or redundant targets that duplicate work | Performance |  |  |  |  |  | ✓ | 1 |
| Don't define targets that always run (e.g., without dependencies); use prerequisites instead | Targets |  |  |  |  |  | ✓ | 1 |
| Don't embed complex logic in recipes; use external scripts for multi-line operations | Commands |  |  |  |  |  | ✓ | 1 |
| Don't ignore command failures; always handle them explicitly | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't use ambiguous variable names; always use descriptive ones (e.g., BUILD_DIR instead of bd) | Style |  |  |  |  |  | ✓ | 1 |
| Don't use wildcards (e.g., *) in rm commands without safeguards | Safety |  |  |  |  |  | ✓ | 1 |
| Don’t hard-code paths or settings that may change across environments | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t hardcode “-j1”; allow parallelism by default and make recipes concurrency-safe | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t hide commands by default; use a Q variable (e.g., Q := @ when VERBOSE=0) to toggle quiet mode | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don’t ignore the output of commands | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t mix variable definitions with recipe commands | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t use dangerous shell commands (`rm -rf`) without clear confirmation | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t use tab characters | Style |  | ✓ |  |  |  |  | 1 |
| Enable strict shell flags for all recipes (SHELL := /bin/bash and .SHELLFLAGS := -eu -o pipefail -c) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Export only the variables required by child processes; do not use export-all | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep target names lowercase-with-dashes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the top-level Makefile under ~300 lines; split details into included .mk files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make help the default goal via “.DEFAULT_GOAL := help” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin versions of external tools used in recipes (e.g., docker images with tags, lang-specific installers) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer “.ONESHELL:” so multi-line recipes share shell state without brittle line continuations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a self-documenting “help” target that lists targets annotated with “## …” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a “check” target to verify required tools and env vars before work | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a “ci” target that runs the exact checks CI uses | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put overridable tool/path variables at the top using ?= (e.g., GO?=go, DOCKER?=docker, BUILD_DIR?=build) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope “clean” to $(BUILD_DIR) and known artifacts; never use unscoped “rm -rf” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start each recipe line with a real tab (do not change RECIPEPREFIX) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Support developer overrides via “-include .env.mk” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use $(MAKE) for recursive Make invocations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use := for computed values and ?= for defaults; avoid = unless you intentionally need lazy evaluation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use order-only prerequisites for directories (e.g., target: \| $(BUILD_DIR)) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

