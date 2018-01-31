from sqlalchemy import Column, String, Integer, UniqueConstraint, Index, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(20))

    def __init__(self, username, password, id=None):
        self.id = None
        self.username = username
        self.password = password

    def __repr__(self):
        return '<[User-%s] username : %s, password : %s>' % (self.id, self.username, self.password)


# 定义Audio对象:
class Audio(Base):
    # 表的名字:
    __tablename__ = 'audios'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    musicname = Column(String(50))
    classification = Column(String(50))
    path = Column(String(50))

    def __init__(self, musicname, classification=None, path=None):
        self.id = None
        self.musicname = musicname
        self.classification = classification
        self.path = path

    def __repr__(self):
        return '<[Audio-%s] musicname : %s, classification : %s, path : %s>' % (
            self.id, self.musicname, self.classification, self.path)


class Preference(Base):
    __tablename__ = 'preferences'
    __table_args__ = (
        PrimaryKeyConstraint('userid', 'musicid'),
    )

    userid = Column(Integer, ForeignKey("users.id"))
    musicid = Column(Integer, ForeignKey("audios.id"))

    def __init__(self, userid, musicid):
        self.userid = userid
        self.musicid = musicid


class Detest(Base):
    __tablename__ = 'detests'
    __table_args__ = (
        PrimaryKeyConstraint('userid', 'musicid'),
    )

    userid = Column(Integer, ForeignKey("users.id"))
    musicid = Column(Integer, ForeignKey("audios.id"))

    def __init__(self, userid, musicid):
        self.userid = userid
        self.musicid = musicid


if __name__ == "__main__":
    pass
