import torch
from torch import nn

""" 自定义 Module 权值初始化 """
class MyLinear(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(MyLinear, self).__init__()
        self.weight = nn.Parameter(torch.randn(in_dim, out_dim))    # 初始化 weight，并用封装为 parameter
        nn.init.constant_(self.weight, 1)
        self.bias = nn.Parameter(torch.randn(out_dim))    # 初始化 bias，并用封装为 parameter
        nn.init.constant_(self.bias, 1)
    def forward(self, x):
        y = x.mm(self.weight) + self.bias
        return y

linear_ctm = MyLinear(3, 1)
param = linear_ctm.state_dict()
out = linear_ctm(torch.tensor([[1,3,5]]).float())

print('Out:', out.detach().numpy())
print('Weight:', param['weight'].t().numpy())
print('Bias:', param['bias'].numpy())


""" 单层权值初始化 """
layer = nn.Linear(3,1)

nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 1)

print(layer.weight, layer.bias)


""" Sequential 权值初始化 """
def init_weight(m):
    if type(m) == nn.Linear:
        torch.nn.init.constant_(m.weight,1)
        m.bias.data.fill_(1)

class Model(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(n_input, n_hidden), nn.LeakyReLU())
        self.layer2 = nn.Linear(n_hidden, n_output)
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        return x

model = Model(1,10,2)
model.apply(init_weight)

param = model.state_dict()
print(param['layer1.0.weight'], param['layer1.0.bias'])
print(param['layer2.weight'], param['layer2.bias'])