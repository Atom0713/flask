import unittest
from main import create_app

app = create_app()

from tests.test_main.test_view import TestView

order_view = unittest.TestLoader().loadTestsFromTestCase(TestView)

suite = [
    order_view
         ]
# CREATE TEST SUITES
testSuite = unittest.TestSuite(suite)
unittest.TextTestRunner(verbosity=2).run(testSuite)