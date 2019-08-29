# -*- coding:utf-8 -*-
from flask import Flask
from settings import name

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world %s' % name

if __name__ == '__main__':
    app.run(debug=True)
