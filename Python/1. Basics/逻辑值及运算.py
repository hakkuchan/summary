""" 1. 逻辑值
    
	· 逻辑值（bool型）：True 和 False
    · bool型是int型的子类
    · bool(0), bool(""), bool([]), bool({}) >>> False 
    · bool(任何非零数、非空容器) >>> True
"""



""" 2. 和、并、否 """
i = 1
j = 4
m = [1, 2, 3]

# and 和
print((i in m) and (j in m)) # >>> False
# or  或
print((i in m) or (j in m))  # >>> True
# not 否
print(i not in m)  # False



""" 3. 成员运算 """
i = 1
m = [1, 2, 3]

# in
print(i in m)  # >>> True
# not in
print(i not in m)  # >>> False

''' 技巧：用 in 代替 or '''
x = 1
if (x == 1) or (x == 2) or (x == 3): 
    pass
# 等价于
if x in (1, 2, 3):
    pass



""" 4. 比较运算 """
# == 等于
print([1,2,3] == [1,2,3])  # >>> True
# != 不等于
print([1,2,3] != [1,2,3]) # >>> False
# > 大于
print(10 > 5)  # >>> True
# < 小于
print(10 < 5)  # >>> False
# >= 大于等于
print(6 >= 5)  # >>> True
# <= 小于等于
print(5 <= 5)  # >>> True

''' 重要：any() 和 all() 比较数组(numpy)对应元素 '''
import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 2, 4])

print((a == b).any()) # >>> True   对应元素只要有相同的就返回 True
print((a == b).all()) # >>> Fasle  对应元素必须全部相同才返回 True