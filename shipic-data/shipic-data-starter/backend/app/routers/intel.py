from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.schemas import SignalOut

from app.services.trends.google_trends import fetch_interest_series

router = APIRouter(prefix="/intel", tags=["intel"])

@router.post("/ingest/google-trends", summary="Fetch & store Google Trends for a keyword")
def ingest_trends(
    keyword: str = Query(..., min_length=2),
    db: Session = Depends(get_db),
):
    items = fetch_interest_series(keyword)
    # TODO: Implement save_signals
    raise NotImplementedError("save_signals function is not implemented.")

@router.get("/signals", response_model=List[SignalOut], summary="Read latest signals by keyword")
def read_signals(
    keyword: str,
    source: str | None = None,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    # TODO: Implement latest_signals
    raise NotImplementedError("latest_signals function is not implemented.")
