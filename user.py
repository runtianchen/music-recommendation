class User(object):
    # 表的结构:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def __str__(self):
        return str(User.user2dict(self))

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @staticmethod
    def user2dict(_user):
        user_dict = {'username': _user.username, 'password': _user.password}
        return user_dict

    @staticmethod
    def data2user(_tuple):
        _user = User(_tuple[1], _tuple[2])
        return _user


if __name__ == "__main__":
    user = User("abc", "123")
    print(user.username)
