#!/usr/bin/env python3
"""Simple flask app."""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config(object):
    """Configuration class"""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Determines best local match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello() -> str:
    """Return hello world"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
