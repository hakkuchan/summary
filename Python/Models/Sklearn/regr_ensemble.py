""" · 集成回归器
    |
    |—— 1. Boosting
    |   |
    |   |—— 1.1 Adaboost
    |   |
    |   |—— 1.2 GBRT
    |
    |
    |—— 2. Bagging
        |
        |—— 2.1 bagging
        |
        |—— 2.2 Random Forest
        |
        |—— 2.3 Extra tree
        
    · 集成回归器与集成分类器各个算法的思想大致相同，不再赘述
      区别在于：集成回归器的结果是个体回归器结果的平均，集成分类器的结果是个体分类器的投票结果
"""

from sklearn import datasets
from sklearn import ensemble
from sklearn import neighbors, svm, tree
from sklearn import metrics
from sklearn import model_selection

# Data: Boston housing price
X = datasets.load_boston().data
y = datasets.load_boston().target
# Score
mse = metrics.make_scorer(metrics.mean_squared_error)


""" 1. Boosting """
''' 1.1 Adaboost '''
base = neighbors.KNeighborsRegressor(n_neighbors=3)
model = ensemble.AdaBoostRegressor(base_estimator=base,
                                   n_estimators=30,
                                   learning_rate=0.1,
                                   random_state=1
                                   )
kfold = model_selection.KFold(n_splits=10, random_state=1)
result = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=mse)
print(f'RMSE of Adaboost: {result.mean()**0.5:.2f}')


''' 1.2 GradientBoostingRegressor (GBRT) '''
model = ensemble.GradientBoostingRegressor(n_estimators=30, random_state=1)
kfold = model_selection.KFold(n_splits=10,random_state=2)
result = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=mse)
print(f'RMSE of GBRT: {result.mean()**0.5:.2f}')



""" 2. Bagging """
''' 2.1 BaggingRegressor '''
base = tree.DecisionTreeRegressor()
model = ensemble.BaggingRegressor(base_estimator=base,
                                  n_estimators=10,
                                  random_state=1)
kfold = model_selection.KFold(n_splits=20,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'RMSE of Bagging: {result.mean()**0.5:.2f}')


''' 2.2 RandomForestRegressor (RF) '''
model = ensemble.RandomForestRegressor(n_estimators=30, random_state=1)
kfold = model_selection.KFold(n_splits=10,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'RMSE of RF: {result.mean()**0.5:.2f}')


''' 2.3 ExtraTreesRegressor (ET) '''
model = ensemble.ExtraTreesRegressor(n_estimators=100,
                                     max_features=8,
                                     random_state=3)
kfold = model_selection.KFold(n_splits=10,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'RMSE of ET: {result.mean()**0.5:.2f}')
