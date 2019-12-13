import time

""" 1. 概述
    递归的本质：一个函数在执行过程中一次或多次调用其本身 
"""

""" 例 1：阶乘 """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

""" 例 2: 二分查找（在有序序列中查找目标） """
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)      
print(binary_search([1,2,3,4,5,6,7,8,9,10], 6, 1, 10))

""" 例 3：斐波那契数列 """

""" (1) 低效方法 -- 调用运算 """
def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        out = bad_fibonacci(n-2) + bad_fibonacci(n-1)
        return out # 调用了 bad_fibonacci(n-2) 和 bad_fibonacci(n-1) 的运算, 运算量随 n 呈指数型增加, O(c^n)

""" (2) 高效方法 -- 调用结果 """
def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1) # 只调用 good_fibonacci(n-1) 的结果, 运算量随 n 呈线性增加, O(n)
        return (a + b, a)

%time print(bad_fibonacci(30))
%time print(good_fibonacci(30)[0])

