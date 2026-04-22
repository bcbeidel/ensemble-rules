# Multi-Model Rules Synthesis System

## Overview

A system for generating authoritative “best practices” rules files by consulting multiple AI models on a given topic (e.g., shell scripts, Python, Terraform), then synthesizing their responses into a single consensus rules file.

**Pattern:** Consensus synthesis of best practices across model perspectives. Conceptually similar to ensemble methods in ML, clinical practice guideline development, and architectural decision record (ADR) aggregation — reducing single-model bias by triangulating across providers.

## Goals


Produce rules files that aren’t biased toward any single model’s opinions or training artifacts.
Capture both the consensus view and notable divergences across models.
Be repeatable: a new rules file for any topic by swapping the subject variable.


## Architecture

Three stages:


**Elicitation** — Send a standardized prompt to N models in parallel.
**Collection** — Persist each model’s response in a structured format.
**Synthesis** — Feed all responses into a synthesizer model to produce the final unified rules file.


```
  ┌──────────────┐
  │   Topic +    │
  │  Template    │
  └──────┬───────┘
         │
   ┌─────┼─────┬─────────┬──────────┐
   ▼     ▼     ▼         ▼          ▼
 GPT-5  Claude Gemini  Grok     (others)
   │     │     │         │          │
   └─────┴─────┴─────────┴──────────┘
                │
                ▼
       ┌─────────────────┐
       │  Collected JSON │
       └────────┬────────┘
                ▼
       ┌─────────────────┐
       │   Synthesizer   │
       │     (model)     │
       └────────┬────────┘
                ▼
       ┌─────────────────┐
       │  Final rules.md │
       └─────────────────┘
```

## Tooling

**Use LiteLLM** as the unified API abstraction. It provides a consistent interface across OpenAI, Anthropic, Google, Cohere, xAI, and others with built-in auth, retries, rate limiting, and cost tracking. Install: `pip install litellm`.

Alternatives considered: Vercel AI SDK (narrower provider coverage), native SDKs per provider (more control, more code). Start with LiteLLM; drop down to native SDKs only if a specific need arises.

## Elicitation Prompt Template

Send this to each model. `{{topic}}` and `{{topic_description}}` are the only variables.

```
You are an expert practitioner and author of technical best practices.

I am building a rules file that defines what "good" looks like for {{topic}}.
This rules file will be used by engineers and AI coding assistants as a
reference, so it must be specific, actionable, and opinionated.

Topic: {{topic}}
Context: {{topic_description}}

Please respond in TWO clearly-separated sections.

## Section 1: Reasoning
Explain the principles, trade-offs, and reasoning behind what makes {{topic}}
good. Cover at minimum: readability, maintainability, correctness, safety,
performance, and common failure modes. Be honest about contested areas where
reasonable practitioners disagree.

## Section 2: Rules File
Produce a concise, scannable rules file as a markdown document. Structure it as:

A short preamble stating scope and intended audience.
Grouped rules under clear headings (e.g., Structure, Error Handling,
    Style, Safety, Performance).

Each rule should be a single imperative sentence ("Do X." / "Don't Y.")
    followed by a one-line rationale.

Mark any rule you consider contested with (contested).


Do not hedge. This is a rules file, not a survey. If you have an opinion, state it.
```

## Synthesis Prompt Template

Run this once after all elicitation responses are collected.

```
You are synthesizing best-practices guidance on {{topic}} from multiple
independent AI models. Your job is to produce a single authoritative rules
file that represents the consensus view while honestly surfacing disagreement.

You will receive N responses, each with a reasoning section and a rules file.

Produce the following output:

## 1. Consensus Rules
Rules that appear (in substance, not wording) across a majority of the inputs.
Write each as a single imperative sentence + one-line rationale. Group by theme.

## 2. Strong Minority Rules
Rules that appear in only one or two inputs but that you assess as well-reasoned
and worth including. Note which model(s) raised them and why you kept them.

## 3. Divergences
Points where models genuinely disagree. For each, summarize the positions,
name who took each side, and give your synthesized recommendation with
reasoning.

## 4. Final Rules File
A clean, standalone markdown rules file combining sections 1 and 2. This is
the artifact engineers and coding assistants will actually use. It should
stand on its own without the preceding analysis.

Inputs follow below, delimited by ===MODEL: <name>=== markers.

{{collected_responses}}
```

