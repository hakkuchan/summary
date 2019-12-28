""" 1. 列表 & 元组
    
    · 列表 和 元组 都是有序数据的容器，
	  可以包含任何类型的数据，例如：[[1,2,3], True, 'a', (100, 50)]
	
    · 二者区别在于：列表是可变类型，元组是不可变类型
	  
    · 可变类型：可以随时改变数据对象。可变类型有：列表、字典、集合
      不可变类型：一旦创建就无法改变数据对象。不可变类型有：数值、字符串、逻辑值、元组
	
    · 可变类型会花费一些计算或存储代价去维持可变性；
	  如果数据对象不需要改变，使用不可变类型的性能更好
"""



""" 2. 列表和元组的操作 """

''' (1) 创建 '''

# 创建列表
m = [1, 2, 3]
n = list(1, 2, 3)
print(m == n)

# 创建元组
m = (1, 2, 3)
n = tuple(1, 2, 3)
print(m == n)

# 利用生成器创建列表和元组
print(list(range(3)))  # >>> [0, 1, 2]
print(list(range(1, 3)))  # >>> [1, 2]
print(tuple(range(0, 6, 2)))  # >>> [0, 2, 4]  range(start: end: step)


''' (2) 通用操作 '''

# 索引 & 切片
m = [1, 2, 3, 4]
print(m[0])  # >>> 1
print(m[-1]) # >>> 4
print(m[0:2]) # >>> [1, 2]
print(m[:2])  # >>> [1, 2]
print(m[0: 5: 2]) # m(start: end: step)  >>> [1, 3]

# 拼接
m = [1, 2] 
n = [3, 4]
print(m + n)  # 1, 2, 3, 4]
print(2 * m + n)      # >>> [1, 2, 1, 2, 3, 4]
print(2 * [m] + [n])  # >>> [[1, 2], [1, 2], [3, 4]]

# 其它
m = [1, 2, 3, 4]
print(len(m))  # >>> 4
print(max(m))  # >>> 4
print(min(m))  # >>> 1
print(sum(m))  # >>> 10
print(m.count(4))  # >>> 1  计算 4 的出现次数
print(m.index(3))  # >>> 2  从列表中找出 3 的第一个匹配项的索引


''' (3) 列表操作 '''

# 添加
m = [1, 2, 3]
m.append(4)  # .append() 末尾添加元素
print(m)     # >>> [1, 2, 3, 4]

n = [1, 2, 3]
n.insert(2, True)  # .insert() 索引 2 处添加 True
print(n)        # >>> [1, 2, True, 3]

m, n = [1, 2, 3], [4, 5, 6]
m.extend(n)  # .extend() 末尾添加序列
print(m)     # >>> [1, 2, 3, 4, 5, 6]


# 删除
m = [1, 2, 3, 4]
m.remove(3)  # .remove() 删除列表中第一个值为x的元素
print(m)  # >>> [1, 2, 4]

m = [1, 2, 3]  
del m[1]  # del 删除索引 1 的元素
print(m)  # >>> [1, 3]

m = [1, 2, 3]
i = m.pop()  # .pop() 删除并返回列表中的最后一个元素
print(m, i)  # >>> [1, 2] 3

m = [1, 2, 3]
j = m.pop(1) # .pop(1) 删除并返回列表中索引为 1 的元素
print(m, j)  # >>> [1, 3] 2

m = [1, 2, 3]
m.clear() # .clear() 删除列表中的所有元素
print(m)  # >>> []  


# 排序
m = [3, 1, 2, 0]
m.sort(reverse=False)  # .sort(reverse=False) 按照元素值排列（正序）
print(m)  # >>> [0, 1, 2, 3]

m = [3, 1, 2, 0]
m.sort(reverse=True)  # .sort(reverse=True) 按照元素值排列（倒序）
print(m)  # >>> [3, 2, 1, 0]

m = [3, 1, 2, 0]
m.reverse()  # .reverse() 按照元素索引倒序排列
print(m)  # >>> [0, 2, 1, 3]