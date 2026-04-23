# Synthesis of LLM Evaluation Suite Best Practices

## 1. Consensus Rules

### Structure & Organization

- **Separate dataset, runner, scorer, and reporter into distinct modules.** Conflation prevents swapping any component without rewriting the others. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Use a predictable, conventional directory structure for evaluation suites, kept separate from production code.** Structural consistency enables tooling, review, and clear ownership. *(substantively similar across GPT-5, Claude Haiku, Gemini, Grok)*
- **Store evaluation datasets as versioned structured files (JSONL/Parquet/YAML), not as Python literals.** Data is a lifecycle artifact, not source code. *(near-identical wording across GPT-5 and Claude Opus; substantively similar in Gemini, Claude Haiku)*

### Dataset Design

- **Assign every test case a stable, unique ID plus structured metadata (tags, provenance, difficulty, rationale).** Per-case regression tracking, slicing, and auditing are impossible without these. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Version datasets explicitly (e.g., semver) and record dataset version in each run.** Score deltas across dataset versions are not comparable without version pinning. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Include explicit negative/adversarial cases (should-refuse, out-of-scope, edge cases).** Suites without negatives measure compliance, not discrimination. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Prevent train/eval leakage and never include PII, secrets, or unanonymized production data.** Leakage inflates scores; sensitive data in repos creates compliance and safety risk. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Maintain a frozen regression set distinct from an exploratory/development set, and never modify regression cases to make tests pass.** Iterating on the regression set silently overfits it. *(substantively similar across Claude Opus, Claude Haiku, Gemini)*

### Scoring & Metrics

- **Prefer deterministic scoring (exact match, regex, JSON schema, structural checks) whenever the task permits; design tasks to produce structured outputs.** Deterministic scorers are cheap, reproducible, and not subject to judge drift. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Match the scoring method to the task; never apply a single one-size-fits-all scorer.** Metric-task mismatch is the most common silent correctness failure. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Run the subject model at temperature=0 with a fixed seed where supported.** Non-determinism in the subject model makes regressions indistinguishable from noise. *(near-identical wording across GPT-5 and Claude Opus; also in Claude Haiku)*
- **Define explicit pass/fail thresholds (and any fuzzy-match cutoffs) before running, and document them.** Prevents post-hoc goal-seeking and makes thresholds auditable. *(substantively similar across GPT-5, Claude Haiku, Gemini)*

### LLM-as-Judge

- **Pin the judge model (with explicit version string), prompt, and prompt hash; treat changes as breaking.** A new judge invalidates historical comparisons. *(near-identical wording across Claude Opus, Claude Haiku, and GPT-5)*
- **Set judge temperature to 0 (or a fixed deterministic value).** Non-determinism in the judge is indistinguishable from quality drift. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Calibrate LLM judges against human labels and sample-review a fraction of judgments periodically.** Uncalibrated judges produce decorative numbers. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*
- **Force LLM-judge outputs into a constrained structured format (JSON schema).** Improves parsability and reduces silent failure modes. *(raised explicitly by Gemini and GPT-5; implied by Claude Opus/Haiku)*

### Regression Tracking

- **Persist per-case raw outputs, scores, and metadata for every run — not just aggregates.** Aggregates hide silent case-level swaps and prevent rescoring. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Record provenance for every run: subject model, prompt hash, dataset version, retrieval index hash, code SHA, config hash.** Without provenance, score deltas are unattributable. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Report confidence intervals (bootstrap, Wilson) rather than point estimates; require significance before gating.** Point estimates on small N invite false regressions. *(substantively similar across GPT-5 and Claude Opus)*
- **Track metrics sliced by capability/tag, not just overall score.** A stable average can mask a destroyed subcapability. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **Never retry failing eval cases to get them to pass.** Retries hide flakiness and inflate scores. *(substantively similar across Claude Opus and Claude Haiku)*

### Cost & Latency Instrumentation

