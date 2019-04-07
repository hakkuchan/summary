"""
三者区别：
    
    赋值引用, b=a: 
        想象a是一个抽屉，b=a相当于给a这个抽屉又贴了一个标签b;
        对a/b的操作完全等价于对b/a的操作。
    
    浅拷贝, b = a.copy():
        想象a是一个抽屉，里面有10个盒子，编号是a[1]、a[2]……a[10]，
        b = a.copy()相当于给这10个盒子又贴了标签b[1]、b[2]...... b[10],
        对a[1]、a[2]……a[10]的操作完全等价于对b[1]、b[2]...... b[10]的操作，反之亦然。
        但对a/b这个抽屉的操作，比如增加一个盒子，对b/a不起作用
    
    深拷贝（需 import copy），b = copy.deepcopy(a)：
        b 完全拷贝了a的抽屉和盒子；
        并把b抽屉放在其它地方
        a, b完全独立。
"""

import copy

a = [1, 2, 3, 4, ['a', 'b']]
b = a # 赋值
c = copy.copy(a) # 浅拷贝
d = copy.deepcopy(a) # 深拷贝
a.append(5)
a[4].append('c')

print(a)
print(b)
print(c)
print(d)

""" 总结：慎用浅拷贝，多用赋值和深拷贝 """