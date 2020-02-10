""" 1. 概述

    · 最优化方法：在一系列限制条件下，寻求使某个或多个指标达到最大（或最小）的方法。
      三个要素：决策变量、目标函数、约束条件。
      其它术语：可行域、可行解、最优解、全局最优解、局部最优解、最优值。

    · 分类
      按约束：无约束优化、约束优化
      按变量：连续优化、组合优化
      按求解：目标规划、动态规划、多层规划、网络优化
      按参数：确定性规划、随机规划
      按目标：单目标规划、多目标规划



    2. Python求解最优化模型

    · 计算当目标函数 (2+x1)/(1+x2)-3*x1+4*x3 最小时，决策变量 x1、x2、x3 的取值
      s.t. 0.1 < x1 < 0.9,  0.2 < x2 < 1.0,  -1. < x3 < 0.0
"""
import numpy as np
from scipy.optimize import minimize

# Step 1: 构建目标函数，必须为lambda表达式形式
def fn():
    y= lambda x: (2+x[0])/(1+x[1]) -3*x[0]+4*x[2] # 决策变量为 x[0], x[1], x[2]
    return y

# Step 2: 定义约束条件
# (注：约束条件有 eq 和 ineq 两种：eq 表示等于0；ineq 表示大于等于 0)
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 0.1},  # x[0] > 0.1
        {'type': 'ineq', 'fun': lambda x: -x[0] + 0.9},  # x[0] < 0.9 
        {'type': 'ineq', 'fun': lambda x:  x[1] - 0.2},  # x[1] > 0.2
        {'type': 'ineq', 'fun': lambda x: -x[1] + 0.8},  # x[1] < 0.8
        {'type': 'ineq', 'fun': lambda x:  x[2] - (-1)}, # x[2] > -1
        {'type': 'ineq', 'fun': lambda x: -x[2] + 0})    # x[2] < 0

# Step 3: 求解
init = np.array((0, 0, 0)) # 设置初始猜测值
out = minimize(fn(), init, constraints=cons) # 求解最优化问题
print(out.fun)   # 目标函数的最优解
print(out.x)     # 最优解对应的 x