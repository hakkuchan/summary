import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import datasets
from sklearn import model_selection
from sklearn.tree import export_graphviz
import pydotplus

''' 准备数据 '''
db = datasets.load_iris()
X = db.data
y = db.target

''' 建立决策树模型 '''
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
 # 目前还无法利用sklearn的决策树接口直接做后剪枝
 
''' 学习及预测 '''
print('|{:>10s}|{:>10s}|'.format('Batch', 'Acc'))
kfold = model_selection.KFold(n_splits=10, random_state=1)
batch = 1
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    model.fit(X_train,y_train)
    print(f'|{batch:>10.0f}|{model.score(X_test, y_test):>10.4f}|')
    batch += 1
out = model_selection.cross_val_score(model, X, y, cv=kfold)
print(f'Mean Accuracy：{out.mean():.4f} ± {out.std():.4f}')

''' 生成决策树图 '''
model.fit(X,y)
dot_data = tree.export_graphviz(model, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_png('E:\Work\Jupyter\Data\Out/DT_iris.png')