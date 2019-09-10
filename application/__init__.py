# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from datetime import datetime, date
# from flask import Flask
from werkzeug.http import http_date
import uuid
from flask._compat import text_type, PY2
from itsdangerous import json as _json


class JSONEncoder_(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            # print(o)
            return dict(o)
        if isinstance(o, datetime):
            return http_date(o.utctimetuple())
        if isinstance(o, date):
            return http_date(o.timetuple())
        if isinstance(o, uuid.UUID):
            return str(o)
        if hasattr(o, '__html__'):
            return text_type(o.__html__())
        return _json.JSONEncoder.default(self, o)

        # if isinstance(o, datetime):
        #     return o.strftime('%Y-%m-%dT%H:%M:%SZ')
        # if isinstance(o, date):
        #     return o.strftime('%Y-%m-%d')
        # return JSONEncoder.default(self, o)


class Flask(_Flask):
    json_encoder = JSONEncoder_


db = SQLAlchemy()


def register_plugins(app):
    db.init_app(app)


def create_app():
    app = Flask(__name__)

    from application.home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/home')

    register_plugins(app)
    return app
