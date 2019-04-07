import torch.nn as nn
import torch.nn.functional as F

""" 方法 1 """
class Model(nn.Module):  # nn.Module 是所有 ANN 的基类，构建 ANN 时需继承它
    def __init__(self):    # class 的初始化函数
        super(Model, self).__init__()      # 确保父类被正确得初始化
        self.conv1 = nn.Conv2d(1, 20, 5)   # 添加子模块 
        self.add_module("conv2", nn.Conv2d(10, 20, 4))   # add_module 添加子模块,与上面的方法作用等价
    
    def forward(self, x):    # 定义了计算执行的步骤
        x = F.relu(self.conv1(x))    # F.relu 是非线性激活函数
        x = F.relu(self.conv2(x))
        return x

CNN = Model()  # 实例化 Model()
print(CNN)     # 输出 CNN 的参数
print(CNN.conv1)    # 输出 CNN 中 conv1 子模块的参数


""" 方法 2：使用 nn.Sequential 顺序添加层（子模块） """
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        
        self.layer1 = nn.Sequential()   # 定义一个空 Sequential 容器
        self.layer1.add_module('conv1', nn.Conv2d(1, 20, 5)) # 向其中添加 conv 层，命名为‘conv1’
        self.layer1.add_module('relu', nn.ReLU())            # 再顺序添加非线性激活层 ReLU，命名为‘relu’
        
        self.layer2 = nn.Sequential(nn.Conv2d(1, 20, 5), nn.ReLU()) # 直接在 Sequential 容器中添加子模块，与上面的方法等价

    def forward(self, x):
        x = layer1(x)
        x = layer2(x)
        return x

CNN = Model()  # 实例化 Model()
print(CNN.layer1)    # 输出 CNN 中 layer1 层的参数