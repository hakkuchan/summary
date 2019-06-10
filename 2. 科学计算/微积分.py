import numpy as np
import sympy as smp
from scipy import misc, integrate

""" 
 内容
  |
  |—— 1. sympy 计算导函数
  |
  |—— 2. sympy 计算积分函数
  |
  |—— 3. 计算导数值
  |
  |—— 4. 计算积分值
  |
"""

""" 1. sympy 计算导函数 """
x, y = smp.symbols('x, y')

f = x ** 2 * smp.sin(x)
smp.diff(f, x, 1)  # 一阶导函数，参数（方程，自变量，阶数）
smp.diff(f, x, 2)  # 二阶导函数

f = x + y + x*y + smp.sin(x*y)
smp.diff(f, x, 1, y, 2) # 偏导数，对 x 求 一阶导，对 y 求二阶导


""" 2. sympy 计算积分函数 """
x, y, a, b, c, d = smp.symbols('x, y, a, b, c, d')

f = x ** 2 + smp.sin(x)
smp.integrate(f, x) # 不定积分
smp.integrate(f, (x,a,b)) # 定积分，从 a 积到 b

f = x * y + smp.sin(x) + smp.cos(y)
smp.integrate(f, x, y) # 双重不定积分
smp.integrate(f, (x,a,b), (y,c,d)) # 双重定积分, x 从 a 积到 b, y 从 c 积到 d


""" 3. 计算导数值 """

""" 方法 1：利用 symbol 求出导函数，然后计算导数值 """

""" 方法 2：利用 scipy，过程如下："""
# step 1：定义函数
def f(x, a, b, c):
    return a * x ** 2 + b * x + c
# step 2：计算一阶导数值
x = np.linspace(0, 10, 11)
drv = scp.misc.derivative(f, x, args=(1,2,3), dx=1e-6)
print(drv)


""" 4. 计算积分值 """

""" 情况一：已知函数形式 """

""" 方法 1：sympy 求出积分函数，再计算积分值 """
  
""" 方法 2：利用 scipy，过程如下："""
# step 1：定义函数
def f(x, a, b, c):
    return a * x ** 2 + b * x + c
# step 2：计算积分值
itg = integrate.quad(f, -1, 1, args=(1,2,3))[0]  # 函数名 f；积分区间 [-1, 1]；f(x)中 a=1,b=2,c=3
print(itg)


""" 情况二：数值积分 """
x = np.linspace(-1,1,1000)
y = x ** 2 + 2 * x + 3
itg = scp.integrate.simps(y,x) # 辛普森积分方法，注意 y 在前，x 在后
print(itg) 