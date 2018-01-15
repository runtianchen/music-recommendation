#
# 采用随机森林算法 做决策
#
# ----------------------------------------
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_iris
import numpy as np

if __name__ == "__main__":
    iris = load_iris()
    # print iris#iris的４个属性是：萼片宽度　萼片长度　花瓣宽度　花瓣长度　标签是花的种类：setosa versicolour virginica
    print(iris['target'].shape)
    rf = RandomForestRegressor()  # 这里使用了默认的参数设置
    rf.fit(iris.data[:150], iris.target[:150])  # 进行模型的训练
    #
    # 随机挑选两个预测不相同的样本
    instance = iris.data[[100, 109]]
    print(instance)
    print('instance 0 prediction；', rf.predict(instance[0].reshape((1, -1))))
    print('instance 1 prediction；', rf.predict(instance[1].reshape((1, -1))))
    print(iris.target[100], iris.target[109])
