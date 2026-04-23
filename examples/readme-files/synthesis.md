# Synthesis of README Best-Practices Guidance

## 1. Consensus Rules

### Structure & Opening

- **Start with a single H1 project title as the first content line.** Anchors the document for readers and tooling. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Follow the title with a one-sentence description of what the project is.** Answers "what is this?" before anything else. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Organize the README with predictable sections in a reader-intent order: description → prerequisites → installation → usage → configuration → troubleshooting → contributing → license.** Matches the path users actually take. *(substantively similar across all models)*
- **Use Markdown headings hierarchically; do not skip levels.** Accessibility tools, renderers, and auto-TOCs rely on sequential hierarchy. *(substantively similar across Claude Opus, Claude Haiku, GPT-5, Grok)*

### Prerequisites & Installation

- **List prerequisites (runtimes, tools, OS) with explicit versions before installation commands.** Unmet prerequisites are the top cause of failed first-runs. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Provide copy-pasteable install commands that work on a clean machine.** Eliminates transcription errors and friction. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Include a Quickstart/Usage section with a minimal runnable example.** Speed to first success drives adoption. *(near-identical across GPT-5, Claude Opus, Claude Haiku)*

### Commands & Code Blocks

- **Put every command in a fenced code block tagged with the correct language (`bash`, `sh`, `console`, `pwsh`, etc.).** Enables syntax highlighting, copy-buttons, and tooling. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Do not prefix command lines with shell prompts (`$`, `>`) unless showing inline output.** Prompt characters break copy-paste. *(near-identical across GPT-5, Claude Opus, Gemini)*
- **Use clearly marked placeholders (e.g., `<YOUR_API_KEY>`) for user-supplied values.** Prevents misuse and signals substitution is required. *(substantively similar across GPT-5, Claude Haiku, Gemini)*

### Links & Assets

- **Ensure every link resolves — internal anchors, relative file paths, and external URLs.** Broken links erode trust and signal neglect. *(substantively similar across GPT-5, Claude Opus, Gemini)*
- **Use relative links for repo-local files.** Relative links survive forks and mirrors. *(GPT-5, Claude Opus, Gemini — note: Claude Haiku disagrees; see Divergences)*
- **Provide descriptive alt text for every image and badge.** Required for accessibility; useful when images fail to load. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*

### License & Contribution

- **Name the license explicitly in the README and link to a `LICENSE` file in the repo root.** Legal clarity is non-negotiable. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Include a Contributing section or link to `CONTRIBUTING.md`.** Even a one-liner is better than silence. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Safety

- **Never include real secrets, tokens, or credentials in examples.** Public docs must not leak credentials; readers copy-paste. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Warn explicitly on destructive or irreversible commands (`rm -rf`, `DROP`, `--force`).** Accidental destruction is unrecoverable. *(substantively similar across GPT-5, Claude Opus, Grok)*
- **Do not recommend `curl … | sh` installers without a manual alternative and a warning.** Pipe-to-shell is a security posture users must opt into. *(near-identical across GPT-5, Claude Opus, Gemini)*

### Style

- **Write in clear, direct language; use imperative mood and second person for instructions.** Matches reader expectations and reduces ambiguity. *(substantively similar across Claude Opus, Claude Haiku, Grok)*
- **Keep lines under ~120 characters in source.** Improves diffs and terminal readability. *(GPT-5, Claude Opus — contested; Grok proposes 80)*

### Maintainability

- **Link to detailed docs rather than duplicating them in the README.** Single source of truth prevents drift. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Keep the README in sync with the code; update it in the same commit as behavioral changes.** Stale instructions are the most common README defect. *(substantively similar across Claude Opus, Claude Haiku, Grok)*

## 2. Strong Minority Rules

