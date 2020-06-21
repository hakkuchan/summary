""" · 字符串
      单行字符串用1对单引号或双引号表示
      多行字符串用3对单引号或双引号表示    
      字符串是不可变类型，对字符串的修改实际上是创造了新字符串

    · 目录
    |
    |—— 1. 通用操作：索引&切片、拼接、成员、内置函数
    |
    |—— 2. 特殊操作：大小写、删除空格、对齐、替换、分割、合并、类型判断、换行符、制表符、原始字符串
    |
    |—— 3. eval()函数 ：把字符串转换为对象或表达式
"""


""" 1. 通用操作（也适用于列表、元组）"""
# 索引 & 切片
s = 'ABCDEFG'
print(s[0])   # >>> A
print(s[-1])  # >>> G
print(s[0:2]) # >>> AB
print(s[:2])  # >>> AB
print(s[0: 8: 2]) # s(start: end: step)  >>> ACEG
# 拼接
print('a' + 2 * 'p' + 'le')  # >>> apple
# 成员运算
print('o' in 'Python')  # >>> True
# 内置函数
s = 'Python'
print(len(s))
print(max(s))
print(min(s))
print(s.count('n'))  # .count(obj)方法：计算值的出现次数
print(s.index('n'))  # .index(obj)方法：从列表中找出某个值第一个匹配项的索引位置


""" 2. 特殊操作（字符串是不可变类型，下面的所有操作，都是生成了新字符串，而非改变原字符串）"""
# 大小写
print('ABcd'.lower())    # 大写转小写  >>> abcd
print('ABcd'.upper())    # 小写转大写  >>> ABCD
print('ABcd'.swapcase()) # 大小写互转  >>> abCD
# 删除空格
print(' Hello world! '.strip())   # 去掉两端的空格
print(' Hello world! '.lstrip())  # 去掉左端的空格
print(' Hello world! '.rstrip())  # 去掉右端的空格
# 对齐
print('Hello world!'.ljust(20))  # 在20个字符宽度内左对齐
print('Hello world!'.center(20)) # 在20个字符宽度内居中对齐
print('Hello world!'.rjust(20))  # 在20个字符宽度内右对齐
# 替换
print('A b c A'.replace('A', 'a')) # >>> 'a b c a'
print('A b c A'.replace('A', ''))  # >>> ' b c '  用于删除特定字符，例如删掉'A'
# 分割
print('A B C'.split(' ')) # 按照空格分割字符串，返回列表  >>> ['A', 'B', 'C']
# 合并
print('-'.join(['A', 'B', 'C']))  # 利用'-'连接列表中的字符串  >>> A-B-C
# 相邻的两个或多个字符串会自动合并
text = ('A'
        'B')
print(text)  # >>> AB
# 判断字符串中文字类型
print('python'.isalpha())    # 判断字符串是否全部由字母构成  >>> True
print('123'.isdigit())       # 判断字符串是否全部由数字构成  >>> True
print('python123'.isalnum()) # 判断字符串是否仅包含字母和数字  >>> True
# \n 换行符
print('''Line1\nLine2\nLine3''')
# \t 制表符
print('''Name\tAge\tGrade''')    
print('''Bob\t28\t98''')
print('''Julia\t27\t100''')
# 原始字符串
print('C:\some\name')  # '\'会转义
print(r'C:\some\name') # 原始字符串


""" 3. eval()函数（在简化代码上非常有用） """
# 把字符串转化为相应的对象
a = "[1,2,3]"
print(eval(a))  # >>> [1, 2, 3]
a = '1,2,3'
print(eval(a))  # >>> (1, 2, 3)
# 把字符串转化为相应的表达式
print(eval('pow(10, 2)'))  # >>> 100
print(eval("100 + 5"))     # >>> 105
