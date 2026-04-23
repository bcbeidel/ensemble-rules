# Synthesis of Python Scripts Best-Practices Guidance

## 1. Consensus Rules

### Structure & Entry Point

- **Start every script with `#!/usr/bin/env python3` as the shebang line.** Portable execution that respects the user's environment. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)*

- **Wrap executable logic in a `main()` function invoked via `if __name__ == "__main__":`.** Enables testing, importability, and prevents import-time side effects. *(substantively similar but differently worded across all 6 models — GPT-5 and Claude Opus specifically recommend `sys.exit(main())`)*

- **Provide a module-level docstring describing the script's purpose.** First orientation point for humans and tools. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Argument Parsing

- **Use `argparse` from the standard library for CLI argument parsing.** Stdlib-native, produces `--help`, handles validation. *(near-identical across all 6 models; all flag it as mildly contested vs. click/typer)*

- **Do not parse `sys.argv` manually instead of using a proper parser.** Manual parsing is fragile and lacks help/validation. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

### Error Handling & Exit Codes

- **Never use bare `except:` clauses; catch specific exception types.** Bare except hides bugs and swallows `KeyboardInterrupt`. *(near-identical across all 6 models)*

- **Return 0 on success and non-zero on failure via `sys.exit()`.** Contract with shells, cron, and CI pipelines. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Use context managers (`with` statements) for files and other resources.** Guarantees cleanup on exceptions. *(substantively similar across GPT-5, Claude Opus, Gemini, Grok)*

### I/O

- **Write data output to stdout and logs/errors to stderr.** Enables composition in Unix pipelines. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Specify `encoding="utf-8"` explicitly on every text-mode `open()` call.** Default encoding is platform-dependent and causes silent corruption. *(near-identical across GPT-5, Claude Opus)*

- **Use `pathlib.Path` instead of `os.path` string manipulation.** Clearer, safer, cross-platform. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### Safety

- **Never pass `shell=True` to `subprocess` calls, especially with interpolated input.** Shell injection risk; pass an argument list instead. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Never use `eval` or `exec` on external input.** Trivial code-injection vector. *(near-identical across GPT-5, Claude Opus, GPT-4o-mini)*

- **Validate user inputs before performing destructive operations.** Fail fast, fail loud, fail before damage. *(substantively similar across Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)*

### Dependencies

- **Prefer the Python standard library over third-party packages.** Minimizes deployment friction and dependency surface. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **If third-party dependencies are required, declare them explicitly (requirements.txt, PEP 723 inline metadata, or top-of-file comment).** Scripts must be reproducible on a fresh machine. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Do not keep unused imports.** Reduces confusion and load time. *(substantively similar across GPT-5, Grok)*

### Style

- **Add type hints to function signatures.** Documentation that doesn't drift; enables static analysis. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok — all flag as mildly contested)*

- **Follow PEP 8 / use an automated formatter (black, ruff).** Eliminates style bikeshedding. *(substantively similar across GPT-5, Claude Haiku, Gemini, Grok, GPT-4o-mini)*

- **Prefer f-strings over `%` or `.format()`.** More readable, faster, less error-prone. *(near-identical across GPT-5, Claude Opus)*

- **Do not use wildcard imports (`from x import *`).** Pollutes namespace and impedes analysis. *(substantively similar across GPT-5, Claude Haiku)*

### Performance

- **Stream large files instead of loading them into memory.** Prevents OOM on files larger than the author imagined. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

## 2. Strong Minority Rules

- **Handle `KeyboardInterrupt` gracefully and exit with code 130 (no traceback).** *(Claude Opus, Claude Haiku)* — A script that prints a traceback on Ctrl+C is user-hostile; this is a small investment with high UX payoff.

- **Handle `BrokenPipeError`/SIGPIPE when writing to closed pipes.** *(GPT-5)* — Specific but real failure mode when scripts are used with `head`, `less`, etc.

- **Set the executable bit (`chmod +x`) on scripts with a shebang.** *(GPT-5, Claude Opus)* — A shebang without `+x` is a lie; worth mechanically enforcing.

