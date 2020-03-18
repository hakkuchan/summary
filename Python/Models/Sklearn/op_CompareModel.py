""" 1. 分类模型比较 """
from sklearn import datasets
from sklearn import model_selection, metrics
from sklearn import linear_model, discriminant_analysis, naive_bayes, neighbors, tree, svm
import matplotlib.pyplot as plt
%matplotlib inline

# Data: Iris
X = datasets.load_iris().data
y = datasets.load_iris().target

# 设置要对比的模型
models = {}
models['LR'] = linear_model.LogisticRegression(solver='liblinear', multi_class='auto')
models['LDA'] = discriminant_analysis.LinearDiscriminantAnalysis()
models['KNN'] = neighbors.KNeighborsClassifier()
models['NB'] = naive_bayes.GaussianNB()
models['Tree'] = tree.DecisionTreeClassifier()
models['SVC'] = svm.SVC(gamma='auto')

# 对比模型性能
kfold = model_selection.KFold(n_splits=10,random_state=1)
results = []
for name in models:
    result = model_selection.cross_val_score(models[name], X, y, cv=kfold, scoring='accuracy')
    results.append(result)
    print(f'{name:>10}: {result.mean():.4f} ± {result.std():.4f}')

# 绘图
fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(1,1,1)
fig.suptitle('Model Comparison')
plt.boxplot(results)
ax.set_xticklabels(models.keys())
plt.show()



""" 2. 回归模型比较 """
from sklearn import datasets
from sklearn import model_selection, metrics
from sklearn import linear_model, neighbors, tree, svm
import matplotlib.pyplot as plt
%matplotlib inline

# Data: Boston housing price
X = datasets.load_boston().data
y = datasets.load_boston().target

# 设置要对比的模型
models = {}
models['LR'] = linear_model.LinearRegression()
models['Ridge'] = linear_model.Ridge()
models['Lasso'] = linear_model.Lasso()
models['Elastic'] = linear_model.ElasticNet()
models['KNR'] = neighbors.KNeighborsRegressor()
models['Tree'] = tree.DecisionTreeRegressor()
models['SVR'] = svm.SVR(gamma='auto')

# 对比模型性能
kfold = model_selection.KFold(n_splits=10,random_state=1)
results = []
mse = metrics.make_scorer(metrics.mean_squared_error)
for name in models:
    result = model_selection.cross_val_score(models[name], X, y, cv=kfold, scoring=mse)
    results.append(result)
    print(f'{name:>10}: {result.mean():.4f} ± {result.std():.4f}')

# 绘图
fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(1,1,1)
fig.suptitle('Model Comparison')
plt.boxplot(results)
ax.set_xticklabels(models.keys())
plt.show()