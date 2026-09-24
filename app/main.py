# SlipBrief HTTP API
# Signature: Mourad.Soltani
from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.engine import score_brief

app = FastAPI(
    title="SlipBrief",
    version="0.1.0",
    description="Score a client brief for scope-slip risk. Built by Mourad.Soltani.",
)


class BriefIn(BaseModel):
    text: str = Field(..., min_length=1, max_length=20_000)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "slipbrief", "author": "Mourad.Soltani"}


@app.post("/v1/score")
def score(payload: BriefIn) -> dict:
    card = score_brief(payload.text)
    if card.word_count == 0:
        raise HTTPException(status_code=422, detail="Brief is empty after trim.")
    return card.as_dict()
