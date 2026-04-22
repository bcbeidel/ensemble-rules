from datetime import datetime, timezone

from ensemble_rules.schema import CollectedRun, ModelResponse, Usage

_MODEL_A_RULES = """## Section 2: Rules File

### Safety
- Always quote shell variables to prevent word splitting.
- Set errexit with `set -e` to fail fast on errors.

### Style
- Prefer long-form options like `--verbose` over `-v` for readability.
"""

_MODEL_A_CHECKS = """## Section 3: Deterministic Validation

### Safety
- Rule: Always quote shell variables to prevent word splitting.
  Signal: output of `shellcheck --format=json`.
  Check: shellcheck SC2086.
  Failure mode: `rm $file` triggers SC2086.
  Limitations: intentional word-splitting with IFS is a false positive.
"""

_MODEL_B_RULES = """## Section 2: Rules File

### Safety
- Always quote your shell variables to avoid word splitting.
- Use `set -euo pipefail` at the top of every script to fail fast.

### Performance
- Avoid subshells in hot loops to reduce fork overhead.
"""

_MODEL_B_CHECKS = """## Section 3: Deterministic Validation

### Safety
- Rule: Always quote your shell variables to avoid word splitting.
  Signal: raw source text via shellcheck.
  Check: shellcheck SC2086.
  Failure mode: unquoted `$var` in command position.
  Limitations: noisy on arrays.
"""

_MODEL_C_RULES = """## Section 2: Rules File

### Safety
- Quote your shell variables to prevent word splitting.

### Style
- Prefer long-form options like `--verbose` over `-v` for readability.
"""

_MODEL_C_CHECKS = """## Section 3: Deterministic Validation

No rules in Section 2 admit a reliable deterministic check.
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
                deterministic_checks=_MODEL_A_CHECKS,
                error=None,
                usage=Usage(total_tokens=100, cost_usd=0.001),
                elapsed_seconds=1.0,
            ),
            ModelResponse(
                model="anthropic/claude-opus-4-7",
                reasoning="reason b",
                rules_file=_MODEL_B_RULES,
                deterministic_checks=_MODEL_B_CHECKS,
                error=None,
                usage=Usage(total_tokens=120, cost_usd=0.002),
                elapsed_seconds=1.5,
            ),
            ModelResponse(
                model="gemini/gemini-2.5-pro",
                reasoning="reason c",
                rules_file=_MODEL_C_RULES,
                deterministic_checks=_MODEL_C_CHECKS,
                error=None,
                usage=Usage(total_tokens=90, cost_usd=0.0005),
                elapsed_seconds=0.9,
            ),
            ModelResponse(
                model="xai/grok-4",
                reasoning="",
                rules_file="",
                deterministic_checks="",
                error="rate limit",
                usage=Usage(),
                elapsed_seconds=0.0,
            ),
        ],
    )
