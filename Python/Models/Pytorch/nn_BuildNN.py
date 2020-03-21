""" 搭建ANN
    
    · Pytorch中搭建的ANN，其本质依然是"类"
      (1) 继承基类 nn.Module，并调用构造函数 super(类名, self).__init__()
      (2) 在初始化函数(__init__)中组合不同的层，以实现ANN的运算
      (3) 利用forward()函数定义前向传播过程;
      (4) 无需定义反向传播过程，nn.Module能够自动检测网络参数，并实现反向传播更新参数
      
    · 目录
    |
    |—— 1. Sequential
    |   |
    |   |—— 1.1 容器
    |   |
    |   |—— 1.2 搭建ANN
    |
    |—— 2. 顺序添加法 (不推荐)
    |
    |—— 3. 参数初始化
"""


import torch
from torch import nn
import torch.nn.functional as F

""" 1. Sequential """

''' 1.1 容器 (Sequential可以理解为一个容器，里面依次列出层，依序执行) '''
# Toy data：3个样本，4个特征
X = torch.randn(3, 4)
# 实例化 nn.Sequential，直接在其中添加层
layer = nn.Sequential(nn.Linear(4, 3),    # 对 X 进行线性变换
                      nn.BatchNorm1d(3),  # 对上一步输出结果进行批标准化
                      nn.Linear(3, 1),    # 对上一步输出结果进行线性变换
                      nn.Sigmoid())       # 对上一步输出结果进行激活函数转换
# 计算
y = layer(X)
print(y.detach())


''' 1.2 搭建ANN '''
class MLP(nn.Module): # 搭建一个多层感知机
    # 定义ANN结构
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(MLP, self).__init__()
        # 方式 1：直接在 Sequential 中添加层
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden_1),
                                    nn.BatchNorm1d(n_hidden_1),
                                    nn.ReLU(True))
        # 方式 2：利用 add_module 在 Sequential 中添加层 
        # (注：方式 1 和 2 基本等价，不同处为方式 2 可以给特定层命名)
        self.layer2 = nn.Sequential()
        self.layer2.add_module('linear_2', nn.Linear(n_hidden_1, n_hidden_2))
        self.layer2.add_module('batchnorm_2', nn.BatchNorm1d(n_hidden_2))
        self.layer2.add_module('relu_3', nn.ReLU(True))
        # 方式 1 和 2 效果等价，
        self.layer3 = nn.Sequential(nn.Linear(n_hidden_2, out_dim))
    # 定义前向传播过程
    def forward(self, x):
        x = layer1(x)
        x = layer2(x)
        x = layer3(x)
        return x

model = MLP(10, 20, 10, 1) # 输入10个特征，第一隐藏层有20个神经元，第二隐藏层有10个神经元，输出维度为1
print('Parameters of hidden layer 1:\n', model.layer1)
print('Parameters of linear_2:\n', model.layer2.linear_2)



""" 2. 顺序添加法 (在构造函数中列出所需层，然后定义层间的运算) """
class MLP(nn.Module):
    # 定义ANN结构
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(MLP, self).__init__()
        # Layer 1
        self.linear_1 = nn.Linear(in_dim, n_hidden_1)
        self.batchnorm_1 = nn.BatchNorm1d(n_hidden_1)
        # Layer 2
        self.linear_2 = nn.Linear(n_hidden_1, n_hidden_2)
        self.batchnorm_2 = nn.BatchNorm1d(n_hidden_2)
        # Layer 3
        self.linear_3 = nn.Linear(n_hidden_2, out_dim)
    # 定义前向传播过程
    def forward(self, x):
        # Layer 1
        x = self.linear_1(x)
        x = self.batchnorm_1(x)
        x = F.relu(x)
        # Layer 2
        x = self.linear_2(x)
        x = self.batchnorm_2(x)
        x = F.relu(x)
        # Layer 3
        x = self.linear_3(x)
        return x

model = MLP(10, 20, 10, 1)
print('Parameters of linear_1:\n', model.linear_1)



""" 3. 参数初始化 """
# 定义参数初始化函数，该函数用于把特定层参数初始化为特定值
def init_param(m):
    if type(m) == nn.Linear: # 若层为 nn.Linear (如果改为 nn.Conv2d，可发现 Linear层的参数不会被修改)
        torch.nn.init.constant_(m.weight,2) # 把权重设为 2
        m.bias.data.fill_(1) # 把偏置项设为 1

# 定义ANN
class MLP(nn.Module):
    def __init__(self, in_dim, n_hidden, out_dim):
        super(MLP, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden),
                                    nn.BatchNorm1d(n_hidden),
                                    nn.ReLU(True))
        self.layer2 = nn.Linear(n_hidden, out_dim)
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        return x

# 实例化MLP
model = MLP(4,10,1) # 输入值 4个特征，一层隐藏层(10个神经元)，输出值维度为 1

# 调用参数初始化函数
model.apply(init_param) 

# 查看参数
param = model.state_dict()
print(param['layer1.0.weight'])
print(param['layer1.0.bias'])
print(param['layer2.weight'])
print(param['layer2.bias'])
