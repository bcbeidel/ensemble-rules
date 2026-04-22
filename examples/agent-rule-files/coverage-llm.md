## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Write each rule as a single imperative sentence. | Content/Style | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Scope paths narrowly via frontmatter globs. | Structure/Scoping | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Include YAML/metadata frontmatter at the top of each file. | Structure | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Keep each rule file small / under a size or line cap. | Performance/Structure | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Keep each file single-purpose / one concern. | Structure/Maintainability | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Group rules under predictable headings (Structure, Safety, etc.). | Structure/Style | ✓ | ✓ | ✓ | ✓ |  |  | 4 |
| Attach a short rationale to each rule. | Content | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Make rules concrete, falsifiable, and verifiable. | Correctness | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Encode only conventions the codebase actually follows (no aspirational rules). | Correctness/Maintainability |  |  | ✓ | ✓ |  |  | 2 |
| Never include secrets, tokens, or credentials in rule files. | Safety | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Periodically review / assign owners to rule files to prevent rot. | Maintainability | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Avoid hedging language ("should", "maybe", "consider"); use absolute/imperative wording. | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Don't duplicate rules already enforced by linters/formatters. | Correctness/Performance |  |  | ✓ | ✓ |  |  | 2 |
| Link to canonical/external docs instead of embedding long content. | Content/Performance | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Define precedence/conflict-resolution for overlapping rule files. | Loading/Precedence | ✓ |  | ✓ |  |  |  | 2 |
| Forbid destructive commands and require confirmation for risky operations. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Treat rule files as code: review, version, and change-control them. | Maintainability | ✓ |  | ✓ |  | ✓ |  | 3 |
| Require/mandate tests for rules or generated code. | Testing/Correctness | ✓ | ✓ |  |  |  |  | 2 |
| Specify exact tools, libraries, or versions by name. | Correctness | ✓ |  | ✓ |  |  |  | 2 |
| Provide a fallback behavior for ambiguity or unmatched cases. | Error Handling | ✓ |  |  |  |  | ✓ | 2 |
| Remove or update rules violated frequently in practice. | Maintainability |  |  | ✓ | ✓ |  |  | 2 |
| Put universally-applicable rules in top-level memory, not path-scoped files. | Scoping | ✓ |  | ✓ |  |  |  | 2 |
| Use consistent file naming that reflects scope/purpose. | Structure | ✓ |  |  |  | ✓ |  | 2 |
| State exceptions to a rule explicitly when they exist. | Correctness |  |  | ✓ | ✓ |  |  | 2 |
| Don't paste untrusted external content into rule files (injection surface). | Safety |  |  | ✓ |  |  |  | 1 |
| Use narrow code examples only when the rule's shape is non-obvious. | Content |  |  | ✓ |  | ✓ |  | 2 |
| Prefer positive framing over negative prohibitions. | Style |  |  |  |  | ✓ |  | 1 |
| Prefer negative rules for defaults the base model gets wrong. | Content |  |  | ✓ |  |  |  | 1 |
| Don't weaken security, logging, or validation via rules. | Safety |  |  |  |  | ✓ |  | 1 |
| Include license headers / license compliance guidance. | Safety | ✓ |  |  |  |  |  | 1 |
| Sanitize or synthesize PII in examples/fixtures. | Safety | ✓ |  |  |  |  |  | 1 |
| Require idempotent, reversible migrations with rollbacks. | Safety | ✓ |  |  |  |  |  | 1 |
| Don't fetch remote code/data during generation. | Safety | ✓ |  |  |  |  |  | 1 |
| Don't execute shell commands; propose them instead. | Safety | ✓ |  |  |  |  |  | 1 |
| Validate frontmatter and glob coverage in CI. | Tooling/CI | ✓ |  |  |  |  |  | 1 |
| Lint rule files for banned hedge words. | Tooling/CI | ✓ |  |  |  |  |  | 1 |
| Enforce a review_by expiration date for rule files. | Maintainability | ✓ |  |  |  |  |  | 1 |
| Bump a version field on substantive rule edits. | Maintainability | ✓ |  |  |  |  | ✓ | 2 |
| Surface a generated index of rules by path in docs. | Tooling | ✓ |  |  |  |  |  | 1 |
| Restate applicable rules before making code changes. | Assistant Interaction | ✓ |  |  |  |  |  | 1 |
| Propose minimal-scope diffs that reference rule IDs. | Assistant Interaction | ✓ |  |  |  |  |  | 1 |
| Don't override rules via prompt; edit the rule file. | Assistant Interaction | ✓ |  |  |  |  |  | 1 |
| When rules conflict or are impossible, stop and ask owners. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Prefer no change over unsafe change under uncertainty. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Reuse existing helpers before writing new ones. | Performance | ✓ |  |  |  |  |  | 1 |
| Set function/module size caps in generated code. | Performance | ✓ |  |  |  |  |  | 1 |
| Mirror CI/linter configs exactly. | Correctness | ✓ |  |  |  |  |  | 1 |
| State the minimum language standard / runtime version. | Correctness | ✓ |  |  |  |  |  | 1 |
| Define directory-level architectural boundaries. | Correctness | ✓ |  |  |  |  |  | 1 |
| Co-locate rule files with the code they govern. | Structure |  |  | ✓ |  |  |  | 1 |
| Open with a one-line scope statement. | Structure |  |  | ✓ |  |  |  | 1 |
| Don't explain language/framework basics the model knows. | Style |  |  | ✓ |  |  |  | 1 |
| Use fenced code blocks with language tags. | Style |  |  | ✓ |  |  |  | 1 |
| Test new rule files by observing whether they fire in a representative task. | Maintainability |  |  | ✓ |  |  |  | 1 |
| Don't include single-file-only rules in shared rule files. | Maintainability |  |  |  | ✓ |  |  | 1 |
| Avoid cargo-culting rules from other projects. | Maintainability |  |  |  | ✓ |  |  | 1 |
| Don't mix unrelated domains (e.g., backend + frontend) in one file. | Structure |  |  |  | ✓ |  |  | 1 |
| Forbid certain third-party libraries only with strong justification. | Correctness |  |  |  | ✓ |  |  | 1 |
| Profile code before applying performance optimizations. | Performance |  | ✓ |  |  |  |  | 1 |
| Only recommend optimizations when justified. | Performance |  | ✓ |  |  |  |  | 1 |
| Define and use jargon only after explaining it. | Style |  | ✓ |  |  |  | ✓ | 2 |
| Document expected behavior for each rule. | Error Handling |  | ✓ |  |  |  |  | 1 |
| Always handle errors explicitly in code samples. | Error Handling |  | ✓ |  |  |  | ✓ | 2 |
| Specify test types (unit vs integration). | Testing |  | ✓ |  |  |  |  | 1 |
| Enforce a maximum line length (e.g., 80 chars). | Style |  |  |  |  |  | ✓ | 1 |
| Don't use conditional logic or variables in rules. | Performance |  |  |  |  |  | ✓ | 1 |
| Don't nest rules deeply within markdown sections. | Structure |  |  |  |  |  | ✓ | 1 |
| Prioritize essential rules over optional ones. | Performance |  |  |  |  |  | ✓ | 1 |
| Use markdown structure (headings, lists) for readability. | Style |  |  |  |  | ✓ |  | 1 |
| State each rule on its own line as a list item. | Style |  |  |  |  | ✓ |  | 1 |

