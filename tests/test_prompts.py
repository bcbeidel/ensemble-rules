import pytest

from ensemble_rules.prompts import load, render


def test_load_elicitation_template_has_markers():
    text = load("elicitation")
    assert "{{topic}}" in text
    assert "{{topic_description}}" in text
    assert "## Section 2" in text
    assert "## Section 3" in text


def test_load_synthesis_template_has_markers():
    text = load("synthesis")
    assert "{{topic}}" in text
    assert "{{collected_responses}}" in text


def test_load_coverage_llm_template_has_marker():
    text = load("coverage_llm")
    assert "{{collected_responses}}" in text


def test_load_missing_template_raises():
    with pytest.raises(FileNotFoundError):
        load("nonexistent-template")


def test_render_strict_substitution():
    template = "Topic: {{topic}}\nDesc: {{topic_description}}\n"
    rendered = render(template, topic="shell", topic_description="bash scripts")
    assert "Topic: shell" in rendered
    assert "Desc: bash scripts" in rendered
    assert "{{" not in rendered


def test_render_does_not_match_whitespace_variants():
    template = "Strict: {{topic}} Loose: {{ topic }}"
    rendered = render(template, topic="X")
    assert "Strict: X" in rendered
    assert "{{ topic }}" in rendered  # unchanged