- **Keep scripts under ~500 lines; convert to a package beyond that.** *(Claude Opus, Claude Haiku)* — The single-file-script pattern breaks down past a threshold; useful warning even if arbitrary.

- **Use `tempfile` for temporary files; never construct `/tmp/foo_{pid}` paths by hand.** *(GPT-5, Claude Opus)* — Race conditions and symlink attacks are real and easy to avoid.

- **Defer heavy imports (pandas, numpy, torch, requests) into the functions that use them.** *(Claude Opus, Claude Haiku)* — Cold-start time matters for CLI tools invoked frequently.

- **For YAML, use `yaml.safe_load` rather than `yaml.load`.** *(GPT-5)* — Specific but critical security guidance with a clean deterministic check.

- **Offer `--dry-run` flags for destructive operations.** *(Claude Opus, Claude Haiku)* — Low-cost safety net; worth keeping as normative guidance.

- **Support `-v/--verbose` and `-q/--quiet` flags for operator-controlled logging noise.** *(GPT-5)* — Standard CLI ergonomics that pays off when scripts reach production.

- **Use `logging` (not `print`) for operational messages, configured to stderr.** *(GPT-5, Claude Opus, Claude Haiku)* — Only a minority flagged this distinctly from the stdout/stderr rule; worth keeping.

- **Don't use mutable default arguments.** *(Claude Opus)* — Classic Python footgun, easily checked by `ruff B006`.

- **Don't hardcode paths, credentials, or hostnames.** *(Gemini, Claude Haiku, Grok)* — Portability and security; worth stating explicitly.

## 3. Divergences

### Max line length

- **Positions:** GPT-5 recommends Black's 88; GPT-4o-mini implies PEP 8's 79; Grok specifies 88; others defer to "PEP 8" or "black" without a number.
- **Synthesis:** Use an automated formatter and don't bikeshed the number. Default to Black's 88 as the de-facto modern standard. This is a contested rule; teams may pick 100 or 120 without harm.

### Catching `Exception` broadly at top level

- **Positions:** Claude Opus forbids `except Exception:` without re-raising. Claude Haiku says catch all exceptions in `main()` and map to exit codes. Gemini forbids catching `Exception`. Grok flags catching broad exceptions as contested.
- **Synthesis:** Recommend a single top-level `try/except Exception` in `main()` that logs and returns a non-zero exit code, *and* explicitly re-catches `KeyboardInterrupt` separately. Bare `except:` is never acceptable. Inside business logic, catch specific exceptions.

### Script length cap

- **Positions:** Claude Opus says ~500 lines; GPT-4o-mini says 300; Claude Haiku says ≤1000; others are silent.
- **Synthesis:** State the principle ("when a script grows past a few hundred lines, convert to a package") without a rigid line count. If a check is wanted, set it at 500 with file-level override allowed.

### Function length cap

- **Positions:** Claude Haiku says ≤50 lines. Others silent.
- **Synthesis:** Include as advisory, not strict. Arbitrary line counts generate false positives for legitimate long functions.

### Inline PEP 723 metadata vs. separate requirements.txt

- **Positions:** Claude Opus prefers PEP 723 inline metadata. GPT-5 prefers colocated requirements.txt. Others say "document dependencies" without specifying.
- **Synthesis:** Either is acceptable; the requirement is that dependencies are *explicit and machine-readable*. PEP 723 is newer and more self-contained; requirements.txt is more widely supported. Recommend PEP 723 for new scripts, accept both.

### Printing tracebacks to users

- **Positions:** GPT-5 says suppress tracebacks by default, gate behind `--debug`. Claude Opus says let unexpected exceptions propagate — tracebacks are diagnostic gold.
- **Synthesis:** These aren't as opposed as they look. For *expected* failure modes (missing file, bad input), print a clean stderr message and exit non-zero. For *unexpected* exceptions, letting them propagate is acceptable; wrapping `main()` in `try/except Exception` to log-and-exit is also acceptable as long as the message includes enough info. Don't swallow tracebacks silently.

### Checking whether `argparse` is used

