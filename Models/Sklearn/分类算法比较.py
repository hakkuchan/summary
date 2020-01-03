import pandas as pd
from numpy import set_printoptions  # 设定打印格式
from sklearn.linear_model import LogisticRegression                   # 逻辑回归算法
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis  # LDA算法
from sklearn.neighbors import KNeighborsClassifier                    # 最近邻算法
from sklearn.tree import DecisionTreeClassifier                       # 决策树算法
from sklearn.svm import SVC                                           # 支持向量机算法
from sklearn.naive_bayes import GaussianNB                            # 贝叶斯算法
from sklearn.model_selection import KFold, cross_val_score
import matplotlib.pyplot as plt
%matplotlib inline
set_printoptions(precision=3)

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\data\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]

models = {}
models['LR'] = LogisticRegression(solver='liblinear')
models['LDA'] = LinearDiscriminantAnalysis()
models['KNN'] = KNeighborsClassifier()
models['CART'] = DecisionTreeClassifier()
models['SVC'] = SVC(gamma='auto')
models['NB'] = GaussianNB()

kfold = KFold(n_splits=10,random_state=1)
results = []
for name in models:
    result = cross_val_score(models[name],X,Y,cv=kfold)
    results.append(result)
    print('%s: %.3f(%.3F)' % (name,result.mean(),result.std()))

fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(111)
fig.suptitle('Algorithm Comparison')
plt.boxplot(results)
ax.set_xticklabels(models.keys())
plt.show()