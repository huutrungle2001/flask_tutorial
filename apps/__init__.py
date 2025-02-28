from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
import os

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
# This will create a file in <app> FOLDER
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite3')
SESSIONS = [
    {
        "session_id": 1,
        "session_name": "Ballet",
        "user_id": 1,
        "date": "2021-01-01",
        "duration": 60,
        "performance_notes": "Great session!"
    },
    {
        "session_id": 2,
        "session_name": "Hip-Hop",
        "user_id": 1,
        "date": "2021-01-02",
        "duration": 45,
        "performance_notes": "Good session!"
    },
    {
        "session_id": 3,
        "session_name": "Salsa",
        "user_id": 2,
        "date": "2021-01-03",
        "duration": 30,
        "performance_notes": "Bad session!"
    },
    {
        "session_id": 4,
        "session_name": "Tango",
        "user_id": 2,
        "date": "2021-01-04",
        "duration": 90,
        "performance_notes": "Great session!"
    },
    {
        "session_id": 5,
        "session_name": "Breakdancing",
        "user_id": 3,
        "date": "2021-01-05",
        "duration": 60,
        "performance_notes": "Good session!"
    }
]


def register_blueprints(app):
    for module_name in (
        "home",
    ):
        module = import_module("apps.{}.routes".format(module_name))
        app.register_blueprint(module.blueprint)

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    register_blueprints(app)

    return app