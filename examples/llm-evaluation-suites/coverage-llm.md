## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Instrument and record token usage, cost, and latency per evaluation case. | Cost & Latency | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Separate dataset, runner, scorer, and reporter into distinct modules. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Pin the LLM-as-judge model version and prompt; treat changes as breaking. | LLM-as-Judge | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Prefer deterministic scoring (exact match, regex, schema) over model-based scoring when possible. | Scoring | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Tag test cases with categories (capability, difficulty, topic, or provenance) for slicing. | Dataset Design | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Version datasets explicitly as artifacts with a recorded version/changelog. | Dataset Design | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Assign every test case a stable unique ID. | Dataset Design | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Calibrate LLM-as-judge against human labels and monitor agreement. | LLM-as-Judge | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Include negative/adversarial controls (refusal, abstain, out-of-scope) in datasets. | Dataset Design | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Match the scoring method to the task (exact match for structured, rubric/judge for open-ended). | Scoring | ✓ | ✓ | ✓ | ✓ |  |  | 4 |
| Prevent train/test or production/eval data leakage; audit for overlap. | Dataset Design | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Provide a README or rubric documenting scope, scoring, and known limitations per suite. | Style & Documentation | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Run model generations at temperature=0 (and fixed seed) for reproducibility. | Reproducibility | ✓ |  | ✓ | ✓ |  |  | 3 |
| Set an explicit per-run cost/budget cap or concurrency limit. | Performance | ✓ |  |  | ✓ |  | ✓ | 3 |
| Store full run artifacts (per-case raw outputs, scores, config hashes). | Regression & CI | ✓ |  | ✓ | ✓ |  |  | 3 |
| Track metrics over time as a regression series and fail builds on regressions. | Regression & CI | ✓ |  | ✓ | ✓ |  | ✓ | 3 |
| Use JSONL/structured formats for datasets rather than inline Python literals. | Dataset Design | ✓ |  | ✓ |  | ✓ |  | 3 |
| Avoid silent retries that mask flakiness or infra errors. | Error Handling | ✓ |  | ✓ | ✓ |  |  | 3 |
| Cache deterministic model/pipeline outputs to reduce cost and variance. | Performance | ✓ |  |  | ✓ | ✓ |  | 3 |
| Implement bounded retries/timeouts and log API failures separately from model failures. | Error Handling | ✓ |  |  | ✓ |  | ✓ | 3 |
| Include safety-specific test cases (prompt injection, PII, toxicity) tagged separately. | Safety | ✓ |  | ✓ |  | ✓ |  | 3 |
| Record full reproducibility metadata (model id, prompt hash, code SHA, dataset version). | Reproducibility | ✓ |  | ✓ |  | ✓ |  | 3 |
| Report confidence intervals or statistical significance on aggregate metrics. | Scoring | ✓ |  | ✓ |  |  |  | 2 |
| Constrain LLM-as-judge output to a structured schema (e.g., JSON). | LLM-as-Judge |  |  |  |  | ✓ |  | 1 |
| Do not commit secrets/API keys to the evaluation repository. | Safety |  |  |  |  | ✓ |  | 1 |
| Evaluate agent trajectories/tool choices separately from final answers. | Agents & Tool Use | ✓ |  | ✓ |  |  |  | 2 |
| Evaluate retrieval and generation separately in RAG pipelines. | RAG | ✓ |  | ✓ |  |  |  | 2 |
| Include no-context and oracle-context baselines for RAG. | RAG | ✓ |  |  |  |  |  | 1 |
| Keep judge prompts free of the gold/expected answer. | LLM-as-Judge | ✓ |  | ✓ |  |  |  | 2 |
| Partition datasets into smoke/standard/full tiers tied to CI trigger. | Regression & CI |  |  | ✓ | ✓ |  |  | 2 |
| Provide a single reproducible command to run the full evaluation. | Structure |  |  | ✓ |  | ✓ |  | 2 |
| Redact or anonymize PII in any production-sampled eval data. | Safety | ✓ |  | ✓ |  |  | ✓ | 3 |
| Report latency as percentiles (p50/p95/p99), not just averages. | Cost & Latency |  |  | ✓ | ✓ |  |  | 2 |
| Require explicit pass/fail thresholds declared before the run. | Regression & CI |  |  |  | ✓ | ✓ |  | 2 |
| Store configuration (model, temperature, paths) in a versioned config file, not code literals. | Structure | ✓ |  |  |  | ✓ |  | 2 |
| Use consistent, human-readable names for suites and test cases. | Style | ✓ |  |  | ✓ |  | ✓ | 3 |
| Use pairwise comparison over absolute rating for LLM-judge quality scoring. | LLM-as-Judge | ✓ |  | ✓ |  |  |  | 2 |
| Validate datasets against a schema (JSON Schema or equivalent) in CI. | Structure | ✓ |  |  | ✓ | ✓ |  | 3 |
| Avoid magic numbers/strings; use named constants in eval code. | Style |  |  |  | ✓ |  | ✓ | 2 |
| Avoid over-deep nesting in evaluation logic. | Style |  |  |  |  |  | ✓ | 1 |
| Emit clear failure messages showing per-case actual vs. expected output. | Error Handling |  |  |  | ✓ |  |  | 1 |
| Enforce a minimum test-set size (e.g., n≥100) before gating. | Regression & CI | ✓ |  |  |  |  |  | 1 |
| Include a `meta`/rationale field explaining why each test case exists. | Dataset Design |  |  |  | ✓ | ✓ |  | 2 |
| Include comprehensive error handling for all evaluation phases. | Error Handling |  | ✓ |  |  |  | ✓ | 2 |
| Investigate or remove flaky test cases; don't ignore intermittent failures. | Error Handling |  |  |  | ✓ |  |  | 1 |
| Keep a frozen regression set separate from an exploratory/development set. | Dataset Design |  |  | ✓ | ✓ | ✓ |  | 3 |
| Keep datasets small enough to be manually reviewable (size cap). | Dataset Design | ✓ |  |  | ✓ |  | ✓ | 3 |
| Limit concurrent API requests to respect rate limits. | Performance | ✓ |  | ✓ |  |  | ✓ | 3 |
| Make datasets human-readable in source (no obfuscation). | Style |  |  |  | ✓ |  |  | 1 |
| Periodically refresh safety suites with new threats. | Safety | ✓ |  |  |  |  |  | 1 |
| Prohibit silent fallbacks to different models or parameters. | Error Handling | ✓ |  |  |  |  |  | 1 |
| Report per-capability / per-slice metrics, not only overall score. | Regression & CI |  |  | ✓ | ✓ |  |  | 2 |
| Sample and manually review a fraction of LLM-judge decisions. | LLM-as-Judge |  |  |  | ✓ |  |  | 1 |
| Score intermediate outputs in multi-step (agent) tasks. | Agents & Tool Use |  |  | ✓ | ✓ |  |  | 2 |
| Tag safety categories and report safety metrics separately from capability metrics. | Safety | ✓ |  | ✓ |  |  |  | 2 |
| Use a consistent directory layout for every suite. | Structure | ✓ |  |  |  | ✓ | ✓ | 3 |
| Use a standard code formatter/linter (e.g., Black) on eval code. | Style |  |  |  |  |  | ✓ | 1 |
| Use at least two independent judges with a deterministic tie-breaker. | LLM-as-Judge | ✓ |  |  |  |  |  | 1 |
| Use configurable (non-hardcoded) thresholds and parameters. | Style |  |  |  |  |  | ✓ | 1 |
| Use parameterized test harnesses (pytest fixtures) rather than copy-pasted test code. | Structure |  |  |  | ✓ |  |  | 1 |
| Warn against BLEU/ROUGE/embedding similarity as primary quality metrics. | Scoring |  |  | ✓ |  |  |  | 1 |

