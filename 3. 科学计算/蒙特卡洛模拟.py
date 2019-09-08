"""
蒙特卡罗（Monte Carlo）方法，又称随机抽样或统计试验方法：

将所求解的问题同一定的概率模型相联系，用计算机实现统计模拟或抽样，以获得问题的近似解。
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


""" (1) π的计算 """
from matplotlib.patches import Circle

n = 10000     # 投点次数
r = 1.0           # 半径
a, b = (0., 0.)   # 圆心
x_min, x_max = a-r, a+r
y_min, y_max = b-r, b+r

# 在正方形区域内随机投点，服从均匀分布
x = np.random.uniform(x_min, x_max, n)
y = np.random.uniform(y_min, y_max, n)

d = np.sqrt((x-a)**2 + (y-b)**2) # 计算点到圆心的距离
res = sum(np.where(d < r, 1, 0)) # 统计落在圆内的点的数目

pi = 4 * res / n  # 计算 pi 的近似值 → Monte Carlo方法：用统计值去近似真实值
print('pi: ', pi)

# 制图
fig = plt.figure(figsize = (6,6))
axes = fig.add_subplot(1,1,1)
plt.plot(x,y,'ro',markersize = 1)
plt.axis('equal')
circle = Circle(xy = (a,b),radius = r, alpha = 0.5 ,color = 'gray')
axes.add_patch(circle)
plt.grid(True, linestyle = "--",linewidth = "0.8")
plt.show()


""" (2) 计算积分 y = x**2 """

n = 10000  # 投点次数
x_min, x_max = 0.0, 1.0  # 矩形区域边界
y_min, y_max = 0.0, 1.0   
# 在矩形区域内随机投点，服从均匀分布
x = np.random.uniform(x_min, x_max, n)
y = np.random.uniform(y_min, y_max, n)

# 创建函数 y = x**2
def f(x):
    return x**2

# 统计落在函数 y=x^2图像下方的点的数目
res = sum(np.where(y < f(x), 1, 0))

# 计算定积分的近似值
integral = res / n
print('integral: ', integral)

# 绘制散点图
fig = plt.figure(figsize = (6,6)) 
axes = fig.add_subplot(111) 
axes.plot(x, y,'ro',markersize = 1)
plt.axis('equal') 

# 绘制 y = x**2 面积图
xi = np.linspace(0,1,100)
yi = xi ** 2
plt.plot(xi,yi,'--k')
plt.fill_between(xi, yi, 0, color ='gray',alpha=0.5,label='area')  
plt.grid()