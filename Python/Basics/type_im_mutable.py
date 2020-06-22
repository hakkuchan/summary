''' 可变类型包括：列表、字典、集合 '''
m = [1,2,3]
id1 = id(m)
m.append(4) # 可变类型数据可随时修改，且内存位置不变
id2 = id(m) 
print(id1 == id2) # >>> True 内存位置不变


''' 不可变类型包括：数值、字符串、逻辑值、元组 '''
m = 'abc'
id1 = id(m)
m += 'd'    # 对不可变类型的数据进行修改，修改值会存放在新内存位置
id2 = id(m)
print(id1 == id2) # >>> False 内存位置改变


''' 可变类型会花费一些计算或存储代价去维持可变性，
    如果数据对象不需要改变，建议使用不可变类型 
'''