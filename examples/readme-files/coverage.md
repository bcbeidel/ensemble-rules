# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Limit the use of badges to essential status indicators like build status and license.** | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| **Avoid hardcoding version numbers that are defined elsewhere.** | Correctness & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Do not include command-line prompts (e.g., `$`, `>`) in code snippets.** | Correctness & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Do not include secrets, tokens, or private keys in examples.** | Safety |  |  |  |  | ✓ |  | 1 |
| **End with "Contributing" and "License" sections.** | Structure & Content |  |  |  |  | ✓ |  | 1 |
| **Ensure all installation and execution commands are fully copy-pasteable.** | Correctness & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Explain the purpose and risk of any command that pipes from `curl` to a shell.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Follow the summary with a concise "Why" or "Problem Statement" section.** | Structure & Content |  |  |  |  | ✓ |  | 1 |
| **Include sections for Prerequisites, Installation, and Usage.** | Structure & Content |  |  |  |  | ✓ |  | 1 |
| **Place a `LICENSE` file in the root and link to it.** | Structure & Content |  |  |  |  | ✓ |  | 1 |
| **Prefer linking to detailed documents over embedding their content.** | Structure & Content |  |  |  |  | ✓ |  | 1 |
| **Provide a "Common Workflows" or "Examples" section.** | Structure & Content |  |  |  |  | ✓ |  | 1 |
| **Start with a one-sentence project summary.** | Structure & Content |  |  |  |  | ✓ |  | 1 |
| **Use Markdown headings (`##`, `###`) to create a scannable document outline.** | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| **Use fenced code blocks with language identifiers for all code snippets.** | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| **Use relative links for all references to files within the repository.** | Correctness & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Use safe and generic placeholders for credentials, like `<YOUR_API_KEY>`.** | Safety |  |  |  |  | ✓ |  | 1 |
| **Use tables to present structured data like configuration options.** | Style & Formatting |  |  |  |  | ✓ |  | 1 |
| **Verify all external links are active and point to the correct resource.** | Correctness & Maintainability |  |  |  |  | ✓ |  | 1 |
| Avoid duplicating instructions that are generated or documented elsewhere; link instead | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid sudo in example commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Call out irreversible actions with an explicit WARNING and safer alternatives | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do detail prerequisites explicitly | Content |  | ✓ |  |  |  |  | 1 |
| Do employ markdown features like code blocks and emphasis sparingly but effectively | Style |  |  |  |  |  | ✓ | 1 |
| Do encourage contributions to the README via the project's workflow | Maintainability |  |  |  |  |  | ✓ | 1 |
| Do explain where to go next after setup or usage, such as contributing guidelines or links to documentation | Content |  | ✓ |  |  |  |  | 1 |
| Do include a project title and brief description | Structure |  | ✓ |  |  |  |  | 1 |
| Do include explicit warnings for potentially destructive actions, like file deletions | Safety |  |  |  |  |  | ✓ | 1 |
| Do include installation instructions with code snippets | Content |  | ✓ |  |  |  |  | 1 |
| Do include sections such as Prerequisites, Installation, Usage, and Contact Information | Structure |  | ✓ |  |  |  |  | 1 |
| Do include version-specific notes for dependencies (contested) | Content Accuracy |  |  |  |  |  | ✓ | 1 |
| Do keep the README file size under 10 KB | Performance |  |  |  |  |  | ✓ | 1 |
| Do link to external resources only if they are stable and relevant | Content Accuracy |  |  |  |  |  | ✓ | 1 |
| Do mention any potential risks or important warnings related to the installation or usage of the project | Safety |  | ✓ |  |  |  |  | 1 |
| Do not include destructive commands (rm -rf, dd, mkfs, DROP DATABASE) in examples | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize content into logical sections like "What is this?", "Installation", "Usage", and "Contributing" | Structure |  |  |  |  |  | ✓ | 1 |
| Do provide a table of contents for extensive READMEs | Structure |  | ✓ |  |  |  |  | 1 |
| Do provide usage examples where applicable | Content |  | ✓ |  |  |  |  | 1 |
| Do recommend using isolated environments (e.g., Docker) for testing | Safety |  |  |  |  |  | ✓ | 1 |
| Do regularly review and update the README as the project evolves | Maintenance |  | ✓ |  |  |  |  | 1 |
| Do start with a descriptive title and project overview | Structure |  |  |  |  |  | ✓ | 1 |
| Do treat the README as code; version it with the project and automate updates where possible | Maintainability |  |  |  |  |  | ✓ | 1 |
| Do use Markdown for formatting | Style |  | ✓ |  |  |  |  | 1 |
| Do use a consistent tense and voice throughout the document for professional tone and clarity | Style |  | ✓ |  |  |  |  | 1 |
| Do use headings and subheadings to organize sections | Structure |  | ✓ |  |  |  |  | 1 |
| Do use headings, subheadings, and bullet points consistently | Structure |  |  |  |  |  | ✓ | 1 |
| Do verify all instructions against the current codebase before committing changes | Content Accuracy |  |  |  |  |  | ✓ | 1 |
| Do write in clear, concise language with active voice and short sentences | Style |  |  |  |  |  | ✓ | 1 |
| Document how to run the tests | Content |  |  | ✓ |  |  |  | 1 |
| Don't assume users have administrative privileges; specify requirements clearly | Safety |  |  |  |  |  | ✓ | 1 |
| Don't bury key instructions deep in the file; place essentials like installation steps near the top (contested) | Structure |  |  |  |  |  | ✓ | 1 |
| Don't embed large images or unnecessary assets | Performance |  |  |  |  |  | ✓ | 1 |
| Don't exceed 80 characters per line in code examples | Style |  |  |  |  |  | ✓ | 1 |
| Don't hand-maintain a duplicate of `--help` output | Correctness & Maintenance |  |  | ✓ |  |  |  | 1 |
| Don't hardcode dynamic information like version numbers; use build scripts or placeholders | Maintainability |  |  |  |  |  | ✓ | 1 |
| Don't include `curl … \| sh` installers without also documenting a manual alternative | Safety |  |  | ✓ |  |  |  | 1 |
| Don't include placeholder text like "TODO" in published READMEs | Content Accuracy |  |  |  |  |  | ✓ | 1 |
| Don't instruct readers to disable TLS verification, SELinux, or firewalls as a workaround | Safety |  |  | ✓ |  |  |  | 1 |
| Don't let issues go unaddressed | Maintenance |  | ✓ |  |  |  |  | 1 |
| Don't put real secrets, tokens, or internal hostnames in examples | Safety |  |  | ✓ |  |  |  | 1 |
| Don't use emoji in headings | Style |  |  | ✓ |  |  |  | 1 |
| Don't use excessive jargon or technical terms without explanations | Style |  | ✓ |  |  |  |  | 1 |
| Don't use jargon without explanation unless it's industry-standard | Style |  |  |  |  |  | ✓ | 1 |
| Ensure all Markdown links resolve (internal anchors, local files, and external URLs) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ensure all local images and assets exist and render | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ensure every command in the README runs successfully on a supported platform as of the last commit | Correctness & Maintenance |  |  | ✓ |  |  |  | 1 |
| Follow the H1 with a single-sentence description of what the project is | Structure |  |  | ✓ |  |  |  | 1 |
| Follow the title with a one-sentence elevator pitch in plain language | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Give a copy-pasteable install command block that works on a clean machine | Content |  |  | ✓ |  |  |  | 1 |
| If the README exceeds ~200 lines, include a Table of Contents | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a table of contents only when the rendered document exceeds roughly 500 lines | Structure |  |  | ✓ |  |  |  | 1 |
| Include a “Configuration” section for environment variables and config files | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “Contributing” section or link to CONTRIBUTING | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “License” section that names the license and links to LICENSE | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “Prerequisites” section listing required runtimes, tools, and explicit versions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “Quickstart” or “Usage” section that gets to a working run | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a “Troubleshooting” or “FAQ” section for common errors and fixes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include an “Installation” section with step-by-step commands | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| It targets repositories with code users can run, install, or integrate, and it optimizes for first-time success, safety, and long-term maintainability | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep Quickstart to three commands or fewer; link out for advanced setup | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep embedded images under 500 KB each, and total README assets under 2 MB | Performance (of the document itself) |  |  | ✓ |  |  |  | 1 |
| Keep lines to 120 characters or fewer | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep lines under 120 characters in the source | Style |  |  | ✓ |  |  |  | 1 |
| Keep relative links valid after file moves | Correctness & Maintenance |  |  | ✓ |  |  |  | 1 |
| Keep status badges relevant and current (build, test, coverage) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the README focused; move deep guides to /docs and link to them | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep the README under 500 lines | Length |  |  | ✓ |  |  |  | 1 |
| Limit badges to five or fewer and place them under the title | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Limit badges to three at the top: build status, package version, license | Style |  |  | ✓ |  |  |  | 1 |
| Link to CHANGELOG, CONTRIBUTING, and architecture docs rather than restating them | Content |  |  | ✓ |  |  |  | 1 |
| Link to the issue tracker and support channels | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| List prerequisites (language runtime, OS, external services) with minimum versions before any install command | Content |  |  | ✓ |  |  |  | 1 |
| List the most common error(s) with fixes or links to solutions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Make commands copy-pastable; do not prefix with shell prompts like “$ ” or “>” | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mark destructive commands (`rm -rf`, `DROP`, `--force`) with an explicit warning callout | Safety |  |  | ✓ |  |  |  | 1 |
| Name the license explicitly and link to the repo’s LICENSE file | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never include real secrets, tokens, or passwords; use placeholders and demonstrate secure configuration | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never recommend piping curl or wget output into a shell (e.g., curl | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Offer a containerized run option when practical | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Optimize Quickstart for the shortest path to a successful run | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place a "Quickstart" or "Install" section above any conceptual or architectural content | Structure |  |  | ✓ |  |  |  | 1 |
| Prefer Markdown over raw HTML; use HTML only when Markdown cannot express the structure | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer SVG or asciicast for terminal demos over animated GIF | Performance (of the document itself) |  |  | ✓ |  |  |  | 1 |
| Prefer dependency installation methods that use caching (e.g., package managers) over ad-hoc scripts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefix shell examples with `$ ` only when showing output inline; otherwise omit the prompt | Style |  |  | ✓ |  |  |  | 1 |
| Provide a way to report security issues privately | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide alt text for every image | Performance (of the document itself) |  |  | ✓ |  |  |  | 1 |
| Provide descriptive alt text for every image and badge | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide uninstall or cleanup instructions alongside install | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide “Next steps” links to deeper docs or examples | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put "License" and "Contributing" as links to separate files, not inline sections | Structure |  |  | ✓ |  |  |  | 1 |
| Put commands in fenced code blocks tagged with the correct language (bash, sh, zsh, pwsh, cmd) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put the project name as the only H1, on line 1 | Structure |  |  | ✓ |  |  |  | 1 |
| Show a minimal runnable example that produces visible output | Content |  |  | ✓ |  |  |  | 1 |
| Show a minimal working example or demo command | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Start with a single H1 project title as the first non-empty line | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State supported platforms and version ranges explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| State the license by name in the README body (e.g., "MIT") even when linked | Content |  |  | ✓ |  |  |  | 1 |
| State the problem the project solves before listing features | Content |  |  | ✓ |  |  |  | 1 |
| This rules file defines what “good” looks like for project README.md files intended for public or internal consumption by engineers | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Update the README in the same commit as the behavior change it documents | Correctness & Maintenance |  |  | ✓ |  |  |  | 1 |
| Use heading levels sequentially (H1 → H2 → H3); never skip a level | Structure |  |  | ✓ |  |  |  | 1 |
| Use placeholders in angle brackets (<TOKEN>) and define each once | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use relative links for repo-local assets and docs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use second person ("you run", "you'll see") and imperative mood for instructions | Style |  |  | ✓ |  |  |  | 1 |
| Write commands as fenced code blocks with a language tag (```bash, ```console, ```sql) | Style |  |  | ✓ |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

