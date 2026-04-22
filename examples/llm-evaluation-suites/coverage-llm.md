## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Include safety tests (prompt injection, jailbreaks, harmful content, PII). | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Instrument and track cost and latency per run. | Performance | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Separate datasets, scoring logic, and harness/execution code. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Validate LLM-as-judge against human-labeled/ground-truth calibration set. | Scoring | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Version and pin datasets, prompts, models, and configs. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Include adversarial, edge, and OOD cases in datasets. | Datasets | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Pin the judge model version to prevent drift. | Scoring | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Report per-slice/per-tag/per-criterion results, not only aggregates. | Reporting | ✓ |  | ✓ | ✓ |  |  | 3 |
| Run multiple samples per case and report mean + variance / CIs for stochastic runs. | Determinism | ✓ |  | ✓ | ✓ |  |  | 3 |
| Store raw outputs / run artifacts (immutable) for later diagnosis. | Reproducibility | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Stratify tests into tiered suites (smoke/regression/full). | Structure | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Tag/annotate test cases with metadata (capability, author, intent). | Structure | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Use exact/structural matching only for objectively constrained outputs. | Scoring | ✓ | ✓ | ✓ | ✓ |  |  | 4 |
| Use rubric-based scoring decomposed into clear/binary criteria. | Scoring | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Block releases on safety regressions. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Compare against baselines and alert/gate on regressions. | Regression Tracking | ✓ | ✓ |  | ✓ | ✓ | ✓ | 5 |
| Define acceptance thresholds / budgets before runs. | Regression Tracking | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Evaluate RAG retrieval separately (recall@k, MRR) from generation. | RAG | ✓ |  | ✓ |  |  |  | 2 |
| Handle errors loudly; don't silently retry flaky tests into passes. | Error Handling | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Keep a private held-out set never used for iteration. | Datasets | ✓ |  | ✓ | ✓ |  |  | 3 |
| Log full judge reasoning/rationales with scores. | Scoring |  |  | ✓ | ✓ | ✓ |  | 3 |
| Log structured run metadata (model, temperature, seed, prompt hash, git SHA). | Reproducibility | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Prefer temperature=0 for deterministic regression runs. (contested) | Determinism | ✓ |  | ✓ |  | ✓ |  | 3 |
| Randomize candidate/position order in judge prompts to mitigate bias. | Scoring | ✓ |  | ✓ |  |  |  | 2 |
| Require structured (JSON/schema) judge output. | Scoring | ✓ |  |  | ✓ |  |  | 2 |
| Cache evaluation results keyed on inputs+params. | Performance | ✓ |  |  | ✓ |  |  | 2 |
| Constrain or disallow chain-of-thought from judges. (contested) | Scoring | ✓ |  |  |  |  |  | 1 |
| Disable caches or separate cold vs warm timings during perf runs. | Performance | ✓ |  |  |  |  |  | 1 |
| Document dataset sourcing, labeling, and known limits. | Datasets | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Enforce cost/budget caps per run and fail when exceeded. | Performance | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Evaluate agents at per-step level (tool choice, arguments), not only end state. | Agents | ✓ |  | ✓ |  |  |  | 2 |
| Include citation/grounding checks for RAG outputs. | RAG | ✓ |  |  |  |  |  | 1 |
| Limit or label synthetic data; don't let it replace human-curated cases. (contested) | Datasets | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Measure inter-rater agreement (Cohen's kappa etc.) on human labels. | Datasets |  |  |  | ✓ |  |  | 1 |
| Name test cases descriptively by capability, not by number. | Style |  | ✓ | ✓ | ✓ |  |  | 3 |
| Never use the same model family as judge and generator. | Scoring |  |  | ✓ |  |  |  | 1 |
| Prefer pairwise comparison for subtle quality differences. (contested) | Scoring | ✓ |  | ✓ |  |  |  | 2 |
| Produce per-run reports highlighting deltas, top failures, and cost/latency. | Reporting | ✓ |  |  | ✓ |  |  | 2 |
| Provide a README / CONTRIBUTING guide for the suite. | Documentation | ✓ |  |  | ✓ |  |  | 2 |
| Require human review / sign-off for regressions or dataset changes. | Governance | ✓ |  |  | ✓ |  |  | 2 |
| Run the suite via a single CLI command / easy local execution. | Structure |  |  | ✓ | ✓ | ✓ |  | 3 |
| Store test cases in human-readable structured files (YAML/JSON/JSONL). | Structure | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Timebox/timeout model and tool calls. | Error Handling | ✓ |  |  | ✓ |  |  | 2 |
| Treat unparsable / schema-invalid outputs as failures. | Error Handling | ✓ |  |  | ✓ |  |  | 2 |
| Use append-only / immutable datasets; don't mutate in place. | Datasets | ✓ |  | ✓ |  |  |  | 2 |
| Validate custom scoring code with its own tests. | Scoring |  |  |  |  | ✓ |  | 1 |
| Version-control judge prompts and rubrics. | Scoring |  |  |  | ✓ | ✓ |  | 2 |
| Avoid overfitting the eval set; keep a blind holdout used only for reporting. | Datasets | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Ban BLEU/ROUGE/string-similarity as primary metrics for free-form generation. | Scoring |  |  |  | ✓ |  |  | 1 |
| Deduplicate/decontaminate test content against training data. | Datasets | ✓ |  | ✓ | ✓ |  |  | 3 |
| Ensure minimum dataset size / statistical power (e.g., 50–200+ per category). | Datasets |  |  |  | ✓ |  |  | 1 |
| Include bias/fairness tests and report disaggregated metrics. | Safety | ✓ |  |  | ✓ | ✓ | ✓ | 4 |
| Mock / record–replay external tools and dependencies. | Structure | ✓ |  |  |  | ✓ |  | 2 |
| Redact secrets and PII from logs/prompts. | Security | ✓ |  |  |  |  |  | 1 |
| Review/audit evaluation suites periodically for drift and representativeness. | Governance | ✓ |  |  | ✓ |  |  | 2 |
| Use retries with backoff for transient API/network failures. | Error Handling |  |  |  | ✓ |  | ✓ | 2 |

