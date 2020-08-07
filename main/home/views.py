from flask import Blueprint
from flask import jsonify
# import mysql.connector

bp = Blueprint("home", __name__)

# def getMysqlConnection():
#     return mysql.connector.connect(user='testing', host='mysql_database', port='3306', password='123', database='returns_test')

@bp.route("/")
def index():
    return jsonify({"status": "ok", "message": "Server is running!"})

# @bp.route("/api/get_users/", methods=['GET'])
# def get_users():
#     db = getMysqlConnection()
#
#     print(db)
#     try:
#         sql = "SELECT * FROM users;"
#         cur = db.cursor()
#         cur.execute(sql)
#         outpu_json = cur.fetchall()
#     except Exception as e:
#         print("Error in SQL: \n ", e)
#     finally:
#         db.close()
#     return jsonify(results=outpu_json)