- **Positions:** GPT-5, Gemini, Grok, Claude Haiku all mandate argparse. Claude Opus accepts `click`/`typer` for complex CLIs.
- **Synthesis:** Use `argparse` unless you have a concrete reason (subcommands, rich help, shell completion) to reach for a third-party parser. The rule favors stdlib-first.

## 4. Notable Omissions

- **Shebang line:** Universal except GPT-4o-mini covered it but without the full `#!/usr/bin/env python3` specificity that others insisted on.

- **stdout/stderr separation:** Absent from GPT-4o-mini and Grok. This is a core Unix composability rule; its absence is surprising given how many failure modes it addresses.

- **`shell=True` prohibition:** Covered by everyone except GPT-4o-mini, which mentioned safety generically but omitted this specific, high-impact rule.

- **`pathlib` over `os.path`:** Absent from GPT-4o-mini, Gemini, and Grok. This is widely agreed-upon modern practice; the omissions likely reflect shorter rule lists rather than disagreement.

- **UTF-8 encoding on `open()`:** Only GPT-5 and Claude Opus raised this. Given the frequency of silent encoding bugs in production, its absence from the other four is a real gap.

- **Explicit exit codes:** GPT-4o-mini omits this. Exit-code discipline is fundamental to script reliability in automation.

- **Context managers for resources:** Missing from GPT-4o-mini and Claude Haiku's explicit rules (Haiku mentions it indirectly).

- **Wildcard import prohibition:** Only GPT-5 and Claude Haiku list it. Everyone agrees in practice; it's a universally-applied lint rule.

## 5. Shared Deterministic Checks

### Clustered (multi-model) checks

- **Check** — Verify the file's first line is exactly `#!/usr/bin/env python3`.
  - **Signal** — Raw source text, first line.
  - **Tool candidate** — ad-hoc (trivial regex/string check).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — GPT-5 and Claude Opus gate the check on whether the file has the executable bit set (reducing false positives on library-like `.py` files). Grok adds a stricter "no hardcoded paths" sub-check. Others apply it universally.

- **Check** — Verify the module contains a top-level `if __name__ == "__main__":` guard that invokes `main()` (ideally via `sys.exit(main())`).
  - **Signal** — Parsed AST; top-level `If` node with a `Compare` against `"__main__"`.
  - **Tool candidate** — ad-hoc AST walker; partial coverage by pylint conventions.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — GPT-5 and Claude Opus specifically require `sys.exit(main())`; Claude Haiku requires a `main` function exist separately; Gemini checks that non-def top-level statements live inside the guard.

- **Check** — Flag any `ExceptHandler` AST node whose `type` is `None` (bare `except:`).
  - **Signal** — Parsed AST.
  - **Tool candidate** — `ruff E722` / `pycodestyle E722`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini.
  - **Variance** — Claude Opus additionally flags `except Exception:` without a re-raise (`ruff BLE001`); Gemini agrees. Others only flag truly bare except.

- **Check** — Flag any `subprocess.run/call/check_output/Popen` call with the keyword `shell=True`.
  - **Signal** — Parsed AST; Call node keywords.
  - **Tool candidate** — `bandit B602`, `ruff S602`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — GPT-5 and Claude Opus escalate severity when the first argument is an f-string or formatted string (interpolation); Claude Haiku and Gemini flag unconditionally.

- **Check** — Flag `open()` calls in text mode that omit the `encoding=` keyword.
  - **Signal** — Parsed AST; Call node to `open` with mode string lacking `"b"`.
  - **Tool candidate** — `ruff PLW1514`, `flake8-encodings`.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Substantively agreed; only two models raised it.

- **Check** — Flag uses of `os.path.*` functions, suggesting `pathlib` instead.
  - **Signal** — Parsed AST; attribute accesses on `os.path`.
  - **Tool candidate** — `ruff PTH100–PTH124` (flake8-use-pathlib).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Models agree on substance; GPT-5 softens to "at minimum ensure `pathlib` is imported if `os.path` is used".

