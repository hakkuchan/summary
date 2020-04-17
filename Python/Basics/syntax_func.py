""" · 函数：实现了对代码段的封装，以便重复使用
    
    · 目录
    |
    |—— 1. 一般形式
    |
    |—— 2. 变量的作用域
    |
    |—— 3. * 的作用
    |
    |—— 4. ** 的作用
    |
    |—— 5. 传递函数
    |
    |—— 6. 匿名函数
    |
    |—— 7. map、filter、reduce函数
    |
    |—— 8-11. unfunc函数、apply函数、说明文档、函数标注
"""


""" 1. 一般形式
    
    def <函数名>(参数)：
      <代码段>
      return <函数返回值>
"""
# 例：
def fn(a, b):
    out = a ** b
    return out



""" 2. 变量的作用域 """
m, n = 1, 2  # 在函数外定义的变量是全局变量，作用域是整个代码段
def f():
    m, n = 3, 4  # 在函数内定义的变量是局部变量，只在该函数定义范围内有效
    return m, n
print('函数内的 m 和 n：',f())  # >>> (3, 4)
print('函数外的 m 和 n：', (m, n))  # >>> (1, 2)

# global关键字：局部变量 → 全局变量
m, n = 1, 2 
def f():
    global m, n  # global把函数内的局部变量变成全局变量
    m, n = 3, 4
    return m, n
print('函数内的 m 和 n：',f())      # >>> (3, 4)
print('函数外的 m 和 n：', (m, n))  # >>> (3, 4)



""" 3. * 的作用 """
''' (1) 使用函数时，如果函数有多个参数，可用 fun(*[参数列表]) 的形式传入参数 '''
def f(a, b):
    return a + b
param = [2,3]
out = f(*param)
print(out)  # >>> 5

''' (2) 定义函数时，如果函数的参数不确定，可 def fun(*x)，使用函数时传入的所有参数都会保存在 x（tuple形式）中 '''
def f(*x):
    y = sum(x)
    return y
out = f(1, 2, 3, 4) 
print(out)  # >>> 10



""" 4. ** 的作用 """
# 定义函数时，使用 **参数 可以把字典作为参数传递给一个函数。
def student_grade(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s grade is {value}")
student_grade(**{'Jack':98, 'Mike':99, 'Lily':97})



""" 5. 传递函数：调用函数时，函数名后不加括号，函数就不会被执行，而可以被传递 """
# 定义函数
def fn(a,b):
    return a + b
# 传递函数
fn1 = fn
fn2 = fn
fn3 = fn
print(fn1(1,2), fn2(3,4), fn(5,6))  # >>> 3, 7, 11



""" 6. 匿名函数：lambda表达式 """
# 下式，“lambda x” 表示设定 x 为自变量；“:” 之后为函数体，即 “ 2 * x ” 
f = lambda x: 2 * x
print(f(2))   
# 等价于：
def g(x):
    return 2 * x
print(g(2))

# lambda表达式也可以定义多个变量
f = lambda x, y: x + y
print(f(2,3))



""" 7. map、filter、reduce 函数
    · 结果列表 = list(map(函数名, 自变量列表))
    · 结果列表 = list(filter(条件式, 自变量列表))
    · 结果 = reduce(函数名, 自变量列表)
"""

''' (1) map() 把输入列表的所有元素依次代入函数进行运算 '''
# 标准用法：
nums = [1,2,3,4,5,6]
def fn(x):
    return x ** 2
print(list(map(fn, nums)))  # nums中的元素被依次带入fn并返回结果
# 也可用lambda表达式定义函数：
print(list(map(lambda x: x**2, nums)))
# 等价于推导式（推荐）：
print(list(x**2 for x in nums))


''' (2) filter() 过滤列表中的元素，并且返回一个由所有符合要求的元素构成的列表 '''
nums = range(-5, 5)
print(list(filter((lambda x: x < 0), nums)))
# 等价于推导式（推荐）：
print([x for x in nums if x < 0])


''' (3) reduce() 先以 nums 中的第 1、2 个元素为 fn 输入, 得到的结果再与第 3 个数据作为 fn 的输入，以此类推 '''
from functools import reduce
nums = range(-5, 5)
fibo = reduce((lambda x,y: x + y), range(100))
print(fibo)



""" 8. ufunc函数：针对ndarray数据类型，可将普通函数转换为"ufunc函数"，详见numpy部分

    9. apply函数：针对DataFrame中的数据，可将普通函数转换为"apply函数"，详见pandas部分 
      
    10. 说明文档
    · 若函数复杂，其第一部分应该是说明文档，内容和格式如下：
      第1行：3个引号开头，简要概述函数目的；
      第2行：空行，以视觉上区分概述和具体描述；
      第3行起：描述函数的调用约定、示例、副作用等； 
      最后一行：3个引号结尾

    11. 函数标注
    · 函数标注以字典的形式存放在函数的 __annotations__ 属性，函数标注不会影响函数的任何其他部分
      位置参数标注：参数名称后加上冒号，后跟标注
      关键字参数标注：参数名称后加上冒号，后跟标注，再接等号，给关键字参数赋值
      返回值标注：加上一个组合符号 ->，后跟标注，该标注位于形参列表和表示 def 语句结束的冒号之间。
"""
# 例：函数标注
def f(sys: int, unit: str = 'bits') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", sys, unit)
    print('system is ' + str(sys) +' ' + unit)
f(64)
# 解析：函数 f 中，sys是一个位置参数；unit是关键字参数；函数名后'-> str'为返回值标注
