""" 池化层对数据进行降采样，即用局部最大值或平均值代表局部，包括：
    (1) 最大池化 (Maxpool1d / Maxpool2d / Maxpool3d) 
    (2) 平均池化 (AvgPool1d / nn.AvgPool2d / nn.AvgPool3d)
"""

import torch
import torch.nn as nn


# 实例化 nn.Maxpool2d 层
layer = nn.MaxPool2d(kernel_size=2, #  k表示池化区域的尺寸,横向 2个像素点，纵向 2个像素点
                     stride=(2,1),  #  stride=(3, 2) 表示横向每隔 2个点池化一次，池化完一行后，向下移动 1个点，进行下一轮池化
                     padding=1)         

# 计算
X = torch.randn(20, 16, 50, 50) # Toy data: 20个样本，" 深度 " 16，横、纵向均50个像素点
out = layer(X)
print(out.size()) # >>> [20, 16, 26, 51]
# 20 表示样本个数
# 16 表示图片 " 深度 "
# 26 表示"新"图片的横向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 2 + 2 * 1) / 2 + 1 = 26
# 51 表示"新"图片的纵向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 2 + 2 * 1) / 1 + 1 = 51