"""Panel roster and synthesizer selection.

Swap the roster here to change which models the pipeline polls.
Diversity of lineage is the point — include weaker/older models
alongside frontier models. A rule that appears only in frontier
models is a different signal than one that appears everywhere.
"""

PANEL: list[str] = [
    "openai/gpt-5",
    "openai/gpt-4o-mini",
    "anthropic/claude-opus-4-7",
    "anthropic/claude-haiku-4-5",
    "vertex_ai/gemini-2.5-pro",
    "xai/grok-3-mini",
]

SYNTHESIZER: str = "anthropic/claude-opus-4-7"
