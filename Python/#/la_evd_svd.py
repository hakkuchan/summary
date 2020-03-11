""" 目录
     |
     |—— 1. 特征值分解
     |   |
     |   |—— 1.1 分解步骤
     |   |
     |   |—— 1.2 代码实现-eig方法
     |
     |—— 2. 奇异值分解
         |
         |—— 2.1 分解步骤
         |
         |—— 2.2 代码实现-分解步骤
         |
         |—— 2.3 代码实现-svd方法
"""



""" 1. 特征值分解 (Eigen Value Decomposition, EVD) 
    
    1.1 分解步骤
        对方阵 A 进行EVD，即令：A @ x = r @ x 
        · 式中：
          @：叉乘
          x：特征向量
          r：特征值

        · 例：对 A = [[6,2,4], [2,3,2], [4,2,6]] 进行特征值分解
        
          Ax = rx  →  Ax = rEx  →  (rE-A)x = 0
          
                   |r-6  -2  -4|
          |rE-A| = |-2  r-3  -2| = 0   →   (r-2)^2(r-11)=0   →   r1=r2=2, r3=11
                   |-4   -3 r-6|
           
          将 r1=r2=2,r3=11 分别代入(rE-A)x=0，
          可求出三个线性无关的基础解系 x1=[-1,0,1], x2=[1,0,1], x3=[0,-1,1]
          进而组成特征向量
          (注意：3个基础解系不唯一，只要线性无关即可)
"""


''' 1.2 代码实现-eig方法 '''
import numpy as np
# 原始方阵
A = np.matrix([[6,2,4], [2,3,2], [4,2,6]])
# 直接计算 eigval(特征值) 和 eigvec(特征向量)
eigval, eigvec = np.linalg.eig(A)  
print('特征值：', np.around(eigval))
print('特征向量: \n', np.around(eigvec))



""" 2. 奇异值分解 (Singular Value Decomposition, SVD)
    
    2.1 分解步骤
        对矩阵M进行SVD，即令：M = U @ S @ V
        · 式中：
          @：叉乘
          U：左奇异向量，等于(M @ M^T)的特征向量
          S：对角线为奇异值的广义对角阵，奇异值为(M @ M^T)特征值的开方
          V：右奇异向量，等于(M^T @ M)的特征向量
        · 若M为3×2矩阵，那么U为3×3矩阵，S为3×2矩阵，V为2×2矩阵
    
    
    2.2 代码实现-分解步骤
"""
# 原始矩阵
M = np.matrix([[0,1], [1,1], [1,0]])

# 计算 (M @ M^T) 的特征值和特征向量
eigval_1, eigvec_1 = np.linalg.eig(M @ M.T)
# 左奇异向量 U 等于 (M @ M^T) 的特征向量
U = eigvec_1

# 计算 (M^T @ M) 的特征值和特征向量
eigval_2, eigvec_2 = np.linalg.eig(M.T @ M)
# 右奇异向量 V 等于 (M^T @ M) 的特征向量
V = eigvec_2

# 奇异值等于 (M @ M^T) 特征值的开方
sv = np.sqrt(np.around(eigval_1))
# 广义对角阵 S
S = np.diag(sv)[:,0:len(V)]

# 结果
print(U, '\n\n', S, '\n\n', V, '\n')
print(np.around(U @ S @ V, 6), '\n')  # 正负号会有变化

""" 2.3 代码实现-svd方法 """
U, S, V = np.linalg.svd(M)
n = np.array(M.shape) - np.array(np.diag(S).shape)
S = np.concatenate((np.diag(S), np.zeros((n[0], V.shape[1]))), axis=0) 
print(U, '\n\n', S, '\n\n', V, '\n')
print(np.around(U @ S @ V, 3))