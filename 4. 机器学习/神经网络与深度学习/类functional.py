""" class torch.nn.Functional """

# nn.Functional定义了很多函数
# 需要注意，这些函数中的参数是不能被优化的

# 示例：
import torch
import torch.nn.functional as F

# 输入 10 个样本，每个样本有 4 个特征
X = torch.randn(3, 4)

# 输出结果
y = F.relu(X)   # 以relu函数为例
print(X,'\n',y)