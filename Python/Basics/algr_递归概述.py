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

# (2) 高效方法
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



""" 3. 分治策略
    
    · 分治：分而治之
      其核心是：将大问题分为若干个小问题，将小问题的解汇总得到大问题的解
      可以看出，分治策略可利用递归算法实现
    
	
    
    4. 贪心策略
    
    · 贪心策略可用于解决某些优化问题（优化问题：找到某些问题的最优解，如最短路径等）
      贪心策略可利用递归算法实现
	  其核心是：每次都试图解决问题的尽量大的一部分
      
    · 实例：假设顾客投入自动售货机 1 美元，买了 9 美分的东西，如何用最少数量的硬币找零 81 美分
      利用贪心策略（从最大面值的硬币开始，用尽量多的数量）：
      (1) 用最大面值的硬币 half dollar (1 half dollar = 50 美分) ，可找零 1 half dollar，余额为 31 美分
      (2) 用下一个最大面值的硬币 quarter (1 quarter = 25 美分) ，可找零 1 quarter，找零余额为 6 美分
      (3) 用下一个最大面值的硬币 dime (1 dime = 10 美分) ，发现 1 dime 大于找零余额，跳过
      (4) 用下一个最大面值的硬币 nickle (1 nickle = 5 美分) ，可找零 1 nickle，找零余额为 1 美分
      (5) 用下一个最大面值的硬币 penny (1 Penny = 1 美分)，可找零 1 penny
      共用硬币 4 个：1 half dollar、1 quarter、1 nickle、1 penny
"""