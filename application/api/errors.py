# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/16 14:59
"""
from flask import jsonify
from wtforms import ValidationError

from . import api


def bad_request(msg):
    resp = jsonify(error='bad request',
                   message=msg)
    resp.status_code = 400
    return resp


def unauthorized(msg):
    resp = jsonify(error='unauthorized', message=msg)
    resp.status_code = 401
    return resp


def forbidden(msg):
    resp = jsonify(error='forbidden', message=msg)
    resp.status_code = 403
    return resp


# 这个属于系统类错误，不用自定义
@api.app_errorhandler(404)
def page_not_found(e):
    response = jsonify(msg=str(e))
    response.status_code = 404
    return response


@api.app_errorhandler(405)
def method_not_allow(e):
    response = jsonify(msg=str(e))
    response.status_code = 405
    return response


@api.app_errorhandler(500)
def interval_error(e):
    response = jsonify(msg=str(e))
    response.status_code = 500
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
