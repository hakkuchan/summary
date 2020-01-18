import numpy as np
import sympy as sy
from scipy import misc


""" 1. sympy 计算导函数 """
x, y = sy.symbols('x, y')

f = x ** 2 * sy.sin(x)
print(sy.diff(f, x, 1))  # 一阶导函数，参数（方程，自变量，阶数）
print(sy.diff(f, x, 2))  # 二阶导函数

f = x + y + x*y + sy.sin(x*y)
print(sy.diff(f, x, 1, y, 2)) # 偏导数，对 x 求 一阶导，对 y 求二阶导


""" 2. 计算导数值 """

""" 方法 1：利用 sympy 求出导函数，然后计算导数值 """

""" 方法 2：利用 scipy，过程如下："""
# step 1：定义函数
def f(x, a, b, c):
    return a * x ** 2 + b * x + c
# step 2：计算一阶导数值
x = np.linspace(0, 10, 11)
drv = misc.derivative(f, x, args=(1,2,3), dx=1e-6)
print(drv)