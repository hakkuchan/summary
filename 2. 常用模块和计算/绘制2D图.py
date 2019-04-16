""" 
5步：准备数据 --> 生成画布 --> 画图 --> 修饰 --> 显示/保存
"""
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline 

""" 准备数据 """
X = np.linspace(-10,10,200)
Y1 = np.sin(X)
Y2 = np.cos(X)

""" 生成画布 """
fig = plt.figure(figsize=(8,6))  # 设置画布

""" 画图 """
ax = fig.add_subplot(1,1,1)
line1 = ax.plot(X, Y1, 
                 color='blue', # 颜色
                 #marker='o',  # 点线图中的点样式
                 ls = '--',    # 线样式
                 linewidth = 2,  # 线宽
                 label='sin')    # 图例
line2 = ax.scatter(X, Y2, color='red', label='cos', s=3)
line3 = ax.plot(X, Y1+Y2, color='green', label='sin+cos')

""" 修饰 """
ax.grid()           # 背景添加网格

fig.tight_layout()  # 自动调整版面

ax.legend(loc='best')   # 设置图例位置

ax.set_xlabel('X', fontsize=14, color='white')      # 显示x轴名称
ax.set_ylabel('Y', fontsize=14, color='white')      # 显示y轴名称
ax.set_title('X vs. Y', fontsize=16, color='white') # 显示图名

ax.set_xlim((-10, 10))    # 设置 x 轴范围
ax.set_ylim((-2, 2))      # 设置 y 轴范围

ax.set_xticks(np.linspace(-10, 10, 9))  # 设置坐标轴刻度
ax.tick_params(color='white', labelsize=14, labelcolor='white')  # 设置坐标轴样式

plt.text(-3, 1.5, 'Trigonometric function', fontdict={'size': 14, 'color': 'red'})  # 显示、设置标注

plt.legend(fontsize=14)  # 显示、设置图例字号

""" 显示/保存 """
plt.savefig('example.png') # 设置画布的 figsize 参数可调节图大小 
plt.show()  # 绘图