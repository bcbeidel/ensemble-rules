## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Always use ref() and source() macros; never hardcode database/schema/table names. | Safety | ✓ | | ✓ | | ✓ | ✓ | 4 |
| Document every model with a non-empty description in schema.yml. | Documentation | ✓ | ✓ | ✓ | | ✓ | ✓ | 5 |
| Layer models into staging, intermediate, and mart folders/layers. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Name staging models with a stg_ prefix (e.g., stg_<source>__<entity>). | Naming | ✓ | | ✓ | ✓ | ✓ | ✓ | 5 |
| Never use SELECT * in production models. | Style | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Require unique and not_null tests on each model's primary key. | Testing | ✓ | | ✓ | ✓ | ✓ | ✓ | 5 |
| Set unique_key on incremental models. | Incremental | ✓ | ✓ | ✓ | ✓ | | ✓ | 5 |
| Use consistent snake_case naming for models/columns. | Naming | ✓ | ✓ | ✓ | | ✓ | ✓ | 5 |
| Choose materialization deliberately (view vs table vs incremental) rather than defaulting blindly. | Materialization | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Default staging/intermediate to views; promote to table/incremental when justified. | Materialization | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Name mart models with dim_/fct_ (or fact_) prefixes. | Naming | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Name intermediate models with int_ prefix. | Naming | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Structure models as CTEs ending in a single final SELECT. | Style | ✓ | | ✓ | ✓ | ✓ | ✓ | 5 |
| Use is_incremental() (and/or filters) to restrict incremental work to new/changed rows. | Incremental | ✓ | | ✓ | ✓ | | | 3 |
| Add relationships tests on foreign keys (especially in marts). | Testing | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Do not include DDL/DML (CREATE/INSERT/UPDATE/DELETE/MERGE) in model SQL. | Safety | ✓ | | ✓ | | | | 2 |
| Do not use ORDER BY/LIMIT in persistent models. | Safety | ✓ | | | ✓ | | | 2 |
| Avoid nondeterministic functions (now(), current_timestamp, random(), uuid()). | Safety | ✓ | | | | | | 1 |
| Do not use SELECT DISTINCT as a deduplication crutch. | Performance | ✓ | | | ✓ | | | 2 |
| Avoid CROSS JOINs / unintended Cartesian products. | Performance | ✓ | | | | | | 1 |
| Configure partitioning/clustering for large incrementals. | Performance | ✓ | | | | | ✓ | 2 |
| Set an owner (meta.owner) on every model. | Documentation | ✓ | | | ✓ | | | 2 |
| Document every column's description in schema.yml. | Documentation | ✓ | | ✓ | ✓ | | ✓ | 4 |
| Tag models by layer in config. | Governance | ✓ | | | | | | 1 |
| Use dbt_utils.generate_surrogate_key() for composite/surrogate keys. | Naming | ✓ | | ✓ | ✓ | | | 3 |
| Declare model config (materialized, tags, unique_key) at the top of the model. | Style | ✓ | | | | | | 1 |
| Use uppercase SQL keywords. | Style | ✓ | | | | | | 1 |
| Use lowercase SQL keywords. | Style | | | ✓ | | | | 1 |
| Coalesce/cast keys explicitly; avoid implicit casts. | Safety | ✓ | | | ✓ | | | 2 |
| Set on_schema_change appropriately (not 'ignore') for incrementals. | Incremental | ✓ | | | | | | 1 |
| Prefer incremental_strategy='merge' when appropriate. | Incremental | ✓ | | ✓ | | | ✓ | 3 |
| Staging models should be 1:1 with a source table (one source per staging model). | Structure | | | ✓ | | ✓ | | 2 |
| Restrict staging logic to renaming, casting, and trivial coercion (no joins/aggregations). | Structure | | | ✓ | | | | 1 |
| Reference raw data only via source() (only in staging). | Structure | ✓ | | ✓ | ✓ | ✓ | | 4 |
| Marts should not reference other marts. | Structure | | | ✓ | | | | 1 |
| Avoid ephemeral materialization. | Materialization | | | ✓ | | | | 1 |
| Use import CTEs at the top of models, named after referenced model. | Style | | | ✓ | | | | 1 |
| Do not use subqueries where a CTE works; avoid nested subqueries. | Style | | | ✓ | ✓ | ✓ | ✓ | 4 |
| Qualify every column with its table/CTE alias in multi-source queries. | Style | | | ✓ | ✓ | | | 2 |
| Avoid short/meaningless table aliases (t1, single-char). | Style | | | ✓ | | | | 1 |
| Add accepted_values tests on low-cardinality categorical columns. | Testing | | | ✓ | | | | 1 |
| Every new/merged model must have at least one test. | Testing | | ✓ | ✓ | | | ✓ | 3 |
| Declare/document the grain of each model. | Documentation | ✓ | | ✓ | ✓ | | | 3 |
| Document incremental strategy and unique_key for incremental models. | Documentation | | | ✓ | | | | 1 |
| Set materialization in dbt_project.yml by directory rather than per-model. | Materialization | | | ✓ | | | | 1 |
| Use a lookback window on incremental filters to catch late-arriving rows. | Incremental | | | ✓ | ✓ | | | 2 |
| Do not use append incremental strategy on mutable data. | Incremental | | | ✓ | ✓ | | | 2 |
| Ensure full-refresh reproduces the incremental table. | Incremental | | | ✓ | | | | 1 |
| Do not commit secrets, credentials, or PII in model files/YAML. | Safety | | | ✓ | | | | 1 |
| Filter data early (ideally in staging) to reduce downstream volume. | Performance | | | ✓ | | ✓ | | 2 |
| Avoid joining on casted/coerced columns when natural keys exist. | Performance | | | ✓ | | | | 1 |
| Prefer group by on surrogate keys over multi-column natural keys. | Performance | | | ✓ | | | | 1 |
| Suffix boolean columns with is_/has_. | Naming | | | ✓ | ✓ | | | 2 |
| Suffix timestamp columns with _at and date columns with _date. | Naming | | | ✓ | ✓ | | | 2 |
| Distinguish surrogate keys (_sk/_surrogate_key) from natural keys (_id). | Naming | | | ✓ | ✓ | | | 2 |
| Limit each model to a single logical transformation/responsibility. | Structure | ✓ | ✓ | | | | ✓ | 3 |
| Avoid abbreviations in model/column names. | Naming | | | | ✓ | | | 1 |
| Avoid special characters/spaces/reserved words in identifiers. | Naming | ✓ | ✓ | | | | | 2 |
| Name CTEs descriptively (e.g., step__subject pattern). | Style | | | | ✓ | | | 1 |
| Place complex conditional logic in CASE statements, not boolean expressions. | Style | | | | ✓ | | | 1 |
| Use LEFT JOIN as the default; justify INNER/CROSS joins. | Style | | | | ✓ | | | 1 |
| Comment non-trivial join cardinality assumptions. | Style | | | | ✓ | | | 1 |
| Never rely on implicit ordering; use explicit ORDER BY in window functions. | Safety | ✓ | | | ✓ | | | 2 |
| Use COALESCE over nvl/ifnull for portability. | Style | | | | ✓ | | | 1 |
| Avoid SELECT * EXCEPT (...) in warehouses that support it; enumerate columns. | Style | | | | ✓ | | | 1 |
| Use WHERE 1=1 as the first condition for commentable WHERE clauses. | Style | | | | ✓ | | | 1 |
| Tag breaking changes (@breaking) and announce in PR. | Change management | | | | ✓ | | | 1 |
| Do not alter mart grain without versioning/migration. | Change management | | | | ✓ | | | 1 |
| Version models (e.g., _v1 suffix) during migrations. | Change management | | | | ✓ | | | 1 |
| Run dbt test/build (and docs generate) in CI before merge. | Safety | | | | ✓ | ✓ | | 2 |
| Tag PII/sensitive columns via meta fields. | Governance | | | | ✓ | | | 1 |
| Pin a modern dbt required-version in dbt_project.yml. | Governance | | | | ✓ | | | 1 |
| Enable warn_error_threshold to treat warnings as errors. | Governance | | | | ✓ | | | 1 |
| Disable quoting by default; enable only when needed. | Governance | | | | ✓ | | | 1 |
| Use alias only for hiding internal staging models, not public renames. | Governance | | | | ✓ | | | 1 |
| File name must match the model name. | Naming | | | | | ✓ | | 1 |
| Do not reference a higher-layer model from a lower layer (respect DAG direction). | Structure | | | | | ✓ | | 1 |
| Format SQL using a standard formatter (e.g., SQLFluff). | Style | | | | | ✓ | ✓ | 2 |
| Use trailing commas in SELECT lists. | Style | | | | | ✓ | | 1 |
| Use GROUP BY ALL or positional GROUP BY. | Style | | | | | ✓ | | 1 |
| Alias and cast columns explicitly in staging models. | Style | | | | | ✓ | | 1 |
| Add tests on source-configured tables. | Testing | | | | | ✓ | | 1 |
| Enforce line length limit (e.g., 80 chars). | Style | | | | | | ✓ | 1 |
| Indent SQL consistently (e.g., two spaces). | Style | | | | | | ✓ | 1 |
| Add indexes/clustering to materialized tables where appropriate. | Performance | | | | | | ✓ | 1 |
| Avoid selecting unnecessary columns. | Performance | ✓ | | | | | ✓ | 2 |
| Use partitioning for time-based incremental models. | Performance | ✓ | | | | | ✓ | 2 |
| Add data tests for known business-invariants (e.g., positive amounts, enums). | Testing | ✓ | | ✓ | ✓ | | | 3 |
| Avoid full-refresh flag in production. | Safety | | | | | | ✓ | 1 |

