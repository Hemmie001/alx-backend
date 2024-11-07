#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")   

def index():
    return render_template("0-index.html")

# Run the development server (optional for testing)
if __name__ == "__main__":
    app.run(debug=True)
