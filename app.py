import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your MySQL Connection
# db = SQLAlchemy()
# db_url = os.environ.get("DATABASE_URL")
# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)
# with app.app_context():
#     db.create_all()

# class Database(db.Model):
#
#     versionID = db.Column('versionID', db.Integer, primary_key=True)
#     versionText = db.Column('versionText', db.String(500),
#     unique=False)
#
#     def __init__(self, versionID, versionText):
#         self.versionID = versionID
#         self.versionText = versionText
#
#     def serialize(self):
#         return {
#             'VersionID'     :   self.versionID,
#             'VersionText'   :   self.versionText
#         }

@app.route("/")
def index():
    return jsonify({"status": "flask", "message": "Server is running!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(8080))