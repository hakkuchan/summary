import numpy as np
import pandas as pd
from sklearn import feature_selection

db = pd.read_csv('E:\Work\Jupyter\data\char_data.csv').values
X = db[:,1:11]
y = db[:,11].astype('int')

""" 单变量特征选择 """  
newX =feature_select.VarianceThreshold(threshold=(0.8*(1-0.8))).fit_transform(X) # 按照差异程度（剔除差异小于阈值的特征）
# 其余略

""" 循环特征消除 """
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear')
rfe = feature_selection.RFE(estimator=model,n_features_to_select=3) # 选择逻辑回归为基模型，选出3个最重要的特征
rfe.fit(X,y)
print(rfe.n_features_)  # 输出所选择的特征个数
print(rfe.support_)     # 输出所选择的特征
print(rfe.ranking_)     # 所有特征重要性排序

""" 主成分分析（PCA 和 LDA）"""
from sklearn.decomposition import PCA
pca = PCA(n_components=3).fit(X)
print('解释方差：%s' % pca.explained_variance_ratio_)
print(pca.components_)

""" 决策树计算特征重要性 """
from sklearn.ensemble import ExtraTreesClassifier
DT = ExtraTreesClassifier(n_estimators=10).fit(X,y)
print('特征重要性得分：',DT.feature_importances_)