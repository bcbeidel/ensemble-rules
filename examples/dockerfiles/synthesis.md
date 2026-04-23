# Dockerfile Best Practices: Synthesized Guidance

## 1. Consensus Rules

### Base Image Selection

- **Never use the `latest` tag or an untagged base image.** Floating tags produce non-reproducible builds that can break without warning. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini, and Grok)*

- **Pin base images by digest (`image@sha256:...`) for production builds.** Tags can be overwritten; digests cannot. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, and Gemini; all mark this contested)*

- **Prefer minimal base images (distroless, `-slim`, alpine) for runtime stages.** Smaller images have a smaller attack surface, pull faster, and cost less to store. *(substantively similar across Claude Opus, Claude Haiku, Gemini; noted as contested due to debuggability trade-off)*

### Structure

- **Use multi-stage builds to separate build-time dependencies from the runtime image.** Keeps compilers, SDKs, and intermediate artifacts out of the final image. *(near-identical wording across all five models)*

- **Set `WORKDIR` explicitly rather than using `cd` in `RUN` instructions.** Absolute, predictable paths avoid confusion and cache issues. *(substantively similar across GPT-5, Claude Opus, Grok)*

### Layer Caching and Performance

- **Order instructions from least- to most-frequently-changed to maximize cache hits.** Copy dependency manifests and install dependencies *before* copying application source. *(substantively similar but differently worded across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok)*

- **Combine `apt-get update` and `apt-get install` in a single `RUN` and clean `/var/lib/apt/lists/*` in the same layer.** Prevents stale indexes and keeps layers small. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Pass `--no-install-recommends` to `apt-get install`.** Avoids pulling unnecessary packages. *(near-identical wording across GPT-5, Claude Opus, Gemini)*

- **Include a `.dockerignore` file that excludes VCS directories, build artifacts, and secrets.** Reduces context size and prevents leaking files into the image. *(near-identical wording across all five models)*

### Security

- **Create and switch to a dedicated non-root user with `USER` in the final stage.** Limits the blast radius of a container escape or application compromise. *(near-identical wording across all five models)*

- **Pin package versions when installing OS or language dependencies.** Unpinned installs silently drift between builds. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini, Grok; marked contested by Claude Opus and Grok)*

- **Never bake secrets into the image via `ARG`, `ENV`, or `COPY`; use BuildKit `--mount=type=secret`.** Build-time values persist in image history and are trivially recoverable. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Verify checksums or signatures for downloaded artifacts; avoid `curl | sh`.** Unverified downloads are a common supply-chain vulnerability. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Instruction Choice

- **Prefer `COPY` over `ADD` unless you specifically need ADD's remote-URL or tar-extraction behavior.** ADD's implicit behaviors surprise reviewers and harm reproducibility. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku, Gemini)*

- **Use `COPY --chown=user:group` rather than a separate `RUN chown`.** A trailing chown doubles the layer size; `--chown` sets ownership in one step. *(near-identical wording across GPT-5, Claude Opus, Claude Haiku)*

### Entrypoint and Runtime

- **Use exec form (JSON array) for `CMD` and `ENTRYPOINT`, never shell form.** Shell form wraps the process in `/bin/sh -c`, breaking signal forwarding so the container won't receive `SIGTERM`. *(near-identical wording across all five models)*

- **Use `ENTRYPOINT` for the program and `CMD` for default arguments.** Gives override ergonomics that match user expectations. *(substantively similar across GPT-5, Claude Opus, Claude Haiku, Gemini)*

### Build Arguments

- **Declare every `ARG` used in the Dockerfile explicitly; provide defaults where appropriate.** Undeclared args become empty strings silently. *(substantively similar across Claude Opus, Claude Haiku, Grok)*

- **Declare `ARG` before any `FROM` that references it.** Matches Docker's ARG scoping rules. *(appears in GPT-5, Claude Opus)*

## 2. Strong Minority Rules

- **Enable `set -Eeuo pipefail` for multi-command `RUN` scripts (via `SHELL` or inline).** *(GPT-5, Claude Haiku, Grok)* — Silent partial pipeline failures are a well-documented footgun; this is a high-value rule even though fewer models surfaced it.

- **Declare a `HEALTHCHECK` for long-running services, or document that the orchestrator provides one.** *(GPT-5, Claude Opus, Gemini)* — Orchestrators increasingly rely on this; worth keeping with the caveat that Kubernetes shops often skip it in favor of probes.

