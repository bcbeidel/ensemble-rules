# Synthesis of dbt SQL Models Best-Practices Guidance

## 1. Consensus Rules

### Structure & Layering

- **Organize models into staging, intermediate, and marts layers.** Clear layering separates concerns and makes lineage navigable. *(substantively similar but differently worded across all 5 models)*
- **Reference raw data only via `source()` in staging; reference other models via `ref()` everywhere else.** These macros build the DAG, enable environment isolation, and centralize source coupling. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*
- **Do not hardcode database/schema/table names in model SQL.** Hardcoded relations break environment isolation and dbt's dependency resolution. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Keep staging models 1:1 with a single source table, limited to renaming/casting/light coercion.** Staging is the single canonical cleanup point for each source. *(substantively similar across Claude Opus, Claude Haiku, Gemini)*

### Naming Conventions

- **Name staging models `stg_<source>__<entity>` (or similar), intermediate `int_<...>`, and marts `dim_<entity>`/`fct_<event>`.** Predictable prefixes make lineage legible and enable grep/tooling. *(near-identical across GPT-5, Claude Opus, Claude Haiku; Gemini and Grok use slightly different separator conventions)*
- **Use snake_case for all model, CTE, and column names.** Consistency avoids quoting issues across warehouses and tools. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Grok)*

### SQL Style

- **Never use `SELECT *` in production model output (exception: import CTEs).** Explicit columns preserve lineage and survive upstream schema drift. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Structure models as CTEs ending in a final `SELECT`; avoid nested subqueries.** Named, sequential steps are more readable and debuggable. *(substantively similar across Claude Opus, Claude Haiku, Gemini, Grok)*
- **Use consistent formatting enforced by a linter (e.g., SQLFluff).** Automated formatting eliminates style debates. *(substantively similar across GPT-5, Claude Opus, Gemini, Grok)*

### Testing

- **Add `unique` and `not_null` tests on the primary key of every model.** These are the minimum checks that catch fan-out joins and silent dedup failures. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Add `relationships` tests on foreign keys (at least in marts).** Referential integrity prevents orphaned records. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*
- **Every model must have at least one test before merge.** Untested models rot silently. *(substantively similar across Claude Opus, Claude Haiku, GPT-4o-mini, Grok)*

### Documentation

- **Every model must have a non-empty `description` in `schema.yml`.** Descriptions document purpose, grain, and ownership. *(near-identical across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini)*
- **Document the grain (e.g., "one row per order") of every mart model.** Grain is the contract with consumers; if you can't state it, the model is wrong. *(substantively similar across Claude Opus, Claude Haiku)*
- **Document every column whose meaning isn't obvious.** Column semantics belong in version control, not tribal knowledge. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Materialization & Incremental

- **Choose materialization based on cost/freshness: default to `view`, promote to `table` when query cost justifies it, use `incremental` only when full refresh is too slow/expensive.** Materialization is a tradeoff; pick deliberately. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, GPT-4o-mini, Grok)*
- **Always define `unique_key` on incremental models unless the source is provably append-only.** Without it, late-arriving data silently duplicates. *(near-identical across GPT-5, Claude Opus, Claude Haiku, GPT-4o-mini, Grok)*
- **Gate incremental logic behind `{% if is_incremental() %}` with a filter on an indexed/partition column.** Unfiltered incrementals defeat the purpose. *(substantively similar across GPT-5, Claude Opus)*
- **Do not write manual DML (INSERT/UPDATE/DELETE/MERGE) in model SQL.** Models are declarative; dbt controls DDL via materializations. *(substantively similar across GPT-5, Claude Opus)*

## 2. Strong Minority Rules

