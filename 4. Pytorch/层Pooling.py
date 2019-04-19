""" class torch.nn.Maxpool2d """

# 池化：用局部特征表示区域特征，局部特征可以取最大值、平均值等，具体参考文档

# 输入 20 个样本（图片），深度 16，横向 50 个像素点，纵向 32 个像素点
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
