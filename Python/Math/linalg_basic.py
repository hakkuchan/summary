""" · 目录
    |
    |—— 1. 加法
    |
    |—— 2. 乘法
    |   |
    |   |—— 2.1 叉乘
    |   |
    |   |—— 2.2 点乘
    |   |
    |   |—— 2.3 数乘
    |
    |—— 3. 求逆
    |   |
    |   |—— 3.1 逆矩阵
    |   |
    |   |—— 3.2 伪逆矩阵
    |
    |—— 4. 其它: 转置、求秩、求迹、求行列式的值
"""

import numpy as np

""" 1. 加法 (对应元素相加) """
A = np.matrix([[1,2,3,4], [5,6,7,8]])
B = np.matrix([[1,2,3,4], [5,6,7,8]])
print(A+B)



""" 2. 乘法 """
''' 2.1 叉乘 (最重要) '''
# Toy matrix
A = np.matrix([[1,2,3,4], [5,6,7,8]]) # 2×4
B = np.matrix([[1,2], [3,4], [5,6], [7,8]]) # 4×2
C = np.matrix([[1,2], [3,4], [5,6], [7,8]]) # 4×2
# (1) 要求：前一个矩阵列数等于后一个矩阵行数
print(A.shape) # >>> (2,4)
print(B.shape) # >>> (4,2)
print((A@B).shape) # >>> (2,2)
# (2) 满足分配律：A(B+C) = AB+AC
print(A@(B+C) == (A@B + A@C))
# (3) 满足结合律：A(BC) = (AB)C'''
D = C.T
print(A@(B@D) == (A@B)@D)
# (4) 大多数情况下不满足交换律： AB ≠ BA
# (5) 转置：(AB)^T = (A^T)(B^T)
print((A@B).T == (B.T@A.T))

''' 2.2 点乘 (对应元素相乘) '''
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[2,2,2],[2,2,2]])
print(A*B) 
# 如果 A、B 为 numpy的 array类型，A*B表示点乘 
# 如果 A、B 为 numpy的 matrix类型，A*B表示叉乘

''' 2.3 数乘 (常数×每个元素) '''
A = np.array([[1,2,3],[4,5,6]])
print(0*A)



""" 3. 求逆 """
''' 3.1 逆矩阵：对于方阵A(且其列向量线性无关)，存在矩阵 B 使得 AB = I，则A和B互为逆矩阵 '''
A = np.matrix([[1,2,1], [1,2,0], [2,5,1]])
print('A的逆矩阵:\n', A.I)
print('A.I @ A:\n', A.I@A)
# 逆矩阵的作用之一：对线性方程组 Ax = y，可得 x = A.I @ y
A = np.matrix([[1,2,1], [1,2,0], [2,5,1]])
x = np.matrix([[7],[8],[9]])
y = A @ x
print('x:\n', A.I @ y)

''' 3.2 伪逆矩阵: 若矩阵 A 不是方阵或列向量线性相关 (奇异, singular)，
        对于 Ax = y，存在矩阵 B 使得 x = By，则A和B互为伪逆矩阵 '''
A = np.matrix([[1,2,3], [4,5,6]])
B = A.I
x = np.matrix([[7],[8],[9]])
y = A @ x
print('x-By:\n', np.around(x - B@y))



""" 4. 其它 """
# 转置
A = np.matrix([[1,2,3], [4,5,6]])
print(A.T)
# 求秩
A = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
print(np.linalg.matrix_rank(A))
# 求迹
A = np.diag([1,2,3,4,5])
print(np.trace(A))
# 求行列式的值
A = np.matrix([[1,1,1], [0,2,1], [3,1,3]])
print(np.linalg.det(A))