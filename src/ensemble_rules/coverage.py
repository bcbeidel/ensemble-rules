from __future__ import annotations

import re
from dataclasses import dataclass, field

from rapidfuzz import fuzz

from ensemble_rules.schema import CollectedRun

_BULLET_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(.+)$")
_HEADING_RE = re.compile(r"^\s*#{1,6}\s+(.+?)\s*$")
_MIN_RULE_CHARS = 20
_CLUSTER_THRESHOLD = 85
_WORDING_IDENTICAL = 95
_WORDING_CONVERGENT = 85

_STOPWORDS = frozenset(
    {
        "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "at",
        "for", "with", "by", "from", "as", "is", "are", "be", "been", "being",
        "do", "does", "did", "don", "t", "not", "no",
        "your", "you", "it", "its", "this", "that", "these", "those",
        "should", "shouldn", "must", "use", "using",
    }
)


@dataclass
class ExtractedRule:
    text: str
    theme: str
    model: str


@dataclass
class RuleCluster:
    canonical: str
    theme: str
    members: dict[str, str] = field(default_factory=dict)


@dataclass
class CoverageReport:
    models: list[str]
    clusters: list[RuleCluster]
    errored_models: list[str]


def extract_rules(rules_file: str, model: str) -> list[ExtractedRule]:
    rules: list[ExtractedRule] = []
    current_heading = ""
    for line in rules_file.splitlines():
        heading_match = _HEADING_RE.match(line)
        if heading_match:
            current_heading = heading_match.group(1).strip()
            continue
        bullet_match = _BULLET_RE.match(line)
        if not bullet_match:
            continue
        body = bullet_match.group(1).strip()
        if len(body) < _MIN_RULE_CHARS:
            continue
        rules.append(ExtractedRule(text=body, theme=current_heading, model=model))
    return rules


def build_matrix(run: CollectedRun) -> CoverageReport:
    successful = [r for r in run.responses if r.error is None]
    errored = [r.model for r in run.responses if r.error is not None]
    models = [r.model for r in successful]

    all_rules: list[ExtractedRule] = []
    for resp in successful:
        all_rules.extend(extract_rules(resp.rules_file, resp.model))

    clusters = _cluster_rules(all_rules)
    return CoverageReport(models=models, clusters=clusters, errored_models=errored)


def render_markdown(report: CoverageReport) -> str:
    out: list[str] = ["# Coverage matrix (deterministic)", ""]
    out.append(
        "Rules are extracted by regex from each model's `rules_file` section "
        "(lines starting with `-`, `*`, or `N.`; minimum 20 chars) and clustered "
        f"with `rapidfuzz.ratio >= {_CLUSTER_THRESHOLD}` on a normalized headline."
    )
    out.append("")

    if report.errored_models:
        out.append(f"**Errored models** (excluded from matrix): {', '.join(report.errored_models)}")
        out.append("")

    if not report.models:
        out.append("_No successful responses — matrix is empty._")
        return "\n".join(out) + "\n"

    header = ["Rule", "Theme", *report.models, "Count"]
    rows = ["| " + " | ".join(header) + " |"]
    rows.append("|" + "|".join(["---"] * len(header)) + "|")

    sorted_clusters = sorted(
        report.clusters,
        key=lambda c: (-len(c.members), c.canonical),
    )
    for cluster in sorted_clusters:
        checks = ["✓" if m in cluster.members else "" for m in report.models]
        row = [_escape_cell(cluster.canonical), _escape_cell(cluster.theme), *checks, str(len(cluster.members))]
        rows.append("| " + " | ".join(row) + " |")
    out.extend(rows)
    out.append("")

    out.append("## Wording variance")
    out.append("")
    out.append(
        "For each cluster, the average pairwise similarity of verbatim phrasings. "
        f">={_WORDING_IDENTICAL} suggests shared training source; "
        f"<{_WORDING_CONVERGENT} suggests genuine convergence."
    )
    out.append("")
    for cluster in sorted_clusters:
        if len(cluster.members) < 2:
            continue
        score = _wording_score(list(cluster.members.values()))
        label = _wording_label(score)
        out.append(f"- **{cluster.canonical}** — avg similarity {score:.0f} ({label})")
        for model, text in cluster.members.items():
            out.append(f"  - `{model}`: {text}")
    out.append("")

    out.append("## Omissions")
    out.append("")
    out.append(
        "Rules that appear in a majority of models but are absent from at least "
        "one. The absence is sometimes the signal."
    )
    out.append("")
    majority = (len(report.models) // 2) + 1
    had_any = False
    for cluster in sorted_clusters:
        if len(cluster.members) < majority:
            continue
        missing = [m for m in report.models if m not in cluster.members]
        if not missing:
            continue
        had_any = True
        out.append(f"- **{cluster.canonical}** — missing from: {', '.join(missing)}")
    if not had_any:
        out.append("_No majority rules with omissions._")
    out.append("")

    return "\n".join(out) + "\n"


def _cluster_rules(rules: list[ExtractedRule]) -> list[RuleCluster]:
    clusters: list[RuleCluster] = []
    normalized_canonicals: list[str] = []
    for rule in rules:
        norm = _normalize(rule.text)
        if not norm:
            continue
        matched_idx: int | None = None
        best_score = 0
        for i, canon_norm in enumerate(normalized_canonicals):
            score = fuzz.ratio(norm, canon_norm)
            if score >= _CLUSTER_THRESHOLD and score > best_score:
                matched_idx = i
                best_score = score
        if matched_idx is None:
            clusters.append(
                RuleCluster(
                    canonical=_first_sentence(rule.text),
                    theme=rule.theme,
                    members={rule.model: rule.text},
                )
            )
            normalized_canonicals.append(norm)
        else:
            cluster = clusters[matched_idx]
            cluster.members.setdefault(rule.model, rule.text)
    return clusters


def _normalize(text: str) -> str:
    sentence = _first_sentence(text).lower()
    stripped = re.sub(r"[^a-z0-9\s]+", " ", sentence)
    tokens = [t for t in stripped.split() if t and t not in _STOPWORDS]
    return " ".join(tokens)


def _first_sentence(text: str) -> str:
    for sep in (". ", "! ", "? "):
        if sep in text:
            return text.split(sep, 1)[0].rstrip(" .!?")
    return text.rstrip(" .!?")


def _wording_score(texts: list[str]) -> float:
    if len(texts) < 2:
        return 100.0
    total = 0.0
    pairs = 0
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            total += fuzz.ratio(texts[i], texts[j])
            pairs += 1
    return total / pairs


def _wording_label(score: float) -> str:
    if score >= _WORDING_IDENTICAL:
        return "near-identical wording — possible shared training source"
    if score >= _WORDING_CONVERGENT:
        return "similar wording"
    return "substantively similar but differently worded — genuine convergence"


def _escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")
