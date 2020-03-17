""" 1. 聚类(Clustering)简介

    · 聚类试图根据样本的数据特征将样本划分为若干个尽可能不相交的子集 (或称为"簇")
    · 一方面，聚类可用于探索数据分布特征：
      例如，通过对医保卡消费数据进行聚类分析，可分为"正常卡"和"骗保卡"
    · 另一方面，聚类可作为预测模型的前驱过程：
      例如，基于聚类分析得到的"正常卡"和"骗保卡"，建立消费行为与卡类型的预测模型
"""



""" 2. K均值聚类 (Kmeans) 
    
    · 原理：把N个样本划分到K个簇中，使每个样本点到簇均值的距离最小
    · 步骤：
      Step 1: 随机在N个样本中选取K个样本点作为聚类中心
      Step 2: 计算每个点到聚类中心的距离，将每个点聚类到离该点最近的聚类中心的簇中去
      Step 3: 重新计算每个聚类中所有点的坐标平均值，并将这个平均值作为新的聚类中心
      Step 4: 反复执行Step 2,3，直到聚类中心点不再变化或变化很小为止。
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import cluster
%matplotlib inline

''' Data: Iris '''
X = datasets.load_iris().data # 150个样本，4个特征（萼长、萼宽、瓣长、瓣宽）
X = X[:,(0,2)] # 只考虑 萼长 和 瓣长

''' Kmeans模型 '''
clst = cluster.KMeans(
                      n_clusters=4, # 设定簇个数，也可不设置
                      init='k-means++' # 设定初始化策略，'k-means++'表示初始向量相距较远，'random'表示随机选择
                     )
labels = clst.fit_predict(X) # 训练Kmeans模型并输出每个样本所属的簇

''' 可视化 '''
# (1) 绘制 (萼长,瓣长) 数据的原始分布图
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1,2,1)
ax.scatter(X[:,0], X[:,1], color='red', s=5)
# (2) 绘制分簇数据分布图
# Step 1: 合并 X 和 labels
X_labels = np.concatenate((X, labels.reshape(-1,1)), axis=1)
# Step 2: 按 labels 分组
clusters = []
for i in range(len(set(labels))):
    globals()['clst'+str(i)] = np.array([j for j in X_labels if j[2]==i])
    clusters.append(globals()['clst'+str(i)])
clusters = np.array(clusters)
# Step 3: 分簇绘图
ax = fig.add_subplot(1,2,2)
colors = {0:'black', 1:'red', 2:'blue', 3:'green', 4:'purple', 5:'orange'}
for n, c in enumerate(clusters):
    ax.scatter(c[:,0], c[:,1], color=colors[n], s=5)