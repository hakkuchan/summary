import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.externals.joblib import dump,load

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\data\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=1)

""" 训练模型 """
model = LogisticRegression()
model.fit(X_train,Y_train)

""" 保存模型 """
model_file = 'E:\Work\Jupyter\data\sklearn_model.sav'
with open(model_file, 'wb') as model_f:
    dump(model, model_f)

""" 加载模型 """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals.joblib import dump,load

name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\data\pima-indians-diabetes.csv',names=name)
diabetes = diabetes_table.values
X = diabetes[:,0:8]
Y = diabetes[:,8]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=1)

model_file = 'E:\Work\Jupyter\data\sklearn_model.sav'
with open(model_file,'rb') as model_f:
    loaded_model = load(model_f)
    result = loaded_model.score(X_test,Y_test)
    print('Result: %.3f%%' % (result*100))