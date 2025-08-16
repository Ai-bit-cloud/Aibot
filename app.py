from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Akshith! Your Flask app is online 🎉"

if __name__ == "__main__":
    app.run()
