""" 1. 装饰器概述
    
    · 本质上是以已有函数或类为输入的函数，
    
    · 目的是在不改变原函数或类代码的情况下，为它们增加新功能
"""


""" 2. 定义装饰器 """
def show_inputs(fn):  # 定义一个名为 show_input 的装饰器，该装饰器的作用是显示传入函数（fn）的输入值
    def new_operation(a,b,c):   # 定义新功能
        print("input:", a,b,c)  # 新功能：输出传入函数的输入值
        return fn(a,b,c)   # 执行原函数的操作
    return new_operation


""" 3. 应用 """
@show_inputs
def square_sum(a, b, c):
    return a**2 + b**2 + c**2
print(square_sum(3,4,5))  # >>> input: 3 4 5  50

# 本质:
def square_sum(a, b, c):
    return a**2 + b**2 + c**2
new_func = show_inputs(square_sum)
print(new_func(3,4,5))    # >>> input: 3 4 5  50