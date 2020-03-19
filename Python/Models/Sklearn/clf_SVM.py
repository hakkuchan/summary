""" 支持向量机

    · 思想：基于训练集的数据，寻找一个分界线(点、面、超平面) 把不同类样本分开
      针对测试集数据，根据其位置预测类别
    
    · 核函数：用于把X转换为高维数据，在建立SVM模型
    
    · SVM分类：SVC、NuSVC、LinearSVC
      其中，SVC 和 NuSVC 差不多，区别仅在于对损失的度量方式不同，以及NuSVC可以使用参数来控制支持向量的个数
       LinearSVC不接受关键词 kernel，仅仅支持线性核函数，对线性不可分的数据不能使用
    
    · 下例以SVC为代表：
"""


import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn import model_selection

""" 1. 基本方法 """
X = [[-2.2,0], [-0.9,1.3], [0,2.1], [0,-1.8], [1,-1.1], [1.8,0]]
y = [0, 0, 0, 1, 1, 1]

clf = svm.SVC(kernel='linear')
clf.fit(X, y)  # 训练模型
print(clf.predict([[3, 3], [0, 10]]))  # 预测值
print(clf.support_vectors_)  # 获得支持向量
print(clf.support_)          # 获得支持向量的索引
print(clf.n_support_)        # 为每一个类别获得支持向量的数量


""" 2. 实例 """
# Data: Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
# Modeling
model = svm.SVC(C=1.0,
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
                random_state=1)
# Train & Test
kfold = model_selection.KFold(n_splits=10, random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Accuracy of SVC: {result.mean()*100:.2f}%')