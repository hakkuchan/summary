import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy import optimize
%matplotlib inline
np.random.seed(1)

""" 定义 Gauss 函数 """
gauss = lambda p: p[0] / p[1] / math.sqrt(2 * math.pi) * np.exp(-(x-p[2])**2/2/p[1]**2)

""" 生成 x, y, y_pseudo 数据 """
x = np.linspace(-20, 20, 600)
p1 = [2, 1, -3] # 子峰1：[峰面积, 峰宽因子, 峰位置]
p2 = [1, 2,  1] # 子峰2：[峰面积, 峰宽因子, 峰位置]
y = gauss(p1) + gauss(p2) 
noise = np.random.uniform(-0.015,0.015,len(x))
y_pseudo = y + noise

""" 定义MSE函数 """
def mse():
    x = np.linspace(-20, 20, 600)
    mse = lambda p: np.sum(np.power(
                      (#面积   #峰宽                                      #位置      #峰宽
                       (p[0] / p[1] / math.sqrt(2 * math.pi) * np.exp(-(x-p[2])**2/2/p[1]**2)) +  # Gauss 1
                       (p[3] / p[4] / math.sqrt(2 * math.pi) * np.exp(-(x-p[5])**2/2/p[4]**2)) +  # Gauss 2
                       (p[6] / p[7] / math.sqrt(2 * math.pi) * np.exp(-(x-p[8])**2/2/p[7]**2))    # Gauss 3
                      ) - y_pseudo,2)/len(x))   
    return mse

""" 设定初值和约束条件 """
init = np.array((1,1,-1,1,2,0.5,1,1,2))
cons = (
        {'type':'ineq', 'fun': lambda p: p[2] - (-3)},
        {'type':'ineq', 'fun': lambda p: -2 - p[2]},
        {'type':'ineq', 'fun': lambda p: p[5] - 0.5},
        {'type':'ineq', 'fun': lambda p: 1 - p[5]},
        {'type':'ineq', 'fun': lambda p: p[8] - 1},
        {'type':'ineq', 'fun': lambda p: 2 - p[8]},
       )

""" 规划 """
out = optimize.minimize(mse(), init, constraints=cons)
p = out.x
gauss1, gauss2, gauss3 =  gauss(p[0:3]), gauss(p[3:6]), gauss(p[6:9])

""" 结果及作图 """
fitting = gauss1 + gauss2 + gauss3
r2 = round(r2_score(y_pseudo, fitting),4)
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(1,1,1)
pseudo, = ax.plot(x, y_pseudo, color='red', label='pseudo spectrum', linewidth=1.5)
gauss1, = ax.plot(x, gauss1, color='blue', label='Guass1', linewidth=1.5)
gauss2, = ax.plot(x, gauss2, color='purple', label='Guass2', linewidth=1.5)
gauss3, = ax.plot(x, gauss3, color='orange', label='Guass3', linewidth=1.5)
fitting, = ax.plot(x, fitting, color='black', label='Fitting line', linewidth=1.5)
plt.legend(fontsize=12)
plt.text(-15, 0.4,'r2='+str(r2), fontsize=12)
plt.show()

print('|            |{:>10}|{:>10}|{:>10}|'.format('Area','Position','Sigma'))
print('|Gauss 1 real|{:>10.2f}|{:>10.2f}|{:>10.2f}|'.format(p1[0], p1[2], p1[1]))
print('|Gauss 2 real|{:>10.2f}|{:>10.2f}|{:>10.2f}|'.format(p2[0], p2[2], p2[1]))
print('|Gauss 1 fit |{:>10.2f}|{:>10.2f}|{:>10.2f}|'.format(p[0], p[2], p[1]))
print('|Gauss 2 fit |{:>10.2f}|{:>10.2f}|{:>10.2f}|'.format(p[3], p[5], p[4]))
print('|Gauss 3 fit |{:>10.2f}|{:>10.2f}|{:>10.2f}|'.format(p[6], p[8], p[7]))