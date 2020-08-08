import unittest
from dashboard import create_app

class TestView(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()
    # executed after each test
    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"message":"Server is running!","status":"flask"}\n', response.data)