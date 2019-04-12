import numpy as np
import torch 
import torch.nn as nn

""" nd 和 ts 相互转换 """
# Creat ndarray data
data_nd = np.array([[1,2],[3,4],[5,6]]).astype('float')
# ndarray --> tensor
data_ts = torch.from_numpy(data_nd)
# tensor  --> ndarray
data_nd = data_ts.numpy()


""" 常用函数 """
# 行列数
print(data_ts.size())  # size(0): 行数，size(1) 列数
# 改变行列数
print(data_ts.view(-1,1))
# 索引，与numpy一样
print(data_ts[:, 1])
# 查数据类型
print(data_ts.type())
# 求平均值
print(data_ts.mean())
# 转化为标量(scalar)，仅对零维矩阵有效
print(torch.tensor([1.25]).item())


""" 自动求导机制 """

""" (1) require_grad 设置 """ 
# 将 ndarray 转化为 可导tensor：
x_nd = np.array([[1.0,2.0],[2.0,3.0]])
x = torch.tensor(x_nd, requires_grad=True)  # requires_grad = True,表示 x 可微分
# 将已有 tensor 转化为 可导tensor：
x = torch.tensor([[1.0,2.0],[2.0,3.0]])
x = x.clone().detach().requires_grad_(True)

""" (2) 自动求导实例 """

""" 例 1 """
# Create tensors.
x = torch.tensor(1., requires_grad=True)
w = torch.tensor(2., requires_grad=True)
b = torch.tensor(3., requires_grad=True)
# Build a computational graph.
y = w * x + b
# Compute gradients.
y.backward()
# Print out the gradients.
print(x.grad)    # 求 dy/dx，此时 w, b 是常数
print(w.grad)    # 求 dy/dw，此时 x, b 是常数
print(b.grad)    # 求 dy/db，此时 w, b 是常数

""" 例 2 """
# Create tensors.
x = torch.tensor(x_nd, requires_grad=True)
# Build a computational graph.
y = x ** 3
# Compute gradients.
y.backward(torch.ones_like(y))  # 求 dy/dx，注意 torch.ones_like(y) 的作用
# print out the gradients.
print(x.grad)

""" 例 3 """
# Create tensors of shape (10, 3) and (10, 2).
x = torch.randn(10, 3)
y = torch.randn(10, 2)
# Build a fully connected layer.
linear = nn.Linear(3, 2)
print ('w: ', linear.weight)
print ('b: ', linear.bias)
# Build loss function and optimizer.
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.01)
# Forward pass.
pred = linear(x)
# Compute loss.
loss = criterion(pred, y)
print('loss: ', loss.item())
# Backward pass.
loss.backward() # loss 函数对 w,b 求导
# Print out the gradients.
print ('dLoss/dw: ', linear.weight.grad) 
print ('dLoss/db: ', linear.bias.grad)
# 1-step gradient descent.
optimizer.step()
# Print out the loss after 1-step gradient descent.
pred = linear(x)
loss = criterion(pred, y)
print('loss after 1 step optimization: ', loss.item())