- **Don't let marts reference other marts.** (Claude Opus) Cross-mart dependencies create tangled DAGs; extract shared logic into intermediate. Worth keeping — it captures a common, pernicious DAG anti-pattern that the other models don't name explicitly.
- **Don't use `ORDER BY` or `LIMIT` in persistent models.** (GPT-5) Tables are unordered; `ORDER BY` wastes compute and misleads consumers, and `LIMIT` masks data issues. Worth keeping — these are real footguns and easily checked.
- **Don't use nondeterministic functions (`now()`, `current_timestamp`, `random()`, `uuid()`) in persistent models.** (GPT-5) Breaks reproducibility and incremental correctness. Worth keeping — subtle and important.
- **Suffix timestamp columns with `_at`, date columns with `_date`, boolean columns with `is_`/`has_` prefix.** (Claude Opus, Claude Haiku) Type and intent visible at a glance. Worth keeping — low cost, high readability payoff.
- **Qualify every column with its table/CTE alias in any query with more than one source.** (Claude Opus, Claude Haiku) Prevents silent ambiguity bugs. Worth keeping — catches a real class of subtle defects.
- **Verify that `dbt run --full-refresh` reproduces the same table as the incremental path.** (Claude Opus) If it doesn't, the model is broken. Worth keeping as a design principle even though checking it is expensive.
- **Set `meta.owner` on every model.** (GPT-5, Claude Haiku) Ownership enables routing and accountability. Worth keeping — operationally valuable and trivially checkable.
- **Filter as early as possible (ideally in staging).** (Claude Opus, Gemini) Reducing data volume early is the cheapest performance win. Worth keeping — a rare performance rule with broad applicability.

## 3. Divergences

### Staging scope: strict 1:1 vs. allowing light domain logic

- **Strict 1:1** (Claude Opus, Gemini): staging is only renaming, casting, trivial coercion — no joins, no aggregations, no business logic.
- **More permissive** (Claude Haiku): staging may apply some domain logic (standardize timestamps, flag nulls, decode enums) because "domain logic belongs in version control."
- **Synthesis**: Favor the strict position. It produces more predictable DAGs and is easier to enforce mechanically. The "permissive" argument conflates where code lives with what it does — light standardization (casting, nullif, trim) is fine; joins and aggregations belong in intermediate.

### Keyword casing: UPPER vs. lower

- **Uppercase keywords** (GPT-5): improves scannability.
- **Lowercase keywords** (Claude Opus): reduces visual noise.
- **Both flag it contested.**
- **Synthesis**: Pick one per project and enforce via SQLFluff (`CP01`). The choice matters less than the consistency.

### Incremental strategy default

- **Prefer `merge`** (GPT-5, Claude Opus): correct on mutable data; handles updates cleanly.
- **Full-refresh over incremental when possible** (Claude Haiku): incremental is complexity debt.
- **Synthesis**: Both are compatible. Default to full refresh; when incremental is required, use `merge` unless you have a specific reason (e.g., partitioned warehouse with `insert_overwrite`, or provably append-only data).

### Ephemeral materialization

- **Don't use it** (Claude Opus): inlines SQL and destroys debuggability.
- **Not mentioned** by other models.
- **Synthesis**: Discourage but don't ban. Ephemerals have niche uses; document when they're appropriate.

### Per-model config vs. `dbt_project.yml`

- **Config at top of model** (GPT-5): co-located, reviewable.
- **Config by directory in `dbt_project.yml`** (Claude Opus): centralized, easier to audit.
- **Synthesis**: Prefer directory-level config in `dbt_project.yml` for defaults; use per-model config for exceptions. Both are valid; consistency within a project is what matters.

### `SELECT DISTINCT`

- **Ban in marts** (GPT-5): hides root-cause duplication.
- **Not mentioned** by others.
- **Synthesis**: Treat as a smell, not a hard ban. Flag it, require justification in a comment.

## 4. Notable Omissions

