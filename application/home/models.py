# -*- coding:utf-8 -*-
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, SmallInteger, orm
from werkzeug.security import generate_password_hash

from application import db, ad


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    # def __init__(self):
    #     pass


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(32))
    content=db.Column(db.Text,nullable=False)
    tag=db.Column(db.String(64),nullable=True)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.title


ad.add_view(ModelView(Article, db.session, name='文章管理'))
ad.add_view(ModelView(User, db.session, name='用户管理'))
ad.add_view(ModelView(Post, db.session, name='投递管理'))
