""" autograd(自动求导) 可对 tensors(条件：requires_gard = True) 上的操作提供自动求导 """


import torch

''' 例 1：标量求导 '''
# 生成 tensors
x = torch.tensor(1., requires_grad=True)
w = torch.tensor(2., requires_grad=True)
b = torch.tensor(3., requires_grad=True)
# 构建运算
y = w * x + b
# backward()方法：计算 y 的导数
y.backward()
# grad属性：记录导数
print(x.grad)    # dy/dx，此时 w, b 是常数
print(w.grad)    # dy/dw，此时 x, b 是常数
print(b.grad)    # dy/db，此时 w, b 是常数


''' 例 2：矩阵求导 '''
# 生成 tensors
x = torch.tensor([[1.,2.],[3.,4.]], requires_grad=True)
# 构建矩阵运算
y = x ** 3
print('y:\n', y)
# 计算每个位置的导数
y.backward(torch.ones_like(y))  # 求 dy/dx (torch.ones_like(y) 用途见《pytorch自动求导机制.pdf》)
# 输出导数
print('dy/dx:\n', x.grad)