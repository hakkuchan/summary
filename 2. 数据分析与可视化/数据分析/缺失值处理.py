import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
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

