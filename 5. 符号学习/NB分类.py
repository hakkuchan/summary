import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import naive_bayes
from sklearn import model_selection


""" datasets for classification """
db = datasets.load_digits()
X = db.data
y = db.target

""" build models """
models = {}

models['Gauss'] = naive_bayes.GaussianNB()

models['Multi'] = naive_bayes.MultinomialNB(alpha=1.0, 
                                            fit_prior=True, 
                                            class_prior=None)

models['Bernoulli'] = naive_bayes.BernoulliNB(alpha=1.0,
                                              binarize=0.0,
                                              fit_prior=True,
                                              class_prior=None)


print('|{:>10s}|{:>10s}|{:>10s}|{:>10s}|'.format('Batch', 'Gauss Acc', 'Multi Acc', 'Bernoulli Acc'))
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
    print('|{:>10.0f}|{:>10.4f}|{:>10.4f}|{:>13.4f}|'.format(batch,results[0],results[1],results[2]))
    batch += 1