""" · 目录
    |
    |—— 1 ~ 5. 计数、平均值、标准差&方差、最小值&最大值、四分位数
    |
    |—— 6 ~ 10. 描述性统计、众数、相关性、偏度、峰度
"""

import numpy as np
import pandas as pd

# Toy data
df = pd.DataFrame({'X':(1,2,2,3), 'Y':(5,5,7,8)})

""" 1. 计数(排除NaN值) """
print(df.count())


""" 2. 平均值 """
print(df.mean())
print(df.mean(skipna=True)) # 跳过 Null值


""" 3. 标准差 & 方差 """
print(df.std())
print(df.var())


""" 4. 最小值 & 最大值 """
print(df.min())
print(df.max())


""" 5. 四分位数：把所有数值由小到大排列并分成四等份，处于三个分割点位置的数值
    
    · 25%位置上的数值：下四分位数
      50%位置上的数值：中位数
      75%位置上的数值：上四分位数
"""
print(df.quantile(q=0.25))   # 下分位数，25%分位数
print(df.median())           # 中位数，50%分位数
print(df.quantile(q=0.5))    # 中位数，50%分位数
print(df.quantile(q=0.75))   # 上分位数，75%分位数
# 注：q也可取其它值


""" 6. 描述性统计: count, mean, std, min, 25%(下分位数), 50%(中位数), 75%(上分位数), max """
print(df.describe())


""" 7. 众数 """
print(df.mode())


""" 8. 相关性 """
print(df.corr(method='pearson'))  # 求各个 X, Y 两两之间的 pearson 相关系数
print(df.corr(method='kendall'))  # 求各个 X, Y 两两之间的 kendall 相关系数
print(df.corr(method='pearson'))  # 求各个 X, Y 两两之间的 spearman 相关系数


""" 9. 偏度：分布对称的数据偏度为0，左侧拖尾时偏度<0，右侧拖尾时偏度>0 """
print(df.skew())


""" 10. 峰度：正态分布的峰度为0，峰度越偏离0，数据越不服从正态分布 """
print(df.kurt())