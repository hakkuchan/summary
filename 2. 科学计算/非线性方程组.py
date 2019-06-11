import math
import numpy as np
from scipy.optimize import fsolve

""" 例 1 """
def fn(x):
    x1, x2 = x.tolist()
    return [
            x1 ** 2 + 3 * x2 - 7,
            2 * x1 + 4 * x2 ** 2 - 8
           ]

x = fsolve(fn,[0,0]) # [0,0] 是估计的初值
print(x)


""" 例 2 """
def fn(x):
    x1, x2, x3 = x.tolist()
    return [
            5 * x2 + 3, 
            4 * x1 ** 2 - 2 * math.sin(x2*x3), 
            x2 * x3 -1.5
           ]

x = fsolve(fn,[1,1,1])
print(x)


""" 例 2 扩展 """
def fn(x):
    x1, x2, x3 = x.tolist()
    return [
            5 * x2 + 3, 
            4 * x1 ** 2 - 2 * math.sin(x2*x3), 
            x2 * x3 -1.5
           ]

# 假如对 fn 的求解过慢（通常涉及多个未知数），为加快运算，可以求出 fn 的雅各比矩阵，如下：

def jcb(x):
    x1, x2, x3 = x.tolist()
    return [
            [0, 5, 0],
            [8*x1, -2*x3*math.cos(x2*x3), -2*x2*math.cos(x2*x3)],
            [0, x3, x2]
           ]

# 分别传入原始函数 fn 和 雅各比函数 jcb
x = fsolve(fn, [1,1,1], fprime=jcb)
print(x)