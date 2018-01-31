# -*- coding: utf-8 -*-

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import mySqlite
from mySqlite import query_db
import decision_arithmetic

app = Flask(__name__)
app.secret_key = '8bca81ae49bdc47625af3fe9769510117dcd6f965c9c1a05'
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.before_request
def before_request():
    g.db = mySqlite.connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


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
            sql = 'select * from users where username = ?'
            flag, res = query_db(sql, (_username,), True)
            if flag and str(res['password']) == _password:
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
            sql = 'insert into users values ( null , ? , ? )'
            flag, res = query_db(sql, (_username, _password))
            if flag:
                session['name'] = _username
                return redirect(url_for('main_interface'))
            else:
                error = '用户名已被注册'
        else:
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
        list_audio = []
        list_preferences = query_db(mySqlite.SQL_QUERY_PREFERENCES, (username,))
        list_detests = query_db(mySqlite.SQL_QUERY_DETESTS, (username,))
        if len(list_preferences) < 5 or len(list_detests) < 5:  # 随机挑选推荐
            list_audio = decision_arithmetic.random_recommend()
            print(list_audio)
        elif len(list_preferences) < 100 or len(list_detests) < 100:  # 决策树推荐
            pass
        else:  # 逻辑回归推荐
            pass
        return render_template('pineapple.html', list_audio=list_audio)
    else:
        return redirect(url_for('signin'))


if __name__ == "__main__":
    # with app.test_request_context():
    #     app.preprocess_request()
    # sql = 'select * from users'
    # sql = 'insert into users values ( null , ? , ? )'
    # print(mySqlite.query_db(sql, ('p',)))
    # print(mySqlite.query_db(sql))
    app.debug = True
    app.run()
