import unittest


from dashboard.order.controller import Fetch

class TestOrderController(unittest.TestCase):
    def setUp(self):
        self.fetch = Fetch()
    def test_multiply(self):
        self.assertEqual(self.fetch.multiply(2, 3), 6)


