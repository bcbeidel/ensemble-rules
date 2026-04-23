---
name: regenerate-artifacts
description: Run every topic-generation make target, commit each regenerated artifact set, and open a PR for review.
---

# Task

Run every topic-generation target in this repo's Makefile, commit the regenerated artifacts, and open a pull request for review.

## Context

- Repo: `ensemble-rules`. Each `make <topic>` target runs an ensemble end-to-end and writes a six-file artifact set to `examples/<topic>/` (`README.md`, `coverage-llm.md`, `coverage.md`, `meta.json`, `raw.json`, `synthesis.md`).
- Each run takes ~60–120s and issues 8 API calls. There are ~20 topic targets; full sweep is ~20–40 minutes of wall clock.
- Current branch: `rerun-with-deterministic-checks`. The working tree already shows deletions of the prior `examples/` contents; new artifacts replace them.
- Recent commit style (from `git log`): `docs(examples): frozen snapshot of <topic> run`.

## Steps

1. Run `make preflight` once to confirm credentials.
2. Parse `make help` to enumerate topic targets. Exclude `help` and `preflight`.
3. For each target, sequentially (never in parallel — each run already fans out to multiple models):
   a. Run `make <target>`.
   b. Verify `examples/<topic>/` exists and contains all six expected files.
   c. Record status (pass / fail), wall-clock time, and any stderr excerpt on failure.
4. After all targets complete, stage and commit the regenerated `examples/` tree. Use one commit per topic, matching the existing message convention.
5. Push the branch and open a PR against `main`.

## Failure handling

- On a single-target failure: record it, continue with remaining targets, list failures in the PR description for manual re-run.
- Do not retry failed targets silently.
- Halt and ask me how to proceed if `preflight` fails, or if three targets fail consecutively (likely a credential or network issue, not a content issue).

## Commit and PR conventions

- Commit message per topic: `docs(examples): frozen snapshot of <topic> run` (mirrors existing history).
- PR title: `docs(examples): regenerate all artifact sets`.
- PR body: table of each target with pass/fail status and wall-clock time; list any failures with short error notes.

## Output

At the end of the run, print:
- A summary table (target, status, duration, artifact path).
- The PR URL.
- Any failures flagged for follow-up.
