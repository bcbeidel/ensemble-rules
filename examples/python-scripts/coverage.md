# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **Do** prefer the standard library over third-party packages | Dependencies |  |  |  |  | ✓ | ✓ | 2 |
| (contested) **Do not use a package manager (pip, poetry) within a script.** The script should not modify the host environment; let the user handle dependency installation upfront | Dependencies |  |  |  | ✓ |  |  | 1 |
| **Annotate function signatures with types.** They are documentation that doesn't drift | Style |  |  | ✓ |  |  |  | 1 |
| **Avoid wildcard imports (`from module import *`).** Makes it impossible to tell where a name came from; use explicit imports | Code Quality and Style |  |  |  | ✓ |  |  | 1 |
| **Capture subprocess output with `subprocess.run(capture_output=True, text=True)` rather than shell redirection.** Reduces quoting errors and makes the intent explicit | Performance and Resource Management |  |  |  | ✓ |  |  | 1 |
| **Catch `KeyboardInterrupt` at the top level and exit with code 130 without a traceback.** A script that prints a traceback on Ctrl+C is user-hostile | Error Handling & Exit Codes |  |  | ✓ |  |  |  | 1 |
| **Catch all exceptions at the top level (in `main()`) and map them to exit codes.** Prevents tracebacks from confusing users and ensures automation can interpret the result | Error Handling and Exit Codes |  |  |  | ✓ |  |  | 1 |
| **Confirm or dry-run before destructive filesystem or network operations.** Offer `--dry-run` and `--yes` flags for anything that deletes or overwrites | Safety |  |  | ✓ |  |  |  | 1 |
| **Declare third-party dependencies inline using PEP 723 script metadata.** Makes the script self-contained and runnable via `uv run` / `pipx run` | Structure |  |  | ✓ |  |  |  | 1 |
| **Defer heavy imports inside functions if they are conditional or rarely used.** Reduces startup time for scripts that may fail early (bad arguments, missing files) | Structure and Entry Point |  |  |  | ✓ |  |  | 1 |
| **Defer imports of heavy modules (pandas, numpy, requests, ML libs) into the functions that use them.** Cold-start time matters for CLI tools | Performance |  |  | ✓ |  |  |  | 1 |
| **Define all imports at the module level, before any function definitions.** Clarifies dependencies upfront and catches import errors early | Structure and Entry Point |  |  |  | ✓ |  |  | 1 |
| **Define an argument parser as a separate function (`def get_parser()`) and call it in `main()`.** Allows testing and reuse of the parser; clarifies the CLI contract | Argument Parsing and Configuration |  |  |  | ✓ |  |  | 1 |
| **Do not hardcode absolute paths; use relative paths or environment variables.** Scripts should be portable across machines and deployment contexts | Safety and Portability |  |  |  | ✓ |  |  | 1 |
| **Do not invoke external commands in a loop without good reason; batch them instead.** Each subprocess invocation has overhead; batch operations reduce latency by 10–100x | Performance and Resource Management |  |  |  | ✓ |  |  | 1 |
| **Do not print sensitive information (passwords, tokens, API keys) to stdout or stderr.** Prevents accidental leaks in logs and debug output | Logging and Output |  |  |  | ✓ |  |  | 1 |
| **Do** call the `main` function from within a `if __name__ == "__main__"` guard | Structure |  |  |  |  | ✓ |  | 1 |
| **Do** catch specific exceptions (e.g., `except FileNotFoundError:`) rather than generic `Exception` | Error Handling & Exit Codes |  |  |  |  | ✓ |  | 1 |
| **Do** document required third-party dependencies in a comment block at the top of the file | Dependencies |  |  |  |  | ✓ |  | 1 |
| **Do** exit with a non-zero status code on failure using `sys.exit(1)` | Error Handling & Exit Codes |  |  |  |  | ✓ |  | 1 |
| **Do** format code with an automated formatter like `black` | Style & Readability |  |  |  |  | ✓ |  | 1 |
| **Do** get confirmation from the user before performing destructive operations (e.g., deleting files) | Safety |  |  |  |  | ✓ |  | 1 |
| **Do** include a module-level docstring explaining the script's purpose and usage | Structure |  |  |  |  | ✓ |  | 1 |
| **Do** isolate script logic within a `main` function | Structure |  |  |  |  | ✓ |  | 1 |
| **Do** pass command-line arguments as a list to `subprocess.run` (e.g., `["ls", "-l", "file"]`) | Safety |  |  |  |  | ✓ |  | 1 |
| **Do** start executable scripts with a shebang line: `#!/usr/bin/env python3` | Structure |  |  |  |  | ✓ |  | 1 |
| **Do** use `try...finally` or context managers (`with open(...)`) to guarantee resource cleanup | Error Handling & Exit Codes |  |  |  |  | ✓ |  | 1 |
| **Do** use the `argparse` module for parsing command-line arguments | Arguments & I/O |  |  |  |  | ✓ |  | 1 |
| **Do** use type hints for function signatures | Style & Readability |  |  |  |  | ✓ |  | 1 |
| **Do** write all logs, errors, and user-facing prompts to `stderr` | Arguments & I/O |  |  |  |  | ✓ |  | 1 |
| **Do** write primary data output to `stdout` | Arguments & I/O |  |  |  |  | ✓ |  | 1 |
| **Document all external dependencies in a comment or docstring at the top of the script.** Allows users and AI assistants to understand what needs to be installed | Dependencies |  |  |  | ✓ |  |  | 1 |
| **Don't log secrets, tokens, or full environment dumps.** Assume logs are world-readable | Safety |  |  | ✓ |  |  |  | 1 |
| **Don't reach for `asyncio`, `threading`, or `multiprocessing` without a measured reason.** Concurrency bugs cost more than the speedup in a one-shot script | Performance |  |  | ✓ |  |  |  | 1 |
| **Don't reach for `click`/`typer` unless you need subcommands, rich help, or shell completion.** Stdlib parsers are sufficient for 90% of scripts | Arguments & I/O |  |  | ✓ |  |  |  | 1 |
| **Don't use mutable default arguments.** Classic footgun; use `None` and assign inside | Style |  |  | ✓ |  |  |  | 1 |
| **Don't** hardcode file paths, credentials, or hostnames; pass them as arguments or environment variables | Arguments & I/O |  |  |  |  | ✓ |  | 1 |
| **Don't** use `shell=True` with `subprocess.run` or `subprocess.Popen` | Safety |  |  |  |  | ✓ |  | 1 |
| **Don't** use a bare `except:` clause | Error Handling & Exit Codes |  |  |  |  | ✓ |  | 1 |
| **Don't** use global variables for passing state between functions | Style & Readability |  |  |  |  | ✓ |  | 1 |
| **Follow PEP 8 for style (naming, spacing, line length ≤100).** Consistency improves readability; use a formatter (black, autopep8) to avoid style debates | Code Quality and Style |  |  |  | ✓ |  |  | 1 |
| **For scripts that manage resources (files, processes, connections), use context managers (`with` statements).** Ensures cleanup even if an exception occurs | Error Handling and Exit Codes |  |  |  | ✓ |  |  | 1 |
| **For scripts that produce or modify files, include a `--dry-run` flag.** Allows users to preview changes before committing; reduces accidents and builds confidence | Testing and Reproducibility |  |  |  | ✓ |  |  | 1 |
| **Handle `KeyboardInterrupt` explicitly and exit cleanly with code 130.** Allows the user to interrupt long-running scripts without seeing a traceback | Error Handling and Exit Codes |  |  |  | ✓ |  |  | 1 |
| **If an external dependency is required, check for its import and exit with a clear error message if missing.** Prevents confusing ImportError tracebacks; guides the user toward installation | Dependencies |  |  |  | ✓ |  |  | 1 |
| **Include a module docstring at the top of the file describing the script's purpose and usage.** Makes the intent clear without reading the code; valuable for downstream maintainers | Code Quality and Style |  |  |  | ✓ |  |  | 1 |
| **Include a shebang line as the first line of the file.** Ensures the script is directly executable across Unix-like systems | Structure and Entry Point |  |  |  | ✓ |  |  | 1 |
| **Include timestamps and log level in log output.** Makes debugging and auditing easier; critical for long-running or batch processes | Logging and Output |  |  |  | ✓ |  |  | 1 |
| **Keep functions to ≤50 lines.** Small functions are easier to test, understand, and reuse; deep nesting and long functions hide intent | Code Quality and Style |  |  |  | ✓ |  |  | 1 |
| **Keep imports at the top of the file, grouped stdlib / third-party / local, except for heavy optional imports deferred into functions.** PEP 8 with one pragmatic exception | Style |  |  | ✓ |  |  |  | 1 |
| **Keep scripts under ~500 lines; convert to a package beyond that.** Single-file discipline exists for a reason; past that threshold it becomes an anti-pattern | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep the top-level code block (main entry point) to fewer than 10 lines.** Ensures the entry point is scannable; dispatch to helper functions | Structure and Entry Point |  |  |  | ✓ |  |  | 1 |
| **Let unexpected exceptions propagate; don't wrap `main()` in a blanket `try/except Exception: print(e)`.** Tracebacks are diagnostic gold; don't discard them | Error Handling & Exit Codes |  |  | ✓ |  |  |  | 1 |
| **Log or print diagnostic information (file counts, row counts, duration) for any batch operation.** Makes it clear what the script did; helps diagnose issues in production | Testing and Reproducibility |  |  |  | ✓ |  |  | 1 |
| **Log or print the error message to stderr before exiting with a non-zero code.** Ensures the user or automation system sees what went wrong | Error Handling and Exit Codes |  |  |  | ✓ |  |  | 1 |
| **Make `main()` importable and testable by keeping side effects inside it, not at module scope.** A script that runs code on import cannot be tested or linted safely | Testing & Reproducibility |  |  | ✓ |  |  |  | 1 |
| **Never call `subprocess.run` with `shell=True` on interpolated input.** Shell injection is trivial; pass an argument list instead | Safety |  |  | ✓ |  |  |  | 1 |
| **Never use `eval` or `exec` on external input.** No exceptions | Safety |  |  | ✓ |  |  |  | 1 |
| **Never use `shell=True` in subprocess calls.** Opens the door to shell injection vulnerabilities; use a list of arguments instead | Safety and Portability |  |  |  | ✓ |  |  | 1 |
| **Never use bare `except:` clauses; always specify the exception type.** A bare except silently swallows typos and KeyboardInterrupt, causing silent failures and lost signals | Error Handling and Exit Codes |  |  |  | ✓ |  |  | 1 |
| **Never use bare `except:` or `except Exception:` without re-raising or explicit handling.** They hide real bugs including `KeyboardInterrupt` in the bare case | Error Handling & Exit Codes |  |  | ✓ |  |  |  | 1 |
| **Parse arguments with `argparse`, not `sys.argv` slicing.** You get `--help`, types, and validation for free | Arguments & I/O |  |  | ✓ |  |  |  | 1 |
| **Pin Python version requirements via `# /// script` `requires-python` or a top-of-file comment.** "Works on 3.12" is not the same as "requires 3.10+" | Testing & Reproducibility |  |  | ✓ |  |  |  | 1 |
| **Prefer f-strings for formatting.** Clearest, fastest, least error-prone | Style |  |  | ✓ |  |  |  | 1 |
| **Prefer subprocess calls over shell scripts only when the task is non-trivial.** Subprocess invocation has overhead; for simple operations, use stdlib modules (pathlib, shutil, json) instead | Performance and Resource Management |  |  |  | ✓ |  |  | 1 |
| **Prefer the Python standard library over external packages.** Reduces deployment complexity, security surface, and friction; justify each external dependency explicitly | Dependencies |  |  |  | ✓ |  |  | 1 |
| **Prefer the standard library.** Fewer deps means fewer environment failures; `argparse`, `pathlib`, `json`, `csv`, `subprocess`, `logging`, `http.client` cover most needs | Structure |  |  | ✓ |  |  |  | 1 |
| **Provide a short and long `--help` text for every argument.** Makes the script self-documenting; users should not need to read the code to understand usage | Argument Parsing and Configuration |  |  |  | ✓ |  |  | 1 |
| **Put a module docstring at the top describing what the script does and showing one example invocation.** It is the first thing a reader sees and often the only documentation | Structure |  |  | ✓ |  |  |  | 1 |
| **Require explicit flag (`--dry-run`, `--verbose`) rather than relying on implicit behavior.** Prevents surprising action (e.g., accidentally deleting files) | Argument Parsing and Configuration |  |  |  | ✓ |  |  | 1 |
| **Return 0 on success, non-zero on failure, and document the exit codes if more than two are used.** Shell scripts and CI depend on this contract | Error Handling & Exit Codes |  |  | ✓ |  |  |  | 1 |
| **Send error and warning messages to stderr; send normal output to stdout.** Allows users and downstream processes to separate signal from noise and redirect appropriately | Logging and Output |  |  |  | ✓ |  |  | 1 |
| **Set sensible defaults for optional arguments; avoid requiring users to pass obvious values.** Reduces cognitive load and makes the most common case the easiest | Argument Parsing and Configuration |  |  |  | ✓ |  |  | 1 |
| **Set the executable bit (`chmod +x`) on scripts meant to be invoked directly.** A shebang without `+x` is a lie | Structure |  |  | ✓ |  |  |  | 1 |
| **Specify `encoding="utf-8"` on every `open()` call.** Default encoding is platform-dependent and a known source of silent corruption | Arguments & I/O |  |  | ✓ |  |  |  | 1 |
| **Start every executable script with `#!/usr/bin/env python3`.** Portable across systems where `python` may be Python 2 or absent | Structure |  |  | ✓ |  |  |  | 1 |
| **Stream large files line-by-line or in chunks; don't `.read()` them into memory.** Scripts get run on files larger than the author imagined | Performance |  |  | ✓ |  |  |  | 1 |
| **Support `-` as a filename meaning stdin/stdout where it makes sense.** Convention across Unix tools; trivial to implement | Arguments & I/O |  |  | ✓ |  |  |  | 1 |
| **Use `#!/usr/bin/env python3` as the shebang, not a hardcoded path.** Allows the script to use the active Python3 in PATH, including virtualenvs | Structure and Entry Point |  |  |  | ✓ |  |  | 1 |
| **Use `argparse` from the stdlib for all argument parsing.** Provides consistent help, validation, and error messages; avoid positional assumptions and manual `sys.argv` parsing | Argument Parsing and Configuration |  |  |  | ✓ |  |  | 1 |
| **Use `if __name__ == "__main__": sys.exit(main())` as the entry point.** Makes the script's behavior explicit and testable | Structure and Entry Point |  |  |  | ✓ |  |  | 1 |
| **Use `logging` configured to stderr for any script with verbosity flags or more than trivial output.** `print` for status messages stops scaling immediately | Style |  |  | ✓ |  |  |  | 1 |
| **Use `os.environ.get()` for environment variables, not direct indexing (`os.environ[]`).** Provides a default and avoids KeyError if the variable is missing | Safety and Portability |  |  |  | ✓ |  |  | 1 |
| **Use `pathlib.Path` instead of string manipulation for file paths.** Handles OS differences (/, \\) automatically; prevents subtle bugs on Windows | Safety and Portability |  |  |  | ✓ |  |  | 1 |
| **Use `pathlib.Path`, not `os.path` string manipulation.** Fewer bugs, clearer intent | Arguments & I/O |  |  | ✓ |  |  |  | 1 |
| **Use `tempfile` for temporary files and directories; never construct paths like `/tmp/foo_{pid}`.** Race conditions and symlink attacks are real | Safety |  |  | ✓ |  |  |  | 1 |
| **Use `type=` and `choices=` in argument definitions for validation.** Catches invalid input early and produces clear error messages | Argument Parsing and Configuration |  |  |  | ✓ |  |  | 1 |
| **Use descriptive variable and function names; avoid single-letter names except for loop counters and comprehensions.** Code is read far more often than it is written; clarity pays dividends | Code Quality and Style |  |  |  | ✓ |  |  | 1 |
| **Use exit code 0 for success, 1 for general failure, 2 for command-line argument errors, and codes > 2 for specific failure modes.** Allows downstream processes (scripts, monitoring, CI) to react appropriately | Error Handling and Exit Codes |  |  |  | ✓ |  |  | 1 |
| **Use generators and iterators instead of building lists in memory for large datasets.** Prevents OOM and keeps the script responsive for streaming operations | Performance and Resource Management |  |  |  | ✓ |  |  | 1 |
| **Use the `logging` module for any script that runs in production or automation contexts.** Allows separate configuration of message severity and destination; easier to parse and filter than print statements | Logging and Output |  |  |  | ✓ |  |  | 1 |
| **Use type hints for function signatures, even if not enforced at runtime.** Makes intent clear and allows static checkers (mypy, pyright) and AI assistants to catch errors | Code Quality and Style |  |  |  | ✓ |  |  | 1 |
| **Validate and sanitize all user input and external data before use.** Prevents injection, path traversal, and other attacks | Safety and Portability |  |  |  | ✓ |  |  | 1 |
| **Validate inputs early and exit with a clear stderr message before doing any destructive work.** Fail fast, fail loud | Error Handling & Exit Codes |  |  | ✓ |  |  |  | 1 |
| **Wrap execution in `def main() -> int:` and call it from `if __name__ == "__main__": sys.exit(main())`.** Enables testing, clean exit codes, and prevents import-time side effects | Structure |  |  | ✓ |  |  |  | 1 |
| **Wrap the main logic in a `def main():` function.** Provides a clear entry point and allows the script to be imported for testing without side effects | Structure and Entry Point |  |  |  | ✓ |  |  | 1 |
| **Write data to stdout and logs/errors to stderr.** Anything else breaks shell pipelines | Arguments & I/O |  |  | ✓ |  |  |  | 1 |
| **Write the script such that the main logic can be tested without side effects.** Allows unit tests to call `main(args)` or helper functions without triggering I/O or state changes | Testing and Reproducibility |  |  |  | ✓ |  |  | 1 |
| Add type hints to function signatures at script boundaries (including main) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers and AI coding assistants producing and reviewing operational scripts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid list(...) or set(...) on large generators unless you truly need materialization | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define __version__ = "X.Y.Z" | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do add type hints for functions and variables | Style |  |  |  |  |  | ✓ | 1 |
| Do always exit with a non-zero code on errors, using `sys.exit(1)` | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do avoid using `eval()` or `exec()` | Safety |  | ✓ |  |  |  |  | 1 |
| Do follow PEP 8 guidelines, including line length limits and consistent indentation | Style |  |  |  |  |  | ✓ | 1 |
| Do follow PEP 8 styling guidelines | Style |  | ✓ |  |  |  |  | 1 |
| Do handle exceptions explicitly | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do include a main guard like `if __name__ == "__main__":` | Structure |  |  |  |  |  | ✓ | 1 |
| Do include a shebang line at the top of every script, such as `#!/usr/bin/env python3`, to ensure portable execution | Shebang and Execution |  |  |  |  |  | ✓ | 1 |
| Do limit script length to under 300 lines | Structure |  | ✓ |  |  |  |  | 1 |
| Do make scripts executable by setting the file mode to +x | Shebang and Execution |  |  |  |  |  | ✓ | 1 |
| Do not ignore subprocess return codes or stderr; handle and log them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not keep unused imports | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not mutate sys.path | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not print Python tracebacks by default; log a concise error and exit nonzero; gate tracebacks behind --debug | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not prompt interactively unless an explicit -i/--interactive flag is provided | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not shadow builtins (e.g., list, file, id) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use eval or exec | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use relative imports | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use wildcard imports (from x import *) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize code into functions for logical sections, even in short scripts | Structure |  |  |  |  |  | ✓ | 1 |
| Do organize code into sections using comments or docstrings | Structure |  | ✓ |  |  |  |  | 1 |
| Do profile and optimize loops or data processing if scripts run frequently | Performance |  |  |  |  |  | ✓ | 1 |
| Do profile performance for bottlenecks in data-wrangling tasks | Performance |  | ✓ |  |  |  |  | 1 |
| Do provide helpful usage messages when arguments are incorrect | Argument Parsing |  | ✓ |  |  |  |  | 1 |
| Do use `argparse` for all scripts that accept command-line arguments | Argument Parsing |  |  |  |  |  | ✓ | 1 |
| Do use a shebang line (`#!/usr/bin/env python3`) | Structure |  | ✓ |  |  |  |  | 1 |
| Do use context managers for resources like files and network connections | Safety |  |  |  |  |  | ✓ | 1 |
| Do use the `argparse` module for command-line argument parsing | Argument Parsing |  | ✓ |  |  |  |  | 1 |
| Do validate all user inputs, such as file paths and arguments | Safety |  |  |  |  |  | ✓ | 1 |
| Do validate user input thoroughly | Safety |  | ✓ |  |  |  |  | 1 |
| Do wrap main logic in try-except blocks to catch and log exceptions | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't catch broad exceptions like `Exception`; use specific ones instead (contested) | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't hard-code constants | Argument Parsing |  | ✓ |  |  |  |  | 1 |
| Don't hardcode the Python executable path in the shebang; use `/usr/bin/env python3` instead | Shebang and Execution |  |  |  |  |  | ✓ | 1 |
| Don't import unnecessary modules; remove unused imports | Dependencies |  |  |  |  |  | ✓ | 1 |
| Don't rely on manual argument parsing with `sys.argv` | Argument Parsing |  |  |  |  |  | ✓ | 1 |
| Don't suppress exceptions with a bare `except:` clause | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don't use global variables except for constants; pass values as arguments instead (contested) | Structure |  |  |  |  |  | ✓ | 1 |
| Don't use global variables for configuration unless necessary | Performance |  | ✓ |  |  |  |  | 1 |
| Don't use inefficient data structures like lists for frequent lookups; prefer sets or dicts | Performance |  |  |  |  |  | ✓ | 1 |
| Don't use magic numbers; define them as constants with descriptive names | Style |  |  |  |  |  | ✓ | 1 |
| Don't use single-letter variable names except in very small loops | Style |  | ✓ |  |  |  |  | 1 |
| Don't write to files without checking for overwrite risks; use temporary files or confirmations | Safety |  |  |  |  |  | ✓ | 1 |
| Exit 2 for CLI usage errors and 1 for runtime failures; return 0 on success | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For YAML, use yaml.safe_load (not yaml.load) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Format with Black at max line length 88 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Give every argument a meaningful help string | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Goal: Make scripts safe, predictable, maintainable, and friendly to Unix pipelines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Handle SIGPIPE/BrokenPipeError gracefully when writing to a closed pipe | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If any third-party import is used, include a colocated requirements.txt | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If shell=True is truly required, quote user-provided parts with shlex.quote and document why in a comment | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Implement main(argv: Sequence[str] \| None = None) -> int | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make the script executable on POSIX (chmod +x) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never pass untrusted input to shell=True | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never use a bare except; catch specific exceptions or Exception as e | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Optionally, do consider type hints for function signatures (contested) | Contestable |  | ✓ |  |  |  |  | 1 |
| Pin third-party requirements with ~= or == in requirements.txt | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer stdlib; use third-party packages only with clear payoff in code clarity or capability | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer streaming over loading entire files into memory | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide --version that prints "<prog> <version>" and exits 0 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a module docstring with a one-line synopsis | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put all executable logic under if __name__ == "__main__": sys.exit(main()) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Standalone Python 3 scripts used as CLI tools, automation, and data-wrangling utilities | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Specify encoding="utf-8" when opening text files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start the file with exactly this shebang: #!/usr/bin/env python3 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Support -v/--verbose (repeatable) and -q/--quiet to control logging level | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use ''.join(...) or io.StringIO instead of += in loops for large string assembly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use argparse for CLI parsing | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use f-strings for string formatting | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use logging for operational messages and print only for program output | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use pathlib.Path for filesystem paths instead of os.path | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use subprocess.run([...], check=True) with a list of args; avoid shell=True | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use sys.stdin.buffer/sys.stdout.buffer for binary data | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use tempfile (e.g., TemporaryDirectory, NamedTemporaryFile) for tmp files and directories | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use with statements for files and subprocess.Popen to ensure resources are closed | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.

- ****Do** prefer the standard library over third-party packages** — avg similarity 46 (substantively similar but differently worded — genuine convergence)
  - `vertex_ai/gemini-2.5-pro`: **Do** prefer the standard library over third-party packages.
  - `xai/grok-3-mini`: Do prefer standard library modules over third-party packages. Rationale: It minimizes dependencies, reducing installation and compatibility issues for standalone scripts.

## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

