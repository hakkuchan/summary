import pandas as pd
from sklearn.linear_model import LogisticRegression
from numpy import set_printoptions  # 设定打印格式
set_printoptions(precision=3)

""" 导入数据 """
name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\data\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
y = diabetes[:,8]


""" 二分类的ROC_AUC指标 """
from sklearn.model_selection import KFold, cross_val_score
model = LogisticRegression(solver='liblinear')
kfold = KFold(n_splits=10,random_state=1)
result = cross_val_score(model,X,y,cv=kfold,scoring='roc_auc')
print(f'AUC: {result.mean():.3f} ± {result.std():.3f}')


""" 混淆矩阵（比较分类结果和实际测得值）"""
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=2)
model = LogisticRegression(solver='liblinear')
model.fit(X_train,y_train)
matrix = confusion_matrix(y_test, model.predict(X_test))
classes = ['0','1']
result = pd.DataFrame(data=matrix,index=classes,columns=classes)
print(result)


""" 分类报告 (精确率，召回率，二者调和值) """
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=2)
model = LogisticRegression(solver='liblinear')
model.fit(X_train,y_train)
report= classification_report(y_test, model.predict(X_test))
print(report)