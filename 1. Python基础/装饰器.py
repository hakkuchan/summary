""" 
装饰器本质上是一个以别的函数或类为输入的函数，
在不改变原函数或类代码的情况下，为它们增加新功能
"""

""" 定义装饰器 """
def show_inputs(fn):    # 定义一个名为 show_input 的装饰器，该装饰器的目的是显示传入函数（fn）的输入值
    def new_operation(a,b,c):   # 定义新功能
        print("input:", a,b,c)  # 新功能：输出传入函数的输入值
        return fn(a,b,c)   # 执行原函数的操作
    return new_operation

""" 应用 """

# 方法1：把现有函数 (square_sum for example) 代入装饰器函数
def square_sum(a, b, c):
    return a**2 + b**2 + c**2

new_func = show_inputs(square_sum)
print(new_func(3,4,5))

# 方法2：魔法函数
@show_inputs
def square_sum(a, b, c):
    return a**2 + b**2 + c**2

print(square_sum(3,4,5))