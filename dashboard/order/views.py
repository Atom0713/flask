from flask import Blueprint, jsonify

bp = Blueprint("order", __name__)

@bp.route("/")
def index():
    return jsonify({"status": "flask", "message": "Server is running!"})