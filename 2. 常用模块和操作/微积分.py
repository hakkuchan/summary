import numpy as np
from scipy import integrate, misc

""" 一重定积分和一阶微分 """

""" 函数微积分 """

# 定义函数
def f(x, a, b, c):
    return a * x ** 2 + b * x + c

# 计算一重定积分
itg = integrate.quad(f, -1, 1, args=(1,2,3))[0]
print(itg)

# 计算一阶微分
x = np.linspace(0, 10, 11)
drv = misc.derivative(f, x, args=(1,2,3), dx=1e-6)
print(drv)

""" 数值积分 """
x = np.linspace(-1,1,1000)
y = x ** 2 + 2 * x + 3
itg = integrate.simps(y,x)
print(itg) # 辛普森积分方法，注意 y 在前，x 在后