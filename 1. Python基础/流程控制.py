"""
条件语句 
if……else……
if……elif……elif……
"""

"""
循环语句
while：布尔条件
for：范围条件，包括：1）for i in range(num)； 2）for i in [1, 2, 3]。
"""

""" 用 in 代替 or """
x = 1
if x == 1 or x ==2 or x == 3:
    pass
# 等价于：  
if x in (1,2,3):
    pass

""" 特殊循环有三种：
items() 取出字典的键值对，
enumerate() 取出索引和元素
zip() 同时取出多个容器的元素
"""

""" 字典中循环时，用 items()可将关键字和对应值同时取出 """
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


""" 在列表中循环时，用 enumerate() 函数可以将索引位置和其对应的值同时取出 """
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
 

""" 同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素匹配 """
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print(('What is your {0}? It is {1}.'.format(q, a)))


""" break 用于跳出最近的 for 或 while 循环,continue 用于继续循环中的下一次迭代,慎用break和continue。"""
""" pass 当语法上需要一个语句，但程序需要什么动作也不做时，可以使用pass。"""