from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "Medication Reminder API running"})

@app.route("/api/medications", methods=["GET"])
def get_medications():
    return jsonify([
        {"name": "Paracetamol", "time": "08:00 AM"},
        {"name": "Vitamin D", "time": "09:00 PM"}
    ])

if __name__ == "__main__":
    app.run(debug=True)