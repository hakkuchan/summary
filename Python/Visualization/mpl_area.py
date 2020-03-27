import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

""" 面积图 """
fig,axes = plt.subplots(2,1,figsize = (8,6))
df1 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])

df1.plot.area(colormap = 'Greens_r',alpha = 0.5,ax = axes[0])
df2.plot.area(stacked=False,colormap = 'Set2',alpha = 0.5,ax = axes[1])
# 使用Series.plot.area()和DataFrame.plot.area()创建面积图
# stacked：是否堆叠，默认情况下，区域图被堆叠
# 为了产生堆积面积图，每列必须是正值或全部负值！
# 当数据有NaN时候，自动填充0，所以图标签需要清洗掉缺失值
plt.show()

""" 填充两个图之间的面积 """
fig,axes = plt.subplots(2,1,figsize = (8,6))
x = np.linspace(0, 1, 500)
y1 = np.sin(4 * np.pi * x) * np.exp(-5 * x)
y2 = -np.sin(4 * np.pi * x) * np.exp(-5 * x)
axes[0].fill(x, y1, 'r',alpha=0.5,label='y1')
axes[0].fill(x, y2, 'g',alpha=0.5,label='y2')
# 对函数与坐标轴之间的区域进行填充，使用fill函数
# 也可写成：plt.fill(x, y1, 'r',x, y2, 'g',alpha=0.5)

x = np.linspace(0, 5 * np.pi, 1000) 
y1 = np.sin(x)  
y2 = np.sin(2 * x)  
axes[1].fill_between(x, y1, y2, color ='b',alpha=0.5,label='area')  
# 填充两个函数之间的区域，使用fill_between函数

for i in range(2):
    axes[i].legend()
    axes[i].grid()
# 添加图例、格网