- **Add OCI labels (`org.opencontainers.image.title`, `version`/`revision`, `source`).** *(GPT-5, Claude Haiku)* — Traceability and provenance benefits are substantial for audit and supply-chain workflows; low cost to include.

- **Name every stage with `AS <name>` in multi-stage builds.** *(Claude Opus, Claude Haiku)* — Makes `COPY --from=<name>` readable and survives reordering; a small rule with outsized maintainability payoff.

- **Do not promote `ARG` into `ENV` unless the value must persist at runtime.** *(Claude Opus)* — ENV values are visible to every process; this distinction is frequently botched.

- **Set `DEBIAN_FRONTEND=noninteractive` per-RUN, not via global `ENV`.** *(Claude Opus)* — Global ENV leaks into the runtime container and surprises users of `docker exec`. Precise and catchable.

- **Do not run `apt-get upgrade`, `dist-upgrade`, or `apk upgrade` in a Dockerfile.** *(GPT-5)* — Undermines reproducibility and bloats images; base-image refresh should happen upstream. Worth keeping.

- **Use BuildKit cache mounts (`--mount=type=cache`) for package-manager caches.** *(Claude Opus)* — Modern alternative to manual cache-dir gymnastics; speeds up rebuilds without bloating the image.

## 3. Divergences

### Pin base images by digest vs. by tag

- **Positions:** GPT-5, Claude Opus, Claude Haiku, and Gemini recommend digest pinning, but all flag it as contested due to the maintenance burden. Grok recommends immutable tags without emphasizing digest pinning.
- **Synthesis:** Recommend digest pinning for production images, with automation (Dependabot, Renovate, or equivalent) to keep digests refreshed. For development or rapidly iterating internal images, specific version tags are acceptable. This matches the majority position while honoring the legitimate maintenance concern.

### Minimize layers aggressively vs. keep logically distinct RUN steps

- **Positions:** GPT-4o-mini and Grok advise minimizing layer count aggressively. Claude Opus and Claude Haiku explicitly argue against this, saying "one logical concern per RUN" is clearer and that diff/cache granularity suffers when unrelated commands are combined.
- **Synthesis:** Combine *related* commands (e.g., `apt-get update && apt-get install && rm -rf /var/lib/apt/lists/*`) for correctness and size. Do not combine unrelated operations purely to reduce layer count — modern Docker does not penalize layer count meaningfully, and readability matters more.

### `ENTRYPOINT` required vs. `CMD` alone acceptable

- **Positions:** Claude Haiku says final images should always have an `ENTRYPOINT`. Gemini explicitly pushes back: for simple applications, `CMD` alone is fine and over-engineering an entrypoint script is a pitfall. GPT-5 and Claude Opus take the middle position: prefer `ENTRYPOINT` + `CMD` when override ergonomics matter, but don't require it.
- **Synthesis:** Use whichever pattern fits. Requiring `ENTRYPOINT` universally is cargo-culting; the real rules are (a) use exec form and (b) think about how users will pass arguments.

### Tini/dumb-init as PID 1

- **Positions:** Claude Opus recommends it only when the process spawns children or doesn't reap zombies. Others do not mention it.
- **Synthesis:** Follow Claude Opus: use an init only when needed. Most modern language runtimes (Python, Node, Go, JVM) handle signals correctly on their own.

### How strict to be about single-responsibility Dockerfiles

- **Positions:** GPT-4o-mini bans multi-role Dockerfiles. No other model raises this.
- **Synthesis:** This is a weak rule — multi-process images are an anti-pattern for different reasons (orchestration, scaling, logging), and the "single responsibility Dockerfile" framing is imprecise. Drop.

### Uninstall/remove package manager in final image

- **Positions:** Claude Haiku requires it. No other model does.
- **Synthesis:** Distroless and scratch bases achieve this implicitly. For Debian/Alpine-based images, actively purging the package manager is rare in practice and often brittle. Drop from consensus; keep as an aspirational note for hardened production images.

## 4. Notable Omissions

- **Non-root user rule** — appears in all five models. No notable omission.

- **Multi-stage builds** — appears in all five models. No notable omission.

- **Exec form for CMD/ENTRYPOINT** — appears in all five. No notable omission.

- **`.dockerignore`** — appears in all five. No notable omission.

- **Never use `:latest`** — appears in all five. No notable omission.

