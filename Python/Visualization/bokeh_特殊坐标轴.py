import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from bokeh.models import ColumnDataSource # 导入ColumnDataSource模块
from bokeh.plotting import figure,show # 导入图表绘制、图标展示模块
from bokeh.io import output_notebook
output_notebook() # 导入notebook绘图模块

""" 轴线类型设置 """

''' 1. 设置对数坐标轴 '''
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y = [10**xx for xx in x]

p = figure(plot_width=400, 
           plot_height=300, 
           y_axis_type="log")  # y_axis_type="log" → 对数坐标轴

p.line(x, y, line_width=2)
p.circle(x, y, fill_color="white", size=8)

show(p)

''' 2. 字符串坐标轴标签  '''
# 当x轴为字符串而非数字时，需将df数据转换为 ColumnDataSource '''

# (1) 构造 series 或 dataframe 数据
df = pd.DataFrame({'score':[98,86,74,67,87]},index = ['小明','小王','小张','小唐','小周'])
# (2) 把横坐标转化为 list 格式 '''
df.index.name = 'name'      # 设置 index 的标题
name = df.index.tolist()    # 提取 name
# (3) 把 series 或 dataframe 数据转换为 ColumnDataDource 数据
source = ColumnDataSource(df)
# (4) 关键步骤： 在创建画布时，把 x_range 设置为之前提取的 list
p = figure(x_range=name,      # 通过 x_range 设置横轴标签，即把上一步提取出的 name 设置为横轴标签
           y_range=(60,100), 
           plot_width=400,
           plot_height=300, 
           title="考试成绩",
           tools="")
# (5) 绘图 (注意导入 source 数据) 并显示
p.circle(x = 'name', y = 'score', 
         source = source,     # 导入 ColumnDataSource 对象
         size = 10, line_color = 'black', line_dash = [6,4],
         fill_color = 'red',fill_alpha = 0.8)
show(p)

''' 3. 设置时间序列坐标轴  '''
# Dataframe DatetimeIndex + x_axis_type

from bokeh.sampledata.commits import data # 导入数据，查看数据

DAYS = ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']
source = ColumnDataSource(data)
p = figure(plot_width=400, plot_height=300, 
           y_range=DAYS,                     # 设置图表的y轴刻度分类
           x_axis_type='datetime',           # 设置x轴类型 → 时间序列
           title="Commits by Time of Day (US/Central) 2012-2016")
p.circle(x='time', y='day',  source=source, alpha=0.2)
p.ygrid.grid_line_color = None
show(p)