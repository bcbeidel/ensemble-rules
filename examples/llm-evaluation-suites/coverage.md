# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| (contested) Do prioritize rubric-based evaluations over exact match scores when assessing qualitative aspect | Contestation |  | ✓ |  |  |  |  | 1 |
| **Alert on per-slice regressions, not only aggregate.** — Aggregates hide the failures users notice | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Block merges on safety regressions; require review on capability regressions.** — Not all regressions are equal | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Calibrate every LLM-judge against human labels on a holdout.** Report agreement (Cohen's κ or similar) and re-calibrate when the judge model changes | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Cap synthetic data at a known fraction and label it.** Never let synthetic examples silently dominate | Dataset Design |  |  | ✓ |  |  |  | 1 |
| **Decompose rubrics into binary checks.** Five yes/no criteria beats one 1–5 score | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Define a cost budget per eval case and fail the run if exceeded.** — Budgets prevent silent cost explosions | Cost & Latency |  |  | ✓ |  |  |  | 1 |
| **Don't aggregate scores across incommensurable rubrics into a single headline number.** — It's uninterpretable and easy to game | Anti-Patterns (Don't Do These) |  |  | ✓ |  |  |  | 1 |
| **Don't delete failing cases because they're "unfair."** Mark them known-hard and track them | Anti-Patterns (Don't Do These) |  |  | ✓ |  |  |  | 1 |
| **Don't ship an eval suite without a human-labeled calibration set, however small.** — Ungrounded metrics drift undetected | Anti-Patterns (Don't Do These) |  |  | ✓ |  |  |  | 1 |
| **Don't tune prompts against the same eval set you report scores on.** — That's overfitting; keep a blind holdout | Anti-Patterns (Don't Do These) |  |  | ✓ |  |  |  | 1 |
| **Don't use a 1–5 Likert from an LLM judge as a primary metric.** — Judges cluster on 3 and 4; signal is weak | Anti-Patterns (Don't Do These) |  |  | ✓ |  |  |  | 1 |
| **Evaluate retrieval and generation separately before evaluating end-to-end.** — Composite scores hide which stage regressed | Agents & RAG |  |  | ✓ |  |  |  | 1 |
| **Fail loudly on API errors; never silently retry into a pass.** — Flaky green is worse than red | Structure & Code |  |  | ✓ |  |  |  | 1 |
| **For agents, evaluate per-step decisions (tool choice, args) in addition to final outcome.** — End-to-end success masks broken intermediate reasoning | Agents & RAG |  |  | ✓ |  |  |  | 1 |
| **Include adversarial, ambiguous, and OOD cases explicitly.** Label them as such | Dataset Design |  |  | ✓ |  |  |  | 1 |
| **Include cases where retrieval returns nothing or returns adversarial chunks.** — Real corpora are messy | Agents & RAG |  |  | ✓ |  |  |  | 1 |
| **Include prompt injection and data exfiltration cases for any agent with tools.** — These are the real production failures | Agents & RAG |  |  | ✓ |  |  |  | 1 |
| **Instrument at the span level (LLM call, tool call, retrieval).** — Attribution is impossible without spans | Cost & Latency |  |  | ✓ |  |  |  | 1 |
| **Log every judge prompt, response, and score to a queryable store.** — Spreadsheets don't scale past 50 cases | Structure & Code |  |  | ✓ |  |  |  | 1 |
| **Maintain a private holdout that never leaves your infra.** — Public benchmarks leak into training data | Dataset Design |  |  | ✓ |  |  |  | 1 |
| **Make every eval runnable locally on a subset with one command.** — If devs can't run it, they won't fix it | Structure & Code |  |  | ✓ |  |  |  | 1 |
| **Measure retrieval with recall@k and MRR against labeled relevant docs.** — "The LLM answered well" isn't a retrieval metric | Agents & RAG |  |  | ✓ |  |  |  | 1 |
| **Name cases by capability, not by number.** `refuses_medical_diagnosis` > `case_042` | Structure & Code |  |  | ✓ |  |  |  | 1 |
| **Never use the same model family as judge and generator for release-gating evals.** — Self-preference bias inflates scores by 5–15% | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Pin model version, temperature, seed, and prompt hash for every run.** — Without pinning, you can't attribute deltas | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Prefer temperature=0 with seed pinning for regression suites; sample for capability evals.** (contested) — Deterministic runs catch regressions faster; sampling measures real user experience | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Randomize position and ordering in pairwise judge prompts.** — LLM judges have strong position bias | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Record provenance for every example.** Source, author, date, and reason for inclusion | Dataset Design |  |  | ✓ |  |  |  | 1 |
| **Reject LLM-as-judge as the sole release gate for safety-critical behavior.** Use human review or deterministic checks | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Report quality-per-dollar, not just quality.** — Pareto trade-offs are the actual decision | Cost & Latency |  |  | ✓ |  |  |  | 1 |
| **Require chain-of-thought from judges and log it.** — Judge reasoning is your debug trail when scores move | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Run N≥5 samples per case for stochastic configs and report mean + 95% CI.** — Single runs are noise | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Separate dataset content (data) from scoring logic (code) from rubrics (text).** — Mixing them blocks reuse and review | Structure & Code |  |  | ✓ |  |  |  | 1 |
| **Split into smoke, regression, and exploratory tiers.** Smoke runs on every PR (<2 min), regression nightly, exploratory on-demand | Dataset Design |  |  | ✓ |  |  |  | 1 |
| **Store raw outputs, not just scores, for every run.** — You will need them to diagnose regressions | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Stratify by user-relevant slices (intent, language, user tier, document type).** Report per-slice scores, not just aggregates | Dataset Design |  |  | ✓ |  |  |  | 1 |
| **Track p50/p95/p99 latency and per-example token cost on every run.** — Quality-only evals hide 3x cost regressions | Cost & Latency |  |  | ✓ |  |  |  | 1 |
| **Treat score deltas smaller than run-to-run variance as noise, not signal.** — Chasing noise wastes weeks | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Use exact-match only for constrained outputs (labels, JSON fields, tool names).** — It's meaningless for free-form text | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Use pairwise comparison for model-vs-model, absolute rubrics for regression tracking.** — Each answers a different question | Scoring Methods |  |  | ✓ |  |  |  | 1 |
| **Version datasets immutably.** Treat each dataset as a content-addressed artifact; never mutate in place | Dataset Design |  |  | ✓ |  |  |  | 1 |
| **Write each case to test one capability.** — Multi-purpose cases make failures ambiguous | Dataset Design |  |  | ✓ |  |  |  | 1 |
| Always compare against the immediate previous baseline and a long-term baseline | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Archive and deprecate tests via documented RFCs rather than deletion | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers, data scientists, and AI tooling who build, run, and gate releases with LLM evals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audit suites quarterly for drift, leakage, and representativeness | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Ban chain-of-thought in both model and judge during eval | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Blind the judge to the ground truth unless explicitly comparing candidates | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cache model outputs keyed by full prompt+params for local dev only | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cap dataset growth; add new files instead of mutating old ones | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cap tool loop iterations and time; fail on exceeding limits | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Co-locate rubrics with datasets and link to examples of good/bad outputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Compute both overall and per-criterion scores and log failures by criterion | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Compute confidence intervals via bootstrap and gate on effect sizes, not just p-values | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Compute inter-judge agreement by sampling multiple judges or seeds | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Constrain judge output to a strict JSON schema with label and reasons | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Deduplicate and decontaminate test content against training and docs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default to exact or structural checks when the task has objective outputs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define acceptance thresholds per metric and per tag before running | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define skip and xfail semantics and document them in code | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Disable caches during performance runs and mark results as uncached | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Disallow chain-of-thought in judge prompts and collect reasons as bullet points only | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Disallow network calls during scoring except approved mocks | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do annotate datasets with metadata for context, such as prompt intent or expected outcomes | Dataset Design |  |  |  |  |  | ✓ | 1 |
| Do cap evaluation runs at a fixed budget, such as limiting API calls per test | Performance |  |  |  |  |  | ✓ | 1 |
| Do document all test cases with brief descriptions | Maintainability |  | ✓ |  |  |  |  | 1 |
| Do document each rule or function with a brief description and rationale | Style |  |  |  |  |  | ✓ | 1 |
| Do follow a consistent naming convention, such as snake_case for functions and variables | Style |  |  |  |  |  | ✓ | 1 |
| Do implement LLM-as-judge as a default for scalable scoring, with human oversight for high-stakes cases (contested) | Scoring Methods |  |  |  |  |  | ✓ | 1 |
| Do implement automated regression tracking for evaluation results | Regression Tracking |  | ✓ |  |  |  |  | 1 |
| Do implement checks for harmful or biased content in outputs | Safety |  | ✓ |  |  |  |  | 1 |
| Do implement robust error handling, such as retries for API failures in LLM-as-judge | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do include diverse examples in your datasets, covering edge cases, biases, and real-world scenarios | Dataset Design |  |  |  |  |  | ✓ | 1 |
| Do include safety checks in every evaluation run, such as toxicity detection for prompts and outputs | Safety |  |  |  |  |  | ✓ | 1 |
| Do instrument your suite to track cost and latency metrics for each evaluation run | Performance |  |  |  |  |  | ✓ | 1 |
| Do integrate automated regression tracking with version control, logging changes in model performance over time | Regression Tracking |  |  |  |  |  | ✓ | 1 |
| Do keep test cases modular | Structure |  | ✓ |  |  |  |  | 1 |
| Do log all errors with detailed context, including timestamps and inputs | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do optimize prompts for response time and efficiency | Performance |  | ✓ |  |  |  |  | 1 |
| Do organize your evaluation suite into modular components, such as separate modules for datasets, scoring, and tracking | Structure |  |  |  |  |  | ✓ | 1 |
| Do prioritize rubric-based scoring over exact match for nuanced evaluations, like agent responses | Scoring Methods |  |  |  |  |  | ✓ | 1 |
| Do set clear thresholds for regression alerts, such as 5% drops in accuracy | Regression Tracking |  |  |  |  |  | ✓ | 1 |
| Do test for bias amplification in RAG pipelines by including diverse demographic examples | Safety |  |  |  |  |  | ✓ | 1 |
| Do use a configuration file (e.g., YAML or JSON) to define suite parameters | Structure |  |  |  |  |  | ✓ | 1 |
| Do use descriptive names for prompts and tests | Readability |  | ✓ |  |  |  |  | 1 |
| Do use diverse scoring methods to evaluate different aspects of model performance | Scoring Methods |  | ✓ |  |  |  |  | 1 |
| Do validate test outputs against expected results rigorously | Correctness |  | ✓ |  |  |  |  | 1 |
| Document label quality, inter-annotator agreement, and sampling method | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't hardcode dataset paths or scoring thresholds; use variables instead | Structure |  |  |  |  |  | ✓ | 1 |
| Don't manually review regressions without tooling; automate reports instead | Regression Tracking |  |  |  |  |  | ✓ | 1 |
| Don't overlook latency in scoring methods; choose lightweight options like exact match for fast feedback | Performance |  |  |  |  |  | ✓ | 1 |
| Don't propagate errors silently; always raise exceptions or alerts | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't rely solely on synthetic data for critical evaluations (contested) | Dataset Design |  |  |  |  |  | ✓ | 1 |
| Don't skip safety evaluations for non-production tests; treat them as mandatory | Safety |  |  |  |  |  | ✓ | 1 |
| Don't use a single scoring method across all tests; tailor it to the application (e.g., exact match for factual prompts) | Scoring Methods |  |  |  |  |  | ✓ | 1 |
| Don't use overly complex code structures; keep functions short and focused | Style |  |  |  |  |  | ✓ | 1 |
| Don’t allow unfiltered outputs to be evaluated | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t create tightly-coupled tests | Structure |  | ✓ |  |  |  |  | 1 |
| Don’t ignore edge cases in prompts | Correctness |  | ✓ |  |  |  |  | 1 |
| Don’t ignore historical data trends | Regression Tracking |  | ✓ |  |  |  |  | 1 |
| Don’t neglect version control on evaluation code | Maintainability |  | ✓ |  |  |  |  | 1 |
| Don’t rely solely on exact match scores | Scoring Methods |  | ✓ |  |  |  |  | 1 |
| Don’t sacrifice completeness for speed | Performance |  | ✓ |  |  |  |  | 1 |
| Don’t use jargon without definition | Readability |  | ✓ |  |  |  |  | 1 |
| Enforce budget caps per run and fail gracefully when exceeded | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Enforce citation presence and coverage; penalize uncited claims | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Evaluate plan quality, tool selection accuracy, and argument validity | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Evaluate retriever recall@k and MRR on labeled queries | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Exclude sensitive attributes from prompts unless testing fairness specifically | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fail fast on harness errors and report separately from model failures | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fail the build on any safety regression regardless of aggregate score | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For RAG, verify citations ground claims and links resolve | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For long-form tasks, use recall-oriented and precision-oriented sub-scores | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For tools, block exfiltrative actions and validate tool arguments against policies | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Highlight cost/latency regressions alongside quality changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If production samples, run k≥3 generations per case and score by majority or best-of defined in advance | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a CONTRIBUTING guide for adding/editing tests and labels | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include domain-shift queries and OOD detection tests | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include negative, edge, and adversarial cases for each capability | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include prompt-injection and jailbreak tests across all evals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include retries and tool invocation overheads in latency | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep a private holdout set not used for model iteration | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep tests hermetic by default; mock or record–replay external tools | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Limit judge/context visibility to least privilege required | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Limit per-batch prompt examples to avoid context contamination | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Log and review safety failures with reproducible minimal cases | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Measure p50/p95/p99 latency and average tokens in/out per test and per tag | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Mock tools with record–replay for correctness tests and use live tools only in perf/safety sandboxes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Normalize strings (case, whitespace, punctuation, Unicode) before matching | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Periodically rotate adversarial bias tests and re-validate labels with domain experts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin model versions, temperatures, seeds, and decoding params in config | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer pairwise comparisons for subtle quality differences | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer pairwise judge comparisons over scalar scores for semantic quality | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer small human-labeled anchor sets plus larger synthetic/adversarial sets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Produce per-run HTML/JSON reports with metrics, CIs, deltas, and top failures | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prohibit uploading proprietary test data to third-party judges without DPA | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a minimal README per dataset describing sourcing, labeling, and known limits | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Randomize candidate order and equilibrate prompts across arms | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Re-run only the failed cases to diagnose; never overwrite original artifacts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Record API pricing version and compute cost per test and per suite | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Record all inputs, outputs, tokens, latency, and environment per case | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Redact secrets from prompts, outputs, and logs automatically | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require review for any change to datasets, rubrics, or gates | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Revalidate judges after model or vendor changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Run lightweight smoke tests on every commit and full suites on schedule or before release | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scan outputs for PII and sensitive content; fail on threshold breaches | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: This rules file defines how to design, implement, and operate evaluation suites for LLM applications (prompts, agents, RAG pipelines), including datasets, scoring, regression tracking, safety, and cost/latency instrumentation | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Score answer correctness conditional on evidence presence and absence | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Score code by executing in a sandbox with time/memory limits | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Score end states and key intermediate invariants (e.g., valid SQL, non-destructive ops) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Separate cold-start from warm-path timing and report both | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Separate datasets, scoring logic, and execution harness into distinct modules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set temperature=0 for eval unless simulating production sampling | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Snapshot retrieval corpora/reranker models used during eval | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Store run artifacts (predictions, judgments, traces) in immutable storage | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Store test cases as human-readable JSONL/YAML with one case per record | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Stratify by demographic or sensitive attributes where applicable and report disaggregated metrics | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Stratify datasets by scenario and difficulty; report metrics per stratum | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Surface the smallest passing change that regresses safety as a blocker | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Tag each test with capability, domain, difficulty, and safety flags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Test for hallucination and overclaiming using adversarial and null-context cases | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Timebox model and tool calls and record timeouts distinctly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Track run metadata: git SHA, dataset/prompt/model versions, config hash, and runner | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Treat any unparsable or schema-invalid output as a test failure | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Treat formatting/units as part of correctness only when requirements demand it | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use LLM-as-judge only after validating against a human-labeled gold set | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use compact, declarative test specs with minimal embedded logic | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use majority-vote over n samples to score stochastic production | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use regex and heuristic validation for domain constraints (e.g., SQL syntax, date ranges) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use span-level F1/EM for extractive QA and set clear tie-breaking rules | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use stable identifiers for tests and do not recycle IDs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use temperature=0 for all evals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate JSON/XML outputs against schemas and reject malformed structures | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Validate chunking and windowing configs; treat them as versioned artifacts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Version datasets, prompts, and configurations explicitly | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Visualize per-tag and per-criterion deltas with trend lines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write rubrics as checklists with binary or scaled criteria and weights | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

