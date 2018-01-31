#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2018/1/31'

import os
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

path = os.getcwd()
DATABASE = path + '/database.db'

SQL_SELECT_USERS = 'select * from users'
SQL_SELECT_AUDIOS = 'select * from audios'
SQL_INSERT_PREFERENCES = 'insert into preferences values (?,?)'
SQL_INSERT_DETESTS = 'insert into detests values (?,?)'
SQL_QUERY_PREFERENCES = 'select users.username, audios.music_name from users inner join preferences ' \
                        'on users.id = preferences.user_id inner join audios ' \
                        'on preferences.audio_id = audios.id where username = ?'
SQL_QUERY_DETESTS = 'select users.username, audios.music_name from users inner join detests ' \
                    'on users.id = detests.user_id inner join audios ' \
                    'on detests.audio_id = audios.id where username = ?'


def connect_db():
    """Connects to the specific database."""
    return sqlite3.connect(DATABASE)


def init_db():
    with closing(connect_db()) as db:
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def query_db(query, args=(), one=False):
    try:
        cur = g.db.execute(query, args)
        g.db.commit()
    except sqlite3.IntegrityError as e:
        return False, e
    else:
        rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
        return True, (rv[0] if rv else None) if one else rv


if __name__ == "__main__":
    # init_db()
    pass
