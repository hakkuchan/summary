""" · 目录
    |
    |—— 1. 自带数据集
    |   |
    |   |—— 1.1 导入数据集
    |   |
    |   |—— 1.2 转换数据
    |   |
    |   |—— 1.3 加载数据
    |
    |—— 2. 其它数据集
"""

import torch
import torchvision
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

""" 1. 自带数据集 (torchvision.datasets内置多个数据集，包括：MNIST, CIFAR10, CIFAR100等) """

''' 1.1 导入数据集 (以MNIST为例) '''
# 导入
mnist = datasets.MNIST(root="E:/Work/Jupyter/Data/MNIST/", # 保存路径/加载路径
                       download=True, # 如果不存在该文件，则自动下载
                       train=True)    # True 表示读取训练集，False 表示读取测试集    
# 提取图片数据
img, label = mnist[0]
# 图片的对应标签
print('Number:', label.item())
# 像素点
print(img.size)
# 显示图片
img.show()


''' 1.2 转换数据 (transform 参数) '''
# 一次转换
mnist = torchvision.datasets.MNIST(root="E:/Work/Jupyter/Data/MNIST/", download=True, train=True,
                                   transform=transforms.ToTensor())
# 多次转换 transform.Compose([])
mnist = torchvision.datasets.MNIST(root="E:/Work/Jupyter/Data/MNIST/", download=True, train=True,
                                   transform=transforms.Compose([transforms.Scale(28*28), 
                                                                 transforms.ToTensor()]))


''' 1.3 加载数据 (DataLoader) '''
# 导入数据集
train_dataset = torchvision.datasets.MNIST(root="E:/Work/Jupyter/Data/MNIST/", download=True, train=True,
                                           transform=transforms.ToTensor())
test_dataset = torchvision.datasets.MNIST(root="E:/Work/Jupyter/Data/MNIST/", download=True, train=False,
                                          transform=transforms.ToTensor())
# 加载数据集
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
# 提取样本数据：
''' 
for i, data in enumerate(train_loader, 1):
    img, label = data  # img.size() = [32, 1, 28, 28] 32个样本，1表示灰度图，28表示像素点
                       # label.size() = [32] 32个样本标签
    img = img.view(img.size(0), -1)  # 对图片格式进行转化 [32, 1*28*28] 32个样本，1*28*28维数据
    img = img.clone().detach().requires_grad_(True) # 使数据可被 autograd 检测并追踪
    label = label.clone().detach()
'''



""" 2. 其它数据集
    
    · Pytorch 提供了接口将各种文件(图片, csv, txt等)中的数据集转换为 datasets 类，
      然后便可利用处理自带数据集的方法处理其它数据集
      
    · 但存在2个问题：
      (1) torch 至今(2020.3.22)没有直接提供 cross validation (CV) 接口，用上述方法实现 CV 会比较麻烦
      (2) torchvision.transform 接口所提供的数据转换方法主要用于处理图片数据，归一化等操作需自定义
    
    · 因此针对其它数据集，不妨以 sklearn 的接口进行操作
	  下例示意了这一过程（batch_size功能需要进一步开发）：
"""

from sklearn import datasets, model_selection, preprocessing # 不可放在本文件开头，datasets会冲突
# 导入数据集
X = datasets.load_digits().data
X = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(X) # 可选操作
y = datasets.load_digits().target
# 分割数据集
kfold = model_selection.KFold(n_splits=10, random_state=1)
for train, test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[test], y[test]
    # 把 X 数据转换为 tensor，可导
    X_train = torch.tensor(X_train).clone().detach().requires_grad_(True).float()
    X_test = torch.tensor(X_test).clone().detach().requires_grad_(True).float()
    # 把 y 数据转换为 tensor，不可导
    y_train = torch.tensor(y_train).clone().detach().requires_grad_(False).float()
    y_test = torch.tensor(y_test).clone().detach().requires_grad_(False).float()
    # 需要注意，X 和 y 转化为 tensor 需在数据集分割后进行