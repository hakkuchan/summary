""" 直接构建 """
grade = {'Jack': 98, 'Mike': 99}

""" 关键字参数来指定键值对 """ 
dict(Jack=98, Mike=99)

""" dict构造函数 """
dict([('Jack', 98), ('Mike': 99)])

""" dict推导式 """
{x: x**2 for x in (2, 4, 6)} >>> {2: 4, 4: 16, 6: 36}