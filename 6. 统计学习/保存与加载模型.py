import torch
from torch import nn, optim

""" 搭建 ANN & 实例化 """
class Model(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden_1),
                                    nn.BatchNorm1d(n_hidden_1),
                                    nn.ReLU(True))
        self.layer2 = nn.Sequential(nn.Linear(n_hidden_1, n_hidden_2),
                                    nn.BatchNorm1d(n_hidden_2),
                                    nn.ReLU(True))
        self.layer3 = nn.Sequential(nn.Linear(n_hidden_2, out_dim))
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x
bpnn = Model(2, 4, 2, 1) # 实例化 ANN


""" 保存 bpnn 的参数 """
torch.save(bpnn.state_dict(), 'E:/Work/Jupyter/data/bpnn.pt') # 保存 bpnn 的参数（假设已训练好）


""" 加载 bpnn 的参数 """
new_bpnn = Model(2, 4, 2, 1) # 实例化 new_bpnn，参数要与 bpnn 一致
new_bpnn.load_state_dict(torch.load('E:/Work/Jupyter/data/bpnn.pt')) # 加载 bpnn 的参数给 new_bpnn


""" 提取 bpnn 的参数 """
param = bpnn.state_dict() # param 的类型是集合
print('显示各层参数的名称：')
for name, val in param.items(): # name 表示各层的参数名称，val 表示具体的参数值
    print(name) # 显示各层参数的名称
print(param['layer1.0.weight'])


# param['layer1.0.weight'].size() >>> [4, 2]    解析：2 个输入变量，分别与 layer1 中 4 个 nodes 连接，因此权重尺寸为 (4 X 2)
# param['layer1.0.bias'].size()   >>> [4]       解析：layer1 的 4 个 nodes 各一个 bias
# param['layer1.1.weight'].size() >>> [4]       解析：批标准化层的 weights
# param['layer1.1.bias'].size()   >>> [4]       解析：批标准化层的 bias
# 之后依次类推