- **Check** — Verify the module starts with a string-literal expression (module docstring).
  - **Signal** — Parsed AST; `body[0]` is an `ast.Expr` wrapping an `ast.Constant(str)`.
  - **Tool candidate** — `ruff D100` / `pydocstyle D100`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Agreed on substance; none try to evaluate docstring quality.

- **Check** — Flag any `ImportFrom` node that imports `*` (wildcard import).
  - **Signal** — Parsed AST.
  - **Tool candidate** — `ruff F403`.
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — None.

- **Check** — Flag unused imports.
  - **Signal** — Static name-resolution over AST.
  - **Tool candidate** — `ruff F401` / `pyflakes`.
  - **Raised by** — GPT-5, Grok.
  - **Variance** — None; both delegate to ruff/flake8.

- **Check** — Verify the module imports `argparse` (or equivalent) when it accesses `sys.argv` beyond `sys.argv[0]`.
  - **Signal** — Parsed AST.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — Grok explicitly pairs "uses `sys.argv`" with "imports `argparse`"; others flag manual parsing more loosely.

- **Check** — For every `parser.add_argument()` call, require a `help=` keyword with a non-empty string.
  - **Signal** — Parsed AST; Call node keywords.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — None; both acknowledge they can't check help *quality*, only presence.

- **Check** — Enforce PEP 8 / formatter compliance and line-length limits.
  - **Signal** — Raw source text; output of formatter/linter.
  - **Tool candidate** — `black --check`, `ruff format --check`, `ruff E501`, `flake8`.
  - **Raised by** — GPT-5, Gemini, Grok, GPT-4o-mini, Claude Haiku.
  - **Variance** — Line-length value varies (88 most common; 79/100 also seen); choice of formatter varies (Black vs. Ruff).

- **Check** — Flag `eval()` and `exec()` calls.
  - **Signal** — Parsed AST; Call nodes with func Name `eval`/`exec`.
  - **Tool candidate** — `bandit B307`, `ruff S307`.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — None.

- **Check** — When any non-stdlib module is imported, verify that dependencies are declared (requirements.txt present in the same directory, PEP 723 `# /// script` block, or documented in a top-of-file comment).
  - **Signal** — Parsed AST imports ∩ `sys.stdlib_module_names`; filesystem or raw source.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — GPT-5 requires `requirements.txt`; Claude Opus requires PEP 723 inline block; Gemini accepts comment-based documentation. Underlying intent agreed; mechanism differs.

- **Check** — Flag `f = open(...)` calls whose result is not used inside a `with` statement.
  - **Signal** — Parsed AST.
  - **Tool candidate** — `ruff SIM115`.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — None.

### Singleton checks (one model but generally useful)

- **Check** — Verify a top-level `__version__ = "X.Y.Z"` string assignment exists.
  - **Signal** — Parsed AST top-level Assign.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Verify the file has the executable bit set when it starts with a shebang.
  - **Signal** — `os.stat().st_mode` with `stat.S_IXUSR`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, Claude Opus (overlaps shebang check).

- **Check** — Flag any mutation of `sys.path` (assignment, `.append`, `.insert`).
  - **Signal** — Parsed AST.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Flag relative imports (`ImportFrom` with `level > 0`).
  - **Signal** — Parsed AST.
  - **Tool candidate** — ad-hoc (covered by several lint rules but script-specific).
  - **Raised by** — GPT-5.

- **Check** — Flag mutable default arguments in function signatures.
  - **Signal** — Parsed AST; `FunctionDef.args.defaults` containing List/Dict/Set literals.
  - **Tool candidate** — `ruff B006`.
  - **Raised by** — Claude Opus.

- **Check** — Flag `yaml.load(...)` without an explicit `SafeLoader`; recommend `yaml.safe_load`.
  - **Signal** — Parsed AST.
  - **Tool candidate** — `bandit B506`.
  - **Raised by** — GPT-5.

- **Check** — Flag string literals starting with `/tmp/` or `/var/tmp/` passed to file-opening or path calls.
  - **Signal** — Parsed AST string literals in argument positions.
  - **Tool candidate** — `bandit B108`, `ruff S108`.
  - **Raised by** — Claude Opus.

