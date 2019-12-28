""" 1. 输入  input()函数 """
score = input('请输入成绩：')  # input()函数用于输入操作
print('该学生成绩为：' + score)
print(type(score))  # 注意：input()返回结果都为字符串



""" 2. 输出  print()函数 """

m, n = 5, 10

# format的用法
print('num: {:.3f}'.format(m)) # 设置输出精度  >>> 5.000
print('|{:>10}|{:>10}|'.format(m, n))        # 生成表格：{:>10} 表示格子宽10个字符，内容右对齐
print('|{:>10.3f}|{:>10.2f}|'.format(m, n))  # 既设置格子，又设置内容精度

# 等价形式(推荐)
print(f'num: {m:.3f}')
print(f'|{m:>10}|{n:>10}|')
print(f'|{m:>10.3f}|{n:>10.2f}|')

''' end的用法 '''
# end = '\r': 覆盖上一行
# end = '\n': 换行
# end = ''  : 不换行