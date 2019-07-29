import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn import model_selection


""" datasets for classification """
db = datasets.load_iris()
X = db.data
y = db.target

""" build models """
model = tree.DecisionTreeClassifier(
                                   criterion='gini',
                                   splitter='best',
                                   max_depth=None,
                                   min_samples_split=2,
                                   min_samples_leaf=1,
                                   min_weight_fraction_leaf=0.,
                                   max_features=None,
                                   random_state=None,
                                   max_leaf_nodes=None,
                                   min_impurity_decrease=0.,
                                   class_weight=None,
                                   presort=False
                                   )

print('|{:>10s}|{:>10s}|'.format('Batch', 'DT Acc'))
kfold = model_selection.KFold(n_splits=10, random_state=1)
batch = 1
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    results = []
    model.fit(X_train,y_train)
    results.append(round(model.score(X_test, y_test),4))
    print('|{:>10.0f}|{:>10.4f}|'.format(batch,results[0]))
    batch += 1