""" leastsq方法：最小二乘优化法，即目标函数是误差平方和的优化方法 """

import numpy as np
from scipy import optimize

# Toy data
x = np.arange(1,11)
y = 3*x**2 + 5*x + 10 + np.random.uniform(-0.1, 0.1, 10)
# 定义误差函数
def error(param):
    a,b,c = param
    return y -(a*x**2 + b*x + c)
# 拟合
out = optimize.leastsq(error, [0,0,0])  # [0,0,0] 为初始值
print(out[0])