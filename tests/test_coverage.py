from ensemble_rules.coverage import (
    build_matrix,
    extract_rules,
    render_markdown,
)
from tests.fixtures.fake_responses import sample_run


def test_extract_rules_picks_bullets_with_theme():
    rules_file = (
        "## Section 2: Rules File\n"
        "### Safety\n"
        "- Always quote variables to prevent splitting.\n"
        "- short\n"
        "### Style\n"
        "* Prefer long-form flags like --verbose for clarity.\n"
        "1. Use shellcheck on every script before merging.\n"
        "Prose line with no bullet is ignored.\n"
    )
    rules = extract_rules(rules_file, model="m1")

    assert len(rules) == 3
    assert rules[0].theme == "Safety"
    assert rules[0].text.startswith("Always quote")
    assert rules[1].theme == "Style"
    assert rules[2].text.startswith("Use shellcheck")


def test_extract_rules_drops_short_lines():
    rules_file = "- too short\n- this rule is plenty long enough to count.\n"
    rules = extract_rules(rules_file, model="m1")
    assert len(rules) == 1


def test_build_matrix_clusters_across_models():
    report = build_matrix(sample_run())

    assert report.errored_models == ["xai/grok-4"]
    assert len(report.models) == 3

    quote_cluster = next(
        (c for c in report.clusters if "quote" in c.canonical.lower()),
        None,
    )
    assert quote_cluster is not None, "expected a 'quote variables' cluster"
    assert len(quote_cluster.members) == 3, (
        f"expected all three successful models in the quote cluster, got {list(quote_cluster.members)}"
    )

    verbose_cluster = next(
        (c for c in report.clusters if "long-form" in c.canonical.lower()),
        None,
    )
    assert verbose_cluster is not None
    assert set(verbose_cluster.members) == {"openai/gpt-5", "gemini/gemini-2.5-pro"}

    subshell_cluster = next(
        (c for c in report.clusters if "subshell" in c.canonical.lower()),
        None,
    )
    assert subshell_cluster is not None
    assert set(subshell_cluster.members) == {"anthropic/claude-opus-4-7"}


def test_render_markdown_produces_table_and_sections():
    report = build_matrix(sample_run())
    md = render_markdown(report)

    assert "# Coverage matrix (deterministic)" in md
    assert "| Rule |" in md
    assert "| Theme |" in md
    assert "openai/gpt-5" in md
    assert "anthropic/claude-opus-4-7" in md
    assert "## Wording variance" in md
    assert "## Omissions" in md
    assert "xai/grok-4" in md  # listed as errored


def test_render_markdown_handles_empty_panel():
    from ensemble_rules.coverage import CoverageReport

    empty = CoverageReport(models=[], clusters=[], errored_models=["m1"])
    md = render_markdown(empty)
    assert "No successful responses" in md
