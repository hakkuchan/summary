""" 激活函数层对输入数据进行非线性转换，包括 nn.ReLU(), nn.Sigmoid(), nn.Tanh() 等 """

import torch
import torch.nn as nn

# 实例化ReLU层
layer = nn.ReLU()

# 计算
X = torch.tensor([[1,2,-3], [4,-5,-6]]).float()
y = layer(X)
print(y) # >>> tensor([[1.,2.,0.], [4.,0.,0.]])

# 激活函数层无可学习的参数
print(layer.state_dict()) # >>> OrderedDict()
