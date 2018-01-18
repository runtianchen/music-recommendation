# 导入:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataObject import User, Audio, Preference,Detest

# 初始化数据库连接:
engine = create_engine("mysql+pymysql://root:password@localhost:3306/music_recommendation?charset=utf8",
                       encoding="utf-8")
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def insert(data_object):
    session = DBSession()
    # 添加到session:
    session.add(data_object)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


def delete(table, data_object):
    pass


def update(table, data_object):
    pass


def select_all(tablename):
    # 创建session对象:
    session = DBSession()
    for table in [User, Audio]:
        if table.__tablename__ == tablename:
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            res = session.query(table).all()
            # 关闭Session:
            session.close()
            return res


def select_one(tablename, vaule):
    # 创建session对象:
    session = DBSession()
    if tablename == User.__tablename__:
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        res = session.query(User).filter(User.username == vaule).one()
        # 关闭Session:
        session.close()
    elif tablename == Audio.__tablename__:
        res = session.query(Audio).filter(Audio.musicname == vaule).one()
        session.close()
    return res


def select_preferences(value):
    session = DBSession()
    user = session.query(User).filter(User.username == value).first()
    pre_list = session.query(Preference.musicid).filter(Preference.userid == user.id).all()
    if pre_list:
        audios = session.query(Audio).filter(Audio.id.in_(list(list(zip(*pre_list))[0]))).all()
        session.close()
        return audios
    else:
        session.close()
        return


def select_detests(value):
    session = DBSession()
    user = session.query(User).filter(User.username == value).first()
    det_list = session.query(Detest.musicid).filter(Detest.userid == user.id).all()
    if det_list:
        audios = session.query(Audio).filter(Audio.id.in_(list(list(zip(*det_list))[0]))).all()
        session.close()
        return audios
    else:
        session.close()
        return


if __name__ == "__main__":
    print(select_all('audios'))
    pass
