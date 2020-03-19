""" K Nearest Neighbors Classifier：把未知样本预测为其K近邻中出现的最多的类别 """

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import neighbors
from sklearn import model_selection

# Data：Iris
X = datasets.load_iris().data
y = datasets.load_iris().target

# Modeling
model = neighbors.KNeighborsClassifier(n_neighbors=5, # 指定 k值
                                       weights='uniform',  # 指定投票的权重类型，uniform指权重相同
                                       algorithm='brute',  # 指点最近邻算法
                                       leaf_size=30,  # 当最近算法为 BallTree 或 KDTree 时，该参数指定叶节点规模
                                       metric='minkowski', # 指定距离度量
                                       p=2, # 指定距离度量的指数，对于Minkowski度量，p=1表示曼哈顿距离，p=2表示欧拉距离
                                       n_jobs=-1 # 指定并行数，-1表示派发任务到所有可用CPU核
                                      )

# Train & Test
results = model_selection.cross_val_score(model, X, y, cv=10, scoring='accuracy')
print(f'Accuracy of KNN : {results.mean()*100:.2f}%')