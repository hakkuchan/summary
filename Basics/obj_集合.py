""" 1. 集合概述
    
    · 集合是不重复元素的无序组合，
      集合会自动忽略重复的数据
      
    · 集合中不能加入可变类型数据（列表、字典、集合）
"""



""" 2. 操作 """

# 创建
m = {'a', 'b', 'c'}
n = set(['a', 'b', 'c'])
print(m == n)

# 增加
m = {'a', 'b'}
m.add(100) # .add() 添加单个元素
print(m)   # >>> {'a', 100, 'b'}  集合中元素无序

m = {'a', 'b'}
m.update([100, True])  # .update() 批量添加元素
print(m)  # >>> {'a', 100, 'b', True}

# 删除
m = {'a', 'b'}
m.remove('a')  # .remove() 删除指定元素
print(m)  # >>> {'b'}

m = {'a', 'b'}
m.discard('a')  # .discard() 删除指定元素
print(m)  # >>> {'b'}

m = {'a', 'b'}
m.clear()  # .clear() 清空集合
print(m)   # >>> {}

# 集合大小
m = {'a', 'b'}
print(len(m))  # >>> 2

# 成员
m = {'a', 'b'}
print('a' in m)  # >>> True

# 求交集和并集
m = {'a', 'b', 'c'}
n = {'a', 'b', 'd'}
print(m & n)  # 求交集 
print(m | n)  # 求并集



""" 3. 技巧 """

# 快速去除重复项
m = [1,2,3,1]
m = set(m)
print(list(m))  # >>> [1, 2, 3]

# 判断元素是否在一组数据中，如果数据次序不重要，使用集合可以获得比列表更好的性能