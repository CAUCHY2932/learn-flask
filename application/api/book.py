# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/16 13:42
"""
from flask import jsonify, request

from application import db
from application.models import Book
from . import api


@api.route('/books/', methods=['GET'])
def get_books():
    books = Book.query.all()
    response = jsonify(books=[b.to_json() for b in books])
    response.status_code = 200
    return response


@api.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    b = Book.query.filter(Book.id == book_id).first()
    if b:
        response = jsonify(search_book=b.to_json())
        response.status_code = 200
        return response
    response = jsonify(search="")
    response.status_code = 200
    return response


@api.route('/book', methods=['POST'])
def new_book():
    b = Book.from_json(request.json)
    db.session.add(b)
    db.session.commit()
    response = jsonify(add_book=b.to_json())
    response.status_code = 200
    return response


@api.route('/book/<int:book_id>', methods=['PUT'])
def put_book(book_id):
    b = Book.query.filter(Book.id == book_id).first()
    if b:
        b.title = request.json.get('title')
        b.tag = request.json.get('tag')
        db.session.add(b)
        db.session.commit()
        response = jsonify(update_book=b.to_json())
        response.status_code = 200
        return response
    response = jsonify(update_book='')
    response.status_code = 200
    return response


@api.route('/book/<int:book_id>', methods=['DELETE'])
def del_book(book_id):
    b = Book.query.filter(Book.id == book_id).first()
    if b:
        db.session.delete(b)
        db.session.commit()
        response = jsonify(del_book=b.to_json())
        response.status_code = 200
        return response
    response = jsonify(del_book='')
    response.status_code = 200
    return response
