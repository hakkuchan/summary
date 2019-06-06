""" class torch.nn.Conv2d """

# 卷积运算的数学公式见《深度学习》P203
# 卷积运算常用于图像处理,因此主要学习 nn.Conv2d

# 示例:
import torch
from torch import nn

# 输入 100 个样本（图片），3 表示RGB彩色图片，横向 50 个像素点，纵向 100 个像素点
X = torch.randn(100, 3, 50, 100)

# 实例化 nn.Conv2d
layer = nn.Conv2d(in_channels=3,   # 彩色图片，in_channels = 3 
                  out_channels=33, # 用 33 个扫描器扫描
                  kernel_size=4,   # 扫描器的大小为 4x4，也可定义为 3x6，kernel_size=(3,6)
                  stride=(1,2),    # 扫描器横向每隔 1 个像素点扫描一次，扫描完一行后，向下移动 2 个像素点，进行下一轮扫描
                  padding=(2,1))   # 在图片的横向补充两行 0，纵向补充1列 0，确保边缘目标被扫描到，也可以 padding = 2

# 输出结果
out = layer(X)
print(out.size()) # out.size = [100, 33, 51, 51]
# 100 表示样本个数
# 33 表示通道数，因为用 33 个扫描器扫描，所以输出 33 个特征
# 51 表示 “新” 图片的横向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 4 + 2 * 2) / 1 + 1 = 51
# 50 表示 “新” 图片的纵向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (100 - 4 + 2 * 1) / 2 + 1 = 50