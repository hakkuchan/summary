""" 过滤式特征选择：以某一统计指标作为阈值，筛选特征 """

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import feature_selection

''' 1. VarianceThreshold: 只保留方差大于阈值的特征 '''
# Toy data: 3个样本，4个属性
X = np.array([[1,  5, 10, 100],
              [2, 10, 20, 200],
              [3, 15, 30, 300]])
# VarianceThreshold
newX = feature_selection.VarianceThreshold(threshold=50).fit_transform(X)
print('after VarianceThreshold:\n', newX, '\n')


''' 2. 单变量特征选择：计算每个特征的统计指标，然后根据指标选取特征
    · SelectKBest 保留统计指标得分最高的k的特征 
    · SelectPercentile 保留统计指标得分最高的、前百分之k的特征
    · 两者用法相似，下面以 SelectKBest 为例
'''
# Toy data: 3个样本，5个属性
X = np.array([[1,2,3,4,5], [5,4,3,2,1], [6,6,6,6,6]])
y = np.array([0,1,0])
# 内置统计指标
score = feature_selection.f_regression # 基于线性回归分析统计指标
score = feature_selection.f_classif  # 方差
score = feature_selection.chi2 # 卡方统计量
# 特征选择
selector = feature_selection.SelectKBest(score_func=score, k=3)
selector.fit(X, y)
# 查看得分
print('scores: \n', selector.scores_, '\n')
# 转换
print('after selection: \n', selector.fit_transform(X,y), '\n')