from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        return render_template("success.html")
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

