# Synthesis of LLM Evaluation Suite Best Practices

## 1. Consensus Rules

### Dataset Design

- **Version datasets immutably and treat them as first-class artifacts under source control.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Enables reproducible comparisons and prevents silent drift.
- **Include adversarial, edge-case, and out-of-distribution examples, not just happy paths.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — Robustness is measured at the edges, and happy-path-only suites give false confidence.
- **Maintain a private held-out set that is never used for prompt tuning or model iteration.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Public benchmarks leak into training data, and overfitting to the eval destroys signal.
- **Stratify datasets by capability, scenario, difficulty, or user slice, and report per-slice scores.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Aggregate wins routinely hide slice regressions that users actually notice.
- **Attach metadata to each test case: author, date, intent/capability, tags, and provenance.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — Enables triage, slicing, pruning, and ownership.
- **Use a structured, human-readable format (YAML/JSON/JSONL) for test cases.** (substantively similar across GPT-5, Claude Haiku, Gemini, Grok) — Structured, diffable data enables tooling, review, and non-engineer contribution.

### Scoring Methods

- **Use exact/structural match only for genuinely constrained outputs (labels, JSON fields, tool names, SQL results).** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Exact match is theater for free-form text.
- **Use a mix of scoring methods; don't rely on a single metric.** (substantively similar across all five models) — Each metric type has blind spots; combinations surface different failure modes.
- **Decompose rubrics into concrete, preferably binary, criteria with examples.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Single Likert scores are weak signals; binary checklists are auditable and debuggable.
- **Calibrate LLM-as-judge against a human-labeled gold set before trusting it; report agreement (e.g., Cohen's κ) and recalibrate when the judge model changes.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Uncalibrated judges are vibes; judge drift is silent.
- **Pin and version-control judge prompts, rubrics, and judge model versions.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Unpinned judges invalidate historical comparisons.
- **Log judge reasoning alongside scores, not just the final number.** (substantively similar across Claude Opus, Claude Haiku, Gemini) — Reasoning is the debug trail when scores move.
- **Randomize candidate/position order in pairwise or multi-candidate judging.** (substantively similar across GPT-5, Claude Opus) — LLM judges exhibit strong position bias.

### Regression Tracking

- **Establish and pin a baseline before making changes; track results in a queryable store over time.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — You cannot know if a change is an improvement without a reference point.
- **Pin model version, temperature, seed, system prompt, and all other parameters that affect output.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Unpinned knobs make deltas unattributable.
- **Run multiple samples per case for stochastic configs and report mean + variance/CI; treat deltas smaller than run-to-run variance as noise.** (substantively similar across GPT-5, Claude Opus, Claude Haiku) — Single runs are noise; chasing it wastes weeks.
- **Store raw outputs (not just scores) from every run.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — You will need them to diagnose a regression nobody anticipated.
- **Set explicit acceptance thresholds and gate merges/releases on them; safety regressions are hard blockers.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Pre-registered thresholds prevent moving goalposts and silent shipping of regressions.

### Safety

- **Maintain a dedicated, mandatory safety suite with prompt injection, jailbreak, PII exfiltration, and harmful-content tests.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — Safety must be tested explicitly and adversarially; it is not emergent from general quality.
- **Treat any safety regression as a hard release blocker regardless of aggregate score.** (substantively similar across GPT-5, Claude Opus, Gemini) — Safety is a constraint, not a metric to average away.

### Performance & Cost

- **Track p50/p95/p99 latency and per-example token cost on every run.** (near-identical across GPT-5 and Claude Opus; substantively similar across Claude Haiku, Gemini, Grok) — Cost and latency are first-class quality metrics; a 2% quality gain at 3x cost is usually a loss.
- **Set explicit cost and latency budgets and fail the run when exceeded.** (substantively similar across GPT-5, Claude Haiku, Gemini, Grok) — Budgets prevent silent cost explosions and runaway CI spend.
- **Instrument at the span level (LLM call, tool call, retrieval) for attribution.** (substantively similar across GPT-5, Claude Opus, Claude Haiku) — Without spans, regression attribution is impossible.
- **Tier the suite: fast smoke tests on every PR, full regression nightly/pre-release, exploratory on demand.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini) — Conflating tiers guarantees either slow CI or skipped evals.

### Structure, Readability & Maintainability

