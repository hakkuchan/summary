import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import neighbors
from sklearn import model_selection


""" datasets for classification """
db = datasets.load_iris()
X = db.data
y = db.target

""" build models """
model = neighbors.KNeighborsClassifier(
                                       n_neighbors=5,
                                       weights='uniform',
                                       algorithm='brute',
                                       leaf_size=30,
                                       p=2,
                                       metric='minkowski',
                                       n_jobs=-1
                                      )

print('|{:>10s}|{:>10s}|'.format('Batch', 'KNN Acc'))
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