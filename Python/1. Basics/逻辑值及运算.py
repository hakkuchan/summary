""" 1. 判断与真值
        · bool型是int型的子类
        · bool(0) = False, bool("") = False, bool([]) = False
        · bool(任何非零数、字符串、非空序列) = True
"""

import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 2, 4])
c = 3
d = 4


""" 2. 逻辑运算 """
# and 和
print('and:', (c in a) and (c in b)) # 为了便于可读，用括号括出条件
# or  或
print('or:', (c in a) or (c in b))
# not 否
print('not:', c not in b)


""" 3. 成员运算 """
# in
print('in:', d in a)
# not in
print('not in:', d not in a)

# 技巧：用 in 代替 or
x = 1
if (x == 1) or (x == 2) or (x == 3):
    pass
# 等价于：  
if x in (1, 2, 3):
    pass


""" 4. 比较运算 """
# == 等于
print('==：', a[0] == b[0])
# != 不等于
print('!=：', a[0] != b[0])
# > 大于
print('>：', a[0] > b[0])
# < 小于
print('<：', a[0] < b[0])
# >= 大于等于
print('>=：', a[0] >= b[0])
# <= 小于等于
print('>=：', a[0] <= b[0])

# 重要：any() 和 all() 比较数组对应元素
print('any()：', (a == b).any()) # a, b 数组中对应元素只要有相同的就返回 True
print('all()：', (a == b).all()) # a, b 数组中对应元素必须全部相同才返回 True