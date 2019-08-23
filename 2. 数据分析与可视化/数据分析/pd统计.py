import numpy as np
import pandas as pd

''' (1) 内置方法 '''
df = pd.DataFrame({'x':np.arange(10), 'y':np.arange(91,101), 'z':np.random.random(10)})
print(df.describe()) # 输出 8 个主要统计量：count, mean, std, min, 25%, 50%, 75%, max 
print(df.count())    # 统计非 NaN 值的数量
print(df.min())      # 最小值
print(df.max())      # 最大值
print(df.mean())     # 平均值
print(df.mean(skipna=False)) # skipna参数：是否忽略 NaN，默认True，如 False，有 NaN 的列统计结果仍为NaN
print(df.std())      # 标准差
print(df.var())      # 方差
print(df.skew())     # 偏度（数据的不对称程度）
print(df.kurt())     # 峰度（正态分布的数据的峰度值为 0；峰度值越显著偏离 0，数据越不服从正态分布。）
print(df.median())   # 中位数，50%分位数
print(df.quantile(q=0.75))   # 分位数，参数 q 确定位置

df = pd.DataFrame({'x':[1,2,3,3,4], 'y':[11,11,12,11,13], 'z':[22,12,22,11,22]})
print(df.mode())    # 众数

df = pd.DataFrame({'x':np.arange(10), 'y':np.arange(91,101), 'z':np.random.random(10)})
print(df.corr(method='pearson'))  # 求各个 x, y, z 两两之间的 pearson 相关系数
print(df.corr(method='kendall'))  # 求各个 x, y, z 两两之间的 kendall 相关系数
print(df.corr(method='pearson'))  # 求各个 x, y, z 两两之间的 spearman 相关系数


''' （2）按行列或列名统计（以 mean 为例） '''
df = pd.DataFrame({'x':np.arange(10), 'y':np.arange(91,101), 'z':np.random.random(10)})
print(df.mean(axis=0))  # axis=0 求每列数据的平均
print(df.mean(axis=1))  # axis=1 求每行数据的平均
print(df['x'].mean())   # 按列名求平均
print(df[['x','z']].mean())   # 按列名求平均


''' (3) 分组统计 '''
df = pd.DataFrame({'name' : ['A', 'B', 'A', 'B','A', 'A', 'A', 'B'],
                   'var1' : ['1d', '2d', '1d', '3d', '2d', '2d', '1d', '3d'],
                   'var2' : np.random.randn(8),
                   'var3' : np.random.randn(8)})
print(df)
print(df.groupby(['name']).get_group('A'))  # .get_group()提取满足条件的组，注意，这种方法不如 df[df['name']=='A'] 方便
print(df.groupby('name').mean())            # 以 name 分组求 mean (基础统计里的函数可以直接套用过来)
print(df.groupby(['name','var1']).mean())
print(df.groupby(['name'])['var3'].mean())  # 以 name 分组，算 var3 的平均值

''' (4) .apply(函数)，对表格中的元素依次进行计算，并输出结果 '''
df = pd.DataFrame({'x':np.arange(1,3), 'y':np.arange(11,13)})
print(df.apply(lambda x: x**2))
print(df['y'].apply(lambda x: x**2))

# 与分组统计结合
df = pd.DataFrame({'key':['A','B','A','B','A'], 'data1':np.random.rand(5), 'data2':np.random.rand(5)})
print(df.groupby('key').apply(lambda x: x.describe())) # apply直接运行其中的函数
# 等价于
def fn(d):
    return(d.describe())
print(df.groupby('key').apply(fn))

''' (5) 透视表：pivot_table '''
# values：要聚合的列或列的列表
# index：数据透视表的index，从原数据的列中筛选
# columns：数据透视表的columns，从原数据的列中筛选
# aggfunc：用于指定函数，支持 numpy 中的 ufunc 函数，默认为 np.mean。
date = ['2017-5-1','2017-5-2','2017-5-3'] * 3
rng = pd.to_datetime(date)
df = pd.DataFrame({'date':rng, 'key':list('abcabcabc'), 'values':np.random.rand(9)*10})
print(df)
print(pd.pivot_table(df, values='values', index='date', columns='key', aggfunc=np.mean)) # 统计不同[date,key]下values的mean
print(pd.pivot_table(df, values='values', index = ['date','key'], aggfunc=np.mean))