- **Record input tokens, output tokens, wall-clock latency, and (where relevant) tool-call count per case and in aggregate.** Quality improvements that triple cost or latency are regressions. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku; also in Gemini, Grok)*
- **Report latency percentiles (p50/p95/p99), not just means.** Tail latency is what users experience. *(substantively similar across Claude Opus and Claude Haiku)*
- **Set and enforce per-run budget/cost caps.** Unmonitored costs spike silently. *(substantively similar across GPT-5, Claude Haiku, Grok)*
- **Cache deterministic intermediate artifacts (model responses, retrieval) keyed by full config.** Reduces variance and spend on re-runs. *(substantively similar across GPT-5, Claude Haiku, Gemini)*

### Reproducibility & Execution

- **Pin every generation parameter (model ID, temperature, top_p, max_tokens, seed, endpoint) in a versioned config file.** Full determinism requires all knobs pinned. *(substantively similar across GPT-5, Claude Opus, Gemini, Grok)*
- **Make every eval run reproducible from a single command with pinned dependencies.** Irreproducible evals are anecdotes. *(substantively similar across Claude Opus, Gemini, Grok)*

### Safety & Robustness

- **Include a dedicated safety suite (prompt injection, PII leakage, toxicity, jailbreaks) tagged and reported separately from capability evals.** Mixing obscures safety regressions behind capability gains. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Never check secrets or API keys into the evaluation repository; scan with secret-detection tooling.** Fundamental security hygiene. *(substantively similar across Claude Haiku and Gemini)*
- **Keep judge prompts free of the expected/gold answer unless the design explicitly requires it.** Leaking the answer into the judge context invalidates the score. *(substantively similar across GPT-5 and Claude Opus)*

### Error Handling

- **Implement bounded retries with exponential backoff and explicit timeouts on every API call; log non-2xx responses as `infra_error`, not `fail`.** Separates infra noise from model errors. *(substantively similar across GPT-5, Claude Haiku, Grok)*

### Style & Documentation

- **Document each suite with a README covering scope, scoring rules, datasets, limitations, and changelog.** Shared understanding and auditability. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Grok)*
- **Use clear, descriptive, consistent names for test cases and IDs; avoid magic numbers and hardcoded constants.** Readability is part of correctness. *(substantively similar across GPT-5, Claude Haiku, Grok)*

### Agent & RAG Specifics

- **For agents, score trajectories (tool choice, intermediate steps) separately from final outputs.** Wrong tool calls that produce right answers are latent bugs. *(substantively similar across GPT-5, Claude Opus, Claude Haiku)*
- **For RAG, evaluate retrieval (recall@k, MRR, hit@k) and generation as distinct metrics, and include no-context and oracle-context baselines.** Separates retrieval failures from generation failures. *(near-identical across GPT-5 and Claude Opus)*

---

## 2. Strong Minority Rules

- **Partition evaluation data into tiers (smoke/standard/deep) and run smoke on every PR, full suite nightly.** *(Claude Haiku; Claude Opus marks this contested.)* Kept because running the full suite on every PR is operationally unrealistic for mature suites and the tiered pattern is well-established in practice.
- **Use pairwise comparison over absolute rating when using LLM judges.** *(Claude Opus, GPT-5; marked contested.)* Kept because pairwise judging has substantially better evidence in the literature for quality-sensitive tasks.
- **Do not use BLEU/ROUGE/embedding similarity as primary quality metrics for generative tasks.** *(Claude Opus, marked contested.)* Kept because this reflects current best practice and warns against a common antipattern.
- **Provide a visible metrics dashboard/report so pass rates, cost, and latency are public across versions.** *(Claude Haiku.)* Kept because transparency is a strong deterrent to metric gaming.
- **Disallow silent fallbacks to different models, parameters, or regions; require explicit `fallback_allowed` config.** *(GPT-5.)* Kept because SDK-level invisible fallbacks are a known source of result invalidation.
- **Stratify datasets by difficulty and source; avoid ceiling effects from uniformly easy cases.** *(Claude Opus.)* Kept because many suites silently saturate without this.
- **Audit datasets for train/test leakage on a recurring schedule (e.g., quarterly).** *(Claude Haiku.)* Kept because leakage is a delayed-failure class that is otherwise never checked.
- **Log the full judge response (scores, reasoning, temperature used) for post-hoc inspection.** *(Claude Haiku.)* Kept because judge debugging is impossible without this.
- **When an eval fails, the failure message must include case ID and full actual vs. expected output.** *(Claude Haiku.)* Kept because triage cost compounds quickly without this.

