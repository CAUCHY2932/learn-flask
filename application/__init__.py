# coding: utf-8
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # register blueprint
    from application.home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/home')

    # register plugins
    db.init_app(app=app)
    mail.init_app(app=app)

    return app
