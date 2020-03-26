import numpy as np
import pandas as pd

""" 2. 分组统计 (统计量以mean为例) """

''' 2.1 axis方法 '''
df = pd.DataFrame({'x':np.arange(10), 'y':np.arange(91,101), 'z':np.random.random(10)})
print(df.mean(axis=0))  # axis=0 求每列数据的平均
print(df.mean(axis=1))  # axis=1 求每行数据的平均

''' 2.2 按列名分组 '''
print(df['x'].mean())   # 按列名求平均
print(df[['x','z']].mean())   # 按列名求平均

''' 2.3 group方法 '''
df = pd.DataFrame({'name' : ['A', 'B', 'A', 'B','A', 'A', 'A', 'B'],
                   'var1' : ['1d', '2d', '1d', '3d', '2d', '2d', '1d', '3d'],
                   'var2' : np.random.randn(8),
                   'var3' : np.random.randn(8)})
print(df)
print(df.groupby(['name']).get_group('A'))  # .get_group()提取满足条件的组（注意：这种方法不如 df[df['name']=='A'] 方便）
print(df.groupby('name').mean())            # 以 name 分组求 mean (基础统计里的函数可以直接套用过来)
print(df.groupby(['name','var1']).mean())
print(df.groupby(['name'])['var3'].mean())  # 以 name 分组，算 var3 的平均值