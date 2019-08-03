import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy import optimize
%matplotlib inline
np.random.seed(1)

""" 波谱结果 """
x = np.linspace(-20, 20, 100)
y_pseudo = [-0.00248934,  0.00660973, -0.01499657, -0.00593002, -0.01059732,
            -0.01222984, -0.00941219, -0.00463318, -0.00309698,  0.0011645 ,
            -0.00242416,  0.00555659, -0.00886643,  0.01134352, -0.01417837,
             0.00511403, -0.00248086,  0.00176069, -0.01078839, -0.00905696,
             0.00902234,  0.01404785, -0.00559727,  0.00576969,  0.0112917 ,
             0.01183827, -0.01244846, -0.01382776, -0.00990341,  0.01134916,
            -0.01203371, -0.0023058 ,  0.01399596,  0.00208404,  0.00992414,
             0.00843571,  0.04592197,  0.10957541,  0.19498126,  0.38269323,
             0.58680565,  0.75058519,  0.81711833,  0.79128984,  0.63220633,
             0.4692239 ,  0.3354238 ,  0.2243627 ,  0.18357212,  0.1713328 ,
             0.17452784,  0.20220142,  0.19107449,  0.18825344,  0.18321358,
             0.15209686,  0.14554341,  0.10855426,  0.09777794,  0.07885836,
             0.04166768,  0.03526981,  0.03148975,  0.01412352, -0.00306878,
             0.00733429,  0.00851689,  0.00243836,  0.01439478,  0.00313511,
             0.01236541, -0.01075211, -0.01076598,  0.00924586, -0.00305968,
            -0.01003538,  0.01282679, -0.00456646,  0.00752456,  0.00678001,
             0.0114992 ,  0.00371017,  0.00752828, -0.00453305, -0.00690216,
             0.01187659, -0.00215726,  0.0139452 ,  0.00490324,  0.00365087,
            -0.01155762,  0.01348468, -0.00150264,  0.00235169, -0.0027559 ,
            -0.00788919,  0.01210139,  0.00221038, -0.01491389,  0.00351435]

""" 定义MSE函数 """
def mse():
    x = np.linspace(-20, 20, 100)
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
gauss = lambda p: p[0] / p[1] / math.sqrt(2 * math.pi) * np.exp(-(x-p[2])**2/2/p[1]**2)
gauss1, gauss2, gauss3 =  gauss(p[0:3]), gauss(p[3:6]), gauss(p[6:9])

""" 结果及作图 """
fitting = gauss1 + gauss2 + gauss3
r2 = round(r2_score(y_pseudo, fitting),4)
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(1,1,1)
pseudo, = ax.plot(x, y_pseudo, color='red', label='pseudo spectrum', linewidth=1.5, ls='solid')
gauss1, = ax.plot(x, gauss1, color='blue', label='Guass1', linewidth=1.5, ls='--')
gauss2, = ax.plot(x, gauss2, color='purple', label='Guass2', linewidth=1.5, ls='--')
gauss3, = ax.plot(x, gauss3, color='orange', label='Guass3', linewidth=1.5, ls='--')
fitting, = ax.plot(x, fitting, color='black', label='Fitting line', linewidth=1.5, ls='-.')
ax.tick_params(color='white',labelsize=12, labelcolor='white')
plt.legend(fontsize=12)
plt.text(-15, 0.4,'r2='+str(r2), fontsize=12)
plt.show()

print('|       |{:>10}|{:>10}|{:>10}|'.format('A','μ','σ'))
print(f'|Gauss 1|{p[0]:>10.2f}|{p[2]:>10.2f}|{p[1]:>10.2f}|')
print(f'|Gauss 2|{p[3]:>10.2f}|{p[5]:>10.2f}|{p[4]:>10.2f}|')
print(f'|Gauss 3|{p[6]:>10.2f}|{p[8]:>10.2f}|{p[7]:>10.2f}|')