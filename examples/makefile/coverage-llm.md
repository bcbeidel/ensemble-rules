## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Declare all non-file targets as .PHONY. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Provide a self-documenting help target that lists available targets. | Self-Documentation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Define variables at the top of the file for tools, paths, and flags. | Variables | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Set a strict shell (bash with -e / pipefail) for recipes. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Scope destructive commands (rm -rf) to validated project paths; never use unscoped deletes. | Safety | ✓ | ✓ | ✓ |  | ✓ | ✓ | 5 |
| Make help the default goal so bare `make` is safe/informative. | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Move long/complex recipe logic into external scripts. | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Prefer immediate (:=) assignment over deferred (=) unless deferral is intentional. | Variables | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Use tabs (not spaces) for recipe indentation. | Style | ✓ | ✓ | ✓ |  |  | ✓ | 4 |
| Use a standard set of public target names (build, test, lint, fmt, run, clean, deploy, ci). | Structure | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Annotate targets with `## description` comments consumed by help. | Self-Documentation | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Disable built-in implicit rules / suffixes for predictability. | Performance | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Provide a ci target (or keep CI and local commands in sync via make). | Tooling/UX | ✓ |  | ✓ |  |  |  | 2 |
| Keep target names lowercase with dashes. | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use $(MAKE) for recursive make invocations. | Structure | ✓ |  |  | ✓ |  |  | 2 |
| Guard destructive/deployment targets with explicit confirmation. | Safety |  |  | ✓ | ✓ |  | ✓ | 3 |
| Do not use sudo or curl|sh / global installs in recipes. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Use sentinel/marker files for expensive idempotent setup. | Correctness |  |  | ✓ | ✓ | ✓ |  | 3 |
| Use `set -o pipefail` (or equivalent) for piped commands. | Safety | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use ?= for variables that may be overridden by the environment. | Variables | ✓ |  |  | ✓ |  |  | 2 |
| Quote variable expansions in shell recipes. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Don't hide commands globally with `@` / .SILENT (show commands by default). | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Group related targets together with comments/sections. | Structure |  | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Keep recipes short (move long ones out). | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use .DELETE_ON_ERROR to avoid partial/corrupt outputs. | Correctness | ✓ |  |  |  |  |  | 1 |
| Use .ONESHELL so multi-line recipes share shell state. | Style | ✓ |  |  |  | ✓ |  | 2 |
| Do NOT use .ONESHELL (keep per-line shell semantics). | Style |  |  | ✓ |  |  |  | 1 |
| Use order-only prerequisites for directories. | Performance | ✓ |  |  |  |  | ✓ | 2 |
| Keep Makefile small; split into included .mk files when needed. | Tooling/UX | ✓ |  |  |  |  |  | 1 |
| Support developer overrides via `-include .env.mk` (or similar). | Variables | ✓ |  |  |  |  |  | 1 |
| Enable --warn-undefined-variables in MAKEFLAGS. | Safety |  |  | ✓ |  |  |  | 1 |
| Pin tool/image versions used in recipes. | Tooling/UX | ✓ |  | ✓ |  |  |  | 2 |
| Pin tool invocations to project-local paths (venv, node_modules). | Correctness |  |  | ✓ |  |  |  | 1 |
| Don't hardcode -j1; allow parallelism. | Performance | ✓ |  |  |  |  |  | 1 |
| Avoid top-level $(shell ...) for expensive commands. | Performance |  |  | ✓ | ✓ |  |  | 2 |
| Don't embed secrets in the Makefile. | Anti-Patterns |  |  | ✓ |  |  |  | 1 |
| Don't swallow errors with `|| true` without justification. | Error Handling |  |  | ✓ | ✓ |  | ✓ | 3 |
| Avoid `cd` in recipes (use $(MAKE) -C or absolute paths). | Correctness |  |  | ✓ | ✓ |  |  | 2 |
| Declare `.PRECIOUS` / `.SECONDARY` for intermediates worth keeping. | Performance |  |  |  | ✓ |  | ✓ | 2 |
| Avoid recursive `$(MAKE) -C subdir` for orchestration (prefer flat graph). | Structure |  |  | ✓ | ✓ |  |  | 2 |
| Escape literal shell `$` as `$$` in recipes. | Shell | | | | ✓ |  |  | 1 |
| Prefix helper/internal targets with `_`. | Style |  |  | ✓ | ✓ |  |  | 2 |
| Limit recipe/line length (e.g., 80 chars) with continuations. | Style |  |  |  |  |  | ✓ | 1 |
| Check command exit statuses explicitly (handle errors). | Error Handling |  | ✓ |  |  |  | ✓ | 2 |
| Don't use shell globbing (*.py) in recipes; use explicit lists. | Safety |  |  |  | ✓ |  |  | 1 |
| Invoke scripts explicitly (e.g., `bash scripts/x.sh`) with shebangs. | Correctness |  |  |  | ✓ |  |  | 1 |
| Provide a `check` target to verify required tools/env vars. | Safety | ✓ |  |  |  |  |  | 1 |

