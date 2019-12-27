""" 1. 字符串的表示
  
    · 用一对 单引号 或 双引号 表示
  
    · 多行字符串用 3个单引号 或 3个双引号表示    
"""


""" 2. 字符串的操作 """

# 索引 & 切片
s = 'ABCDEFG'
print(s[0])
print(s[-1])
print(s[0:2])
print(s[:2])
print(s[0: 8: 2]) # start: end: step


# 常用
s = 'Python'
print(len(s))
print(max(s))
print(min(s))
print(s.count('n'))  # .count(obj)方法：计算值的出现次数
print(s.index('n'))  # .index(obj)方法：从列表中找出某个值第一个匹配项的索引位置


# 拼接
print('a' + 2 * 'p' + 'le') # 字符串可以用 + 进行连接，也可以用 * 进行重复


# 成员
print('o' in 'Python')


# 删除空格
print(' Hello world! '.strip())   # 去掉两端的空格
print(' Hello world! '.lstrip())  # 去掉左端的空格
print(' Hello world! '.rstrip())  # 去掉右端的空格


# 大小写
print('ABcd'.lower())    # 大写转小写
print('ABcd'.upper())    # 小写转大写
print('ABcd'.swapcase()) # 大小写互转


# 左中右对齐
print('Hello world!'.ljust(20))  # 在20个字符宽度内左对齐
print('Hello world!'.center(20)) # 在20个字符宽度内居中对齐
print('Hello world!'.rjust(20))  # 在20个字符宽度内右对齐


# 替换
print('Tom Michael Jane Jane'.replace('Jane', 'Kay'))


# 判断文字类型
print('python'.isalpha())    # 判断字符串是否全部由字母构成
print('123'.isdigit())       # 判断字符串是否全部由数字构成
print('python123'.isalnum()) # 判断字符串是否仅包含字母和数字


# 分割 & 合并
print('Hello world !'.split(' ')) # 按照空格分割字符串，返回列表
print('-'.join(['A', 'B', 'C']))  # 利用 - 连接列表中的字符串
# 相邻的两个或多个字符串会自动合并 """
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)


# 输出原始字符串
print('C:\some\name') 
print(r'C:\some\name') # 当字符串为目录时使用


# eval()函数
# (1) 把字符串转化为相应的表达式
print(eval('pow(10,2)'))
print(eval("100 + 4"))
# (2) 把字符串转化为相应的对象 '''
a = "[1,2,3,4,5,6]"
print(eval(a))
a = '1,2,3,4,5,6'
print(eval(a))