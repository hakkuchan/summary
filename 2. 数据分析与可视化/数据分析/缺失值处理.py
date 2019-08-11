import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
%matplotlib inline


""" 判断是否有缺失值数据： .isnull() 和 .notnull() """
df = pd.DataFrame({'value1':[12,33,45,23,np.nan,np.nan,66,54,np.nan,99,190],
                   'value2':['a','b','c','d','e',np.nan,np.nan,'f','g',np.nan,'g']})
print(df.isnull())   # isnull：缺失值为True，非缺失值为False
print(df.notnull())  # notnull：缺失值为False，非缺失值为True
print(df['value1'].notnull())  # 通过索引判断


""" 筛选非缺失值 """
df = df[df['value1'].notnull()]
df = df[df['value2'].notnull()]
print(df)


""" 删除缺失值 .dropna() """
''' (1) 删除有缺失值的样本 .dropna(axis=0) '''
df = pd.DataFrame({'value1':[12,33,np.nan,66,np.nan,99], 'value2':['a','b','c',np.nan,'f','g']})
df = df.dropna(axis=0)
print(df)
''' (2) 删除有缺失值的列 .dropna(axis=1) '''
df = pd.DataFrame({'value1':[12,33,15,66,22,99], 'value2':['a','b','c',np.nan,'f','g']})
df = df.dropna(axis=1)
print(df)


""" 填充缺失数据 .fillna() """
df = pd.DataFrame({'value1':[12,33,np.nan,66,np.nan,99], 'value2':['a','b','c',np.nan,'f','g']})
df.fillna(value='FILL', inplace=True)
print(df)


""" 替换缺失数据 .replace() """
df = pd.DataFrame({'value1':[12,33,np.nan,66,np.nan,99], 'value2':['a','b','c',np.nan,'f','g']})
df.replace(np.nan,'REPLACE',inplace = True) 
# 替换其它值也可以，比如把 'a' 换成 'b', 即：df.replace('a','b',inplace = True)
print(df)


""" 缺失值插补方法一: 均值/中位数/众数插补 """
df = pd.DataFrame({'value1':[12,33,np.nan,66,np.nan,99], 'value2':['a','b','c',np.nan,'f','g']})
ave = df['value1'].mean()     # 均值
med = df['value1'].median()   # 中位数
mod = df['value1'].mode()     # 众数
df['value1'].fillna(ave,inplace = True) # 用均值填补
print(f'均值：{ave}','\n', df)


""" 缺失值插补方法二: 临近值插补 """
df = pd.DataFrame({'value1':[12,33,np.nan,66,np.nan,99], 'value2':['a','b','c',np.nan,'f','g']})
df.fillna(method = 'ffill',inplace = True) # ffill：用前值插补；bfill 用后值插补
print(df)


""" 缺失值插补方法三: 拉格朗日插值法 """
''' 
(1) 什么是拉格朗日插值？
    假如有 n 个已知点，可以拟合出多项式 y = a0 + a1 * x + a2 * x^2 + ... + a(n-1) * x^(n-1)；
    用该多项式预测其它 x 的 y 值。
'''
x = [3, 6, 9, 14]
y = [10, 8, 6, 2]
print(lagrange(x,y)) # 输出多项式的形式(注意：3，2表示立方和平方)
print(lagrange(x,y)(10)) # 输出当 x = 10 是 y 的插值


''' (2) 用拉格朗日插值补充缺失值 '''
df = pd.DataFrame({'value1':[1,3,5,7,9,11,13,15], 'value2':[1,9,np.nan,49,81,np.nan,169,225]})
print('----------插值前----------')
print(df)
print()
# 一般来说，用 nan 值前后的少数点做插值即可，没必要用全部点，所以进行以下操作
x = df['value1'].tolist()
y = df['value2'].tolist()
out = []
for i in range(len(y)):
    if np.isnan(y[i]):   # 判断索引 i 处的 y 值是否是 nan，如果是，执行下列操作
        _x = [x[i-2], x[i-1], x[i+1], x[i+2]]  # 导出 nan 的前两个点的 x
        _y = [y[i-2], y[i-1], y[i+1], y[i+2]]  # 导出 nan 的前两个点的 y
        _z = lambda x, y, x_test: lagrange(x,y)(x_test) # 利用 nan 值前后 2 个非 nan 点计算插值
        out.append(_z(_x, _y, x[i]))
    else:
        out.append(y[i])
df['value2'] = out  # 用插值后的数据代替原数据
print('----------插值后----------')
print(df)