---

## 3. Divergences

### LLM-as-Judge: When is it legitimate?
- **Cautious/last-resort camp:** Gemini and Claude Opus argue LLM-as-judge should be a last resort, used only when deterministic scoring cannot capture the criterion, and only after human calibration.
- **Pragmatic-with-guardrails camp:** GPT-5 and Claude Haiku accept LLM-as-judge more broadly but insist on pinning, calibration, and sampled review.
- **Skeptical-of-pairwise:** Claude Haiku and Gemini do not strongly endorse pairwise-over-absolute; Claude Opus and GPT-5 do.
- **Synthesis:** Default to deterministic scoring. Use LLM-as-judge deliberately for semantic tasks, always pinned, always calibrated against human labels (target κ ≥ 0.7), always with sampled human review, and prefer pairwise for quality ranking. Treat judge changes as breaking changes regardless of camp.

### Dataset Size
- **Small-and-focused:** Claude Haiku recommends 50–300 cases, arguing large suites become unreviewable and mask failures. Grok caps at 1,000 samples per run for performance.
- **Larger-and-stratified:** Claude Opus recommends 50–500 per capability (so totals are larger). GPT-5 sets a hard ceiling of 10,000 items per JSONL but requires n≥100 for gating.
- **Synthesis:** Per-capability target of 50–500 cases; minimum n≈100 for any gating metric to support statistical claims; avoid single-file datasets >10k items. Actual size should be driven by statistical power needs, not by arbitrary caps.

### CI Gating Frequency
- **Per-PR full suite:** Grok and GPT-5 imply full evals in CI.
- **Tiered (smoke on PR, full nightly):** Claude Opus (contested), Claude Haiku.
- **Synthesis:** Tiered. Run a fast smoke subset on every PR; run the full suite nightly or on release branches. Gate merges on smoke + cost/latency budgets; use full-suite results for release decisions.

### Temperature Policy
- **Always 0:** GPT-5 (for exact-match), Claude Opus, Claude Haiku.
- **Context-dependent:** Gemini, Grok acknowledge some tasks legitimately need temperature > 0.
- **Synthesis:** Default temperature=0 with fixed seed. Allow temperature>0 only with an explicit annotation (e.g., `# eval: stochastic-allowed`) and multi-sample aggregation.

### Safety Blocklists
- **Enforce:** GPT-5 (marked contested) recommends blocklisting dangerous output patterns.
- **Not mentioned or skeptical:** Others emphasize tagged safety suites rather than content blocklists.
- **Synthesis:** Use tagged safety suites as primary; blocklists are acceptable as a secondary fail-closed mechanism but should not be the main signal because of false-positive/negative rates.

### Grok's 1,000-sample Cap
- Grok alone proposes a hard performance cap on dataset size. This conflicts with statistical power needs described by others. **Recommendation:** reject as a fixed rule; treat as a guideline only where latency/cost require it, and use sampling instead.

---

## 4. Notable Omissions

