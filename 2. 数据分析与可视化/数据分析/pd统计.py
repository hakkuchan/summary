import numpy as np
import pandas as pd

''' (1) 基础操作 '''
df = pd.DataFrame({'x':np.arange(10), 'y':np.arange(91,101)})
print(df)
print(df.count())    # 统计非 NaN 值的数量
print(df.min())      # 统计最小值
print(df['y'].max()) # 特定列的最大值

print(df.sum())        # sum求和
print(df.sum(axis=1))  # axis参数: 规定按行还是按列
print(df.mean())       # mean求平均值\n')
print(df.mean(skipna=False)) # skipna参数：是否忽略NaN，默认True，如False，有NaN的列统计结果仍为NaN
print(df.std())    # 求标准差
print(df.var())    # 求方差

print(df.median()) # median求算数中位数，50%分位数
print(df.quantile(q=0.75))   # quantile统计分位数，参数q确定位置

print(df.skew())   # 求样本的偏度
print(df.kurt())   # 求样本的峰度

df = pd.DataFrame({'x':np.random.random(10), 'y':np.random.random(10), 'z':np.random.random(10)})
df.corr(method='pearson')  # 求各个 x, y, z 两两之间的pearson相关系数
df.corr(method='pearson')  # 求各个 x, y, z 两两之间的spearman相关系数
df.corr(method='kendall')  # 求各个 x, y, z 两两之间的kendall相关系数

s = pd.Series(list('asdvasdcfgg'))
print(pd.Series(s.unique())) # 统计值的种类：.unique()

s = pd.Series(np.arange(10,15))
df = pd.DataFrame({'key1':list('asdcbvasd'),'key2':np.arange(4,13)})
print(s, s.isin([5,14]))          # 成员资格:isin(); s 的值为 [5,14]
print(df.isin(['a','bc','10',8])) # df 的值为 ['a','bc','10',8]

''' (2) 分组统计 '''
df = pd.DataFrame({'name' : ['A', 'B', 'A', 'B','A', 'A', 'A', 'B'],
                   'var1' : ['1d', '2d', '1d', '3d', '2d', '2d', '1d', '3d'],
                   'var2' : np.random.randn(8),
                   'var3' : np.random.randn(8)})
print(df) 
print(df.groupby(['name']).get_group('A')) # .get_group()提取分组后的组
print(df.groupby('name').mean())           # 以 name 分组求 mean (基础统计里的函数可以直接套用过来)
print(df.groupby(['name','var1']).mean())
print(df.groupby(['name'])['var3'].mean())  # 以 name 分组，算 var3 的平均值

''' (4) apply '''
df = pd.DataFrame({'key':['one','two','one','two','one'], 'data1':np.random.rand(5), 'data2':np.random.rand(5)})
# Case 1:
print(df.groupby('key').apply(lambda x: x.describe())) # apply直接运行其中的函数
# Case 2:
def fn(d,n):
    return(d.sort_index()[:n])
print(df.groupby('key').apply(fn,2))

''' (3) 透视表：pivot_table '''
# pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
# data：DataFrame对象
# values：要聚合的列或列的列表
# index：数据透视表的index，从原数据的列中筛选
# columns：数据透视表的columns，从原数据的列中筛选
# aggfunc：用于聚合的函数，默认为numpy.mean，支持numpy计算方法
date = ['2017-5-1','2017-5-2','2017-5-3']*3
rng = pd.to_datetime(date)
df = pd.DataFrame({'date':rng, 'key':list('abcabcabc'), 'values':np.random.rand(9)*10})
print(df)
print(pd.pivot_table(df, values='values', index='date', columns='key', aggfunc=np.mean)) # 统计不同[date,key]下values的mean
print(pd.pivot_table(df, values='values', index = ['date','key'], aggfunc=np.mean))