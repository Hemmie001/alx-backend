#!/usr/bin/env python3
"""Creates a user login system"""

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ Class configuration"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    This function retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    This function performs some routines before each
    request's resolution.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    This function retrieves the locale for a web page
    and returnsstr:best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    This default route returns html homepage
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
```

The key changes are:

1. The `users` dictionary is defined as a mocked user table.
2. The `get_user` function is defined to retrieve a user based on the `login_as` URL parameter.
3. The `before_request` function is defined and decorated with `@app.before_request` to execute before all other functions. This function calls `get_user` and sets the retrieved user (if any) as a global variable `g.user`.

The rest of the code remains the same, with the `5-index.html` template using the `g.user` variable to display the appropriate message.
