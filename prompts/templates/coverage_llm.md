You are analyzing responses from multiple independent AI models about
the same topic. Your sole job is to produce a **rule × model coverage
matrix** — which rules appear in which models' responses.

Do not synthesize, rewrite, recommend, or draft a final rules file. Do
not grade the rules. Only cluster and tabulate.

You will receive N responses, each with a reasoning section and a rules
file. Inputs appear below, delimited by `===MODEL: <name>===` markers.

Produce the following output in markdown, in this order:

## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

A markdown table with these columns:

| Rule | Theme | Model A | Model B | ... | Count |

- **Rule** — a single concise imperative sentence summarizing the
  cluster ("Quote all shell variables to prevent word splitting.").
- **Theme** — the heading group most of the contributing rules lived
  under (e.g., Safety, Style, Error Handling).
- **One column per model**, in the order the models appear in the
  inputs. Use `✓` if the model raised that rule (in substance, not
  wording) and blank otherwise.
- **Count** — total number of models that raised the rule.

Sort rows by Count descending, then by Rule ascending. Use the exact
model names from the `===MODEL: <name>===` headers as the column
headers.

## Notes on clustering decisions

For any cluster where your judgment was non-obvious — rules that *could*
have gone into separate clusters, or phrasings so different that a
regex-based matcher would miss them — add a short bullet noting the
decision. This is the audit trail a human reader uses to catch
over-eager or under-eager clustering.

---

Inputs follow below.

{{collected_responses}}
