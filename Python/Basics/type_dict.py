""" · 字典
      字典中包含着一系列"键(key)-值(value)对"，通过 key 索引 value
      字典查找和插入的速度极快，不会随着key的增加而变慢。但字典需要占用大量的内存。
      字典是可变类型，但其中的 key 必须是不可变类型（数值、逻辑值、字符串、元组），value 可以是任何数据类型

    · 操作：创建、嵌套、添加、合并、大小、删除(del, pop, clear)、提取(get, keys, values, items)  
"""


""" 1. 创建 """
# 创建方法 1
a = {'Jack': 98, 'Mike': 99}          
# 创建方法 2
b = dict(Jack = 98, Mike = 99)
# 创建方法 3
c = dict([('Jack',98), ('Mike',99)])
# 创建方法 4
d = {}  
d['Jack'] = 98
d['Mike'] = 99

print(r == s == t == u) # >>> True


""" 2. 嵌套 """
info = {'name':'Mike', 'city':'Shanghai', 'contact':{'address':'somewhere', 'num':666}}
print(info['contact']['address'])


""" 3. 添加 """
m = {'a':1, 'b':2}
m.update({'c':3})  # .update()添加数据
print(m)  # >>> {'a': 1, 'b': 2, 'c': 3}


""" 4. 合并 """
m = {'a':1, 'b':2}
n = {'c':3, 'd':4}
print({**m, **n}) # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}


""" 5. 大小 """
m = {'a':1, 'b':2}
print(len(m))


""" 6. 删除 """
m = {'a':1, 'b':2}
del m['a']  # del删除指定键值对
print(m)    # >>> {'b': 2}

m = {'a':1, 'b':2}
n = m.pop('b')  # .pop()删除指定标签的数据项并返回数据值
print(m, n)     # >>> {'a': 1} 2

m = {'a':1, 'b':2}
m.clear()  # .clear()清空字典  
print(m)   # >>> {}


""" 7. 提取 """
m = {'a':1, 'b':2}
print(m.get('a')) # .get() 提取 key 'a' 对应的 value
print(m.keys())   # .keys() 提取 key
print(m.values()) # .values() 提取 value
print(m.items())  # .items() 提取键值对


""" * 技巧：用字典取代多个elif """
def fun(x):
    if x == 1:
        print('one')
    elif x == 2:
        print('two')
# 等价于:
def fun(x):
    return {1:'one', 2:'two'}.get(x)
