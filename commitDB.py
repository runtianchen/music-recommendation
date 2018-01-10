import pymysql.cursors
import user
import os
from mutagen import File
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 数据库配置
config = {'host': '127.0.0.1',
          'port': 3306,
          'user': 'root',
          'password': 'password',
          'db': 'music_recommendation',
          'charset': 'utf8mb4'}


# 创建连接
def init_conn():
    conn = pymysql.connect(**config)
    return conn


# 查找所有用户
def select_all(_db):
    conn = init_conn()
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = 'SELECT * FROM %s' % _db
            cursor.execute(sql)
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        conn.commit()
    finally:
        conn.close()
    # users_list = []
    # if result:
    #        users_list.append(user.User.data2user(_data))
    return result


# 查找用户通过username
def select_name(_db, _name):
    conn = init_conn()
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = 'SELECT * FROM %s where username = %s' % (_db, _name)
            cursor.execute(sql)
            # 获取查询结果
            result = cursor.fetchone()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        conn.commit()
    finally:
        conn.close()
    if result:
        # _user = user.User.data2user(result)
        return result


# 添加一个新的用户
def insert_user(_user):
    conn = init_conn()
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = 'INSERT INTO users (username,password) VALUES (%s,%s);'
            cursor.execute(sql, (_user.username, _user.password))
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        conn.commit()
    finally:
        conn.close()


# 获得指定用户喜欢的歌曲列表
def getpreferencesbyname(_username):
    conn = init_conn()
    try:
        with conn.cursor() as cursor:
            sql = 'select users.username, audios.musicname from users inner join preference ' \
                  'on users.id = preference.userid inner join audios ' \
                  'on preference.musicid = audios.id where username = %s'
            cursor.execute(sql, _username)
            # 获取查询结果
            _result = cursor.fetchall()
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            conn.commit()
    finally:
        conn.close()
    _music_list = []
    if _result:
        for _data in _result:
            _music_list.append(_data[1])
    return _music_list


# 获得指定用户厌恶的歌曲列表
def getdetestsbyname(_username):
    conn = init_conn()
    try:
        with conn.cursor() as cursor:
            sql = 'select users.username, audios.musicname from users inner join detest ' \
                  'on users.id = detest.userid inner join audios ' \
                  'on detest.musicid = audios.id where username = %s'
            cursor.execute(sql, _username)
            # 获取查询结果
            _result = cursor.fetchall()
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            conn.commit()
    finally:
        conn.close()
    _music_list = []
    if _result:
        for _data in _result:
            _music_list.append(_data[1])
    return _music_list


def updatabyid(_db, **_kwargs):
    conn = init_conn()
    cursor = conn.cursor()
    sql = 'show columns from audios'
    cursor.execute(sql)
    _result = cursor.fetchall()
    columns = []
    for i in _result:
        columns.append(i[0])
    sql = 'update %s set '
    for column in columns:
        if column == 'id':
            continue
        else:
            sql = '%s%s%s' % (sql, column, ' = %s ')
    sql = '%s%s' % (sql, 'where id = %s')
    print(sql % (_db, _kwargs['musicname'], _kwargs['singer'], _kwargs['addr'], _kwargs['img_addr'],
                 str(_kwargs['id'])))
    # print(sql)
    # cursor.execute(sql )
    # conn.commit()


if __name__ == "__main__":
    """
    os.chdir(os.path.abspath('.') + r'\audio')
    conn = init_conn()
    cursor = conn.cursor()
    for file in os.listdir():
        if os.path.isfile(file):
            _audio = File(os.getcwd() + r'\\' + file)
            musicname = _audio.tags["TIT2"].text[0]
            singer = _audio.tags["TPE1"].text[0]
            addr = r'\\audio\\' + file
            file = file.split('.')
            file = file[0] + '.jpg'
            img_addr = r'\\img\\' + file
            kwargs = {'musicname': musicname, 'singer': singer, 'addr': addr,
                      'img_addr': img_addr}
            sql = 'insert into audios values(Null,"%s","%s","%s","%s")' % (musicname, singer, addr, img_addr)
            #print(sql)
            cursor.execute(sql)
    conn.commit()
    conn.close()
    """
    pass
