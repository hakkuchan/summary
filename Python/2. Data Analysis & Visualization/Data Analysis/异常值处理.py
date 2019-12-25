import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


""" 异常值分析 """
'''
1. 3σ 判断法：
    假定数据服从正态分布，
    异常值被定义为与平均值的偏差超过3倍标准差的值 
    即：p(|x - μ| > 3σ) ≤ 0.003
'''

data = pd.Series(np.random.randn(10000)*100)
ave = data.mean()  # 计算均值
std = data.std()  # 计算标准差
print('均值为：%.3f \n标准差为：%.3f' % (ave,std))

abnormal = data[np.abs(data - ave) > 3*std]   # 筛选出异常值
normal = data[np.abs(data - ave) <= 3*std] # 筛查出非异常值
print(f'异常值共 {len(abnormal)} 个')

''' 散点图展示数据分布 '''
plt.scatter(normal.index, normal, color='k', marker='.', alpha = 0.3)
plt.scatter(abnormal.index, abnormal, color='r', marker='.', alpha = 0.5)
plt.xlim([-10,10010])
plt.grid()
plt.show()


''' 
2. 四分位数判断法（比3σ 判断法更严格）:
    四分位数是指把所有数值由小到大排列并分成四等份，
    处于三个分割点位置的数值,
    分别是：1/4位数、中位数、3/4位数
'''

s = data.describe()  # 获得 8 组基本统计量
print(s) # 包括：样本个数、平均值、标准差、最小值、1/4位数、中位数、3/4位数、最大值
q25 = s['25%']   # 1/4位
q75 = s['75%']   # 3/4位
dqr = q75 - q25  # 分位差
l_lim = q25 - 1.5 * dqr  # 低于下限 l_lim 被认为是异常值
h_lim = q75 + 1.5 * dqr  # 高于上限 h_lim 被认为是异常值
abnormal = data[(data < l_lim) | (data > h_lim)]
normal = data[(data >= l_lim) & (data <= h_lim)]
print(f'异常值共 {len(abnormal)} 个')

''' 用箱型图展示四分位分析 '''
fig = plt.figure(figsize = (10,6))
ax1 = fig.add_subplot(2,1,1)
data.plot.box(vert=False, grid=True, ax = ax1)
plt.show()

''' 散点图展示数据分布 '''
ax2 = fig.add_subplot(2,1,2)
plt.scatter(normal.index,normal,color = 'k',marker='.',alpha = 0.3)
plt.scatter(abnormal.index,abnormal,color = 'r',marker='.',alpha = 0.5)
plt.xlim([-10,10010])
plt.grid()
plt.show()