## Notes on clustering decisions

- **"Separate dataset, runner, scorer, reporter"** clustered together with gpt-4o-mini's "organize components according to purpose (data collection, scoring, reporting)" and grok-3-mini's "modular components" and gemini's "separate data from logic" — all describe the same modularity principle even though wording and granularity differ.
- **"Instrument token usage, cost, and latency"** merged across models that separately mentioned cost OR latency OR tokens; I treated the general instrumentation intent as one cluster rather than splitting by which specific metric each model named. Haiku's p50/p95/p99 rule is kept as a distinct finer-grained rule.
- **"Tag test cases with categories"** collapses capability tags (opus), tags+rationale (haiku), provenance (opus/haiku), and topic/domain tags (gpt-5) — all are "add structured per-case metadata." A stricter reading would split these into capability-tagging vs. provenance-tagging; I clustered because they share the same mechanism and intent.
- **"Version datasets explicitly"** includes both gemini's Git LFS rule and others' semver/changelog rules — the underlying norm (datasets are versioned artifacts) is the same even though the concrete mechanism differs.
- **"Pin the LLM-as-judge model and prompt"** and **"Calibrate LLM-as-judge"** kept as separate rules; they frequently co-occur but address different concerns (reproducibility vs. validity).
- **"Prefer deterministic scoring"** and **"Match metric to task"** kept separate: the former is a preference ordering, the latter is a correspondence rule. Some models (gpt-4o-mini) only stated one or the other.
- **"Avoid silent retries"** (opus) vs. **"Implement bounded retries with timeouts"** (gpt-5, haiku, grok) — these are related but not identical; one forbids retry-to-pass on scoring, the other mandates transport-layer retry policy. Kept distinct.
- **"Redact PII"** and **"Include safety test cases (PII/injection/toxicity)"** kept separate: one is about eval-dataset hygiene, the other about what capability the suite measures. gpt-5 and opus each touch both.
- **grok-3-mini's "don't reuse production data without anonymization"** was folded into the PII-redaction cluster rather than into the leakage cluster; the rationale cited is privacy, matching the redaction intent.
- **"Consistent directory layout"** (gpt-5 evals/<suite>/…, gemini required-template, grok naming convention) clustered together even though gpt-5 specifies files and gemini specifies directory templates — both enforce structural predictability.
- **gpt-4o-mini** contributed very few specific rules; many of its entries ("do X", "don't ignore Y") are generic and were mapped to the nearest specific cluster only when the intent was unambiguous (e.g., "instrument for cost and latency", "comprehensive error handling"). This is why its ✓ count looks sparse — a regex matcher would likely match even fewer.
- **"Keep a frozen regression set separate from exploratory set"** — grok's "maintain baseline" was *not* clustered here; grok's rule is about regression baselines/thresholds, not dataset partitioning. Close call.
- **"Include negative examples"** (gemini, grok) clustered with opus's "explicit negative cases (should-refuse/abstain)" and gpt-5's "positive/negative controls" — all three describe complementary-label coverage, though opus is more specific about refusal semantics.