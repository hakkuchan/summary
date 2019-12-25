""" 1. 赋值推导式 """
x = -1
out = 0 if x < 0 else x
print(out)
# 等价于：
print(0 if x < 0 else x)


""" 2. 列表推导式 """
lst = [x**2 for x in range(10)]
print(lst)
# 等价于：
print([x**2 for x in range(10)])
''' 其他例子 '''
print([[x**2, 3*x] for x in range(10)])
print([round(3.1415926, i) for i in range(1, 6)])
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])


""" 3. 字典推导式 """
dic = {i:j for i,j in zip(['a','b','c'], [1,2,3])}
print(dic)
# 等价于：
print({i:j for i,j in zip(['a','b','c'], [1,2,3])})
''' 与 .items() 联合使用 '''
dic = {"a":1, "b":2, "c":3, "d":4}
print({v+100:k for k,v in dic.items()})