# Buyer notes — SlipBrief

Author: Mourad.Soltani

## What you are buying

A small FastAPI product that turns a messy client brief into a risk score and a reply checklist. Useful as a paid utility, an upsell inside a proposal tool, or a white-label widget on an agency site.

## Who pays

- Freelance PMs and designers who bid 3–10 projects a month
- 2–8 person web studios
- Proposal-software makers who want a “brief quality” add-on

## Why it is defensible enough for a first sale

Scoring is rule-based. You can show a prospect the exact phrase that raised the score. LLM wrappers cannot do that without extra cost and drift.

## Demo script (10 minutes)

1. Hit `/health`.
2. POST the messy brief in `tests/test_health.py`.
3. POST the clean brief. Show the band drop.
4. Walk the `questions` array as the email they send the client.

## Suggested offer

- Source + 30 days of email support from Mourad.Soltani: $490 one-time
- Or hosted at $9 / $29 per month once auth lands

## What is not included

Payments, multi-tenant auth, stored briefs. Those are week-two work.

## Transfer checklist

- Repo + LICENSE (MIT, Mourad.Soltani)
- Passing `pytest`
- This file and outreach templates (do not blast; one-to-one only)