- **Cost and latency instrumentation:** GPT-4o-mini mentioned it only vaguely; it is a near-universal rule elsewhere.
- **Pinning model versions / reproducibility configuration:** Absent from GPT-4o-mini and Grok in concrete form, despite being foundational everywhere else.
- **LLM-as-judge calibration and pinning:** Absent from GPT-4o-mini entirely; barely addressed by Grok.
- **RAG-specific retrieval metrics and agent trajectory scoring:** Absent from GPT-4o-mini, Gemini, Grok, and Claude Haiku in specific form — only GPT-5 and Claude Opus cover these in depth. Given these are the two dominant LLM application patterns, the omission is significant.
- **Per-case raw output persistence:** Absent from GPT-4o-mini, Gemini, Grok. Claude Opus and Claude Haiku are emphatic about this; its absence elsewhere would make rescoring and silent-swap detection impossible.
- **Negative / refusal / out-of-scope test cases:** GPT-4o-mini skips this entirely.
- **Confidence intervals / statistical significance for gating:** Only GPT-5 and Claude Opus raise this; its absence from the others means their suites would be prone to noise-driven false regressions.
- **Frozen regression set separate from development set:** Absent from GPT-5 (implicit via splits), GPT-4o-mini, Grok. Claude Opus, Claude Haiku, and Gemini raise it explicitly.
- **Dataset version recorded in each run:** GPT-4o-mini and Grok skip this despite its centrality to reproducibility.

GPT-4o-mini's response is notably thin across the board — it omits more than half the consensus rules and contributes no unique insight.

---

## 5. Shared Deterministic Checks

### Shared checks (raised by multiple models)

- **Check** — Verify each dataset record has a non-empty, unique `id` field.
  - **Signal** — Parsed dataset files (JSONL/Parquet).
  - **Tool candidate** — ad-hoc (JSON Schema validator can handle presence/type; uniqueness is ad-hoc).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Claude Opus additionally requires IDs match a stable pattern (UUID/slug) rather than array indices; others only enforce presence+uniqueness.

- **Check** — Verify each dataset record has required structured metadata fields (e.g., `capability`/`tags`, `difficulty`/`split`, `provenance`, `rationale`, `expected`).
  - **Signal** — Parsed dataset files validated against a JSON Schema.
  - **Tool candidate** — JSON Schema validator (e.g., `ajv`, `jsonschema`).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku.
  - **Variance** — Required field sets differ slightly (GPT-5: `id/input/expected/metadata.tags`; Opus: `capability/difficulty/provenance`; Haiku: `id/input/expected_output/tags/rationale`). Implementation should accept a repo-local schema file.

- **Check** — Verify dataset manifest contains a semver `version` field, and each run record references a known dataset version.
  - **Signal** — Dataset manifest file (`dataset.yaml` or equivalent) and run-output records.
  - **Tool candidate** — ad-hoc (regex `^\d+\.\d+\.\d+$` + presence check).
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Substantively agreed. GPT-5 extends the check to `suite.yaml` metadata (owners, license).

- **Check** — Verify all model-invocation call sites use `temperature=0` (or a literal constant) and a pinned `seed`, with an explicit escape hatch annotation for stochastic cases.
  - **Signal** — Parsed AST of runner/scorer code plus config files.
  - **Tool candidate** — ad-hoc (AST walker); partially expressible in custom `ruff`/`pylint` rules.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — Claude Opus allows `# eval: stochastic-allowed` annotation; Haiku sets an upper bound of 0.3 for scoring contexts; GPT-5 ties the check to scorer type.

- **Check** — Verify LLM-judge model identifiers are fully versioned (include date or version suffix), not unversioned aliases.
  - **Signal** — Judge configuration file and/or AST of judge instantiation.
  - **Tool candidate** — ad-hoc (regex-based scanner with a repo-local allowlist).
  - **Raised by** — Claude Opus, Claude Haiku.
  - **Variance** — Opus additionally requires the judge prompt be referenced by content hash and that changes trigger a required PR label; Haiku focuses on version-suffix presence only.

- **Check** — Verify per-case result records contain `input_tokens`, `output_tokens`, `latency_ms`, and (where applicable) `tool_calls` / `cost_usd`.
  - **Signal** — Run-output artifact schema / per-case results file.
  - **Tool candidate** — JSON Schema validator.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — GPT-5 also requires aggregate totals; Opus additionally requires summary-level p50/p95/p99 latency fields.

- **Check** — Verify every run artifact records provenance (subject model, prompt hash, code SHA, dataset version, retrieval index hash if applicable).
  - **Signal** — Run-output artifact schema.
  - **Tool candidate** — JSON Schema validator.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Substantively agreed; field names differ.

