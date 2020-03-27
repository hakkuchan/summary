""" 特征编码
    1. 标签转换
    2. 离散化
    3. 阈值转换
"""

import numpy as np
import pandas as pd
from sklearn import preprocessing

""" 1. 标签转换：把文本转化为数字 """
# Toy data 1: 一组字母类型 (也可以是 df['types'])
types = ['B','A','A','C','C','A','B']
# 转换为数字
new_y = preprocessing.LabelEncoder().fit_transform(types)
print(new_y) # >>> [1 0 0 2 2 0 1]  0,1,2 分别对应 A,B,C

# Toy data 2: 一组动物类型 (也可以是 df['types'])
types = ['mammals','birds','reptiles','mammals','birds','insects']
# 转换为数字
new_y = preprocessing.LabelEncoder().fit_transform(types)
print(new_y) # >>> [2 0 3 2 0 1] 顺序是首字母排序：birds(0), insects(1), mammals(2), reptiles(3)


""" 2. 离散化
    · 目的：连续数据变换成分类属性
    · 方法：把连续数据的取值范围划分为离散化的区间，再用不同符号代表每个子区间
"""
# Toy data: 一组人员年龄数据 (也可以是 df['ages'])
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
# 将年龄设置为 4个区间：18-25、26-35、36-60、60-100
bins = [18,25,35,60,100]
# 数据离散化
cats = pd.cut(ages, bins)
print(cats.codes) # >>> [0 0 0 1 0 0 2 1 3 2 2 1] 0-3 分别 4个区间
# 按照区间计数
print(pd.value_counts(cats))
# 设置区间名称
names=['Youth','YoungAdult','MiddleAged','Senior']
print(pd.cut(ages, bins, labels=names))


""" 3. 阈值转换
    · 比如大于阈值设为1，小于阈值设为0
	· 用于形成bool型新特征
"""
Y = np.array([-1, -2, 0, 5, 10]).reshape(-1,1)
newY = preprocessing.Binarizer(threshold=1.5).fit_transform(Y)
print('after Binarizer: \n', newY, '\n')