- **Check** — Flag `%`-format and `.format()` string operations where f-strings apply.
  - **Signal** — Parsed AST; `BinOp(op=Mod)` on string constants, `.format` calls on string literals.
  - **Tool candidate** — `ruff UP031`, `UP032` (pyupgrade).
  - **Raised by** — GPT-5, Claude Opus.

- **Check** — Flag top-level executable statements outside of imports, class/function defs, constant assignments, and the `__main__` guard.
  - **Signal** — Parsed AST top-level body.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verify function signatures have type annotations on parameters and return.
  - **Signal** — Parsed AST FunctionDef nodes.
  - **Tool candidate** — `ruff ANN` rules, `mypy --disallow-untyped-defs`.
  - **Raised by** — Claude Haiku, Gemini, GPT-5 (restricted to `main`).

- **Check** — Verify `subprocess.run` calls include `check=True` or their result is inspected.
  - **Signal** — Parsed AST.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Flag names that shadow builtins (`list`, `id`, `file`, etc.) at module scope.
  - **Signal** — Parsed AST.
  - **Tool candidate** — `ruff A001`/`A002` (flake8-builtins).
  - **Raised by** — GPT-5.

- **Check** — Flag `.read()` on a file handle followed by `.splitlines()` or used inside a `for` loop (prefer line iteration).
  - **Signal** — Parsed AST; advisory only.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

---

## 6. Final Rules File

# Python Scripts — Rules

**Scope.** Standalone single-file Python 3 scripts used as CLI tools, automation helpers, and data-wrangling utilities. Not libraries, not multi-module applications.

**Audience.** Engineers and AI coding assistants producing and reviewing such scripts.

**Principles.** Make scripts predictable to run, easy to read under pressure, safe by default, and honest about failure. Prefer the standard library. Fail loud and early. Play nicely with Unix pipelines.

## Structure & Entry Point

- Start the file with exactly `#!/usr/bin/env python3`. Portable across systems where `python` may be Python 2 or absent.
- Set the executable bit (`chmod +x`) on scripts meant to be invoked directly. A shebang without `+x` is a lie.
- Include a module docstring as the first statement, describing the script's purpose and one example invocation. It is often the only documentation.
- Wrap execution in `def main(argv: Sequence[str] | None = None) -> int:` and call it from `if __name__ == "__main__": sys.exit(main())`. Enables testing, clean exit codes, and prevents import-time side effects.
- Keep all executable logic under the `__main__` guard or inside functions. Top-level statements should be limited to imports, constant assignments, class/function definitions, and the guard itself.
- Do not mutate `sys.path`. Hidden import paths create non-reproducible behavior.
- Do not use relative imports in scripts. Relative imports are fragile outside packages.
- When a script grows past a few hundred lines or acquires non-trivial shared state, convert it to a package. Single-file discipline breaks down past that threshold.

## Dependencies

- Prefer the standard library over third-party packages. `argparse`, `pathlib`, `json`, `csv`, `subprocess`, `logging`, `http.client`, and `tempfile` cover most scripting needs.
- Declare third-party dependencies explicitly — either via PEP 723 inline script metadata (`# /// script` block) or a colocated `requirements.txt`. Scripts must be reproducible on a fresh machine.
- Pin third-party requirements with `==` or `~=` when using `requirements.txt`.
- Remove unused imports. They confuse readers and bloat load time.

## Arguments & I/O

- Use `argparse` for CLI parsing. Do not reach for `click`/`typer` unless you need subcommands, rich help, or shell completion. *(contested)*
- Do not parse `sys.argv` manually; `argparse` gives you `--help`, types, and validation for free.
- Give every argument a non-empty `help=` string.
- Use `type=` and `choices=` to validate arguments where applicable.
- Support `--version` where meaningful, printing `<prog> <version>` and exiting 0.
- Support `-v/--verbose` (repeatable) and `-q/--quiet` to control log verbosity.
- Do not prompt interactively unless an explicit `-i/--interactive` flag is given. Scripts should be pipeline-friendly by default.
- Write primary data output to stdout. Write logs, errors, and prompts to stderr. Anything else breaks shell pipelines.
- Support `-` as a filename meaning stdin/stdout where it makes sense.
- Specify `encoding="utf-8"` on every text-mode `open()` call. Default encoding is platform-dependent and a known source of silent corruption.
- Use `sys.stdin.buffer` / `sys.stdout.buffer` for binary data.
- Use `pathlib.Path` instead of `os.path` string manipulation.

