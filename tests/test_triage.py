import unittest

from app.triage import TriageInput, triage_exception


class TestTriage(unittest.TestCase):
    def test_critical_enterprise_case(self):
        payload = TriageInput(
            order_id="SB-1",
            carrier="UPS",
            exception_code="DELAY_WEATHER",
            hours_delayed=52,
            inventory_risk="high",
            customer_tier="enterprise",
            region="Northeast",
        )

        result = triage_exception(payload)

        self.assertEqual(result["severity"], "critical")
        self.assertEqual(result["owner_team"], "enterprise-support")
        self.assertEqual(result["sla_hours"], 1)
        self.assertIn("Page on-call and schedule 30-min war room", result["recommended_actions"])

    def test_medium_standard_case(self):
        payload = TriageInput(
            order_id="SB-2",
            carrier="USPS",
            exception_code="LABEL_SCAN_MISS",
            hours_delayed=10,
            inventory_risk="low",
            customer_tier="standard",
            region="West",
        )

        result = triage_exception(payload)

        self.assertEqual(result["severity"], "low")
        self.assertEqual(result["owner_team"], "carrier-ops")
        self.assertEqual(result["sla_hours"], 24)


if __name__ == "__main__":
    unittest.main()