## Notes on clustering decisions

- **"Reference raw data via source()" vs "Always use ref()/source() (no hardcoding)"** — I split these into two clusters because several models framed them separately: one is about *which layer touches raw data* (staging-only), the other is about *never hardcoding DB.schema.table identifiers*. gpt-5 and opus addressed both; gemini grouped them together but I credited it under both since its rule explicitly covers both cases.
- **Materialization rules** — I kept three distinct clusters: (a) "choose materialization deliberately" (meta-rule), (b) "default staging/intermediate to views", and (c) "use incremental only when justified". Several models conflate these; I credited a model to the meta cluster if it mentioned choosing by use case even if it also hit (b) or (c).
- **Keyword casing** — uppercase (gpt-5) and lowercase (opus) are opposing rules; kept as separate rows rather than a single "be consistent about casing" cluster, because they make contradictory prescriptions.
- **Nested subqueries vs CTEs** — clustered "don't nest subqueries; use CTEs" with "structure as CTEs" only when the model explicitly called out subquery avoidance. gpt-5's "end with a single final SELECT" is about CTE structure, not subquery avoidance, so I counted it only in the CTE-structure cluster.
- **Grain documentation** — merged "declare grain in YAML description" (opus, haiku) with gpt-5's "header comment containing grain:" since they target the same intent (grain must be explicit), even though the mechanism differs (YAML vs SQL comment).
- **Surrogate key naming vs generation** — "use dbt_utils.generate_surrogate_key()" (gpt-5, opus, haiku) and "distinguish _sk from _id" (opus, haiku) are related but distinct; kept separate because one is about generation mechanism and the other about naming.
- **Testing rules** — I split "PK has unique+not_null", "at least one test per model", "relationships tests on FKs", and "accepted_values on enums" into separate clusters even though they overlap; combining them would hide which specific test types each model endorsed.
- **Business-invariant tests** — gpt-5's "add data tests for known invariants", opus's "accepted_values on categoricals", and haiku's "use dbt_expectations for business rules" were close but not identical; I put accepted_values in its own row and kept a general "invariants/business rules tests" row for the broader framing.
- **"Limit model to single responsibility"** — gpt-4o-mini's "one primary transformation per model" and gpt-5's "one logical transformation per model" and grok's "don't combine multiple business logics" all cluster here; opus's layering rules approach the same idea from a different angle and were not credited.
- **Filter early** — opus and gemini both say this explicitly; gpt-5 does not, despite performance section.
- **Late-arriving data / lookback** — opus and haiku both raise this; counted together even though haiku frames it as `dbt_valid_from/to` and opus as a lookback window.