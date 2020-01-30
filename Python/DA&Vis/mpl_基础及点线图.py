""" 绘图流程：

    · Step 1：准备数据
    ↓
    · Step 2：生成画布
    ↓
    · Step 3：绘图（以点线图为例）：颜色、点样式、线样式、线宽、图例
    ↓
    · Step 4：修饰：标题、坐标轴、背景网格、标注、图例
"""


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline


''' Step 1: 准备数据 '''
X = np.linspace(-10,10,200)
Y1 = np.sin(X)
Y2 = np.cos(X)


''' Step 2: 生成画布 '''
fig = plt.figure(figsize=(8,6))  # figsize 设置画布大小


''' Step 3: 画图 (以折线图为例) '''
ax = fig.add_subplot(1,1,1)
line1 = ax.plot(X, Y1, 
                color='blue', # 颜色
                marker='o',   # 点样式
                ls = '--',    # 线样式
                linewidth=1,  # 线宽
                label='sin')  # 图例
line2 = ax.scatter(X, Y2, color='red', label='cos', s=1)
line3 = ax.plot(X, Y1+Y2, color='green', label='sin+cos')


''' Step 4: 修饰 '''

# (1) 标题
ax.set_title('Example', fontsize=16, color='black') 

# (2) 坐标轴
ax.set_xlabel('X', fontsize=14, color='blue')   # 显示x轴名称
ax.set_ylabel('Y', fontsize=14, color='blue')   # 显示y轴名称
ax.set_xlim((-10, 10))  # 设置 x 轴范围
ax.set_ylim((-2, 2))    # 设置 y 轴范围
ax.set_xticks(range(-10,10))    # 设置x刻度
ax.set_yticks([-2,-1,0,1,2])    # 设置y刻度
ax.tick_params(labelcolor='white', labelsize=14)  # 设置坐标轴样式
mpl.rcParams['xtick.direction'] = 'in'  # 设置刻度的方向: in,out,inout
mpl.rcParams['ytick.direction'] = 'out' # 设置刻度的方向，in,out,inout
# 这里需要导入matploltib

# (3) 背景网格、标注、图例
ax.grid(True, 
        linestyle = "--",
        color = "gray", 
        linewidth = "0.5",
        axis = 'both') # x,y,both
ax.text(-3, 1.5, 'Trigonometrics', fontdict={'size': 14, 'color': 'red'})  
ax.legend(loc='best', fontsize=14)  # 设置图例
# 'best'/'upper right'/'upper left'/'lower left'/'lower right'/'right'
# 'center left'/ 'center right' / 'lower center' / 'upper center' / 'center'

plt.show()