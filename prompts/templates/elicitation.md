You are an expert practitioner and author of technical best practices.

I am building a rules file that defines what "good" looks like for {{topic}}.
This rules file will be used by engineers and AI coding assistants as a
reference, so it must be specific, actionable, and opinionated.

Topic: {{topic}}
Context: {{topic_description}}

Please respond in TWO clearly-separated sections. The section headers must
appear verbatim as shown below — a downstream parser splits on them.

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
