# Coding Agent Session Walkthrough (for submission)

## Goal
Build a logistics-facing AI backend prototype that demonstrates FDE strengths:

- translating ops pain points into productized workflow logic,
- exposing model/agent decisions through an API,
- and keeping outputs explainable and actionable.

## What was built
- A FastAPI service (`app/main.py`) with `POST /triage` endpoint.
- A deterministic triage policy engine (`app/triage.py`) that creates:
  - severity,
  - owner team,
  - SLA,
  - recommended actions,
  - and summary narrative.
- Unit tests validating critical vs low-severity behavior (`tests/test_triage.py`).

## Why this aligns with Suraj Botcha's resume
- Uses your **agentic + orchestration mindset** to convert raw events into structured decisions.
- Demonstrates **backend platform design** with reusable modules and API contracts.
- Emphasizes **explainability and operations impact**, similar to your anomaly and RCA work.

## Expansion ideas (mention in interview)
1. Add retrieval from runbooks (RAG over SOP docs).
2. Add LLM-generated customer messaging with policy constraints.
3. Persist incidents and feedback loop for severity calibration.
4. Add simulation harness and offline evaluation metrics.
