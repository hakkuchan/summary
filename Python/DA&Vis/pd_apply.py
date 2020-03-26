""" apply 自定义函数对批量数据进行操作 """

import pandas as pd


''' 1. 引例 '''
df = pd.DataFrame({'x':np.arange(1,3), 'y':np.arange(11,13)})
print(df.apply(lambda a: a**2))
# 等价于
def fn(a):
    return a ** 2
print(df.apply(fn))


''' 2. 分组 '''
# 例 1：
print(df['y'].apply(lambda a: a+1))

# 例 2：
df = pd.DataFrame({'key':['A','B','A','B','A'], 'P1':np.random.rand(5), 'P2':np.random.rand(5)})
print(df.groupby('key').apply(lambda x: x.describe())) # 按 key 分组后进行 describe() 方法
# 等价于
def fn(d):
    return(d.describe())
print(df.groupby('key').apply(fn))