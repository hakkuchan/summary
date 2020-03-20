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

# 实例化 torch.nn.Linear 层
layer = nn.Linear(3,1, bias=True)

# 将 nn.Linear 中的权重和偏置项设置为 1
nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 2)

# 计算结果
y = layer(X) # 1*1 + 2*1 + 3*1 + 2 = 8; 1*4 + 1*5 + 1*6 + 2 = 17
print(y)


""" class torch.nn.BatchNorm1d(2d,3d) """

# 对一批数据进行标准化 (使数据服从正态分布)
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


""" class torch.nn.Conv2d """

# 卷积运算的数学公式见《深度学习》P203
# 卷积运算常用于图像处理,因此主要学习 nn.Conv2d

# 示例:
import torch
from torch import nn

# 输入 100 个样本（图片），3 表示RGB彩色图片，横向 50 个像素点，纵向 100 个像素点
X = torch.randn(100, 3, 50, 100)

# 实例化 nn.Conv2d
layer = nn.Conv2d(in_channels=3,   # 彩色图片，in_channels = 3 
                  out_channels=33, # 用 33 个扫描器扫描
                  kernel_size=4,   # 扫描器的大小为 4x4，也可定义为 3x6，kernel_size=(3,6)
                  stride=(1,2),    # 扫描器横向每隔 1 个像素点扫描一次，扫描完一行后，向下移动 2 个像素点，进行下一轮扫描
                  padding=(2,1))   # 在图片的横向补充两行 0，纵向补充1列 0，确保边缘目标被扫描到，也可以 padding = 2，相当于padding=(2,2)

# 输出结果
out = layer(X)
print(out.size()) # out.size = [100, 33, 51, 51]
# 100 表示样本个数
# 33 表示通道数，因为用 33 个扫描器扫描，所以输出 33 个特征
# 51 表示 “新” 图片的横向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 4 + 2 * 2) / 1 + 1 = 51
# 50 表示 “新” 图片的纵向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (100 - 4 + 2 * 1) / 2 + 1 = 50


""" class torch.nn.Maxpool2d """

# 池化：用局部特征表示区域特征，局部特征可以取最大值、平均值等，具体参考文档

# 输入 20 个样本（图片），深度 16，横向 50 个像素点，纵向 50 个像素点
X = torch.randn(20, 16, 50, 50)

# 实例化 nn.Maxpool2d
layer = nn.MaxPool2d(
                     kernel_size=2,   #  k表示池化区域的尺寸,横向 2 个像素点,纵向 2 个像素点
                     stride=(2,1),    #  stride=(3, 2) 表示横向每隔 2 个点池化一次，池化完一行后，向下移动 1 个点，下一轮池化
                     padding=1
                    )         

out = layer(X)
print(out.size()) # out.size = [20, 16, 26, 51]

# 100 表示样本个数
# 16 表示通道数
# 26 表示 “新” 图片的横向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 2 + 2 * 1) / 2 + 1 = 26
# 51 表示 “新” 图片的纵向像素点个数，(in_size - kernel_size + 2 * padding) / stride + 1 = (50 - 2 + 2 * 1) / 1 + 1 = 51


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