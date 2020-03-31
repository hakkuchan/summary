""" · 目录
    |
    |—— 1. 逆矩阵
    |
    |—— 2. 伪逆矩阵
"""

import numpy as np

""" 1. 逆矩阵：对于方阵A(且其列向量线性无关)，存在矩阵 B 使得 AB = I，则A和B互为逆矩阵 """
A = np.matrix([[1,2,1], [1,2,0], [2,5,1]])
print('A的逆矩阵:\n', A.I)
print('A.I @ A:\n', A.I@A)

# 逆矩阵的作用之一：对线性方程组 Ax = y，可得 x = A.I @ y
A = np.matrix([[1,2,1], [1,2,0], [2,5,1]])
x = np.matrix([[7],[8],[9]])
y = A @ x
print('x:\n', A.I @ y)



""" 2. 伪逆矩阵: 若矩阵 A 不是方阵或其列向量线性相关(奇异, singular)，对于 Ax = y，
       存在矩阵 B 使得 x = By，则A和B互为伪逆矩阵
"""
A = np.matrix([[1,2,3], [4,5,6]])
B = A.I
x = np.matrix([[7],[8],[9]])
y = A @ x
print('x-By:\n', np.around(x - B@y))