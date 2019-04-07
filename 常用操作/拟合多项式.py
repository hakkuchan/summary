import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.metrics import r2_score
%matplotlib inline

a_, b_, c_ = 1, 3, 1
xdata = np.linspace(-1,1,num=100)
ydata = np.array([a_*x**2 + b_*x + c_ + random.uniform(-0.15, 0.15) for x in xdata])
plt.scatter(xdata, ydata)
plt.show()

def fn(x, a, b, c):
    return a * x ** 2 + b * x + c

params, params_covariance = optimize.curve_fit(fn, xdata, ydata)

def calculate_r2(params, xdata, ydata):
    y_calcd = params[0] * xdata ** 2 + params[1] * xdata +params[2]
    r2 = r2_score(ydata, y_calcd)
    return r2

r2 = calculate_r2(params, xdata, ydata)

print('Curve form: y = ax^2 + bx + c')
print('          |{:>10}|{:>10}|{:>10}|{:>10}|'.format('a','b','c','r2'))
print('Real curve|{:>10.0f}|{:>10.0f}|{:>10.0f}|{:>10}|'.format(a_,b_,c_,'/'))
print(' Fit curve|{:>10.2f}|{:>10.2f}|{:>10.2f}|{:>10.4f}|'.format(params[0], params[1], params[2], r2))