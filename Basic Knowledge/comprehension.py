""" 列表推导式 """
import math
print([x**2 for x in range(10)])
print([[x**2, 3*x] for x in range(10)])
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print([round(math.pi, i) for i in range(1, 6)])

""" 字典推导式 """
a = {"a":1, "b":2, "c":3, "d":4}
print(a)
print({v:k for k,v in a.items()})