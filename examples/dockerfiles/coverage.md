# Coverage matrix (deterministic)

Rules are extracted by regex from each model's `rules_file` section (lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered with `rapidfuzz.ratio >= 85` on a normalized headline.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| **(contested) Prefer minimal base images like `distroless`, `alpine`, or `slim-debian`.** // A smaller base image reduces attack surface, storage cost, and pull times | Base Image |  |  |  |  | ✓ |  | 1 |
| **(contested) Use a lightweight `ENTRYPOINT` script to handle container initialization logic.** // This allows for environment-based configuration or waiting for dependencies before starting the main application with `exec "$@"` | Runtime |  |  |  |  | ✓ |  | 1 |
| **Add a `LABEL` with at minimum `maintainer` and `description`.** Documents ownership and purpose; required for audit and SLA tracking | Structure & Clarity |  |  |  | ✓ |  |  | 1 |
| **Assign each build stage a meaningful name (e.g., `builder`, `app`).** Clarifies intent and makes multi-stage logic auditable | Structure & Clarity |  |  |  | ✓ |  |  | 1 |
| **Avoid using `SHELL` to change the shell in the final image.** Can break assumptions about scripts and signal handling; use the base image's shell or document deviation | Style & Hygiene |  |  |  | ✓ |  |  | 1 |
| **Clean up package manager caches in the same `RUN` statement where packages are installed.** (e.g., `apt-get clean`, `apk cache sync --purge`, `yum clean all`) | Style & Hygiene |  |  |  | ✓ |  |  | 1 |
| **Clean up package manager caches within the same `RUN` layer they were created.** // For example, add `&& rm -rf /var/lib/apt/lists/*` to your `apt-get` command to reduce layer size | Build Process |  |  |  |  | ✓ |  | 1 |
| **Combine `RUN apt-get update` with `apt-get install` in the same instruction.** // This prevents a stale cache from causing mismatched or failed package installs | Build Process |  |  |  |  | ✓ |  | 1 |
| **Combine related commands in a single `RUN` using `&&` and line continuations.** One logical step, one layer | Performance |  |  | ✓ |  |  |  | 1 |
| **Comment non-obvious choices (digest pins, workarounds, version locks).** Future-you will not remember why | Style |  |  | ✓ |  |  |  | 1 |
| **Consolidate `apt-get update` with install and cleanup in a single RUN.** Prevents stale package index in intermediate layers and saves space | Optimization |  |  |  | ✓ |  |  | 1 |
| **Copy dependency manifests and install dependencies before copying application source.** Source changes shouldn't invalidate the dependency layer | Structure |  |  | ✓ |  |  |  | 1 |
| **Copy files from build stages with full `--from=stagename --chown=user:group` flags.** Ensures correct ownership and permissions without requiring a second `RUN chmod` | Multi-Stage Build Specifics |  |  |  | ✓ |  |  | 1 |
| **Create a `.dockerignore` file in the build context.** // This prevents leaking secrets, build artifacts, or version control history into the image | Structure & Clarity |  |  |  |  | ✓ |  | 1 |
| **Create a dedicated application user (e.g., `appuser`) with no login shell and a high UID (≥1000).** Prevents collision with system accounts and enforces intent | Security & Hardening |  |  |  | ✓ |  |  | 1 |
| **Create a non-root user and switch to it with the `USER` instruction before the `CMD` or `ENTRYPOINT`.** // Running as root is a major security risk; the principle of least privilege must apply | Security |  |  |  |  | ✓ |  | 1 |
| **Create and switch to a non-root user with `USER` before the final `CMD`/`ENTRYPOINT`.** Containers running as root are a privilege-escalation waiting to happen | Safety |  |  | ✓ |  |  |  | 1 |
| **Declare a `.dockerignore` alongside every Dockerfile.** Prevents accidentally copying `.git`, `node_modules`, secrets, and build artifacts into the context | Structure |  |  | ✓ |  |  |  | 1 |
| **Declare a `HEALTHCHECK` or explicitly document that the orchestrator provides one.** Silent unhealthy containers are worse than crashed ones | Safety |  |  | ✓ |  |  |  | 1 |
| **Declare all build arguments with `ARG` at the top of the Dockerfile (after FROM).** Makes build configuration explicit and discoverable | Build Arguments & Runtime Configuration |  |  |  | ✓ |  |  | 1 |
| **Declare every `ARG` you use; don't rely on implicit globals.** Undeclared args silently become empty strings | Build-Arg Hygiene |  |  | ✓ |  |  |  | 1 |
| **Do not `COPY` private keys, `.env` files, or credentials into any stage that ships.** Secrets in intermediate layers that are discarded are acceptable; secrets in the final image are not | Safety |  |  | ✓ |  |  |  | 1 |
| **Do not hardcode hostnames, ports, or credentials in `ENTRYPOINT` or `CMD`.** Use environment variables or config files; enables reuse across environments | Entrypoint & Command Discipline |  |  |  | ✓ |  |  | 1 |
| **Do not install recommended or suggested packages unless required.** // Use flags like `--no-install-recommends` with `apt-get` to keep the image minimal | Build Process |  |  |  |  | ✓ |  | 1 |
| **Do not pass secrets as plaintext `ARG` or `ENV` variables.** // These values are persisted in the image layers | Security |  |  |  |  | ✓ |  | 1 |
| **Do not use `ADD` with remote URLs; use `COPY` or `RUN curl/wget`.** Opaque URL validation in `ADD` has caused security issues; explicit download is auditable | Security & Hardening |  |  |  | ✓ |  |  | 1 |
| **Do not use `ARG` for runtime configuration; use `ENV` instead.** `ARG` values do not persist in the final image; misleading if the Dockerfile is read without consulting build flags | Build Arguments & Runtime Configuration |  |  |  | ✓ |  |  | 1 |
| **Don't promote `ARG` values into `ENV` unless they must persist at runtime.** ENVs are visible to every process in the container | Build-Arg Hygiene |  |  | ✓ |  |  |  | 1 |
| **Exclude sensitive files and build artifacts via `.dockerignore`.** Keeps build context small; prevents accidental inclusion of `.git`, `.env`, `node_modules`, or compiled binaries | Security & Hardening |  |  |  | ✓ |  |  | 1 |
| **Expose only the necessary ports using the `EXPOSE` instruction.** // This serves as documentation for the user and can be used by automation | Runtime |  |  |  |  | ✓ |  | 1 |
| **Expose ports with `EXPOSE` for documentation; do not rely on it for networking.** It's metadata, not configuration | Entrypoint Discipline |  |  | ✓ |  |  |  | 1 |
| **Group related `RUN` commands with a comment.** // This explains the purpose of a set of shell commands, aiding maintainability | Structure & Clarity |  |  |  |  | ✓ |  | 1 |
| **If digests are not feasible, pin to a specific version tag (e.g., `1.16.8-alpine`).** // Do not use floating tags like `latest`, `stable`, or major versions like `1.16` | Base Image |  |  |  |  | ✓ |  | 1 |
| **Implement a `HEALTHCHECK` instruction for long-running services.** // This gives the Docker daemon and orchestrators like Kubernetes a reliable way to determine if the container is functioning correctly | Runtime |  |  |  |  | ✓ |  | 1 |
| **Install a static analysis tool like `trivy` or `grype` in a build stage to scan for vulnerabilities.** // This fails the build if known high-severity vulnerabilities are found in the base image or dependencies | Security |  |  |  |  | ✓ |  | 1 |
| **Keep RUN instructions focused and commented if complex.** Each `RUN` is a layer; bundling unrelated operations obscures intent | Style & Hygiene |  |  |  | ✓ |  |  | 1 |
| **Keep the build context small via `.dockerignore`.** Large contexts slow every build and leak files into layers | Performance |  |  | ✓ |  |  |  | 1 |
| **Name every stage with `AS <name>`.** Makes `COPY --from=<name>` readable and stable under reordering | Structure |  |  | ✓ |  |  |  | 1 |
| **Never embed secrets (API keys, tokens, credentials) in `ENV`, `ARG`, or `RUN` statements.** Layer history is immutable and readable; use build secrets (Docker BuildKit) or external secret management | Security & Hardening |  |  |  | ✓ |  |  | 1 |
| **Never pass secrets via `ARG` or `ENV`.** Both are recoverable from image history or the running container; use `--mount=type=secret` | Safety |  |  | ✓ |  |  |  | 1 |
| **Never use `:latest`.** It is not a version | Base Images |  |  | ✓ |  |  |  | 1 |
| **One logical concern per `RUN`.** Unrelated commands chained together make diffs and cache invalidation worse | Style |  |  | ✓ |  |  |  | 1 |
| **Order COPY commands so that stable files (e.g., dependency manifests) come before volatile files (e.g., source code).** Maximizes cache hits during development iteration | Optimization |  |  |  | ✓ |  |  | 1 |
| **Order Dockerfile instructions to maximize cache hit on iterative builds.** Place `COPY` of source code and `RUN` application-specific commands near the end, after system dependencies and package manager setup | Structure & Clarity |  |  |  | ✓ |  |  | 1 |
| **Order `LABEL` instructions together near the top of the final stage.** Easy to find, easy to audit | Style |  |  | ✓ |  |  |  | 1 |
| **Order instructions to optimize layer caching.** // Place instructions that change infrequently (e.g., installing packages) before ones that change frequently (e.g., copying source code) | Build Process |  |  |  |  | ✓ |  | 1 |
| **Pass `--no-install-recommends` to `apt-get install` and clean `/var/lib/apt/lists/*` in the same `RUN`.** Reduces size and prevents stale package indexes | Safety |  |  | ✓ |  |  |  | 1 |
| **Pin application dependencies in lock files (e.g., `package-lock.json`, `Pipfile.lock`, `go.sum`).** Ensures repeatable builds across time and machines | Error Handling & Correctness |  |  |  | ✓ |  |  | 1 |
| **Pin base image by digest (SHA-256) in production Dockerfiles.** Guarantees byte-for-byte reproducibility even if a tag is retagged or overwritten | Structure & Clarity |  |  |  | ✓ |  |  | 1 |
| **Pin base images by digest (`image@sha256:...`), not by tag alone.** Tags mutate; digests don't | Base Images |  |  | ✓ |  |  |  | 1 |
| **Pin base images to a specific and immutable digest (`image:tag@sha256:...`).** // This is the only way to guarantee a truly reproducible build; a tag can be overwritten | Base Image |  |  |  |  | ✓ |  | 1 |
| **Pin versions of OS packages and language dependencies you install.** Unpinned installs make builds non-reproducible | Safety |  |  | ✓ |  |  |  | 1 |
| **Place `FROM` as the first instruction, except for global `ARG` directives.** Makes the base image immediately visible and allows multi-stage inheritance | Structure & Clarity |  |  |  | ✓ |  |  | 1 |
| **Place a comment header at the top of the file explaining its purpose and ownership.** // A Dockerfile without context is a liability for the next engineer | Structure & Clarity |  |  |  |  | ✓ |  | 1 |
| **Place instructions from least-volatile to most-volatile.** Maximizes layer cache hits | Structure |  |  | ✓ |  |  |  | 1 |
| **Prefer `COPY` over `ADD` for local files and directories.** // `COPY` is more transparent and predictable; `ADD` has complex features (URL/archive extraction) that harm reproducibility | Structure & Clarity |  |  |  |  | ✓ |  | 1 |
| **Prefer `ENTRYPOINT` over `CMD` for the main application.** Clarifies that the container is meant to run a specific program; prevents accidental override | Entrypoint & Command Discipline |  |  |  | ✓ |  |  | 1 |
| **Prefer minimal bases (`-slim`, distroless, `scratch`) for runtime stages.** Smaller attack surface, faster pulls | Base Images |  |  | ✓ |  |  |  | 1 |
| **Provide a default value for every `ARG` that might be overridden at build time.** Ensures builds do not fail if `--build-arg` is omitted | Build Arguments & Runtime Configuration |  |  |  | ✓ |  |  | 1 |
| **Remove or disable the package manager in the final image (production only).** Reduces attack surface; prevents `apt-get install` inside a running container | Security & Hardening |  |  |  | ✓ |  |  | 1 |
| **Run a proper init (`tini`, `dumb-init`) as PID 1 when your process spawns children or doesn't reap zombies.** Otherwise use your app directly | Entrypoint Discipline |  |  | ✓ |  |  |  | 1 |
| **Run the final container as a non-root user.** Limits blast radius of container escape, privilege escalation, or malware | Security & Hardening |  |  |  | ✓ |  |  | 1 |
| **Scan the final image for CVEs before pushing to a registry.** Use Trivy, Grype, or equivalent; establish a policy for remediation | Security & Hardening |  |  |  | ✓ |  |  | 1 |
| **Scope `ARG` to the stage that needs it.** ARGs declared before `FROM` have different scoping rules and leak surprises | Build-Arg Hygiene |  |  | ✓ |  |  |  | 1 |
| **Set `DEBIAN_FRONTEND=noninteractive` per-RUN, not via global `ENV`.** Global ENV leaks into the runtime container | Safety |  |  | ✓ |  |  |  | 1 |
| **Set `WORKDIR` explicitly; never rely on `/`.** Avoids cluttering the root filesystem and makes relative paths predictable | Structure |  |  | ✓ |  |  |  | 1 |
| **Use BuildKit cache mounts (`--mount=type=cache`) for package-manager caches.** Faster rebuilds without bloating the image | Performance |  |  | ✓ |  |  |  | 1 |
| **Use `.dockerignore` to exclude `.git`, `.gitignore`, test directories, documentation, and temporary files from the build context.** Reduces context size and speeds up builds | Optimization |  |  |  | ✓ |  |  | 1 |
| **Use `ARG` to parameterize base image tag or version.** (contested) Allows `docker build --build-arg BASE_TAG=3.11 .` to target different runtime versions without editing the Dockerfile | Build Arguments & Runtime Configuration |  |  |  | ✓ |  |  | 1 |
| **Use `COPY --chown=user:group` rather than a separate `RUN chown`.** A trailing chown doubles the copied layer's size | Performance |  |  | ✓ |  |  |  | 1 |
| **Use `COPY`, not `ADD`, unless you need ADD's tar extraction or remote-URL fetch.** ADD's implicit behaviors cause surprises | Structure |  |  | ✓ |  |  |  | 1 |
| **Use `ENTRYPOINT` for the program and `CMD` for default arguments when users may override args.** Clean override ergonomics | Entrypoint Discipline |  |  | ✓ |  |  |  | 1 |
| **Use `ENTRYPOINT` with `CMD` for arguments.** Allows `docker run image arg1 arg2` to pass arguments to the entrypoint without overriding it | Entrypoint & Command Discipline |  |  |  | ✓ |  |  | 1 |
| **Use `set -e` (exit on error) in all RUN scripts with multiple commands.** Prevents silent partial failures in chained shell commands | Error Handling & Correctness |  |  |  | ✓ |  |  | 1 |
| **Use `set -u` (error on undefined variable) in RUN scripts.** Catches typos and missing build arguments early | Error Handling & Correctness |  |  |  | ✓ |  |  | 1 |
| **Use a `.dockerignore` file in the same directory as the Dockerfile.** Minimizes build context; improves build speed and layer inspection | Style & Hygiene |  |  |  | ✓ |  |  | 1 |
| **Use a descriptive stage name and copy only necessary artifacts to the final stage.** Prevents accidental leakage of build dependencies and documentation into the runtime image | Multi-Stage Build Specifics |  |  |  | ✓ |  |  | 1 |
| **Use exec form (`["bin", "arg"]`) for `CMD` and `ENTRYPOINT`, never shell form.** Shell form breaks signal handling; your process won't receive `SIGTERM` | Entrypoint Discipline |  |  | ✓ |  |  |  | 1 |
| **Use explicit package versions in `apt-get install`, `apk add`, `yum install`, or equivalent.** Non-pinned package specs silently pull new versions on rebuild, breaking reproducibility | Error Handling & Correctness |  |  |  | ✓ |  |  | 1 |
| **Use explicit, non-`latest` base image tags.** Prevents silent breakage when upstream publishes a new release | Structure & Clarity |  |  |  | ✓ |  |  | 1 |
| **Use lowercase image names and tag names.** Docker image names are case-insensitive but convention is lowercase; reduces confusion | Style & Hygiene |  |  |  | ✓ |  |  | 1 |
| **Use multi-stage builds for any image larger than 200 MB or that requires a compiler.** Separates build dependencies from runtime; dramatically reduces final size | Structure & Clarity |  |  |  | ✓ |  |  | 1 |
| **Use multi-stage builds for any image that compiles code or installs build-only tooling.** Keeps build dependencies out of the runtime image | Structure |  |  | ✓ |  |  |  | 1 |
| **Use multi-stage builds for applications that require a build step.** // This keeps the final image lean by excluding compilers, SDKs, and build-time dependencies | Build Process |  |  |  |  | ✓ |  | 1 |
| **Use the `--chown` flag in `COPY` instructions to set ownership on added files.** // This prevents files from being owned by root, which could be a security risk if the non-root user needs to write to them | Security |  |  |  |  | ✓ |  | 1 |
| **Use the `exec` form (JSON array) for `CMD` and `ENTRYPOINT` instructions.** // This avoids a shell wrapper, ensuring signals are passed correctly to your application (e.g., `SIGTERM` for graceful shutdown) | Runtime |  |  |  |  | ✓ |  | 1 |
| **Use the same base-image family across stages where practical.** Glibc/musl mismatches between build and runtime cause silent breakage | Base Images |  |  | ✓ |  |  |  | 1 |
| **Verify checksums for anything downloaded during build.** `curl \| sh` with no verification is a supply-chain hole | Safety |  |  | ✓ |  |  |  | 1 |
| **Verify checksums or GPG signatures for downloaded artifacts.** Guards against man-in-the-middle and supply-chain attack; demonstrates due diligence | Error Handling & Correctness |  |  |  | ✓ |  |  | 1 |
| **Write entrypoints as a shell script or go binary, not inline in `ENTRYPOINT`.** Improves readability, allows conditional logic, and enables cleaner signal handling | Entrypoint & Command Discipline |  |  |  | ✓ |  |  | 1 |
| Add OCI labels (org.opencontainers.image.*) for title, version or revision, and source | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Audience: Engineers and AI coding assistants authoring or reviewing Dockerfiles in application repositories and base-image repos | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Avoid ADD from remote URLs; prefetch into the build context or verify strongly if you must | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Clean package caches (apk/apt) in the same RUN as install | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Combine apt-get update and apt-get install in a single RUN and remove /var/lib/apt/lists | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Create a dedicated non-root user and switch to it in the final stage | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Declare ARG before any FROM if it is referenced in that FROM | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Define WORKDIR and avoid using cd in RUN instructions | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do add explicit error handling in RUN commands, such as using `set -e` in shells, to fail builds on script errors and prevent faulty images | Error Handling |  |  |  |  |  | ✓ | 1 |
| Do comment on complex and non-obvious steps | Style |  | ✓ |  |  |  |  | 1 |
| Do configure containers to run as a non-root user via the USER instruction, minimizing security risks from privilege escalation | Safety |  |  |  |  |  | ✓ | 1 |
| Do end the Dockerfile with a clear entrypoint or command definition, ensuring the container starts predictably on run | Style |  |  |  |  |  | ✓ | 1 |
| Do include comments for complex instructions to explain their purpose, enhancing readability and team collaboration | Style |  |  |  |  |  | ✓ | 1 |
| Do incorporate security hardening tools like `apk add --no-cache` for Alpine-based images to avoid cached vulnerabilities | Safety |  |  |  |  |  | ✓ | 1 |
| Do leverage build arguments for configurable elements like versions, but limit them to essential uses to prevent overuse | Performance |  |  |  |  |  | ✓ | 1 |
| Do minimize the number of layers | Performance |  | ✓ |  |  |  |  | 1 |
| Do minimize the number of layers by combining related RUN instructions (e.g., using && to chain commands), optimizing build speed and storage | Performance |  |  |  |  |  | ✓ | 1 |
| Do not bake secrets into layers via ARG, ENV, or COPY; use BuildKit secrets and runtime mounts | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not run apt-get upgrade/dist-upgrade/full-upgrade or apk upgrade | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do not use sudo in Dockerfiles | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Do order Dockerfile instructions to maximize layer caching, such as placing stable commands (e.g., package installations) before variable ones (e.g., COPY of source code) | Structure |  |  |  |  |  | ✓ | 1 |
| Do regularly scan images for vulnerabilities | Safety |  | ✓ |  |  |  |  | 1 |
| Do run containers as a non-root user | Safety |  | ✓ |  |  |  |  | 1 |
| Do select official base images with specific, immutable tags (e.g., `FROM node:14-alpine`), ensuring reproducibility and trusted sources | Safety |  |  |  |  |  | ✓ | 1 |
| Do use `ENTRYPOINT` for image execution and `CMD` for default arguments | Error Handling |  | ✓ |  |  |  |  | 1 |
| Do use multi-stage builds | Structure |  | ✓ |  |  |  |  | 1 |
| Do use multi-stage builds to separate build and runtime environments, reducing image size and improving isolation | Structure |  |  |  |  |  | ✓ | 1 |
| Don't copy unnecessary files into the image | Performance |  | ✓ |  |  |  |  | 1 |
| Don't expose unnecessary ports or volumes in the Dockerfile; define them only if required for the application's functionality | Safety |  |  |  |  |  | ✓ | 1 |
| Don't hardcode sensitive information like API keys; use build arguments or environment variables instead for better security and flexibility | Style |  |  |  |  |  | ✓ | 1 |
| Don't ignore the output of commands during the build process | Error Handling |  | ✓ |  |  |  |  | 1 |
| Don't include unnecessary instructions or files in the final image; every layer should serve a clear purpose to maintain a lean structure | Structure |  |  |  |  |  | ✓ | 1 |
| Don't leave large, uncommented sections of code | Style |  | ✓ |  |  |  |  | 1 |
| Don't overload a single Dockerfile with too many roles | Structure |  | ✓ |  |  |  |  | 1 |
| Don't rely on implicit defaults for build contexts; always specify WORKDIR to avoid path-related failures in multi-stage builds | Error Handling |  |  |  |  |  | ✓ | 1 |
| Don't use `latest` tags for base images | Safety |  | ✓ |  |  |  |  | 1 |
| Don't use wildcard patterns in COPY instructions; specify exact files to enable efficient caching and avoid unnecessary rebuilds | Performance |  |  |  |  |  | ✓ | 1 |
| Enable pipefail and exit-on-error for shell invocations (via SHELL or set -Eeuo pipefail in RUN) | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| If you need a wrapper script, ensure it execs "$@" and propagates signals | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Include a .dockerignore that excludes VCS directories, build outputs, and secrets | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Never use latest or an untagged base image | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Order COPY instructions to maximize cache hits by copying dependency manifests before application sources | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin package versions in apt/apk/pip installs | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Pin the base image by digest in every FROM line | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer COPY to ADD except for remote URLs or automatic archive extraction | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Prefer digest-pinned language/runtime base images for final stages | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Provide a HEALTHCHECK for long-running services | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Scope: Dockerfiles for Linux containers built with Docker/BuildKit, targeting reproducible, secure, and efficient images | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use --no-install-recommends with apt-get install | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use COPY --chown to set file ownership instead of chown in a separate RUN | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use ENTRYPOINT for the main process and CMD only for default arguments | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use absolute paths for WORKDIR and COPY/ADD destinations | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use build args only for safe, cache-stable toggles; prefer explicit files for content changes | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use multi-stage builds to separate build-time dependencies from the final runtime image | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Use the exec (JSON array) form for ENTRYPOINT and CMD | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |
| Verify downloaded artifacts with checksums or signatures, and never curl \| bash | Section 2: Rules File | ✓ |  |  |  |  |  | 1 |

## Wording variance

For each cluster, the average pairwise similarity of verbatim phrasings. >=95 suggests shared training source; <85 suggests genuine convergence.


## Omissions

Rules that appear in a majority of models but are absent from at least one. The absence is sometimes the signal.

_No majority rules with omissions._