- **GPT-4o-mini** omitted nearly every specific rule the others converged on: no mention of `ref()`/`source()` macros, no mention of `unique`/`not_null` tests specifically, no mention of `SELECT *`, no mention of incremental `unique_key`, no mention of snake_case. Its rules file is generic software-engineering advice with "dbt" attached; it carries less independent signal.
- **Grok** omitted layering/DAG discipline rules (no explicit rule that marts shouldn't reference marts; no rule about staging 1:1 with sources; no rule against hardcoded references). Its rules read more as general-purpose style guidance than dbt-specific architecture.
- **GPT-4o-mini and Grok** both omit the `is_incremental()` gating rule, which every other model considers essential for correct incremental behavior.
- **GPT-4o-mini** omits `relationships` tests on foreign keys, which Claude Opus, Claude Haiku, GPT-5, and Gemini all include.
- **Gemini** omits any rule about `ORDER BY`/`LIMIT` in persistent models, which GPT-5 flags as important safety.
- **Claude Haiku** is alone in including several governance rules (`required-version`, `warn_error_threshold`, `quoting` defaults) — absent from all other models. Useful, but the absence across four others suggests they're lower priority or project-specific.

## 5. Shared Deterministic Checks

### Shared checks (multiple models)

- **Check** — Verify every model file lives under a recognized layer directory (`staging/`, `intermediate/`, `marts/`) or a configured equivalent.
  - **Signal** — File path under `models/`.
  - **Tool candidate** — ad-hoc (path glob); `dbt-project-evaluator` covers related checks.
  - **Raised by** — GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku.
  - **Variance** — GPT-5 requires exactly these three folders; Claude Opus and Haiku allow a configurable whitelist for `utilities/`, `snapshots/`, etc. Substance is the same.

- **Check** — Verify staging model filenames match `stg_<source>__<entity>` pattern; intermediate match `int_...`; marts match `(dim|fct)_...`.
  - **Signal** — File basename.
  - **Tool candidate** — ad-hoc regex; `dbt-project-evaluator`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Grok.
  - **Variance** — Separator conventions differ: some require double-underscore for staging (`stg_source__entity`), others accept single underscore. Mart prefix set varies (`dim`/`fct` vs. also allowing `rpt`/`agg`). Configure per project.

- **Check** — Flag any `SELECT *` outside of explicit import CTEs.
  - **Signal** — Parsed SQL AST.
  - **Tool candidate** — SQLFluff rules `AM04`/`L044`.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Claude Opus explicitly exempts import CTEs; others apply blanket bans. The import-CTE exemption is the more useful version.

- **Check** — Flag any dot-qualified table reference outside `ref()`/`source()` calls.
  - **Signal** — Raw SQL (with Jinja-aware tokenization) or compiled SQL.
  - **Tool candidate** — `dbt-project-evaluator` (`fct_hard_coded_references`); `dbt-checkpoint` `check-hard-coded-references`.
  - **Raised by** — GPT-5, Claude Opus, Gemini, Grok.
  - **Variance** — GPT-5 and Gemini suggest regex; Claude Opus correctly notes Jinja-aware parsing is needed to avoid false positives. Use the off-the-shelf tool.

- **Check** — Every model in `manifest.json` has a non-empty `description`.
  - **Signal** — Parsed `manifest.json`.
  - **Tool candidate** — `dbt-project-evaluator` (`fct_undocumented_models`).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok, GPT-4o-mini.
  - **Variance** — Claude Opus additionally asserts length > 20 chars and not equal to the model name. Others just check presence. The stricter version is preferable.

- **Check** — Every model has at least one column with both `unique` and `not_null` tests.
  - **Signal** — Parsed `manifest.json` or `schema.yml`.
  - **Tool candidate** — `dbt-project-evaluator` (`fct_missing_primary_key_tests`).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — None substantive; all acknowledge this can't verify the tested column is truly the intended PK.

- **Check** — Every incremental model (`config.materialized == "incremental"`) has `unique_key` set.
  - **Signal** — Parsed `manifest.json`.
  - **Tool candidate** — ad-hoc over `manifest.json`.
  - **Raised by** — GPT-5, Claude Opus, GPT-4o-mini, Grok.
  - **Variance** — Claude Opus allows opt-out via `append_only` tag; GPT-5 additionally requires `on_schema_change='sync_all_columns'`. The opt-out pattern is more realistic.

- **Check** — Every incremental model contains at least one `is_incremental()` Jinja block.
  - **Signal** — Raw SQL.
  - **Tool candidate** — ad-hoc regex.
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Claude Opus additionally requires a `where` clause inside the block; GPT-5 just checks presence. The stricter version catches more defects.

- **Check** — Staging model files contain exactly one `{{ source(...) }}` call and zero `{{ ref(...) }}` calls.
  - **Signal** — Raw SQL.
  - **Tool candidate** — ad-hoc regex or `manifest.json` inspection.
  - **Raised by** — Claude Opus, Gemini.
  - **Variance** — Gemini uses `manifest.json` (more robust); Claude Opus uses raw text scan.

- **Check** — SQL keyword casing consistent per project (upper or lower).
  - **Signal** — Parsed SQL.
  - **Tool candidate** — SQLFluff rule `CP01`.
  - **Raised by** — GPT-5 (uppercase), Claude Opus (lowercase), Grok (implicit).
  - **Variance** — Direction contested; the check exists, the setting is configurable.

- **Check** — Flag `ORDER BY` and `LIMIT` in non-ephemeral model SQL (excluding `ORDER BY` inside `OVER()` window clauses).
  - **Signal** — Parsed SQL AST.
  - **Tool candidate** — ad-hoc via AST (`sqlglot`).
  - **Raised by** — GPT-5 (both), Claude Haiku (ordering partially).
  - **Variance** — GPT-5 is explicit; Haiku's window-function check is related but narrower.

### Singleton checks worth promoting

- **Check** — Flag `select * except (...)` in Snowflake/BigQuery projects. *(Signal: raw SQL + warehouse type; Tool: ad-hoc regex; Raised by: Claude Haiku.)*
- **Check** — Flag presence of DDL/DML (`CREATE`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`, `TRUNCATE`) as a top-level statement in a model file. *(Signal: SQL AST; Tool: ad-hoc via `sqlglot`; Raised by: GPT-5, Claude Opus.)*
- **Check** — Flag use of nondeterministic functions (`now()`, `current_timestamp`, `random()`, `uuid()`) outside Jinja/comments. *(Signal: raw SQL + token filter; Tool: ad-hoc regex; Raised by: GPT-5.)*
- **Check** — Run a secret scanner over `models/` to catch committed credentials/PII. *(Signal: raw file contents; Tool: `gitleaks` or `trufflehog`; Raised by: Claude Opus.)*
- **Check** — Flag models in `marts/` that depend on other `marts/` models via `manifest.json` `depends_on.nodes`. *(Signal: `manifest.json`; Tool: ad-hoc; Raised by: Claude Opus.)*
- **Check** — Flag models in `marts/` that contain `SELECT DISTINCT`. *(Signal: raw SQL; Tool: ad-hoc regex; Raised by: GPT-5.)*
- **Check** — Flag `CROSS JOIN` occurrences without an override comment. *(Signal: raw SQL; Tool: ad-hoc regex; Raised by: GPT-5.)*
- **Check** — Verify every staging model has `tags: ['staging']` (or equivalent per layer) in its config or YAML. *(Signal: raw SQL config block or `schema.yml`; Tool: ad-hoc; Raised by: GPT-5.)*
- **Check** — Verify every model has a non-empty `meta.owner` field. *(Signal: `manifest.json`; Tool: ad-hoc; Raised by: GPT-5, Claude Haiku.)*
- **Check** — Flag window functions used without an `ORDER BY` in the `OVER()` clause. *(Signal: SQL AST; Tool: ad-hoc via `sqlglot`; Raised by: Claude Haiku.)*
- **Check** — Verify boolean-typed columns (per `catalog.json`) have names prefixed `is_`/`has_`; timestamp-typed columns end in `_at`; date-typed columns end in `_date`. *(Signal: `catalog.json`; Tool: ad-hoc; Raised by: Claude Opus, Claude Haiku.)*
- **Check** — Flag any staging model whose AST contains `JOIN`, `GROUP BY`, `HAVING`, `UNION`, or window functions. *(Signal: SQL AST; Tool: ad-hoc via `sqlglot`; Raised by: Claude Opus.)*

---

## 6. Final Rules File

# dbt SQL Models — Rules

**Scope:** SQL model files under `models/` in a dbt project (Core or Cloud, dbt v1.0+).
**Audience:** Analytics engineers and AI coding assistants authoring or reviewing dbt models.
**Goal:** Specify what "good" looks like — readable, safe, correct, and performant by default. Deviations are allowed when justified and documented.

---

## Structure & Layering

- **Place every model in exactly one of `staging/`, `intermediate/`, or `marts/`.** Clear layering is the foundation of a maintainable dbt project.
- **Reference raw data only via `{{ source() }}`, and only in staging models.** Nothing else should touch raw tables; source coupling stays in one layer.
- **Reference other models only via `{{ ref() }}`, never by hardcoded name.** `ref` builds the DAG and enables environment isolation.
- **Keep staging models 1:1 with a single source table.** One staging model per source table gives each source a single canonical cleaned version.
- **Restrict staging logic to renaming, casting, and trivial coercion.** No joins, aggregations, or business logic in staging.
- **Put reusable joins and business logic in `intermediate/`.** Marts should read like a final assembly, not a recipe.
- **Don't let marts reference other marts.** Cross-mart dependencies create tangled DAGs; extract shared logic into intermediate.
- **Don't reference a higher layer from a lower one.** Staging must not `ref()` intermediate or marts; intermediate must not `ref()` marts.
- **Put one logical transformation per model.** Single responsibility simplifies testing and change.

## Naming

- **Name staging models `stg_<source>__<entity>`.** Double underscore unambiguously separates source from entity.
- **Name intermediate models with an `int_` prefix describing transformation and subject.** Signals the transformation step.
- **Name fact tables `fct_<event>` and dimension tables `dim_<entity>`.** Standard dimensional naming makes marts navigable.
- **Use snake_case for all model, CTE, and column names.** Consistent casing avoids quoting issues across warehouses.
- **Prefix boolean columns with `is_` or `has_`.** Makes boolean type obvious at call sites.
- **Suffix timestamp columns with `_at` and date columns with `_date`.** Type and granularity visible at a glance.
- **Prefix foreign keys with the dimension name (e.g., `customer_id`, not `id`).** Foreign keys should name their target.
- **Don't use abbreviations in model or column names unless widely understood in the domain.** Full names age better than clever short forms.

## SQL Style

- **Write every model as a series of CTEs ending in a final `select`.** Consistent shape makes every model scannable.
- **Start each model with import CTEs that simply select from `ref()`/`source()` calls.** Separates dependency declaration from logic.
- **Don't use `SELECT *` outside of import CTEs.** Explicit columns preserve lineage and survive upstream schema changes.
- **Don't use subqueries where a CTE works.** CTEs are named, debuggable, and reusable.
- **Qualify every column with its table/CTE alias when more than one source is in scope.** Ambiguity bugs are silent and nasty.
- **Don't use single-character or meaningless table aliases like `t1`.** Use the CTE name or a readable abbreviation.
- **Pick one SQL keyword case convention per project and enforce it via SQLFluff.** The choice matters less than the consistency.
- **Use trailing commas before `FROM` or `GROUP BY`.** Cleaner diffs when adding or removing columns.
- **Format all SQL with an automated formatter (e.g., SQLFluff).** Automated formatting eliminates debates.

## Documentation

- **Every model must have a non-empty `description` in its YAML.** Describe purpose, grain, and owner.
- **Declare the grain of every mart model (e.g., "one row per order") in its description.** If you can't state the grain in one sentence, the model is wrong.
- **Document every column whose meaning isn't obvious from its name.** Skip trivial ones; don't waste reviewer attention.
- **Document the incremental strategy and `unique_key` in the description of incremental models.** Future maintainers need to know the contract.
- **Set `meta.owner` on every model.** Ownership enables routing and accountability.

## Testing

- **Add `unique` and `not_null` tests on the primary key of every model.** The minimum that catches fan-out and silent dedup failures.
- **Add `relationships` tests on foreign keys in marts.** Catches referential breakage. Skip only for known-nullable or very high-volume FKs with documented justification.
- **Add `accepted_values` tests to low-cardinality categorical columns.** Catches upstream enum drift.
- **Every new model must have at least one test before merge.** Untested models rot silently.
- **CI must run `dbt build` (or `dbt run` + `dbt test`) and block merges on failure.** Tests that don't gate merges don't protect production.

## Materialization

- **Default to `view`.** Cheapest to build, always fresh, no storage cost.
- **Promote to `table` when query cost exceeds build cost.** Typical for marts and heavily-joined intermediates.
- **Use `incremental` only when full-refresh runtime or cost is unacceptable.** Incremental is complexity debt; don't take it on speculatively.
- **Don't use `ephemeral` as a default.** Inlining SQL into consumers destroys debuggability; use it only for genuinely private helpers.
- **Prefer setting materialization by directory in `dbt_project.yml`; override per-model only for exceptions.** Centralized defaults are easier to audit.

## Incremental Models

- **Always define `unique_key` on incremental models unless the source is provably append-only.** Without it, late-arriving data silently duplicates.
- **Use `merge` strategy by default; use `insert_overwrite` only on partitioned tables with a stable partition column.** `merge` is correct; `insert_overwrite` is fast but error-prone.
- **Gate incremental logic behind `{% if is_incremental() %}` with a `where` clause on an indexed/partition column.** Unfiltered incremental scans defeat the purpose.
- **Use a lookback window (e.g., `>= (select max(updated_at) from {{ this }}) - interval '3 days'`) for late-arriving rows.** Protects against data arriving out of order.
- **Ensure `dbt run --full-refresh` produces the same table as the incremental path.** If it doesn't, the model is broken.
- **Don't use `append` strategy on mutable source data.** Produces silent duplicates on updates.
- **Don't write manual `INSERT`/`UPDATE`/`DELETE`/`MERGE` SQL in models; rely on dbt's incremental materialization.** Centralizes change logic.

## Safety

- **Don't hardcode database/schema/table names in model SQL.** Use `{{ ref }}`, `{{ source }}`, or `{{ target }}`; hardcoding breaks env isolation.
- **Don't write DML or DDL other than `SELECT` in a model.** Models are declarative; side effects belong in hooks or operations.
- **Don't use `ORDER BY` in persistent models.** Tables and views are unordered; ordering wastes compute and misleads consumers.
- **Don't use `LIMIT` in persistent models.** `LIMIT` masks data issues and distorts aggregates.
- **Don't use nondeterministic functions (`now()`, `current_timestamp`, `random()`, `uuid()`) in persistent models.** Nondeterminism breaks reproducibility and incremental correctness.
- **Don't commit secrets, credentials, or PII sample data in model files or YAML.** Use `env_var` and secret management.
- **Cast keys explicitly; don't rely on implicit casts.** Prevents type surprises and join mismatches.

## Performance

- **Filter as early as possible — ideally in staging.** Less data through the DAG is cheaper everywhere downstream.
- **Don't use `SELECT DISTINCT` as a deduplication strategy in marts.** Fix root-cause duplication upstream; `DISTINCT` hides the bug and wastes compute.
- **Avoid `CROSS JOIN`.** Rarely intended; require an inline comment justifying it when used.
- **Don't join on casted or coerced columns when a natural key exists.** Destroys index/partition pruning.
- **For large incremental tables, configure partitioning and/or clustering where the warehouse supports it.** Prunes scans.

---

**Notes on contested rules:** Keyword casing (upper vs. lower), exact intermediate naming conventions, whether to materialize intermediate models as tables, and exactly how much logic belongs in staging are all subjects of reasonable disagreement. Pick one convention per project and enforce it via tooling — consistency matters more than the specific choice.