- **Separate datasets, scoring logic, rubrics, and harness code into distinct modules.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok) — Separation of concerns enables independent evolution and review.
- **Name test cases descriptively by capability, not by number.** (near-identical between Claude Opus and Claude Haiku; also GPT-5, Grok) — `refuses_medical_diagnosis` > `test_042`; names are documentation.
- **Make the suite runnable locally via a single CLI command on a subset.** (substantively similar across Claude Opus, Gemini) — If devs can't run it, they won't fix it.
- **Document what each test measures and why in a README; include how to add tests and update baselines.** (substantively similar across Claude Haiku, Gemini, Grok) — New contributors should be able to use the suite without asking questions.

### Error Handling & Reproducibility

- **Fail loudly on harness/API errors; never silently retry into a pass.** (substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok) — Flaky green is worse than red.
- **Implement timeouts and bounded retries with exponential backoff for transient failures.** (substantively similar across GPT-5, Claude Haiku, Grok) — Unbounded operations eventually hang and corrupt runs.
- **Validate model outputs (schema, parse) before scoring; malformed output is a failure, not a skip.** (substantively similar across GPT-5, Claude Haiku) — If you can't parse it, you can't use it.

---

## 2. Strong Minority Rules

- **Never use the same model family as judge and generator for release gating.** (Claude Opus only) — Self-preference bias inflates scores measurably (5–15%); this is well-documented and worth adopting.
- **Use inter-rater agreement (Cohen's κ, Krippendorff's α) to validate human-labeled ground truth; if κ < 0.7, fix the rubric before labeling more.** (Claude Haiku, echoed partially by GPT-5) — Without this, you're measuring annotator noise, not quality.
- **Evaluate retrieval and generation separately before end-to-end for RAG systems; measure recall@k and MRR against labeled relevant docs.** (GPT-5, Claude Opus) — Composite scores hide which stage regressed.
- **For agents, evaluate per-step decisions (tool choice, argument validity) in addition to final outcomes.** (GPT-5, Claude Opus) — End-to-end success masks broken intermediate reasoning.
- **Audit test results against real-world user feedback on a rolling basis.** (Claude Haiku) — If the suite says 90% quality but users complain, the suite is measuring the wrong thing; this is the only rule that closes the loop with reality.
- **Don't delete failing cases because they're "unfair"; mark them known-hard and track them.** (Claude Opus) — Deletion is how quality silently erodes; this is a concrete governance rule worth keeping.
- **Run a "no change" sanity baseline — same model, same params, twice — to quantify irreducible variance.** (Claude Haiku) — If variance is large, you have a reproducibility problem that outranks any score.
- **Minimum dataset sizes: ≥50 examples per category, ≥200 for production-critical paths.** (Claude Haiku) — Concrete number that practitioners can act on; small datasets are statistically unreliable.
- **Require review (RFC/PR) for any change to datasets, rubrics, or gates; archive deprecated tests rather than deleting.** (GPT-5) — Prevents silent metric gaming and preserves institutional memory.
- **Don't aggregate scores across incommensurable rubrics into a single headline number.** (Claude Opus) — Such numbers are uninterpretable and easy to game.

---

## 3. Divergences

### 3a. Temperature: deterministic vs. sampling

- **Deterministic (temperature=0) as default:** Gemini explicitly recommends temp=0 for primary CI regression tests; GPT-5 leans this way but flags it as contested; Claude Haiku favors determinism where possible.
- **Sample multiple runs:** Claude Opus argues for N≥5 samples with mean + CI as the primary discipline; GPT-5 presents both sides.
- **Hybrid:** Gemini and Claude Opus converge on "temp=0 for regression gating, sampling for capability/variance eval."

**Synthesis:** Use **temperature=0 with pinned seed for regression gates** (for fast, low-noise signal), but run a **separate sampled-variance suite (N≥3–5)** on schedule to measure real-user-experience distributions. Report both. Never rely solely on a single-run stochastic score.

### 3b. LLM-as-judge as a primary/release-gating metric

- **Acceptable with calibration:** Gemini, Claude Haiku, Grok, GPT-5 — validate against gold, pin models/prompts, use for scale.
- **Reject for safety-critical gating:** Claude Opus — judges fail silently on exactly the cases that matter most; require human or deterministic checks for release gating on safety.

**Synthesis:** LLM-as-judge is appropriate for **capability regression tracking after calibration**, but **safety-critical release gates should use deterministic checks or human review** — not judges alone. Always report judge-human agreement.

### 3c. Chain-of-thought from judges: require vs. ban

- **Require CoT/reasoning from judges:** Claude Opus, Claude Haiku, Gemini — reasoning is the debug trail; log it verbatim.
- **Ban CoT in judges:** GPT-5 — CoT can leak, bias, and harm reproducibility; collect brief bullet rationales only.

