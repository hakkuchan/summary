""" 连续数据离散化：
    · 目的：连续数据变换成分类属性
    · 方法：把连续数据的取值范围划分为离散化的区间，再用不同符号代表每个子区间
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ages = [20,22,25,27,21,23,37,31,61,45,41,32] # 一组人员年龄数据 (也可以是 df['ages'])
bins = [18,25,35,60,100]        # 上述数据将划分为“18到25”,“26到35”,“36到60”,“60以上”
cats = pd.cut(ages, bins)
print(cats.codes)               # 0-3对应分组后的四个区间，用代号来注释数据对应区间
print(pd.value_counts(cats))    # 按照区间计数
print(pd.cut(ages,[18,26,36,61,100],right=False)) # 通过right函数修改闭端，默认为True
group_names=['Youth','YoungAdult','MiddleAged','Senior']
print(pd.cut(ages, bins, labels=group_names))     # 可以设置自己的区间名称，用labels参数