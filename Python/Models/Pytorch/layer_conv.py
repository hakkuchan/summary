""" 卷积层对输入数据的卷积运算，根据数据维度不同，可分为 Conv1d / Conv2d / Conv3d """

import torch
import torch.nn as nn

# 实例化 Conv2d 层
layer = nn.Conv2d(in_channels=3,   # 黑白图片: in_channels=1; RGB彩色图片: in_channels=3
                  out_channels=10, # 卷积核的个数：用多少个卷积核扫描图片
                  kernel_size=4,   # 卷积核的大小，也可为(m,n)形式 
                  stride=1,        # 表示扫描速度：每次移动的像素点数，也可为(m,n)形式 
                  padding=2)       # 宽卷积：边缘补充几层 0，也可为(m,n)形式 

# 初始化参数 (可选操作)
nn.init.constant_(layer.weight, 1.)
nn.init.constant_(layer.bias, 0.)


# 计算
X = torch.randn(100, 3, 50, 100) # Toy data：100个样本；3表示RGB彩图；横纵向分别 50、100个像素点
y = layer(X)
print(y.size()) # >>> [100, 10, 51, 101]
# 100 表示样本个数
# 10  表示用10个卷积核扫描，所以输出10个特征
# 51  表示"新"图片的横向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50-4+2*2)/1+1 = 51
# 101 表示"新"图片的纵向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (100-4+2*2)/1+1 = 101