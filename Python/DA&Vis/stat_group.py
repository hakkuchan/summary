""" · 目录
    |
    |—— 1. axis参数
    |
    |—— 2. 按列名
    |
    |—— 3. group方法
    |
    |—— 4. 透视表 pivot_table()
"""


import numpy as np
import pandas as pd


""" 1. axis参数 """
df = pd.DataFrame({'X':np.arange(0,5), 'Y':np.arange(10,15)})
print(df.mean(axis=0))  # axis=0 求每列数据的平均
print(df.mean(axis=1))  # axis=1 求每行数据的平均


""" 2. 按列名 """
df = pd.DataFrame({'A':np.arange(0,5), 'B':np.arange(10,15), 'C':np.arange(20,25)})
print(df['A'].mean()) # 按列名求平均
print(df[['A','C']].mean()) # 按列名求平均


""" 3. group方法 """
df = pd.DataFrame({'name' : ['A', 'B', 'A', 'B','A', 'A', 'A', 'B'],
                   'var1' : ['1d', '2d', '1d', '3d', '2d', '2d', '1d', '3d'],
                   'var2' : np.random.randn(8),
                   'var3' : np.random.randn(8)})
print(df)
# (1) get_group()提取满足条件的组 (注意：这种方法不如 df[df['name']=='A'] 方便)
print(df.groupby(['name']).get_group('A'))
# (2) 以 name 分组求 mean
print(df.groupby('name').mean())          
# (3) 以 name 分组，输出 var3 的 mean
print(df.groupby(['name'])['var3'].mean())
# (4) 先以 name分组，再以 var1分组，求 var2、var3的 mean
print(df.groupby(['name','var1']).mean())


""" 4. 透视表 pivot_table() """
# Toy data
date = ['2017-5-1','2017-5-2','2017-5-3'] * 3
date = pd.to_datetime(date)
df = pd.DataFrame({'date': date, 'name': list('abcabcabc'), 'values': np.random.rand(9)*10})
print(df)

''' pivot_table()参数用法：
    · values：被统计的列
    · index：数据透视表的"行名"，从原数据的列中筛选
    · columns：数据透视表的"列名"，从原数据的列中筛选
    · aggfunc：指定函数，支持numpy的ufunc函数
'''

# 例：统计不同date, name下 values 的 mean
print(pd.pivot_table(df, values='values', index='date', columns='name', aggfunc=np.mean)) 