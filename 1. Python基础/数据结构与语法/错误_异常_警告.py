""" 1. 错误
    语法错误(SyntaxError: invalid syntax)，又称为解析错误。
    代码无法执行。
"""


""" 2. 异常
    语法正确，但执行时引发了错误，包括：
    ZeroDivisionError：除以0导致错误
    NameError：name 'xxx' is not defined 未声明对象
    TypeError：对类型无效的操作
    OverflowError：数值运算超出最大限制
    AttributeError：对象没有这个属性
    KeyError：映射（字典）中没有这个键
    DeprecationWarning：关于被弃用的特征的警告，更新一下anaconda所有的库即可 conda update --all
"""


""" 3. 处理异常 """

""" try:... except:...语句
    首先，执行 try 子句，如果没有异常发生，则跳过 except 子句，并完成 try 语句的执行。
    如果在执行try子句时发生了异常，则跳过该子句中剩下的部分；
    然后，如果异常的类型和 except 关键字后面的异常匹配，则执行 except 子句。
    如果发生的异常和 except 子句中指定的异常不匹配，则将其传递到外部的 try 语句中；
    如果没有找到处理程序，则它是一个未处理异常，程序中止
    一个 try 语句可能有多个 except 子句，以指定不同异常的处理程序
    如果发生多种异常，处理方法都一样，可以用一个 except 子句对应多个异常命名（用元组表示）
    例如：except (RuntimeError, TypeError, NameError):
"""

""" try:... except:... else:...语句："""
def fn(a, b):
    return a / b

try:
    fn(1, 0)
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Result is", fn(0, 1))


""" 4. 屏蔽警告信息 """

""" 有时导入库时会显示警告信息，比如废用特性或使用问题,可屏蔽 """

import warnings
warnings.filterwarnings('ignore') # 不发出警告

""" 关于警告的更多信息，可参考 cookbook 中 14.11 输出警告信息 """