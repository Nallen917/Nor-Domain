#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<username>")
def index(username):
    return render_template("whatyacooking.html", name = username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

