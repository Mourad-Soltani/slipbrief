# SlipBrief rule catalog
# Signature: Mourad.Soltani
"""Deterministic signals that usually precede scope slip or unpaid extras."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Signal:
    key: str
    weight: int
    category: str
    hint: str
    phrases: tuple[str, ...]


SIGNALS: tuple[Signal, ...] = (
    Signal(
        "unbounded_revisions",
        18,
        "scope",
        "Cap revisions in writing (e.g. 2 rounds).",
        ("unlimited revisions", "as many revisions", "until we love it", "tweak until perfect"),
    ),
    Signal(
        "open_ended_scope",
        16,
        "scope",
        "Replace 'and more' language with a numbered deliverable list.",
        ("and more", "etc.", "other tasks as needed", "whatever is required", "flexible scope"),
    ),
    Signal(
        "missing_deadline",
        10,
        "timeline",
        "Ask for a single launch date and what happens if it slips.",
        (),
    ),
    Signal(
        "missing_budget",
        12,
        "money",
        "Ask for a budget band before estimating hours.",
        (),
    ),
    Signal(
        "pay_later",
        20,
        "money",
        "Require a deposit. Avoid 100% net-30 on first projects.",
        ("pay after", "pay when done", "net 60", "net 90", "we'll pay later", "invoice after launch"),
    ),
    Signal(
        "equity_instead",
        14,
        "money",
        "Treat equity-only as a no unless you already wanted that bet.",
        ("paid in equity", "sweat equity", "revenue share only", "exposure instead"),
    ),
    Signal(
        "stakeholder_fog",
        11,
        "process",
        "Name one decision owner. Group feedback is a delay machine.",
        ("the team will review", "several stakeholders", "board needs to see", "everyone must approve"),
    ),
    Signal(
        "asset_vacuum",
        9,
        "process",
        "List required assets and who supplies them, with dates.",
        ("you can find the copy", "just use whatever", "we will send later", "assets incoming"),
    ),
    Signal(
        "urgent_yesterday",
        13,
        "timeline",
        "Rush + vague scope is a classic underprice trap. Add a rush fee.",
        ("asap", "yesterday", "urgent", "this week no matter what"),
    ),
)


BUDGET_MARKERS = ("budget", "$", "usd", "eur", "retainer", "fixed price", "hourly")
DATE_MARKERS = (
    "deadline",
    "due",
    "by friday",
    "by monday",
    "launch",
    "go live",
    "2025",
    "2026",
    "2027",
)
