""" 目录
     |
     |—— 1. 缺失值判别: isnull() 和 notnull()
     |
     |—— 2. 缺失值处理
         |
         |—— 2.1 删除
         |
         |—— 2.2 填充
         |
         |—— 2.3 替换
         |
         |—— 2.4 插值：均值/中位数/众数、前/后值、拉格朗日法
                 (注：插值方法还有很多，如多重插补、压缩感知等，用时再查)
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
%matplotlib inline


""" 1. 缺失值判别: isnull() 和 notnull() """
df = pd.DataFrame({'value1':[1, 2, np.nan, 3, np.nan], 'value2':['a','b','c', np.nan, np.nan]})
# isnull：缺失值为True，非缺失值为False
print(df.isnull())
# notnull：缺失值为False，非缺失值为True
print(df.notnull())
# 加索引
print(df['value1'].notnull())



""" 2. 缺失值处理 """

''' 2.1 删除 dropna() '''
# 删除含有缺失值的样本
df = pd.DataFrame({'value1':[1, 2, np.nan, 3, np.nan], 'value2':['a','b','c', np.nan, np.nan]})
df = df.dropna(axis=0)
print(df)
# 删除含有缺失值的特征 '''
df = pd.DataFrame({'value1':[1,2,3], 'value2':['a','b',np.nan]})
df = df.dropna(axis=1)
print(df)

''' 2.2 填充 fillna() '''
df = pd.DataFrame({'value1':[1,2,np.nan,3], 'value2':['a','b','c',np.nan]})
df.fillna(value='FILL', inplace=True)
print(df)

''' 2.3 替换 replace() '''
df = pd.DataFrame({'value1':[1,2,np.nan,3], 'value2':['a',np.nan,'b','c']})
df.replace(np.nan,'REPLACE',inplace = True) 
# 替换其它值也可以，比如把 'a' 换成 'b', 即：df.replace('a','b',inplace = True)
print(df)

''' 2.4 插值 '''

# (1) 利用 均值/中位数/众数 插值
df = pd.DataFrame({'value1':[1,2,np.nan,3,np.nan,4], 'value2':['a','b','c',np.nan,'f','g']})
ave = df['value1'].mean()     # 均值
med = df['value1'].median()   # 中位数
mod = df['value1'].mode()     # 众数
df['value1'].fillna(ave, inplace = True) # 用均值填补
print(f'均值：{ave}','\n', df)

# (2) 利用前/后值插值
df = pd.DataFrame({'value1':[12,33,np.nan,66,np.nan,99], 'value2':['a','b','c',np.nan,'f','g']})
df.fillna(method = 'ffill',inplace = True) # ffill：用前值插补；bfill 用后值插补
print(df)

# (3) 拉格朗日插值
# a. 原理：假如有 n 个已知点，可以拟合出多项式 y= a0 + a1*x + ... + a(n-1)*x^(n-1)，以此计算缺失值
# b. 拉格朗日函数示例：
x = [3, 6, 9, 14]
y = [10, 8, 6, 2]
print(lagrange(x,y)) # 输出多项式的形式(注意：3，2表示立方和平方)
print(lagrange(x,y)(10)) # 输出当 x = 10 是 y 的插值
# c. 拉格朗日插法补充缺失值
df = pd.DataFrame({'value1':[1,3,5,7,9,11,13,15], 'value2':[1,9,np.nan,49,81,np.nan,169,225]})
print('插值前:\n', df)
x = df['value1'].tolist() # 生成 X 轴数据
y = df['value2'].tolist() # 生成 Y 轴数据
out = []
for i in range(len(y)):
    # 一般来说，用 nan 值前后的少数点做插值即可，没必要用全部点，所以进行以下操作
    if np.isnan(y[i]): # 判断索引 i 行的 y 值是否是 nan
        x_fit = [x[i-2], x[i-1], x[i+1], x[i+2]]  # nan前、后两个样本的 x
        y_fit = [y[i-2], y[i-1], y[i+1], y[i+2]]  # nan前、后两个样本的 y
        out.append(lagrange(x_fit, y_fit)(x[i]))
    else:
        out.append(y[i])
df['value2'] = out  # 用插值后的数据代替原数据
print('插值后:\n', df)