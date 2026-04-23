## Coverage matrix (LLM-judged)

> Synthesizer bias warning: this matrix reflects one model's judgment
> of which rules are "the same rule" across inputs. A deterministic
> `rapidfuzz`-based companion matrix lives in `coverage.md`; compare
> the two.

| Rule | Theme | openai/gpt-5 | openai/gpt-4o-mini | anthropic/claude-opus-4-7 | anthropic/claude-haiku-4-5 | vertex_ai/gemini-2.5-pro | xai/grok-3-mini | Count |
|---|---|---|---|---|---|---|---|---|
| Do not use the `latest` tag or untagged base images. | Base Image | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Run the container as a non-root user via `USER`. | Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use multi-stage builds to separate build and runtime. | Structure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 6 |
| Use a `.dockerignore` file to exclude unnecessary/sensitive files from the build context. | Performance | ✓ | ✓ | ✓ | ✓ | ✓ |  | 5 |
| Use exec (JSON array) form for CMD/ENTRYPOINT for proper signal handling. | Entrypoint | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Never bake secrets into ARG/ENV/layers; use BuildKit secret mounts. | Safety | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Order instructions (deps before source) to maximize layer caching. | Performance | ✓ |  | ✓ | ✓ | ✓ | ✓ | 5 |
| Pin base images by digest (sha256) for reproducibility. | Base Image | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Pin OS/language package versions during install. | Reproducibility | ✓ |  | ✓ | ✓ |  | ✓ | 4 |
| Combine `apt-get update` and install in a single RUN and clean package caches in the same layer. | Performance | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Prefer COPY over ADD unless you need URL fetch or archive extraction. | Style | ✓ |  | ✓ | ✓ | ✓ |  | 4 |
| Use `--no-install-recommends` with apt-get install. | Performance | ✓ |  | ✓ |  | ✓ | ✓ | 4 |
| Verify checksums/signatures for downloaded artifacts; never `curl \| sh`. | Safety | ✓ |  | ✓ | ✓ |  |  | 3 |
| Use ENTRYPOINT for the main program and CMD for default arguments. | Entrypoint | ✓ |  | ✓ | ✓ |  |  | 3 |
| Define WORKDIR explicitly rather than relying on `cd` or root. | Structure | ✓ |  | ✓ |  |  | ✓ | 3 |
| Use `COPY --chown` instead of a separate RUN chown. | Performance | ✓ |  | ✓ | ✓ |  |  | 3 |
| Declare ARGs explicitly (with proper scope/placement). | Build Args | ✓ |  | ✓ | ✓ |  |  | 3 |
| Provide a HEALTHCHECK for long-running services. | Runtime | ✓ |  | ✓ |  | ✓ |  | 3 |
| Comment non-obvious or complex instructions. | Style |  | ✓ | ✓ |  | ✓ | ✓ | 4 |
| Enable shell error handling (`set -e`/pipefail) in multi-command RUNs. | Error Handling | ✓ |  |  | ✓ |  | ✓ | 3 |
| Add OCI/LABEL metadata (maintainer, source, version, description). | Structure | ✓ |  |  | ✓ |  |  | 2 |
| Name each build stage with `AS <name>`. | Structure |  |  | ✓ | ✓ |  |  | 2 |
| Do not run apt-get upgrade / dist-upgrade in images. | Safety | ✓ |  |  |  |  |  | 1 |
| Use absolute paths for WORKDIR and COPY/ADD destinations. | Structure | ✓ |  |  |  |  |  | 1 |
| Set DEBIAN_FRONTEND=noninteractive per-RUN, not via global ENV. | Safety |  |  | ✓ |  |  |  | 1 |
| Prefer minimal base images (distroless/slim/alpine). | Base Image |  |  | ✓ |  | ✓ |  | 2 |
| Keep base-image family consistent across stages (avoid glibc/musl mismatch). | Base Image |  |  | ✓ |  |  |  | 1 |
| Don't promote ARG values into ENV unless they must persist at runtime. | Build Args |  |  | ✓ |  |  |  | 1 |
| One logical concern per RUN instruction. | Style |  |  | ✓ |  |  |  | 1 |
| Use BuildKit cache mounts for package manager caches. | Performance |  |  | ✓ |  |  |  | 1 |
| Keep LABEL instructions grouped near the top of the final stage. | Style |  |  | ✓ |  |  |  | 1 |
| Use EXPOSE for documentation only; don't rely on it for networking. | Runtime |  |  | ✓ |  | ✓ |  | 2 |
| Pin application dependencies via lock files. | Reproducibility |  |  |  | ✓ |  |  | 1 |
| Create a dedicated app user with no login shell and UID ≥ 1000. | Safety |  |  |  | ✓ |  |  | 1 |
| Remove/disable the package manager in the final production image. | Safety |  |  |  | ✓ |  |  | 1 |
| Do not use ADD with remote URLs (use COPY or explicit curl/wget). | Style |  |  |  | ✓ | ✓ |  | 2 |
| Provide default values for every ARG. | Build Args |  |  |  | ✓ |  |  | 1 |
| Scan built images for CVEs using tools like Trivy/Grype. | Safety |  | ✓ |  | ✓ | ✓ |  | 3 |
| Write entrypoints as external scripts, not complex inline ENTRYPOINT. | Entrypoint |  |  |  | ✓ | ✓ |  | 2 |
| Do not hardcode hostnames, ports, or credentials in ENTRYPOINT/CMD. | Entrypoint |  |  |  | ✓ |  |  | 1 |
| Use lowercase image and tag names. | Style |  |  |  | ✓ |  |  | 1 |
| Avoid using SHELL to change the default shell in the final image. | Style |  |  |  | ✓ |  |  | 1 |
| Don't overload a Dockerfile with multiple unrelated roles. | Structure |  | ✓ |  |  |  |  | 1 |
| Don't silently ignore errors (e.g., `\|\| true`) in RUN steps. | Error Handling |  | ✓ |  |  |  |  | 1 |
| Place a comment header describing purpose/ownership at the top. | Style |  |  |  |  | ✓ |  | 1 |
| Don't expose unnecessary ports or volumes. | Safety |  |  |  |  |  | ✓ | 1 |
| Don't use wildcard COPY; specify exact files. | Performance |  |  |  |  |  | ✓ | 1 |

