# ensemble-rules

Exploring what a panel of LLMs agrees on — and disagrees on — when asked to write best-practices rules.

## What this is

A thought experiment. Given a topic (e.g., "shell scripts", "Terraform modules", "Python CLI tools"), poll several LLMs independently with the same prompt, then synthesize the responses into a single rules file that surfaces consensus, minority positions, and genuine disagreements.

The interesting output isn't the final rules file — it's the pattern of agreement and divergence across models.

## Why

- **Triangulation.** Single-model answers reflect that model's training and quirks. Polling a panel and looking at overlap separates "likely true" from "one model's hobbyhorse."
- **Weaker models as signal.** Including smaller/older models on purpose. If a rule shows up only in frontier models, that may be sophistication. If it shows up everywhere, it's probably in the shared training substrate.
- **Disagreement is the point.** Where models diverge is where there's actually something to learn — contested practice, domain-specific trade-offs, or artifacts of different training data.

## Status

Exploratory. No stable interface. Expect churn.

## Install

Python 3.11+, editable install only for v1 (prompt templates are loaded
from the repo, not the installed wheel):

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Prerequisites

The default panel pulls from four providers. Each has its own credential.
You only need keys for the providers you keep in `PANEL`; any model
without valid credentials errors in `raw.json` and the pipeline continues
with the rest.

```sh
export OPENAI_API_KEY=...                       # openai/gpt-5, openai/gpt-4o-mini
export ANTHROPIC_API_KEY=...                    # anthropic/claude-opus-4-7, anthropic/claude-haiku-3-5
export GOOGLE_APPLICATION_CREDENTIALS=/path/... # vertex_ai/gemini-2.5-pro (ADC)
export XAI_API_KEY=...                          # xai/grok-4
```

Edit `src/ensemble_rules/config.py` to swap the roster.

## Run

```sh
ensemble-rules run "shell scripts" \
  --description "Bash/POSIX shell scripts used in production ops tooling"
```

Artifacts land under `runs/<timestamp>-<slug>/`:

- `raw.json` — collected responses, split into `reasoning` and `rules_file`
- `synthesis.md` — synthesizer's consensus / minority / divergence / final rules
- `coverage.md` — deterministic rule × model matrix (`rapidfuzz`-clustered)
- `coverage-llm.md` — LLM-judged matrix (same inputs, different clusterer)
- `meta.json` — per-model token usage and cost, plus synthesis and
  coverage-LLM call usage recorded separately

Exit codes: `0` on success, `2` if every model in the panel errored
(the run directory is still written with `raw.json` and `meta.json` so
you can inspect what broke).
