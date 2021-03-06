""" 奇异值分解 (Singular Value Decomposition, SVD)
    
    1. 原理
    
        对矩阵 A (非方阵)进行SVD，即令：A = U @ S @ V
        · 式中：
          @：叉乘
          U：左奇异向量，等于(A @ A.T)的特征向量
          S：对角线为奇异值的广义对角阵，奇异值为(A @ A.T)特征值的开方
          V：右奇异向量，等于(A.T @ A)的特征向量
        · 若A为3×2矩阵，那么U为3×3矩阵，S为3×2矩阵，V为2×2矩阵
"""    



""" 2. 代码实现 """

''' 2.1 分解步骤'''
import numpy as np
# 原始矩阵
A = np.matrix([[0,1], [1,1], [1,0]])
# 计算 (A @ A.T) 的特征值和特征向量
eigval_1, eigvec_1 = np.linalg.eig(A @ A.T)
# 左奇异向量 U 等于 (A @ A.T) 的特征向量
U = eigvec_1
# 计算 (A.T @ A) 的特征值和特征向量
eigval_2, eigvec_2 = np.linalg.eig(A.T @ A)
# 右奇异向量 V 等于 (A^T @ A) 的特征向量
V = eigvec_2
# 奇异值等于 (A @ A^T) 特征值的开方
sv = np.sqrt(np.around(eigval_1))
# 广义对角阵 S
S = np.diag(sv)[:,0:len(V)]
# 结果
print('原矩阵：\n', A, '\n')
print('左奇异向量：\n', U, '\n')
print('广义对角阵：\n', S, '\n')
print('右奇异向量：\n', V, '\n')
print('基于奇异向量和奇异值计算原矩阵（正负号可能会有变化）：\n', np.around(U @ S @ V, 6), '\n')

''' 2.2 svd方法（推荐） '''
U, S, V = np.linalg.svd(A)
n = np.array(A.shape) - np.array(np.diag(S).shape)
S = np.concatenate((np.diag(S), np.zeros((n[0], V.shape[1]))), axis=0) 
print('原矩阵：\n', A, '\n')
print('左奇异向量：\n', U, '\n')
print('广义对角阵：\n', S, '\n')
print('右奇异向量：\n', V, '\n')
print('基于奇异向量和奇异值计算原矩阵（正负号可能会有变化）：\n', np.around(U @ S @ V, 6), '\n')