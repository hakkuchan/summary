""" 目录：
     |
     |—— 1. 简单分割验证
     |
     |—— 2. K折交叉验证
     |
     |—— 3. 留一验证
     | 
     |—— 4. 留P验证
     |
     |—— 5. cross_val_score
"""


from sklearn import datasets
from sklearn import model_selection
from sklearn import svm
from sklearn import preprocessing
from sklearn import metrics

iris = datasets.load_iris()
X = iris.data    # (150, 4)
y = iris.target  # (150,)


""" 1. 简单分离验证 """
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                    test_size=0.2,  # 20%的数据作为测试集
                                                                    random_state=1  # 设置随机种子
                                                                   )
print(X_train.shape, y_train.shape)  # >>> (120, 4) (120,)  150*0.8=120
print(X_test.shape, y_test.shape)    # >>> (30, 4) (30,)  150*0.2=30



""" 2. K折交叉验证 """
kfold = model_selection.KFold(n_splits=10, random_state=1)
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
print(X_train.shape, y_train.shape)  # >>> (135, 4) (135,)  150*0.9=135
print(X_test.shape, y_test.shape)    # >>> (15, 4) (15,)  150*0.1=15



""" 3. 留一验证 """
loo = model_selection.LeaveOneOut()
for train,test in loo.split(X):
    X_train,X_test = X[train],X[test]
    y_train,y_test = y[train],y[test]
print(X_train.shape, y_train.shape)  # >>> (149, 4) (149,)
print(X_test.shape, y_test.shape)    # >>> (1, 4) (1,)



""" 4. 留P验证 """
lpo = model_selection.LeavePOut(p=2)
for train,test in lpo.split(X):
    X_train,X_test = X[train],X[test]
    y_train,y_test = y[train],y[test]
print(X_train.shape, y_train.shape)  # >>> (148, 4) (148,)
print(X_test.shape, y_test.shape)    # >>> (2, 4) (2,)



""" 5. cross_val_score """
model = svm.SVC(gamma='auto', kernel='rbf')
kfold = model_selection.KFold(n_splits=10, random_state=1)
out = model_selection.cross_val_score(
                                      model,
                                      X, y, 
                                      cv=kfold, # 设置分割策略，cv也可以是3、4中的 loo，lpo
                                      scoring='accuracy' # 设置评价指标，对于非内置指标，见'make_scorer'
                                     ) 
print(out)
print(f'Aaccuracy: {out.mean()*100:.2f} ± {out.std()*100:.2f}%')

''' make_scorer '''
mse = metrics.make_scorer(metrics.mean_squared_error)
out = model_selection.cross_val_score(……, scoring=mse) 