- **Limit badges to roughly three to five, placed under the title.** (GPT-5, Claude Opus, Claude Haiku, Gemini) — Multiple models converge on "few badges, not many"; the exact count is contested but the principle is consistent. Kept because badge overload is a real and common defect.
- **Keep embedded images under ~500 KB each and total README assets under ~2 MB; prefer SVG or asciicast over animated GIFs.** (Claude Opus) — Well-reasoned performance concern for mobile and low-bandwidth readers; not contradicted by any model.
- **Show expected output after command blocks.** (Claude Haiku) — Unexplained silence breeds doubt; helps users confirm their run succeeded.
- **Provide uninstall or cleanup instructions alongside install.** (GPT-5, Claude Haiku) — Reversibility is part of safety; frequently forgotten.
- **Use RFC-reserved example domains/IPs (`example.com`, `127.0.0.1`, RFC 5737 ranges) — never real hostnames.** (Claude Haiku) — Concrete, testable safety/hygiene guidance.
- **Provide a private security-disclosure channel (link to `SECURITY.md` or a contact email).** (GPT-5, Claude Haiku) — Responsible disclosure protects users; absent from most responses but important.
- **Do not instruct readers to disable TLS verification, SELinux, or firewalls as a workaround.** (Claude Opus) — Specific, actionable safety rule.
- **Avoid emoji in headings.** (Claude Opus) — Breaks grep, anchor links, and screen readers. Marked contested but well-reasoned.
- **Do not hand-maintain duplicates of `--help` output.** (Claude Opus) — Specific instance of the broader "don't duplicate" rule; worth calling out.

## 3. Divergences

### Relative vs. absolute links for repo-local files

- **Relative links** (GPT-5, Claude Opus, Gemini): "Relative links survive forks and mirrors."
- **Absolute GitHub URLs** (Claude Haiku): "Relative paths break when the README is viewed on npm, PyPI, or other mirrors."

**Synthesis:** The majority is correct for the GitHub-first case, and Claude Haiku is correct for the package-mirror case. **Recommendation:** use relative links for docs that live in the same repo, but absolute URLs for references package consumers will view on npm/PyPI (or configure your package tooling to rewrite relative links). Flag as a known trade-off rather than a single rule.

### Line-length limit

- **120 characters** (GPT-5, Claude Opus)
- **100 characters for prose** (Claude Haiku)
- **80 characters in code examples** (Grok)

