import numpy as np
from sklearn import datasets
from sklearn import decomposition

''' 导入原始数据 '''
iris = datasets.load_iris()
X = iris.data
print('原始数据集的行列数:', X.shape) # >>> (150, 4) 150组数据，4个特征

''' 求协方差矩阵 '''
cov = np.cov(X.T)

''' 求特征值和特征向量 '''
eigval, eigvect = np.linalg.eig(np.cov(X.T))
print('特征值:', eigval)  # >>> [4.22824171 0.24267075 0.0782095  0.02383509]
print('特征向量:\n', eigvect)

''' 数据降维 '''
proj = eigvect[:,(0,1)]  # 根据特征值，选择前两列特征向量作为投影矩阵
print('投影矩阵:\n', proj)
print('投影矩阵行列数：', proj.shape)
Xm = X - np.mean(X, axis=0)  # X去中心化
Xd = Xm @ proj  # 降维后的数据
print('降维后数据集的行列数:', Xd.shape)

''' * 与sklearn.decomposition.PCA方法对比 '''
pca = decomposition.PCA(2)
Xr = pca.fit_transform(X) # 转化后的正负会有差别，但不影响降维效果
print('对比:\n', (abs(Xd) - abs(Xr))[0:3,:])

''' sklearn.decomposition.PCA无法直接给出投影矩阵，
    由于 转化后的矩阵 = 去中心化的原始数据矩阵 @ 投影矩阵
    所以 投影矩阵 = (去中心化的原始数据矩阵)^(-1) @ 转化后的矩阵
'''
print('所求投影矩阵:\n', np.matrix(Xm).I @ Xr)