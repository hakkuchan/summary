""" SVM回归:
    
    · 基本思想：学习一个函数 f(x) = w1*x1 + w2*x2 + ... + b
      显然，这个函数在SVM分类时，起分界限的作用，
      而在SVM回归时，这个函数就是回归模型本身
      该模型周围存在由支持向量界定的范围，预测值落入该范围内，都被认为是正确预测(不计算损失)

    · SVR 主要包括：SVR、NuSVR、LinearSVR
      其中，SVR 和 NuSVR 差不多
      LinearSVR 不接受关键词 kernel，仅仅支持线性核函数
    
    · 以SVR为例：
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn import model_selection, metrics


''' Example 1 '''
X = [[0,0], [1,1], [2,2]]
y = [0.5, 1.5, 2.5]
regr = svm.SVR(kernel='linear', gamma='auto')
regr.fit(X, y)
print('Weights:', regr.coef_)   # >>> [[0.45 0.45]]
print('Bias:', regr.intercept_) # >>> [0.6]
print(regr.predict([[1, 1], [1.5, 1.5]])) # >>> [1.5  1.95]


''' Example 2 '''
# Data：Boston housing price
X = datasets.load_boston().data
y = datasets.load_boston().target 
# modeling
regr = svm.SVR(kernel='rbf',
               degree=3,
               gamma='auto',
               coef0=0.0,
               tol=1e-3,
               C=1.0,
               epsilon=0.1,
               cache_size=1.0,
               verbose=False,
               max_iter=-1)
# Train & Test
mse = metrics.make_scorer(metrics.mean_squared_error)
results = model_selection.cross_val_score(regr, X, y, cv=10, scoring=mse)
print(f'RMSE of SVR : {results.mean()**0.5:.2f}')