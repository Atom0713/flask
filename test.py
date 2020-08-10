from tests.test_order.test_view import TestView
from tests.test_order.test_controller import TestOrderController

# app.testing = True
# app = app.test_client()
# db_url = os.environ.get("DATABASE_URL")
# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)
# with app.app_context():
#     db.create_all()

import unittest
order_view = unittest.TestLoader().loadTestsFromTestCase(TestView)
order_controller = unittest.TestLoader().loadTestsFromTestCase(TestOrderController)

suite = [
    order_view,
order_controller
         ]
# CREATE TEST SUITES
testSuite = unittest.TestSuite(suite)
unittest.TextTestRunner(verbosity=2).run(testSuite)