- **Check** — Scan repository for committed secrets, API keys, or PII patterns.
  - **Signal** — Raw source text of all files + git history.
  - **Tool candidate** — `gitleaks`, `truffleHog`, `detect-secrets`.
  - **Raised by** — Claude Haiku, Gemini, GPT-5.
  - **Variance** — GPT-5 scopes to dataset files with a safety-tag exception; Haiku and Gemini recommend repo-wide scanning.

- **Check** — Verify eval-module source contains no large inline dataset literals; datasets are loaded from files.
  - **Signal** — AST of eval modules.
  - **Tool candidate** — ad-hoc AST walker (threshold: flag list/dict literals with eval-case-shaped keys and >N entries).
  - **Raised by** — Claude Opus, Gemini.
  - **Variance** — Opus specifies threshold of ~5 entries and allows unit-test fixtures; Gemini flags any same-directory colocation of data and logic.

- **Check** — Verify API call sites specify explicit timeouts and bounded retries.
  - **Signal** — AST of runner code.
  - **Tool candidate** — ad-hoc AST walker; partially expressible as `ruff`/`pylint` custom rules.
  - **Raised by** — Claude Haiku, GPT-5, Grok.
  - **Variance** — GPT-5 caps retries at ≤3 with exponential backoff; Haiku focuses on timeout presence; Grok focuses on try/except coverage.

- **Check** — Verify README.md for each suite contains required sections (Scope, Scoring, Datasets, Known Limitations, Changelog).
  - **Signal** — Parsed markdown headings.
  - **Tool candidate** — ad-hoc (markdown AST + case-insensitive heading match).
  - **Raised by** — GPT-5, Claude Haiku.
  - **Variance** — Substantively agreed; heading names differ slightly.

