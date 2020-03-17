""" 密度聚类 (Density-based spatial clustering of applications with noise, DBSCAN)

    · 思想：把紧密程度高于阈值的样本划为同类簇
    · 步骤：
      Step 1: 随机选择一个对象p，检查p的邻域e内是否至少包含MinPts个样本
      Step 2: 若不包含，p被标记为噪声，不参与之后的聚类；
              若包含，基于p创建一个簇C，邻域e的中所有对象都放到候选集合N中
      Step 5: 遍历候选集合N中的所有样本，若样本的邻域e内至少有MinPts个对象，将这些对象全部添加到N中
      Step 6: 遍历候选集合N中的样本，若样本不属于其它簇，便将其添加到簇C中
      Step 7: 遍历结束后，簇C被生成
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

''' DBSCAN模型 '''
clst = cluster.DBSCAN(
                      eps=0.5, # 确定邻域e的大小，调小时一些样本点会被视作噪声
                      min_samples=5, # 确定邻域内最少包含的点个数，调小时一些样本点会被视作噪声
                     )
labels = clst.fit_predict(X) # 训练DBSCAN模型并输出每个样本所属的簇标记

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
for n, c in enumerate(clusters[:-1]):
    ax.scatter(c[:,0], c[:,1], color=colors[n], s=5)