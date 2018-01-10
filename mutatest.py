from mutagen import File
from mutagen.id3 import ID3
import os


def func():
    _path = os.getcwd()
    print(_path)
    os.chdir(_path + "\\audio")
    for file in os.listdir('.'):
        if os.path.isfile(file):
            _audio = File(file)
            try:
                _image = _audio.tags['APIC:'].data
                os.chdir(_path + '\\img')
                file = file.split('.')
                file = file[0] + '.jpg'
                _img = open(file, 'wb')
                _img.write(_image)
                _img.close()
            except KeyError as e:
                print(e)
                continue
        os.chdir(_path + "\\audio")


if __name__ == "__main__":
    #func()
    _audio = File(os.getcwd()+'\\audio\\中华民谣.mp3')
    k = _audio.tags["TIT2"]
    print(k)
    print(_audio.tags["TPE1"])
    pass
