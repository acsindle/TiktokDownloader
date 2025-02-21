from flask import Flask, request
from core.System import Bot
import os

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        update = request.get_json()
        Bot(update)
        return "oke - 200"
    else:
        return "INDEX"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.environ.get('PORT', 3000))
