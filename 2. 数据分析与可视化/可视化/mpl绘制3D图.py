import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
%matplotlib inline

""" 生成数据 """
xdata = np.linspace(0, 1, 200)
ydata = np.linspace(0, 1, 200)
zdata1 = (3 - (xdata ** 3 + ydata ** 3)) ** (1/3) + np.random.uniform(-0.1,0.1,200)
zdata2 = (6 - (xdata ** 2 + ydata ** 2)) ** 0.5 + np.random.uniform(-0.1,0.1,200)

""" 生成画布并绘图 """
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
line1 = ax.scatter(xdata, ydata, zdata1, label='Y1',s=10)
line2 = ax.plot(xdata, ydata, zdata2, label='Y2', linewidth=1)

""" 图修饰 """
ax.grid()         # 背景添加网格
ax.legend()       # 显示图例
ax.set_xlabel('X Label')    # 显示 X 轴名称
ax.set_ylabel('Y Label')    # 显示 Y 轴名称
ax.set_zlabel('Z Label')    # 显示 Z 轴名称
ax.set_title('X vs. Y vs. Z')  # 显示图名
plt.show()    # 绘图


""" Example 2："""

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
ax.set_zlim(-2, 2)
plt.show()