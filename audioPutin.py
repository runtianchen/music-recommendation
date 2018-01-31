#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2018/1/18'
import os
import shutil
from mutatest import File
from dataObject import Audio
from dbConn import insert
import features_extraction
import sqlite3

# path = os.path.abspath('.')
db = sqlite3.connect('database.db')
sql = 'insert into audios values (null,?,?,?)'


def audioputindb(category):
    _path = r'D:\戏曲\越剧\\'
    file_list = os.listdir(_path)
    for i in file_list:
        file_type = os.path.splitext(i)[1].lower()
        if file_type == '.mp3':
            # if os.path.exists('./static/audio/' + i):
            #     os.unlink('./static/audio/buffer store/' + i)
            # else:
            music_name = os.path.splitext(i)[0]
            path = '/audio/' + i
            # shutil.move('./static/audio/buffer store/' + i, './static/audio')
            # insert(Audio(_musicname, _classification, _path))
            # features_extraction.extraction(i)
            cur = db.cursor()
            try:
                cur.execute(sql, (music_name, category, path))
            except sqlite3.IntegrityError as e:
                print(music_name, e)
    db.commit()


if __name__ == "__main__":
    # audioputindb('越剧')
    # db.close()
    pass
