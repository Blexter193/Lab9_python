import unittest
from labs.lab_7.Functions.api_client import ApiClient

class TestApiClient(unittest.TestCase):
    def setUp(self):
        self.client = ApiClient("https://jsonplaceholder.typicode.com")

    def test_get_posts(self):
        posts = self.client.get_data("posts")
        self.assertIsInstance(posts, list)

if __name__ == '__main__':
    unittest.main()