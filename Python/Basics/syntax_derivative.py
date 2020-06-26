""" 1. 列表推导式 """
alist = [x**2 for x in range(5)]
print(alist)
# 等价于：
print([x**2 for x in range(5)])

# 其他例子
print([[x**2, x**3] for x in range(5)])
print([(x, y) for x in [1,2] for y in [1,2] if x != y])
print([x if x % 2 == 0 else -x for x in range(1, 11)])


""" 2. 字典推导式 """
adict = {i:j for i,j in zip(['a','b','c'], [1,2,3])}
print(adict)
# 等价于：
print({i:j for i,j in zip(['a','b','c'], [1,2,3])})

# 与 .items() 联合使用
adict = {'a':1, 'b':2, 'c':3, 'd':4}
print({v+100:k for k,v in adict.items()})


""" 3. 生成器推导式 """
''' (1) 用()创建generator '''
x = -1
out = (0 if x < 0 else x) # <generator object>
print(out)
# 等价于：
print(0 if x < 0 else x)

''' (2) 把列表生成式的[]改成()创建generator '''
a = (x**2 for x in range(10))
# a. 用next提取生成器中的元素
print(next(a))  # >>> 0
print(next(a))  # >>> 1
print(next(a))  # >>> 4
# b. 循环提取生成器中的元素
for n in a:
    print(n)
