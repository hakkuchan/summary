import numpy as np

""" 比较运算符 """
a = np.array([1,2,3])
b = np.array([1,2,4])

# == 等于
print('==：',a[0]==b[0])
# != 不等于
print('!=：',a[0]!=b[0])
# > 大于
print('>：',a[0]>b[0])
# < 小于
print('<：',a[0]<b[0])
# >= 大于等于
print('>=：',a[0]>=b[0])
# <= 小于等于
print('>=：',a[0]<=b[0])
# any() 和 all() 比较数组对应元素
print('any()：', (a==b).any()) # a, b 数组中对应元素只要有相同的就返回 True
print('all()：', (a==b).all()) # a, b 数组中对应元素必须全部相同才返回 True


""" 逻辑运算符 """
c = 3
# and 和
print('and:', c in a and c in b)
# or 或
print('or:', c in a or c in b)


""" 成员运算符 """
d = 4
# in
print('in:', d in a, a, d)
# not in
print('not in:', d not in a, a, d)
