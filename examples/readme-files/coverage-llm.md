## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Include an Installation section with clear setup commands. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Include a License section naming the license and linking to the LICENSE file. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| List prerequisites (runtimes, tools, versions) before install steps. | Content | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Put commands in fenced code blocks with language tags. | Commands & Code | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use headings/subheadings to organize sections consistently. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Include a Quickstart or Usage section with a minimal working example. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Include a Contributing section or link to CONTRIBUTING. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Never include real secrets, tokens, or credentials in examples. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Start the README with a project title/H1 and a one-sentence description. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Include a Table of Contents for long READMEs. | Structure | ✓ | ✓ | ✓ | ✓ |  |  | 4 |
| Keep the README focused and link out to deeper docs rather than duplicating them. | Maintenance | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Provide descriptive alt text for images. | Style | ✓ |  | ✓ | ✓ |  |  | 3 |
| Include a Configuration section documenting environment variables and options. | Structure | ✓ |  |  | ✓ | ✓ |  | 3 |
| Include a Troubleshooting/FAQ section for common errors. | Structure | ✓ |  |  | ✓ | ✓ |  | 3 |
| Limit badges to a small set of meaningful, auto-updated ones. | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Verify/ensure all links (internal and external) resolve. | Correctness | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Don't prefix shell commands with prompts like `$` or `>`. | Commands & Code | ✓ |  | ✓ |  | ✓ |  | 3 |
| Avoid or warn about `curl \| sh`-style installers. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Warn on destructive commands (rm -rf, DROP, etc.). | Safety | ✓ | ✓ | ✓ |  |  | ✓ | 4 |
| Use placeholders (e.g., `<YOUR_API_KEY>`) instead of real values. | Safety/Commands | ✓ |  |  | ✓ | ✓ |  | 3 |
| Keep lines within a reasonable length limit (~80–120 chars). | Style | ✓ |  | ✓ |  |  | ✓ | 3 |
| Link to issue tracker / support channels. | Support | ✓ |  |  | ✓ |  |  | 2 |
| State supported platforms and OS/version ranges explicitly. | Content | ✓ |  |  | ✓ |  |  | 2 |
| Keep commands/examples copy-pasteable (no wrapping or special chars). | Commands & Code | ✓ |  |  | ✓ | ✓ |  | 3 |
| Optimize the Quickstart to the shortest path to success (few commands). | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Keep the README as a stable entry-point updated alongside project changes. | Maintenance |  |  | ✓ | ✓ | ✓ | ✓ | 4 |
| Show expected output alongside example commands. | Commands & Code |  |  |  | ✓ | ✓ |  | 2 |
| Use relative links for in-repo assets. | Correctness | ✓ |  |  |  | ✓ |  | 2 |
| Avoid sudo or require least-privilege in examples. | Safety | ✓ |  |  |  |  | ✓ | 2 |
| Don't skip heading levels (H1→H2→H3). | Structure |  |  | ✓ | ✓ |  |  | 2 |
| Explain the problem the project solves / value proposition. | Content |  |  | ✓ | ✓ | ✓ |  | 3 |
| Avoid hardcoding version numbers that live elsewhere. | Maintenance |  |  | ✓ |  | ✓ | ✓ | 3 |
| Use imperative / second-person voice for instructions. | Style |  |  | ✓ | ✓ |  |  | 2 |
| Provide uninstall or cleanup instructions. | Commands & Code | ✓ |  |  | ✓ |  |  | 2 |
| Avoid emoji in headings. | Style |  |  | ✓ |  |  |  | 1 |
| Keep embedded images/assets small; prefer SVG/asciicast over heavy GIF. | Performance |  |  | ✓ |  |  |  | 1 |
| Ensure commands in the README actually run on supported platforms (CI-tested). | Correctness |  |  | ✓ | ✓ |  |  | 2 |
| Keep the README under a length limit (e.g., ~500 lines / 10 KB). | Length/Performance |  |  | ✓ |  |  | ✓ | 2 |
| Provide a security contact / responsible disclosure policy. | Safety | ✓ |  |  | ✓ |  |  | 2 |
| Give a "next steps" pointer to deeper docs or examples. | Content | ✓ | ✓ |  |  |  |  | 2 |
| Provide platform-specific instructions when multiple OSes are supported. | Content |  |  |  | ✓ |  |  | 1 |
| Avoid smart quotes / non-ASCII in code blocks. | Style |  |  |  | ✓ |  |  | 1 |
| Avoid using real production URLs/IPs in examples (use reserved ranges/example.com). | Safety |  |  |  | ✓ |  |  | 1 |
| Avoid jargon without definitions. | Style |  | ✓ |  | ✓ |  | ✓ | 3 |
| Use consistent tense/voice throughout. | Style |  | ✓ |  |  |  |  | 1 |
| Use Markdown (prefer it over raw HTML). | Style | ✓ | ✓ |  |  |  |  | 2 |
| Mention risks/warnings for the project. | Safety | ✓ | ✓ |  |  |  | ✓ | 3 |
| Provide a file/directory structure overview for larger projects. | Content |  |  |  | ✓ |  |  | 1 |
| Document how to run the tests. | Content |  |  | ✓ |  |  |  | 1 |
| Indicate last-tested versions / maintenance status. | Maintenance |  |  |  | ✓ |  |  | 1 |
| Don't include placeholder text like "TODO" in published READMEs. | Content |  |  |  |  |  | ✓ | 1 |
| Track the README in version control. | Maintenance |  |  |  |  |  | ✓ | 1 |
| Recommend isolated environments (Docker/venv) for testing. | Safety | ✓ |  |  |  |  | ✓ | 2 |
| Prefer caching-friendly package managers over ad-hoc scripts. | Performance | ✓ |  |  |  |  |  | 1 |
| Include multiple examples when the tool has multiple modes. | Content |  |  |  | ✓ |  |  | 1 |

