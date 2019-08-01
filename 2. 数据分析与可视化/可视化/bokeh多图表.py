""" 多图表设置 gridplot """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from bokeh.models import ColumnDataSource # 导入ColumnDataSource模块
from bokeh.plotting import figure,show # 导入图表绘制、图标展示模块
from bokeh.io import output_notebook
output_notebook() # 导入notebook绘图模块

from bokeh.layouts import gridplot # 导入gridplot模块

# 创建数据
x = list(range(11))
y0 = x
y1 = [10-xx for xx in x]
y2 = [abs(xx-5) for xx in x]

# 散点图1
s1 = figure(plot_width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# 散点图2，设置和散点图1一样的x_range/y_range → 图表联动
s2 = figure(plot_width=250, plot_height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# 散点图3，设置和散点图1一样的x_range/y_range → 图表联动
s3 = figure(plot_width=250, plot_height=250, x_range=s1.x_range, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

# 组合图表
p = gridplot([[s1, s2, s3]]) # 1 行 3 表
p = gridplot([[s1, s2],[s3, None]]) # 2 行

# 显示
show(p)