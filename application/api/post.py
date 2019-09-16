# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/16 13:31
"""
from . import api


@api.route('/article', methods=['GET'])
def get_post():
    return 'art'


@api.route('/article', methods=['POST'])
def new_post():
    pass
