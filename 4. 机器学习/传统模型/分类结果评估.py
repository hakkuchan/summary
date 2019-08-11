import pandas as pd
from sklearn.linear_model import LogisticRegression
from numpy import set_printoptions  # 设定打印格式
set_printoptions(precision=3)

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\data\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]


""" 二分类的ROC_AUC指标 """
from sklearn.model_selection import KFold,cross_val_score
model = LogisticRegression()
kfold = KFold(n_splits=10,random_state=1)
result = cross_val_score(model,X,Y,cv=kfold,scoring='roc_auc')
print('AUC %.3f(%.3f)' % (result.mean(),result.std()))


""" 混淆矩阵（比较分类结果和实际测得值）"""
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=2)
model = LogisticRegression()
model.fit(X_train,Y_train)
matrix = confusion_matrix(Y_test, model.predict(X_test))
classes = ['0','1']
result = pd.DataFrame(data=matrix,index=classes,columns=classes)
print(result)


""" 分类报告(精确率，召回率，二者调和值) """
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=2)
model = LogisticRegression()
model.fit(X_train,Y_train)
report= classification_report(Y_test, model.predict(X_test))
print(report)