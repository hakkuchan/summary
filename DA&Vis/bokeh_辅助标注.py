""" 辅助线、矩形、注释、矢量箭头 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from bokeh.plotting import figure,show # 导入图表绘制、图标展示模块
from bokeh.io import output_notebook
output_notebook() # 导入notebook绘图模块

''' 辅助标注 - 线 '''
from bokeh.models.annotations import Span # 导入Span模块画辅助线

# 创建数据并绘图
x = np.linspace(0, 20, 200)
y = np.sin(x) 
p = figure(y_range=(-2, 2))
p.line(x, y)

# 绘制辅助线1
upper = Span(location=1,           # 设置位置，对应坐标值
             dimension='width',    # 设置方向，width为横向，height为纵向  
             line_color='olive',   # 设置线颜色
             line_width=4          # 设置线宽
            )
p.add_layout(upper) # 在图中增加辅助线

# 绘制辅助线2
lower = Span(location=-1, dimension='width', line_color='firebrick', line_width=4)
p.add_layout(lower)

# 显示
show(p)


''' 辅助标注 - 矩形 '''
from bokeh.models.annotations import BoxAnnotation # 导入BoxAnnotation模块

# 创建数据并绘图
x = np.linspace(0, 20, 200)
y = np.sin(x)
p = figure(y_range=(-2, 2))
p.line(x, y)

# 绘制辅助矩形1
upper = BoxAnnotation(bottom=1, fill_alpha=0.1, fill_color='olive', line_width=2, line_dash=[6,2], line_color='red')
p.add_layout(upper)  # 在图中增加注释
# 绘制辅助矩形2
middle = BoxAnnotation(top=0.6, bottom=-0.6, left=7, right=12,  # 设置矩形四边位置
                       fill_alpha=0.1, fill_color='navy'        # 设置透明度、颜色
                      )
p.add_layout(middle)
# 绘制辅助矩形3
lower = BoxAnnotation(top=-1, fill_alpha=0.5, fill_color='firebrick')
p.add_layout(lower)

# 显示
show(p)


''' 注释 '''
from bokeh.models.annotations import Label # 导入Label模块，注意是 annotations中的 Label

# 绘制散点图
p = figure(plot_width=300, plot_height=300, x_range=(0,10), y_range=(0,10))
p.circle([2, 5, 8], [4, 7, 6], color="olive", size=10)

# 绘制注释
label = Label(x=5, y=7,                 # 标注注释位置
              x_offset=12,              # x偏移，同理y_offset
              text="Second Point",      # 注释内容
              text_font_size="12pt",    # 字体大小
              border_line_color="red",  # 背景线条颜色
              background_fill_color="gray",  # 背景颜色
              background_fill_alpha = 0.5,   # 透明度
              border_line_dash=[6,4]
             )
p.add_layout(label)

# 显示
show(p)


''' 箭头 '''
from bokeh.models.annotations import Arrow
from bokeh.models.arrow_heads import OpenHead, NormalHead, VeeHead   # 三种箭头类型

# 绘制散点图
p = figure(plot_width=300, plot_height=300)
p.circle(x=[0, 1, 0.5], y=[0, 0, 0.7], radius=0.05, color=["green", "blue", "red"], fill_alpha=0.1)

# 绘制箭头1
p.add_layout(Arrow(end=OpenHead(line_color="firebrick", line_width=4), # 箭头类型，及相关参数：OpenHead, NormalHead, VeeHead
                   x_start=0, y_start=0, x_end=1, y_end=0))  # 设置箭头矢量方向
# 绘制箭头2
p.add_layout(Arrow(end=NormalHead(fill_color="orange"),
                   x_start=1, y_start=0, x_end=0.5, y_end=0.7))
# 绘制箭头3
p.add_layout(Arrow(end=VeeHead(size=35), line_color="red",
                   x_start=0.5, y_start=0.7, x_end=0, y_end=0))

# 显示
show(p)