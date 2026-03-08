# ShipBob FDE Assignment Project: Exception Triage Copilot

This repository contains a **portfolio-ready project** for Suraj Botcha's Forward Deployed Engineer application.

## Why this project fits your background

This project maps directly to your experience:

- **Agentic AI and RAG-style decision support** for operations workflows.
- **Backend/API engineering** with structured JSON contracts.
- **Explainability-first output** suitable for customer-facing and internal ops teams.

## Project summary

**Exception Triage Copilot** is a lightweight service that ingests fulfillment/shipping exception data and returns:

1. A severity score (`low | medium | high | critical`)
2. Action recommendations
3. A concise, explainable root-cause narrative
4. Suggested owner team and SLA

This mirrors real Forward Deployed work: turning ambiguous operational issues into reliable workflows with clear human handoff.

## Quick start

```bash
python -m unittest discover -s tests -p "test_*.py"
```

To run API locally (requires FastAPI + Uvicorn):

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Demo endpoints

- `GET /health`
- `POST /triage`

Sample payload:

```json
{
  "order_id": "SB-100234",
  "carrier": "UPS",
  "exception_code": "DELAY_WEATHER",
  "hours_delayed": 18,
  "inventory_risk": "medium",
  "customer_tier": "enterprise",
  "region": "Northeast"
}
```

## Why this is strong for your submission

- It's **domain-relevant** for ShipBob logistics operations.
- It demonstrates **production-minded API design**, deterministic guardrails, and explainable decisions.
- It is easy to demo in a 3–5 minute Loom with clear inputs/outputs.

See `docs/loom_script.md` and `docs/session_walkthrough.md` for a polished submission package.
