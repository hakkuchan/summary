import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import model_selection
 
db = pd.read_csv('E:\Work\Jupyter\data\char_data.csv').values
X = db[:,1:11]
y = db[:,11].astype('int')

""" 简单分离验证 """
X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=0.3, random_state=1)   # 30%的数据作为测试集


""" K折交叉验证 """
# 方法 1：
kfold = model_selection.KFold(n_splits=10, random_state=2)
for train,test in kfold.split(X):
    X_train,X_test = X[train],X[test]
    y_train,y_test = y[train],y[test]
    
# 方法 2: cross_val_score
model = svm.SVC(gamma = 'auto')
kfold = model_selection.KFold(n_splits=10, random_state=2)
out = model_selection.cross_val_score(model,X,y,cv=kfold)
print('Mean_accuracy: {:.3f}% -- STD: {:.3f}' .format(out.mean()*100,out.std()*100))

   
""" 留一验证 """
# 方法 1: 
loo = model_selection.LeaveOneOut()
for train,test in loo.split(X):
    X_train,X_test = X[train],X[test]
    y_train,y_test = y[train],y[test]

# 方法 2: cross_val_score
from sklearn.model_selection import LeaveOneOut, cross_val_score
model = svm.SVC(gamma = 'auto')
loo = model_selection.LeaveOneOut()
out = cross_val_score(model,X,y,cv=loo)
print('Mean_accuracy: {:.3f}% -- STD: {:.3f}' .format(out.mean()*100,out.std()*100))