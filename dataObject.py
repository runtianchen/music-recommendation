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
    singer = Column(String(20))
    addr = Column(String(50))
    img_addr = Column(String(50))

    def __init__(self, musicname, singer=None, addr=None, img_addr=None, id=None):
        self.id = None
        self.musicname = musicname
        self.singer = singer
        self.addr = addr
        self.img_addr = img_addr

    def __repr__(self):
        return '<[Audio-%s] musicname : %s, singer : %s, addr : %s, img_addr : %s>' % (
            self.id, self.musicname, self.singer, self.addr, self.img_addr)


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
