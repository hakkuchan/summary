""" · 目录
    |
    |—— 1. 创建：数组、Series、字典
    |   
    |—— 2. 切片和索引
    |   |
    |   |—— 2.1 按标签选择列 (df[列名])
    |   |
    |   |—— 2.2 按标签选择行 (df.loc[行名])
    |   |
    |   |—— 2.3 按索引选择多行 (df.iloc[])
    |   |
    |   |—— 2.4 布尔型索引 (按条件提取数据)
    |   |
    |   |—— 2.5 重置索引
    |
    |—— 3. 操作
        |
        |—— 3.1 查看
        |
        |—— 3.2 增改
        |
        |—— 3.3 删
        |
        |—— 3.4 排序：单列、多列、按行
        |
        |—— 3.5 运算和自动对齐
        |
        |—— 3.6 合并
"""

import numpy as np
import pandas as pd

""" 1. 创建 """

''' 1.1 由数组创建 '''
ar = np.random.rand(9).reshape(3,3)
print(pd.DataFrame(ar, index=['a','b','c'], columns=['x1','x2','x3'])) # 如果不指定index和columns，两者均返回默认数字格式

''' 1.2 由Series创建 '''
s = {'x1':pd.Series(np.random.rand(2), index = ['a','b']),
     'x2':pd.Series(np.random.rand(3), index = ['a','b','c'])}
print(pd.DataFrame(s))

''' 1.3 由字典创建 '''
# 方法 1:
data = {'a':[1,2,3], 'b':[3,4,5], 'c':[5,6,7]}  # 字典的键对应的是列名
print(pd.DataFrame(data))
print(pd.DataFrame(data, columns = ['b','c','a','d'])) # columns重新指定列的顺序, 没有对应列时产生NaN
print(pd.DataFrame(data, columns = ['b','c']))         # columns重新指定列的数量可以少于原数据
print(pd.DataFrame(data, index = ['f1','f2','f3']))    # index重新定义index，格式为list，长度必须保持一致
# 方法 2:
data = {'Jack':{'Math':90,'English':89,'Art':78}, # 嵌套字典，主键为行名，子键为列名
        'Mary':{'Math':82,'English':95,'Art':92},
        'Mike':{'Math':78,'English':67}}
print(pd.DataFrame(data))
print(pd.DataFrame(data, columns = ['Mary','Jack','Mike'])) # columns参数可以增加和减少现有列，如出现新的列，值为NaN
print(pd.DataFrame(data, index = ['a','b','c'])) # index在这里和并不能改变原有index，如果指向新的标签，值为NaN (非常重要)。



""" 2. 切片和索引 """

''' 2.1 按标签选择列 (df[列名]) '''
data = {'name':['Jack','Mike','Mary'], 'age':[18,19,20], 'gender':['m','m','w']}
df = pd.DataFrame(data)
print(df['age'])
print(df[['name','gender']])

''' 2.2 按标签选择行 (df.loc[行名]) '''
data = {'name':['Jack','Mike','Mary'], 'age':[18,19,20], 'gender':['m','m','w']}
df = pd.DataFrame(data)
print(df)
print(df.loc[[0,2]])
df = pd.DataFrame(data, index=['p1','p2','p3'])
print(df.loc[['p1','p3']])

''' 2.3 按索引选择多行 (df.iloc[]) '''
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
print(df)
print(df.iloc[-1])      # 单位置索引
print(df.iloc[[3,2,1]]) # 多位置索引
print(df.iloc[::2])     # 切片索引

''' 2.4 布尔型索引 (按条件提取数据) '''
# 方法 1：所有数据判断
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
print(df)
b1 = df < 20
print(b1)
print(df[b1])
print(df[df<20])
# 方法 2：单列判断
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
print(df)
b2 = df['a'] > 50
print(b2)
print(df[b2])
print(df[df['a'] > 50])
# 方法 3：多列判断
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
print(df)
b3 = df[['a','b']] > 50
print(b3,type(b3))
print(df[b3])  
print(df[['a','b']] > 50)
print(df[(df['a'] > 50) & (df['b'] > 20)]) # 且
print(df[(df['a'] > 50) | (df['b'] > 60)]) # 或
# 方法 4：多行判断
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
b4 = df.loc[['x1','x3']] < 50
print(b4,type(b4))
print(df[b4])
print(df[df.loc[['x1','x3']] < 50])
# 方法 5：多重索引：比如同时索引行和列
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
print(df)
print(df['a'].loc[['x1','x3']])       # 选择a列的one，three行
print(df[['b','c','d']].iloc[::2])    # 选择 b，c，d 列的 x1，x3行
print(df[df['a'] < 50].iloc[:2])      # 选择满足判断索引的前两行数据

''' 2.5 重置索引 '''
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
df.set_index(np.array(['y1','y2','y3','y4']))



""" 3. 操作 """

''' 3.1 查看 '''
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df)
print(df.head(2))  # .head()查看头部数据
print(df.tail())   # .tail()查看尾部数据, 默认查看5条
print(df.index)    # .index查看行标签
print(df.columns)  # .columns查看列标签
print(df.values)   # .values查看值，数据类型为ndarray
print(df.T)        # .T 转置
print(df.dtypes)   # 每列数据类型
print(df.shape)    # 表格维度
print(df.shape[1]) # 列数
print(df.shape[0]) # 行数

''' 3.2 增改 '''
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df)
df['e'] = df['d']/10  # 新增列并赋值
df.loc[4] = 20        # 新增行并赋值
print(df)
df[['a','c']] = 100   # 索引后直接修改值
print(df)

''' 3.3 删 '''
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df)
del df['a'] # del语句- 删除列
print(df)
print(df.drop(0))     # drop()删除行    
print(df.drop([1,2])) # inplace=False → 删除后生成新的数据，不改变原数据
print(df)
print(df.drop(['d'], axis = 1)) # drop()删除列，需要加上axis = 1
print(df)

''' 3.4 排序 '''
# 方法 1：单列排序
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df1)
print(df1.sort_values(['a'], ascending = True))   # 升序
print(df1.sort_values(['a'], ascending = False))  # 降序
# 方法 2：多列排序
df2 = pd.DataFrame({'a':[1,1,1,1,2,2,2,2],'b':list(range(8)),'c':list(range(8,0,-1))})
print(df2)
print(df2.sort_values(['a','c']))
# 方法 3：按行排序
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = [4,2,3,1], columns = ['a','b','c','d'])
print(df1)
print(df1.sort_index()) # 默认 ascending=True, inplace=False
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x2','x3','x1','x4'], columns = ['a','b','c','d'])
print(df2)
print(df2.sort_index())

''' 3.5 运算和自动对齐 '''
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print(df1)
print(df2)
print(df1 / df2) # 对应位置元素进行计算，并自动对齐，缺失位置补充为 NaN

''' 3.6 合并 '''
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
df3 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
df4 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
print(pd.merge(df1, df2, on='key'))  # merge合并 
print(pd.merge(df3, df4, on=['key1','key2']))  # 多个链接键
print(pd.merge(df3, df4, on=['key1','key2'], how = 'inner'))  # inner：默认，取交集
print(pd.merge(df3, df4, on=['key1','key2'], how = 'outer'))  # outer：取并集，数据缺失范围NaN
print(pd.merge(df3, df4, on=['key1','key2'], how = 'left'))   # left：按照df3为参考合并，数据缺失范围NaN
print(pd.merge(df3, df4, on=['key1','key2'], how = 'right'))  # right：按照df4为参考合并，数据缺失范围NaN