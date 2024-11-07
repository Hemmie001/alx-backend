#!/usr/bin/env python3
"""This is a Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Routes to index(default)"""
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
