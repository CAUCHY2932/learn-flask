# -*- coding:utf-8 -*-
from . import home
from flask import jsonify


@home.route('/')
def index():
    u = dict(msg='welcome to my site!')
    response = jsonify(u)
    response.status_code = 200
    return response
