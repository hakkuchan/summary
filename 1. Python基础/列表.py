""" 列表中可以是任何结构的数据，eg: a = [[1,2,3], 1, 'a'] """

""" 索引 """
squares = [1, 4, 9, 16, 25]
squares[0] = 1

""" 切片 """ 
squares[2:] = [9, 16, 25]
squares[-3:] = [9, 16, 25]

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
print(list(range(5)))       # 代表指向了0,1,2,3,4这几个值
print(list(range(2,5)))     # 代表指向了2,3,4这几个值，注意这里不是使用:
print(range(0,10,2))        # 代表指向了0,2,4,6,8这几个值，最后的2代表步长

""" 拼接 """
squares = [1, 4, 9, 16, 25] 
cubes = [1, 8, 27, 64, 125]
print(squares + cubes)

""" 重复 """
lst3 = [1,2,3]
lst3 = lst3 * 3
print(lst3)

""" 添加 """
lst.append(2)        # .append() 末尾添加对象
lst.insert(2, 9)   # .insert() 索引 2 处添加 9

""" 排序 """
lst.sort(key=None, reverse=False)

""" 删除 """
lst.remove(3)  # .remove() 删除列表中第一个值为x的元素
del lst[2]     # del 删除索引 2 的元素
lst.pop()      # .pop() 删除并返回列表中的最后一个元素
lst.pop(2)     # .pop() 删除并返回列表中索引为 2 的元素
lst.clear()    # .clear()  删除列表中的所有元素