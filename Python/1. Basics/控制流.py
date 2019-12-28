""" 1. if 条件分支
    
    · if…… 
    · if…… else……  
    · if…… elif…… elif……  



    2. while 条件循环
    
    · while <逻辑表达式，布尔条件>
    · while…… else……
    
    
    
    3. for 迭代循环
    
    · for i in range(num)
    · for i in [1, 2, 3]
    · 两种特殊 for循环 见后面
    
    
    
    4. break 和 continue 语句：
    
    · break 用于终止最近的 for 或 while 循环，执行之后的代码; 
    · continue 跳过当前 for 或 while 循环的剩余语句，然后继续进行下一轮循环。
    · 慎用break和continue。



    5. pass 语句：
    
    · 当语法上需要一个语句，但需要程序不做任何操作时，可以使用 pass。
"""


'''  两种特殊for循环 '''
# (1) enumerate()取出索引和元素
for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)

for i, j in enumerate(['a', 'b', 'c'], 3): # 索引起始值从3开始
    print(i, j)
    
# (2) zip()同时取出多个容器的元素
item = ['name:', 'age:']
info = ['Michael', '27']
for m, n in zip(item, info):
     print(m, n)