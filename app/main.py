from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.triage import TriageInput, triage_exception

app = FastAPI(title="ShipBob Exception Triage Copilot", version="0.1.0")


class TriageRequest(BaseModel):
    order_id: str = Field(..., description="ShipBob order reference")
    carrier: str
    exception_code: str
    hours_delayed: int = Field(..., ge=0)
    inventory_risk: str
    customer_tier: str
    region: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/triage")
def triage(request: TriageRequest) -> dict:
    payload = TriageInput(**request.model_dump())
    return triage_exception(payload)
