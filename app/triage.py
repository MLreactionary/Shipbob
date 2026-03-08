from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TriageInput:
    order_id: str
    carrier: str
    exception_code: str
    hours_delayed: int
    inventory_risk: str
    customer_tier: str
    region: str


def _base_score(hours_delayed: int, inventory_risk: str, customer_tier: str) -> int:
    score = 0

    if hours_delayed >= 48:
        score += 4
    elif hours_delayed >= 24:
        score += 3
    elif hours_delayed >= 12:
        score += 2
    elif hours_delayed > 0:
        score += 1

    inventory_weights = {"low": 0, "medium": 2, "high": 4}
    score += inventory_weights.get(inventory_risk.lower(), 1)

    tier_weights = {"standard": 0, "pro": 1, "enterprise": 3}
    score += tier_weights.get(customer_tier.lower(), 1)

    return score


def _severity(score: int) -> str:
    if score >= 10:
        return "critical"
    if score >= 7:
        return "high"
    if score >= 4:
        return "medium"
    return "low"


def triage_exception(payload: TriageInput) -> Dict[str, object]:
    score = _base_score(payload.hours_delayed, payload.inventory_risk, payload.customer_tier)
    severity = _severity(score)

    owner = "carrier-ops"
    if payload.inventory_risk.lower() == "high":
        owner = "inventory-control"
    if payload.customer_tier.lower() == "enterprise" and severity in {"high", "critical"}:
        owner = "enterprise-support"

    actions: List[str] = [
        "Open incident in operations queue",
        "Notify customer with ETA and mitigation options",
    ]

    if payload.hours_delayed >= 24:
        actions.append("Escalate to carrier success manager")
    if payload.inventory_risk.lower() == "high":
        actions.append("Trigger safety-stock reallocation check")
    if severity == "critical":
        actions.append("Page on-call and schedule 30-min war room")

    summary = (
        f"Order {payload.order_id} shows {payload.exception_code} with {payload.hours_delayed}h delay "
        f"for a {payload.customer_tier} account in {payload.region}. "
        f"Inventory risk is {payload.inventory_risk}, yielding {severity} severity."
    )

    sla_hours = {"low": 24, "medium": 8, "high": 4, "critical": 1}[severity]

    return {
        "order_id": payload.order_id,
        "severity": severity,
        "score": score,
        "owner_team": owner,
        "sla_hours": sla_hours,
        "recommended_actions": actions,
        "summary": summary,
    }
