# coding: utf-8
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_admin import Admin

db = SQLAlchemy()
mail = Mail()
# ad = Admin(name='microblog', template_mode='bootstrap3')
ad = Admin(name='microblog')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # register blueprint
    from application.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from application.admin import manage as manage_blueprint
    app.register_blueprint(manage_blueprint, url_prefix='/manage')

    # register plugins
    db.init_app(app=app)
    mail.init_app(app=app)
    ad.init_app(app=app)

    return app
