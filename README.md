# SlipBrief

Signature: **Mourad.Soltani**

Micro-SaaS that scores a freelance or agency client brief for scope-slip risk.

Paste the brief. Get a 0–100 score, a low/medium/high band, the phrases that triggered it, and the questions to send back before you quote.

Built as a solo, shippable API. No LLM required. Rules are deterministic so quotes stay consistent.

## Why this now

Freelancers still underprice vague briefs. Trending “meeting ROI” and “proposal hub” tools are crowded. A brief-risk gate that lives in front of the proposal is still thin on GitHub (no `slipbrief` product repo at build time).

Buyer: independent designers, web shops, and boutique agencies who already write proposals by hand.

Price sketch: $9/mo solo, $29/mo studio (shared workspace later).

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

Health: `GET /health`  
Score: `POST /v1/score` with `{"text": "...brief..."}`

## Tests

```bash
pytest -q
```

## Scope of this MVP

- Rule catalog for money, timeline, scope, and process risk
- JSON API + health check
- Tests that must pass before zip / push

Out of scope (next paid slice): accounts, saved briefs, Slack paste, PDF export.

## Author

Mourad.Soltani
