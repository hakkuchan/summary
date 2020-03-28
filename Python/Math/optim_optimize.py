""" · 最优化方法：在一系列约束条件下，使某个或多个指标达到最大/最小的技术

    · 目录
    |
    |—— 1. minimize方法
    |
    |—— 2. leastsq方法
    |
    |—— 3. curve_fit方法  
"""

import numpy as np
from scipy import optimize

""" 1. minimize方法
    
    例：计算当目标函数 (2+x1)/(1+x2)-3*x1+4*x3 最小时，决策变量 x1、x2、x3 的取值
        约束条件： 0.1 < x1 < 0.9, 0.2 < x2 < 1.0, -1. < x3 < 0.0
"""
# Step 1: 构建目标函数，须为lambda表达式
def fn():
    y= lambda x: (2+x[0])/(1+x[1]) -3*x[0]+4*x[2] # 决策变量为 x[0], x[1], x[2]
    return y
#  Step 2: 定义约束条件 (注：约束条件2种：eq表示等于0；ineq表示大于等于 0)
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 0.1},  # x[0] ≥ 0.1
        {'type': 'ineq', 'fun': lambda x: -x[0] + 0.9},  # x[0] ≤ 0.9 
        {'type': 'ineq', 'fun': lambda x:  x[1] - 0.2},  # x[1] ≥ 0.2
        {'type': 'ineq', 'fun': lambda x: -x[1] + 0.8},  # x[1] ≤ 0.8
        {'type': 'ineq', 'fun': lambda x:  x[2] - (-1)}, # x[2] ≥ -1
        {'type': 'ineq', 'fun': lambda x: -x[2] + 0})    # x[2] ≤ 0
# Step 3: 求解 '''
init = np.array((0, 0, 0)) # 设置初始值
out = optimize.minimize(fn(), init, method='SLSQP', constraints=cons) # 求解最优化问题
print(out.fun)   # 目标函数的最优解
print(out.x)     # 最优解对应的 x


""" 2. leastsq方法 (最小二乘拟合，目标函数是误差的平方和) """
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


""" 3. curve_fit方法 (曲线拟合，本质上也是最优化问题) """
# Toy data
x = np.arange(1,11)
y = 3*x**2 + 5*x + 10 + np.random.uniform(-0.1, 0.1, 10)
# 定义待拟合函数
def fn(x, a, b, c):
    return a*x**2 + b*x + c
# 拟合
out = optimize.curve_fit(fn, x, y)
print(out[0])