""" 饼图 plt.pie() """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.Series(3 * np.random.rand(4), index=['a','b','c','d'], name='series')
plt.axis('equal')  # 保证长宽相等
plt.pie(data, # 数据
        explode = [0.2,0,0.2,0],      # 指定每部分的偏移量
        labels = s.index,             # 标签
        colors=['r','g','b','c'],     # 颜色
        autopct='%.2f%%',             # 饼图上的数据标签显示方式
        pctdistance=0.5,              # 百分比与中心的距离
        labeldistance=0.7,            # 标签与中心的距离
        shadow=False,                 # 是否显示阴影
        startangle=90,                # 起始角度
        radius=2,                     # 半径
        frame=False,                  # 图框
        counterclock=False)           # 指定指针方向，True为逆时针，False为顺时针
plt.show()
print(data)