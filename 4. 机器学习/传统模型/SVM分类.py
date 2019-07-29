import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn import model_selection


"""
|SVM 分类
|
|--1. LinearSVC
|
|--2. SVC
|
"""

""" datasets for classification """
db = datasets.load_iris()
X = db.data
y = db.target

""" build models """
models = {}
models['LSVC'] = svm.LinearSVC(penalty='l2', 
                                    loss='squared_hinge', 
                                    dual=False, 
                                    tol=0.00001, 
                                    C=1.0,
                                    multi_class='ovr',
                                    fit_intercept=True, 
                                    intercept_scaling=1, 
                                    class_weight=None,
                                    verbose=1, 
                                    random_state=None, 
                                    max_iter=1000)

models['SVC'] = svm.SVC(C=1.0,
                        kernel='rbf',
                        degree=3,
                        gamma='auto',
                        coef0=0.0,
                        shrinking=True,
                        probability=False,
                        tol=0.001,
                        cache_size=200,
                        class_weight=None,
                        verbose=False,
                        max_iter=-1,
                        decision_function_shape='ovr',
                        random_state=None)

print('|{:>10s}|{:>10s}|{:>10s}|{:>10s}|'.format('No use','Batch', 'LSVC Acc', 'SVC Acc'))
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