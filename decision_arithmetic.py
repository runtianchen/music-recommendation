#
# 采用随lg算法 做决策
#
# ----------------------------------------
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_iris
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from mySqlite import query_db, SQL_SELECT_AUDIOS
from scipy import interp
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.metrics import roc_curve, auc, accuracy_score, recall_score, precision_score, f1_score
from sklearn.cross_validation import StratifiedKFold


def random_recommend():
    sql = SQL_SELECT_AUDIOS
    flag, list_recomm = query_db(sql)
    return random.sample(list_recomm, k=10)


if __name__ == "__main__":
    # pre_musics = []
    # pre_target = []
    # for i in dbConn.select_preferences('刘一'):
    #     temp = np.load('./static/music-features/' + i.musicname + '.npy')
    #     pre_musics.append(temp)
    #     pre_target.append(1)
    # rf = RandomForestRegressor()  # 这里使用了默认的参数设置
    # rf.fit(pre_musics, pre_target)  # 进行模型的训练
    # instance = np.load('./static/music-features/沧海一声笑.npy')
    # print('instance 1 prediction；', rf.predict(instance.reshape((1, -1))))
    path_lx = r'D:\戏曲\audios\京剧\\'
    for file in os.listdir(path_lx):
        temp = np.load(path_lx + file)
        temp = np.append(temp, 0)
        try:
            instance = np.concatenate((instance, temp))
        except:
            instance = temp
    path_cj = r'D:\戏曲\audios\昆曲\\'
    for file in os.listdir(path_cj):
        temp = np.load(path_cj + file)
        temp = np.append(temp, 1)
        try:
            instance = np.concatenate((instance, temp))
        except:
            instance = temp
    path_qin = r'D:\戏曲\audios\评剧\\'
    for file in os.listdir(path_qin):
        temp = np.load(path_qin + file)
        temp = np.append(temp, 1)
        try:
            instance = np.concatenate((instance, temp))
        except:
            instance = temp
    path_qin = r'D:\戏曲\audios\越剧\\'
    for file in os.listdir(path_qin):
        temp = np.load(path_qin + file)
        temp = np.append(temp, 1)
        try:
            instance = np.concatenate((instance, temp))
        except:
            instance = temp
    path_qin = r'D:\戏曲\audios\黄梅戏\\'
    for file in os.listdir(path_qin):
        temp = np.load(path_qin + file)
        temp = np.append(temp, 1)
        try:
            instance = np.concatenate((instance, temp))
        except:
            instance = temp
    path_qin = r'D:\戏曲\audios\川剧\\'
    for file in os.listdir(path_qin):
        temp = np.load(path_qin + file)
        temp = np.append(temp, 1)
        try:
            instance = np.concatenate((instance, temp))
        except:
            instance = temp
    path_qin = r'D:\戏曲\audios\秦腔\\'
    for file in os.listdir(path_qin):
        temp = np.load(path_qin + file)
        temp = np.append(temp, 1)
        try:
            instance = np.concatenate((instance, temp))
        except:
            instance = temp
    instance = np.reshape(instance, (-1, 53))
    instance_feature = instance[:, :52]
    instance_label = instance[:, 52]

    # feature_train, feature_test, label_train, label_test = train_test_split(instance_feature, instance_label,
    #                                                                         test_size=0.2,
    #                                                                         random_state=42)

    # Run classifier with cross-validation and plot ROC curves
    # 使用6折交叉验证，并且画ROC曲线
    cv = StratifiedKFold(instance_label, n_folds=6)
    lg = LogisticRegression()

    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = []

    for i, (train, test) in enumerate(cv):
        lg.fit(instance_feature[train], instance_label[train])
        predict_test_proba = lg.predict_proba(instance_feature[test])
        predict_test = lg.predict(instance_feature[test])
        fpr, tpr, thresholds = roc_curve(instance_label[test], predict_test_proba[:, 0], pos_label=0)
        print(instance_label[test])
        print(predict_test)
        print(fpr, tpr)
        roc_auc = auc(fpr, tpr)
        # 画图，只需要plt.plot(fpr,tpr),变量roc_auc只是记录auc的值，通过auc()函数能计算出来
        plt.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
        # 对mean_tpr在mean_fpr处进行插值，通过scipy包调用interp()函数
        mean_tpr += interp(mean_fpr, fpr, tpr)
    # 画对角线
    plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

    mean_tpr[0] = 0.0  # 初始处为0
    mean_tpr /= len(cv)  # 在mean_fpr100个点，每个点处插值插值多次取平均
    mean_tpr[-1] = 1.0  # 坐标最后一个点为（1,1）
    mean_auc = auc(mean_fpr, mean_tpr)  # 计算平均AUC值
    # 画平均ROC曲线
    # print mean_fpr,len(mean_fpr)
    # print mean_tpr
    plt.plot(mean_fpr, mean_tpr, 'k--',
             label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    # plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()
