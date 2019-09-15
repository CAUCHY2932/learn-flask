# -*- coding:utf-8 -*-
from . import home
from flask import jsonify
from application.home.models import User
from application import db


@home.app_errorhandler(404)
def page_not_found(e):
    response = jsonify(msg=str(e))
    response.status_code = 404
    return response


@home.app_errorhandler(500)
def interval_error(e):
    response = jsonify(msg=str(e))
    response.status_code = 500
    return response


@home.route('/')
def index():
    u = User(id=1, name='zhangsan')

    # db.session.add(User)

    response = jsonify(u)
    response.status_code = 200
    return response
