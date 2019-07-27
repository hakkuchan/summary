""" 赋值推导式 """
x = -1
out = 0 if x < 0 else x
print(out)

print(0 if x < 0 else x) # 也可直接输出推导式

""" 列表推导式 """
import math
print([x**2 for x in range(10)])
print([[x**2, 3*x] for x in range(10)])
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print([round(math.pi, i) for i in range(1, 6)])

""" 字典推导式 """
print({i:j for i,j in zip(['a','b','c'], [1,2,3])})

eg_dict = {"a":1, "b":2, "c":3, "d":4}
print({v+100:k for k,v in eg_dict.items()})