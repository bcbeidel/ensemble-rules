from ensemble_rules.errors import MalformedResponseError

_SECTION_2_MARKER = "## Section 2"
_SECTION_3_MARKER = "## Section 3"


def split_sections(text: str) -> tuple[str, str, str]:
    if _SECTION_2_MARKER not in text:
        raise MalformedResponseError(
            f"response missing required marker {_SECTION_2_MARKER!r}"
        )
    if _SECTION_3_MARKER not in text:
        raise MalformedResponseError(
            f"response missing required marker {_SECTION_3_MARKER!r}"
        )
    reasoning, rest = text.split(_SECTION_2_MARKER, 1)
    rules_body, checks_body = rest.split(_SECTION_3_MARKER, 1)
    rules_file = (_SECTION_2_MARKER + rules_body).strip()
    deterministic_checks = (_SECTION_3_MARKER + checks_body).strip()
    return reasoning.strip(), rules_file, deterministic_checks