## Error Handling & Exit Codes

- Return 0 on success, non-zero on failure. Use exit code 2 for CLI usage errors (argparse default), 1 for general runtime failure, 130 for `KeyboardInterrupt`.
- Never use a bare `except:`. It swallows `KeyboardInterrupt` and `SystemExit` and hides real bugs.
- Catch specific exceptions where possible (e.g., `FileNotFoundError`, `ValueError`). A top-level `try/except Exception` in `main()` that logs and returns non-zero is acceptable.
- Catch `KeyboardInterrupt` at the top level and exit with code 130 without printing a traceback. A script that dumps a traceback on Ctrl+C is user-hostile.
- Handle `BrokenPipeError` (SIGPIPE) gracefully when writing to a closed pipe.
- Validate inputs early; fail before doing destructive work.
- Use context managers (`with` statements) for files, locks, subprocess pipes, and other resources. Guarantees cleanup on exceptions.
- Log a concise error message to stderr before exiting non-zero; gate full tracebacks behind `--debug` or `--verbose`.

## Logging & Output

- Use the `logging` module (configured to stderr) for any script with verbosity flags or more than trivial output. Reserve `print` for primary data output to stdout.
- Include timestamps and log level for scripts that run in automation or long-running contexts.
- Do not log secrets, tokens, API keys, or full environment dumps. Assume logs are world-readable.

## Safety

- Never call `subprocess.run` (or `call`/`Popen`/`check_output`) with `shell=True`, especially with interpolated input. Pass an argument list.
- Pass arguments to `subprocess.run([...], check=True)` as a list; inspect the return code or use `check=True`.
- If `shell=True` is truly required, quote interpolated values with `shlex.quote` and document why in a comment.
- Never use `eval` or `exec` on external input.
- For YAML, use `yaml.safe_load`, not `yaml.load`.
- Use `tempfile` (`TemporaryDirectory`, `NamedTemporaryFile`, `mkstemp`) for temporary files. Never construct `/tmp/foo_{pid}` paths by hand — race conditions and symlink attacks are real.
- Do not hardcode paths, credentials, or hostnames. Pass them as arguments or read from environment variables (`os.environ.get()` with a default).
- Offer `--dry-run` and `--yes` flags for destructive filesystem or network operations.

## Style

- Format with an automated formatter (Black or `ruff format`). Default to line length 88. *(contested)*
- Add type hints to function signatures, at minimum on `main()` and script boundaries. They are documentation that doesn't drift. *(contested)*
- Keep imports grouped at the top (stdlib / third-party / local), with deferred heavy imports (pandas, numpy, torch, requests) inside the functions that use them to preserve cold-start time.
- Prefer f-strings over `%` formatting or `.format()`.
- Do not use wildcard imports (`from x import *`).
- Do not shadow builtins (`list`, `id`, `file`, etc.).
- Do not use mutable default arguments. Use `None` and assign inside.
- Use descriptive names; avoid single-letter names except for loop counters or standard math contexts.

## Performance

- Stream large files line-by-line or in chunks; do not `.read()` entire files into memory when you will iterate over them anyway.
- Use `''.join(...)` or `io.StringIO` instead of `+=` in loops for large string assembly.
- Avoid materializing large generators with `list()` or `set()` unless you need the materialization.
- Do not reach for `asyncio`, `threading`, or `multiprocessing` without a measured reason.

## Testing & Reproducibility

- Keep `main()` importable and side-effect-free at module scope so it can be tested.
- Pin the required Python version via PEP 723 `requires-python` or a top-of-file comment. "Works on 3.12" is not the same as "requires 3.10+".
- Log diagnostic counters (file counts, row counts, duration) for any batch operation.