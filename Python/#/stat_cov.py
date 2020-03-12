""" 目录
     |
     |—— 1. 基础知识
     |   |
     |   |—— 1.1 计算方法
     |   |
     |   |—— 1.2 统计意义
     |
     |—— 2. 代码实现
         |
         |—— 2.1 基本公式
         |
         |—— 2.2 矩阵运算
         |
         |—— 2.3 cov方法
"""



""" 1. 基础知识
    
	1.1 计算方法
       
        X, Y 两个变量的协方差:
        cov(X, Y) = ([x_i - E(X)] * [y_i - E(Y)])之和 / (样本数-1)
		
	1.2 统计意义
	
	    协方差衡量了两个变量的相关性：
		· 协方差为正，说明两个变量正相关
		· 协方差为负，说明两个变量负相关
		· 协方差为零，说明两个变量完全相关
"""



""" 2. 代码实现 """
import numpy as np
import itertools
# Toy data：3个样本，每个样本有4个特征
X = np.array([[1.0, 2.0, 3.0, 4.0],
              [1.1, 2.1, 3.1, 3.7],
              [0.8, 1.7, 2.7, 4.1]])


''' 2.1 基本公式 '''
# 去中心化，即每个属性减去该属性的均值
Xm = X - np.mean(X, axis=0)
# 提取特征
v1 = Xm[:,0]
v2 = Xm[:,1]
v3 = Xm[:,2]
v4 = Xm[:,3]
# 计算 2个特征的协方差
def cov(data1, data2):
    cov = 0
    for i,j in zip(data1, data2):
        cov += i*j
    return cov/(len(data1)-1)
# 生成协方差矩阵
combs = list(itertools.product([1,2,3,4], [1,2,3,4]))
cov_mat_1 = [cov(eval('v'+str(comb[0])), eval('v'+str(comb[1]))) for comb in combs]
cov_mat_1 = np.array(cov_mat).reshape(4,4)


''' 2.2 矩阵运算 '''
# 去中心化，即每个属性减去该属性的均值
X = X - np.mean(X, axis=0)
cov_mat_2 = X.T @ X / (len(X)-1)


''' 2.3 cov方法 '''
cov_mat_3 = np.cov(X.T) # 注意 X 需转置

# 对比
print(np.around(cov_mat_1 - cov_mat_2))
print(np.around(cov_mat_1 - cov_mat_3))
print(np.around(cov_mat_2 - cov_mat_3))