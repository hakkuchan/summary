""" map用法：map(函数，输入列表)
会把输入列表的所有元素依次代入函数进行运算
"""

nums = [1,2,3,4,5,6]  # 输入列表

def func(x):    # 函数
    return x ** 2

print(list(map(func, nums))) # 标准用法

print(list(map(lambda x: x**2, nums)))  # 函数也可用lambda表达式定义

print(list(x**2 for x in nums))  # 也可用推导式实现 map 的功能，比 map 可读性更好


""" filter:过滤列表中的元素，并且返回一个由所有符合要求的元素构成的列表 """
nums = range(-5, 5)
print(list(filter(lambda x: x < 0, nums)))
print([x for x in nums if x < 0])  # 也可用推导式实现 filter 的功能


""" reduce 用法：reduce(func(x,y), nums)
func(x,y) 先以 nums 中的第 1、2 个元素为输入，
得到的结果再与第 3 个数据作为 func(x, y) 的输入，
以此类推
"""

from functools import reduce
out = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(out)