## Notes on clustering decisions

- **"No `latest` tag" vs "Pin by digest" vs "Pin to specific tag"**: Treated as three related but distinct rules. All models condemned `latest`, but only some escalated to digest pinning, and gemini explicitly mentioned pinning to a specific tag as a fallback — I folded that fallback into the "no latest" cluster rather than creating a third row, since it's the same underlying prohibition.
- **Layer caching / instruction ordering**: gpt-5's "Order COPY instructions to maximize cache hits", opus's "least-volatile to most-volatile" + "manifests before source", haiku's "Order COPY commands", gemini's "Order instructions to optimize layer caching", and grok's similar rule were all merged into one cluster. They differ in phrasing but share the same substance.
- **Secrets handling**: Merged "never bake secrets into ARG/ENV" (gpt-5, opus, gemini, grok) with haiku's "Never embed secrets in ENV/ARG/RUN" into one row. The secret-pattern-scanning aspect is implied by the same rule.
- **apt cache cleanup vs single-RUN apt update+install**: gpt-5, opus, haiku, and gemini all express this as one combined rule ("combine update+install and clean lists in same RUN"). I kept it as a single row rather than splitting into two (combine vs clean), since the models present them inseparably.
- **Comments on complex steps**: gpt-4o-mini, opus ("Comment non-obvious choices"), gemini ("Group related RUN commands with a comment"), and grok all hit this theme. Opus's rule is narrower (document non-obvious choices) but I clustered it here rather than creating a separate "document rationale" row.
- **ENTRYPOINT vs CMD discipline**: Split into two rows — "exec form" (signal handling) and "ENTRYPOINT for program, CMD for args" — because several models raised one without the other (e.g., gemini raised exec-form only; grok raised exec-form only).
- **Image vulnerability scanning**: gpt-4o-mini's "regularly scan images for vulnerabilities", haiku's "Scan the final image for CVEs", and gemini's "Install trivy/grype in a build stage" were clustered together despite differing in where the scan happens (CI vs build stage).
- **Non-root user + dedicated app user**: Kept haiku's more specific "create dedicated user with no login shell and UID ≥ 1000" as a separate row from the general "run as non-root", since it's a stricter, distinct rule only haiku raised.
- **`.dockerignore`**: Merged variants that emphasize existence, contents (excluding `.git`, `node_modules`, secrets), and "keep context small" into one row. Grok didn't explicitly call out `.dockerignore` as a standalone rule (only referenced it implicitly in "don't hardcode sensitive info"), so grok is left blank.
- **ADD with URLs**: Haiku and gemini raised "don't use ADD with remote URLs" specifically; gpt-5 and opus cover the broader "prefer COPY over ADD" rule which technically subsumes this. I kept them as two rows because haiku/gemini's URL-specific rule is narrower than the general COPY-vs-ADD guidance, and a regex matcher would not catch them as the same.
- **grok's "hardcode sensitive info" rule**: Clustered under the secrets-in-ARG/ENV row rather than creating a separate "don't hardcode credentials" row, since it's substantively the same concern.