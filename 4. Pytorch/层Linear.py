""" class torch.nn.Linear """

# 对数据做线性转化：out = AX + b
# 完整形式是：nn.Linear(in_features, out_features, bias=True)
# in_features: 输入样本的维度，比如输入样本有 3 个特征，infeatures = 3
# out_features: 输出样本的维度，比如输出一个值，则 out_features = 1；输出 10 个类别，则 out_features = 10
# bias：设定是否需要偏置项，若需要，bias = True (默认为 True)；若不需要，bias = False，相当于 out = AX

# 示例:
import torch
from torch import nn

# 输入 2 个样本，每个样本有 3 个特征
X = torch.tensor([[1,2,3], [4,5,6]]).float()

# 实例化 torch.nn.Linear
layer = nn.Linear(3,1, bias=True)

# 将 nn.Linear 中的权重和偏置项设置为 1
nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 2)

# 计算结果
y = layer(X) # 1*1 + 2*1 + 3*1 + 2 = 8; 1*4 + 1*5 + 1*6 + 2 = 17
print(y)