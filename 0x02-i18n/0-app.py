#!/usr/bin/env python3
"""Initializes a flask app and index route 
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Defines homepage"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
