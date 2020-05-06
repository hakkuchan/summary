""" 层概述
    
    · Pytorch中，神经网络可由层搭建而得
      层的功能类似于函数：定义对输入数据进行的运算，并返回输出结果（前向传播过程）
      但不同于普通的函数，层的参数可被优化（反向传播过程）
    
    · 本章先自定义一个线性层，以帮助理解层的本质；
      然后讨论常见内置层的参数初始化方法；
      内置层的主要知识见后
      
    · 目录
    |
    |—— 1. 自定义层
    |
    |—— 2. 参数初始化
"""


import torch
import torch.nn as nn


""" 1. 自定义层
    
    · 注意事项：
      (1) 层的数据类型为"类"，自定义层时需先继承基类 nn.Module
      (2) 在初始化函数 __init__ 中定义层涉及的参数
      (3) 调用构造函数 super(类名, self).__init__()，
          初始化并封装层参数为 nn.Parameter ，使其可被自动检测和学习
      (4) forward() 函数实现自定义层的具体运算，即前向传播过程
      (5) 无需写反向传播函数，nn.Module 能够利用 autograd 自动实现反向传播
    
    · 下例定义了一个线性层(MyLinear)，
      在搭建 ANN 时，可直接用 MyLinear 代替之后介绍的 nn.Linear
      ANN 的性能可能会改变，是由于 MyLinear 和 nn.Linear 初始化参数的不同
"""
class MyLinear(nn.Module):  # 继承基类 nn.Module
    def __init__(self, in_dim, out_dim):  # 初始化函数(__init__)中定义层涉及的参数
        super(MyLinear, self).__init__()  # 调用构造函数 super(类名, self).__init__()
        self.weight = nn.Parameter(torch.ones(in_dim, out_dim)) # 初始化 weight 为 1，并封装为 nn.Parameter
        self.bias = nn.Parameter(torch.ones(out_dim))           # 初始化 bias 为 1，并封装为 nn.Parameter     
    def forward(self, x):
        # 定义前向传播运算
        y = x.mm(self.weight) + self.bias
        return y

# 实例化 MyLinear
layer = MyLinear(3, 1)
# 返回层参数
param = layer.state_dict()
# 计算
X = torch.tensor([[1.,2.,3.],[4.,5.,6.]])
y = layer(X)
print('Out:\n', y.detach().numpy())
print('Weight:', param['weight'].t().numpy())
print('Bias:', param['bias'].numpy())



""" 2. 参数初始化（以内置层 nn.Linear 为例）"""
# 初始化线性层
layer = nn.Linear(3,1, bias=True)
# 初始化参数：可选操作，因为调用内置层时会自动初始化
nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 2)
# 输出参数
print(layer.state_dict()) # 显示可学习的参数
print('Weights:', layer.weight.detach())
print('Bias:', layer.bias.detach())