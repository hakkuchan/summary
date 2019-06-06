""" class torch.nn.BatchNorm1d(2d,3d) """

# 对一批数据进行标准化 (使数据服从正态分布)，数学公式见手写笔记
# 完整形式是：nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True)
# 一般设定 num_features 即可，该参数表示每个数据的维度
# 其余参数暂不表

# 示例：
from torch import nn

# 输入 5 个样本，每个样本有 3 个特征
X = torch.rand(5,3).float()

# 实例化 nn.BatchNorm1d
layer = nn.BatchNorm1d(3)

# 计算结果
y = layer(X)
print(y)