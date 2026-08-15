from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/gold")
def gold():
    interval = request.args.get("interval", "1m")
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/XAUUSD=X?interval={interval}&range=7d"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()
    except Exception as e:
        return jsonify({"error": "Yahoo request failed", "details": str(e)}), 500

    # اگر دیتا خالی بود
    if "chart" not in data or data["chart"]["result"] is None:
        return jsonify({"error": "Empty data from Yahoo"}), 500

    try:
        result = data["chart"]["result"][0]
        timestamps = result["timestamp"]
        indicators = result["indicators"]["quote"][0]
    except Exception as e:
        return jsonify({"error": "Invalid Yahoo format", "details": str(e)}), 500

    return jsonify({
        "timestamp": timestamps,
        "open": indicators["open"],
        "high": indicators["high"],
        "low": indicators["low"],
        "close": indicators["close"]
    })

@app.route("/")
def home():
    return "Gold API Relay is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
