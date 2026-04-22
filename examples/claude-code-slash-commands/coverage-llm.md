## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Require explicit confirmation or opt-in flag for destructive operations. | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Validate arguments up front and fail fast with actionable error messages. | Correctness | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Include a clear description/summary at the top of each command. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Document every argument with name, type, and expected behavior. | Arguments | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Never interpolate unescaped/unvalidated input into shell or other execution contexts. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Keep each command focused on a single purpose; prefer composition over monoliths. | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Use consistent (kebab-case) file/command naming conventions. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Make commands idempotent so repeated runs are safe. | Correctness | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Include at least one concrete usage example. | Structure | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Declare/document side effects explicitly in the command. | Safety | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Use frontmatter/metadata (description, args, version, owners) for each command. | Structure | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Never embed secrets, tokens, or sensitive data in commands; mask them in logs. | Safety | ✓ | ✓ | ✓ |  |  |  | 3 |
| Document environment prerequisites (tools, versions, auth, env vars). | Structure | ✓ |  | ✓ | ✓ |  |  | 3 |
| Keep command files short/focused (under ~50–100 lines). | Structure |  |  | ✓ | ✓ |  |  | 2 |
| Limit `allowed-tools` / script permissions to the minimum required (least privilege). | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Prefer positional/named argument slots over a single raw `$ARGUMENTS` blob. | Arguments |  |  | ✓ | ✓ |  |  | 2 |
| Write instructions in active voice / imperative mood. | Style |  |  | ✓ | ✓ |  | ✓ | 3 |
| State explicit success criteria / expected output format in the prompt. | Style / Prompting |  |  | ✓ |  | ✓ |  | 2 |
| Review/test commands like code (PR review, CI, manual test). | Maintenance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Version commands alongside the codebase (commit to repo, changelog). | Maintenance | ✓ |  |  | ✓ |  |  | 2 |
| Deprecate commands with clear warnings/migration paths instead of silent deletion. | Maintenance | ✓ |  |  | ✓ |  |  | 2 |
| Parallelize independent work for performance. | Performance | ✓ |  |  | ✓ |  |  | 2 |
| Cache expensive results with clear invalidation. | Performance | ✓ |  |  |  |  | ✓ | 2 |
| Show progress / feedback for long-running commands. | Performance / UX | ✓ |  |  | ✓ |  |  | 2 |
| Apply timeouts and bounded retries to network/long-running calls. | Performance | ✓ |  |  |  |  |  | 1 |
| Provide a `--dry-run` mode that previews effects before applying changes. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Provide `--verbose` / adjustable output verbosity. | Logging & UX | ✓ |  |  |  |  |  | 1 |
| Set strict shell mode (`set -euo pipefail`, safe `IFS`). | Execution & Shell | ✓ |  |  |  |  |  | 1 |
| Detect OS/tool variants and branch explicitly for portability. | Portability | ✓ |  |  | ✓ |  |  | 2 |
| Check required tools/versions with actionable install hints. | Execution & Shell | ✓ |  |  | ✓ |  |  | 2 |
| Default to the smallest safe scope (e.g., changed files, current file). | Arguments / Safety | ✓ |  |  | ✓ |  |  | 2 |
| Refuse to run with a dirty working tree unless declared safe. | Safety | ✓ |  |  |  |  |  | 1 |
| Do not pipe untrusted network content to a shell (no `curl \| sh`). | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Prefer letting the model open files on demand rather than front-loading context. | Model & Performance |  |  | ✓ |  |  |  | 1 |
| Do not `@`-include large generated files or lockfiles. | Model & Performance |  |  | ✓ |  |  |  | 1 |
| Inherit the default model unless a command truly needs a different tier. | Model & Performance |  |  | ✓ |  |  |  | 1 |
| Keep LLM prompts specific with goals, constraints, and acceptance criteria. | LLM Usage | ✓ |  |  |  | ✓ |  | 2 |
| Use XML tags / structured delimiters around interpolated context in prompts. | LLM Usage |  |  |  |  | ✓ |  | 1 |
| Provide few-shot examples of desired output in the prompt. | LLM Usage |  |  |  |  | ✓ |  | 1 |
| Set temperature to 0 for deterministic edits; higher only for ideation. | LLM Usage | ✓ |  |  |  |  |  | 1 |
| Require human review / show diffs before applying LLM-generated edits. | LLM Usage | ✓ |  |  |  |  |  | 1 |
| Redact secrets from prompts and model inputs. | LLM Usage | ✓ |  |  |  |  |  | 1 |
| Prefer prompt-based logic over scripting; use scripts only for what the model can't do. | Scripting / LLM | ✓ (contested) |  | ✓ |  | ✓ (contested) |  | 3 |
| Keep side-effect scripts short, idempotent, and inspectable. | Scripting | ✓ |  | ✓ | ✓ |  |  | 3 |
| Prefer bash (with strict mode) for complex shell steps. | Execution & Shell | ✓ (contested) |  |  |  |  |  | 1 |
| Use a shebang line to specify script interpreter. | Scripting |  |  |  |  | ✓ |  | 1 |
| Pass script args as flags/stdin and emit primary output on stdout. | Scripting |  |  |  |  | ✓ |  | 1 |
| Log script/side-effect execution for transparency/auditing. | Safety / Logging |  |  |  | ✓ |  | ✓ | 2 |
| Place instructions before context/examples in prompts. | LLM Usage |  |  |  |  | ✓ |  | 1 |
| Normalize paths to the repo root and verify existence. | Arguments | ✓ |  |  |  |  |  | 1 |
| Use locale-independent settings for reproducibility. | Correctness | ✓ |  |  |  |  |  | 1 |
| Auto-disable ANSI colors when output is non-TTY. | Logging & UX | ✓ |  |  |  |  |  | 1 |
| Assign CODEOWNERS for shared command directories. | Maintenance | ✓ |  |  |  |  |  | 1 |
| Separate personal vs. shared commands (`~/.claude/` vs `.claude/`). | Structure |  |  | ✓ |  |  |  | 1 |
| Avoid unnecessary complexity / over-parameterization. | Style |  | ✓ (contested) |  | ✓ |  |  | 2 |
| Avoid globally mutable state in commands. | Performance / Correctness |  | ✓ |  |  |  |  | 1 |
| Limit frequency of external API calls. | Performance |  | ✓ |  |  |  |  | 1 |
| Provide a README/help index listing all commands. | Maintenance | ✓ |  |  | ✓ |  |  | 2 |
| Structure the prompt body as Purpose → Inputs → Context → Steps → Success Criteria. | Style |  |  | ✓ |  |  |  | 1 |
| Use numbered lists / bullets for procedural steps. | Style |  |  | ✓ | ✓ |  | ✓ | 3 |
| Review commands periodically (e.g., quarterly) and remove unused ones. | Maintenance |  |  | ✓ | ✓ |  |  | 2 |
| Gather repo state deterministically (e.g., `!git status`) at the top of commands. | Arguments / Context |  |  | ✓ |  |  |  | 1 |
| Use explicit, unambiguous argument names (e.g., `{currentFile}` not `{file}`). | Arguments |  |  | ✓ | ✓ |  |  | 2 |

