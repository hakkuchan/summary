import numpy as np
from sklearn import preprocessing

""" 数据预处理包括：1）调整数据尺度；2）正态化数据；3）标准化数据；4）阈值转换 ……"""
""" 通用格式为： newX = preprocessing.模块名(参数).fit_transform(X) """

X = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]).astype('float')


""" 调整数据纵向尺度 """
newX = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(X)   # 设定范围


""" 调节数据为服从正态分布 """
newX = preprocessing.StandardScaler().fit_transform(X)
newX = preprocessing.scale(X)


""" 归一化数据（适用于稀疏数据，即有很多0的数据）"""
newX = preprocessing.Normalizer(norm='l1').fit_transform(X)    # 归一化数据
newX = preprocessing.Normalizer(norm='l2').fit_transform(X)


""" 阈值转换（比如大于阈值设为1，小于阈值设为0）,用于形成新特征 """
newX = preprocessing.Binarizer(threshold=1.5).fit_transform(X)