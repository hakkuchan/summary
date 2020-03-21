""" 层
    
    · Pytorch中，神经网络可由层搭建而得
      层的功能类似于 Python 中的函数：层定义了对输入数据进行的运算，并返回输出结果（前向传播过程）
      但不同于普通的函数，层中的参数可被优化（反向传播过程）
    
    · 本章将先自定义一个线性层，以帮助理解层的本质
      
    · 目录
    |
    |—— 1. 自定义层
    |
    |—— 2. Linear & 参数初始化
    |
    |—— 3. 激活函数层
    |
    |—— 4. BatchNorm1d / BatchNorm2d/ BatchNorm3d
    |
    |—— 5. Conv1d / Conv2d / Conv3d
    |
    |—— 6. Maxpool1d / Maxpool2d / Maxpool3d
"""

import torch
import torch.nn as nn

""" 1. 自定义层
    
    · 注意事项：
      (1) 层的数据结构为"类"，自定义层时需先继承基类 nn.Module
      (2) 在初始化函数(__init__)中定义层涉及的参数，并调用构造函数 super(类名, self).__init__()
          把需要学习的参数封装成 nn.Parameter，使参数能够被自动检测和学习
      (3) forward()函数实现自定义层的具体运算 (前向传播过程);
      (4) 无需写反向传播函数，nn.Module能够利用autograd自动实现反向传播。
    
    · 下例会自定义一个线性层(MyLinear)，
      在搭建ANN时，可直接用 MyLinear 代替之后介绍的 nn.Linear 
      ANN预测性能可能会因此改变，是由于 MyLinear 的初始化参数与 nn.Linear 的不同 
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
# 返回模型参数
param = layer.state_dict()
# 计算
out = layer(torch.tensor([[1.,2.,3.],[4.,5.,6.]]))
print('Out:\n', out.detach().numpy())
print('Weight:', param['weight'].t().numpy())
print('Bias:', param['bias'].numpy())


""" 2. Linear & 参数初始化

    · torch.nn.Linear 实现数据的线性转化：y = AX + b
    · 完整形式：nn.Linear(in_features, out_features, bias=True)
      (1) in_features: 输入样本的维度，比如输入样本有3个特征，infeatures=3
      (2) out_features: 输出样本的维度，比如输出10个值，则 out_features=10
      (3) bias：设定是否需要偏置项
"""
# Toy data: 2个样本，3个特征
X = torch.tensor([[1,2,3], [4,5,6]]).float()
# 实例化 torch.nn.Linear 层
layer = nn.Linear(3,1, bias=True)
# 初始化 layer 的 weight 和 bias
nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 2)
# 计算结果
y = layer(X) # 1*1+2*1+3*1+2=8; 1*4+1*5+1*6+2=17
print(y.detach()) # >>> [[8.], [17.]]
# 输出参数
print(layer.state_dict())
print('Weights:', layer.weight.detach())
print('Bias:', layer.bias.detach())


""" 3. 激活函数层

    · 该类层实现对输入数据进行"激活"，没有可学习的参数
      这类层包括：nn.ReLU(), nn.Sigmoid(), nn.Tanh()等
"""
X = torch.tensor([[1,2,-3], [4,5,-6]]).float()
layer = nn.ReLU()
out = layer(X)
print(out) # >>> tensor([[1.,2.,0.], [4.,5.,0.]])
print(layer.state_dict()) # >>> OrderedDict() 无可学习的参数


""" 4. BatchNorm1d / BatchNorm2d/ BatchNorm3d
    
    · 该类层实现了对输入数据的标准化，即使数据服从正态分布
    · 完整形式是：nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True)
      一般设定 num_features 即可，该参数表示每个数据的维度，其余参数暂不表
"""
# Toy data: 5个样本，3个特征
X = torch.randint(10,(10,3)).float()
# 实例化 nn.BatchNorm1d 层
layer = nn.BatchNorm1d(3)
# 计算结果
y = layer(X)
print(y)


""" 5. Conv1d /  Conv2d / Conv3d

    · 该类卷积层实现对输入数据的卷积运算
      数学公式见《深度学习》P203
"""
# Toy data: 100个图片样本，3表示RGB彩色图片，横向50个像素点，纵向100个像素点
X = torch.randn(100, 3, 50, 100)
# 实例化 nn.Conv2d 层
layer = nn.Conv2d(in_channels=3,   # 彩色图片，in_channels = 3 
                  out_channels=33, # 用 33 个扫描器扫描
                  kernel_size=4, # 扫描器的大小为 4x4，也可定义为非正方形，kernel_size=(3,6)
                  stride=(1,2),  # 扫描器横向每隔 1 个像素点扫描一次，扫描完一行后，向下移动 2 个像素点，进行下一轮扫描
                  padding=2)  # 在图片的边缘补充两行/列 0，确保边缘目标被扫描到，也可以padding=(2,1)

# 输出结果
out = layer(X)
print(out.size()) # >>> [100, 33, 51, 51]
# 100 表示样本个数
# 33 表示通道数，因为用 33 个扫描器扫描，所以输出 33 个特征
# 51 表示"新"图片的横向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 4 + 2 * 2) / 1 + 1 = 51
# 50 表示"新"图片的纵向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (100 - 4 + 2 * 2) / 2 + 1 = 51


""" 6. Maxpool1d / Maxpool2d / Maxpool3d

    · 该类池化层对数据进行池化运算，即用局部特征表示区域特征，
      局部特征可以取最大值、平均值等，具体暂且不表
"""
# Toy data: 20个样本，深度16，横、纵向均50个像素点
X = torch.randn(20, 16, 50, 50)
# 实例化 nn.Maxpool2d 层
layer = nn.MaxPool2d(kernel_size=2, #  k表示池化区域的尺寸,横向 2个像素点，纵向 2个像素点
                     stride=(2,1),  #  stride=(3, 2) 表示横向每隔 2个点池化一次，池化完一行后，向下移动 1个点，进行下一轮池化
                     padding=1
                    )         
out = layer(X)
print(out.size()) # >>> [20, 16, 26, 51]
# 20 表示样本个数
# 16 表示通道数
# 26 表示"新"图片的横向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 2 + 2 * 1) / 2 + 1 = 26
# 51 表示"新"图片的纵向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 2 + 2 * 1) / 1 + 1 = 51