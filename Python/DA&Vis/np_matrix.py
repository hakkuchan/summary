""" 目录
     |
     |—— 1. 概述
     |
     |—— 2. 示例
         |
         |—— 2.1 求逆
         |
         |—— 2.2 乘法：*   @  .dot()
         |
         |—— 2.3 幂运算
         |
         |—— 2.4 其它：相互转换、通用方法
"""


""" 1. 概述
    
    · matrix类型是array类型的分支，两者在很多时候都是通用的
    
    · 主要区别在于：
      
      (1) matrix只能表示一维数组或二维矩阵
      
      (2) matrix可直接进行求逆（matrix.I)
          而对于array，虽然可使用 np.linalg.inv(array) 求逆，但要求 array 必须是方阵
      
      (3) array*array 表示点乘；matrix*matrix 表示叉乘；array*matrix 表示叉乘
      
      (4) matrix进行幂运算时，表示的是连续进行矩阵乘法，所以指数必须是整数
          array进行幂运算时，表示对每个元素进行幂运算，指数任意
"""



""" 2. 示例 """

import numpy as np
matrix = np.matrix([[1,2],[3,4]])
array = np.array([[1,2],[3,4]])

''' 2.1 求逆 '''
print(matrix.I) # 也适用于非方阵求逆
print(np.linalg.inv(array))  # 当 array非方阵时会报错

''' 2.2 乘法 '''
# 运算符 *
print(array * array)   # 点乘
print(matrix * array)  # 叉乘
print(matrix * matrix) # 叉乘
# 预算符 @
print(matrix @ matrix) # 叉乘
print(array @ array)   # 叉乘
# 预算符 .dot()
print(matrix.dot(matrix)) # 叉乘
print(array.dot(array))   # 叉乘

''' 2.3 幂运算 '''
print(matrix ** 2)
print(array ** 2)
# print(matrix ** 0.5) >>> 报错
print(array ** 0.5)

''' 2.3 其它 '''
# (1) 相互转换
print(type(np.asmatrix(array)))
print(type(np.asarray(matrix)))
# (2) 通用方法(同array)
print(matrix.T) # 转置
print(matrix[:,0]) # 切片
print(matrix.shape) # 行列数
print(matrix.size)  # 元素总数
print(matrix.ravel()) # 展开
print(matrix.reshape(4,1)) # 改变行列数
print(matrix.astype('float')) # 类型转换
print(np.concatenate((matrix, matrix), axis=0)) # 按行拼接
print(np.concatenate((matrix, matrix), axis=1)) # 按列拼接
print(matrix + 10)    # 加法
print(matrix * 2)     # 乘法
print(1 / (matrix+1)) # 除法
print(matrix.sum())          # 所有元素求和
print(matrix.sum(axis=0))    # axis=0:每行数据求和; axis=1:按每列数据求和
print(np.sum(matrix,axis=0)) # axis=0:每行数据求和; axis=1:按每列数据求和
print(matrix.mean())  # 求平均值
print(matrix.max())   # 求最大值
print(matrix.min())   # 求最小值
print(matrix.std())   # 求标准差
print(matrix.var())   # 求方差