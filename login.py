from flask import Flask, request, render_template
import commitDB
import os
import pygame
import time
import threading

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    user = commitDB.select_name(username)
    if user:
        if user.password == password:
            _preferences_list = commitDB.getpreferencesbyname(username)
            _detest_list = commitDB.getdetestsbyname(username)
            return render_template('pineapple.html', username=username, preferences_list=_preferences_list,
                                   detest_list=_detest_list, path=os.path.abspath('.'),
                                   listsize=[username, username, username, username, username, username, username,
                                             username, username, ])
    return render_template('form.html', message='Bad username or password', username=username)


def play_audio(_file):
    print("播放音乐1")
    track = pygame.mixer.music.load(_file)
    pygame.mixer.music.play()


if __name__ == '__main__':
    """    pygame.mixer.init()
    t = threading.Thread(target=play_audio, args=(file,))
    t.setDaemon(True)
    t.start()
    while 1:
        pass
    t.join()"""
    """    path = os.path.abspath('.')
    print(path)
    os.chdir(r'%s\audio' % path)
    print(os.path.abspath('.'))
    for file in os.listdir('.'):
        if os.path.isfile(file):
            print(file)"""
    print(app.root_path)
    app.debug = True
    app.run()
