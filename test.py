from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Wazzup y'all! Welcome to <h1>QWER HACKS!!!<h1>"

if __name__ == "__name__":
    app.run()