""" KernelPCA (KPCA)：KPCA是PCA的扩展，即先利用核函数对数据进行升维，然后再降维 """

import numpy as np
from sklearn import datasets
from sklearn import decomposition

# Data：Iris
iris = datasets.load_iris()
X = iris.data
print('Shape of X:', X.shape) # >>> (150, 4) 150个样本，4个特征

# KernelPCA降维
kpca = decomposition.KernelPCA(n_components=2, kernel='rbf') # 设置降维后的维度，核函数类型
Xr = kpca.fit_transform(X) # 降维

# 由于 KernelPCA方法 无法直接获得投影矩阵，投影矩阵需要间接计算
# 方法：Xr = Xm @ proj  →  proj = Xm.I @ Xr    
Xm = np.matrix(X - np.mean(X, axis=0)) # 样本去中心化
proj = Xm.I @ Xr
print('Shape of proj:', proj.shape) # >>> (4, 2)
print('Shape of Xr:', Xr.shape) # >>> (150, 2) 150个样本，2个特征
print('Proj:\n', proj)