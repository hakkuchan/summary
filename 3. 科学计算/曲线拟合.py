import numpy as np
from scipy import optimize

a, b, c = 1, 3, 2
x = np.linspace(-1,1,num=100)
y = np.array([a * x ** 2 + b * x + c + np.random.uniform(-0.1, 0.1, len(x))]).ravel()

def fn(x, p0, p1, p2):
    return p0 * x ** 2 + p1 * x + p2

p, p_covariance = optimize.curve_fit(fn, x, y)

print(p)

# 显然，用最优化问题的方法求解曲线拟合也是可以的，但不推荐。