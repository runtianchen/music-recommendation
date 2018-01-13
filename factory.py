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
import commitDB

app = Flask(__name__)
app.secret_key = '8bca81ae49bdc47625af3fe9769510117dcd6f965c9c1a05'


@app.route('/')
def index():
    return redirect(url_for('main_interface'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        if _username:
            _user = commitDB.select_name(_username)
            if _user and _user[2] == _password:
                # flash('You were logged in')
                session['name'] = _username
                return redirect(url_for('main_interface'))
            else:
                error = '错误的用户名或密码'
        else:
            return redirect(url_for('signup'))
    return render_template('signin.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        if _username and _password:
            session['name'] = _username
            return redirect(url_for('main_interface'))
        error = '用户名，密码不能为空'
    return render_template('signup.html', error=error)


@app.route('/signout')
def signout():
    session.pop('name', None)
    # flash('You were logged out')
    return redirect(url_for('signin'))


@app.route('/interface')
def main_interface():
    username = session.get('name')
    if username:
        _music_list = commitDB.getpreferencesbyname(username)
        return render_template('pineapple.html', music_list=_music_list)
    else:
        return redirect(url_for('signin'))


if __name__ == "__main__":
    app.debug = True
    app.run()
