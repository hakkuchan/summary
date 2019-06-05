import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn import model_selection


"""
|SVM 回归
|
|--1. LinearSVR
|
|--2. SVR
|
"""


""" datasets for regression """
db = datasets.load_diabetes()
X = db.data
y = db.target


""" build models """
models = {}

models['LSVR'] = svm.LinearSVR(epsilon=0.1, 
                               tol=1e-4, 
                               C=1.0, 
                               loss='squared_epsilon_insensitive', 
                               fit_intercept=True,
                               intercept_scaling=1,
                               dual=True,
                               verbose=0,
                               random_state=None,
                               max_iter=1000)

models['SVR'] = svm.SVR(kernel='rbf',
                        degree=3,
                        gamma='auto',
                        coef0=0.0,
                        tol=1e-3,
                        C=1.0,
                        epsilon=0.1,
                        cache_size=1.0,
                        verbose=False,
                        max_iter=-1)

print('|{:>10s}|{:>10s}|{:>10s}|'.format('Batch', 'LSVR MSE', 'SVR MSE'))
kfold = model_selection.KFold(n_splits=10, random_state=1)
batch = 1
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    results = []
    for name in models:
        model = models[name]
        model.fit(X_train,y_train)
        results.append(round(model.score(X_test, y_test),4))
    print('|{:>10.0f}|{:>10.4f}|{:>10.4f}|'.format(batch,results[0],results[1]))
    batch += 1