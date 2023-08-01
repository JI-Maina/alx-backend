#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configures available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Defines homepage"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """determines the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
