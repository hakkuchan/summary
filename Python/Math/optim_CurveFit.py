# 曲线拟合本质上是最优化问题
# 由于scipy库提供了 curve_fit 方法，不必采用求解最优化模型的标准方法

import numpy as np
from scipy import optimize

a, b, c = 1, 3, 2
x = np.linspace(-1,1,num=100)
y = np.array([a * x ** 2 + b * x + c + np.random.uniform(-0.1, 0.1, len(x))]).ravel()

def fn(x, p0, p1, p2):
    return p0 * x ** 2 + p1 * x + p2

p, p_covariance = optimize.curve_fit(fn, x, y)

print(p)