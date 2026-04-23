# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Make test data human-readable in the primary source.** Don't obfuscate it | Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Assign every test case a stable unique ID.** Per-case regression tracking is impossible without stable IDs | Structure |  |  | ✓ |  |  |  | 1 |
| **Audit your evaluation dataset for train–test leakage quarterly.** Compare a sample of evaluation cases against production query logs | Robustness and Safety |  |  |  | ✓ |  |  | 1 |
| **Avoid magic strings and numbers.** Define thresholds, model names, and API parameters as named constants at the top of the evaluation module, not hardcoded in assertions | Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Calibrate every LLM-as-judge against human labels on a holdout before trusting it.** Uncalibrated judges produce decorative numbers | Scoring |  |  | ✓ |  |  |  | 1 |
| **Catch and log all API failures** (rate limits, timeouts, provider outages) separately from scoring failures | Error Handling and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **Default to deterministic scoring (exact match, regex, formal rules).** Deterministic scoring is reproducible, debuggable, and cheap; use it whenever the expected output is well-defined | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Design tasks to produce structured outputs so deterministic scoring is viable.** Free-form prose is a choice, not a requirement | Scoring |  |  | ✓ |  |  |  | 1 |
| **Do not use BLEU, ROUGE, or embedding similarity as primary quality metrics for generative tasks.** (contested) They correlate poorly with human judgment | Scoring |  |  | ✓ |  |  |  | 1 |
| **Document edge cases and known limitations explicitly.** For each test case that is particularly tricky or has uncertain ground truth, add a comment explaining why it's included and what outcome is expected | Robustness and Safety |  |  |  | ✓ |  |  | 1 |
| **Document why each test case exists.** Link to a GitHub issue, design doc, or bug report if one prompted it | Failure Diagnosis and Maintainability |  |  |  | ✓ |  |  | 1 |
| **Don't evaluate on adversarial or jailbreak-style prompts unless you explicitly intend to measure robustness to them.** Otherwise they pollute your baseline and distract from task performance | Robustness and Safety |  |  |  | ✓ |  |  | 1 |
| **Don't mix binary (pass/fail) and continuous (0–1 score) metrics without clear semantics.** Use continuous scores for exploration, binary for CI gates | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Exclude any case whose inputs appear in training or fine-tuning data.** Leakage inflates scores and masks regressions | Dataset Hygiene |  |  | ✓ |  |  |  | 1 |
| **Fail builds on per-capability regressions, not just overall score.** A stable average can mask a destroyed subcapability | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Fix the LLM-as-judge model, version, and prompt; treat changes as breaking.** A new judge invalidates historical comparisons | Scoring |  |  | ✓ |  |  |  | 1 |
| **For LLM-as-judge, log the full judge response** (scores, reasoning, temperature used) | Failure Diagnosis and Maintainability |  |  |  | ✓ |  |  | 1 |
| **For RAG, evaluate retrieval and generation as separate metrics.** A good answer from bad retrieval is luck; a bad answer from good retrieval is a prompt problem | Agent and RAG Specifics |  |  | ✓ |  |  |  | 1 |
| **For batch evaluations, use exponential backoff with jitter when retrying API failures.** Don't blast a provider with requests on failure | Error Handling and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **For multi-step tasks (e.g., agent steps), score intermediate outputs independently** in addition to final correctness | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Gate merges on cost and latency budgets, not only quality thresholds.** Unbudgeted cost regressions ship by default | Cost and Latency |  |  | ✓ |  |  |  | 1 |
| **If an evaluation case is flaky** (passes/fails randomly), investigate and either fix it or remove it | Failure Diagnosis and Maintainability |  |  |  | ✓ |  |  | 1 |
| **If an evaluation crashes mid-run, log which cases completed and which failed.** Resume or report partial results; don't discard the work | Error Handling and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **If using LLM-as-judge, version the model explicitly** (e.g., `gpt-4-turbo-2024-01`, not `gpt-4-turbo`) | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Include explicit negative cases (should-refuse, should-abstain, out-of-scope).** Suites without negatives measure only compliance, not discrimination | Dataset Hygiene |  |  | ✓ |  |  |  | 1 |
| **Include groundedness/faithfulness checks that verify claims against retrieved context.** Hallucination is the characteristic RAG failure mode | Agent and RAG Specifics |  |  | ✓ |  |  |  | 1 |
| **Keep a frozen regression set separate from an exploratory development set.** Iterating against a regression set silently overfits it | Structure |  |  | ✓ |  |  |  | 1 |
| **Keep dataset size proportional to the stability of the system.** Start with 50–200 examples | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Keep judge prompts free of the expected answer or gold label.** Leaking the answer into the judge context invalidates the score | Safety |  |  | ✓ |  |  |  | 1 |
| **Log the cost per evaluation run** (API calls, tokens, estimated USD) | Regression Tracking and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **Maintain a public metrics dashboard or report.** Transparency prevents metrics from being tuned away | Regression Tracking and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **Make every eval run reproducible from a single command with pinned dependencies.** Irreproducible evals are anecdotes | Execution |  |  | ✓ |  |  |  | 1 |
| **Never gate CI on latency alone.** Latency thresholds are soft; use them for monitoring and investigation, not release blockers | Regression Tracking and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **Never include secrets, PII, or production data in evaluation sets.** If you need realistic data, anonymize it or use synthetic data | Robustness and Safety |  |  |  | ✓ |  |  | 1 |
| **Never modify regression-set cases to make failing tests pass.** That converts a regression signal into a rubber stamp | Dataset Hygiene |  |  | ✓ |  |  |  | 1 |
| **Never retry failing eval cases to get them to pass.** Retries hide flakiness and inflate scores | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Organize evaluations into a dedicated module or package,** separate from application code | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Organize test cases by tag or category** and allow selective evaluation (`pytest -m smoke`, `pytest --tag edge_case`) | Failure Diagnosis and Maintainability |  |  |  | ✓ |  |  | 1 |
| **Parallelize case execution with a concurrency cap and rate-limit handling.** Sequential runs make suites slow enough that people skip them | Execution |  |  | ✓ |  |  |  | 1 |
| **Partition evaluation data into tiers: smoke (10–20 examples, <1min runtime), standard (100–300 examples, <10min), and deep (>500 examples).** Run smoke on every PR, standard on main, deep on releases | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Persist per-case raw outputs and scores for every run, not just aggregates.** Aggregates hide silent case-level swaps and prevent rescoring | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Prefer exact match, schema validation, or regex over model-based scoring whenever the task permits.** Deterministic scorers are cheaper, faster, and not subject to judge drift | Scoring |  |  | ✓ |  |  |  | 1 |
| **Provide a rubric or scoring specification for all evaluations.** For exact match: define what counts as a match (case-sensitive? trailing whitespace?) | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Record input tokens, output tokens, wall-clock latency, and tool-call count per case.** Quality improvements that triple cost are regressions | Cost and Latency |  |  | ✓ |  |  |  | 1 |
| **Record the subject model, prompt hash, retrieval index hash, and code SHA with every run.** Without provenance, score deltas are unattributable | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Redact or pseudonymize PII in sampled production cases before committing them.** Eval datasets are code-adjacent artifacts and leak accordingly | Safety |  |  | ✓ |  |  |  | 1 |
| **Report confidence intervals (bootstrap or Wilson) on aggregate metrics.** Point estimates on small N invite false regressions | Regression Tracking |  |  | ✓ |  |  |  | 1 |
| **Report p50, p95, and p99 latency, not averages.** Tail latency is what users feel | Cost and Latency |  |  | ✓ |  |  |  | 1 |
| **Rule:** Actively test for PII leakage using both synthetic and real PII patterns | Safety & Robustness |  |  |  |  | ✓ |  | 1 |
| **Rule:** Automate the entire evaluation run with a single command | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Rule:** Cache deterministic intermediate artifacts from the application pipeline | Performance & Cost |  |  |  |  | ✓ |  | 1 |
| **Rule:** Define a consistent directory structure for all evaluation suites | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Rule:** Define an explicit pass/fail threshold for key metrics before running the evaluation | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| **Rule:** Define data schemas using a structured, self-describing format | Dataset Design |  |  |  |  | ✓ |  | 1 |
| **Rule:** Do not check secrets or API keys into the evaluation suite repository | Performance & Cost |  |  |  |  | ✓ |  | 1 |
| **Rule:** Force LLM-as-judge outputs into a structured format like JSON with a constrained schema | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| **Rule:** Include a `meta` block for each test case with its author, creation date, and intent | Dataset Design |  |  |  |  | ✓ |  | 1 |
| **Rule:** Include a dedicated set of prompt injection attacks in every suite | Safety & Robustness |  |  |  |  | ✓ |  | 1 |
| **Rule:** Include negative examples and "known bad" inputs in your dataset | Dataset Design |  |  |  |  | ✓ |  | 1 |
| **Rule:** Instrument and log the token costs and latency for every test case | Performance & Cost |  |  |  |  | ✓ |  | 1 |
| **Rule:** Maintain a core, static regression set for tracking quality over time | Dataset Design |  |  |  |  | ✓ |  | 1 |
| **Rule:** Prefer deterministic scoring methods over probabilistic ones | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| **Rule:** Separate data files from evaluation logic | Dataset Design |  |  |  |  | ✓ |  | 1 |
| **Rule:** Store configuration in a dedicated, versioned file (e.g., YAML, TOML) | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Rule:** Test for over-reliance on specific phrasing in the system prompt | Safety & Robustness |  |  |  |  | ✓ |  | 1 |
| **Rule:** Track multiple, distinct metrics for each evaluation | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| **Rule:** Use LLM-as-judge as a last resort, not a first choice | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| **Rule:** Version datasets using a system like Git LFS | Dataset Design |  |  |  |  | ✓ |  | 1 |
| **Rule:** Version the full evaluation context: application code, evaluation code, model ID, and dataset hash | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| **Run a dedicated safety/refusal eval suite separate from capability evals.** Mixing them obscures safety regressions behind capability gains | Safety |  |  | ✓ |  |  |  | 1 |
| **Run a fast smoke subset on every PR; run the full suite nightly.** (contested) Full-suite-per-PR costs dominate benefit past a certain suite size | Execution |  |  | ✓ |  |  |  | 1 |
| **Run generations at temperature=0 and fixed seed for reproducibility where the API supports it.** Non-determinism in the subject model makes regressions indistinguishable from noise | Scoring |  |  | ✓ |  |  |  | 1 |
| **Sample and manually review 5–10% of LLM-judge decisions** to detect grader collapse and calibration drift | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Score agent trajectories, not only final outputs.** Wrong tool calls that happen to produce right answers are latent bugs | Agent and RAG Specifics |  |  | ✓ |  |  |  | 1 |
| **Separate dataset, runner, scorer, and reporter into distinct modules.** Conflation prevents swapping any one component without rewriting the others | Structure |  |  | ✓ |  |  |  | 1 |
| **Set alert thresholds conservatively.** If a metric has drifted 3–5% historically, don't gate on changes <2% | Regression Tracking and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **Set explicit timeouts on API calls** (e.g., 30s for a single evaluation query) | Error Handling and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **Set the LLM-judge temperature deterministically** (e.g., `temperature=0` for scoring, not sampled inference) | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Store datasets as versioned JSONL or Parquet files, not as Python literals.** Data is an artifact with a lifecycle; code is not the right container | Structure |  |  | ✓ |  |  |  | 1 |
| **Stratify datasets by difficulty and source; do not oversample easy cases.** Uniform difficulty produces ceiling-effect scores | Dataset Hygiene |  |  | ✓ |  |  |  | 1 |
| **Tag every case with provenance (synthetic, curated, production-sampled, adversarial).** Provenance is required for debugging and for excluding leaked cases | Dataset Hygiene |  |  | ✓ |  |  |  | 1 |
| **Tag every test case with a capability label and difficulty tier.** Aggregate-only metrics hide which capability regressed | Structure |  |  | ✓ |  |  |  | 1 |
| **Track metrics as a time series per commit** (or experiment) | Regression Tracking and Instrumentation |  |  |  | ✓ |  |  | 1 |
| **Use LLM-as-judge only when the task requires semantic judgment** (e.g., summarization, reasoning quality, tone) | Scoring and Correctness |  |  |  | ✓ |  |  | 1 |
| **Use a structured metadata format (JSON, YAML, or CSV) for test cases,** with at minimum: `id`, `input`, `expected_output`, `tags` (e.g., "edge_case", "multilingual"), and `rationale` (why this case matters) | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **Use a test harness that supports parameterized evaluation** (e.g., pytest fixtures, custom test runners) | Failure Diagnosis and Maintainability |  |  |  | ✓ |  |  | 1 |
| **Use clear, human-readable names for test cases.** Bad: `test_1`, `eval_case_xyz` | Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Use consistent naming for inputs and outputs.** If one test uses `prompt`, `response`, and another uses `query`, `result`, refactor for consistency | Style and Clarity |  |  |  | ✓ |  |  | 1 |
| **Use immutable evaluation runners.** If code or prompts change, change them only for future runs; don't retroactively re-score old results | Robustness and Safety |  |  |  | ✓ |  |  | 1 |
| **Use pairwise comparison over absolute rating when using LLM judges.** (contested) Judges rank more reliably than they score | Scoring |  |  | ✓ |  |  |  | 1 |
| **Version datasets explicitly with a semver-style tag recorded in each run.** Score deltas across dataset versions are not comparable | Structure |  |  | ✓ |  |  |  | 1 |
| **Version your evaluation dataset.** Store it in version control (or a versioned artifact store) with a CHANGELOG documenting additions, removals, and labeling corrections | Structure and Organization |  |  |  | ✓ |  |  | 1 |
| **When an evaluation fails, the failure message should identify the specific test case and show the actual vs | Failure Diagnosis and Maintainability |  |  |  | ✓ |  |  | 1 |
| **Write comments for non-obvious scoring decisions.** Example: "This test expects the model to infer implicit context; scoring is lenient on formatting to isolate reasoning." | Style and Clarity |  |  |  | ✓ |  |  | 1 |
| *Rationale:* A single "quality" score can hide critical regressions in areas like latency, cost, or factuality | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| *Rationale:* A system's quality is defined by how it handles failure as much as success | Dataset Design |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Deterministic scores (e.g., regex match, keyword count) are cheaper, faster, and perfectly reproducible | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Drastically improves the reliability and parsability of judge outputs over free-text rationales | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Drastically reduces the cost and runtime of re-evaluating RAG systems where retrieval is expensive but deterministic | Performance & Cost |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Ensures that changes to evaluation data are deliberate, reviewable, and reproducible | Dataset Design |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Ensures the system is robust to minor, semantically-irrelevant changes in its instructions | Safety & Robustness |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Guarantees that an evaluation result can be perfectly reproduced in the future | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* LLM judges are expensive, non-deterministic, and prone to biases; reserve them for nuanced criteria that other methods cannot capture | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Lowers the friction to run evaluations, encouraging frequent use | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Makes suites predictable and easy to navigate for all team members | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Makes the economic and performance impact of a change visible and trackable | Performance & Cost |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Prevents "p-hacking" and goal-seeking after results are known | Scoring & Metrics |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Prevents parsing errors and makes the purpose of each data field explicit | Dataset Design |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Promotes modularity and allows data to be updated without changing execution code | Dataset Design |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Provides a stable baseline for measuring the impact of changes without dataset drift | Dataset Design |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Provides crucial context for why a test case exists, especially for obscure edge cases | Dataset Design |  |  |  |  | ✓ |  | 1 |
| *Rationale:* Separates configurable parameters (model name, temperature) from the core evaluation logic | Structure & Maintainability |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This is a fundamental security practice to prevent credential leakage | Performance & Cost |  |  |  |  | ✓ |  | 1 |
| *Rationale:* This is one of the most common and severe vulnerabilities in LLM applications | Safety & Robustness |  |  |  |  | ✓ |  | 1 |
| *Rationale:* What the model is not supposed to say is as important as what it is supposed to say | Safety & Robustness |  |  |  |  | ✓ |  | 1 |
| Audience: Engineers and AI practitioners implementing evals in a codebase with CI | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Blocklist known-dangerous output patterns and log violations as safety_fail | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cache model responses keyed by full input, model, and config | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Calibrate judges on a human-labeled set and publish agreement (e.g., Cohen’s κ) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Check evals in CI with pinned configs and fail the build on metric regressions above thresholds | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Compress and dedupe artifacts; keep only the latest N runs per branch | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Disallow silent fallbacks to different models or parameters | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do enforce content filters in scoring methods | Safety |  |  |  |  |  | ✓ | 1 |
| Do establish a modular architecture for your evaluation suite | Structure |  | ✓ |  |  |  |  | 1 |
| Do follow a linter like Black for code formatting in evaluation scripts | Style |  |  |  |  |  | ✓ | 1 |
| Do implement LLM-as-judge only with human oversight and calibration | Scoring Methods |  |  |  |  |  | ✓ | 1 |
| Do implement comprehensive error handling for each evaluation phase | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do implement robust error handling for API failures in LLM calls | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do include diverse examples in datasets, covering edge cases like ambiguous queries and adversarial inputs | Dataset Design |  |  |  |  |  | ✓ | 1 |
| Do include red-teaming tests for potential harms, like toxicity detection | Safety |  |  |  |  |  | ✓ | 1 |
| Do include safety checks to assess model outputs for biases | Safety |  | ✓ |  |  |  |  | 1 |
| Do instrument all evaluations for cost and latency metrics | Performance |  | ✓ |  |  |  |  | 1 |
| Do instrument all evaluations to track token usage and API latency | Cost/Latency Instrumentation |  |  |  |  |  | ✓ | 1 |
| Do integrate automated regression checks that compare current results to a baseline | Regression Tracking |  |  |  |  |  | ✓ | 1 |
| Do log all errors with detailed context | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do log all evaluation metadata, including timestamps and model versions | Regression Tracking |  |  |  |  |  | ✓ | 1 |
| Do optimize dataset sizes to under 1,000 samples per run | Performance |  |  |  |  |  | ✓ | 1 |
| Do organize evaluation components according to purpose (data collection, scoring, reporting) | Structure |  | ✓ |  |  |  |  | 1 |
| Do organize evaluation suites into modular components, such as separate files for datasets, scorers, and runners | Structure |  |  |  |  |  | ✓ | 1 |
| Do prioritize rubric-based scoring over exact match for non-factual evaluations | Scoring Methods |  |  |  |  |  | ✓ | 1 |
| Do set alerts for thresholds, such as latency over 5 seconds | Cost/Latency Instrumentation |  |  |  |  |  | ✓ | 1 |
| Do use a consistent naming convention for test files and functions, such as prefixing with "eval_" | Structure |  |  |  |  |  | ✓ | 1 |
| Do use caching for repeated evaluations | Performance |  |  |  |  |  | ✓ | 1 |
| Do use consistent naming conventions across files and functions | Style |  | ✓ |  |  |  |  | 1 |
| Do validate datasets for balance across categories (e.g., equal representation of topics) | Dataset Design |  |  |  |  |  | ✓ | 1 |
| Document dataset provenance and known limitations in README.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Don't deploy evaluations without safety checklists | Safety |  |  |  |  |  | ✓ | 1 |
| Don't hardcode error thresholds; use configurable values | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't ignore error rates in performance metrics | Performance |  |  |  |  |  | ✓ | 1 |
| Don't nest evaluation logic more than three levels deep | Structure |  |  |  |  |  | ✓ | 1 |
| Don't reuse production data without anonymization | Dataset Design |  |  |  |  |  | ✓ | 1 |
| Don't run evaluations without capping concurrent requests | Cost/Latency Instrumentation |  |  |  |  |  | ✓ | 1 |
| Don't skip baseline updates after major changes; always re-establish them | Regression Tracking |  |  |  |  |  | ✓ | 1 |
| Don't use a single scoring method for all tests; combine approaches like exact match and metrics-based | Scoring Methods |  |  |  |  |  | ✓ | 1 |
| Don't use magic numbers in scoring functions; define them as constants | Style |  |  |  |  |  | ✓ | 1 |
| Don’t allow undocumented or unmonitored changes to evaluation criteria | Safety |  | ✓ |  |  |  |  | 1 |
| Don’t create overly complex scoring functions | Style |  | ✓ |  |  |  |  | 1 |
| Don’t ignore failure cases in scoring methods | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don’t neglect regression tracking in updates to the LLM | Performance |  | ✓ |  |  |  |  | 1 |
| Ensure no train/test overlap by content hash | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Evaluate tool-choice accuracy separately from final-task success | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Fix top_k and retrieve-time parameters in runner.yaml | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For exact-match scorers, set model temperature=0 | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For fuzzy match, define a single threshold and justify it in README.md | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For safety, include prompt-injection and tool-abuse test cases with explicit tags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For small deltas, require statistical significance before passing gates | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Gate merges on predeclared metrics and slices in ci.yaml | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Goal: Deterministic, trustworthy metrics with actionable regression signals, including cost/latency | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Hash and store prompts and tool schemas referenced in the run | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Implement bounded retries with exponential backoff and a hard timeout per call | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include JSON Schema files for datasets and logs, and validate in CI | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a suite.yaml with name, version (semver), owners, and license | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include at least one no-context baseline and one oracle-context baseline | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Keep IDs stable and unique across dataset items | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Limit dataset file size to ≤10,000 items per JSONL file | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Log all non-2xx API responses and mark affected cases as infra_error, not fail | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Log all tool calls, inputs, outputs, and latency with a chain_id | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Log retrieval diagnostics per case: retrieved_ids, ground_truth_ids, hit_at_k, MRR, and context_token_count | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Match metric to task: exact-match for structured extraction, normalized fuzzy match for paraphrase, rubric or LLM-as-judge for open-ended | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Parallelize evaluation within declared resource limits; do not exceed QPS quotas | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Periodically refresh safety suites with contemporary threats and document changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin judge model, prompt, and prompt hash; store prompt in repo | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin model identifiers, temperature, top_p, max_tokens, seed, and API endpoint in runner.yaml | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin scorer version and config in scorer.yaml | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prohibit PII in datasets unless explicitly safety-tagged and access-controlled | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prohibit judges from seeing gold answers unless the design requires it and is documented | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide at least 20 positive and 20 negative controls per suite | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put each suite under evals/<suite_name>/ with dataset.jsonl, scorer.yaml, runner.yaml, README.md, and golden.json | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Record tokens_in, tokens_out, cost_usd, and latency_ms per case and aggregated | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Reject undecided judgments explicitly and count them separately | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Report per-case scores and aggregate metrics with 95% confidence intervals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Require n≥100 test items for gating unless strong justification is documented | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Save run artifacts: request/response logs, scores.jsonl, summary.json, and config hashes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Rules for building, running, and maintaining LLM Evaluation Suites for prompts, agents, and RAG pipelines | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Separate dataset, runner, scorer, and reporter code/configs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set a per-run budget cap and fail fast when exceeded | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Store document provenance and a content hash for every retrieved chunk | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Store fields: id, input, expected (allow list for multi-reference), and metadata.tags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Store golden.json of prior passing results and diff against it | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Tag items with split: train\|dev\|test and topic/domain tags | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Tag safety categories on items and report safety metrics separately | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use JSONL for datasets with one JSON object per line | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use at least two independent judges with a deterministic tie-breaker | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use deterministic normalization (lowercase, trim, collapse whitespace, canonicalize punctuation) before exact or fuzzy match | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use pairwise judging over absolute Likert scoring for quality | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use snake_case for suite names and stable, human-meaningful IDs for items | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Warm caches in CI for stable suites; record cache hit rate in summary | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Write README.md per suite with Scope, Scoring, Datasets, Known Limitations, and Change Log sections | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

