You are an expert practitioner and author of technical best practices.

I am building a rules file that defines what "good" looks like for {{topic}}.
This rules file will be used by engineers and AI coding assistants as a
reference, so it must be specific, actionable, and opinionated.

Topic: {{topic}}
Context: {{topic_description}}

Please respond in THREE clearly-separated sections. The section headers
must appear verbatim as shown below — a downstream parser splits on them.

## Section 1: Reasoning

Explain the principles, trade-offs, and reasoning behind what makes
{{topic}} good. Cover at minimum: readability, maintainability,
correctness, safety, performance, and common failure modes. Be honest
about contested areas where reasonable practitioners disagree.

## Section 2: Rules File

Produce a concise, scannable rules file as a markdown document. Structure
it as:

- A short preamble stating scope and intended audience.
- Grouped rules under clear headings (e.g., Structure, Error Handling,
  Style, Safety, Performance).
- Each rule as a single imperative sentence ("Do X." / "Don't Y.")
  followed by a one-line rationale.
- Mark any rule you consider contested with `(contested)`.

Do not hedge. This is a rules file, not a survey. If you have an opinion,
state it.

## Section 3: Deterministic Validation

For each rule in Section 2 that can be checked mechanically, describe the
check in enough detail that a competent engineer could implement it
elsewhere. **Do not write the script.** Describe it.

Not every rule belongs here. A rule belongs here only if a machine can
decide pass/fail from inputs that are cheap to obtain (source text, a
parsed AST, a file on disk, the output of a widely-available tool). If a
rule requires taste, context, or human judgment, leave it out and say so
is fine — this section can be short or list only a subset of Section 2.
Do not invent checks for rules that don't warrant them.

For each applicable rule, produce a bullet with these labeled fields:

- **Rule** — quote the rule from Section 2 verbatim (or close enough to
  match unambiguously).
- **Signal** — what input the check reads (e.g., "raw source file",
  "AST node of type X", "output of `shellcheck --format=json`",
  "presence of a specific shebang line").
- **Check** — the decision procedure in plain prose. Be precise about
  what counts as a violation. If an existing off-the-shelf tool already
  implements it, name the tool and the relevant rule code
  (e.g., "shellcheck SC2086", "ruff E501").
- **Failure mode** — what a violation looks like, ideally with a
  one-line example of offending input.
- **Limitations** — known false positives or false negatives, or cases
  where the check would need to be relaxed.

Group bullets by the same theme headings used in Section 2 so the
mapping is obvious. If no rules in Section 2 admit a deterministic
check, write a single line stating that explicitly; do not fabricate
checks to fill the section.
