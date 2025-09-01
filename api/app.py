from flask import Flask, request, jsonify
from database import ping, fetch_all

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home(): 
    ok, err = ping()
    if ok: 
        return jsonify({"status": "ok", "message": "Connect DB OK"}), 200
    return jsonify({"status": "error", "message": "Connect DB Failed", "error": err}), 503

@app.route("/stocks/all", methods=["GET"])
def list_stocks():
    try: 
        rows = fetch_all()
        return jsonify({"status": "ok", "data": rows }), 200
    except Exception as e: 
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__": 
    ok, err = ping()
    if ok: 
        app.logger.info("Connected to Postgres successfully.")
    else: 
        app.logger.info(f"Connection to Postgres failed : {err}")

    app.run(host="0.0.0.0", port=5000, debug=True)
