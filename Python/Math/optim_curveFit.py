""" curve_fit方法：多项式拟合，本质上也为优化问题 """

import numpy as np
from scipy import optimize

# Toy data
x = np.arange(1,11)
y = 3*x**2 + 5*x + 10 + np.random.uniform(-0.1, 0.1, 10)
# 定义待拟合函数
def fn(x, a, b, c):
    return a*x**2 + b*x + c
# 拟合
out = optimize.curve_fit(fn, x, y)
print(out[0])