**Synthesis:** The three-to-one split favors requiring structured reasoning. **Require judges to emit structured JSON with a score plus concise rationale (bulleted, not free-flowing CoT)**, and log it. This captures the debug-trail benefit while limiting leakage and unbounded reasoning.

### 3d. Pairwise vs. absolute scoring

- **Pairwise is more discriminative:** GPT-5, Claude Opus — prefer pairwise for subtle quality differences and model-vs-model comparisons.
- **Absolute is needed for tracking:** Claude Opus explicitly — pairwise alone doesn't give an absolute quality number.

**Synthesis:** Use **pairwise for model-vs-model decisions (A/B, bake-offs)** and **absolute rubric scores for longitudinal regression tracking**. They answer different questions.

### 3e. Synthetic data

- **Useful for augmentation, cap the fraction:** GPT-5, Claude Opus, Gemini, Grok — synthetic data expands coverage but encodes model biases; label it and cap it.
- **Acceptable as a supplement only:** Grok explicitly notes the trade-off.

**Synthesis:** Converged position — **use synthetic data to augment diversity and adversarial coverage, never to replace human-curated golden examples; label synthetic cases and cap their fraction of any evaluation set.**

### 3f. Test-suite versioning vs. application versioning

- **Version separately:** Claude Haiku — eval expectations evolve differently than code.
- **Version together:** Claude Haiku also recommends co-locating in source control; GPT-5 says version datasets explicitly.

**Synthesis:** **Co-locate in source control, but tag datasets and rubrics with independent semantic versions.** This gives reproducibility without coupling eval evolution to product release cadence.

---

## 4. Notable Omissions

- **No mention of safety-specific tests (prompt injection, jailbreaks, PII)** — missing from **GPT-4o-mini**. It mentions "harmful or biased content" abstractly but omits the concrete adversarial categories every other model calls out.
- **No mention of cost/latency instrumentation specifics (p50/p95/p99, token cost per example)** — missing from **GPT-4o-mini**. It says "optimize for response time" but lacks any concrete performance-tracking rule.
- **No mention of LLM-as-judge calibration against human labels** — missing from **GPT-4o-mini** and **Grok**. Both mention LLM-as-judge but neither requires validation against gold data; this is arguably the single most important rule about judges, and its absence is a signal.
- **No mention of private held-out sets / contamination control** — missing from **GPT-4o-mini** and **Grok**. Both discuss "diverse datasets" but omit holdouts, which is how you actually detect overfitting to the eval.
- **No mention of storing raw outputs for forensic analysis** — missing from **GPT-4o-mini** and **Grok**. Both discuss tracking results but not preserving the inputs/outputs you need to diagnose regressions later.
- **No mention of stratified/per-slice reporting** — missing from **GPT-4o-mini** and **Grok**. Every other model emphasizes that aggregate scores hide slice regressions.
- **No mention of multiple samples / variance / confidence intervals** — missing from **GPT-4o-mini** and **Gemini** (Gemini addresses it indirectly via temp=0 choice). Claude Opus and Claude Haiku are most explicit.
- **No mention of RAG or agent-specific evaluation patterns** — missing from **GPT-4o-mini**, **Claude Haiku** (briefly), and **Grok**. GPT-5, Claude Opus, and Gemini address RAG/agents explicitly.

The pattern: **GPT-4o-mini's response is conspicuously thin across almost every rigorous concern.** It reads like generic software testing advice lightly adapted to LLMs. Treat its omissions as a signal that it underweights the statistical and adversarial character of this domain.

---

## 5. Final Rules File

