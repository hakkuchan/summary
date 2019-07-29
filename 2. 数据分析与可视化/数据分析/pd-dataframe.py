""" 
Panda中的dataframe

是一个表格型的数据结构，

其列的值类型可以是数值、字符串、布尔值等。

"""

import pandas as pd
import numpy as np

''' (1) 创建方法 '''
# a. 由数组创建
ar = np.random.rand(9).reshape(3,3)
print(pd.DataFrame(ar,index=['a','b','c'], columns=['x1','x2','x3'])) # 如果不指定index和columns，两者均返回默认数字格式

# b. 由Series组成的字典
data1 = {'one':pd.Series(np.random.rand(2)), 
         'two':pd.Series(np.random.rand(3))}
data2 = {'one':pd.Series(np.random.rand(2), index = ['a','b']),
         'two':pd.Series(np.random.rand(3), index = ['a','b','c'])}
# data1没有设置index，data2设置了index
# columns为字典key
# index为Series的标签（如果Series没有指定标签，则是默认数字标签）
print(pd.DataFrame(data1))
print(pd.DataFrame(data2))

# c. 由字典组成的字典
# Case 1:
data = {'a':[1,2,3], 'b':[3,4,5], 'c':[5,6,7]}
print(pd.DataFrame(data))
print(pd.DataFrame(data, columns = ['b','c','a','d'])) # columns参数：可以重新指定列的顺序, 没有对应列时产生NaN
print(pd.DataFrame(data, columns = ['b','c']))        # 如果columns重新指定时候，列的数量可以少于原数据
print(pd.DataFrame(data, index = ['f1','f2','f3']))   # index参数：重新定义index，格式为list，长度必须保持一致
# Case 2:
data = {'Jack':{'math':90,'english':89,'art':78},
        'Mary':{'math':82,'english':95,'art':92},
        'Mike':{'math':78,'english':67}}
print(pd.DataFrame(data))
print(pd.DataFrame(data, columns = ['Jack','Mary','Mike'])) # columns参数可以增加和减少现有列，如出现新的列，值为NaN
print(pd.DataFrame(data, index = ['a','b','c'])) # index在这里和并不能改变原有index，如果指向新的标签，值为NaN （非常重要！）


''' (2) 切片和索引 '''
data = {'name':['Jack','Mike','Mary'], 'age':[18,19,20], 'gender':['m','m','w']}

# a. 按列 (df[col]一般用于选择列，[]中写列名)
df = pd.DataFrame(data)
print(df['age'])
print(df[['name','gender']])

# b. 按行 (df.loc[label]主要针对index选择行，同时支持指定index，及默认数字index)
df = pd.DataFrame(data)
print(df.loc[[0,2]])
df = pd.DataFrame(data, index=['p1','p2','p3'])
print(df.loc['p2'])
print(df.loc[['p1','p3']])

# c. 多行 (df.iloc[])
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
print(df)
print(df.iloc[-1])      # 单位置索引
print(df.iloc[[3,2,1]]) # 多位置索引
print(df.iloc[::2])     # 切片索引

# d. 布尔型索引 (按条件提取数据)
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
# 所有数据判断
print(df)
b1 = df < 20
print(b1)
print(df[b1])
print(df[df<20])
# 单列判断
print(df)
b2 = df['a'] > 50
print(b2)
print(df[b2])
print(df[df['a'] > 50])
# 多列判断
print(df)
b3 = df[['a','b']] > 50
print(b3,type(b3))
print(df[b3])  
print(df[['a','b']] > 50)
# 多行判断
b4 = df.loc[['x1','x3']] < 50
print(b4,type(b4))
print(df[b4])
print(df[df.loc[['x1','x3']] < 50])

# e. 多重索引：比如同时索引行和列
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x1','x2','x3','x4'], columns = ['a','b','c','d'])
print(df)
print(df['a'].loc[['x1','x3']])   # 选择a列的one，three行
print(df[['b','c','d']].iloc[::2])    # 选择 b，c，d 列的 x1，x3行
print(df[df['a'] < 50].iloc[:2])      # 选择满足判断索引的前两行数据

''' (3) 基本操作 '''
data = {'name':['Jack','Mike','Mary'], 'age':[18,19,20], 'gender':['m','m','w']}
df = pd.DataFrame(data)
print(df)  
print(df.index)    # .index查看行标签
print(df.columns)  # .columns查看列标签
print(df.values)   # .values查看值，数据类型为ndarray
print(df.T)        # .T 转置
print(df.dtypes)   # 每列数据类型
print(df.shape)    # 表格维度
print(df.shape[1]) # 列数
print(df.shape[0]) # 行数 

# 增、改
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df)
df['e'] = df['d']/10    # 新增列并赋值
df.loc[4] = 20  # 新增行并赋值
print(df)
df[['a','c']] = 100 # 索引后直接修改值
print(df)

# 删
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df)
del df['a'] # del语句- 删除列
print(df)
print(df.drop(0))     # drop()删除行    
print(df.drop([1,2])) # inplace=False → 删除后生成新的数据，不改变原数据
print(df)
print(df.drop(['d'], axis = 1)) # drop()删除列，需要加上axis = 1
print(df)

# 查
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df)
print(df.head(2)) # .head()查看头部数据
print(df.tail())  # .tail()查看尾部数据, 默认查看5条

# 单列排序
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns = ['a','b','c','d'])
print(df1)
print(df1.sort_values(['a'], ascending = True))   # 升序
print(df1.sort_values(['a'], ascending = False))  # 降序
# 多列排序
df2 = pd.DataFrame({'a':[1,1,1,1,2,2,2,2],'b':list(range(8)),'c':list(range(8,0,-1))})
print(df2)
print(df2.sort_values(['a','c']))
# 按行排序
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = [4,2,3,1], columns = ['a','b','c','d'])
print(df1)
print(df1.sort_index()) # 默认 ascending=True, inplace=False
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, index = ['x2','x3','x1','x4'], columns = ['a','b','c','d'])
print(df2)
print(df2.sort_index()) 

# 对齐（DataFrame对象之间的数据自动按照列和索引（行标签）对齐）
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print(df1 + df2)