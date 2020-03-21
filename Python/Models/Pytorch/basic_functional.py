""" functional
    
    · 模块 nn.functional 中定义了很多函数，实现对输入数据的运算，并返回输出结果
      这些函数中的参数非 Parameter 类型，即它们不可被学习
"""

import numpy
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
%matplotlib inline

""" 1. 示例 """ 
# Toy data：2个样本，4个特征
X = torch.tensor([[1,2,-3,-4],[5,6,-7,-8]])
# 以relu函数为例
y = F.relu(X)
print(y)



""" 2. 激活函数 """

def pic(x, y, loc, label):
    # 绘图函数
    fig.add_subplot(loc[0], loc[1], loc[2])
    plt.plot(x.numpy(), y.numpy(),label=label)
    plt.legend(fontsize=12)
fig = plt.figure(figsize=(16,8))    

''' relu/ leaky_relu/ rrelu'''
x = torch.arange(-10,1,0.1).view(-1,1)
y = F.relu(x)
pic(x, y, (2,4,1), 'relu')
y = F.leaky_relu(x)
pic(x, y, (2,4,1), 'leaky_relu')
y = F.rrelu(x)
pic(x, y, (2,4,1), 'rrelu')

''' elu/ softplus'''
x = torch.arange(-5,5,0.1).view(-1,1)
y = F.elu(x)
pic(x, y, (2,4,2), 'elu')
y = F.softplus(x)
pic(x, y, (2,4,2), 'softplus')

''' tanh/ hardtanh/ softsign '''
x = torch.arange(-5,5,0.1).view(-1,1)
y = F.tanh(x)
pic(x, y, (2,4,3), 'tanh')
y = F.hardtanh(x)
pic(x, y, (2,4,3), 'hardtanh')
y = F.softsign(x)
pic(x, y, (2,4,3), 'softsign')

''' hardshrink/ tanhshrink/ tanhshrink '''
x = torch.arange(-3,3,0.1).view(-1,1)
y = F.hardshrink(x)
pic(x, y, (2,4,4), 'hardshrink')
y = F.tanhshrink(x)
pic(x, y, (2,4,4), 'tanhshrink')
y = F.softshrink(x)
pic(x, y, (2,4,4), 'tanhshrink')

''' sigmoid '''
x = torch.arange(-5,5,0.1).view(-1,1)
y = F.sigmoid(x)
pic(x, y, (2,4,5), 'sigmoid')

''' relu6 '''
x = torch.arange(-5,10,0.1).view(-1,1)
y = F.relu6(x)
pic(x, y, (2,4,6), 'relu6')

''' logsigmoid '''
x = torch.arange(-3,3,0.1).view(-1,1)
y = F.logsigmoid(x)
pic(x, y, (2,4,7), 'hardshrink')

''' hardshrink '''
x = torch.arange(-3,3,0.1).view(-1,1)
y = torch.nn.functional.threshold(x,threshold=1,value=5)
pic(x, y, (2,4,8), 'hardshrink')

plt.show()