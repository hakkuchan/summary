""" 默认参数 """
def f(x, n=2): # n的默认值为2，如果不另行指定则以默认值计算
    return(x ** n)
print(f(10))   
print(f(10,3))


""" * 的作用 """
''' (1) 使用函数时，如果函数有多个参数，可用 fun(*[参数列表]) 的形式传入参数 '''
def func(a, b):
    return a + b
param = [2,3]
out = func(*param)
print(out)

''' (2) 定义函数时，如果函数的参数不确定，可 def fun(*x)，使用函数时传入的所有参数都会保存在 x（tuple形式）中 '''
def func(*x):
    y = sum(x)
    return y
out = func(1,2,3,4,5,6) 
print(out)


""" ** 的作用 """
# 定义函数时，使用 **参数 可以把字典作为参数传递给一个函数。
def student_grade(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s grade is {value}")
student_grade(**{'Jack':98, 'Mike':99, 'Lily':97})


""" 局部变量：定义在函数‘内’的变量，只能在函数内访问。全局变量: 定义在函数‘外’的变量，可在整个程序内访问。"""
x = 5 
def test():
    x = 1
    print(f'In test func: x = {x}')
test()
print(f'Global x = {x}')

''' global语句 → 把局部变量变为全局变量 '''
x = 5
def test(val):
    global x
    x = val
    print(f'In test func: x = {x}')
test(1)
print(f'Global x = {x}')


""" 匿名函数：lambda表达式 """
''' x 为入口参数，x ** 2 + 2 * x 为函数体 '''
f = lambda x: x ** 2 + 2 * x
print(f(2))   
# 等价于：
def g(x):
    return x ** 2 + 2 * x
print(g(2))

''' lambda表达式也可以定义多个变量 '''
f = lambda x, y: x + y
print(f(2,3))


""" 传递函数 """
# 传递函数的关键在于函数名后的括号，没有括号，函数就不会被执行，而可以被传递
def fn(a,b):
    return a+b
fn1 = fn
fn2 = fn
fn3 = fn
print(fn1(1,2), fn2(3,4), fn(5,6))


""" 说明文档 """
# 若函数复杂，其第一部分应该是说明文档，内容和格式如下：
# 第1行：3个双引号开头，简要概述函数目的；
# 第2行：空白，以视觉上区分概述和具体描述；
# 第3行起：描述函数的调用约定、示例、副作用等；
# 最后一行：3个双引号结尾


""" 函数标注 """
# 函数标注 以字典的形式存放在函数的 __annotations__ 属性
# 函数标注不会影响函数的任何其他部分
# 形参标注的定义方式是在形参名称后加上冒号，后跟标注
# 返回值标注的定义方式是加上一个组合符号 ->，后跟标注，该标注位于形参列表和表示 def 语句结束的冒号之间。

def f(sys: int, unit: str = 'bits') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", sys, unit)
    print('system is ' + str(sys) +' ' + unit)
f(64)

# 解析：函数f中，sys是一个位置参数，
# unit是一个关键字参数，关键字参数一般以param=a 的形式给出,
# 可以看出当标注关键字参数时，标注在关键字参数后面，但在赋值语句前面。