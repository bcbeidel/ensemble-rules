"""One-shot canary: verify each provider in the panel is reachable with
current credentials. Prints status per provider; does not raise."""
from __future__ import annotations

import os
import sys
import time

import litellm

_PROMPT = "Say 'ok' and nothing else."

_VERTEX_KWARGS = {"vertex_project": os.environ.get("VERTEXAI_PROJECT")}

CANARIES = [
    ("openai-small", "openai/gpt-4o-mini", {}),
    ("openai-frontier", "openai/gpt-5", {}),
    ("anthropic-small", "anthropic/claude-haiku-4-5", {}),
    ("anthropic-frontier", "anthropic/claude-opus-4-7", {}),
    ("vertex_ai-small", "vertex_ai/gemini-2.5-flash", _VERTEX_KWARGS),
    ("vertex_ai-frontier", "vertex_ai/gemini-2.5-pro", _VERTEX_KWARGS),
    ("xai-small", "xai/grok-3-mini", {}),
]


def main() -> int:
    print(f"{'provider':<12}  {'model':<36}  {'status':<8}  {'ms':>5}  detail")
    print("-" * 90)
    any_fail = False
    for label, model, kwargs in CANARIES:
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        started = time.monotonic()
        try:
            resp = litellm.completion(
                model=model,
                messages=[{"role": "user", "content": _PROMPT}],
                max_tokens=10,
                **kwargs,
            )
            elapsed_ms = int((time.monotonic() - started) * 1000)
            content = (resp.choices[0].message.content or "").strip().replace("\n", " ")
            usage = getattr(resp, "usage", None)
            total = getattr(usage, "total_tokens", None) if usage else None
            detail = f"reply={content!r} tokens={total}"
            print(f"{label:<12}  {model:<36}  {'OK':<8}  {elapsed_ms:>5}  {detail}")
        except Exception as exc:
            elapsed_ms = int((time.monotonic() - started) * 1000)
            msg = f"{type(exc).__name__}: {exc}"
            if len(msg) > 200:
                msg = msg[:200] + "..."
            print(f"{label:<12}  {model:<36}  {'FAIL':<8}  {elapsed_ms:>5}  {msg}")
            any_fail = True
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
