import torch
from torch import nn, optim

# 搭建 ANN
class MLP(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(MLP, self).__init__()
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
# 实例化 MLP
model = MLP(2, 4, 2, 1)


''' 保存 model参数 (假设已训练好) '''
torch.save(model.state_dict(), 'E:/Work/Jupyter/Data/model_test.pt')


''' 加载 model参数 '''
# 使 new_model与 model 结构一致
new_model = MLP(2, 4, 2, 1)
# 加载 model参数给 new_model
new_model.load_state_dict(torch.load('E:/Work/Jupyter/Data/model_test.pt'))


''' model参数 '''
# param是集合
param = model.state_dict()
print('显示各层参数的名称：')
for name, val in param.items(): # name 表示各层的参数名称，val 表示具体的参数值
    print(name) # 显示各层参数的名称
print(param['layer1.0.weight'].size())  # >>> [4,2]  2个输入变量，分别与 layer1 中 4个 nodes连接，因此权重尺寸为 (4 X 2)
print(param['layer1.0.bias'].size())    # >>> [4]    layer1 的 4 个 nodes 各一个 bias
print(param['layer1.1.weight'].size())  # >>> [4]    批标准化层的 weights
print(param['layer1.1.bias'].size())    # >>> [4]    批标准化层的 bias
# 之后依次类推