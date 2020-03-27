""" 流形学习（manifold learning）
    
    · 核心思想：把高维数据降为低维数据时，保证不同样本的关系（如距离、线性关系等）不变
    
    · 目录
    |
    |—— 1. 多维缩放 (Multiple Dimensional Scaling, MDS)
    |
    |—— 2. 等度量映射 (Isometric Mapping, Isomap)
    |
    |—— 3. 局部线性嵌入 (Locally Linear Embedding, LLE)
	|
	|—— 4. T分布邻域嵌入 (T-distributed Stochastic Neighbor Embedding, TSNE)
"""


from sklearn import datasets
from sklearn import manifold


""" 1. 多维缩放 (Multiple Dimensional Scaling, MDS)
    
    · 核心思想：利用MDS降维时，需保持原始空间中不同样本的距离在低维空间中不变
"""
# Data: Iris
iris = datasets.load_iris()
X = iris.data # 150个样本，4个特征
# MDS降维
mds = manifold.MDS(n_components=2) # 设置降维后的维度
Xr = mds.fit_transform(X) # 转换 X
print(Xr.shape) # >>> (150, 2)



""" 2. 等度量映射 (Isometric Mapping, Isomap)
    
    · MDS降维存在误导性：在高维空间中，有时不同样本的距离不能视作直线距离
    
    · 为解决这一问题，Isomap计算2个样本距离的方法是：
      从一个样本出发，不断寻找 第Top K 近邻点，直到另一个样本，
      以经过的路程作为2个样本的距离。
    
    · 需要注意，K的选择至关重要：
      (1) "短路"问题：K过大可能导致把相距很远的点当成近邻点
      (2) "断路"问题：K过小可能导致从一个样本到不了另一个样本
      "短路"和"断路"都会误导后续计算
"""
# Data: Iris
iris = datasets.load_iris()
X = iris.data
# Isomap降维
isomap = manifold.Isomap(n_neighbors=3, n_components=2) # 设置 第Top K 近邻 和 降维后的维度
Xr = isomap.fit_transform(X) # 转换 X
print(Xr.shape) # >>> (150, 2)



""" 3. 局部线性嵌入 (Locally Linear Embedding, LLE)
    
    · LLE降维时保持的是邻近点的线性关系
      比如：xi = w1x1 + w2x2 + w3x3 （x1, x2, x3 是 xi 的 Top 3 近邻点）
"""
# Data: Iris
iris = datasets.load_iris()
X = iris.data
# LLE降维
lle = manifold.LocallyLinearEmbedding(n_neighbors=3, n_components=2) # 设置 Top K 近邻 和 降维后的维度
Xr = lle.fit_transform(X)  # 转换 X
print(Xr.shape) # >>> (150, 2)



""" 4. T分布邻域嵌入 (T-distributed Stochastic Neighbor Embedding, TSNE)

    · TSNE在降维时会先计算高维数据间的距离，并把距离转换为条件概率，并使降维后数据的条件概率分布与降维前相同
      其核心思想依然是：在高维空间中靠近的样本，降至低维空间后依然使其靠近，反之亦然
"""
# Data: Iris
iris = datasets.load_iris()
X = iris.data
# TSNE降维
lle = manifold.TSNE(n_components=2) # 设置降维后的维度
Xr = lle.fit_transform(X)  # 转换 X
print(Xr.shape) # >>> (150, 2)