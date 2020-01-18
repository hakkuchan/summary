import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

sns.set_style("white") # 设置风格


""" 1、综合散点图 - jointplot() """

''' (1) 散点图 + 分布图 ''' 

rs = np.random.RandomState(2)
df = pd.DataFrame(rs.randn(100,2), columns = ['A','B'])

sns.jointplot(x=df['A'], y=df['B'], # 设置x, y轴，显示columns名称
              data=df,        # 设置数据
              color='b',      # 设置颜色
              s = 50,         # 设置散点大小
              edgecolor="w",  # 设置边缘线颜色及宽度
              linewidth=1,    # 设置边缘线宽度(只针对scatter）
              kind = 'scatter',
              space = 0.2,    # 设置散点图和布局图的间距
              height = 7,     # 图表大小（自动调整为正方形）
              ratio = 5,      # 散点图与布局图高度比，整型
              marginal_kws=dict(bins=15, rug=True))  # 设置柱状图箱数，是否设置rug
plt.show()


''' (2) 散点图 + 六边形分布图 '''

df = pd.DataFrame(rs.randn(500,2),columns = ['A','B'])

sns.jointplot(x=df['A'], y=df['B'],
              data = df, 
              kind="hex", 
              color="g",
              marginal_kws=dict(bins=20))
plt.show()


''' (3) 散点图 + 密度分布图 '''

rs = np.random.RandomState(15)
df = pd.DataFrame(rs.randn(300,2),columns = ['A','B'])

g = sns.jointplot(x=df['A'], y=df['B'],data = df,
                  kind="kde", color="k",
                  shade_lowest=False)

g.plot_joint(plt.scatter,c="w", s=30, linewidth=1, marker="+")
plt.show()


""" 2. 绘制的可拆分的散点图 """

''' (1) plot_joint() + ax_marg_x.hist() + ax_marg_y.hist() '''
# 设置风格
sns.set_style("white") 
# 导入数据
tips = sns.load_dataset("tips")
print(tips.head())
# 创建一个绘图表格区域，设置好x、y对应数据
g = sns.JointGrid(x="total_bill", y="tip", data=tips)

g.plot_joint(plt.scatter, color ='m', edgecolor = 'white')  # 设置框内图表，scatter

g.ax_marg_x.hist(tips["total_bill"], color="b", alpha=.6,
                 bins=np.arange(0, 60, 3))            # 设置x轴直方图，注意bins是数组
g.ax_marg_y.hist(tips["tip"], color="r", alpha=.6,
                 orientation="horizontal",
                 bins=np.arange(0, 12, 1))            # 设置x轴直方图，注意需要orientation参数
plt.grid(linestyle = '--')
plt.show()


''' (2) plot_joint() + plot_marginals() '''

# Case 1：
g = sns.JointGrid(x="total_bill", y="tip", data=tips) # 创建一个绘图表格区域，设置好x、y对应数据
g = g.plot_joint(plt.scatter,color="g", s=40, edgecolor="white")   # 绘制散点图
plt.grid(linestyle = '--')
g.plot_marginals(sns.distplot, kde=True, color="g")                # 绘制x，y轴直方图
plt.show()

# Case 2：
g = sns.JointGrid(x="total_bill", y="tip", data=tips)   # 创建一个绘图表格区域，设置好x、y对应数据
g = g.plot_joint(sns.kdeplot,cmap = 'Reds_r')           # 绘制密度图
plt.grid(linestyle = '--')
g.plot_marginals(sns.kdeplot, shade = True, color="r")  # 绘制x，y轴密度图
plt.show()