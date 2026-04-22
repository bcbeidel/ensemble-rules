from ensemble_rules.errors import MalformedResponseError

_SECTION_MARKER = "## Section 2"


def split_sections(text: str) -> tuple[str, str]:
    if _SECTION_MARKER not in text:
        raise MalformedResponseError(
            f"response missing required marker {_SECTION_MARKER!r}"
        )
    left, right = text.split(_SECTION_MARKER, 1)
    return left.strip(), (_SECTION_MARKER + right).strip()
