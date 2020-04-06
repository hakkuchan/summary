""" 特征值分解 (Eigenvalue Decomposition, EVD) 
    
    1. 原理
        
       对方阵 A 进行EVD，即令：A = X @ S @ X.I 
       · 式中：
         @：叉乘
         X：特征向量，X.I为X的逆矩阵
         S：以特征值为对角线元素的对角矩阵
    
    
    2. 代码实现-eig方法
"""
import numpy as np
# 原始方阵
A = np.matrix([[6,2,4], [2,3,2], [4,2,6]])
# 直接计算 eigval(特征值) 和 eigvec(特征向量)
eigval, eigvec = np.linalg.eig(A)
print('原矩阵：\n', A, '\n')
print('特征值：', eigval, '\n')
print('特征向量: \n', eigvec, '\n')
print('基于特征值和特征向量计算原矩阵：\n' ,eigvec @ np.diag(eigval) @ eigvec.I, '\n')