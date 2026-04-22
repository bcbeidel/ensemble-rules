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
