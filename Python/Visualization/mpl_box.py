import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline



""" 1. Dataframe直接绘制箱线图 """
# Toy data
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
# 生成画布
fig, axes = plt.subplots(2,1,figsize=(10,6))
# 箱线图配色要以字典形式传入
color = dict(boxes='Black',      # boxes → 箱线
             whiskers='DarkRed', # whiskers → 分位数与error bar横线之间竖线的颜色
             medians='Red',      # medians → 中位数线颜色
             caps='Blue')        # caps → error bar横线颜色
# 绘图 1
df.plot.box(ylim=[-0.2,1.2], # Y轴范围
            grid=False,      # 底纹
            color=color,     # 配色
            ax=axes[0])      # 子图 0
# 绘图 2
df.plot.box(vert=False,      # 是否垂直，默认True
            grid=True,       # 底纹
            color=color,     # 配色
            ax=axes[1])      # 子图 1
plt.show()



""" 2. bodplot()绘制箱线图 """
# Toy data
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
# 设置画布
plt.figure(figsize=(10,4))
f = df.boxplot(sym = 'o',    # 异常点形状，参考marker
               vert = True,  # 是否垂直
               whis = 1.5,   # IQR，默认1.5，也可以设置区间比如[5,95]，代表强制上下边缘为数据95%和5%位置
               patch_artist = True,              # 上下四分位框内是否填充，True为填充
               meanline = False,showmeans=True,  # 是否有均值线及其形状
               showbox = True,     # 是否显示箱线
               showcaps = True,    # 是否显示边缘线
               showfliers = True,  # 是否显示异常值
               notch = False,      # 中间箱体是否缺口
               return_type='dict'  # 返回类型为字典
              ) 
for box in f['boxes']:         # boxes, 箱线
    box.set( color='b', linewidth=1)        # 箱体边框颜色
    box.set( facecolor = 'b' ,alpha=0.5)    # 箱体内部填充颜色
for whisker in f['whiskers']:  # whiskers, 从box到error bar之间的竖线.
    whisker.set(color='k', linewidth=0.5,linestyle='-')
for cap in f['caps']:          # caps, error bar横线
    cap.set(color='gray', linewidth=2)
for median in f['medians']:    # medians, 中位值的横线,
    median.set(color='DarkBlue', linewidth=2)
for flier in f['fliers']:      # fliers, 异常值
    flier.set(marker='o', color='y', alpha=0.5)
plt.show()



""" 3. 分组绘制箱线图 """
df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])
df['Y'] = pd.Series(['A','B','A','B','A','B','A','B','A','B'])
df.boxplot(by = 'X')
df.boxplot(column=['Col1','Col2'],  # columns：按照数据的列分子图
           by=['X','Y'])            # by：按照列分组做箱型图
plt.show()