""" 1. 递归(Recursion)概述

    · 递归是一种解决问题的方法
    
    · 其精髓在于：
      把问题分解为更小规模的相同问题，并调用自身，
      通过重复解决“最小规模”问题，解决总问题。
      
    · 递归算法的要素：
      (1) 必须有一个基本结束条件（最小规模问题的直接解决）
      (2) 必须能改变状态向基本结束条件演进（减小问题规模）
      (3) 递归算法必须调用自身（解决减小了规模的相同问题）
"""

# 例 1：十进制整数转换为(2-16)任意进制
def to_str(num, base):
    convert_str = '0123456789ABCDEF'
    if num < base:  # 基本结束条件
        return convert_str[num]
    else:
        # 通过整除操作不断向基本结束条件演进，并调用自身
        out = to_str(num // base, base) + convert_str[num % base]
        return out
print(to_str(20190901, 16))


# 例 2：阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


# 例 3：斐波那契数列
import time

# (1) 低效方法
def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        # 调用了 bad_fibonacci(n-2) 和 bad_fibonacci(n-1) 的运算, 运算量随 n 呈指数型增加, O(c^n)
        out = bad_fibonacci(n-2) + bad_fibonacci(n-1)
        return out

# (2) 高效方法 -- 调用结果 """
def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        # 只调用 good_fibonacci(n-1) 的结果, 运算量随 n 呈线性增加, O(n)
        (a, b) = good_fibonacci(n-1)
        return (a + b, a)

%time print(bad_fibonacci(32))
%time print(good_fibonacci(32)[0])



""" 2. 递归调用的底层
    
    · 当一个函数被调用的时候，系统会把调用时的现场数据（栈帧）压入到系统调用栈
     （栈帧：函数名、参数、局部变量、函数的返回地址）
      当函数返回时，要从调用栈的栈顶取得返回地址，恢复现场，弹出栈帧，按地址返回
    
    · 递归是不断调用自身的函数，每调用一次自身，会把当时情况下的栈帧压入系统调用栈（先进后出），
      当达到基本结束条件后，再从栈顶不断依次调出栈帧，恢复现场并返回计算结果。
    
    · 系统调用栈具有最大深度，如果函数调用次数过多，就会溢出
      查看、修改系统调用栈最大深度的方法如下：
"""

import sys
sys.getrecursionlimit()  # 获取系统设定的最大递归次数  >>> 3000
sys.setrecursionlimit(5000)  # 把递归次数设定为 5000 次（当重启服务后，最大递归次数回到默认值）
sys.getrecursionlimit()  # >>> 5000 