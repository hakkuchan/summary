''' bokeh绘图流程 '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from bokeh.plotting import figure,show # 导入图表绘制、图标展示模块
from bokeh.io import output_notebook   # 导入notebook绘图模块以确保在 jupyter notebook 中使用
output_notebook() # notebook绘图命令

# (1) 提取数据
df = pd.DataFrame(np.random.randn(100,2),columns = ['A','B'])

# (2) 创建绘图空间（画布）
p = figure(plot_width=600, plot_height=400,         # 图表宽度、高度
           tools = 'pan, wheel_zoom, box_zoom, save, reset,help',  # 设置工具栏，默认全部显示
           toolbar_location='above',                # 工具栏位置："above"，"below"，"left"，"right"
           x_axis_label = 'A', y_axis_label = 'B',  # X,Y轴label
           x_range = [-3,3], y_range = [-3,3],      # X,Y轴范围
           title="Simple example"                   # 设置图表title
          )
 
# (3) 绘图
p.circle(df['A'], df['B'], size=20, alpha=0.5)

# (4) 显示
show(p)

''' 设置标题：颜色、字体、风格、背景颜色 '''
df = pd.DataFrame(np.random.randn(100,2),columns = ['A','B'])
p = figure(plot_width=600, plot_height=400, title="Simple example")
p.circle(df['A'], df['B'], size=20,  alpha=0.5)
p.title.text_color = "white"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.title.background_fill_color = "blue"
show(p)


''' 颜色设置 ''' 
# (1) 147个CSS颜色，参考网址：http://www.colors.commutercreative.com/grid/
# (2) RGB颜色值，参考网址：https://coolors.co/87f1ff-c0f5fa-bd8b9c-af125a-582b11
p = figure(plot_width=600, plot_height=400) # 创建绘图空间
p.circle(df.index, df['A'], color = 'red', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = 'blue', size=10,  alpha=0.5)
show(p)

''' 图表边框线参数设置 ''' 
p = figure(plot_width=600, plot_height=400)
p.circle(df['A'], df['B'], color = 'green', size=10,  alpha=0.5)
p.outline_line_width = 10         # 边框线宽
p.outline_line_alpha = 0.5        # 边框线透明度
p.outline_line_color = "navy"     # 边框线颜色
p.outline_line_dash = [6,4]       # 边框样式
show(p)

''' 设置绘图空间背景 '''
p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
p.background_fill_color = "yellow"    # 绘图空间背景颜色
p.background_fill_alpha = 0.3        # 绘图空间背景透明度
show(p)

''' 设置外边界背景 '''
p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
p.border_fill_color = "whitesmoke"    # 外边界背景颜色
p.border_fill_alpha = 0.8             # 外边界透明度
p.min_border_left = 50                # 外边界背景 - 左边宽度
p.min_border_right = 50               # 外边界背景 - 右边宽度
p.min_border_top = 30                 # 外边界背景 - 上宽度
p.min_border_bottom = 30              # 外边界背景 - 下宽度
show(p)

''' 轴线设置 '''
# 轴线标签、轴线线宽、轴线颜色
# 字体颜色、字体角度
p = figure(plot_width=400, plot_height=400)
p.circle([1,2,3,4,5], [2,5,8,2,7], size=10)
# 设置x轴线：标签、线宽、轴线颜色
p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"
# 设置y轴线：标签、字体颜色、字体角度
p.yaxis.axis_label = "Pressure"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"
# 设置刻度
p.axis.minor_tick_in = 0    # 刻度往绘图区域内延伸长度
p.axis.minor_tick_out = 5   # 刻度往绘图区域外延伸长度
# 设置轴线范围
p.xaxis.bounds = (2,4)
show(p)

''' 轴标签设置 '''
p = figure(plot_width=400, plot_height=400)
p.circle([1,2,3,4,5], [2,5,8,2,7], size=10)
# 设置标签名称、字体颜色、偏移距离
p.xaxis.axis_label = "Lot Number"
p.xaxis.axis_label_text_color = "#aa6666"
p.xaxis.axis_label_standoff = 30
# 设置标签名称、字体
p.yaxis.axis_label = "Bin Count"
p.yaxis.axis_label_text_font_style = "italic"
p.yaxis.axis_label_text_font_size = "22pt"
show(p)

''' 背景网格线  '''
p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = '#FF0000', size=10,  alpha=0.5)
p.xgrid.grid_line_color = None   # 颜色设置，None时则不显示
p.ygrid.grid_line_alpha = 0.8    # 设置透明度，虚线设置
p.ygrid.grid_line_dash = [6, 4]  # dash → 通过设置间隔来做虚线
p.xgrid.minor_grid_line_color = 'navy'  # minor_line → 设置次轴线
p.xgrid.minor_grid_line_alpha = 0.1
show(p)

''' 背景网格线填充 '''
# 绘制散点图
p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
# 设置颜色为空
p.xgrid.grid_line_color = None
# 设置颜色填充，及透明度
p.ygrid.band_fill_alpha = 0.1
p.ygrid.band_fill_color = "navy"
# 设置填充边界
p.grid.bounds = (-1, 1)
show(p)

''' 图例 '''
p = figure(plot_width=600, plot_height=400)
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
# 绘制line1，设置图例名称
p.circle(x, y, legend="sin(x)")
p.line(x, y, legend="sin(x)")
# 绘制line2，设置图例名称
p.line(x, 2*y, legend="2*sin(x)",line_dash=[4, 4], line_color="orange", line_width=2)
# 绘制line3，设置图例名称
p.square(x, 3*y, legend="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3*y, legend="3*sin(x)", line_color="green")

# 设置图例位置："top_left"、"top_center"、"top_right" (the default)、"center_right"、"bottom_right"、"bottom_center"
# "bottom_left"、"center_left"、"center"
p.legend.location = "bottom_left"
# 设置图例排列方向："vertical" （默认）or "horizontal"
p.legend.orientation = "vertical"
# 设置图例：字体、风格、颜色、字体大小
p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"  # 斜体
p.legend.label_text_color = "navy"
p.legend.label_text_font_size = '12pt'
# 设置图例外边线：宽度、颜色、透明度
p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.5
# 设置图例背景：颜色、透明度
p.legend.background_fill_color = "gray"
p.legend.background_fill_alpha = 0.2
show(p)