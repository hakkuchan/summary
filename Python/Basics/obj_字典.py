""" · 目录
    |
    |—— 1. 概述
    |
    |—— 2. 操作：创建、嵌套、添加、合并、大小、删除(del, pop, clear)、提取(get, keys, values, items)
    |
    |—— 3. 技巧：取代elif、对比模型            
"""



""" 1. 概述
    
    · 字典中包含着一系列 key : value 对，通过 key 来索引 value
    
    · 字典是可变类型，
      但其中的 key 必须是不可变类型（数值、逻辑值、字符串、元组），
      value 可以是任何数据类型
"""



""" 2. 操作 """

# 创建
r = {'Jack': 98, 'Mike': 99}          # 直接创建法
s = dict(Jack = 98, Mike = 99)        # dict函数创建法 1
t = dict([('Jack',98), ('Mike',99)])  # dict构造创建法 2
print(r == s == t) # >>> True

# 嵌套
info = {'name':'Mike', 'city':'Shanghai', 'contact':{'address':'somewhere', 'num':666}}
print(info['contact']['address'])

# 添加
m = {'a':1, 'b':2}
m.update({'c':3})  # .update()添加数据
print(m)  # >>> {'a': 1, 'b': 2, 'c': 3}

# 合并
m = {'a':1, 'b':2}
n = {'c':3, 'd':4}
print({**m, **n}) # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 大小
m = {'a':1, 'b':2}
print(len(m))

# 删除
m = {'a':1, 'b':2}
del m['a']  # del删除指定标签的数据项
print(m)    # >>> {'b': 2}

m = {'a':1, 'b':2}
n = m.pop('b')  # .pop()删除指定标签的数据项并返回数据值
print(m, n)     # >>> {'a': 1} 2

m = {'a':1, 'b':2}
m.clear()  # 清空字典
print(m)   # >>> {}

# 提取
m = {'a':1, 'b':2}
print(m.get('a')) # .get() 提取 key 'a' 对应的 value
print(m.keys())   # .keys() 提取 key
print(m.values()) # .values() 提取 value
print(m.items())  # .items() 提取键值对



""" 3. 技巧 """

''' (1) 字典取代多个 elif '''
def fun(x):
    if x == 1:
        print('one')
    elif x == 2:
        print('two')
# 等价于:
def fun(x):
    return {1:'one', 2:'two'}.get(x)


''' (2) 利用字典对比模型 
    
    models = {}
    models['LR'] = LogisticRegression(solver='liblinear')
    models['SVC'] = SVC(gamma='auto')
    models['KNN'] = KNeighborsClassifier()
    kfold = KFold(n_splits=10,random_state=1)
    for name in models:
        result = cross_val_score(models[name],X,Y,cv=kfold)
    print(result)
'''