from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)


    # apply the blueprints to the app
    from dashboard import order

    app.register_blueprint(order.bp)

    return app