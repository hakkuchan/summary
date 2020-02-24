import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import neighbors
from sklearn import model_selection

''' 准备数据 '''
db = datasets.load_iris()
X = db.data
y = db.target

''' 建立模型 '''
model = neighbors.KNeighborsClassifier(
                                       n_neighbors=5, # 指定k值
                                       weights='uniform',  # 指定投票的权重类型，uniform指权重相同
                                       algorithm='brute',  # 指点最近邻算法
                                       leaf_size=30,  # 当最近算法为 BallTree 或 KDTree 时，该参数指定叶节点规模
                                       metric='minkowski', # 指定距离度量
                                       p=2, # 指定距离度量的指数，对于Minkowski度量，p=1表示曼哈顿距离，p=2表示欧拉距离
                                       n_jobs=-1 # 指定并行数，-1表示派发任务到所有可用CPU核
                                      )

''' 学习及预测 '''
print('|{:>10s}|{:>10s}|'.format('Batch', 'KNN Acc'))
kfold = model_selection.KFold(n_splits=10, random_state=1)
batch = 1
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    results = []
    model.fit(X_train,y_train)
    results.append(round(model.score(X_test, y_test),4))
    print('|{:>10.0f}|{:>10.4f}|'.format(batch,results[0]))
    batch += 1