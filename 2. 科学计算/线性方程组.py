import numpy as np
from scipy import linalg
from scipy.optimize import fsolve

""" 
求解线性方程组:
3 * x1 + 2 * x2 + x3 = 8
2 * x1 + 4 * x2 + 3 * x3 = 13
x1 + x2 + x3 = 4
"""

""" 方法 1：利用 numpy 中的 linalg """
A=np.array([[3,2,1],[2,4,3],[1,1,1]])
B=np.array([8,13,4])
x=linalg.solve(A,B)
print('方法 1 结果:',x)

""" 方法 2：利用 scipy 中的 fsolve """
def fn(x):
    x1,x2,x3 = x.tolist()
    return np.array([
                     3 * x1 + 2 * x2 + x3 - 8,
                     2 * x1 + 4 * x2 + 3 * x3 -13, 
                     x1 + x2 + x3 - 4
                    ])

x = fsolve(fn,[0,0,0])
print('方法 2 结果:',x)