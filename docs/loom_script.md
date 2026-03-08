# 3–5 Minute Loom Script

## 0:00–0:30 — Intro
"Hi, I’m Suraj Botcha. For this demo, I built an Exception Triage Copilot for ShipBob-like fulfillment operations. The objective is to automatically classify shipping exceptions, route ownership, and provide clear recommended actions."

## 0:30–1:30 — Problem framing
"In fulfillment ops, exceptions are frequent and context-heavy. Teams lose time deciding urgency and owner. This system converts an event into a severity, SLA, and action list so humans can act immediately."

## 1:30–2:30 — Technical walkthrough
- Show `app/triage.py` scoring logic.
- Explain weighted signals: delay, inventory risk, customer tier.
- Show deterministic owner-routing and SLA mapping.
- Highlight explainable summary string.

## 2:30–3:30 — API and test demo
- Show `app/main.py` endpoints.
- Run `python -m unittest discover -s tests -p "test_*.py"`.
- Optionally call `/triage` with sample JSON and show response.

## 3:30–4:30 — Why I’m proud of it
"I’m proud because this is realistic FDE work: turning messy operational pain into a robust, explainable workflow that can be integrated into production systems. It’s intentionally simple to deploy, and extensible with retrieval + LLM layers."

## 4:30–5:00 — Close
"Next, I’d add runbook retrieval, human feedback capture, and model-based messaging generation under policy constraints."
