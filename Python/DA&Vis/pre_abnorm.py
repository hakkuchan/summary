""" 异常值分析：
    1. 3σ判别法
    2. 四分位数判别法 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

''' 1. 3σ判别法：假定数据服从正态分布，异常值为与平均值偏差超过3倍标准差的值 '''
# Toy data
data = pd.Series(np.random.randn(10000)*100)
# 计算统计量
ave = data.mean()  # 计算均值
std = data.std()   # 计算标准差
print('均值为：%.3f \n标准差为：%.3f' % (ave,std))
# 筛选
abnormal = data[np.abs(data - ave) > 3*std]   # 筛选出异常值
normal = data[np.abs(data - ave) <= 3*std]    # 筛选出非异常值
print(f'异常值共 {len(abnormal)} 个')
# 可视化数据分布
plt.scatter(normal.index, normal, color='k', marker='.', alpha = 0.3)
plt.scatter(abnormal.index, abnormal, color='r', marker='.', alpha = 0.5)
plt.xlim([-10,10010])
plt.grid()
plt.show()


''' 2. 四分位数判别法:

    · 原理：  
      四分位数是指把所有数值由小到大排列并分成四等份，
      三个分割点分别是：1/4位数、中位数、3/4位数
      分位差定义为：3/4位数 - 1/4位数
      
      合理值下限 = 1/4位数 - 1.5 * 分位差
      合理值上限 = 3/4位数 + 1.5 * 分位差
      
      异常值：低于下限或高于上限的值定义为
      
    · 四分位数判别法 比 3σ判别法 更严格
'''
# Toy data
data = pd.Series(np.random.randn(10000)*100)
# 计算统计量
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

# 四分位分析箱型图 '''
fig = plt.figure(figsize = (10,6))
ax1 = fig.add_subplot(2,1,1)
data.plot.box(vert=False, grid=True, ax = ax1)
plt.show()

# 可视化数据分布 '''
ax2 = fig.add_subplot(2,1,2)
plt.scatter(normal.index,normal,color = 'k',marker='.',alpha = 0.3)
plt.scatter(abnormal.index,abnormal,color = 'r',marker='.',alpha = 0.5)
plt.xlim([-10,10010])
plt.grid()
plt.show()