## Notes on clustering decisions

- **"Scope paths narrowly"** (5 models) vs **"Include YAML frontmatter"** (4 models): I kept these separate because some models stressed *having* frontmatter as a loading prerequisite while others stressed *narrowness* of the globs. Gemini and grok discuss both; gpt-5 and opus explicitly separate them.
- **"Keep each file single-purpose"** vs **"Keep each rule file small"**: Related but distinct — size caps (bytes/lines) vs topical scope. gpt-5, opus, and haiku raised both; I did not merge.
- **"Make rules concrete/falsifiable"** is a broad cluster: includes gpt-5's "concrete, checkable constraints", 4o-mini's "single actionable directive / unambiguous", opus's "falsifiable against a diff", haiku's "objectively falsifiable", and gemini's "avoid vague rules". A stricter matcher would split these, but the intent overlaps heavily.
- **"Avoid hedging language"** clusters gpt-5's "Do/Don't/Must, not should/might", opus's "Don't hedge", haiku's imperative vs. suggestion, and gemini's imperative-mood advocacy.
- **"Link to canonical docs"** clusters gpt-5's explicit rule, haiku's "link to external docs", gemini's "reference canonical documentation", and grok's "reference external standards". 4o-mini and opus do not say this.
- **Safety sub-rules** (destructive commands, secrets, remote fetches, PII, migrations) were kept as separate rows because different models named different specific hazards; only "no secrets" appears across multiple models. A coarser matcher might merge them all under a single "safety guardrails" rule.
- **"Treat rule files as code / review them"** merges gemini's code-review framing with gpt-5's owner/version/review_by requirements and opus's review-on-code-change rule. Arguable whether gpt-5's "owners in frontmatter" belongs here vs. under a separate "assign owners" rule (which I collapsed into periodic review).
- **"Bump a version field"**: gpt-5 calls for versioning on substantive edits; grok lists a version field in frontmatter. Different motivations (change tracking vs. rollback), but I merged.
- **"Define and use jargon only after explaining it"** merges 4o-mini's "avoid jargon unless defined" and grok's "don't use jargon without definition".
- **"Always handle errors explicitly in code samples"** merges 4o-mini's rule with grok's "mandate error handling in all rule examples".
- **Opus's "Don't use `paths: **/*`"** is essentially the same as gpt-5's "universal rules go in top-level memory" — merged.
- **Positive vs negative framing**: gemini prefers positive; opus prefers negative for base-model defaults. I kept these as two separate rows because they are in tension, not the same rule.
- **Haiku's "Don't forbid third-party libraries without justification"** and gpt-5's "Enumerate allowed dependency scopes and pin levels" are about dependency policy but point in opposite directions; not merged.