import numpy as np
from sklearn import preprocessing

""" 数据范围调整包括：
    1）调整数据尺度；
    2）正态化数据；
    3）标准化数据；
    4）阈值转换
    ……
    
    通用格式为： newX = preprocessing.方法(参数).fit_transform(X) 
"""

# Toy data：3个样本，4个特征
X = np.array([[1,1,1,1],
              [2,2,2,2],
              [3,3,3,3]]).astype('float')
print('X:\n', X, '\n')


''' 1. 标准化 '''
newX = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(X)
print('after MinMaxScaler: \n', newX, '\n')


''' 2. 正态分布化 '''
newX = preprocessing.StandardScaler().fit_transform(X)
print('after StandardScaler: \n', newX, '\n')
newX = preprocessing.scale(X)
print('after scale: \n', newX, '\n')


''' 3. 归一化（适用于稀疏数据，即有很多0的数据) '''
newX = preprocessing.Normalizer(norm='l1').fit_transform(X)
print('after L1 normalized: \n', newX, '\n')
newX = preprocessing.Normalizer(norm='l2').fit_transform(X)
print('after L2 normalized: \n', newX, '\n')


''' 4. 阈值转换（比如大于阈值设为1，小于阈值设为0，用于形成bool型新特征) '''
newX = preprocessing.Binarizer(threshold=1.5).fit_transform(X)
print('after Binarizer: \n', newX, '\n')