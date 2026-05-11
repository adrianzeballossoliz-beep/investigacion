import os
from flask import Flask, send_file

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return send_file(os.path.join(BASE, "dashboard.html"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)