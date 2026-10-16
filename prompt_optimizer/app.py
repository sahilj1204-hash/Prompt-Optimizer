from flask import Flask, render_template, request, jsonify
from optimizer import optimize_prompt

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received."}), 400

    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Please enter a prompt."}), 400

    result = optimize_prompt(prompt)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)