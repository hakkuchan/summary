""" 1. 聚类(Clustering)简介

    · 聚类试图将样本划分为若干个不相交的子集(或称为"簇")
      以医保卡消费为例，通过对消费数据的聚类分析，可分为 正常消费行为(簇) 和 疑似骗保行为(簇)
      (注意：聚类仅能自动形成簇结构，簇对应的组名需要使用者自行考虑和设置)
    
    · 聚类既能探索数据分布特征，例如分析医保卡的“正常消费行为”和“疑似骗保行为”；
      也能作为预测模型的前驱过程，例如根据聚类结果把医保卡分为“正常卡”和“骗保卡”，再建立消费行为与卡类型的预测模型
"""


""" 2. K均值聚类 (Kmeans) """

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import cluster
%matplotlib inline

''' Data: Iris '''
X = datasets.load_iris().data # 150个样本，4个特征（萼长、萼宽、瓣长、瓣宽）
X = X[:,(0,2)] # 只考虑 萼长 和 瓣长

''' 调用 Kmeans方法 '''
clst = cluster.KMeans(n_clusters=4) # 设定预计的类别个数，也可不设置
clst.fit(X)
labels = clst.predict(X) # 聚类结果

''' 绘制数据分布图 '''
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