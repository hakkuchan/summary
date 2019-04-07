import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy import optimize, integrate
%matplotlib inline

""" 生成伪谱图 """
np.random.seed(1)
x = np.linspace(-50, 50, 300)
y_pseudo = (6 / 6 / math.sqrt(2 * math.pi) * np.exp(-(x-0)**2/2/6**2)
          + 6 / 4 / math.sqrt(2 * math.pi) * np.exp(-(x+15)**2/2/4**2)
          + np.random.uniform(-0.02,0.02,300))
		 

""" 定义高斯函数，这个函数只能用来求子峰面积 """
def gauss(x, A, S):
    y = A / S / math.sqrt(2 * math.pi) * np.exp(-(x-0)**2/2/S**2)
    return y


""" 定义子峰函数

    如果需要4个子峰，就要定义 4 个子峰函数
	
	注意：每个子峰的 u_fit 决定了峰位置
"""
def gauss_fit1(x, A, S):
    u_fit1 = -20
    y = A / S / math.sqrt(2 * math.pi) * np.exp(-(x-u_fit1)**2/2/S**2)    # Gauss function
    return y, u_fit1

def gauss_fit2(x, A, S):
    u_fit2 = -14
    y = A / S / math.sqrt(2 * math.pi) * np.exp(-(x-u_fit2)**2/2/S**2)    # Gauss function
    return y, u_fit2

def gauss_fit3(x, A, S):
    u_fit3 = -1.5
    y = A / S / math.sqrt(2 * math.pi) * np.exp(-(x-u_fit3)**2/2/S**2)    # Gauss function
    return y, u_fit3

def gauss_fit4(x, A, S):
    u_fit4 = 3
    y = A / S / math.sqrt(2 * math.pi) * np.exp(-(x-u_fit4)**2/2/S**2)    # Gauss function
    return y, u_fit4


""" 定义 MSE 函数 """
def MSE(param):    
    y_fit1, u_fit1 = gauss_fit1(x,*param[0:2])
    y_fit2, u_fit2 = gauss_fit2(x,*param[2:4])
    y_fit3, u_fit3 = gauss_fit3(x,*param[4:6])
    y_fit4, u_fit4 = gauss_fit4(x,*param[6:8]) 
    y_fit = y_fit1 + y_fit2 + y_fit3 + y_fit4
    MSE = np.sum(np.power(y_fit - y_pseudo, 2)) / len(x)
    return MSE


""" 谱图拟合 """
fit = optimize.minimize(MSE, [1, 1, 1, 1, 1, 1, 1, 1])
A_fit1, S_fit1, A_fit2, S_fit2, A_fit3, S_fit3, A_fit4, S_fit4  = fit.x[0:8]
y_fit1, u_fit1 = gauss_fit1(x, A_fit1, S_fit1)
y_fit2, u_fit2 = gauss_fit2(x, A_fit2, S_fit2)
y_fit3, u_fit3 = gauss_fit3(x, A_fit3, S_fit3)
y_fit4, u_fit4 = gauss_fit4(x, A_fit3, S_fit4)
y_fit = y_fit1 + y_fit2 + y_fit3 + y_fit4
r2 = r2_score(y_pseudo, y_fit)

""" 计算子峰面积及相对比例 """
peak_param = list(fit.x)
peak_seq = [num+1 for num in range(int(len(peak_param)/2))]
peak_info = [peak_param[i:i+2] for i in range(0, len(peak_param), 2)]
peak_area = [integrate.quad(gauss, -40, 40, args = tuple(ele))[0] for ele in peak_info]
peak_ratio = [ele/sum(peak_area)*100 for ele in peak_area]
print(11 * ' '+'|{:>10}|{:>10}|'.format('A', '%'))
for r,s,t in zip(peak_seq, peak_area, peak_ratio):
    print('    Gauss {}|{:>10.2f}|{:>10.2f}|'.format(r,s,t))


""" 作图 """
fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot(1,1,1)
pseudo, = ax.plot(x, y_pseudo, label=('Pseudo: A=6|6   u=0|-15   S=6|4'),color='red',linewidth=1.25)
Gauss1, = ax.plot(x, y_fit1, 
                 label=('Gauss1: A='+str(round(A_fit1,2)))+'  u='+str(round(u_fit1,2))+'  S='+str(round(S_fit1,2)),
                 color='green',linewidth=1.25)
Gauss2, = ax.plot(x, y_fit2, 
                 label=('Gauss2: A='+str(round(A_fit2,2)))+'  u='+str(round(u_fit2,2))+'  S='+str(round(S_fit2,2)),
                 color='blue',linewidth=1.25)
Gauss3, = ax.plot(x, y_fit3, 
                 label=('Gauss3: A='+str(round(A_fit3,2)))+'  u='+str(round(u_fit3,2))+'  S='+str(round(S_fit3,2)),
                 color='purple',linewidth=1.25)
Gauss4, = ax.plot(x, y_fit4, 
                 label=('Gauss4: A='+str(round(A_fit4,2)))+'  u='+str(round(u_fit4,2))+'  S='+str(round(S_fit4,2)),
                 color='orange',linewidth=1.25)
fitting, = ax.plot(x, y_fit, label=('Fitting line'),color='black',linewidth=1.5)
plt.legend(loc='upper right',fontsize=10.5)
plt.text(-40, 0.35, 'r2 ='+str(round(r2, 6)), fontdict={'size':12, 'color':'red'})
plt.show()