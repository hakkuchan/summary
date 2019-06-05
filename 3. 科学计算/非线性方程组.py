import numpy as np
from scipy.optimize import fsolve

""" 
求解非线性方程组:
x1 = 2, x2 = 1
x1 ^ 2 + 3 * x2 - 3 = 4
2 * x1 + 4 * x2 ^2 - 10 = -2
"""

def fn(x):
    return np.array([
                     x[0] ** 2 + 3 * x[1] - 7,
                     2 * x[0] + 4 * x[1] ** 2 - 8
                    ])

x = fsolve(fn,[0,0])
print(x)