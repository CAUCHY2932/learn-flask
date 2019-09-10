# -*- coding:utf-8 -*-
from . import home
from flask import jsonify
from application.home.models import User
from application import db


@home.route('/')
def index():
    u = User(id=1, name='zhangsan')

    # db.session.add(User)


    response = jsonify(u)
    response.status_code = 200
    return response
