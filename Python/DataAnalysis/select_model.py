""" 嵌入式特征选择：
    · 使用一个含有 coef_ 或 feature_importance_ 属性的学习器进行特征选择
      当某特征的 coef_ 或 feature_importance_ 低于阈值时，该特征被移除
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import feature_selection
from sklearn.ensemble import ExtraTreesClassifier

# Data：Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
# 设定学习器
model = ExtraTreesClassifier(n_estimators=10)
# 选择器
selector = feature_selection.SelectFromModel(estimator=model, 
                                             threshold='mean') # 注：还可设为'median'或任意值 
selector.fit(X, y)
# 生成 newX
newX = selector.transform(X)
# 结果
print('特征重要性:', model.fit(X,y).feature_importances_)
print('阈值:', selector.threshold_)
print('特征个数:', newX.shape[1])