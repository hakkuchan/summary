""" 决策树回归：
    
    · 思想：根据划分准则选择特征，不断划分训练集数据集，直至形成叶节点（具体取值）
    针对测试集数据，逐层向下，最终落到某一取值(附近)
"""

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import datasets
from sklearn import model_selection, metrics
from sklearn.tree import export_graphviz
import pydotplus

# Data：Boston housing price
X = datasets.load_boston().data
y = datasets.load_boston().target

# Modeling
model = tree.DecisionTreeRegressor(
                                   criterion='mse', # 设置划分准则
                                   splitter='best', # 设置划分原则 
                                   max_depth=4,  # 树的最大深度，可用于预剪枝
                                   min_samples_split=2, # 每个内部节点最少包含的样本数，可用于预剪枝
                                   min_samples_leaf=1,  # 每个叶节点最少包含的样本数，可用于预剪枝
                                   min_weight_fraction_leaf=0.0, # 叶节点中样本的最小权重系数
                                   max_features=None,   # 寻找best split时考虑的特征数量
                                   random_state=1,      # 设置随机种子
                                   max_leaf_nodes=None, # 指定最大的叶节点数量
                                   min_impurity_decrease=0.0,
                                   presort=False  # 是否提前排序数据，从而加速寻找最优划分的过程（而对于大样本量的数据集，排序过程慢，不建议使用）
                                  )

# Train & Test
mse = metrics.make_scorer(metrics.mean_squared_error)
results = model_selection.cross_val_score(model, X, y, cv=10, scoring=mse)
print(f'RMSE of DT : {results.mean()**0.5:.2f}')

# 生成决策树图
model.fit(X,y)
dot_data = tree.export_graphviz(model, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_png('E:\Work\Jupyter\Data\DT_graph/DT_Boston.png')