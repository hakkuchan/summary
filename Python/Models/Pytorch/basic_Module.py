""" · nn.Module 是 Pytorch 中的一个重要基类，用于定义层及神经网络(神经网络由层搭建而得)
    
    · 层及神经网络的功能类似于函数：定义输入数据的计算流程，并返回输出结果（前向传播过程）
      但不同于普通函数，层及神经网络的参数可被自动优化（反向传播过程）
    
    · 为帮助理解 nn.Module，下例定义了一个线性层 (MyLinear)，
      MyLinear 的效果与内置线性层 nn.Linear 的效果基本相同
"""

import torch
import torch.nn as nn

# Step 1: 创建 Mylinear类，并继承基类 nn.Module
class MyLinear(nn.Module):
    # Step 2: 初始化函数：引入涉及的参数
    def __init__(self, in_dim, out_dim):  
        # Step 3: 调用构造函数 super(类名, self).__init__()，初始化并封装层参数为 nn.Parameter ，使其可被自动检测和学习
        super(MyLinear, self).__init__()  
        self.weight = nn.Parameter(torch.ones(in_dim, out_dim)) # 初始化 weight 为 1，并封装为 nn.Parameter
        self.bias = nn.Parameter(torch.ones(out_dim))           # 初始化 bias 为 1，并封装为 nn.Parameter         
    # Step 4: 定义层的具体运算，即前向传播过程
    def forward(self, x):
        y = x.mm(self.weight) + self.bias
        return y

# 实例化 MyLinear
layer = MyLinear(3, 1)
# 计算
X = torch.tensor([[1.,2.,3.],[4.,5.,6.]])
y = layer(X)
print('Out:\n', y.detach().numpy())
# 返回层参数
param = layer.state_dict()
print('Weight:\n', param['weight'].t().numpy())
print('Bias:\n', param['bias'].numpy())