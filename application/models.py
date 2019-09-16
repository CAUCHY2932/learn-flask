# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/16 11:52
"""
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError

from application import db


class Base(db.Model):
    __abstract__ = True
    create_time = db.Column(db.Integer)
    status = db.Column(db.SmallInteger, default=1)

    # def __init__(self):
    #     pass

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    passwd_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),default=3)
    email = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>'% self.name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.passwd_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passwd_hash, password)


    def to_json(self):

        return dict(username=self.username,id=id)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    tag = db.Column(db.String(30))

    def to_json(self):
        return dict(id=self.id, title=self.title, tag=self.tag)

    @staticmethod
    def from_json(json_post):
        title = json_post.get('title')
        tag = json_post.get('tag')
        if title is None or title == '':
            raise ValidationError('post does not have a title')
        return Book(title=title, tag=tag)

# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title=db.Column(db.String(32))
#     content=db.Column(db.Text,nullable=False)
#     tag=db.Column(db.String(64),nullable=True)
#     create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)
#
#     def __repr__(self):
#         return '<User %r>' % self.title


# ad.add_view(ModelView(Article, db.session, name='文章管理'))
