import pandas as pd
from sklearn.model_selection import KFold, cross_val_score

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\Backup\Data\diabetes\pima-indians-diabetes.csv', names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]


""" Bagged Decision Tree """
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
cart = DecisionTreeClassifier()
model = BaggingClassifier(base_estimator=cart,n_estimators=100,random_state=1)
kfold = KFold(n_splits=10,random_state=2)
result = cross_val_score(model,X,Y,cv=kfold)
print(f'Bagged Decision Tree: {result.mean():>10}')


""" 随机森林 """
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100,max_features=3,random_state=3)
kfold = KFold(n_splits=10,random_state=2)
result = cross_val_score(model,X,Y,cv=kfold)
print(f'随机森林: {result.mean():>10}')


""" 极端随机树 """
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier(n_estimators=100,max_features=7,random_state=3)
kfold = KFold(n_splits=10,random_state=2)
result = cross_val_score(model,X,Y,cv=kfold)
print(f'极端随机树: {result.mean():>10}')


""" Adaboost """
from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier(n_estimators=30, random_state=1)
kfold = KFold(n_splits=10,random_state=2)
result = cross_val_score(model,X,Y,cv=kfold)
print(f'Adaboost: {result.mean():>10}')


""" 随机梯度提升 """
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=30, random_state=1)
kfold = KFold(n_splits=10,random_state=2)
result = cross_val_score(model,X,Y,cv=kfold)
print(f'随机梯度提升: {result.mean():>10}')


""" voting """
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\Data\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
y = diabetes[:,8]

model_1 = DecisionTreeClassifier()
model_2 = SVC(gamma='auto')

models = []
models.append(('DecisionTreeClassifier',model_1))
models.append(('SVC',model_2))

ensemble_model = VotingClassifier(estimators=models)
kfold = KFold(n_splits=10,random_state=2)
result = cross_val_score(ensemble_model,X,y,cv=kfold)
print(f'Voting: {result.mean():>10}')