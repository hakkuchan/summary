""" 装饰器：本身为函数或类，用于为其它函数或类扩充增加新功能 """


''' 1. 使用函数装饰器扩充函数的功能 '''
# 定义装饰器，类型为函数，该装饰器的作用是输出函数 fn 的输入值
def decorator(fn):
    def show_inputs(a,b,c):   # 定义装饰器的功能
        print("inputs:", a,b,c)  # 功能：输出传入函数的输入值
        return fn(a,b,c)   # 执行原函数的操作
    return show_inputs

# "装饰"函数 fn (fn本身只计算平方和，不给出输入值)
@decorator
def fn(a,b,c):
    print('result:', a**2+b**2+c**2)
fn(1,2,3)  # >>> input: 3 4 5  result: 50

# 装饰器的本质：把一个函数作为另一个函数(装饰器)的输入
def fn(a,b,c):
    print('result:', a**2+b**2+c**2)
new_fn = decorator(fn) # 把 fn 作为 decorator 的输入
new_fn(1,2,3)  # >>> input: 3 4 5  result: 50


''' 2. 使用类装饰器扩充函数的功能 '''
# 定义装饰器，类型为类，该装饰器的作用是输出函数 fn 的输入值
class Decorator(object):
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *args):  # __call__()方法：用于调用 self.fn 的参数
        print('inputs:', *args)
        self.fn(*args)

# "装饰"函数 fn
@Decorator
def fn(a,b,c):
    print('result:', a**2+b**2+c**2)
fn(4,5,6)


''' 3. 使用函数装饰器扩充类的功能 '''
# 定义装饰器，类型为函数，该装饰器的作用是输出类的属性值
def decorator(cls):
    def show_inputs(a, b, c):      # 定义装饰器的功能
        print("inputs:", a, b, c)  # 功能：输出传入函数的输入值
        return cls(a, b, c)        # 执行原类的操作
    return show_inputs

# "装饰"类 AClass
@decorator
class AClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def square_sum(self):
        print('result:', self.a**2 + self.b**2 + self.c**2)

y = AClass(7,8,9)
y.square_sum()
