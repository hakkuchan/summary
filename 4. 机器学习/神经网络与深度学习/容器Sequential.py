""" torch.nn.Sequential(*args) """

# nn.Sequential()可以理解为一个容器，里面依次列出各个操作；
# 输入这个容器的 X 会依次执行操作，最终输出结果。

# 示例：
import torch
from torch import nn

# 输入 10 个样本，每个样本有 4 个特征
X = torch.randn(10, 4)

# 实例化 nn.Sequential
layer = nn.Sequential(
                      nn.Linear(4, 3),    # 对 X 进行线性变换
                      nn.BatchNorm1d(3),  # 对上一步输出结果进行批标准化
                      nn.Linear(3, 2),    # 对上一步输出结果进行线性变换
                      nn.Sigmoid()        # 对上一步输出结果进行激活函数转换
                      )

# 输出结果
y = layer(X)
print(y)