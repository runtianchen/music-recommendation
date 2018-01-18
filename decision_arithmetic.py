#
# 采用随机森林算法 做决策
#
# ----------------------------------------
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_iris
import numpy as np
import dbConn

if __name__ == "__main__":
    pre_musics = []
    pre_target = []
    for i in dbConn.select_preferences('刘一'):
        temp = np.load('./static/music-features/' + i.musicname + '.npy')
        pre_musics.append(temp)
        pre_target.append(1)
    rf = RandomForestRegressor()  # 这里使用了默认的参数设置
    rf.fit(pre_musics, pre_target)  # 进行模型的训练
    instance = np.load('./static/music-features/沧海一声笑.npy')
    print('instance 1 prediction；', rf.predict(instance.reshape((1, -1))))
