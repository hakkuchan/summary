import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

""" 1. 直方图 + 密度图 """
s = pd.Series(np.random.randn(1000))
s.hist(bins=40,                   # 箱子个数
       histtype = 'bar',          # 风格：bar，barstacked，step，stepfilled
       align = 'mid',             # 对齐方式：left, mid, right
       orientation = 'vertical',  # 水平还是垂直 horizontal, vertical
       alpha=1, # 透明度 (1为实色)
       density=True)
s.plot(kind='kde',style='k--') # 绘制密度图
plt.show()


""" 2. 堆叠直方图 """
plt.figure(num=1)
df = pd.DataFrame({'a': np.random.randn(1000), 'b': np.random.randn(1000)+1, 
                   'c': np.random.randn(1000)+2}, columns=['a', 'b', 'c',''])
df.plot.hist(stacked=True, bins=40, colormap='Blues_r', alpha=1, grid=True) # stacked设置堆叠
plt.show()


""" 多个直方图 """
df = pd.DataFrame({'a': np.random.randn(1000)-10, 'b': np.random.randn(1000)-5,
                   'c': np.random.randn(1000)+5, 'd': np.random.randn(1000)+10})
df.hist(bins=50)
plt.show()