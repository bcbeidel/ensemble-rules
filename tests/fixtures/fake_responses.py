from datetime import datetime, timezone

from ensemble_rules.schema import CollectedRun, ModelResponse, Usage

_MODEL_A_RULES = """## Section 2: Rules File

### Safety
- Always quote shell variables to prevent word splitting.
- Set errexit with `set -e` to fail fast on errors.

### Style
- Prefer long-form options like `--verbose` over `-v` for readability.
"""

_MODEL_B_RULES = """## Section 2: Rules File

### Safety
- Always quote your shell variables to avoid word splitting.
- Use `set -euo pipefail` at the top of every script to fail fast.

### Performance
- Avoid subshells in hot loops to reduce fork overhead.
"""

_MODEL_C_RULES = """## Section 2: Rules File

### Safety
- Quote your shell variables to prevent word splitting.

### Style
- Prefer long-form options like `--verbose` over `-v` for readability.
"""


def sample_run() -> CollectedRun:
    return CollectedRun(
        topic="shell-scripts",
        topic_description="Bash/POSIX shell scripts",
        timestamp=datetime.now(timezone.utc).isoformat(),
        panel=["openai/gpt-5", "anthropic/claude-opus-4-7", "gemini/gemini-2.5-pro", "xai/grok-4"],
        synthesizer="anthropic/claude-opus-4-7",
        responses=[
            ModelResponse(
                model="openai/gpt-5",
                reasoning="reason a",
                rules_file=_MODEL_A_RULES,
                error=None,
                usage=Usage(total_tokens=100, cost_usd=0.001),
                elapsed_seconds=1.0,
            ),
            ModelResponse(
                model="anthropic/claude-opus-4-7",
                reasoning="reason b",
                rules_file=_MODEL_B_RULES,
                error=None,
                usage=Usage(total_tokens=120, cost_usd=0.002),
                elapsed_seconds=1.5,
            ),
            ModelResponse(
                model="gemini/gemini-2.5-pro",
                reasoning="reason c",
                rules_file=_MODEL_C_RULES,
                error=None,
                usage=Usage(total_tokens=90, cost_usd=0.0005),
                elapsed_seconds=0.9,
            ),
            ModelResponse(
                model="xai/grok-4",
                reasoning="",
                rules_file="",
                error="rate limit",
                usage=Usage(),
                elapsed_seconds=0.0,
            ),
        ],
    )
