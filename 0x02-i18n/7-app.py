#!/usr/bin/env python3
"""Parametrizes templates
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict
import pytz


class Config:
    """configures available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/")
def index() -> str:
    """Defines homepage"""
    return render_template("7-index.html")


@babel.localeselector
def get_locale() -> str:
    """determines the best match with our supported languages"""
    locale_url = request.args.get('locale')
    if locale_url:
        return locale_url

    user_id = request.args.get('login_as')
    if user_id:
        locale_user = users.get(int(user_id)).get('locale')
        if locale_user in app.config['LANGUAGES']:
            return locale_user

    locale_headers = request.headers.get('locale')
    if locale_headers:
        return locale_headers

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """determines the best timezone"""
    try:
        timezone_url = request.args.get('timezone')
        if timezone_url:
            return pytz.timezone(timezone_url)

        user_id = request.args.get('login_as')
        if user_id:
            timezone_user = users.get(int(user_id)).get('timezone')
            if timezone_user:
                return pytz.timezone(timezone_user)
    except pytz.UnknownTimeZoneError:
        return app.config.get['BABEL_DEFAULT_TIMEZONE']

    return app.config.get['BABEL_DEFAULT_TIMEZONE']


def get_user() -> Dict:
    """returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """uses get_user to find a user if any, and set it as a global"""
    g.user = get_user()


if __name__ == "__main__":
    app.run(debug=True)