- **`--no-install-recommends` and apt cache cleanup** — GPT-4o-mini and Grok do not mention these specifically, though they are standard hygiene raised by GPT-5, Claude Opus, Claude Haiku, and Gemini. The omission from GPT-4o-mini and Grok suggests shallower depth on package-manager specifics.

- **Secrets should not go in ARG/ENV** — Grok mentions "don't hardcode sensitive information" and recommends build args, which is partially contradictory. GPT-4o-mini does not address secrets at all. This is a significant omission.

- **Verify checksums on downloads / ban `curl | sh`** — GPT-4o-mini and Grok do not surface this. Given it's a real supply-chain vector, the omission is meaningful.

- **Order COPY to maximize cache (manifests before source)** — GPT-4o-mini does not mention this specifically. A standard practice that shouldn't be missing.

- **COPY vs ADD** — Grok does not raise this. A standard, widely-cited rule.

- **Multi-stage build naming (`AS <name>`)** — GPT-5, GPT-4o-mini, Gemini, and Grok do not mention this. Only Claude Opus and Claude Haiku raised it.

## 5. Shared Deterministic Checks

### Clustered (raised by multiple models)

- **Check** — No `FROM` instruction uses the `:latest` tag or an untagged image reference.
  - **Signal** — Parsed Dockerfile AST (FROM instructions).
  - **Tool candidate** — `hadolint` DL3006 / DL3007.
  - **Raised by** — GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — Substantively identical across models.

