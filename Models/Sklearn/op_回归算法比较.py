import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression     # 线性回归
from sklearn.linear_model import Ridge                # 岭回归
from sklearn.linear_model import Lasso                # 套索回归
from sklearn.linear_model import ElasticNet           # 弹性网络回归
from sklearn.neighbors import KNeighborsRegressor     # K近邻回归
from sklearn.tree import DecisionTreeRegressor        # 回归树算法
from sklearn.svm import SVR                           # 支持向量机回归
from sklearn.model_selection import KFold, cross_val_score
import matplotlib.pyplot as plt
from numpy import set_printoptions  # 设定打印格式
%matplotlib inline
set_printoptions(precision=3)

boston_dataset = datasets.load_boston()
Feature = boston_dataset.data
Price = boston_dataset.target
boston_row = pd.DataFrame(Feature)
boston_row.columns = boston_dataset.feature_names
boston_row['PRICE'] = Price
boston = boston_row.values

X = boston[:,0:13]
Y = boston[:,13]

models = {}
models['LR'] = LinearRegression()
models['RIDGE'] = Ridge()
models['LASSO'] = Lasso()
models['EN'] = ElasticNet()
models['KNR'] = KNeighborsRegressor()
models['DTR'] = DecisionTreeRegressor()
models['SVR'] = SVR()

kfold = KFold(n_splits=10,random_state=1)
results = []
for name in models:
    result = cross_val_score(models[name],X,Y,cv=kfold,scoring='neg_mean_absolute_error')
    results.append(result)
    print('%s: %.3f(%.3F)' % (name,result.mean(),result.std()))

fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(111)
fig.suptitle('Algorithm Comparison')
plt.boxplot(results)
ax.set_xticklabels(models.keys())
plt.show()