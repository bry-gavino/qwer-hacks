from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/filter/")
def filter():
    return render_template("filter.html")

if __name__ == "__name__":
    app.run()