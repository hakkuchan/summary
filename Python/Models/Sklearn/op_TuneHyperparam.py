""" 超参数优化 """
from sklearn import datasets
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import svm
import scipy

# Data：Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, 
                                                                    test_size=0.2, 
                                                                    random_state=1)
""" 1. 网格搜索 """
# 设置超参数网格
hyperparams = {'C':[1,10,100], 
               'kernel':['linear', 'rbf', 'poly'],
               'gamma':['auto','scale', 1, 2, 3]}
# 设置模型
clf = model_selection.GridSearchCV(svm.SVC(), hyperparams, cv=10)
clf.fit(X, y)
print(f'Best hyperparameters: {clf.best_params_}')
print(f'Top score: {clf.best_score_}')


""" 2. 随机搜索 (从scipy.stats提供的分布类型中，连续、随机挑选一些值作为超参数) """
# 设置超参数分布
hyperparams = {'C': scipy.stats.expon(),
               'gamma': scipy.stats.uniform()}
# 设置模型
clf = model_selection.RandomizedSearchCV(svm.SVC(), hyperparams, cv=10, random_state=1)
clf.fit(X, y)
print(f'Best hyperparameters: {clf.best_params_}')
print(f'Top score: {clf.best_score_}')