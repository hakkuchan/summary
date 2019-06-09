import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import neighbors
from sklearn import model_selection


""" datasets for regression """
db = datasets.load_diabetes()
X = db.data
y = db.target


""" build models """
model = neighbors.KNeighborsRegressor(
                                      n_neighbors= 3,
                                      weights='uniform',
                                      algorithm='kd_tree',
                                      leaf_size=30,
                                      p=2,
                                      metric='minkowski',
                                      metric_params=None,
                                      n_jobs=-1
                                     )


print('|{:>10s}|{:>10s}|'.format('Batch', 'KNN MSE'))
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