import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" 三种魔法语句 (切换时，需要重启 .ipynb 文件) """

''' 直接在notebook中显示，不可交互 '''
# %matplotlib inline
''' 直接在notebook中显示，可交互 '''
%matplotlib notebook
''' 弹出一个控制页面，可交互 '''
# %matplotlib qt5

x, y = np.random.randn(300), np.random.randn(300)
plt.scatter(x,y)
# plt.show() # 建议当 %matplotlib inline 时写这句，另外两种魔法语句下不要写