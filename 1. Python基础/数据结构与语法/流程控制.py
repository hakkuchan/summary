""" 1. 条件语句: (1) if……else……     (2) if……elif……elif…… """

""" 2. 循环语句: (1) while 布尔条件 (2) for 范围条件，包括 2 种用法：for i in range(num) 和 for i in [1, 2, 3] """

""" 3. 三种特殊循环: (1) items() 取出字典的键值对; (2) enumerate() 取出索引和元素; (3) zip() 同时取出多个容器的元素"""

''' items() 示例 '''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

''' enumerate() 示例 '''
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

''' zip() 示例 '''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print(('What is your {0}? It is {1}.'.format(q, a)))

""" 4. break 和 continue: 
       break 用于终止最近的 for 或 while 循环，执行之后的代码; 
       continue 跳过当前循环的剩余语句，然后继续进行下一轮循环。
	   慎用break和continue。
"""

""" 5. pass 当语法上需要一个语句，但程序需要什么动作也不做时，可以使用 pass。"""

""" 6. 输入函数 input() """
score = input('请输入成绩：') # 注意：input()返回结果都为字符串，如果需要变为数字则用到int()/float()
print('该学生成绩为：' + score)