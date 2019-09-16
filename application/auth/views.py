# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/15 22:40
"""
from flask import jsonify

from application import db
from application.models import User
from . import auth
from .forms import RegisterForm


@auth.route('/', methods=['POST'])
def register():
    form = RegisterForm()
    if form.validate():

    # if form.validate_on_submit():
        u = User(email=form.email.data.lower(),
                 username=form.username.data,
                 password=form.password.data
                 )
        db.session.add(u)
        db.session.commit()
        return jsonify(user=u.to_json())

    return jsonify(msg='create_error')
