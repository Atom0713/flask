import unittest
# from test import app
from app import app


class TestView(unittest.TestCase):
    # executed after each test
    def tearDown(self):
        pass

    def test_index(self):
        response = app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"message":"Server is running!","status":"ok"}\n', response.data)