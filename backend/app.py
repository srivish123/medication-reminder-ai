from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Medication Reminder Backend - Pre Event Setup"

if __name__ == "__main__":
    app.run(debug=True)
