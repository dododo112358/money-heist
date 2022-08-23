import joblib
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/",methods=["POST"])
def return_pstns():
    username = request.headers["username"]
    code = request.json["code"]
    if username != "7105idanhe":
        return "Not Authorized", 401
    if code != "3786":
        return 500
    return jsonify({"a": 2})

joblib.dump(["idan","roei"],"lst.zlib")

# app.run()