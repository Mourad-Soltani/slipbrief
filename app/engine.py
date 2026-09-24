# SlipBrief scoring engine
# Signature: Mourad.Soltani
from __future__ import annotations

from dataclasses import dataclass, field

from app.rules import BUDGET_MARKERS, DATE_MARKERS, SIGNALS, Signal


@dataclass
class Hit:
    key: str
    category: str
    weight: int
    hint: str
    evidence: str


@dataclass
class Scorecard:
    risk_score: int
    band: str
    hits: list[Hit] = field(default_factory=list)
    word_count: int = 0
    questions: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "risk_score": self.risk_score,
            "band": self.band,
            "word_count": self.word_count,
            "hits": [hit.__dict__ for hit in self.hits],
            "questions": self.questions,
            "author": "Mourad.Soltani",
        }


def _band(score: int) -> str:
    if score >= 45:
        return "high"
    if score >= 22:
        return "medium"
    return "low"


def _contains_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle in text for needle in needles)


def score_brief(raw: str) -> Scorecard:
    text = (raw or "").strip()
    lowered = text.lower()
    words = [w for w in text.split() if w]
    hits: list[Hit] = []

    for signal in SIGNALS:
        if signal.key == "missing_deadline":
            if text and not _contains_any(lowered, DATE_MARKERS):
                hits.append(_hit(signal, "no date or deadline language"))
            continue
        if signal.key == "missing_budget":
            if text and not _contains_any(lowered, BUDGET_MARKERS):
                hits.append(_hit(signal, "no budget or rate language"))
            continue
        for phrase in signal.phrases:
            if phrase in lowered:
                hits.append(_hit(signal, phrase))
                break

    total = min(100, sum(h.weight for h in hits))
    questions = [h.hint for h in hits]
    if len(words) < 40 and text:
        questions.append("Ask the client to write a one-page brief before you quote.")
        total = min(100, total + 8)
        hits.append(
            Hit(
                key="thin_brief",
                category="process",
                weight=8,
                hint="Ask the client to write a one-page brief before you quote.",
                evidence=f"{len(words)} words",
            )
        )
    return Scorecard(
        risk_score=total,
        band=_band(total),
        hits=hits,
        word_count=len(words),
        questions=questions,
    )


def _hit(signal: Signal, evidence: str) -> Hit:
    return Hit(
        key=signal.key,
        category=signal.category,
        weight=signal.weight,
        hint=signal.hint,
        evidence=evidence,
    )
