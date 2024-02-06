#!/usr/bin/env python3
"""
This app uses the babel.localeselector decorator
to create the get locale function
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Babel configuaration"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    This function retrieves the locale for a web page.
    and returns str: best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Routes to the index page: homepage"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
