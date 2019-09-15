# -*- coding:utf-8 -*-
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, SmallInteger, orm
from werkzeug.security import generate_password_hash

from application import db


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        # self.create_time = int(datetime.now().timestamp())
        pass

    def __getitem__(self, item):
        return getattr(self, item)

    # @property
    # def create_datetime(self):
    #     if self.create_time:
    #         return datetime.fromtimestamp(self.create_time)
    #     else:
    #         return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)
            # if hasattr(self, key) and key != 'id':
            #     setattr(self, key, value)

    def delete(self):
        self.status = 0

    def keys(self):
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    passwd = generate_password_hash('')
    # insert_date = Column(Date)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'binding',
                       'publisher',
                       'price', 'pages', 'pubdate', 'isbn',
                       'summary',
                       'image']
