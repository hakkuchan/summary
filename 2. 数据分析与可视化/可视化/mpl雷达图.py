import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

""" 雷达图1（首尾不闭合） """

plt.figure(figsize=(10,5))

ax1= plt.subplot(111, projection='polar') # 设置极坐标
ax1.set_title('radar map\n')  # 创建标题
ax1.set_rlim(0,12)

# 创建数据
data1 = np.random.randint(1,10,10)
data2 = np.random.randint(1,10,10)
data3 = np.random.randint(1,10,10)
theta=np.arange(0,2*np.pi,2*np.pi/10)

# 绘制雷达线
ax1.plot(theta,data1,'.--',label='data1')
ax1.fill(theta,data1,alpha=0.2)
ax1.plot(theta,data2,'.--',label='data2')
ax1.fill(theta,data2,alpha=0.2)
ax1.plot(theta,data3,'.--',label='data3')
ax1.fill(theta,data3,alpha=0.2)

plt.show()


""" 雷达图2（首尾闭合） """
labels = np.array(['a','b','c','d','e','f']) # 标签
dataLenth = 6 # 数据长度
data1 = np.random.randint(0,10,6) 
data2 = np.random.randint(0,10,6) # 数据

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False) # 分割圆周长
data1 = np.concatenate((data1, [data1[0]])) # 闭合
data2 = np.concatenate((data2, [data2[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

plt.polar(angles, data1, 'o-', linewidth=1) #做极坐标系
plt.fill(angles, data1, alpha=0.25)# 填充
plt.polar(angles, data2, 'o-', linewidth=1) #做极坐标系
plt.fill(angles, data2, alpha=0.25)# 填充

plt.thetagrids(angles * 180/np.pi, labels) # 设置网格、标签
plt.ylim(0,10)  # polar的极值设置为ylim

plt.show()