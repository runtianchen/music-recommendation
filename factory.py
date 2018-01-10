# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~
    A microblog example application written as Flask tutorial with
    Flask and sqlite3.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #     if request.form['username'] != app.config['USERNAME']:
        #         error = 'Invalid username'
        #     elif request.form['password'] != app.config['PASSWORD']:
        #         error = 'Invalid password'
        #     else:
        #         session['logged_in'] = True
        #         flash('You were logged in')
        return render_template('pineapple.html')
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.debug = True
    app.run()
