import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

sns.set_style("white") # 设置风格


""" 1. 矩阵散点图 - pairplot() """

iris = sns.load_dataset("iris")
print(iris.head()) # 读取数据

sns.pairplot(iris,
            kind = 'scatter',  # 散点图/回归分布图 {‘scatter’, ‘reg’}  
            diag_kind="hist",  # 直方图/密度图 {‘hist’, ‘kde’}
            hue="species",   # 按照某一字段进行分类
            palette="husl",  # 设置调色板
            markers=["o", "s", "D"],  # 设置不同系列的点样式（这里根据参考分类个数）
            height = 2,   # 图表大小
            )
plt.show()

''' (1) 只提取局部变量进行对比 '''

sns.pairplot(iris,vars=["sepal_width", "sepal_length"],
             kind = 'reg', diag_kind="kde", 
             hue="species", palette="husl")
plt.show()


''' (2) 其它设置 '''
sns.pairplot(iris, diag_kind="kde", markers="+",
             plot_kws=dict(s=50, edgecolor="b", linewidth=1),
             # 设置点样式
             diag_kws=dict(shade=True)
             # 设置密度图样式
            )
plt.show()



""" 2、可拆分绘制的矩阵散点图 - PairGrid() """

''' (1) 方法一：map_diag() + map_offdiag() ''' 

# 创建一个绘图表格区域，设置好x、y对应数据，按照species分类
g = sns.PairGrid(iris,hue="species",
                 palette = 'hls',
                 vars = ['sepal_length','sepal_width','petal_length','petal_width'],  # 可筛选
                 )

# 对角线图表，plt.hist/sns.kdeplot
g.map_diag(plt.hist, 
           histtype = 'barstacked',   # 可选：'bar', 'barstacked', 'step', 'stepfilled'
           linewidth = 1, edgecolor = 'w')           


# 其他图表，plt.scatter/plt.bar
g.map_offdiag(plt.scatter,
              edgecolor="w",s=40, linewidth = 1)    # 设置点颜色、大小、描边宽度
g.add_legend()
plt.show()


''' (2) 方法二：map_diag() + map_upper() + map_lower() '''
# 可拆分绘制的散点图
# map_diag() + map_lower() + map_upper()

g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot, lw=3)   # 设置对角线图表
g.map_upper(plt.scatter, color = 'r')     # 设置对角线上端图表
g.map_lower(sns.kdeplot, cmap="Blues_d")      # 设置对角线下端图表
plt.show()