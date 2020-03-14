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
         |—— 2.3 其它：相互转换、转置
"""


""" 1. 概述
    
    · matrix类型是array类型的分支，两者在很多时候都是通用的
    
    · 主要区别在于：
      1) matrix只能表示一维数组或二维矩阵
      2) matrix可直接进行求逆（matrix.I)
      3）对array类型，虽然可使用 np.linalg.inv(array) 求逆，但要求 array 必须是方阵
      4) array*array 表示点乘；matrix*matrix 表示叉乘；array*matrix 表示叉乘
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
print(matrix * matrix) # 叉乘
print(array * array)   # 点乘 (!!!)
# 预算符 @
print(matrix @ matrix) # 叉乘
print(array @ array)   # 叉乘
# 预算符 .dot()
print(matrix.dot(matrix)) # 叉乘
print(array.dot(array))   # 叉乘

''' 2.3 其它 '''
# (1) 相互转换
print(type(np.asmatrix(array)))
print(type(np.asarray(matrix)))
# (2) 转置
print(matrix.T)
print(matrix.T)