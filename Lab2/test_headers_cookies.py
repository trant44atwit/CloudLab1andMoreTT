import unittest
import requests

PORT = "http://localhost:8080"

def test_getHeaders(self):
    headers = {
        "Content-Type": "application/json",
        "Y-Custom": "CustomValue",
        "user-email": "TTran",
        "my-val": "my_value"
    }

    response = requests.get(f"{PORT}/getHeaders", headers=headers)

    print("Status code: ", response.status_code)
    print("Response body: ", response.json())
    self.assertEqual(response.status_code, 200)