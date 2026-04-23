import pytest

from ensemble_rules.errors import MalformedResponseError
from ensemble_rules.parse import split_sections


def test_splits_on_section_markers():
    text = (
        "## Section 1: Reasoning\n"
        "because reasons.\n\n"
        "## Section 2: Rules File\n"
        "- Do the thing.\n\n"
        "## Section 3: Deterministic Validation\n"
        "- Rule: Do the thing.\n"
        "  Signal: source text.\n"
    )
    reasoning, rules_file, deterministic_checks = split_sections(text)
    assert reasoning.startswith("## Section 1")
    assert "because reasons." in reasoning
    assert rules_file.startswith("## Section 2")
    assert "Do the thing." in rules_file
    assert "## Section 3" not in rules_file
    assert deterministic_checks.startswith("## Section 3")
    assert "Signal: source text." in deterministic_checks


def test_raises_when_section_2_marker_missing():
    text = "## Section 1: Reasoning\njust some prose, no second section.\n"
    with pytest.raises(MalformedResponseError, match="Section 2"):
        split_sections(text)


def test_raises_when_section_3_marker_missing():
    text = (
        "## Section 1: Reasoning\n"
        "because.\n"
        "## Section 2: Rules File\n"
        "- Do X.\n"
    )
    with pytest.raises(MalformedResponseError, match="Section 3"):
        split_sections(text)


def test_raises_on_empty_string():
    with pytest.raises(MalformedResponseError):
        split_sections("")
