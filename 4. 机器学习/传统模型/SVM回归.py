import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn import model_selection


""" SVM回归主要包括：SVR、NuSVR、LinearSVR
    其中，SVR 和 NuSVR 差不多
    LinearSVR 不接受关键词 kernel，仅仅支持线性核函数
    主要以SVR为例：
"""


""" 1. 简单示例 """
X = [[0,0], [1,1], [2,2]]
y = [0.5, 1.5, 2.5]
regr = svm.SVR(gamma='auto')
regr.fit(X, y)
print(regr.predict([[1, 1], [1.5, 1.5]]))    # 预测值


""" 2. 实例 (diabetes) """

''' 导入数据 (diabetes) '''
db = datasets.load_diabetes()
X = db.data
y = db.target 

''' 构建模型 '''
regr = svm.SVR(kernel='poly',
               degree=3,
               gamma='auto',
               coef0=0.0,
               tol=1e-3,
               C=1.0,
               epsilon=0.1,
               cache_size=1.0,
               verbose=False,
               max_iter=-1)

''' 计算 '''
print('|{:>10s}|{:>10s}|'.format('Batch', 'Acc'))
kfold = model_selection.KFold(n_splits=10, random_state=1)
batch = 1
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    results = []
    regr.fit(X_train,y_train)
    results.append(round(regr.score(X_test, y_test), 4))
    print(f'|{batch:>10}|{results[0]:>10}|')
    batch += 1