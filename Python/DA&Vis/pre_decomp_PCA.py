""" PCA降维

    · 核心思想：把高维特征转换为尽可能相互正交的低维特征，
      在降低了数据维度的同时，消除了高维特征的共线性
    
    · sklearn中提供了 典型PCA 和 KernelPCA
      二者区别仅在于 KernelPCA 会先用核函数对数据升维，然后再进行典型PCA降维

    · 目录
    |
    |—— 1. PCA
    |   |
    |   |—— 1.1 典型PCA
    |   |
    |   |—— 1.2 分解步骤
    |
    |—— 2. KernelPCA
"""

import numpy as np
from sklearn import datasets
from sklearn import decomposition

""" 1. PCA """
''' 1.1 典型PCA '''
# Data：Iris
iris = datasets.load_iris()
X = iris.data  # >>> (150, 4) 150个样本，4个特征

# 典型PCA降维
pca = decomposition.PCA(n_components=2) # 设置降维后的维度
Xr = pca.fit_transform(X) # 转换 X
print('Shape of Xr:', Xr.shape) # >>> (150, 2) 150个样本，2个特征
print(f'Top {len(pca.explained_variance_)} 特征值:', pca.explained_variance_)
print(f'Top {len(pca.explained_variance_)} 特征值所占比例:', pca.explained_variance_ratio_)

# 投影矩阵的计算，思路：Xr = Xm @ proj  →  proj = Xm.I @ Xr
Xm = np.matrix(X - np.mean(X, axis=0)) # 样本去中心化
proj = Xm.I @ Xr
print('Shape of proj:', proj.shape) # >>> (4, 2)


''' 1.2 分解步骤 '''
# Data：Iris
iris = datasets.load_iris()
X = iris.data  # >>> (150, 4) 150个样本，4个特征

# Step 1: 计算样本的协方差矩阵
cov = np.cov(X.T)

# Step 2: 对协方差矩阵进行特征值分解
eigval, eigvec = np.linalg.eig(cov) # eigval:特征值   eigvec:特征向量
print('特征值:', eigval) # >>> [4.22824171 0.24267075 0.0782095  0.02383509]

# Step 3: 投影矩阵
proj_ = eigvec[:,(0,1)] # 根据特征值，将 4维数据降至 2维

# Step 4: 样本去中心化
Xm = X - np.mean(X, axis=0)

# Step 5: 典型PCA降维
Xr = Xm @ proj_  # 转换 X
print('1与2所得投影矩阵之差:\n', np.around(abs(proj)-abs(proj_))) # 特征向量的计算有时会有正负号区别



""" 2. KernelPCA """
# Data：Iris
iris = datasets.load_iris()
X = iris.data # 150个样本，4个特征

# KernelPCA降维
kpca = decomposition.KernelPCA(n_components=2, kernel='rbf') # 设置 降维后的维度 和 核函数类型
Xr = kpca.fit_transform(X) # 转换 X
print('Shape of Xr:', Xr.shape) # >>> (150, 2) 150个样本，2个特征

# 投影矩阵的计算，思路：Xr = Xm @ proj  →  proj = Xm.I @ Xr  
Xm = np.matrix(X - np.mean(X, axis=0)) # 样本去中心化
proj = Xm.I @ Xr
print('Shape of proj:', proj.shape) # >>> (4, 2)