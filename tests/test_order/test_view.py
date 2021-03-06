import unittest
# from dashboard import create_app
from app import app
class TestView(unittest.TestCase):
    def setUp(self):
        # app = create_app()
        # app.testing = True
        self.app = app.test_client(self)
    # executed after each test
    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"message":"Server is running!","status":"flask"}\n', response.data)

    def test_inde(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"message":"erver is running!","status":"flask"}\n', response.data)