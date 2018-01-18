import os
import numpy as np
from librosa import feature, load, effects


def extraction(file, reset=False):
    path = os.path.abspath('.')
    os.chdir(path + '/static/music-features')
    # 判断歌曲特征是否已经提取
    if not reset:
        file_npy = os.path.splitext(file)[0] + ".npy"
        if os.path.exists(file_npy):
            os.chdir(path)
            return
    os.chdir(path + '/static/audio')
    if os.path.exists(file) and os.path.splitext(file)[1] == ".mp3":
        y, sr = load(file)
        # mfcc系数 20 维
        mfccs = feature.mfcc(y, sr)
        mfccs_mean = np.mean(mfccs, axis=1)
        mfccs_var = np.var(mfccs, axis=1)
        # Tonal centroid features for each frame. 6维
        y = effects.harmonic(y)
        tonnetz = feature.tonnetz(y=y, sr=sr)
        tonnetz_mean = np.mean(tonnetz, axis=1)
        tonnetz_var = np.var(tonnetz, axis=1)
        features = np.concatenate((mfccs_mean, mfccs_var, tonnetz_mean, tonnetz_var))
        os.chdir(path + '/static/music-features')
        _file_name = os.path.splitext(file)[0]
        np.save(_file_name, features)
    else:
        print('未找到指定文件')
    os.chdir(path)


def extraction_all(path=None):
    if not path:
        path = os.getcwd()
    for music in os.listdir(path + "/static/audio"):
        extraction(music)


# 从audio文件夹提取音乐对应的特征以.npy格式保存到music-features文件夹
if __name__ == "__main__":
    extraction_all()
