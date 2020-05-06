""" 参数初始化（以内置层 nn.Linear 为例）"""
# 初始化线性层
layer = nn.Linear(3,1, bias=True)
# 初始化参数：可选操作，因为调用内置层时会自动初始化
nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 2)
# 输出参数
print(layer.state_dict()) # 显示可学习的参数
print('Weights:', layer.weight.detach())
print('Bias:', layer.bias.detach())