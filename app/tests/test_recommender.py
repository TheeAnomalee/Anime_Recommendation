import unittest
from app.recommender import recommend_anime, anime_df

class TestRecommender(unittest.TestCase):
    def test_valid_title(self):
        result = recommend_anime("Naruto")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0], "Naruto")

    
    def test_invalid_title(self):
        result = recommend_anime("Nonexistent Anime")
        self.assertEqual(result, ['Anime not found.'])


    def test_return_fields(self):
        result = recommend_anime("Naruto")
        self.assertTrue(any("Naruto" in anime for anime in result))


if __name__ == '__main__':
    unittest.main()