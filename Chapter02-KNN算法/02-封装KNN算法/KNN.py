# 对knn算法进行封装

import numpy as np
from math import sqrt
from collections import Counter

# k: k值
# X_train: 训练数据集
# y_train: 训练数据集标签
# x: 预测点

def KNN_classify(k, X_train, y_train, x):
    assert 1 <= k <= X_train.shape[0], "k must be valid"
    assert X_train.shape[0] == y_train.shape[0], \
        "the size of X_train must equal to the size of y_train"
    assert X_train.shape[1] == x.shape[0], \
        "the feature number of x must be equal to X_train"

    distance = [sqrt(np.sum((x_train) - x) ** 2) for x_train in X_train]
    nearest = np.argsort(distance)

    