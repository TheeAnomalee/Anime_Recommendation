import unittest
from app.webapp import app
from app.recommender import recommend_anime


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter Anime Title:', response.data)

    def test_home_post_valid(self):
        response = self.client.post("/", data={"title": "Naruto"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recommendations for", response.data)

    def test_home_post_invalid(self):
        response = self.client.post("/", data={"title": "ThisDoesNotExist"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Anime not found", response.data)

if __name__ == '__main__':
    unittest.main()
