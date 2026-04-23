## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Start the file with `#!/usr/bin/env python3` shebang. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use argparse for command-line argument parsing. | Arguments | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Never use bare `except:` clauses; catch specific exceptions. | Error Handling | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Never use `shell=True` with subprocess on interpolated/untrusted input. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Wrap execution in a `main()` function called from `if __name__ == "__main__"`. | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Prefer the standard library over third-party dependencies. | Dependencies | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Include a module-level docstring describing purpose/usage. | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use type hints on function signatures. | Style | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Do not use `eval` or `exec`. | Safety | ✓ | ✓ | ✓ |  |  |  | 3 |
| Use `pathlib.Path` instead of `os.path` string manipulation. | I/O | ✓ |  | ✓ | ✓ |  |  | 3 |
| Specify `encoding="utf-8"` explicitly on text-mode `open()` calls. | I/O | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use context managers (`with`) for file and resource handling. | I/O | ✓ |  |  | ✓ | ✓ |  | 3 |
| Write primary data to stdout and logs/errors to stderr. | I/O | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use exit code 0 for success and non-zero on failure. | Error Handling | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Handle KeyboardInterrupt / SIGPIPE cleanly rather than dumping tracebacks. | Error Handling | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use `logging` (to stderr) rather than print for operational messages. | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Do not use wildcard imports (`from x import *`). | Style | ✓ |  |  | ✓ |  |  | 2 |
| Prefer f-strings for string formatting. | Style | ✓ |  | ✓ |  |  |  | 2 |
| Document/declare third-party dependencies (requirements.txt or PEP 723). | Dependencies | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Remove unused imports. | Style | ✓ |  |  |  |  | ✓ | 2 |
| Provide a `--version` flag. | Arguments | ✓ |  |  |  |  |  | 1 |
| Define `__version__` constant. | Structure | ✓ |  |  |  |  |  | 1 |
| Support `-v/--verbose` and `-q/--quiet` verbosity flags. | Arguments | ✓ |  |  |  |  |  | 1 |
| Do not mutate `sys.path`. | Structure | ✓ |  |  |  |  |  | 1 |
| Do not use relative imports in scripts. | Structure | ✓ |  |  |  |  |  | 1 |
| Give every argparse argument a meaningful help string. | Arguments | ✓ |  |  | ✓ |  |  | 2 |
| Use `subprocess.run([...], check=True)` with an argument list. | I/O | ✓ |  |  | ✓ |  |  | 2 |
| Use `tempfile` for temp files/dirs rather than ad-hoc `/tmp/...` paths. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Use `yaml.safe_load` instead of `yaml.load`. | Safety | ✓ |  |  |  |  |  | 1 |
| Stream large files instead of reading them fully into memory. | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Avoid `s += ...` in loops; use `''.join` / `StringIO`. | Performance | ✓ |  |  |  |  |  | 1 |
| Avoid materializing large generators with `list()`/`set()` unnecessarily. | Performance | ✓ |  |  | ✓ |  |  | 2 |
| Format code with Black (or similar automated formatter). | Style | ✓ |  |  |  | ✓ |  | 2 |
| Do not shadow builtins. | Style | ✓ |  |  |  |  |  | 1 |
| Pin third-party requirements (`==` or `~=`). | Dependencies | ✓ |  |  |  |  |  | 1 |
| Do not prompt interactively unless an explicit `-i/--interactive` flag is set. | Arguments | ✓ |  |  |  |  |  | 1 |
| Limit script length (convert to package past a threshold). | Structure |  | ✓ | ✓ |  |  |  | 2 |
| Follow PEP 8 style. | Style |  | ✓ |  | ✓ |  | ✓ | 3 |
| Don't hard-code constants/paths; use args or env variables. | Safety |  | ✓ |  | ✓ | ✓ | ✓ | 4 |
| Avoid single-letter / non-descriptive variable names. | Style |  | ✓ |  | ✓ |  |  | 2 |
| Profile for performance bottlenecks when needed. | Performance |  | ✓ |  |  |  | ✓ | 2 |
| Don't use global variables for state/config. | Structure |  | ✓ |  |  | ✓ | ✓ | 3 |
| Validate user inputs before destructive operations. | Safety |  | ✓ | ✓ | ✓ |  | ✓ | 4 |
| Set the executable bit (chmod +x) on scripts with a shebang. | Structure |  |  | ✓ | ✓ |  | ✓ | 3 |
| Keep imports at top of file; defer only heavy/conditional imports. | Structure |  |  | ✓ | ✓ |  |  | 2 |
| Don't use mutable default arguments. | Style |  |  | ✓ |  |  |  | 1 |
| Support `-` for stdin/stdout where appropriate. | Arguments |  |  | ✓ |  |  |  | 1 |
| No side effects at module scope; keep `main()` importable/testable. | Testing |  |  | ✓ | ✓ |  |  | 2 |
| Pin or declare required Python version. | Testing |  |  | ✓ |  |  |  | 1 |
| Provide a `--dry-run` flag for destructive operations. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Do not log secrets, tokens, or credentials. | Safety |  |  | ✓ | ✓ |  |  | 2 |
| Don't reach for asyncio/threading/multiprocessing without a measured reason. | Performance |  |  | ✓ | ✓ |  |  | 2 |
| Keep functions short (≤50 lines) and cohesive. | Style |  |  |  | ✓ |  |  | 1 |
| Extract argparse configuration into a `get_parser()` function. | Arguments |  |  |  | ✓ |  |  | 1 |
| Use `type=` and `choices=` for argparse validation. | Arguments |  |  |  | ✓ |  |  | 1 |
| Check for required third-party imports and fail with clear error. | Dependencies |  |  |  | ✓ |  |  | 1 |
| Prefer stdlib modules (pathlib/shutil/json) over shelling out. | Performance |  |  |  | ✓ |  |  | 1 |
| Use `subprocess.run(capture_output=True, text=True)` for subprocess output. | I/O |  |  |  | ✓ |  |  | 1 |
| Use `os.environ.get()` with defaults, not direct indexing. | Safety |  |  |  | ✓ |  |  | 1 |
| Log diagnostic info (counts, durations) for batch operations. | Style |  |  |  | ✓ |  |  | 1 |
| Include timestamps and levels in log output. | Style |  |  |  | ✓ |  |  | 1 |
| Keep the `__main__` block very short (dispatch to `main()`). | Structure |  |  |  | ✓ |  |  | 1 |
| Don't run package-management operations (pip install) from inside the script. | Dependencies |  |  |  | ✓ |  |  | 1 |
| Confirm before performing destructive operations. | Safety |  |  |  | ✓ | ✓ |  | 2 |

