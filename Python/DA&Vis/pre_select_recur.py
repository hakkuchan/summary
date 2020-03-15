""" 循环式特征消除 (Recurrent Feature Elimination, RFE)
    · 设定一个学习器(比如线性模型)
      → 计算每个特征在学习器中的权重
      → 剔除权重最小的特征，计算剩余特征在学习器中的权重
      → 直至所有特征被剔除
    · 越后被剔除的特征，重要性越大
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import feature_selection

''' 1. 典型RFE '''
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# Data: Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
# 设定学习器
model = LinearDiscriminantAnalysis()
# 设定 RFE (选出2个最重要的特征)
rfe = feature_selection.RFE(estimator=model,n_features_to_select=2)
rfe.fit(X,y)
# 结果
print('所选特征的个数:', rfe.n_features_)
print('所有特征重要性排序:', rfe.ranking_)
print('所选特征的列:', rfe.support_)


''' 2. RFECV：执行交叉验证寻找最有特征，不需要人为指定特征个数 '''
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# Data: Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
# 设定学习器
model = LinearDiscriminantAnalysis()
# 设定 RFE (选出2个最重要的特征)
rfecv = feature_selection.RFECV(estimator=model, cv=10)
rfecv.fit(X,y)
# 结果
print('所选特征的个数:', rfecv.n_features_)
print('所有特征重要性排序:', rfecv.ranking_)
print('所选特征的列:', rfecv.support_)
print('交叉验证性能得分:', rfecv.grid_scores_)