import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

''' 直方图 + 密度图 '''
s = pd.Series(np.random.randn(1000))
s.hist(bins=40,          # bins：箱子个数
       histtype = 'bar', # histtype 风格，bar，barstacked，step，stepfilled
       align = 'mid',     # align : {‘left’, ‘mid’, ‘right’}, optional(对齐方式)
       orientation = 'vertical',  # orientation 水平还是垂直{‘horizontal’, ‘vertical’}
       alpha=0.8, 
       density =True)
s.plot(kind='kde',style='k--') # 绘制密度图
plt.show()


""" 堆叠直方图 """
plt.figure(num=1)
df = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
                   'c': np.random.randn(1000) - 1, 'd': np.random.randn(1000)-2},
                   columns=['a', 'b', 'c','d'])
df.plot.hist(stacked=True, #是否堆叠
             bins=20,
             colormap='Greens_r',
             alpha=0.5,
             grid=True)
plt.show()

""" 生成多个直方图 """
df = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
                   'c': np.random.randn(1000) - 1, 'd': np.random.randn(1000)-2})
df.hist(bins=50)
plt.show()