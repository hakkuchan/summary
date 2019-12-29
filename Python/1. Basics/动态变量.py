""" 1. 概述

    · 通过内置的 globals()函数 和 locals()函数 可动态生成变量名并赋值
    
    · 但所生成变量的作用域和手动定义的变量有很多不同，要慎重地使用！
"""



""" 2. globals()函数 """

# 例 1：
for i in range(0,3):
    globals()['x'+str(i)] = 2 * i  # globals()函数实现动态变量名
print(x0 + x1 + x2) # >>> 6
print(id(x0) == id(x1) == id(x2))  # >>> False


# 例 2：
x0, x1, x2 = 10, 100, 1000
def f():
    for i in range(0, 3):
        globals()['x'+str(i)] = 2 * i   
    return x0 + x1 + x2
print(f())  # >>> 6
print(x0, x1, x2)  # >>> 0 2 4  说明定义在函数中的 globals()变量 是全局变量



""" 3. locals()函数 """

# 例 1：
for i in range(0,3):
    locals()['x'+str(i)] = 2 * i  # locals()函数实现动态变量名
print(x0 + x1 + x2) # >>> 6
print(id(x0) == id(x1) == id(x2))  # >>> False
# 此时，效果和 globals() 一样


# 例 2：
x0, x1, x2 = 10, 100, 1000
def f():
    for i in range(0, 3):
        locals()['x'+str(i)] = 2 * i
    return x0 + x1 + x2
print(f())  # >>> 1110  说明当存在同名全局变量时，定义在函数中的 locals()变量 也未被访问
print(x0, x1, x2)  # >>> 10 100 1000


# 例 3：
x0, x1, x2 = 10, 100, 1000
def f():
    for i in range(0, 3):
        locals()['x'+str(i)] = 2 * i
    global x0, x1, x2
    return x0 + x1 + x2
print(f())  # >>> 1110  说明 global locals()变量 没有转换为全局变量
print(x0, x1, x2)  # >>> 10 100 1000