# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Avoid materializing intermediate models as tables unless they are used in 3+ downstream models and run time is > 2 minutes.** | Performance |  |  |  | ✓ |  |  | 1 |
| **(contested) Prefer full-refresh strategies for mart-layer models and reserve incremental for high-volume fact tables with append-only logic.** | Materialization & Incremental Logic |  |  |  | ✓ |  |  | 1 |
| **Add `accepted_values` tests to every low-cardinality categorical column.** Catches upstream enum drift | Tests |  |  | ✓ |  |  |  | 1 |
| **Add `relationships` tests on foreign keys in marts.** (contested) Expensive on large tables; skip on known-nullable or high-volume FKs | Tests |  |  | ✓ |  |  |  | 1 |
| **Add a `meta.owner` field in `schema.yml` for every mart model and pair it with a Slack channel or email for questions.** | Safety & Change Management |  |  |  | ✓ |  |  | 1 |
| **Add a `pre_hook` or `post_hook` comment if a model depends on external state or triggers downstream actions; document the dependency.** | Testing & Documentation |  |  |  | ✓ |  |  | 1 |
| **Add a comment above any `join` that is not intuitively one-to-one or one-to-many, e.g., `-- many-to-many: accounts may have multiple contacts`.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Add a row-count test on every mart model: `assert row_count > 0` and, if possible, `assert row_count <= <previous_run_count> * 1.1` to catch sudden bloat.** | Testing & Documentation |  |  |  | ✓ |  |  | 1 |
| **Always cast string columns that represent codes or enums to explicitly named types, e.g., `lower(trim(status))::varchar(50)`, not just `status`.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Always define `unique_key` on incremental models unless the source is provably append-only.** Without it, late-arriving data silently duplicates | Incremental Models |  |  | ✓ |  |  |  | 1 |
| **Avoid subqueries in the `from` clause; use CTEs instead for readability.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Avoid window functions in CTEs that feed other window functions; use separate CTEs or consider a single pass with nested CTEs.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Begin every model with a `select` statement; do not use CTEs for single-table models or trivial aliasing.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Declare a `unique` and `not_null` test on the primary key of every model.** Catches fan-out and dedup bugs immediately | Tests |  |  | ✓ |  |  |  | 1 |
| **Declare the grain of every mart model in its YAML description.** If you can't state the grain in one sentence, the model is wrong | Tests |  |  | ✓ |  |  |  | 1 |
| **Default to `view` for staging and intermediate models; use `table` only when run time > 1 minute or refresh frequency requires it.** | Materialization & Incremental Logic |  |  |  | ✓ |  |  | 1 |
| **Default to `view` materialization.** Cheapest to build, always fresh | Materialization |  |  | ✓ |  |  |  | 1 |
| **Define a primary key test on every mart model and every staging model; use `unique` + `not_null` or `dbt_expectations.expect_compound_columns_to_be_unique` for composites.** | Testing & Documentation |  |  |  | ✓ |  |  | 1 |
| **Disable `quoting` by default; enable it only for reserved keywords or spaces in names.** | dbt Configuration & Governance |  |  |  | ✓ |  |  | 1 |
| **Do not add indexes or partitions to dbt models; configure them in the database layer or document them in a post-hook.** | Performance |  |  |  | ✓ |  |  | 1 |
| **Do not introduce or rename columns without updating `schema.yml` and tests; breaking downstream models is a production incident.** | Column Naming & Type Conventions |  |  |  | ✓ |  |  | 1 |
| **Do not modify the grain or cardinality of a mart model without a major version bump and migration period.** | Safety & Change Management |  |  |  | ✓ |  |  | 1 |
| **Do not nest subqueries; use CTEs instead.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Do not query source tables directly in intermediate or mart models; always go through staging.** | Layering & Naming |  |  |  | ✓ |  |  | 1 |
| **Do not use abbreviations in model names unless widely understood in your domain, e.g., `KPI`, `ARR`; avoid `acct`, `mgr`, `svc`.** | Layering & Naming |  |  |  | ✓ |  |  | 1 |
| **Do not use column tests to enforce implicit business rules; use assertions or a dbt_expectations suite instead.** | Testing & Documentation |  |  |  | ✓ |  |  | 1 |
| **Document every column whose meaning isn't obvious from its name.** Skip obvious ones like `created_at`; don't waste reviewer attention | Documentation |  |  | ✓ |  |  |  | 1 |
| **Document the grain (e.g., "one row per order") and any slowly-changing dimension logic in a `description` field in `schema.yml`.** | Testing & Documentation |  |  |  | ✓ |  |  | 1 |
| **Document the incremental strategy and `unique_key` in the model description for incremental models.** Future maintainers need to know the contract | Documentation |  |  | ✓ |  |  |  | 1 |
| **Don't commit secrets, credentials, or PII sample data in model files or YAML.** Use environment variables and dbt's `env_var` macro | Safety |  |  | ✓ |  |  |  | 1 |
| **Don't hardcode database or schema names in model SQL.** Use `{{ target }}` or `{{ ref }}`; hardcoding breaks dev/prod isolation | Safety |  |  | ✓ |  |  |  | 1 |
| **Don't join on casted or coerced columns when a natural key exists.** Destroys index/partition pruning | Performance |  |  | ✓ |  |  |  | 1 |
| **Don't let marts reference other marts.** Cross-mart dependencies create tangled DAGs; extract shared logic into intermediate | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Don't merge a new model without at least one test.** Untested models rot silently | Tests |  |  | ✓ |  |  |  | 1 |
| **Don't use `append` strategy on mutable source data.** Produces silent duplicates on updates | Incremental Models |  |  | ✓ |  |  |  | 1 |
| **Don't use `select *` outside of import CTEs.** Explicit columns preserve lineage and survive upstream schema changes | SQL Style |  |  | ✓ |  |  |  | 1 |
| **Don't use ephemeral materialization.** It inlines SQL into consumers and destroys debuggability | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Don't use subqueries where a CTE works.** CTEs are named, debuggable, and reusable | SQL Style |  |  | ✓ |  |  |  | 1 |
| **Don't use table aliases shorter than 2 characters or meaningless ones like `t1`.** Use the CTE name or a readable abbreviation | SQL Style |  |  | ✓ |  |  |  | 1 |
| **Don't write DML other than `select` in a model.** Models are declarative; side effects belong in hooks or operations | Safety |  |  | ✓ |  |  |  | 1 |
| **Enable `warn_error_threshold` in `dbt_project.yml` to fail the build if > 1 warning occurs.** | dbt Configuration & Governance |  |  |  | ✓ |  |  | 1 |
| **Ensure the incremental filter uses a lookback window (e.g., `>= (select max(updated_at) from {{ this }}) - interval '3 days'`).** Protects against late-arriving rows | Incremental Models |  |  | ✓ |  |  |  | 1 |
| **Filter as early as possible, ideally in staging.** Less data through the DAG is cheaper everywhere downstream | Performance |  |  | ✓ |  |  |  | 1 |
| **For incremental fact tables, use `dbt_internal_utils.surrogate_key()` or equivalent for composite keys to avoid collisions, and test uniqueness.** | Materialization & Incremental Logic |  |  |  | ✓ |  |  | 1 |
| **For incremental models, include a `dbt_valid_from` and `dbt_valid_to` timestamp if the model supports corrections; document this in a comment.** | Materialization & Incremental Logic |  |  |  | ✓ |  |  | 1 |
| **Gate incremental logic behind `{% if is_incremental() %}` with a filter on an indexed/partition column.** Unfiltered incremental scans defeat the purpose | Incremental Models |  |  | ✓ |  |  |  | 1 |
| **Give every model a `description` in its YAML.** State purpose, grain, and owner | Documentation |  |  | ✓ |  |  |  | 1 |
| **Lowercase all SQL keywords.** (contested) Reduces visual noise; pick one convention and enforce it | SQL Style |  |  | ✓ |  |  |  | 1 |
| **Make staging models 1:1 with a source table.** One staging model per source table, no joins, so each source has a single canonical cleaned version | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Materialize as `table` when query cost exceeds build cost.** Typical for marts and heavily-joined intermediates | Materialization |  |  | ✓ |  |  |  | 1 |
| **Name aggregated or derived metrics explicitly: `total_revenue`, `count_distinct_customers`, `pct_churn`.** | Column Naming & Type Conventions |  |  |  | ✓ |  |  | 1 |
| **Name fact tables `fct_<event>` and dimension tables `dim_<entity>`.** Standard dimensional naming makes marts navigable | Naming |  |  | ✓ |  |  |  | 1 |
| **Name intermediate models `int_<domain>_<transform>`, e.g., `int_finance_revenue_by_month`.** | Layering & Naming |  |  |  | ✓ |  |  | 1 |
| **Name intermediate models `int_<entity>_<verb>ed` or `int_<entity>_<verb>ing`.** Signals the transformation step | Naming |  |  | ✓ |  |  |  | 1 |
| **Name mart models using `dim_` (slowly changing dimensions), `fact_` (grain-specific facts), or descriptive names if neither applies, e.g., `revenue_by_region`.** | Layering & Naming |  |  |  | ✓ |  |  | 1 |
| **Name staging models `stg_<source>__<table>`.** Double underscore separates source from table unambiguously | Naming |  |  | ✓ |  |  |  | 1 |
| **Name staging models `stg_<source_system>_<entity>`; do not abbreviate source names.** | Layering & Naming |  |  |  | ✓ |  |  | 1 |
| **Name surrogate keys `<entity>_sk` and natural keys `<entity>_id`.** Distinguishes generated keys from source keys | Naming |  |  | ✓ |  |  |  | 1 |
| **Never assume incremental models will re-run on past data; design them to be idempotent if corrections are possible.** | Materialization & Incremental Logic |  |  |  | ✓ |  |  | 1 |
| **Never rely on implicit ordering; use `order by` if the sequence matters, or `row_number() over (order by <key>)` to make it explicit.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Never use `select * except (...)` in Snowflake or BigQuery; enumerate columns instead.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Never use `select *` in production models.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Only use `incremental` when full-refresh runtime or cost is unacceptable.** Incremental is complexity debt; don't take it on speculatively | Materialization |  |  | ✓ |  |  |  | 1 |
| **Order CTEs from upstream (sources/seeds) to downstream (final output); place the final `select` last.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Organize models into three layers: staging (stg_), intermediate (int_), and mart (dim_/fact_).** | Layering & Naming |  |  |  | ✓ |  |  | 1 |
| **Place complex conditional logic in `case` statements, not in boolean expressions; use clear labels for branches.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Prefer `group by` on surrogate keys over multi-column natural keys in large aggregations.** Single-column group-by is faster and more cache-friendly | Performance |  |  | ✓ |  |  |  | 1 |
| **Prefix boolean columns with `is_` or `has_`, e.g., `is_active`, `has_discount`.** | Column Naming & Type Conventions |  |  |  | ✓ |  |  | 1 |
| **Prefix foreign keys with the dimension name, e.g., `customer_id`, not `cust_id` or `id`.** | Column Naming & Type Conventions |  |  |  | ✓ |  |  | 1 |
| **Profile expensive models with `dbt debug --select <model> --operation profile` or warehouse-native query profilers before optimizing.** | Performance |  |  |  | ✓ |  |  | 1 |
| **Put every model in exactly one of `staging/`, `intermediate/`, or `marts/`.** Clear layering is the foundation of a maintainable dbt project | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Put reusable joins and business logic in `intermediate/`, not in marts.** Marts should read like a final assembly, not a recipe | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Qualify all column references with their alias, even if unambiguous, in joins and multi-table queries.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Qualify every column with its table/CTE alias in any query with more than one source.** Ambiguity bugs are silent and nasty | SQL Style |  |  | ✓ |  |  |  | 1 |
| **Reference other models only via `{{ ref() }}`, never by hardcoded name.** `ref` is what builds the DAG and enables environment isolation | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Reference raw data only via `{{ source() }}` in staging models.** Nothing else should touch raw tables; this keeps source coupling in one layer | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Require a description for every column in downstream-facing models (stg_, int_, dim_, fact_); allow shorter descriptions for internal stage columns if the name is self-explanatory.** | Testing & Documentation |  |  |  | ✓ |  |  | 1 |
| **Restrict staging logic to renaming, casting, and trivial coercion.** No joins, no aggregations, no business logic in staging | Structure & Layering |  |  | ✓ |  |  |  | 1 |
| **Run `dbt test` and `dbt docs generate` before submitting a pull request; require both to pass before merge.** | Safety & Change Management |  |  |  | ✓ |  |  | 1 |
| **Set `required-version` in `dbt_project.yml` to a modern major version (e.g., `>=1.5`).** | dbt Configuration & Governance |  |  |  | ✓ |  |  | 1 |
| **Set materialization in `dbt_project.yml` by directory, not per-model, unless the model is an exception.** Centralized config is easier to audit | Materialization |  |  | ✓ |  |  |  | 1 |
| **Start each model with import CTEs named after the referenced model.** e.g | SQL Style |  |  | ✓ |  |  |  | 1 |
| **Suffix boolean columns with `is_` or `has_` prefix.** Makes type obvious at call sites | Naming |  |  | ✓ |  |  |  | 1 |
| **Suffix timestamp columns with `_at` and date columns with `_date`.** Type and granularity visible at a glance | Naming |  |  | ✓ |  |  |  | 1 |
| **Tag every breaking change (column rename, grain change, deletion) with `@breaking` in `schema.yml` and announce it in a pull request comment.** | Safety & Change Management |  |  |  | ✓ |  |  | 1 |
| **Test foreign key relationships at the source and target; use `dbt_expectations.expect_column_values_to_be_in_set` or `relationships` tests.** | Testing & Documentation |  |  |  | ✓ |  |  | 1 |
| **Use `_at` for timestamps (e.g., `created_at`, `updated_at`), `_date` for dates, and `_count` for counts.** | Column Naming & Type Conventions |  |  |  | ✓ |  |  | 1 |
| **Use `alias` in model config only to hide internal staging models; do not use it to rename public models.** | dbt Configuration & Governance |  |  |  | ✓ |  |  | 1 |
| **Use `coalesce()` to handle NULLs in joins; avoid `nvl()` or `ifnull()` for portability.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Use `incremental` materialization only when the transformation logic is append-only or supports idempotent upserts.** | Materialization & Incremental Logic |  |  |  | ✓ |  |  | 1 |
| **Use `left join` as the default; justify inner joins and cross joins with inline comments.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Use `merge` strategy by default; use `insert_overwrite` only on partitioned tables with a stable partition column.** `merge` is correct; `insert_overwrite` is fast but error-prone | Incremental Models |  |  | ✓ |  |  |  | 1 |
| **Use `meta` fields to tag sensitive columns, e.g., `meta: { pii: true, sensitivity: "high" }`; enforce masking in downstream tools.** | dbt Configuration & Governance |  |  |  | ✓ |  |  | 1 |
| **Use `select` statements over aggregation functions where possible; e.g., prefer a `group by 1` over `select distinct` if the intent is clearer.** | Performance |  |  |  | ✓ |  |  | 1 |
| **Use `surrogate_key` for composite primary keys generated by dbt, not `id` or `pk`.** | Column Naming & Type Conventions |  |  |  | ✓ |  |  | 1 |
| **Use `where 1=1` as the first condition in a where clause if subsequent conditions may be commented out; makes commenting safe.** | SQL Style & Safety |  |  |  | ✓ |  |  | 1 |
| **Use one CTE per logical transformation step; name CTEs in `snake_case` as `<step>__<subject>`, e.g., `filtered__orders`, `aggregated__daily_revenue`.** | Structure & Readability |  |  |  | ✓ |  |  | 1 |
| **Use snake_case for all model and column names.** Consistent casing avoids quoting headaches across warehouses | Naming |  |  | ✓ |  |  |  | 1 |
| **Verify that `dbt run --full-refresh` reproduces the same table as the incremental path.** If it doesn't, the model is broken | Incremental Models |  |  | ✓ |  |  |  | 1 |
| **Version your models using a `_v0`, `_v1` suffix if you need to maintain two versions during a migration period; delete the old version once the new one is validated.** | Safety & Change Management |  |  |  | ✓ |  |  | 1 |
| **Write every model as a series of CTEs ending in a final `select * from <cte>`.** Consistent shape makes every model scannable | SQL Style |  |  | ✓ |  |  |  | 1 |
| Add `not_null` and `unique` tests to the primary key of every model | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Add `relationship` tests to all foreign keys to ensure referential integrity | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Add a plain-language `description` to every model in its corresponding `.yml` file | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Add at least one test (e.g., `not_null`, `accepted_values`) to every column in a source-configured table | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Add data tests for known invariants (e.g., positive amounts, valid enums) near their source | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add not_null and unique tests on the model’s primary key column | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Add relationships tests on foreign key columns in mart models | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Alias all columns explicitly in staging models, using snake_case | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Align JOIN | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| All pull requests must pass `dbt build` in a CI job before being merged | Safety and Dependencies |  |  |  |  | ✓ |  | 1 |
| Always use the `ref()` and `source()` macros to refer to other tables | Safety and Dependencies |  |  |  |  | ✓ |  | 1 |
| Avoid CROSS JOINs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid creating subdirectories within the `models/staging` and `models/marts` directories | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Begin each model with header comments containing grain: and primary_key: | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Cast all columns to their correct data types in staging models | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Coalesce and cast keys explicitly; do not rely on implicit casts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare model config at the top: materialized, tags, and unique_key when incremental | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Default to materializing models as `view` | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| Do add a description block to every model using dbt's `{{ doc() }}` macro | Documentation |  |  |  |  |  | ✓ | 1 |
| Do add error handling, such as checks for empty sources | Safety |  |  |  |  |  | ✓ | 1 |
| Do add indexes or clustering to materialized tables where appropriate | Performance |  |  |  |  |  | ✓ | 1 |
| Do choose `incremental` materialization for large, append-only datasets | Materialization Choices |  |  |  |  |  | ✓ | 1 |
| Do define a unique key for incremental models to handle updates correctly | Incremental Strategies |  |  |  |  |  | ✓ | 1 |
| Do document column-level details, including data types and business meanings | Documentation |  |  |  |  |  | ✓ | 1 |
| Do document each model with clear descriptions in dbt's documentation files | Documentation |  | ✓ |  |  |  |  | 1 |
| Do enable dbt's full-refresh flag only in non-production environments | Safety |  |  |  |  |  | ✓ | 1 |
| Do implement incremental models where data volume warrants it | Incremental Strategies |  | ✓ |  |  |  |  | 1 |
| Do implement merge strategies for models with upserts | Incremental Strategies |  |  |  |  |  | ✓ | 1 |
| Do include at least one test per model, such as not_null or unique tests on key columns | Tests |  |  |  |  |  | ✓ | 1 |
| Do indent SQL code consistently with two spaces | Style |  |  |  |  |  | ✓ | 1 |
| Do layer models into staging, intermediate, and mart levels | Structure |  | ✓ |  |  |  |  | 1 |
| Do limit lines to 80 characters | Style |  |  |  |  |  | ✓ | 1 |
| Do limit models to one primary transformation per model file | Structure |  | ✓ |  |  |  |  | 1 |
| Do not `ref()` a model from a "higher" layer (e.g., a staging model must not `ref()` a mart model) | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Do not hard-code database.schema.table; only use ref() or source() | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not include DDL/DML (CREATE/INSERT/UPDATE/DELETE/MERGE) in model SQL | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not reference raw tables directly; use source() in staging and ref() elsewhere | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use LIMIT in persistent models | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use ORDER BY in persistent models | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use `SELECT *` in a final `SELECT` statement | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Do not use hardcoded database, schema, or table names in a model's `SELECT` statement | Safety and Dependencies |  |  |  |  | ✓ |  | 1 |
| Do not use nondeterministic functions (now(), current_timestamp, random(), uuid()) in persistent models | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use reserved words or spaces in identifiers | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not write manual MERGE/DELETE/UPDATE in model SQL; rely on dbt incremental | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do organize models into a layered architecture with staging, intermediate, and mart layers | Structure |  |  |  |  |  | ✓ | 1 |
| Do prefix model names with their layer (e.g., `stg_`, `int_`, `mart_`) | Naming Conventions |  |  |  |  |  | ✓ | 1 |
| Do use `table` materialization for marts and frequently queried models | Materialization Choices |  |  |  |  |  | ✓ | 1 |
| Do use consistent naming conventions for models, tables, and columns | Naming Conventions |  | ✓ |  |  |  |  | 1 |
| Do use dbt refs and sources consistently to reference other models or raw data | Structure |  |  |  |  |  | ✓ | 1 |
| Do use lowercase snake_case for model and column names (e.g., `staging_orders`) | Naming Conventions |  |  |  |  |  | ✓ | 1 |
| Do use partitioning for time-based incremental models | Performance |  |  |  |  |  | ✓ | 1 |
| Do use the appropriate materialization strategy based on use cases (table, view, incremental) | Materialization Choices |  | ✓ |  |  |  |  | 1 |
| Do utilize dbt's built-in testing framework for key constraints | Tests |  | ✓ |  |  |  |  | 1 |
| Do write descriptive test names that explain the expected outcome | Tests |  |  |  |  |  | ✓ | 1 |
| Don't combine multiple business logics into a single model | Structure |  |  |  |  |  | ✓ | 1 |
| Don't default to `view` for intermediate models without evaluating update frequency | Materialization Choices |  |  |  |  |  | ✓ | 1 |
| Don't hardcode sensitive values like dates or keys | Safety |  |  |  |  |  | ✓ | 1 |
| Don't leave documentation vague or incomplete | Documentation |  |  |  |  |  | ✓ | 1 |
| Don't rely solely on generic tests; customize them to business rules | Tests |  |  |  |  |  | ✓ | 1 |
| Don't select unnecessary columns in models | Performance |  |  |  |  |  | ✓ | 1 |
| Don't use generic names like `temp_table` or `data_model_1` | Naming Conventions |  |  |  |  |  | ✓ | 1 |
| Don't use incremental strategies for small, static datasets | Incremental Strategies |  |  |  |  |  | ✓ | 1 |
| Don't use overly complex SQL expressions; break them into CTEs | Style |  |  |  |  |  | ✓ | 1 |
| Don't use special characters or spaces in names | Naming Conventions |  | ✓ |  |  |  |  | 1 |
| Don’t default to using tables for all models | Materialization Choices |  | ✓ |  |  |  |  | 1 |
| Don’t forget to define unique keys for incremental models | Incremental Strategies |  | ✓ |  |  |  |  | 1 |
| Don’t neglect documenting transformations or assumptions | Documentation |  | ✓ |  |  |  |  | 1 |
| Don’t write transformation logic without accompanying tests | Tests |  | ✓ |  |  |  |  | 1 |
| Each staging model should represent one and only one source table | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Ensure the file name matches the model name | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Fail fast on unexpected schema change in non-dev targets via on_schema_change not set to ignore | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Filter data as early as possible in your CTEs | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| For large incrementals, configure partitioning and/or clustering when supported | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| For materialized='incremental', set unique_key and on_schema_change='sync_all_columns' | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Format all SQL code using a standard formatter like SQLFluff | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Generate surrogate keys with dbt_utils.generate_surrogate_key() where natural keys are composite | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Goal: Specify what “good” looks like—readable, safe, correct, and performant by default | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Intermediate models must select from staging or other intermediate models | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Mart models must select from intermediate or staging models | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Materialize final mart models and heavily used intermediate models as `table` | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| Materialize mart models as table or incremental; do not use view | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Materialize staging and intermediate models as views | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name intermediate models int_<domain>__<purpose> | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name marts as dim_<entity> or fct_<process> | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Name model files `[layer_prefix]_[source_or_concept].sql` | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Name staging models stg_<source>__<entity> | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never use SELECT * | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Place models under models/staging/, models/intermediate/, or models/marts/ | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer incremental_strategy='merge' when supported by the adapter | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a schema.yml entry for every model with a non-empty description | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide descriptions for all documented columns in schema.yml | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Put one logical transformation per model | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Rationale: A flat structure is simpler to navigate; use the `int_` prefix and good naming for grouping intermediate logic | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Rationale: Automated formatting eliminates debates and ensures universal readability | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Rationale: Incremental models add significant logical complexity and are harder to debug | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| Rationale: Marts are the final, user-facing output and should build upon cleanly prepared data | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: Reducing the volume of data being processed early in a query is a key performance optimization | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| Rationale: These standard prefixes create a clear, shared vocabulary for layering | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Rationale: This allows dbt to infer the complete dependency graph, ensuring models are built in the correct order | Safety and Dependencies |  |  |  |  | ✓ |  | 1 |
| Rationale: This breaks logic into named, sequential steps, which is far more readable than nested subqueries | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Rationale: This creates a consistent naming convention, abstracting away ugly source system names | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Rationale: This enforces a clean boundary between raw source data and the dbt project | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: This enforces type safety at the entry point of the DAG | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Rationale: This ensures that code changes do not break existing models or fail data tests | Safety and Dependencies |  |  |  |  | ✓ |  | 1 |
| Rationale: This explains the model's business purpose to future developers and data consumers | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Rationale: This improves query performance for downstream tools and users at the cost of storage and build time | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| Rationale: This is less verbose and less error-prone than re-listing every column name | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Rationale: This is the minimum requirement for asserting the grain and integrity of a model | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Rationale: This isolates source-specific transformations and makes upstream lineage clear | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: This layer is for combining and transforming staged data before final presentation | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: This makes adding or removing columns cleaner in version control | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Rationale: This makes the model's purpose and position in the DAG instantly recognizable from the filename | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Rationale: This makes the project brittle and breaks dbt's ability to manage environments and dependencies | Safety and Dependencies |  |  |  |  | ✓ |  | 1 |
| Rationale: This prevents circular dependencies and ensures the DAG flows in one direction | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Rationale: This prevents confusion and makes finding the code for a given model straightforward | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Rationale: This prevents orphaned records and validates joins between models | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Rationale: This prevents unexpected columns from flowing downstream and makes dependencies explicit | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Rationale: This validates assumptions about source data quality as early as possible | Testing and Documentation |  |  |  |  | ✓ |  | 1 |
| Rationale: Views have no storage cost and always reflect the freshest data, making them ideal for development and simple transformations | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| Remove duplicates upstream; do not use SELECT DISTINCT in marts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: dbt SQL models that define analytics transformations (staging, intermediate, marts) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Set meta.owner on every model | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Staging models must select only from `source()` macros | Layering and Structure |  |  |  |  | ✓ |  | 1 |
| Structure all non-trivial models with Common Table Expressions (CTEs) | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Tag models by layer (staging, intermediate, mart) in config | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use CTEs to structure logic and end with a single final SELECT | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use `GROUP BY ALL` or `GROUP BY 1, 2, 3...` for all non-aggregated columns | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Use `stg_` for staging, `int_` for intermediate, and `dim_`/`fct_` for dimension/fact mart models | File and Model Naming |  |  |  |  | ✓ |  | 1 |
| Use is_incremental() to restrict work to new/changed rows | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use snake_case for all model, CTE, and column names | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use the `incremental` materialization only for very large, event-like tables where a full refresh is too slow or expensive | Performance and Materialization |  |  |  |  | ✓ |  | 1 |
| Use trailing commas before the `FROM` or `GROUP BY` clause | SQL Style and Readability |  |  |  |  | ✓ |  | 1 |
| Use uppercase SQL keywords | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