## Data Format

Store collected responses as JSON so the synthesis step can be scripted:

```json
{
  "topic": "shell scripts",
  "topic_description": "Bash/POSIX shell scripts used in production ops tooling",
  "timestamp": "2026-04-22T00:00:00Z",
  "responses": [
    {
      "model": "openai/gpt-5",
      "reasoning": "...",
      "rules_file": "..."
    },
    {
      "model": "anthropic/claude-opus-4-7",
      "reasoning": "...",
      "rules_file": "..."
    }
  ]
}
```

## Reference Implementation (Python + LiteLLM)

```python
import json
from datetime import datetime
from litellm import completion

MODELS = [
    "openai/gpt-5",
    "anthropic/claude-opus-4-7",
    "gemini/gemini-2.5-pro",
    "xai/grok-4",
]

SYNTHESIZER = "anthropic/claude-opus-4-7"

ELICITATION_TEMPLATE = """..."""  # paste template from above
SYNTHESIS_TEMPLATE = """..."""    # paste template from above



def elicit(topic: str, topic_description: str) -> dict:
    prompt = ELICITATION_TEMPLATE.replace("{{topic}}", topic) \
                                 .replace("{{topic_description}}", topic_description)
    responses = []
    for model in MODELS:
        try:
            resp = completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
            )
            text = resp.choices[0].message.content
            reasoning, rules_file = split_sections(text)
            responses.append({
                "model": model,
                "reasoning": reasoning,
                "rules_file": rules_file,
            })
        except Exception as e:
            responses.append({"model": model, "error": str(e)})
    return {
        "topic": topic,
        "topic_description": topic_description,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "responses": responses,
    }



def split_sections(text: str) -> tuple[str, str]:
    # Split on the "## Section 2" header; fall back to raw text if not found.
    marker = "## Section 2"
    if marker in text:
        left, right = text.split(marker, 1)
        return left.strip(), (marker + right).strip()
    return text.strip(), ""



def synthesize(collected: dict) -> str:
    blocks = []
    for r in collected["responses"]:
        if "error" in r:
            continue
        blocks.append(f"===MODEL: {r['model']}===\n\n"
                      f"{r['reasoning']}\n\n{r['rules_file']}")
    prompt = SYNTHESIS_TEMPLATE \
        .replace("{{topic}}", collected["topic"]) \
        .replace("{{collected_responses}}", "\n\n".join(blocks))
    resp = completion(
        model=SYNTHESIZER,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content



def run(topic: str, topic_description: str, out_dir: str = "."):
    collected = elicit(topic, topic_description)
    with open(f"{out_dir}/{topic}-raw.json", "w") as f:
        json.dump(collected, f, indent=2)
    final = synthesize(collected)
    with open(f"{out_dir}/{topic}-rules.md", "w") as f:
        f.write(final)



if __name__ == "__main__":
    run("shell-scripts", "Bash/POSIX shell scripts for production ops tooling")
```

## Environment

Set API keys as env vars (LiteLLM picks these up automatically):

```bash
export OPENAI_API_KEY=...
export ANTHROPIC_API_KEY=...
export GEMINI_API_KEY=...
export XAI_API_KEY=...
```

## Extensions to Consider


**Parallel elicitation.** Swap the serial loop for `asyncio` + `litellm.acompletion` once the basic flow works.
**Model weighting.** Not all models deserve equal vote. Consider a weight per model in the synthesis prompt if one consistently outperforms.
**Multi-pass synthesis.** Run synthesis with two different synthesizer models and diff the results as a sanity check.
**Cost/token logging.** LiteLLM exposes usage on each response — log it per run.
**Versioning.** Store raw JSON alongside the final rules file so you can re-synthesize later as models improve.
**Test harness.** Once you have rules files for several topics, dogfood them: feed each back to the models as a system prompt and measure whether outputs improve on a holdout task.