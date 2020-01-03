import numpy as np
import torch 
import torch.nn as nn


""" 自动求导 """

''' 例 1 '''
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

''' 例 2 '''
# Create tensors.
x_nd = np.array([[1.0,2.0],[2.0,3.0]])
x = torch.tensor(x_nd, requires_grad=True)
# Build a computational graph.
y = x ** 3
# Compute gradients.
y.backward(torch.ones_like(y))  # 求 dy/dx，注意 torch.ones_like(y) 的作用见 pytorch自动求导机制.pdf
# show the gradients.
print(x.grad)

''' 例 3 '''
# Create tensors of shape (10, 3) and (10, 2)
x = torch.randn(10, 3)
y = torch.randn(10, 2)
# Build a fully connected layer
linear = nn.Linear(3, 2)
print ('w: ', linear.weight)
print ('b: ', linear.bias)
# Build loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.01)
# Forward pass
pred = linear(x)
# Compute loss
loss = criterion(pred, y)
print('loss: ', loss.item())
# Backward pass
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