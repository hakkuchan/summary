import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import datasets
from sklearn import model_selection
from sklearn.tree import export_graphviz
import pydotplus

# 准备数据
db = datasets.load_diabetes()
X = db.data
y = db.target

# 建立决策树模型
model = tree.DecisionTreeRegressor(
                                   criterion='mse',
                                   splitter='best',
                                   max_depth=None,
                                   min_samples_split=2,
                                   min_samples_leaf=1,
                                   min_weight_fraction_leaf=0.,
                                   max_features=None,
                                   random_state=None,
                                   max_leaf_nodes=None,
                                   min_impurity_decrease=0.,
                                   presort=False
                                  )

# 学习及预测
print('|{:>10s}|{:>10s}|'.format('Batch', 'R^2'))
kfold = model_selection.KFold(n_splits=10, random_state=1)
batch = 1
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    model.fit(X_train,y_train)
    print(f'|{batch:>10.0f}|{model.score(X_test, y_test):>10.4f}|')
    batch += 1
out = model_selection.cross_val_score(model, X, y, cv=kfold)
print(f'Mean R^2：{out.mean():.4f} ± {out.std():.4f}')

# 生成决策树图
model.fit(X,y)
dot_data = tree.export_graphviz(model, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_png('E:\Work\Jupyter\Data\Out/DT_diabetes.png')