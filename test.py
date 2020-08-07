import os
import unittest
from app import app, db

from tests.test_view import TestView

# app.testing = True
# app = app.test_client()
db_url = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

order_view = unittest.TestLoader().loadTestsFromTestCase(TestView)

suite = [
    order_view
         ]
# CREATE TEST SUITES
testSuite = unittest.TestSuite(suite)
unittest.TextTestRunner(verbosity=2).run(testSuite)