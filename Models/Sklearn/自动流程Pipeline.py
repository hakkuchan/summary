import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline,FeatureUnion
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from numpy import set_printoptions
set_printoptions(precision=3)

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\Backup\Data\diabetes\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]

features = []
features.append(('pca',PCA()))
features.append(('select_best',SelectKBest(k=6)))

steps = []
steps.append(('Standaridize',StandardScaler()))
steps.append(('feature_union',FeatureUnion(features)))
steps.append(('LR',LogisticRegression(solver='lbfgs')))

model = Pipeline(steps)
kfold = KFold(n_splits=10,random_state=1)
result = cross_val_score(model,X,Y,cv=kfold)

print(result.mean())