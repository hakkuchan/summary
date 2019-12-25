import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


""" 1. 分布类型：
    uniform:均匀分布 | binom:二项分布 | norm:正态分布   | poisson:泊松分布     
    beta:贝塔分布    | gamma:伽马分布 | cauchy:柯西分布 | laplace:拉普拉斯分布 | rayleigh:瑞利分布
    expon:指数分布   | lognorm:对数正态分布 | hypergeom：超几何分布 
    chi2:卡方分布    | f:F分布        | t:t分布
"""


""" 2. 通用方法（以norm为例） """
''' (1) rvs : 产生服从指定分布的随机数 '''
nums = stats.norm.rvs(loc=0,     # loc指定随机变量的偏移，此处对应的是正态分布的期望
                      scale=1,   # scale指定随机变量的缩放参数，此处对应的是正态分布的标准差
                      size=100)  # size指定随机变量的个数
print(num, '\n', type(nums))
''' (2) pdf : 概率密度函数 '''
print(stats.norm.pdf(x=1, loc=0, scale=1)) # 求概率密度函数指定点的函数值
print(stats.norm.pdf(np.arange(3),loc = 0,scale = 1))
''' (3) cdf : 累计分布函数 '''
print(stats.norm.cdf(0,loc=3,scale=1)) # 求累计分布函数指定点的函数值
print(stats.norm.cdf(np.arange(3),loc=3,scale=1))
print(stats.norm.cdf(0,0,1))
''' (4) sf : 残存函数（1-CDF）'''
print(stats.norm.sf(0,0,1))
''' (5) ppf : 分位点函数（CDF的逆） '''
print(stats.norm.ppf(0.5))
''' (6) isf : 逆残存函数（sf的逆） '''
print(stats.norm.isf(0.5))
''' (7) fit : 对一组随机取样进行拟合 '''
print(stats.norm.fit(stats.norm.rvs(0,1,10))) # 最大似然估计方法找出最适合取样数据的概率密度函数系数


""" 3. KS检验: 检验数据是否符合某种概率分布 """

''' 例 1 '''
data = [87,77,92,68,77,72,84,86,80,68,77,87,76,77,78,92,75,80,78,85] # 样本数据，20位健康男性在未进食之前的血糖浓度
df = pd.DataFrame(data, columns=['blood sugar'])
ave = df['blood sugar'].mean()  # 计算均值
std = df['blood sugar'].std()   # 计算标准差
s = stats.kstest(df['blood sugar'],  # 数据
                 'norm',             # 检查是否服从正态分布
                (ave, std))         # 输入均值和标准差
print(s[:])  # 返回两个结果：D值 和 P值（p值大于0.05，为正态分布）


''' 例2  检验指定的两个数列是否服从相同分布 '''
a = np.random.normal(7,9,1000)
b = np.random.normal(0,1,1000)
s = stats.ks_2samp(a, b)
print(s[:])