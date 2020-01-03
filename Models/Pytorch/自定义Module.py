""" 直观上可将 MyModule 看成函数，调用 Module(input) 即可得到对应的结果 """

"""以 nn 内置的 Linear 函数为例："""
import torch
from torch import nn
linear_std = nn.Linear(3, 1)
param = linear_std.state_dict()
out = linear_std(torch.tensor([[1,3,5]]).float())

print('Out:', out.detach().numpy())
print('Weight:', param['weight'].numpy())
print('Bias:', param['bias'].numpy())


"""
自定义层 MyModule 必须继承 nn.Module，并调用构造函数 super(MyModule, self).__init__()；

在构造函数__init__中定义可学习的参数，并封装成Parameter；

Module能够自动检测到自己的Parameter，并将其作为学习参数;

forward() 函数实现 MyModule 的具体功能;

无需写反向传播函数，nn.Module能够利用autograd自动实现反向传播。

"""

""" 下面自定义 MyLinear Module，以实现 nn.Linear 的功能："""

class MyLinear(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(MyLinear, self).__init__()
        self.weight = nn.Parameter(torch.randn(in_dim, out_dim))    # 初始化 weight，并用封装为 parameter
        self.bias = nn.Parameter(torch.randn(out_dim))              # 初始化 bias，并用封装为 parameter
        
    def forward(self, x):
        y = x.mm(self.weight) + self.bias
        return y

linear_ctm = MyLinear(3, 1)
param = linear_ctm.state_dict()
out = linear_ctm(torch.tensor([[1,3,5]]).float())

print('Out:', out.detach().numpy())
print('Weight:', param['weight'].t().numpy())
print('Bias:', param['bias'].numpy())


""" 搭建 ANN 模型时，可以直接用 MyLinear 代替 nn.Linear """

""" 例如： """
class Model(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(MyLinear(in_dim, n_hidden_1),  # MyLinear 的位置之前是 nn.Linear
                                    nn.BatchNorm1d(n_hidden_1),
                                    nn.ReLU(True))
        self.layer2 = nn.Sequential(MyLinear(n_hidden_1, n_hidden_2),
                                    nn.BatchNorm1d(n_hidden_2),
                                    nn.ReLU(True))
        self.layer3 = nn.Sequential(MyLinear(n_hidden_2, out_dim))
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x

""" 有时候用 MyLinear 代替 nn.Linear 时，ANN 的预测性能会改变，是因为 MyLinear 的初始化参数与 nn.Linear 的不同 """