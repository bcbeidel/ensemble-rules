You are synthesizing best-practices guidance on {{topic}} from multiple
independent AI models. Your job is to produce a single authoritative rules
file that represents the consensus view while honestly surfacing
disagreement.

You will receive N responses, each with a reasoning section and a rules
file. Inputs appear below, delimited by `===MODEL: <name>===` markers.

Produce the following output in markdown, in this order:

## 1. Consensus Rules

Rules that appear (in substance, not wording) across a majority of the
inputs. Write each as a single imperative sentence + one-line rationale.
Group by theme.

For each consensus rule, note whether the phrasing across models is
**near-identical** (suggests a shared training source) or **substantively
similar but differently worded** (suggests genuine convergence). Flag the
distinction inline — e.g., `(near-identical wording across GPT-5 and
Claude)` — because it changes how much independent signal the rule
carries.

## 2. Strong Minority Rules

Rules that appear in only one or two inputs but that you assess as
well-reasoned and worth including. Note which model(s) raised them and
why you kept them.

## 3. Divergences

Points where models genuinely disagree. For each, summarize the positions,
name who took each side, and give your synthesized recommendation with
reasoning.

## 4. Notable Omissions

Rules that appear in a majority of inputs but are conspicuously absent
from one model's response. List each omission with the rule and the
model that skipped it. Sometimes the absence is the signal — do not
dismiss it.

## 5. Final Rules File

A clean, standalone markdown rules file combining sections 1 and 2. This
is the artifact engineers and coding assistants will actually use. It
should stand on its own without the preceding analysis.

---

Inputs follow below.

{{collected_responses}}
