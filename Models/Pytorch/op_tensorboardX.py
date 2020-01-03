""" tensorboard 启动 """

# 比如日志文件夹的目录是：E:\Work\Jupyter\Data\Log
# 在上一级目录的地址栏（即 E:\Work\Jupyter\Data）中输入cmd --> 输入命令:tensorboard --logdir=Log
# 在chrome输入网址： cmd 中给出的网址 或 http://localhost:6006/



""" tensorboardX 记录标量：add_scalar(), add_scalars() """

""" add_scalar() """
# 功能：在一个图表中记录一个标量的变化，常用于 Loss 和 Accuracy 曲线的记录。
# 完整形式：add_scalar(tag, scalar_value, global_step=None, walltime=None)
# 参数含义：
# tag(string) - 该图的标签
# scalar_value(float or string/blobname) - 用于存储的值，曲线图的 y 坐标
# global_step(int) - 曲线图的 x 坐标
# walltime(float) - 为 event 文件的文件名设置时间，默认为 time.time()

import torch
from tensorboardX import SummaryWriter
writer = SummaryWriter('E:\Work\Jupyter\Data\Log') # 创建日志文件夹
for n_iter in range(100):
    s = torch.rand(1)
    writer.add_scalar('random_scalar', s[0], n_iter)
writer.close()


""" add_scalars() """
# 功能：在一个图表中记录多个标量的变化，常用于对比。
# 完整形式：add_scalars(main_tag,tag_scalar_dict,global_step=None,walltime=None)
# main_tag(string) - 该图的标签
# tag.scalar_dict(dict) - dict中，key是变量的tag，value是变量的值
# global_step(int) - 曲线图的x坐标
# walltime(float)- 为event文件的文件名设置时间，默认为time.timeO

import numpy as np
import torch
from tensorboardX import SummaryWriter
writer = SummaryWriter('E:\Work\Jupyter\Data\Log') # 创建日志文件夹
for n_iter in range(1, 100):
    writer.add_scalars('two trigonometrics', {"xsinx": n_iter * np.sin(n_iter), "xcosx": n_iter * np.cos(n_iter),}, n_iter)
writer.close()


""" tensorboardX 绘制网络结构：add_graph() """

import torch
import torch.nn as nn
from tensorboardX import SummaryWriter

class Model(nn.Module):
    def __init__(self, in_dim, n_hidden, out_dim):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden),
                                    nn.BatchNorm1d(n_hidden),
                                    nn.ReLU(True))
        self.layer2 = nn.Linear(n_hidden, out_dim)
    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        return out
    
X = torch.rand(100, 10)
mlp = Model(10, 20, 1)
writer = SummaryWriter('E:\Work\Jupyter\Data\Log')  # 创建日志文件夹
writer.add_graph(mlp, (X,))
writer.close()