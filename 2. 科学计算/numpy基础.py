import numpy as np
import pandas as pd

char = pd.read_csv('E:\Work\Jupyter\data\char_data.csv')
char = char.values

""" 结构和维度 """
# 数据结构
print(type(char))
# 表格维度  
print(char.shape)
# 列数  
print(char.shape[1])
# 行数 
print(char.shape[0])

""" 索引和切片 """
# 第一行数据
print(char[0])
# 第1~4行数据
print(char[0:3])
# 第2,4,6行数据
print(char[[2,4,6]])
# 第1,3,5列数据
print(char[:,[1,3,5]])

""" 矩阵维数的转化 """
# 2行3列
X = np.array([[1,2,3],[4,5,6]])
# 转化为3行2列
X = X.reshape(3,2)
# 转化为1行若干列
X = X.reshape(1,-1)
X = X.ravel()
# 转化为若干行1列
X = X.reshape(-1,1)
# 高维转化         
X = X.reshape(-1,1,1)       

""" 矩阵数据类型的转化 """
X = np.array([[1,2,3],[4,5,6]])
X = X.astype('float')

""" 矩阵维数的拼接 """
# 2行3列
X1 = np.array([[1,2,3],[4,5,6]])
# 2行3列
X2 = np.array([[7,8,9],[10,11,12]])
# 列增加
X_ = np.concatenate((X1, X2), axis=0)
# 行增加
X_ = np.concatenate((X1, X2), axis=1)

""" 数组转化为表格"""
X = np.array([[1,2,3],[4,5,6]])
df = pd.DataFrame(X, columns=['A', 'B', 'C'])