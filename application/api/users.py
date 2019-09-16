# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/16 11:54
"""
from . import api


@api.route('/')
def api_index():
    return 'hello'
