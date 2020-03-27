""" · 目录
    |
    |—— 1. 概述
    |
    |—— 2. 创建：字典、数组、标量
    |
    |—— 3. 操作
        |
        |—— 3.1 索引：位置、切片、标签、布尔
        |
        |—— 3.2 查看：head、tail
        |
        |—— 3.3 修改
        |
        |—— 3.4 删除
        |
        |—— 3.5 增加
        |
        |—— 3.6 拼接
        |
        |—— 3.7 重置索引
        |
        |—— 3.8 对齐
        |
        |—— 3.9 name/rename
"""

import numpy as np
import pandas as pd

""" 1. 概述 
    series 是带有标签的一维数组
    可以保存任何数据类型（整数，字符串，浮点数，Python对象等）
    轴标签统称为索引，从0开始
    当只看 series 的值的时候，就是一个一维数组
"""
s = pd.Series(np.random.randint(0,3,5))
print(s)         # 查看series
print(type(s))   # 查看series类型
print(s.index)   # 查看series索引
print(s.values)  # 查看series值



""" 2. 创建 """
# (1) 由字典创建
print(pd.Series({'a':1 ,'b':2 , 'c':3, '4':4, '5':5}))
# (2) 由数组创建
print(pd.Series(np.random.randint(0, 3, 5)))
print(pd.Series(np.random.randint(0, 3, 5), index = ['a','b','c','d','e'], dtype = np.object)) # 更换索引和数据类型
# (3) 由标量创建
print(pd.Series([10,11,12,13], index = range(4)))



""" 3. 操作 """

''' 3.1 索引 '''
s = pd.Series(np.random.random(5), index = ['a','b','c','d','e'])
# (1) 位置索引
print(s[1])
# (2) 标签索引
print(s['c'])
# (3) 切片索引
print(s[1::])
print(s[2:-1])
print(s[1:4], s[4])      
print(s['a':'c'],s['c'])
# (4) 布尔索引
s = pd.Series(np.random.rand(4)*100)
s[4] = None       # 添加一个空值
print(s)
# a) 按条件筛选
bs1 = s > 50      # 判断每个元素是否 > 50
print(bs1)
print(s[s > 50])  # 输出满足条件的值
# b) 是否为null
bs2 = s.isnull()  # 判断每个元素是否为空值
print(bs2)        # 是 null 的话返回 True
bs3 = s.notnull() # 判断每个元素是否不是空值
print(bs3)        # 不是 null 的话返回 True
print(s[bs3])     # 输出满足条件的值

''' 3.2 查看 '''
s = pd.Series(np.random.rand(50))
print(s.head(3))  # 查看头部数据
print(s.tail())   # 查看尾部数据, 默认查看5条

''' 3.3 修改 '''
s = pd.Series(np.random.rand(3), index = list('abc'))
print(s)
s[2] = 100
print(s)
s['a'] = 100
print(s)
s['a','c'] = 200
print(s)

''' 3.4 删除 '''
s = pd.Series(np.random.rand(5), index = list('abcde'))
s1 = s.drop('a')
s2 = s.drop(['c','e'])
print(s)
print(s1)
print(s2)

''' 3.5 增加 '''
s1 = pd.Series(np.random.rand(3), index = list('abc'))
print(s1)
s2 = pd.Series(np.random.rand(2), index = list('de'))
print(s2)
s3 = s1.append(s2)
print(s3)

''' 3.6 拼接 '''
s1 = pd.Series([1,2,3])
s2 = pd.Series([2,3,4])
s3 = pd.Series([1,2,3], index = ['a','c','f'])
s4 = pd.Series([2,3,4], index = ['b','e','d'])
print(pd.concat([s1,s2]))    # 默认axis=0，行 + 行
print(pd.concat([s3,s4], axis=1, sort=True))  # axis=1,列+列，成为一个Dataframe

''' 3.7 重置索引 '''
s = pd.Series(np.random.rand(3), index = ['a','b','c'])
s1 = s.reindex(['d','c','b','a']) # 如果当前索引不存在，则引入缺失值 NaN
print(s)
print(s1)
s2 = s.reindex(['c','b','a','d'], fill_value = 0) # fill_value参数：填充缺失值的值
print(s2)

''' 3.8 对齐 '''
s1 = pd.Series(np.random.rand(3), index = ['Jack','Marry','Tom'])
s2 = pd.Series(np.random.rand(3), index = ['Wang','Jack','Marry'])
print(s1+s2) # series会根据标签自动对齐, 空值和任何值计算结果为空值

''' 3.9 name/rename '''
s1 = pd.Series(np.random.randn(5))
s2 = pd.Series(np.random.randn(5), name = 'test')
s3 = s2.rename('hehehe')
print(s1.name, s2.name, s3.name)