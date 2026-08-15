from flask import Flask, request, jsonify
import requests
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
