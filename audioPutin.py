#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2018/1/18'
import os
import shutil
from mutatest import File
from dataObject import Audio
from dbConn import insert
import features_extraction

path = os.path.abspath('.')


def audioputindb(category):
    file_list = os.listdir("./static/audio/buffer store")
    for i in file_list:
        if os.path.splitext(i)[1] == '.mp3':
            if os.path.exists('./static/audio/' + i):
                os.unlink('./static/audio/buffer store/' + i)
            else:
                _audio = File('./static/audio/buffer store/' + i)
                _musicname = _audio.tags['TIT2'].text[0]
                _singer = None
                _addr = '/audio/' + i
                shutil.move('./static/audio/buffer store/' + i, './static/audio')
                _img_addr = None
                try:
                    _singer = _audio.tags['TPE1'].text[0]
                    _image = _audio.tags['APIC:'].data
                    _img_name = os.path.splitext(i)[0] + '.jpg'
                    _img = open('./static/img/' + _img_name, 'wb')
                    _img.write(_image)
                    _img.close()
                    _img_addr = '/img/' + _img_name
                except KeyError as _:
                    pass
                _category = category
                insert(Audio(_musicname, _singer, _addr, _img_addr, _category))
                features_extraction.extraction(i)


if __name__ == "__main__":
    audioputindb('秦腔')
    pass
