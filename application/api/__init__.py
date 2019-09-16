# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/16 11:48
"""
from flask import Blueprint

api = Blueprint('api', __name__)

from . import users, book, post, errors
