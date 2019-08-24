"""
1. 条件语句: 
    (1) if……else……  
    (2) if……elif……elif……  

2. 循环语句: 
    (1) while 布尔条件 
    (2) for 范围条件，包括 2 种用法：
        (a) for i in range(num)
        (b) for i in [1, 2, 3]
        
3. break 和 continue 语句：
    (1) break 用于终止最近的 for 或 while 循环，执行之后的代码; 
    (2) continue 跳过当前循环的剩余语句，然后继续进行下一轮循环。
    (3) 慎用break和continue。
    
4. pass 语句：
    当语法上需要一个语句，但程序需要什么动作也不做时，可以使用 pass。
"""


""" 三种特殊循环"""

# items() 取出字典的键值对
knights = {'Mike': 99, 'Julia': 97}
for k, v in knights.items():
    print(k, v)
    
# enumerate() 取出索引和元素
for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)
    
# zip() 同时取出多个容器的元素
questions = ['name', 'age']
answers = ['Mike', '27']
for a, b in zip(questions, answers):
     print((f'What is your {a}?  It is {b}.'))
   
   
""" input()函数 """
score = input('请输入成绩：')  # 注意：input()返回结果都为字符串
print('该学生成绩为：' + score)
print(type(score))