```markdown
# LLM Evaluation Suite Rules

**Scope:** Evaluation suites for LLM-backed applications — prompts, RAG pipelines, agents.
**Audience:** Engineers, ML practitioners, and AI coding assistants who design, build, and maintain eval suites.

An LLM eval suite is a statistical measurement instrument against fuzzy specifications, not a deterministic unit test. These rules treat that reality head-on.

---

## Dataset Design

- **Version datasets immutably as content-addressed artifacts; never mutate in place.** Enables reproducible historical comparisons.
- **Store test cases in structured, human-readable formats (YAML/JSON/JSONL), one case per record.** Diffable, greppable, reviewable by non-engineers.
- **Attach metadata to every case: id, author, date, intent/capability, tags, provenance, source.** Enables triage, slicing, and auditing stale cases.
- **Name cases by capability, not by number.** `refuses_medical_diagnosis` > `case_042`. Names are documentation.
- **Write each case to test one capability.** Multi-purpose cases make failures ambiguous.
- **Include adversarial, ambiguous, edge, and out-of-distribution cases explicitly, and label them as such.** Happy-path-only suites give false confidence.
- **Maintain a private held-out set that never leaves your infra and is never used for prompt tuning.** Public benchmarks leak into training data; holdouts detect overfitting to the suite.
- **Stratify cases by capability, difficulty, and user-relevant slices (intent, language, tier, document type); report per-slice scores.** Aggregate wins routinely hide slice regressions.
- **Minimum sizes: ≥50 examples per category, ≥200 for production-critical paths.** Smaller sets produce noise, not signal.
- **Cap synthetic data at a known, labeled fraction; never let it silently dominate.** Synthetic data encodes model biases into the eval and creates feedback loops.
- **Document dataset provenance, sampling method, label quality, and inter-annotator agreement in a per-dataset README.** Provenance is trust.
- **Measure and publish inter-rater agreement (Cohen's κ or Krippendorff's α) for human-labeled data; if κ < 0.7, fix the rubric before labeling more.** Ungrounded labels measure annotator noise, not quality.
- **Append-only: add new cases in new files rather than mutating old ones.** Preserves history.

## Scoring Methods

- **Use a mix of scoring methods; never rely on a single metric.** Each method has blind spots.
- **Use exact/structural match only for genuinely constrained outputs (labels, JSON fields, tool names, SQL result sets).** For free-form text, exact match is theater.
- **Normalize strings (case, whitespace, Unicode) before exact match; validate JSON/XML against schemas.** Removes irrelevant variance.
- **Score code by execution in a sandbox with time/memory limits.** Execution reveals functional correctness.
- **Decompose rubrics into concrete, preferably binary criteria with concrete examples per level.** Five yes/no checks beat one 1–5 Likert score.
- **Don't rely on a single Likert score from an LLM judge as a primary metric.** Judges cluster on the middle; signal is weak.
- **Don't use BLEU/ROUGE as a primary metric for open-ended generation.** They correlate poorly with user satisfaction and are easily gamed.
- **Don't aggregate incommensurable rubric scores into a single headline number.** Uninterpretable and easy to game.

## LLM-as-Judge

- **Validate every judge against a human-labeled gold set before using it; report agreement (κ, within-1, rank correlation) and re-validate when the judge model changes.** Uncalibrated judges are vibes; judge drift is silent.
- **Pin and version-control the judge model, judge prompt, and rubric.** Unpinned judges invalidate historical comparisons.
- **Never use the same model family as judge and generator for release gating.** Self-preference bias inflates scores 5–15%.
- **Randomize candidate/position order in pairwise judging.** LLM judges have strong position bias.
- **Require structured JSON output (score + concise bulleted rationale) from judges and log the reasoning.** The rationale is your debug trail; bulleted output limits unbounded CoT contamination.
- **Use pairwise comparison for model-vs-model decisions; use absolute rubrics for longitudinal regression tracking.** Each answers a different question.
- **Do not use LLM-as-judge as the sole release gate for safety-critical behavior; require deterministic checks or human review.** Judges fail silently on the cases that matter most.

## Regression Tracking

- **Establish and pin a baseline before making changes.** You cannot call something an improvement without a reference.
- **Pin model version, temperature, seed, system prompt, decoding params, and prompt hash for every run.** Without pinning, deltas are unattributable.
- **Use temperature=0 with pinned seed for regression gates; run a separate N≥3–5 sampled suite to measure real-world variance.** Deterministic runs catch regressions fast; sampling measures reality.
- **Report mean + 95% CI for stochastic configs; treat deltas smaller than run-to-run variance as noise.** Chasing noise wastes weeks.
- **Run a "no change" sanity baseline (same model, same params, twice) to quantify irreducible variance.** If variance is large, reproducibility outranks any score.
- **Store raw outputs (predictions, traces, judge responses), not just scores, for every run, in immutable storage.** You will need them to diagnose unexpected regressions.
- **Log run metadata: git SHA, dataset/prompt/model versions, config hash, runner, environment.** Makes results auditable.
- **Define acceptance thresholds per metric and per slice before running.** Pre-registration prevents moving goalposts.
- **Alert on per-slice regressions, not only aggregate.** Aggregates hide the failures users notice.
- **Compute confidence intervals (bootstrap) and gate on effect sizes, not just p-values.** Practical significance matters more than statistical.
- **Block merges on safety regressions; require review for capability regressions.** Not all regressions are equal.

## Safety

- **Maintain a dedicated, mandatory safety suite: prompt injection, jailbreaks, PII exfiltration, harmful content, bias.** Safety must be tested explicitly and adversarially; it is not emergent.
- **Treat any safety regression as a hard release blocker regardless of aggregate score.** Safety is a constraint, not a metric to average.
- **For agents with tools, include data exfiltration and destructive-action tests; validate tool arguments against policies.** Tool misuse amplifies harm.
- **For RAG, verify citations actually ground claims and that links resolve; penalize uncited claims.** Grounding prevents fabricated sources.
- **Redact secrets from prompts, outputs, and logs automatically.** Secrets often leak into traces.

## RAG-Specific

- **Evaluate retrieval and generation separately before evaluating end-to-end.** Composite scores hide which stage regressed.
- **Measure retrieval with recall@k and MRR against labeled relevant documents.** "The LLM answered well" is not a retrieval metric.
- **Include cases where retrieval returns nothing or returns adversarial/misleading chunks.** Real corpora are messy.
- **Snapshot retrieval corpora, chunking configs, and reranker versions; treat them as versioned artifacts.** Preprocessing changes alter recall silently.

## Agents & Tool Use

- **Evaluate per-step decisions (tool choice, argument validity, plan quality) in addition to final outcome.** End-to-end success masks broken intermediate reasoning.
- **Use record/replay for tool mocks in correctness tests; reserve live tools for perf/safety sandboxes.** Controlled environments prevent side effects.
- **Cap tool-loop iterations and wall-clock time; fail on exceeding limits.** Infinite loops and stalls are real production failures.

## Cost & Latency

- **Track p50/p95/p99 latency and per-example token cost on every run.** Quality-only evals hide 3x cost regressions.
- **Instrument at the span level (LLM call, tool call, retrieval).** Attribution is impossible without spans.
- **Separate cold-start from warm-path latency and report both.** Cold starts dominate user-perceived latency.
- **Include retry and tool-invocation overhead in latency.** Users experience the whole pipeline.
- **Set explicit cost and latency budgets per run and fail when exceeded.** Budgets prevent silent cost explosions.
- **Disable output caching during performance runs; mark cached results explicitly.** Caches hide true latency.
- **Report quality-per-dollar, not just quality.** Pareto trade-offs are the actual decision.

## Structure & Code

- **Separate dataset content, scoring logic, rubrics, and harness code into distinct modules.** Independent evolution and review.
- **Make the suite runnable locally on a subset via a single CLI command.** If devs can't run it, they won't fix it.
- **Tier the suite: smoke (<2 min, every PR), regression (nightly), exploratory/full (on-demand, pre-release).** Conflating tiers guarantees slow CI or skipped evals.
- **Use a config file (YAML/JSON) for suite parameters; don't hardcode paths or thresholds.** Portability and central change control.
- **Log all inputs, outputs, token counts, latency, judge prompts, and judge reasoning to a queryable store.** Spreadsheets don't scale past 50 cases.

## Error Handling & Robustness

- **Fail loudly on harness/API errors; never silently retry into a pass.** Flaky green is worse than red.
- **Implement timeouts for every LLM call, tool call, and scoring operation.** Unbounded operations eventually corrupt runs.
- **Use bounded retries with exponential backoff for transient failures; give up and report after N tries.** Don't retry forever.
- **Validate and parse model outputs before scoring; malformed output is a failure, not a skip.** If you can't parse it, you can't use it.
- **Report harness errors separately from model failures.** Harness bugs shouldn't pollute model metrics.

## Governance & Lifecycle

- **Require code review / RFC for any change to datasets, rubrics, or acceptance gates.** Prevents silent metric gaming.
- **Archive and deprecate tests via documented process rather than deletion.** Preserves institutional memory; deletion is how quality silently erodes.
- **Don't delete failing cases because they're "unfair"; mark them known-hard and track them.** Same reasoning.
- **Don't tune prompts against the same eval set you report scores on.** That's overfitting; reserve a blind holdout.
- **Audit suites periodically (quarterly) for drift, leakage, and representativeness.** Periodic hygiene keeps evals relevant.
- **Audit eval results against real-world user feedback on a rolling basis.** If the suite says 90% but users complain, the suite is measuring the wrong thing. This is the only rule that closes the loop with reality.
- **Document decisions: why this judge, why this threshold, why this slice was excluded.** Future-you will thank you.
- **Include a README covering: how to run, how to interpret, how to add tests, how to update baselines.** New contributors should self-serve.

## Reporting

- **Produce per-run reports (HTML/JSON) with metrics, CIs, deltas vs. baseline, per-slice breakdowns, and top failure examples.** Clear reports drive action.
- **Include a headline summary: accuracy, p95 latency, cost/run, baseline delta.** Make the answer immediately obvious.
- **Surface cost and latency regressions with the same prominence as quality regressions.** Performance is part of quality.
```