- **Check** — Every `FROM` in a production Dockerfile includes a `@sha256:` digest.
  - **Signal** — Raw FROM instruction text; regex `@sha256:[a-f0-9]{64}`.
  - **Tool candidate** — ad-hoc (hadolint doesn't enforce this by default).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — All agree the check should be opt-in or scoped to production; stage-alias references (`FROM builder`) must be excluded.

- **Check** — The final stage contains a `USER` instruction whose effective UID is not 0 or `root`.
  - **Signal** — Parsed AST, instructions of the final stage.
  - **Tool candidate** — `hadolint` DL3002.
  - **Raised by** — GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — Claude Haiku adds an extra requirement (UID ≥ 1000, no login shell); others only require non-root.

- **Check** — `CMD` and `ENTRYPOINT` instructions use JSON array (exec) form.
  - **Signal** — Parsed AST of CMD/ENTRYPOINT.
  - **Tool candidate** — `hadolint` DL3025.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Agreement on substance; no meaningful differences.

- **Check** — Any `RUN` containing `apt-get install` also contains `--no-install-recommends` and a cleanup of `/var/lib/apt/lists` in the same RUN.
  - **Signal** — Tokenized RUN text.
  - **Tool candidate** — `hadolint` DL3009, DL3015.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Agreement on substance.

- **Check** — `apt-get update` and `apt-get install` appear in the same `RUN` instruction (no stale-cache split).
  - **Signal** — Tokenized RUN text.
  - **Tool candidate** — `hadolint` DL3009.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini, Grok.
  - **Variance** — Agreement on substance.

- **Check** — Package installations pin versions (apt `pkg=version`, apk `pkg=version`, pip `==`, npm lockfile).
  - **Signal** — Tokenized RUN text.
  - **Tool candidate** — `hadolint` DL3008 (apt), DL3018 (apk), DL3013 (pip), DL3016 (npm).
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — All flag contested; all recommend suppression mechanism for cases like `ca-certificates`.

- **Check** — No `ADD` instruction where `COPY` would suffice (local, non-archive source).
  - **Signal** — ADD instruction source argument.
  - **Tool candidate** — `hadolint` DL3020.
  - **Raised by** — GPT-5, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Claude Haiku bans any `ADD` with remote URLs specifically; others flag ADD more broadly with a suppression mechanism.

- **Check** — A `.dockerignore` file exists in the build context and excludes at minimum `.git` and common build dirs (`node_modules`, `dist`, `target`, `.venv`).
  - **Signal** — Filesystem presence and content of `.dockerignore`.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5, GPT-4o-mini, Claude Opus, Claude Haiku, Gemini.
  - **Variance** — Minimum pattern set varies; GPT-5 requires `.git`, Claude Haiku requires a longer list.

- **Check** — Each stage has a `WORKDIR` set to an absolute path before any `RUN`/`COPY` using relative paths; no `RUN cd ...` chains.
  - **Signal** — Parsed AST; tokenized RUN text.
  - **Tool candidate** — `hadolint` DL3000 (WORKDIR absolute), DL3003 (no `cd`).
  - **Raised by** — GPT-5, Claude Opus.
  - **Variance** — Agreement on substance.

- **Check** — `ARG`/`ENV` names do not match a regex of known secret tokens (`SECRET`, `TOKEN`, `PASSWORD`, `API_KEY`, `AWS_SECRET`, etc.).
  - **Signal** — ARG and ENV instruction names.
  - **Tool candidate** — ad-hoc; supplement with `detect-secrets` or `trufflehog` on values.
  - **Raised by** — Claude Opus, Claude Haiku, Gemini.
  - **Variance** — All acknowledge high false-positive rate; all treat as a heuristic.

- **Check** — Multi-command `RUN` instructions include `set -e` (and optionally `-u`/`pipefail`); alternatively, a `SHELL` instruction sets `-o pipefail`.
  - **Signal** — Tokenized RUN text and SHELL instruction.
  - **Tool candidate** — `hadolint` DL4006.
  - **Raised by** — GPT-5, Claude Haiku, Grok.
  - **Variance** — GPT-5 scopes the check to RUNs with pipelines; Claude Haiku applies it to any multi-command RUN; Grok is less precise.

### Singleton checks

- **Check** — Every variable reference `${VAR}` in the Dockerfile has a corresponding in-scope `ARG` or `ENV` declaration (or is a documented Docker built-in like `TARGETPLATFORM`).
  - **Signal** — Parsed AST with scope tracking.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — If the Dockerfile has more than one `FROM`, every `FROM` has an `AS <name>` alias.
  - **Signal** — Parsed FROM instructions.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, Claude Haiku.

- **Check** — No `ENV DEBIAN_FRONTEND=noninteractive` at top level (should be scoped to individual `RUN`s or declared as `ARG`).
  - **Signal** — ENV instructions.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — No `RUN` contains `apt-get upgrade`, `dist-upgrade`, `full-upgrade`, or `apk upgrade`.
  - **Signal** — RUN instruction text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — No `RUN` contains the token `sudo`.
  - **Signal** — RUN instruction text.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — No pipeline of the form `(curl|wget) ... | (ba)?sh` appears in any `RUN`.
  - **Signal** — RUN instruction text, regex.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — Final stage contains a `HEALTHCHECK` instruction or a recognized suppression comment.
  - **Signal** — Parsed AST of final stage.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — Final stage contains an OCI LABEL set (`org.opencontainers.image.title`, `version`/`revision`, `source`) with non-empty values.
  - **Signal** — LABEL instructions in final stage.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — GPT-5.

- **Check** — No `COPY` in the final stage sources files matching credential patterns (`*.pem`, `*.key`, `id_rsa*`, `.env`, `.env.*`, `*.pfx`, `*.p12`, `.aws/`, `.npmrc`, `.netrc`).
  - **Signal** — COPY/ADD source paths.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus.

- **Check** — No `COPY` followed by a `RUN chown -R` on the copied target (should use `COPY --chown`).
  - **Signal** — Adjacent COPY and RUN instructions with path overlap.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Opus, GPT-5.

- **Check** — `EXPOSE` port values are within 1–65535.
  - **Signal** — EXPOSE instruction.
  - **Tool candidate** — `hadolint` DL3011.
  - **Raised by** — Claude Opus.

- **Check** — Every `ARG` declaration includes a default value (`ARG NAME=default`).
  - **Signal** — ARG instructions.
  - **Tool candidate** — ad-hoc.
  - **Raised by** — Claude Haiku.

---

## 6. Final Rules File

# Dockerfile Rules

**Scope.** Production Dockerfiles building application or service images on Linux, using Docker/BuildKit.
**Audience.** Engineers and AI coding assistants authoring or reviewing Dockerfiles.

Rules marked *(contested)* reflect trade-offs where reasonable teams disagree; apply judgment to your context.

## Base Images

- **Never use `:latest` or an untagged base image.** Floating tags produce non-reproducible builds.
- **Pin base images by digest (`image@sha256:...`) for production images.** Tags can be overwritten; digests cannot. *(contested — trade-off with maintenance burden; pair with an automated digest updater)*
- **Prefer minimal base images (distroless, `-slim`, alpine, `scratch`) for runtime stages.** Smaller images have a smaller attack surface and pull faster. *(contested — distroless complicates debugging; alpine's musl libc has compatibility caveats)*
- **Use the same base-image family across build and runtime stages where practical.** Glibc/musl mismatches cause silent breakage.

## Structure

- **Use multi-stage builds to separate build-time dependencies from the runtime image.** Keeps compilers, SDKs, and intermediate artifacts out of the final image.
- **Name every stage with `AS <name>`.** Makes `COPY --from=<name>` readable and stable under reordering.
- **Set `WORKDIR` to an absolute path; never use `cd` in `RUN` instructions.** Predictable paths avoid confusion and cache issues.
- **Include a `.dockerignore` that excludes VCS directories (`.git`), build outputs (`node_modules`, `dist`, `target`, `.venv`), and secrets (`.env`, `*.pem`, `*.key`).** Reduces context size and prevents leaking files.
- **Add OCI labels (`org.opencontainers.image.title`, `version` or `revision`, `source`) in the final stage.** Supports provenance and audit.

## Layer Caching and Performance

- **Order instructions from least- to most-volatile.** Copy dependency manifests and install dependencies *before* copying application source.
- **Combine `apt-get update` and `apt-get install` in a single `RUN`; remove `/var/lib/apt/lists/*` in the same layer.** Prevents stale indexes and bloated layers.
- **Pass `--no-install-recommends` to `apt-get install`.** Avoids pulling unnecessary packages.
- **Pin versions of OS and language packages you install (`pkg=version`, `==version`, lockfiles).** Unpinned installs silently drift. *(contested — maintenance burden; allowlist packages like `ca-certificates`)*
- **Combine related commands in a single `RUN`; keep unrelated commands in separate `RUN` instructions.** Related commands share caching semantics; separate concerns stay readable.
- **Use BuildKit cache mounts (`--mount=type=cache`) for package-manager caches.** Speeds up rebuilds without bloating the image.

## Security

- **Create and switch to a non-root user with `USER` before the final `CMD`/`ENTRYPOINT`.** Containers running as root are a privilege-escalation waiting to happen.
- **Never pass secrets via `ARG`, `ENV`, or `COPY` into a shipped stage; use `--mount=type=secret`.** Build-time values persist in image history and are trivially recoverable.
- **Verify checksums or signatures for anything downloaded during the build; never `curl | sh`.** Unverified downloads are a common supply-chain vector.
- **Do not run `apt-get upgrade`/`dist-upgrade` or `apk upgrade` in a Dockerfile.** Produces non-reproducible, bloated images; base-image refresh should happen upstream.
- **Do not use `sudo` in Dockerfiles.** The build user is already effective; `sudo` adds risk and complexity.
- **Set `DEBIAN_FRONTEND=noninteractive` per-`RUN`, not via global `ENV`.** Global ENV leaks into the runtime container.

## Instruction Choice

- **Prefer `COPY` over `ADD` unless you specifically need ADD's remote-URL or tar-extraction behavior.** ADD's implicit behaviors surprise reviewers.
- **Use `COPY --chown=user:group` rather than a separate `RUN chown`.** A trailing chown doubles the layer's size.

## Build Arguments

- **Declare every `ARG` used; provide defaults where appropriate.** Undeclared ARGs silently become empty strings.
- **Declare `ARG` before any `FROM` that references it.** Matches Docker's ARG scoping rules.
- **Do not promote `ARG` into `ENV` unless the value must persist at runtime.** ENVs are visible to every process in the container.

## Entrypoint and Runtime

- **Use exec form (JSON array) for `CMD` and `ENTRYPOINT`, never shell form.** Shell form breaks signal forwarding; your container won't receive `SIGTERM`.
- **Use `ENTRYPOINT` for the program and `CMD` for default arguments when users may override args.** Clean override ergonomics. For simple applications, `CMD` alone is acceptable.
- **Run an init (`tini`, `dumb-init`) as PID 1 only when your process spawns children or doesn't reap zombies.** Otherwise run the app directly.
- **Declare a `HEALTHCHECK` for long-running services, or document that the orchestrator provides one.** Silent unhealthy containers are worse than crashed ones.
- **Use `EXPOSE` for documentation; don't rely on it for networking.** It's metadata, not configuration.

## Error Handling

- **For multi-command `RUN` instructions, enable `set -Eeuo pipefail` (inline or via a `SHELL` instruction).** Prevents silent partial pipeline failures.

## Style

- **Comment non-obvious choices: digest pins, workarounds, version locks.** Future readers will not remember why.
- **One logical concern per `RUN`.** Unrelated commands chained together make diffs and cache invalidation worse.
- **Use lowercase image and tag names.** Consistent with community convention.