""" 
画图5步流程：画布 --> 画框 --> 画图 --> 修饰 --> 显示 
	1) 画布：fig = plt.figure(figsize=(x,x))
	2) 画框：ax = fig.add_subplot(1,1,1)
	3) 画图：line1, = ax.plot(...)
	      line2, = ax.scatter(...)
    4) 修饰(以x为例)：set_xlabel, xticks, xlim, title
    5) 显示：plt.legend(), plt.text(), plt.show()	
"""

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline 

""" 数据 """
X = np.linspace(-1,1,200)                         # 在-1至1范围内生成200个x
Y = 0.5 * X + 2 + np.random.uniform(-0.1,0.1,200) # 生成y

""" 生成画布并绘图 """
fig = plt.figure(figsize=(4,4))  # 设置画布
ax = fig.add_subplot(1,1,1)      # 设置画框(1,1,1 表示 1 行 1 个画框 绘图在第一个画框中)
line1, = ax.plot(X, Y, color='blue',label='Y1',linewidth=3)     # 添加一条曲线 line1, line1 后面必须有逗号,否则不显示图例
line2, = ax.plot(X, Y+1, color='green',label='Y2',linewidth=1)  # 添加一条曲线 line2
line3  = ax.scatter(X, Y+2, color='red',label='Y3', s=2)        # 添加一条散点线 line3 ,散点线 line3 后面不能加逗号

""" 图修饰 """
ax.grid()          # 背景添加网格

fig.tight_layout()   # 自动调整版面

ax.legend(loc='best')   # 显示图例

ax.set_xlabel('X')      # 显示x轴名称
ax.set_ylabel('Y')      # 显示y轴名称
ax.set_title('X vs. Y') # 显示图名

ax.set_xlim((-1.5, 1.5))    # 设置 x 轴范围
ax.set_ylim((1, 5))         # 设置 y 轴范围

new_ticks = np.linspace(-1.5, 1.5, 6) # 设置刻度
ax.set_xticks(new_ticks)

plt.text(0.5, 1.5, 'Example', fontdict={'size': 12, 'color': 'red'}) # 显示、设置标注

plt.legend(fontsize=12) # 显示、设置图例字号

plt.show()    # 绘图