- **Check** — Verify eval runner code does not retry failing scoring decisions (distinct from transport-layer retries).
  - **Signal** — AST of runner/scorer code.
  - **Tool candidate** — ad-hoc AST walker.
  - **Raised by** — Claude Opus (Haiku's "don't ignore flaky cases" is adjacent).
  - **Variance** — Opus distinguishes HTTP-error retries (allowed, scoped to network call) from score-retry loops (violation).

### Singleton checks

- **Check** — Verify no train/test content-hash overlap across splits.
  - **Signal** — Parsed dataset + sha256 of normalized `input`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Verify judge prompt templates do not reference `expected`/`gold`/`answer_key` fields except via allowlisted rubric-reference variables.
  - **Signal** — Judge prompt template + AST of judge-invocation code.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verify repository has a lockfile (`poetry.lock`, `uv.lock`, pinned `requirements.txt`) and a single-command reproducible entrypoint.
  - **Signal** — Filesystem + dependency manifest.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verify summary artifact reports latency as p50/p95/p99, not only mean/avg.
  - **Signal** — Summary JSON/Markdown.
  - **Tool candidate** — JSON Schema validator.
  - **Raised by** — Claude Opus.

- **Check** — Verify `.gitattributes` configures Git LFS for large dataset file extensions.
  - **Signal** — `.gitattributes` file.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — Gemini.

- **Check** — Verify evaluation configuration (model, temperature, endpoint) is loaded from config rather than hardcoded as string literals in code.
  - **Signal** — AST of runner code.
  - **Tool candidate** — ad-hoc AST walker.
  - **Raised by** — Gemini.

- **Check** — Verify scorer modules are accompanied by a colocated rubric/specification (docstring or adjacent markdown).
  - **Signal** — Source code + filesystem.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Haiku.

- **Check** — Verify negative-case coverage meets a minimum threshold (e.g., ≥5% of regression set).
  - **Signal** — Parsed dataset.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Verify summary reports include bootstrap/Wilson 95% CI fields for each gated metric.
  - **Signal** — Summary JSON.
  - **Tool candidate** — JSON Schema validator.
  - **Raised by** — GPT-5.

- **Check** — Verify source code is formatted to a pinned formatter (Black/ruff).
  - **Signal** — Raw source files.
  - **Tool candidate** — `black --check`, `ruff format --check`.
  - **Raised by** — Grok.

---

## 6. Final Rules File

# LLM Evaluation Suite Rules

**Scope.** Standards for designing, running, and maintaining automated evaluation suites for LLM applications (prompts, agents, RAG pipelines).
**Audience.** ML engineers, applied scientists, and AI coding assistants authoring eval code, datasets, and CI configuration.
**Goal.** Reproducible, trustworthy, cost-aware metrics that produce actionable regression signals.

## Structure & Organization

- Keep evaluation code in a dedicated top-level directory (e.g., `evals/`), separate from production code, with no production imports from it.
- Separate dataset, runner, scorer, and reporter into distinct modules so each can be swapped independently.
- Use a consistent per-suite directory layout (e.g., `dataset.jsonl`, `scorer.yaml`, `runner.yaml`, `README.md`, `golden.json`).
- Store datasets as versioned JSONL or Parquet files, not as Python literals. Small inline fixtures are allowed only for unit-testing the scorer itself.
- Version large dataset files with Git LFS (or equivalent) via `.gitattributes`.

## Dataset Design

- Assign every test case a stable, unique, human-meaningful ID (not array indices or opaque UUIDs only).
- Tag every case with structured metadata: capability/topic, difficulty, split (`train`/`dev`/`test`), provenance (`synthetic`/`curated`/`production`/`adversarial`), and a human-readable rationale for why the case exists.
- Define and check dataset records against a JSON Schema committed in the repo.
- Version datasets with semver in a manifest; record `dataset_version` in every run artifact.
- Maintain a frozen regression set separate from an exploratory development set. Never modify regression-set cases to make failing tests pass.
- Stratify datasets by difficulty and source; do not oversample easy cases.
- Include explicit negative cases (should-refuse, should-abstain, out-of-scope) — at least ~5% of the regression set.
- Prevent train/test leakage by content-hash comparison across splits.
- Exclude PII, secrets, and unanonymized production data. If sampled production data is required, redact or pseudonymize it before commit.
- Audit the evaluation set against training data and production logs on a recurring schedule.
- Target 50–500 cases per capability; require n≥100 for any gating metric.

## Scoring & Metrics

- Prefer deterministic scoring (exact match, regex, JSON schema validation, numeric tolerance) whenever the task permits. Design tasks to produce structured outputs so deterministic scoring is viable.
- Match the scorer to the task: exact match for structured extraction, rubric-based programmatic checks for targeted properties, LLM-as-judge only for semantic criteria other methods cannot capture.
- Do not use BLEU, ROUGE, or embedding similarity as primary quality metrics for generative tasks. *(contested)*
- Apply deterministic text normalization (lowercase, trim, whitespace-collapse, punctuation canonicalization) before exact or fuzzy match.
- Define explicit pass/fail thresholds (and any fuzzy-match cutoffs) before running the evaluation; document thresholds in the README.
- Pin scorer type, version, and configuration in a committed config file.
- Run the subject model at `temperature=0` with a fixed seed where supported. Allow `temperature>0` only with an explicit annotation (e.g., `# eval: stochastic-allowed`) and multi-sample aggregation.
- For multi-step or agent tasks, score intermediate steps (tool choice, trajectory) independently from final outputs.

## LLM-as-Judge

- Pin the judge model with a fully-versioned identifier (e.g., `gpt-4o-2024-08-06`, not `gpt-4o`). Pin the judge prompt by content hash. Treat changes to either as breaking.
- Run judges at `temperature=0` (or a fixed deterministic value).
- Constrain judge outputs to a JSON schema.
- Calibrate every LLM judge against human labels on a holdout before trusting it; publish agreement (e.g., Cohen's κ) and fail the suite if calibration is below threshold (target κ ≥ 0.7).
- Sample-review 5–10% of judge decisions on an ongoing basis; alert on rising disagreement rates.
- Prefer pairwise comparison over absolute rating for quality judgments. *(contested)*
- Use at least two independent judges with a deterministic tie-breaker; count undecided outcomes explicitly.
- Never include the expected/gold answer in the judge prompt unless the design explicitly requires it and the allowance is annotated.
- Log the full judge response (score, rationale, parameters) per case for post-hoc inspection.

## Regression Tracking

- Persist per-case raw outputs, scores, and metadata for every run — not just aggregates.
- Record full run provenance: subject model, prompt hash, dataset version, retrieval index hash (where applicable), code SHA, scorer version, config hash.
- Report confidence intervals (bootstrap or Wilson) on aggregate metrics; require statistical significance before gating.
- Track metrics sliced by capability and tag, not just overall score. Fail builds on per-capability regressions, not only global regressions.
- Diff against a committed `golden.json` of prior passing results.
- Never retry failing eval cases to get them to pass. Transport-layer retries (HTTP 429/5xx/timeout) are allowed only if scoped strictly to the network call.

## Cost & Latency

- Record `input_tokens`, `output_tokens`, `latency_ms`, `cost_usd`, and (where relevant) `tool_calls` per case and in aggregate.
- Report latency as p50/p95/p99 — not only mean or average.
- Set and enforce a per-run budget cap; fail fast when exceeded.
- Gate merges on cost and latency budgets in addition to quality thresholds. Do not block CI on latency alone without an observed production SLO.
- Cache deterministic intermediate artifacts (model responses, retrieval results) keyed by the full input + model + generation config.

## Reproducibility & Execution

- Pin model identifier, temperature, top_p, max_tokens, seed, and endpoint in a versioned runner config.
- Hash and commit all prompts and tool schemas referenced in a run.
- Make every eval run reproducible from a single command with pinned dependencies (lockfile present).
- Use a tiered execution model: fast smoke subset on every PR, full suite nightly or on release branches. *(contested)*
- Parallelize case execution with a concurrency cap and rate-limit handling; do not exceed vendor QPS.

## Safety & Robustness

- Run a dedicated safety/refusal suite separate from capability evals, with its own metrics and thresholds.
- Include prompt-injection, jailbreak, and tool-abuse test cases explicitly tagged.
- Test for PII leakage using synthetic and pattern-based inputs.
- Never check secrets or API keys into the repository; scan with `gitleaks` or equivalent in CI.
- Prohibit silent fallbacks to different models, parameters, or regions; require an explicit `fallback_allowed` flag.

## Error Handling

- Implement bounded retries (max 3) with exponential backoff and explicit per-call timeouts.
- Log all non-2xx API responses and mark affected cases as `infra_error`, excluded from the quality denominator — not counted as model failures.
- On partial run failure, log which cases completed and which did not; support resume or partial reporting.

## RAG Specifics

- Evaluate retrieval and generation as separate metrics; log `retrieved_ids`, `ground_truth_ids`, `hit@k`, MRR, and `context_token_count` per case.
- Pin `top_k` and retrieval parameters in the runner config.
- Include at least one no-context baseline and one oracle-context baseline.
- Include groundedness/faithfulness checks that verify claims against retrieved context.
- Record document provenance and a content hash for every retrieved chunk.

## Agent Specifics

- Log every tool call with `chain_id`, tool name, input, output, and latency.
- Evaluate tool-choice accuracy separately from final-task success.

## Style & Documentation

- Write a README per suite with Scope, Scoring, Datasets, Known Limitations, and Changelog sections.
- Use descriptive, human-readable names for test cases and functions. Avoid `test_1`, `case_xyz`, or index-based IDs.
- Define thresholds, model names, and API parameters as named constants or config values — not magic numbers in assertions.
- Run a formatter (Black, `ruff format`) and linter in CI on evaluation code.
- On failure, the error message must identify the case ID and show actual vs. expected output in full (with a truncation note if output exceeds ~1000 characters).
- Maintain a visible metrics dashboard or report showing pass rates, cost, and latency across versions.