""" 散点图：(1) 基本散点图绘制; (2) 散点图颜色、大小设置方法; (3) 不同符号的散点图。"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from bokeh.io import output_notebook
output_notebook() # 导入notebook绘图模块
from bokeh.plotting import figure,show # 导入图表绘制、图标展示模块

''' 1、基本散点图绘制 '''

# 创建数据
s = pd.Series(np.random.randn(80))

# 创建画布
p = figure(plot_width=400, plot_height=300)  

# ciecle() 绘制散点图
p.circle(x=s.index, y=s.values,   # x，y值
         size=20, # 点大小
#          radius = 2,    # 设置点的半径，和size只能同时选一个
         color="navy",  # 点及其边线的颜色，优先级低于后面的 fill_color 参数
         alpha=0.1,     # 点的透明度，优先级低于后面的 fill_alpha 参数
         fill_color = 'green',  # 点填充的颜色
         fill_alpha = 0.6,      # 点填充的透明度
         line_color = 'blue',   # 点边线的颜色
         line_alpha = 0.8,      # 点边线的透明度
         line_dash = 'dashed',  # 点边线虚线
         line_width = 2,        # 点边线宽度
         legend = 'scatter-circle',    # 设置图例

        )

# 设置图例位置
p.legend.location = "top_right"
show(p)


''' 2、散点图不同颜色/大小的方法 '''
from bokeh.palettes import brewer

# 创建数据，有2列随机值
rng = np.random.RandomState(1)
df = pd.DataFrame(rng.randn(50,2)*100,columns = ['A','B'])

# 调色盘设置方法一：
df['size'] = rng.randint(10,30,50)   # 设置点大小字段
colormap = {1: 'red', 2: 'green', 3: 'blue'}    
df['color'] = [colormap1[x] for x in rng.randint(1,4,50)]           

# 调色盘 (蓝色渐变) 设置方法二：
n = 8
colormap = brewer['Blues'][n]
df['color'] = [colormap2[x] for x in rng.randint(0,n,50)]

# 创建画布
p = figure(plot_width=400, plot_height=300)
p.circle(df['A'], df['B'],          # 设置散点图x，y值
         line_color= None,          # 设置点边线为白色
         fill_color = df['color'],  # 设置内部填充颜色
         fill_alpha = 1,          # 设置填充透明度
         size = df['size']          # 设置点大小
        )

show(p)


''' 3. 不同符号的散点图  '''

# 创建画布
p = figure(plot_width=600, plot_height=400,x_range = [0,3], y_range = [0,7])

# 创建不同类型的点
p.x(2, 6, size=30, alpha=1, legend='x')
p.cross(1, 1, size=30, alpha=1, legend='cross')
p.square(1, 2, size=30, alpha=1, legend='square')
p.diamond(1, 3, size=30, alpha=1, legend='diamond')
p.asterisk(1, 4, size=30, alpha=1, legend='asterisk')
p.circle_x(1, 5, size=30, alpha=1, legend='circle_x')
p.square_x(1, 6, size=30, alpha=1, legend='square_x')
p.triangle(2, 1, size=30, alpha=1, legend='triangle')
p.square_cross(2, 2, size=30, alpha=1, legend='square_cross')
p.circle_cross(2, 3, size=30, alpha=1, legend='circle_cross')
p.diamond_cross(2, 4, size=30, alpha=1, legend='diamond_cross')
p.inverted_triangle(2, 5, size=30, alpha=1, legend='inverted_triangle')

# 设置图例位置
p.legend.location = "bottom_right"

# 显示
show(p)