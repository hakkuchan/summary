""" 综合实例 —— 线性回归的实现

    · 本篇试图利用前几篇 (层, Loss, optimizer) 的内容训练线性回归模型，目的是帮助理解这些内容
      由于训练线性回归模型和训练ANN没有本质区别，本篇既是基础部分的回顾，也是ANN部分的入门
"""

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
%matplotlib inline

''' 例 1：训练细节 '''
# Toy data
X = torch.randn(10, 5) # 10个样本，5个特征
y = torch.randn(10, 1)
# 构建linear层
linear = nn.Linear(5, 1) # 输入维度 5，输出维度 1
print('Initialized w, b:', linear.weight.detach(), linear.bias.detach())
# 构建 损失函数 和 优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.001)
# 向前传播：计算 y
y_pred = linear(X)
# 计算损失
loss = criterion(y_pred, y)
print('Loss =', loss.item())
# 向后传播：即loss函数对 w,b 求导
loss.backward()
print ('d(Loss)/dw =', linear.weight.grad) 
print ('d(Loss)/db =', linear.bias.grad)
# 基于计算所得 gradients 进行一次优化
optimizer.step()
# 计算一次优化后的损失函数
y_pred = linear(X)
loss = criterion(y_pred, y)
print('Loss =', loss.item())


''' 例 2：线性回归 '''
# Toy data
X = torch.arange(0,20,0.5).view(-1,1)
y = 3 * X + torch.randn_like(X)
# 构建 Linear 层
linear = nn.Linear(1,1)
# 构建损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.001)
# 训练20次
for epoch in range(20):
    # 向前传播：计算预测值和损失函数
    y_pred = linear(X)
    loss = criterion(y_pred, y)
    # 向后传播：计算损失函数对模型参数的梯度，并基于梯度优化参数
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    # 输出进度和损失函数值
    if (epoch+1) % 5 == 0:
        print (f'Epoch [{epoch+1}/20], Loss: {loss.item():.4f}')
# 绘图 (X轴：真实 y值，Y轴：预测 y值)
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(1,1,1)
X.view(1,-1).numpy()[0]
ax.scatter(y.view(1,-1).numpy()[0], y_pred.view(1,-1).detach().numpy()[0])
plt.show()