## Notes on clustering decisions

- **"Main function" vs "`if __name__` guard"**: treated as a single cluster because every model that raised one raised the other as a paired pattern; separating them would create two nearly identical columns. gpt-4o-mini did not raise either and is left blank.
- **"Non-zero exit code on failure"** absorbed gpt-5's more detailed "exit 2 for usage / 1 for runtime" rule, claude-haiku's tiered codes, and gemini's `sys.exit(1)` rule. These differ in specificity but share the underlying imperative.
- **"Stdout for data, stderr for logs"** and **"Use logging rather than print"** are kept as separate rules because several models raised only the stream-separation point without mentioning the `logging` module (and vice versa).
- **"Declare third-party deps"** merges gpt-5's `requirements.txt`, claude-opus's PEP 723 inline metadata, claude-haiku's top-of-file comment, and grok's top-of-file comment. The mechanism differs but the rule ("make deps explicit") is the same. Pinning (gpt-5 only) is kept separate since it's a distinct claim.
- **"Never use `shell=True`"** merges the absolutist phrasings (gemini, grok, claude-haiku) with the conditional ones (gpt-5, claude-opus: "...on interpolated input"). A stricter clusterer could split these.
- **"Validate user inputs"** merges claude-opus's "validate early before destructive work," gpt-4o-mini's "validate user input thoroughly," claude-haiku's "validate and sanitize," and grok's "validate all user inputs." Claude-opus's version overlaps with the separate "confirm before destructive ops" rule; kept separate because the confirmation/`--dry-run` framing is distinct from input validation.
- **"Don't hard-code paths/constants"**: gpt-4o-mini's "don't hard-code constants" and gemini/claude-haiku/grok's "don't hard-code paths/credentials" clustered together as one rule about externalizing configuration.
- **"Stream large files"** merges gpt-5's generic streaming rule, claude-opus's "don't `.read()` large files," and claude-haiku's "use generators/iterators for large datasets." These are arguably three rules but share the same imperative.
- **"PEP 8 style"** and **"Format with Black"** kept separate: Black implies a specific tool and line length (88); PEP 8 is the broader convention. gpt-5 and gemini chose Black; gpt-4o-mini, claude-haiku, and grok chose PEP 8.
- **"Handle KeyboardInterrupt/SIGPIPE"** merges gpt-5's SIGPIPE rule with claude-opus and claude-haiku's Ctrl+C/exit-130 rules. Different signals but same underlying principle ("don't dump tracebacks on expected interrupts"); a stricter clusterer would split.
- **"Use argparse"**: grok's rule is phrased as an opinionated choice, claude-opus's is phrased as "don't reach for click/typer unless…" — both clustered as the same positive imperative. gpt-4o-mini's rule is identical in substance.
- **"Keep functions short"** (claude-haiku only) and **"Limit script length"** (gpt-4o-mini, claude-opus) are kept as separate rules since one bounds function size and the other bounds file size.
- **"Confirm before destructive operations"** and **"Provide `--dry-run`"** kept separate because they're different mitigations, though claude-haiku raises both and claude-opus raises both within the same bullet.