**Synthesis:** 120 for prose source lines, 80 for code blocks is a defensible consensus (Grok's 80 applies only to code; the others apply to prose). Recommend 120 for prose, 80 for code within fenced blocks.

### Should Quickstart come before or after a "Why/What" section?

- **Quickstart first** (Claude Opus: "Readers come to do, not to learn")
- **Problem/Why first** (Claude Haiku, Gemini: "Establishes value before technical details")

**Synthesis:** Both agree the one-sentence description is line 2. They disagree on whether the next block is a problem statement or install commands. Recommend: one-sentence description → 2-3 sentence "what problem it solves" → Quickstart. This is a small ordering choice; either works if the top 30 seconds answer "what is this and should I care."

### Are version numbers appropriate in the README body?

- **Yes, explicit versions** (Claude Haiku, Grok)
- **Avoid hardcoding versions defined elsewhere** (Gemini: link to `package.json` instead)

**Synthesis:** State prerequisite version ranges/minimums in the README (Node 18+), but don't restate the project's own pinned version numbers that live in manifests. This reconciles both positions.

### Table of contents threshold

- **~200 lines** (GPT-5)
- **~500 lines or ~500 words** (Claude Opus, Claude Haiku)
- **Required for "extensive" READMEs** (GPT-4o-mini)

**Synthesis:** No strong basis for a specific number. Recommend a TOC when the rendered document exceeds roughly one screen of section headings (~400-500 lines is a reasonable default). GitHub's sidebar auto-TOC reduces the need for a hand-maintained one.

### How strict to be about `sudo` in examples

- **Avoid `sudo`** (GPT-5, contested)
- **No position** (others)

**Synthesis:** Flag `sudo` as a soft warning, not a hard violation — some package managers legitimately require it. Suggest non-sudo alternatives where they exist.

## 4. Notable Omissions

- **GPT-4o-mini omits nearly everything concrete.** No rules on link validation, secrets, code-fence language tags, command copy-pasteability, prerequisites, placeholders, or license files. Its rules file is ~15 bullets; the others are 30-50+. The absence is the signal: this response is substantially less thorough and should be weighted accordingly.
- **Grok omits link validation** (relative links, dead-link checking, anchor validation). Every other model addresses this. Grok's focus on file-size/line-length performance metrics is idiosyncratic.
- **Grok omits specific safety rules** around `curl | sh` and secret scanning that the other four models all include.
- **GPT-4o-mini omits the license rule** beyond a passing mention of "contact information" — all other models make license naming + link to LICENSE file a core requirement.
- **Gemini omits a troubleshooting/FAQ section requirement** that GPT-5, Claude Opus, and Claude Haiku all include.
- **GPT-4o-mini and Grok omit code-fence language tagging**, which is one of the most near-identical rules across the other three.

## 5. Shared Deterministic Checks

### Shared checks (raised by multiple models)

- **Check** — Verify the file's first non-empty, non-frontmatter block is a single H1 heading and that exactly one H1 exists.
  - **Signal** — Parsed Markdown AST.
  - **Tool candidate** — `markdownlint` MD025 + MD041.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Claude Opus explicitly handles YAML frontmatter; GPT-5 does not. Otherwise identical.

- **Check** — Verify that headings for the standard sections (Prerequisites/Installation/Usage/Configuration/Troubleshooting/Contributing/License or close synonyms) exist and appear in reader-intent order.
  - **Signal** — Parsed Markdown AST, heading sequence.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Claude Haiku, Gemini, Grok.
  - **Variance** — Models differ on which sections are required. Consensus minimum: Installation, Usage, License. GPT-5 and Claude Haiku require more; Gemini minimum. Ordering check is a Claude Haiku specific addition.

- **Check** — Verify heading levels increment by at most 1 (no skipped levels like H2→H4).
  - **Signal** — Parsed Markdown AST.
  - **Tool candidate** — `markdownlint` MD001.
  - **Raised by** — Claude Opus, Claude Haiku.
  - **Variance** — None.

- **Check** — Verify every fenced code block has a non-empty language info-string.
  - **Signal** — Parsed Markdown AST.
  - **Tool candidate** — `markdownlint` MD040.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — None meaningful; all allow `text`/`console` as fallback.

- **Check** — Flag shell-block lines that begin with `$`, `>`, or `#` prompt prefixes.
  - **Signal** — Parsed Markdown AST, shell-tagged code blocks.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Gemini.
  - **Variance** — Gemini notes false-positive risk for legitimate outputs starting with `$`; GPT-5 notes Windows `>` redirection ambiguity.

- **Check** — Verify every image has non-empty, non-placeholder alt text.
  - **Signal** — Parsed Markdown AST, image nodes.
  - **Tool candidate** — `markdownlint` MD045.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Claude Opus additionally rejects placeholder alts like "image" or the filename.

- **Check** — Verify every relative link resolves to an existing file; verify every fragment link matches a heading slug; optionally verify external URLs return 2xx/3xx.
  - **Signal** — Parsed Markdown AST + filesystem + HTTP.
  - **Tool candidate** — `lychee` or `markdown-link-check`.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — GPT-5 and Gemini focus on local and external; Claude Opus adds fragment/anchor validation with renderer-specific slugifiers.

- **Check** — Scan README for credentials using a secret scanner.
  - **Signal** — Raw text + code block contents.
  - **Tool candidate** — `gitleaks`, `trufflehog`, or `detect-secrets`.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — None; all name the same tools and acknowledge false-positive handling via allowlists.

- **Check** — Flag `curl … | sh`, `wget … | bash`, and PowerShell `iex (iwr …)` patterns in code blocks.
  - **Signal** — Code-block contents.
  - **Tool candidate** — Ad-hoc regex.
  - **Raised by** — GPT-5, Gemini (Claude Opus describes narratively).
  - **Variance** — GPT-5 provides most complete regex including PowerShell equivalents.

- **Check** — Flag destructive commands (`rm -rf`, `dd if=`, `mkfs`, `DROP DATABASE`) in examples.
  - **Signal** — Code-block contents.
  - **Tool candidate** — Ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — None substantive.

- **Check** — Verify a `LICENSE` file exists in repo root and the README contains a link to it; verify a heading matching `/license/i`.
  - **Signal** — Filesystem + parsed AST.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Claude Opus, Gemini.
  - **Variance** — Claude Opus additionally requires an SPDX identifier in the README text; GPT-5 and Gemini require the link only.

- **Check** — Verify a Contributing section exists OR a link to `CONTRIBUTING.md` is present.
  - **Signal** — Parsed AST + filesystem.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — None.

- **Check** — Flag source lines exceeding a configured max length, excluding fenced code blocks, tables, and bare-URL lines.
  - **Signal** — Raw source.
  - **Tool candidate** — `markdownlint` MD013.
  - **Raised by** — GPT-5, Claude Opus, Grok.
  - **Variance** — GPT-5/Claude Opus use 120 for prose; Grok uses 80 for code blocks specifically. Reconcilable as two thresholds.

- **Check** — If total line count exceeds a threshold, require a Table of Contents heading.
  - **Signal** — Raw source line count + parsed AST.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5 (200 lines), GPT-4o-mini (500 words), Claude Opus (500 lines), Claude Haiku (500 words).
  - **Variance** — Threshold varies significantly (200-500). Recommend configurable default of 400 lines.

### Singleton checks

- **Check** — Flag undefined `<PLACEHOLDER>` tokens (tokens used in examples but never defined in a Configuration or Placeholders section).
  - **Signal** — Raw source + section analysis.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Count badge-like image nodes in the prelude (between H1 and first prose block); flag if over a configured threshold.
  - **Signal** — Parsed AST.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Measure byte size of each referenced image and the total; flag individual images over 500 KB and total over 2 MB.
  - **Signal** — Filesystem + HTTP HEAD.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Flag smart quotes, em/en-dashes, and ellipsis characters inside code blocks.
  - **Signal** — Raw source (Unicode code points within fenced blocks).
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Haiku.

- **Check** — Flag IPs and domains in examples outside RFC 5737 documentation ranges and reserved example TLDs.
  - **Signal** — Raw text and code blocks.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Claude Haiku.

- **Check** — Flag emoji code points in heading text.
  - **Signal** — Parsed AST heading nodes.
  - **Tool candidate** — Ad-hoc (Unicode `Emoji_Presentation` property).
  - **Raised by** — Claude Opus.

- **Check** — Flag `TODO`, `FIXME`, `XXX` markers in the published README.
  - **Signal** — Raw text regex.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — Grok.

- **Check** — Verify README.md is tracked in version control (not in `.gitignore`).
  - **Signal** — `git check-ignore`.
  - **Tool candidate** — Git.
  - **Raised by** — Grok.

- **Check** — Execute tagged `bash`/`sh` code blocks in a clean container and assert zero exit.
  - **Signal** — Extracted code blocks + container runtime.
  - **Tool candidate** — `mdsh`, `bats`.
  - **Raised by** — Claude Opus.

- **Check** — Fetch badge image URLs and flag 404s or images containing "unknown"/"failing" text.
  - **Signal** — HTTP HEAD + image inspection.
  - **Tool candidate** — Ad-hoc.
  - **Raised by** — GPT-5.

---

## 6. Final Rules File

# README.md Rules

**Scope:** Project `README.md` files in source repositories.
**Audience:** Engineers and AI assistants writing, reviewing, or generating README files.
**Goal:** Make READMEs that reduce time-to-first-success, stay correct over time, and don't put readers at risk.

## Structure

- Put the project name as the only H1, on the first content line (after any YAML frontmatter). Readers and tools expect the title there.
- Follow the H1 with a one-sentence description of what the project is. It is the most-read line in the document.
- Follow that with 2-3 sentences stating the problem the project solves. Features answer "how"; problems answer "why I should care."
- Organize H2 sections in this order: Prerequisites → Installation → Usage/Quickstart → Configuration → Troubleshooting → Contributing → License. This matches the order readers need information.
- Use heading levels sequentially (H1 → H2 → H3); never skip a level. Accessibility tools and Markdown renderers rely on hierarchy.
- Add a hand-maintained Table of Contents only when the rendered document exceeds ~400 lines. Below that, platform auto-TOCs suffice.
- Keep the README under ~500 lines. Longer documentation belongs in `/docs` with the README linking in.

## Prerequisites & Installation

- List prerequisites (runtimes, tools, OS, external services) with minimum versions before any install command. Unmet prerequisites are the top cause of failed first-runs.
- Provide copy-pasteable install commands that work on a clean machine. Transcription errors are a primary source of friction.
- If the project supports multiple platforms, show distinct command blocks for each with clear labels. Don't assume Unix-like shells.
- Include at least one fully-worked clone → install → run example early in the document. Proof-of-life validates the path.
- Provide uninstall or cleanup instructions alongside install. Reversibility is part of safety.

## Usage

- Include a Quickstart or Usage section with a minimal, runnable example that produces visible output. "Hello world" beats a feature tour.
- Show expected output after each command block. Unexplained silence breeds doubt.
- Document how to run the tests. If a contributor can't verify their change, they won't contribute.

## Commands & Code Blocks

- Put every command in a fenced code block tagged with the correct language (`bash`, `sh`, `console`, `pwsh`, `cmd`, `sql`, etc.). Enables syntax highlighting and copy buttons.
- Do not prefix command lines with shell prompts (`$`, `>`, `#`) unless demonstrating output inline. Prompt characters break copy-paste.
- Use clearly marked placeholders like `<YOUR_API_KEY>` for user-supplied values and define each one once. Prevents misuse.
- Don't include commands that require mid-command manual edits; show how to export an environment variable instead.
- Keep code-block lines under 80 characters; don't soft-wrap inside a code block. Wrapping breaks copy-paste.

## Configuration

- Document required and optional configuration options with clear defaults, using a table or structured list. Centralizing knobs prevents guesswork.
- For environment variables, list name, type, default, and whether required in a code block or table. Variables described only in prose get missed.

## Troubleshooting

- Include a Troubleshooting or FAQ section listing common errors with symptom, cause, and fix. Anticipation prevents dead-ends.
- Link to the issue tracker and any community support channel. Clear support paths reduce friction.

## Links & Assets

- Ensure every link resolves: internal anchors, local file paths, and external URLs. Broken links erode trust and signal neglect.
- Prefer relative links for repo-local files; use absolute URLs only when the README is consumed on external mirrors (npm, PyPI). Relative links survive forks; absolute links survive package registries — pick per project.
- Provide descriptive, non-placeholder alt text for every image and badge. Required for accessibility.
- Keep embedded images under 500 KB each and total README assets under 2 MB. Repo page load matters on mobile and low-bandwidth connections.
- Prefer SVG or asciicast for terminal demos over animated GIFs. Smaller, scalable, with selectable text.
- Limit badges to ~3-5 placed under the title. More than that harms scanability. *(contested)*

## License & Contributing

- Name the license explicitly in the body (e.g., "MIT"), and link to a `LICENSE` file in the repo root. Legal clarity requires both the name and the canonical text.
- Include a Contributing section or link to `CONTRIBUTING.md`. A one-liner beats silence.

## Safety

- Never include real secrets, tokens, credentials, or internal hostnames in examples. Readers copy-paste; reviewers miss it.
- Don't recommend `curl … | sh` (or `iex (iwr …)`) installers without also documenting a manual alternative and a warning. Pipe-to-shell is a security posture users must opt into.
- Don't include destructive commands (`rm -rf`, `dd`, `mkfs`, `DROP DATABASE`, `--force`) in examples without an explicit warning callout. Accidental destruction is unrecoverable.
- Don't instruct readers to disable TLS verification, SELinux, or firewalls as a workaround. Document the real fix or file the bug.
- Use reserved example domains (`example.com`, `*.test`, `*.local`) and IPs (`127.0.0.1`, RFC 5737 ranges). Never use real hostnames or production IPs.
- Avoid `sudo` in examples when a non-privileged alternative exists. *(contested — some package managers legitimately require it.)*
- Link to a private security-disclosure channel (`SECURITY.md` or an email). Responsible disclosure protects users.

## Style & Formatting

- Write in clear, direct language. Use second person and imperative mood for instructions ("Run `npm install`", not "You should run…").
- Define jargon on first use; assume your reader is competent but new to the project.
- Keep prose lines under 120 characters in source. Reviewers read diffs, not rendered output.
- Use ASCII quotes and dashes inside code blocks. Smart quotes break shell copy-paste.
- Don't use emoji in headings. They break grep, anchor links, and screen readers. *(contested)*

## Correctness & Maintenance

- Ensure every command in the README runs successfully on a supported platform as of the last commit. Stale commands are the most common README defect.
- Update the README in the same commit as any behavior change it documents. Separate commits mean docs lose the race.
- Link to detailed documentation (`CONTRIBUTING`, `ARCHITECTURE`, `CHANGELOG`) rather than duplicating it. Single source of truth.
- Don't hand-maintain duplicates of `--help` output or version manifests. Regenerate or link.
- Don't leave `TODO`, `FIXME`, or `XXX` markers in a published README. They signal incompleteness.

## Rules Requiring Human Review

These rules matter but cannot be checked mechanically: whether the one-sentence description actually describes the project well; whether warnings on destructive commands are prominent enough; whether troubleshooting entries reflect real user pain; whether the example is genuinely minimal. Automated checks catch structure; code review catches meaning.