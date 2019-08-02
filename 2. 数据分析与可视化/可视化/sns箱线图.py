import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set_style("whitegrid")

tips = sns.load_dataset("tips")
print(tips.head())

""" 方式一： """
sns.boxplot(x="day", y="total_bill", data=tips,
            linewidth = 2,   # 线宽
            width = 0.8,     # 箱之间的间隔比例
            fliersize = 3,   # 异常点大小
            palette = 'hls', # 设置调色板
            whis = 1.5,      # 设置IQR 
            notch = True,    # 设置是否以中值做凹槽
            order = ['Thur','Fri','Sat','Sun'],  # 筛选类别
           )
plt.show()


""" 方式二 """
sns.boxplot(x="day", y="total_bill", data=tips, hue = 'smoker', palette = 'Reds')
plt.show()