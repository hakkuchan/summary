""" PCA是一种最常用的降维方法
    其核心思想是把高维特征处理成尽可能相互正交的低维特征
"""

import numpy as np
from sklearn import datasets
from sklearn import decomposition

# Data：Iris
iris = datasets.load_iris()
X = iris.data
print('Shape of X:', X.shape) # >>> (150, 4) 150个样本，4个特征

''' 1. PCA方法 '''
pca = decomposition.PCA(n_components=2) # 设置降维后的维度
Xr = pca.fit_transform(X) # 降维
# 由于PCA方法无法直接获得投影矩阵，投影矩阵需要间接计算
# 方法：Xr = Xm @ proj  →  proj = Xm.I @ Xr    
Xm = np.matrix(X - np.mean(X, axis=0)) # 样本去中心化
proj = Xm.I @ Xr
print('Shape of proj:', proj.shape) # >>> (4, 2)
print('Shape of Xr:', Xr.shape) # >>> (150, 2) 150个样本，2个特征
print(60*'-')

''' 2. 分解步骤 '''
# Step 1: 计算样本的协方差矩阵
cov = np.cov(X.T)
print('Covariance matrix:\n', cov)
# Step 2: 对协方差矩阵进行特征值分解
eigval, eigvec = np.linalg.eig(cov)
print('Eigen value:', eigval) # >>> [4.2 0.2 0.08 0.02] 根据特征值，将 4维数据降至 2维
print('Eigen vetor:\n', eigvec)
# Step 3: 投影矩阵
proj_ = eigvec[:,(0,1)]
# Step 4: 样本去中心化
Xm = X - np.mean(X, axis=0)
# Step 5: 降维
Xr = Xm @ proj_
print(60*'-')
print('1与2所得投影矩阵之差:\n', np.around(abs(proj)-abs(proj_))) # 特征向量的计算有时会有正负号区别