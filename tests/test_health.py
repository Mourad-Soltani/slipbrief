# SlipBrief health tests
# Signature: Mourad.Soltani
from fastapi.testclient import TestClient

from app.engine import score_brief
from app.main import app

client = TestClient(app)


def test_health_ok():
    res = client.get("/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "ok"
    assert body["author"] == "Mourad.Soltani"


def test_score_flags_unbounded_and_pay_later():
    brief = (
        "Need a new site with unlimited revisions and other tasks as needed. "
        "Pay after launch. The team will review. ASAP."
    )
    res = client.post("/v1/score", json={"text": brief})
    assert res.status_code == 200
    data = res.json()
    keys = {h["key"] for h in data["hits"]}
    assert "unbounded_revisions" in keys
    assert "pay_later" in keys
    assert data["band"] in {"medium", "high"}
    assert data["risk_score"] >= 22


def test_clean_brief_is_low_risk():
    brief = (
        "Build a 5-page marketing site for Acme. Budget $4,000 USD fixed. "
        "Deadline 2026-11-01. Two revision rounds. I am the only approver. "
        "Copy and brand assets will be delivered on 2026-10-01."
    )
    card = score_brief(brief)
    assert card.band == "low"
    assert card.risk_score < 22


def test_empty_rejected():
    res = client.post("/v1/score", json={"text": "   "})
    assert res.status_code == 422
