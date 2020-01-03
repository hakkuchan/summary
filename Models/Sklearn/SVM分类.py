import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn import model_selection

""" SVM分类主要包括：SVC、NuSVC、LinearSVC
    其中，SVC 和 NuSVC 差不多，区别仅在于对损失的度量方式不同，以及NuSVC可以使用参数来控制支持向量的个数
    LinearSVC不接受关键词 kernel，仅仅支持线性核函数，对线性不可分的数据不能使用
    下面的实例以SVC为代表：
"""

""" 1. 基本方法 """
X = [[-2.2,0], [-0.9,1.3], [0,2.1], [0,-1.8], [1,-1.1], [1.8,0]]
y = [0, 0, 0, 1, 1, 1]

clf = svm.SVC(kernel='linear')

clf.fit(X, y)  # 训练模型
print(clf.predict([[3, 3], [0, 10]]))  # 预测值
print(clf.support_vectors_)  # 获得支持向量
print(clf.support_)          # 获得支持向量的索引
print(clf.n_support_)        # 为每一个类别获得支持向量的数量


""" 2. 实例（Iris） """

''' 导入数据 '''
db = datasets.load_iris()
X = db.data
y = db.target

''' 构建模型 '''
models['SVC'] = svm.SVC(C=1.0,
                        kernel='rbf',
                        degree=3,
                        gamma='auto',
                        coef0=0.0,
                        shrinking=True,
                        probability=False,
                        tol=0.001,
                        cache_size=200,
                        class_weight=None,
                        verbose=False,
                        max_iter=-1,
                        decision_function_shape='ovr',
                        random_state=None)

''' 计算 '''
print('|{:>10s}|{:>10s}|'.format('Batch', 'Acc'))
kfold = model_selection.KFold(n_splits=10, random_state=1)
batch = 1
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    results = []
    model.fit(X_train,y_train)
    results.append(round(model.score(X_test, y_test), 4))
    print(f'|{batch:>10}|{results[0]:>10}|')
    batch += 1