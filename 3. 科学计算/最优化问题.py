""" 
计算 (2+x1)/(1+x2) - 3*x1+4*x3 的最小值  
s.t. 0.1 < x1 < 0.9, 0.2 < x2 < 1, -1 < x3 < 0

"""

import numpy as np
from scipy.optimize import minimize

# 定义函数
def fn():
    y= lambda x: (2+x[0])/(1+x[1]) -3*x[0]+4*x[2]
    return y

# 定义约束条件
# 约束条件 分为eq 和ineq
# eq表示 函数结果等于0 ； ineq 表示 表达式大于等于0  
cons = ({'type': 'ineq', 'fun': lambda x: x[0] - 0.1},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 0.9},
        {'type': 'ineq', 'fun': lambda x: x[1] - 0.2},
        {'type': 'ineq', 'fun': lambda x: -x[1] + 0.8},
        {'type': 'ineq', 'fun': lambda x: x[2] - (-1)},
        {'type': 'ineq', 'fun': lambda x: -x[2] + 0})


#设置初始猜测值  
x0 = np.array((0.5,0.5,0.5))
res = minimize(fn(), x0, constraints=cons)

print(res.fun)
print(res.x)