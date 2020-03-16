""" 混合高斯模型 """

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import mixture
%matplotlib inline

''' Data: Iris '''
X = datasets.load_iris().data # 150个样本，4个特征（萼长、萼宽、瓣长、瓣宽）
X = X[:,(0,2)] # 只考虑 萼长 和 瓣长

''' 调用 GaussianMixture方法 '''
clst = mixture.GaussianMixture(n_components=4)  # 设定预计的类别个数，也可不设置
labels = clst.fit_predict(X) # 聚类结果

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