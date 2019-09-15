# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/15 22:40
"""
from . import manage


@manage.route('/')
def index():
    return 'manage site'
