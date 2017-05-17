#!/usr/bin/python
# __author__ = 'jasonsheh'
# -*- coding:utf-8 -*-

import sys

from database import Database

from flask import Flask, render_template
app = Flask(__name__)

max_page = Database().count()


@app.route('/')
@app.route('/index')
@app.route('/<int:page>')
def index(page=1):
    results = Database().select_page(page)
    return render_template('index.html',
                           results=results, page=page, max_page=max_page)


@app.route('/detail/<int:_id>')
def detail(_id):
    result = Database().select_detail(_id)
    print(result)
    return render_template('detail.html',
                           result=result)


if __name__ == '__main__':
    try:
        app.run()
    except KeyboardInterrupt:
        sys.exit()