## Notes on clustering decisions

- "Set a strict shell" clusters gpt-5's `SHELL:=/bin/bash` + `.SHELLFLAGS:=-eu -o pipefail -c`, claude-opus's identical rule, grok's "prefix recipes with specific shell", gemini's "strict SHELL environment", and haiku's `set -e`/`.SHELLFLAGS := -e`. A stricter reading would split `set -e` (per-recipe) from setting a project-wide SHELL var; I merged them since they target the same failure mode.
- "pipefail for piped commands" is kept separate from the generic "strict shell" rule because haiku and gemini call it out specifically, and gpt-5/claude-opus fold it into SHELLFLAGS. I counted models that mention pipefail either way.
- ".ONESHELL" has a pro-row (gpt-5, gemini) and an explicit anti-row (claude-opus). These are opposing opinions so I did not collapse them.
- "Make help the default goal" vs "Provide a self-documenting help target" are adjacent but distinct: the former is about `.DEFAULT_GOAL`/first-target ordering, the latter about the target's existence/content. gpt-4o-mini and grok describe only the latter; gemini describes both via one rule (counted in both rows).
- "Standard target names" clusters gpt-5's explicit target list, claude-opus's lowercase-verb list, gemini's `build/test/lint/run/format/clean/deploy`, and grok's "descriptive target names." grok's rule is weaker (about descriptiveness, not a canonical set) — borderline inclusion.
- "Keep target names lowercase-with-dashes" is separated from the standard-names cluster because several models mention the naming shape without enumerating targets.
- "Scope destructive commands" merges: gpt-5 (scope clean to $(BUILD_DIR)), gpt-4o-mini (don't use dangerous `rm -rf` without confirmation), claude-opus (validate VAR before `rm -rf $(VAR)`), gemini (protect destructive `rm`), grok (don't wildcard rm without safeguards). Haiku doesn't have a matching rule at the Makefile level (its `|| true` rule is different).
- "Guard destructive/deployment targets with confirmation" is kept separate from the generic rm-safety rule because it targets `deploy`/`publish` specifically.
- "Move complex logic into scripts" and "Keep recipes short" overlap heavily; I kept them as two rows because some models emphasize a line-count threshold (haiku, claude-opus) and others emphasize the delegation-to-scripts principle (gemini, grok). A human could reasonably merge them.
- "Don't hide commands with @" clusters gemini's explicit anti-`@` rule, claude-opus's "no `@` except echo/printf", haiku's nuanced version, and gpt-5's "don't global-silence / use Q var." These share intent (visibility) even though the mechanisms differ.
- grok's "use order-only prerequisites for files that don't affect outcomes" was clustered with gpt-5's "order-only prereqs for directories" — same Make feature, slightly different framing.
- gpt-4o-mini's "don't mix variable definitions with recipe commands" was folded into the "variables at top" cluster.
- gpt-4o-mini's "utilize variables for frequently used commands and flags" was clustered with the broader "define variables for tools/paths/flags" rule rather than creating a DRY-specific row.