""" 直接构建 """
grade = {'Jack': 98, 'Mike': 99}


""" 关键字参数来指定键值对 """ 
dict(Jack=98, Mike=99)


""" dict构造函数 """
dict([('Jack', 98), ('Mike': 99)])


""" 合并字典 """
x = {'a':1, 'b':2}
y = {'c':3, 'd':4}
z = {**x, **y}


""" 字典取代多个 elif """
def fun(x):
    if x == 1:
        print('one')
    elif x == 2:
        print('two')
    elif x == 3:
        print('three')

# 等价于:
def fun(x):
    return {1:'one', 2:'two', 3:'three'}.get(x)


""" 字典的一种用法 """
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