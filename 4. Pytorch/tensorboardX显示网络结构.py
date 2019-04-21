import torch
import torch.nn as nn
from tensorboardX import SummaryWriter

""" 搭建模型及实例化 """
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
    
X = torch.rand(100, 10)
net = Model(10, 20, 30, 10)

""" 创建日志目录和日志comment """
writer = SummaryWriter('E:\Work\Jupyter\Log', comment='MLP')    # 日志文件夹名为 Log

""" 写入日志 """
with writer:
    writer.add_graph(net, (X,))

""" 运行tensorboard """

# 在Log目录上一级目录的地址栏中输入cmd --> 输入命令:tensorboard --logdir=Log

# 在chrome输入网址：http://localhost:6006/