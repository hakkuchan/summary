""" · 批标准化层对输入数据进行转换，使之服从正态分布
      根据处理数据的维度不同，批标准化层分为 BatchNorm1d / BatchNorm2d / BatchNorm3d
"""

import torch
import torch.nn as nn

# 实例化 nn.BatchNorm1d 层
layer = nn.BatchNorm1d(num_features=3)

# 计算
X = torch.randint(10,(100,3)).float()
y = layer(X)
print(y)