import pandas as pd
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
print(result.mean())