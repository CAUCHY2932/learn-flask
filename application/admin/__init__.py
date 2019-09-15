# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/15 22:39
"""
from flask import Blueprint


manage = Blueprint('manage', __name__)

from . import views