## Notes on clustering decisions

- **"Start with H1 + one-sentence description"** merges two near-universal but separately phrased rules: gpt-5 and opus separate "H1 on line 1" from "one-sentence elevator pitch", while grok and haiku frame it as a single "title + overview" rule. Treated as one cluster since every model is arguing for the same front-matter.
- **"Keep the README focused / link out to deeper docs"** and **"Avoid duplicating content elsewhere"** were merged — multiple models phrase it either as a maintenance rule (don't duplicate) or a structure rule (link, don't mirror). A stricter matcher would split these.
- **"Limit badges"** includes both "limit count / reduce noise" (gpt-5, opus, gemini) and haiku's distinct "only include auto-updated badges" rule. They overlap in intent (signal vs. noise) but haiku's rule is really about staleness; borderline cluster.
- **"Verify links resolve"** merges gpt-5's "all markdown links resolve" with gemini's "external links active" and opus's "relative links valid after moves" and haiku's "use absolute URLs". These are arguably three different rules (link correctness, relative vs absolute, link rot) but all target the broader "links work" concern. Split candidates.
- **"Copy-pasteable commands"** merges gpt-5's "copy-pastable (no prompts)", gemini's "fully copy-pasteable", and haiku's "no smart quotes / no manual-edit placeholders". I kept the no-prompt rule as a separate row because it's a distinct mechanical check that three models call out explicitly.
- **"Warn on destructive commands"** and **"Mention project risks/warnings"** were kept separate: the former is specifically about `rm -rf`/DROP-style examples, the latter is grok/4o-mini/gpt-5's broader "flag risky actions" guidance. Some overlap.
- **"Quickstart ≤ N commands / shortest path"** merges gpt-5's explicit "≤3 commands", opus's "≤5 commands or use a script", and haiku's "2-minute to output" — same underlying principle, different thresholds.
- **"Prerequisites before install"** is folded into the broader "list prerequisites" cluster since every model that mentions prerequisites implies ordering; haiku alone states the ordering explicitly.
- **"Avoid jargon"** clusters 4o-mini's "don't use excessive jargon", haiku's "avoid jargon unless expected", and grok's "don't use jargon without explanation" — phrasings differ but intent matches.
- **"Use Markdown / prefer Markdown over HTML"** merges gpt-5's anti-HTML rule with 4o-mini's "use Markdown for formatting" — these are arguably different (one is prescriptive, one proscriptive) but I treated as one cluster.
- **Haiku has many very granular rules** (e.g., separate rules for libraries vs CLIs vs web apps, env-var formatting, multiple-examples requirement) that no other model states. Most collapse into the single-example/quickstart cluster; a stricter matcher would leave them as singletons.
- **"Recommend isolated environments"** clusters gpt-5's "offer a containerized run option" with grok's "use Docker/venv for testing" — gpt-5 frames it as performance/reproducibility, grok as safety. Borderline.