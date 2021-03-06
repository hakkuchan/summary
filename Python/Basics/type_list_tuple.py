""" · 列表 & 元组
      列表 和 元组 都是有序数据的容器，可以包含任何类型的数据，例如：[[1,2,3], True, 'a', (100, 50)]
      二者区别在于：列表是可变类型，元组是不可变类型
    
    · 目录
    |
    |—— 1. 创建：直接创建、生成器创建
    |
    |—— 2. 通用操作：索引和切片、拼接、内置函数
    |
    |—— 3. 列表操作：添加(append, insert, extend)、删除(remove, del, pop, clear)、排序
"""


""" 1. 创建 """
''' 1.1 直接创建 '''
m = [1, 2, 3] # 列表
n = (1, 2, 3) # 元组

''' 1.2 生成器创建 '''
print(list(range(3)))  # >>> [0, 1, 2]
print(list(range(1, 3)))  # >>> [1, 2]
print(tuple(range(0, 6, 2)))  # >>> (0, 2, 4)  range(start: end: step)


""" 2. 通用操作 """
''' 2.1 索引和切片 '''
m = [1, 2, 3, 4]
print(m[0])  # >>> 1
print(m[-1]) # >>> 4
print(m[0:2]) # >>> [1, 2]
print(m[:2])  # >>> [1, 2]
print(m[0: 5: 2]) # m(start: end: step)  >>> [1, 3]

''' 2.2 拼接 '''
m = [1, 2] 
n = [3, 4]
print(m + n)  # 1, 2, 3, 4]
print(2 * m + n)      # >>> [1, 2, 1, 2, 3, 4]
print(2 * [m] + [n])  # >>> [[1, 2], [1, 2], [3, 4]]

''' 2.3 内置函数 '''
m = [1, 2, 3, 4]
print(len(m))  # >>> 4
print(max(m))  # >>> 4
print(min(m))  # >>> 1
print(sum(m))  # >>> 10
print(m.count(4))  # >>> 1  计算 4 的出现次数
print(m.index(3))  # >>> 2  从列表中找出 3 的第一个匹配项的索引


""" 3. 列表操作 """
''' 3.1 添加 '''
# .append() 末尾添加元素
m = [1, 2, 3]
m.append(4)
print(m) # >>> [1, 2, 3, 4]
# .insert() 索引 2 处添加 True
n = [1, 2, 3]
n.insert(2, True)  
print(n) # >>> [1, 2, True, 3]
# .extend() 末尾添加序列
m, n = [1, 2, 3], [4, 5, 6]
m.extend(n)
print(m) # >>> [1, 2, 3, 4, 5, 6]

''' 3.2 删除 '''
# .remove() 删除列表中第一个值为x的元素
m = [1, 2, 3, 4]
m.remove(3)
print(m)  # >>> [1, 2, 4]
# del 删除索引 1 的元素
m = [1, 2, 3]  
del m[1]  
print(m)  # >>> [1, 3]
# .pop() 删除并返回列表中的最后一个元素
m = [1, 2, 3]
i = m.pop()  
print(m, i)  # >>> [1, 2] 3
# .pop(1) 删除并返回列表中索引为 1 的元素
m = [1, 2, 3]
j = m.pop(1)
print(m, j)  # >>> [1, 3] 2
# .clear() 删除列表中的所有元素
m = [1, 2, 3]
m.clear()
print(m)  # >>> []  

''' 3.3 排序 '''
# .sort(reverse=False) 按照元素值排列（正序）
m = [3, 1, 2, 0]
m.sort(reverse=False)  
print(m)  # >>> [0, 1, 2, 3]
# .sort(reverse=True) 按照元素值排列（倒序）
m = [3, 1, 2, 0]
m.sort(reverse=True)
print(m)  # >>> [3, 2, 1, 0]
# .reverse() 按照元素索引倒序排列
m = [3, 1, 2, 0]
m.reverse()  
print(m)  # >>> [0, 2, 1, 3]
# 按索引倒序排列
m = [0, 2, 1, 3]
n = m[::-1]  
print(n)
