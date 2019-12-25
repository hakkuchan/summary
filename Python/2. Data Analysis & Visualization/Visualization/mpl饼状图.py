import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

""" 饼图 plt.pie() """
s = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
plt.axis('equal')  # 保证长宽相等
plt.pie(s,
        explode = [0.1,0.1,0,0],      # explode：指定每部分的偏移量
        labels = s.index,             # labels：标签
        colors=['r', 'g', 'b', 'c'],  # colors：颜色
        autopct='%.2f%%',             # autopct：饼图上的数据标签显示方式
        pctdistance=0.6,              # pctdistance：每个饼切片的中心和通过autopct生成的文本开始之间的比例
        labeldistance = 1.2,          # labeldistance：被画饼标记的直径,默认值：1.1
        shadow = True,                # shadow：阴影
        startangle=0,                 # startangle：开始角度
        radius=2,                     # radius：半径
        frame=False,                  # frame：图框
        counterclock=False)           # counterclock：指定指针方向，顺时针或者逆时针
print(s)