import pandas as pd
from sklearn import model_selection
from sklearn import preprocessing
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\Data\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
y = diabetes[:,8]

""" build models """
models = {}
models['Bag'] = DecisionTreeClassifier(class_weight=None, 
                                       criterion='gini', 
                                       max_depth=None,
                                       max_features=None, 
                                       max_leaf_nodes=None,
                                       min_impurity_decrease=0.0, 
                                       min_impurity_split=None,
                                       min_samples_leaf=1, 
                                       min_samples_split=2,            
                                       min_weight_fraction_leaf=0.0, 
                                       presort=False, 
                                       random_state=None,
                                       splitter='best')

models['Boost'] = AdaBoostClassifier(algorithm='SAMME.R', 
                                     base_estimator=None,
                                     learning_rate=1.0, 
                                     n_estimators=30, 
                                     random_state=1)

models['Grad'] = GradientBoostingClassifier(criterion='friedman_mse',
                                            init=None,
                                            learning_rate=0.1, 
                                            loss='deviance', 
                                            max_depth=3,
                                            max_features=None, 
                                            max_leaf_nodes=None,
                                            min_impurity_decrease=0.0, 
                                            min_impurity_split=None,
                                            min_samples_leaf=1, 
                                            min_samples_split=2,
                                            min_weight_fraction_leaf=0.0, 
                                            n_estimators=30,
                                            n_iter_no_change=None, 
                                            presort='auto', 
                                            random_state=1,
                                            subsample=1.0, 
                                            tol=0.0001, 
                                            validation_fraction=0.1,
                                            verbose=0, 
                                            warm_start=False)

kfold = model_selection.KFold(n_splits=10, random_state=2)

print('|{:>10s}|{:>10s}|{:>10s}|{:>10s}|'.format('Batch', 'Bag', 'Boost', 'Grad'))
batch = 1
for train,test in kfold.split(X):
    X_train,X_test = X[train],X[test]
    y_train,y_test = y[train],y[test]
    results = []
    for name in models:
        model = models[name]
        model.fit(X_train, y_train)
        results.append(round(model.score(X_test, y_test),4))
    print('|{:>10.0f}|{:>10.4f}|{:>10.4f}|{:>10.4f}|'.format(batch,results[0],results[1],results[2]))
    batch += 1