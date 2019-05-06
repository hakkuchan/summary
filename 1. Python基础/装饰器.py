""" 
装饰器本质上是一个函数，

在不改变其它函数、类的代码的情况下增加其功能

引例：
"""

# 装饰器会输出其它函数的输入值
def decorator(func):
    def new_func(a, b):
        print("input:", a, b)
        return func(a, b)
    return new_func


@decorator # 以下的函数会传入decorator
def square_sum(a, b):
    return a**2 + b**2

@decorator
def square_dif(a, b):
    return a**2 - b**2

@decorator
def square_mul(a, b):
    return a**2 * b**2

@decorator
def square_div(a, b):
    return a**2 / b**2


print(square_sum(4, 3))
print(square_dif(4, 3))
print(square_mul(4, 3))
print(square_div(4, 3))

""" 
装饰器的本质：

把函数作为自变量传入另一个函数，

以 square_sum 为例
"""

def decorator(func):
    def new_func(a, b):
        print("input:", a, b)
        return func(a, b)
    return new_func

def square_sum(a, b):
    return a**2 + b**2

a = decorator(square_sum)
print(a(4, 3))

