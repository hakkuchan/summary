""" · 逻辑值
      True 和 False (bool型数据，是int型的子类)
      bool(任何非零数、非空容器) 为 True，反之为 False
    
    · 目录
    |
    |—— 1. 和、或、否
    |
    |—— 2. 成员运算
    |
    |—— 3. 比较运算
"""

""" 1. 和、或、否 """
i, j = 1, 4
lst = [1, 2, 3]
# and 和
print((i in lst) and (j in lst)) # >>> False
# or  或
print((i in lst) or (j in lst))  # >>> True
# not 否
print(i not in lst)  # >>> False


""" 2. 成员运算 (in / not in) """
i = 1
lst = [1, 2, 3]
# in
print(i in lst)  # >>> True
# not in
print(i not in lst)  # >>> False

''' * 用in代替or的技巧：if (x==1) or (x==2) or (x==3) 等价于 if x in (1,2,3) '''


""" 3. 比较运算 """
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

''' * ndarray的比较运算：any() 和 all() 的作用 '''
import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 2, 4])
print((a == b).any()) # >>> True   对应元素只要有相同的就返回 True
print((a == b).all()) # >>> Fasle  对应元素必须全部相同才返回 True