## Notes on clustering decisions

- **"Validate arguments and fail fast"** bundles together several overlapping rules: gpt-5's "validate before side effects," 4o-mini's "do not ignore edge cases," Opus's "validate in first step and abort," Haiku's "fail fast and with actionable messages," Gemini's "mark non-obvious arguments as required," and Grok's "validate all required arguments." Error-message specificity (Haiku, 4o-mini) was folded in rather than split out.
- **"Require confirmation for destructive operations"** includes Opus's "gate behind `--yes` flag," Haiku's `--confirm`, gpt-5's `--force` default, Gemini's "confirmation within workflow," Grok's "confirmation prompts," and 4o-mini's "prompts for data-modifying actions." These could arguably split into "preview/dry-run" vs "confirmation flag" — I kept dry-run as a separate row since gpt-5 and Opus call it out distinctly.
- **"Keep each command focused on a single purpose"** merges gpt-5's "one thing well," Opus's "single stated purpose," Haiku's "granular is better," Gemini's "favor specific commands," and Grok's "limit to single primary action." 4o-mini doesn't clearly state this, though its "avoid unnecessary complexity" is adjacent.
- **"Never interpolate unescaped input"** bundles shell-quoting (gpt-5), sanitization (Grok, Haiku), no-`eval` (Gemini, gpt-5), and XML-tagging for prompt injection (Gemini). One could split shell-injection from prompt-injection; I clustered them as a single "don't trust raw interpolation" rule.
- **"Prefer prompt logic over scripts"** is marked contested by gpt-5 (implicitly — they advocate the opposite via hermetic toolchains) and explicitly contested by Gemini. Opus's "move judgment to prompt, deterministic logic to scripts" is a nuanced variant I counted as agreement.
- **"Frontmatter/metadata"** clusters gpt-5's YAML frontmatter, Opus's `description:`/`argument-hint:`/`allowed-tools:`, Gemini's frontmatter args, and Grok's YAML frontmatter. Haiku describes a "description block" but doesn't mandate frontmatter specifically — I still counted it since the intent overlaps.
- **"Document every argument"** is distinct from "use frontmatter" — Haiku and Gemini emphasize per-argument docs without necessarily requiring frontmatter; gpt-5 and Grok require both.
- **"Use consistent naming conventions"** — all six models mention this in some form (kebab-case, lowercase, verb-object). Grok marks the exact format contested.
- **"Keep side-effect scripts short and idempotent"** merges gpt-5's idempotence rule, Opus's "deterministic logic in scripts," Haiku's "under 20 lines and idempotent," and Gemini's idempotence rule. I treated idempotence-of-commands (a broader rule) as separate from idempotence-of-scripts, though they overlap.
- **"Avoid unnecessary complexity"** (4o-mini, Haiku) is close to "single-purpose commands" but I kept them separate since 4o-mini explicitly flags complexity-vs-functionality as contested whereas the single-purpose rule is about scope, not cleverness.
- A regex matcher would likely miss: Opus's "argument-hint" ↔ gpt-5's "document parameters"; Gemini's "XML tags around interpolation" ↔ gpt-5's "quote interpolated values"; Haiku's "{currentFile} not {file}" ↔ Opus's "state argument semantics explicitly."