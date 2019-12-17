import numpy as np
import sympy as sy
from scipy import integrate


""" 1. sympy 计算积分函数 """
x, y, a, b, c, d = sy.symbols('x, y, a, b, c, d')

f = x ** 2 + sy.sin(x)
print(sy.integrate(f, x))       # 不定积分
print(sy.integrate(f, (x,a,b))) # 定积分，从 a 积到 b

f = x * y + sy.sin(x) + sy.cos(y)
print(sy.integrate(f, x, y))    # 双重不定积分
print(sy.integrate(f, (x,a,b), (y,c,d))) # 双重定积分, x 从 a 积到 b, y 从 c 积到 d


""" 2. 计算积分值 """

""" 情况一：已知函数形式 """

''' 方法 1：sympy 求出积分函数，再计算积分值 '''
  
''' 方法 2：利用 scipy，过程如下：'''
# step 1：定义函数
def f(x, a, b, c):
    return a * x ** 2 + b * x + c
# step 2：计算积分值
itg = integrate.quad(f, -1, 1, args=(1,2,3))[0]  # 函数名 f；积分区间 [-1, 1]；f(x)中 a=1,b=2,c=3
print(itg)

''' 情况二：未知函数形式，数值积分 '''
x = np.linspace(-1,1,1000)
y = x ** 2 + 2 * x + 3
itg = integrate.simps(y,x) # 辛普森积分方法，注意 y 在前，x 在后
print(itg)