""" 构建字典 """
grade = {'Jack': 98, 'Mike': 99}  # 直接构建法
dict(Jack = 98, Mike = 99)        # dict函数构建法 1
dict([('Jack',98), ('Mike',99)])  # dict构造构建法 2

""" 合并字典 """
x = {'a':1, 'b':2}
y = {'c':3, 'd':4}
z = {**x, **y}

""" 嵌套字典 """
info = {'name':'Mike', 'city':'Shanghai', 'contact':{'address':'somewhere', 'num':666}}
print(info['contact']['address'])

""" .copy() 复制一个新字典 (深拷贝) """
a = {'m':1, 'n':2, 'p':3}
b = a.copy()
a.update({'q':4})
print(a,b)

""" 遍历 """
info = {'name':'Mike', 'city':'Shanghai', 'contact':{'address':'somewhere', 'num':666}}
''' .keys() 取出键 '''
for key in info.keys():
    print(key)
''' .values() 取出值 '''
for value in info.values():
    print(value)
''' .items()取出键和值 '''
for (key, value) in info.items():
    print(key, value)

""" 字典取代多个 elif """
def fun(x):
    if x == 1:
        print('one')
    elif x == 2:
        print('two')
# 等价于:
def fun(x):
    return {1:'one', 2:'two'}.get(x)

""" 利用字典对比模型 """
'''
models = {}
models['LR'] = LogisticRegression(solver='liblinear')
models['NB'] = GaussianNB()
models['SVC'] = SVC(gamma='auto')
models['LDA'] = LinearDiscriminantAnalysis()
models['KNN'] = KNeighborsClassifier()
models['CART'] = DecisionTreeClassifier()
kfold = KFold(n_splits=10,random_state=1)
for name in models:
    result = cross_val_score(models[name],X,Y,cv=kfold)
print(result)
'''