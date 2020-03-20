""" class torch.nn.Functional """

# nn.Functional定义了很多函数
# 需要注意，这些函数中的参数是不能被优化的

# 示例：
import torch
import torch.nn.functional as F

# 输入 10 个样本，每个样本有 4 个特征
X = torch.randn(3, 4)

# 输出结果
y = F.relu(X)   # 以relu函数为例
print(X,'\n',y)


import numpy as np
import torch
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline


fig = plt.figure(figsize=(15,8))

''' relu '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.relu(x)
fig.add_subplot(2,4,1)
plt.plot(x.numpy(),y.numpy(),label='relu')
plt.legend(fontsize=12)

''' leaky_relu '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.leaky_relu(x,negative_slope=0.1)
fig.add_subplot(2,4,1)
plt.plot(x.numpy(),y.numpy(),label='leaky_relu')
plt.text(-9.5, 3, 'leaky_relu:\nneg slope=0.1', fontdict={'size':12, 'color':'red'})
plt.legend(fontsize=12)

''' rrelu '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.rrelu(x,lower=0.15, upper=0.5)
fig.add_subplot(2,4,1)
plt.plot(x.numpy(),y.numpy(),label='rrelu')
plt.text(1, -2, 'rrelu:\nlower=0.15\nupper=0.5', fontdict={'size':12, 'color':'red'})
plt.legend(fontsize=12)

''' elu '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.elu(x)
fig.add_subplot(2,4,2)
plt.plot(x.numpy(),y.numpy(),label='elu')
plt.legend(fontsize=12)

''' softplus '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.softplus(x)
fig.add_subplot(2,4,2)
plt.plot(x.numpy(),y.numpy(),label='softplus')
plt.legend(fontsize=12)

''' sigmoid '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.sigmoid(x)
fig.add_subplot(2,4,3)
plt.plot(x.numpy(),y.numpy(),label='sigmoid')
plt.legend(fontsize=12)

''' tanh '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.tanh(x)
fig.add_subplot(2,4,3)
plt.plot(x.numpy(),y.numpy(),label='tanh')
plt.legend(fontsize=12)

''' softsign '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.softsign(x)
fig.add_subplot(2,4,3)
plt.plot(x.numpy(),y.numpy(),label='softsign')
plt.legend(fontsize=12)

''' hardtanh '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.hardtanh(x)
fig.add_subplot(2,4,4)
plt.plot(x.numpy(),y.numpy(),label='hardtanh')
plt.legend(fontsize=12)

''' relu6 '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.relu6(x)
fig.add_subplot(2,4,4)
plt.plot(x.numpy(),y.numpy(),label='relu6')
plt.legend(fontsize=12)

''' hardshrink '''
x = torch.from_numpy(np.arange(-2,2,0.1)).view(-1,1)
y = torch.nn.functional.hardshrink(x)
fig.add_subplot(2,4,5)
plt.plot(x.numpy(),y.numpy(),label='hardshrink')
plt.legend(fontsize=12)

''' tanhshrink '''
x = torch.from_numpy(np.arange(-2,2,0.1)).view(-1,1)
y = torch.nn.functional.tanhshrink(x)
fig.add_subplot(2,4,5)
plt.plot(x.numpy(),y.numpy(),label='tanhshrink')
plt.legend(fontsize=12)

''' softshrink '''
x = torch.from_numpy(np.arange(-2,2,0.1)).view(-1,1)
y = torch.nn.functional.softshrink(x)
fig.add_subplot(2,4,5)
plt.plot(x.numpy(),y.numpy(),label='softplus')
plt.legend(fontsize=12)

''' logsigmoid '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.logsigmoid(x)
fig.add_subplot(2,4,6)
plt.plot(x.numpy(),y.numpy(),label='logsigmoid')
plt.legend(fontsize=12)

''' threshold '''
x = torch.from_numpy(np.arange(-10,10,0.1)).view(-1,1)
y = torch.nn.functional.threshold(x,threshold=2,value=5)
fig.add_subplot(2,4,7)
plt.plot(x.numpy(),y.numpy(),label='threshold')
plt.text(-7, 6, 'value=5\nthreshold=2', fontdict={'size': 12, 'color': 'red'})
plt.legend(fontsize=12)

plt.show()