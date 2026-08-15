from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/gold")
def gold():
    interval = request.args.get("interval", "1m")
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/XAUUSD=X?interval={interval}&range=7d"

    r = requests.get(url)
    return jsonify(r.json())

@app.route("/")
def home():
    return "Gold API Relay is running!"