## Notes on clustering decisions

- **"Separate datasets, scoring logic, and harness"** merges gpt-5's explicit three-way split, 4o-mini's "modular test cases", opus's data/code/rubric separation, haiku's co-location-but-separation guidance, and gemini's "separate test case data from evaluation logic". Grok's "modular components" is similar but framed around dataset/scoring/tracking modules; judged close enough to cluster — arguable.
- **"Version datasets, prompts, models, configs"** bundles several distinct sub-rules (version-control datasets, pin model versions, pin configs) that most models conflate. Haiku and gemini specifically emphasize VCS commits; opus emphasizes immutable content-addressed datasets. Kept as one cluster even though a stricter reading would split "pin runtime params" from "version dataset artifacts".
- **"Pin the judge model version"** kept separate from generic versioning because four models call it out explicitly as a distinct concern (judge drift).
- **"Use rubric-based scoring"** includes opus's "decompose into binary checks", haiku's "concrete examples per score level", and 4o-mini/grok's generic rubric preference. The binary-vs-Likert nuance is lost in clustering.
- **"Validate LLM-as-judge against ground truth"** and **"Pin judge model version"** could be one cluster about judge reliability; kept separate because the remediation differs (calibration vs. version pinning) and different models emphasize different ones.
- **"Include adversarial/edge/OOD cases"** merges RAG-specific adversarial chunks (opus), general adversarial cases (gpt-5, haiku), and diverse examples (grok). 4o-mini's "don't ignore edge cases" is tangential but included.
- **"Enforce cost/budget caps"** and **"Instrument cost/latency"** kept separate — the first is a gating behavior, the second is measurement. Some models (gpt-5, haiku, gemini) do both.
- **"Block releases on safety regressions"** overlaps with the general safety-testing rule but is a distinct governance stance; kept separate.
- **"Temperature=0 for determinism"** marked contested; opus and gpt-5 explicitly flag it as contested, gemini recommends it without the label.
- **"Limit synthetic data"** marked contested because gpt-5, opus, gemini, and grok all hedge on it; 4o-mini/haiku don't address it.
- **Regression tracking cluster** is broad: "compare against baselines / alert on regressions" covers gpt-5's dual-baseline, 4o-mini's "automated regression tracking", haiku's baseline rule, gemini's historical tracking, grok's thresholded alerts. A stricter reading would split "establish baseline" from "alert on regression" from "dual baseline".
- **"Avoid overfitting the eval set"** merges gpt-5's holdout rotation, opus's "don't tune against the same set", haiku's dev/val/test split, and grok's overfitting warning. Related to but distinct from "keep a private holdout".
- 4o-mini's response is notably sparser than others; its blank cells in many rows reflect genuine absence rather than clustering miss.
- Grok's rules are often generic ("do document", "do follow naming conventions") and were only counted when they substantively matched a specific rule from other models.