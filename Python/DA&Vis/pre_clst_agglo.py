""" 层次聚类 (Hierarchical Clustering, Sklearn中层次聚类模型为AgglomerativeClustering)
    
    · 原理：通过计算不同簇的相似度类创建一个有层次的嵌套树
      需要注意：树的建立是"自下而上"，即先从叶节点(单个样本)开始，
               根据相似度生成根节点，最终生成K个树 (K=设定的簇个数)
    · 步骤：
      Step 1: 把每个样本都视为一个簇
      Step 2: 计算各个簇之间的相似度
      Step 3: 把最近的两个簇归为一个簇
      Step 4: 重复Step 2、3，直到所有样本归为所设的的K簇
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

''' AgglomerativeClustering模型 '''
clst = cluster.AgglomerativeClustering(
                                       n_clusters=4, # 设定簇个数，也可不设置
                                      )
labels = clst.fit_predict(X) # 训练AgglomerativeClustering模型并输出每个样本所属的簇标记

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
colors = {0:'black', 1:'red', 2:'blue', 3:'green'}
for n, c in enumerate(clusters):
    ax.scatter(c[:,0], c[:,1], color=colors[n], s=5)