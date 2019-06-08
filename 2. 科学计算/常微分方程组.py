import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline

"""
常微分方程组（以洛伦兹方程为例）：
dx/dt = p(y-x)
dy/dt = x(r-z)-y
dz/dt = xy - bz
"""

""" 定义常微分方程组 """
def lorentz(w,t,p,r,b):
    """
    w：位置矢量
    t: 时间
    p,r,b：其他参数
    """
    x,y,z = w.tolist()
    dx_dt = p*(y-x)
    dy_dt = x*(r-z)-y
    dz_dt = x*y - b*z
    return dx_dt, dy_dt, dz_dt
 
""" 调用 odeint 对常微分方程组 odeint 进行求解 """
t = np.arange(0,30,0.01)  # 设定时间
track = odeint(lorentz,(0,0,0),t,args = (10,30,3)) 
# 其中，(0,0,0) 是位置矢量 w 的初值; args设定的是常微分方程组中的参数 p,r,b

""" 画3维空间的曲线 """ 
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(out[:,0],out[:,1],out[:,2], color='red', linewidth=1) # out[:,0],out[:,1],out[:,2] 分别是不同 t 下的 x, y, z
plt.show()