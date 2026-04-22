import pytest

from ensemble_rules.errors import MalformedResponseError
from ensemble_rules.parse import split_sections


def test_splits_on_section_marker():
    text = (
        "## Section 1: Reasoning\n"
        "because reasons.\n\n"
        "## Section 2: Rules File\n"
        "- Do the thing.\n"
    )
    reasoning, rules_file = split_sections(text)
    assert reasoning.startswith("## Section 1")
    assert "because reasons." in reasoning
    assert rules_file.startswith("## Section 2")
    assert "Do the thing." in rules_file


def test_raises_when_marker_missing():
    text = "## Section 1: Reasoning\njust some prose, no second section.\n"
    with pytest.raises(MalformedResponseError):
        split_sections(text)


def test_raises_on_empty_string():
    with pytest.raises(MalformedResponseError):
        split_sections("")
