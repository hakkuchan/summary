""" 1. map filter reduce 用法概述:
    (1) 结果列表 = list(map(函数名, 自变量列表))
    (2) 结果列表 = list(filter(条件式, 自变量列表))
    (3) 结果 = reduce(函数名, 自变量列表)
"""


""" 2. map：把输入列表的所有元素依次代入函数进行运算 """
''' 标准用法 '''
nums = [1,2,3,4,5,6]
def fn(x):
    return x ** 2
print(list(map(fn, nums)))
# 等价于推导式（推荐）：
print(list(x**2 for x in nums))

''' 函数也可用lambda表达式定义 '''
print(list(map(lambda x: x**2, nums)))


""" 3. filter: 过滤列表中的元素，并且返回一个由所有符合要求的元素构成的列表 """
nums = range(-5, 5)
print(list(filter((lambda x: x < 0), nums)))
# 等价推导式（推荐）：
print([x for x in nums if x < 0])


""" 4. reduce：先以 nums 中的第 1、2 个元素为 fn 输入, 得到的结果再与第 3 个数据作为 fn 的输入，以此类推 """
from functools import reduce
nums = range(-5, 5)
fibo = reduce((lambda x,y: x + y), range(100))
print(fibo)