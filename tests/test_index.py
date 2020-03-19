import json
import unittest
from services.app import app


class TestIndex(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_index_view(self):
        response = self.client.get("/")
        body = json.loads(response.data.decode("utf-8"))
        self.assertEqual(body, {})


if __name__ == "__main__":
    unittest.main()
