import unittest
import requests

PORT = "http://localhost:8080"

class L1Testing(unittest.TestCase):

    def test_root_route(self):
        response = requests.get(f"{PORT}/")
        expected_key = "message"
        expected_message = "Hello from the Cloud!"
        print(f"[ROOT] Expected: '{expected_key}': {expected_message}', Actual response: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], expected_message)

    def test_greetings(self):
        response = requests.get(f"{PORT}/greetings?name=Alice&age=25")
        expected = "Greetings Alice, good to know you are 25 years old."
        print(f"[GREETINGS] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Greetings Alice", response.text)

    def test_salutations_path(self):
        response = requests.get(f"{PORT}/salutations/Bob/40")
        expected = "Salutations Bob, you are 40 years old."
        print(f"[SALUTATIONS] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Salutations Bob", response.text)

    def test_yoda_personclass(self):
        response = requests.post(f"{PORT}/Yoda_personclass", json={"name": "Luke", "age": 21})
        expected = "21 years you are, young Luke"
        print(f"[YODA] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected, response.text)

    def test_time(self):
        response = requests.get(f"{PORT}/time")
        print(f"[TIME] Expected key: 'time', Actual response: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("time", response.json())

    def test_date(self):
        response = requests.get(f"{PORT}/date")
        print(f"[DATE] Expected key: 'date', Actual response: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("date", response.json())

    def test_addition(self):
        response = requests.get(f"{PORT}/addition?int1=5&int2=7")
        expected_total = 12
        actual_total = response.json()["total"]
        print(f"[ADDITION] Expected total: {expected_total}, Actual total: {actual_total}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_total, expected_total)

    def test_subtraction(self):
        response = requests.get(f"{PORT}/subtraction?int1=10&int2=4")
        expected_total = 6
        actual_total = response.json()["total"]
        print(f"[SUBTRACTION] Expected total: {expected_total}, Actual total: {actual_total}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_total, expected_total)

    def test_arrow(self):
        info = {"range1": 100, "range2": 200}
        response = requests.post(f"{PORT}/Arrow", json=info)
        expected = "The arrow's range is 100 or 200 meters."
        print(f"[ARROW] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("range is 100 or 200 meters", response.text)

    def test_choice(self):
        response = requests.post(f"{PORT}/Choice", json={"c1": "cats", "c2": "dogs"})
        expected = "It is either cats or dogs."
        print(f"[CHOICE] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("It is either cats or dogs", response.text)