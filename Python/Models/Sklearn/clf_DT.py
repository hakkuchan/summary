""" 决策树分类：
    
    · 基本思想：计算所有特征的信息熵，基于信息熵最大的特征，把数据集划分为2个子数据集
      对子数据集进行同样的操作，构建二叉树，直至样本按类别被分开
    
    · 剪枝（以提高其泛化性能）
      预剪枝：对节点划分前先估计能不能提高泛化能力，若不能则停止划分并把当前节点设为叶节点
      后剪枝：生成完整的决策树，之后从递归地研究删除当前叶节点能否提高泛化能力，如能则删掉当前叶节点
"""

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import datasets
from sklearn import model_selection
from sklearn.tree import export_graphviz
import pydotplus

# Data: Iris
X = datasets.load_iris().data
y = datasets.load_iris().target

# Modeling（目前还无法利用sklearn的决策树接口直接做后剪枝）
model = tree.DecisionTreeClassifier(
                                    criterion='gini',  # 设置最优划分属性的评价标准
                                    splitter='best',   # 设置划分原则
                                    max_depth=None,    # 树的最大深度，可用于预剪枝
                                    min_samples_split=2, # 每个内部节点最少包含的样本数，可用于预剪枝
                                    min_samples_leaf=1,  # 每个叶节点最少包含的样本数，可用于预剪枝
                                    min_weight_fraction_leaf=0.0,  # 叶节点中样本的最小权重系数                                    
                                    max_features=None, # 寻找best split时考虑的特征数量
                                    random_state=None, # 设置随机种子
                                    max_leaf_nodes=None, # 指定最大的叶节点数量
                                    min_impurity_decrease=0.0,
                                    class_weight=None, # 指定分类的权重
                                    presort=False  # 是否提前排序数据，从而加速寻找最优划分的过程（而对于大样本量的数据集，排序过程慢，不建议使用）
                                   )
 
# Train & Test
kfold = model_selection.KFold(n_splits=10,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Accuracy of DT: {result.mean()*100:.2f}%')

# 生成决策树图
model.fit(X,y)
dot_data = tree.export_graphviz(model, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_png('E:\Work\Jupyter\Data\DT_graph/DT_iris.png')