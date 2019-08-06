""" 直接构建 """
grade = {'Jack': 98, 'Mike': 99}


""" 关键字参数来指定键值对 """ 
dict(Jack = 98, Mike = 99)


""" dict构造函数 """
dict([('Jack', 98), ('Mike', 99)])


""" 合并字典 """
x = {'a':1, 'b':2}
y = {'c':3, 'd':4}
z = {**x, **y}


""" 通过.copy()方法，复制一个新的字典 """
a = {'m':1 , 'n':2 , 'p':3}
b = a.copy()
a.update({'q':4})
print(a,b)


""" 对于嵌套字典，输出嵌套内容，通过重复指向来输出 """
poi = {'name':'shop', 'city':'shanghai', 'information':{'address':'somewhere', 'num':666}}
print(poi['information']['address'])


""" 字典的元素遍历 """
poi = {'name':'shop', 'city':'shanghai', 'information':{'address':'somewhere', 'num':666}}
for key in poi.keys():
    print(key)
print('-------')

for value in poi.values():
    print(value)
print('-------')


""" for函数遍历 """
for (k,v) in poi.items():
    print('key为 %s, value为 %s' %(k,v))
print('-------')  



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