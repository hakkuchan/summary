""" 单线图、多线图 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from bokeh.plotting import figure,show # 导入图表绘制、图标展示模块
from bokeh.io import output_notebook
output_notebook() # 导入notebook绘图模块

''' 1、折线图 - 单线图 '''

df = pd.DataFrame({'A':np.arange(100),"B":np.random.randn(100).cumsum()})

# 创建画布
p = figure(plot_width=400, plot_height=300)

# 绘制折线图
p.line(df['A'], df['B'], line_width=1, line_alpha=0.8, line_color='black', line_dash=[10,4])

# 绘制折点
p.circle(df['A'],df['B'], size=5,color='red',alpha=0.8)

# 显示
show(p)


''' 2-1、多线图 '''

# 创建数据
df1 = pd.DataFrame({'A':np.arange(100),'B':np.sin(np.arange(100))})
df2 = pd.DataFrame({'C':np.arange(100),'D':np.cos(np.arange(100))})

# 创建画布
p = figure(plot_width=600, plot_height=400)
p.multi_line([df1['A'], df2['C']], [df1['B'], df2['D']],   # 注意x，y值的设置 → [x1,x2,x3,..], [y1,y2,y3,...]
             color=["firebrick", "navy"],
             alpha=[0.8, 0.6],     # 可同时设置 → alpha = 0.6
             line_width=[2,3],     # 可同时设置 → line_width = 2
            )

# 显示
show(p)


''' 2-2、折线图 - 多线图 '''

# 创建x值
x = np.linspace(0.1, 5, 100)

# 创建画布
p = figure(title="log axis example", y_axis_type="log",y_range=(0.001, 10**22)) # y_axis_type设置坐标类型，默认线性

# line1
p.line(x, np.sqrt(x), legend="y=sqrt(x)", line_color="tomato", line_dash="dotdash")

# line2，折线图+散点图
p.line(x, x, legend="y=x")
p.circle(x, x, legend="y=x")

# line3
p.line(x, x**2, legend="y=x**2")
p.circle(x, x**2, legend="y=x**2",fill_color=None, line_color="olivedrab")

# line4
p.line(x, 10**x, legend="y=10^x",line_color="gold", line_width=2)

# line5
p.line(x, x**x, legend="y=x^x",line_dash="dotted", line_color="indigo", line_width=2)

# line6
p.line(x, 10**(x**2), legend="y=10^(x^2)",line_color="coral", line_dash="dashed", line_width=2)

# 设置图例及label
p.legend.location = "top_left"
p.xaxis.axis_label = 'Domain'
p.yaxis.axis_label = 'Values (log scale)'

# 显示
show(p)


''' 3、单维度面积图 '''

# 创建数据
s = pd.Series(np.random.randn(100).cumsum())
# 注意设定起始值和终点值为最低点
s.iloc[0] = 2
s.iloc[-1] = 5

# 创建画布
p = figure(plot_width=600, plot_height=400)

# 绘制面积图
# .patch将会把所有点连接成一个闭合面
p.patch(s.index, s.values,     # 设置x，y值
        line_width=1, line_alpha = 0.8, line_color = 'black',line_dash = [10,4],   # 线型基本设置
        fill_color = 'black',fill_alpha = 0.2)

# 绘制折点
p.circle(s.index, s.values,size = 5,color = 'red',alpha = 0.8)

# 显示
show(p)


''' 4、面积堆叠图 '''
from bokeh.palettes import brewer # 导入brewer模块

# 创建数据，20个点，10个类型
N = 20
cats = 10 
rng = np.random.RandomState(1)
df = pd.DataFrame(rng.randint(10, 100, size=(N, cats))).add_prefix('y')

df_top = df.cumsum(axis=1) # 每一个堆叠面积图的最高点
df_bottom = df_top.shift(axis=1).fillna({'y0': 0})[::-1]       # 每一个堆叠面积图的最低点，并反向

colors = brewer['Spectral'][df_stack.shape[1]]    # 根据变量数拆分颜色
x = np.hstack((df.index[::-1], df.index))         # 得到围合顺序的index，这里由于一列是20个元素，所以连接成面需要40个点

p = figure(x_range=(0, N-1), y_range=(0, 700))
p.patches([x] * df_stack.shape[1],                    # 得到10组index
          [df_stack[c].values for c in df_stack],     # c为df_stack的列名，这里得到10组对应的valyes
          color=colors, alpha=0.8, line_color=None)   # 设置其他参数

show(p)