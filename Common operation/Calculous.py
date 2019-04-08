import numpy as np
from scipy import integrate, misc

# 定义函数
def f(x, a, b, c):
    return a * x ** 2 + b * x + c

# 计算一重定积分
integ = integrate.quad(f, -1, 1, args=(1,2,3))[0]
print(integ)

# 计算一阶导数
x = np.array([i for i in range(10)])
deriv = misc.derivative(f, x, args=(1,2,3), dx=1e-6)
print(deriv)