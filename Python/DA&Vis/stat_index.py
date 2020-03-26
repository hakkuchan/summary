import numpy as np
import pandas as pd

df = pd.DataFrame({'x':np.arange(10), 'y':np.arange(91,101), 'z':np.random.random(10)})
print(df.describe()) # 输出 8 个主要统计量：count, mean, std, min, 25%, 50%, 75%, max 
print(df.count())    # 统计非 NaN 值的数量
print(df.min())      # 最小值
print(df.max())      # 最大值
print(df.mean())     # 平均值
print(df.mean(skipna=False)) # skipna参数：是否忽略 NaN，默认True，如 False，有 NaN 的列统计结果仍为NaN
print(df.std())      # 标准差
print(df.var())      # 方差
print(df.skew())     # 偏度（数据的不对称程度）
print(df.kurt())     # 峰度（正态分布的数据的峰度值为 0；峰度值越显著偏离 0，数据越不服从正态分布。）
print(df.median())   # 中位数，50%分位数
print(df.quantile(q=0.75))   # 分位数，参数 q 确定位置
df = pd.DataFrame({'x':[1,2,3,3,4], 'y':[11,11,12,11,13], 'z':[22,12,22,11,22]})
print(df.mode())    # 众数
df = pd.DataFrame({'x':np.arange(10), 'y':np.arange(91,101), 'z':np.random.random(10)})
print(df.corr(method='pearson'))  # 求各个 x, y, z 两两之间的 pearson 相关系数
print(df.corr(method='kendall'))  # 求各个 x, y, z 两两之间的 kendall 相关系数
print(df.corr(method='pearson'))  # 求各个 x, y, z 两两之间的 spearman 相关系数