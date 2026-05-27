import unittest

from backend.services import get_dashboard_payload, predict_patient


class BackendServicesTest(unittest.TestCase):
    def test_dashboard_payload_uses_required_modules_and_assets(self):
        payload = get_dashboard_payload()

        self.assertEqual(
            payload["modules"],
            [
                "Cohort Overview",
                "Patient Risk Assessment",
                "High-Risk Patients",
                "Patient Timeline",
                "Global Risk Drivers",
                "Research Export",
            ],
        )
        self.assertGreaterEqual(payload["cohort"]["rawRecords"], 200)
        self.assertGreaterEqual(len(payload["patients"]), 100)
        self.assertEqual(len(payload["shapAssets"]["ckd"]["dependencePlots"]), 3)
        self.assertEqual(len(payload["shapAssets"]["remission"]["dependencePlots"]), 4)

    def test_predict_patient_returns_two_catboost_risk_outputs(self):
        payload = get_dashboard_payload()
        patient = payload["patients"][0]

        result = predict_patient(patient["inputs"])

        self.assertEqual(result["predictionSource"], "catboost")
        self.assertEqual(result["shapSource"], "local_shap")
        self.assertEqual(len(result["outcomes"]), 2)
        for outcome in result["outcomes"]:
            self.assertIn(outcome["target"], ["CKD", "Delayed remission"])
            self.assertGreaterEqual(outcome["probability"], 0)
            self.assertLessEqual(outcome["probability"], 1)
            self.assertIn(outcome["riskCategory"], ["Low", "Moderate", "High"])
            self.assertGreater(len(outcome["topRiskDrivers"]), 0)


if __name__ == "__main__":
    unittest.main()
