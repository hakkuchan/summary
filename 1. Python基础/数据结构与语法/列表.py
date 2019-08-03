""" 列表中可以是任何结构的数据，eg: a = [[1,2,3], 1, 'a'] """

""" 索引 """
squares = [1, 4, 9, 16, 25]
squares[0] = 1

""" 切片 """ 
squares[2:] = [9, 16, 25]
squares[-3 : ] = [9, 16, 25]

""" 步长 """
lst = [1,2,3,4,5,6,7,8,9,0]
print(lst[0:5:2])  # List[i:j:n]代表：索引 i - 索引 j，以n为步长
print(lst[::2])    # 按照2为步长，从第一个值开始截取lst数据
print(lst[1::2])   # 按照2为步长，从第二个值开始截取lst数据

""" 序列的内置全局函数 (也适用于 str 和 tuple) """
lst = [1,2,3,4,5,6,7,8,9,0]
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
lst = [1,1,2,3,3,4,4,4,4,5,6]
print(lst.count(4))  # .count(obj)方法：计算值的出现次数
print(lst.index(3))  # .index(obj)方法：从列表中找出某个值第一个匹配项的索引位置

""" range 生成器 """
print(range(5))       # 代表指向了0,1,2,3,4这几个值
print(range(2,5))     # 代表指向了2,3,4这几个值，注意这里不是使用:
print(range(0,10,2))  # 代表指向了0,2,4,6,8这几个值，最后的2代表步长

""" 列表操作：拼、添、插、数、序、删（4种）"""

""" 拼接-1 """
# 列表可以加和拼接
squares = [1, 4, 9, 16, 25] 
cubes = [1, 8, 27, 64, 125]
print(squares + cubes)
""" 拼接-2 """
lst3 = [1,2,3]
lst3 = lst3 * 3
print(lst3)

""" 末尾添加新对象 """
lst.append(2)

""" 特定位置插入一个元素 """
lst.insert(索引, 元素) eg: lst.insert(0, x) 在列表lst头部插入x

""" 统计某个元素在列表中出现的次数 """
lst.count(obj)

""" 对原列表进行排序 """
lst.sort(key=None, reverse=False)

""" 删除列表中第一个值为x的元素 """
lst.remove(x)

""" 特定位置删除一个元素 """
del lst[i] >> 删除位置i的元素
del lst[:] >> 删除lst中所有元素

""" 删除列表中的所有元素 """
lst.clear()

""" 删除列表中给定位置的元素并返回它，如果没有给定位置，list.pop() 将会删除并返回列表中的最后一个元素 """
lst = [1,2,3,4,5,6,7,8,9]
lst.pop() >>> 9 （此时，lst = [1,2,3,4,5,6,7,8]
lst.pop(2) >>> 3 (此时，lst = [1,2,4,5,6,7,8])