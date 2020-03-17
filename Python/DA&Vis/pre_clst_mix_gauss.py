""" 混合高斯模型 
    
    · 原理：把N个样本分为K个簇，确保同簇样本落在同一高斯分布的概率最大
    · 步骤：
      Step 1: 设定有K个簇，生成K个高斯分布，随机给每个分布函数赋值均值和方差
      Step 2: 计算每个样本其在各个高斯分布下的概率
      Step 3: 对于每个高斯分布，每个样本对该高斯分布的贡献可以由其概率表示，
              概率越大则表示贡献越大，反之亦然
              把样本对该高斯分布的贡献作为权重来计算加权的均值和方差，替代其原本的均值和方差
      Step 4: 重复Step 2、3，直至每个高斯分布的均值和方差收敛
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import mixture
%matplotlib inline

''' Data: Iris '''
X = datasets.load_iris().data # 150个样本，4个特征（萼长、萼宽、瓣长、瓣宽）
X = X[:,(0,2)] # 只考虑 萼长 和 瓣长

''' GaussianMixture模型 '''
clst = mixture.GaussianMixture(n_components=4)  # 设定簇个数，也可不设置
labels = clst.fit_predict(X) # 训练GaussianMixture模型并输出每个样本的簇标记

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