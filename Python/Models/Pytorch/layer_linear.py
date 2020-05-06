''' 线性层 nn.Linear 实现数据的线性转化：y = AX + b '''

import torch
import torch.nn as nn

# 实例化线性层
layer = nn.Linear(in_features=3,  # 输入变量的维度，比如输入变量有3个特征，则 in_features=3
                  out_features=1, # 输出结果的维度，比如结果为一个数值，则 out_features=1
                  bias=True)      # 设定是否需要偏置项

# 初始化参数 (可选操作)
nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 2)

# 计算
X = torch.tensor([[1,2,3], [4,5,6]]).float()  # Toy data: 2个样本，3个特征
y = layer(X)      # 1*1+2*1+3*1+2=8; 1*4+1*5+1*6+2=17
print(y.detach()) # >>> [[8.], [17.]]
print(layer.state_dict()) # 显示输出层中可学习的参数