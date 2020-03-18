from sklearn import datasets
from sklearn import svm
from sklearn import model_selection
from sklearn.externals.joblib import dump,load

''' 训练模型 '''
# Data: Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.2,random_state=1)
# 模型
model = svm.SVC(gamma='auto')
model.fit(X_train,y_train)

''' 保存模型 '''
path = 'E:\Work\Jupyter\data\sklearn_model.sav'
with open(path, 'wb') as f:
    dump(model, f)

''' 加载模型 '''
# Data：Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.2,random_state=1)
# 加载
path = 'E:\Work\Jupyter\data\sklearn_model.sav'
with open(path,'rb') as f:
    load_model = load(f)
    result = load_model.score(X_test,y_test)
    print(f'Result: {result*100:.2f} %')