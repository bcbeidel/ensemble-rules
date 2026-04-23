You are synthesizing best-practices guidance on {{topic}} from multiple
independent AI models. Your job is to produce a single authoritative rules
file that represents the consensus view while honestly surfacing
disagreement.

You will receive N responses, each with a reasoning section, a rules
file, and a deterministic-validation section describing machine-checkable
rules. Inputs appear below, delimited by `===MODEL: <name>===` markers.

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

## 5. Shared Deterministic Checks

Cluster the deterministic-validation bullets across models and surface
the ones that multiple models converged on. The goal is to identify
checks general enough to be implemented once and reused across topics,
so they can live as scripts outside the rules file rather than being
re-described inline every time.

For each shared check, produce a bullet with:

- **Check** — a one-sentence description of what it verifies, written
  to stand alone (not tied to one model's wording).
- **Signal** — the input the check reads, reconciled across models
  (e.g., "raw source text", "parsed AST", "output of `shellcheck`").
- **Tool candidate** — if multiple models named the same off-the-shelf
  tool (e.g., `shellcheck SC2086`, `ruff E501`), name it. If models
  described equivalent checks without naming a tool, say "ad-hoc".
- **Raised by** — list the models that described this check.
- **Variance** — note any meaningful differences in how models defined
  the check (stricter vs. looser thresholds, different failure modes,
  etc.). If models agreed on substance, say so.

Then list **singleton checks** — deterministic checks that only one
model proposed but that look generally useful. One bullet each, same
structure, minus the variance field.

Do not generate code. Do not write scripts. The output of this section
is a catalog of candidates for later extraction into shared tooling;
describing them precisely is enough.

## 6. Final Rules File

A clean, standalone markdown rules file combining sections 1 and 2. This
is the artifact engineers and coding assistants will actually use. It
should stand on its own without the preceding analysis.

---

Inputs follow below.

{{collected_responses}}
