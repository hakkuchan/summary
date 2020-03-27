import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

""" 简例: 柱状图 | 堆叠图 """

fig, axes = plt.subplots(4,1,figsize = (10,20))
 
''' 单系列柱状图方法一：plt.plot(kind='bar/barh') '''
s = pd.Series(np.random.randint(0,10,16), index=list('abcdefghijklmnop')) 
s.plot(kind='bar',color = 'k',grid = True,alpha = 0.5,ax = axes[0])  # ax参数 → 选择第几个子图

''' 多系列柱状图 '''
df = pd.DataFrame(np.random.rand(10,3), columns=['a','b','c'])
df.plot(kind='bar',ax = axes[1],grid = True,colormap='Reds_r')

''' 多系列堆叠图 '''
df = pd.DataFrame(np.random.rand(10,3), columns=['a','b','c'])
df.plot(kind='bar',ax = axes[2],grid = True, colormap='Blues_r', stacked=True) 

df = pd.DataFrame(np.random.rand(10,3), columns=['a','b','c'])
df.plot(kind='barh',ax = axes[3],grid = True, colormap='Blues_r', stacked=True) 

plt.show()

""" 柱状图 plt.bar()详细设置 """
np.random.seed(1)
plt.figure(figsize=(10,4))
x = np.arange(10)
y1 = np.random.rand(10)
y2 = -np.random.rand(10)

plt.bar(x,y1,width = 1,
        facecolor = 'yellowgreen', # facecolor柱状图里填充的颜色
        edgecolor = 'white',       # edgecolor是边框的颜色
        yerr = y1*0.1)             # 误差棒
plt.bar(x,y2,width = 1,facecolor = 'lightskyblue',edgecolor = 'white',yerr = y2*0.1)

for i,j in zip(x,y1):
    plt.text(i-0.1,j-0.15,'%.2f' % j, color = 'white')
for i,j in zip(x,y2):
    plt.text(i+0.3,j+0.05,'%.2f' % -j, color = 'white')
# 给图添加text
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
plt.show()