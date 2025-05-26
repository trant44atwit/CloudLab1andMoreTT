import unittest
import requests

PORT = "http://localhost:8080"

class L1Testing(unittest.TestCase):

    def test_root_route(self):
        response = requests.get(f"{PORT}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_greetings(self):
        response = requests.get(f"{PORT}/greetings", params={"name": "Alice", "age": 25})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Greetings Alice", response.text)

    def test_salutations_path(self):
        response = requests.get(f"{PORT}/salutations/Bob/40")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Salutations Bob", response.text)

    def test_yoda_personclass(self):
        payload = {"name": "Luke", "age": 21}
        response = requests.post(f"{PORT}/Yoda_personclass", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("21 years you are, young Luke", response.text)

    def test_time(self):
        response = requests.get(f"{PORT}/time")
        self.assertEqual(response.status_code, 200)
        self.assertIn("time", response.json())

    def test_date(self):
        response = requests.get(f"{PORT}/date")
        self.assertEqual(response.status_code, 200)
        self.assertIn("date", response.json())

    def test_addition(self):
        response = requests.get(f"{PORT}/addition", params={"int1": 5, "int2": 7})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], 12)

    def test_subtraction(self):
        response = requests.get(f"{PORT}/subtraction", params={"int1": 10, "int2": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], 6)

    def test_arrow(self):
        payload = {"range1": 100, "range2": 200}
        response = requests.post(f"{PORT}/Arrow", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("range is 100 or 200 meters", response.text)

    def test_choice(self):
        payload = {"c1": "cats", "c2": "dogs"}
        response = requests.post(f"{PORT}/choice", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("either cats or dogs", response.text)
