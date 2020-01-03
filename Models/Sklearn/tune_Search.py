""" 参数优化 """

''' 1. 随机搜索优化参数 '''
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\Backup\Data\diabetes\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]

model = Ridge()

param_grid = {'alpha':uniform()}
grid = RandomizedSearchCV(estimator=model, param_distributions=param_grid,
                          n_iter=100,random_state=7, cv=5)
grid.fit(X,Y)

print('最高得分：%.3f' % grid.best_score_)
print('最优参数：%s' % grid.best_estimator_.alpha)



''' 2. 网格搜索优化参数 '''
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\Backup\Data\diabetes\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]

model = Ridge()

param_grid = {'alpha':[1,0.1,0.01,0.001,0]}
grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
grid.fit(X,Y)

print('最高得分：%.3f' % grid.best_score_)
print('最优参数：%s' % grid.best_estimator_.alpha)