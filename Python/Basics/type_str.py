""" · 编码
      字符串指计算机处理的文本数据，计算机处理文本时须先把文本转换为数字，该过程成为编码。
	  
	  最早有127个字符(大小写英文字母、数字和一些符号)被编码(比如，A被编码为65)，该编码表称为ASCII码；
	  为了处理中文，中国制定了GB2312编码；同理，日本、韩国等分别制定了Shift_JIS、Euc-kr编码。
	  由于各国各有标准，不可避免地出现了冲突。使得在多语言混合文本中，有时会显示出乱码。
	  
	  在此背景下，Unicode编码把所有语言统一到一套编码里，
	  但问题是用Unicode比ASCII编码需要多一倍的存储空间(ASCII编码是1个字节，而Unicode编码通常是2个字节)，
	  如果文本中英文很多的话，用Unicode编码在存储和传输上十分不划算。
	  
	  所以出现了UTF-8编码，该编码把Unicode字符根据不同类型编码成1-6个字节：
	  英文字母被编码成1个字节，常用汉字是3个字节，生僻字是4-6个字节。
	  如此一来，如果文本包含大量英文字符，用UTF-8编码就能节省空间。
	  UTF-8编码的另一个好处是：ASCII编码实际上可被看成是UTF-8编码的一部分，所以很多只支持ASCII编码的遗留软件可以在UTF-8编码下使用。

      计算机系统通用的字符编码工作方式是：
	  (1) 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或传输时，转换为UTF-8编码。
	  (2) 在编辑文件时，从文件读取的UTF-8字符被转换为Unicode字符到内存里；编辑完成后，保存时再把Unicode转换为UTF-8。
	  (3) 在浏览网页时，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器。
"""

# ord()函数用于获取字符的整数表示
print(ord('A')) # >>> 65
# chr()函数用于把编码转换为对应字符
print(chr(65)) # >>> A
# encode()函数可把字符串转换为用于传输和存储的比特
print('中文'.encode('utf-8'))
print('A'.encode('ascii'))
# decode()函数用于把比特转换为字符串
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))



""" · 字符串
      在Python中，字符串以Unicode编码，因此支持多种语言
	  单行字符串用1对单引号或双引号表示，多行字符串用3对单引号或双引号表示    
      字符串是不可变类型，对字符串的修改实际上是创造了新字符串


    · 目录
    |
    |—— 1. 通用操作：索引&切片、拼接、成员、内置函数
    |
    |—— 2. 特殊操作：大小写、删除空格、对齐、替换、分割、合并、类型判断、换行符、制表符、原始字符串、格式化
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
# 格式化 (更推荐 format 函数，见"输入/输出"节)
print('Name: %s, Age: %d' % ('Michael', 28)) # >>> Name: Michael, Age: 28


""" 3. eval()函数（在简化代码上非常有用） """
# 把字符串转化为相应的对象
a = "[1,2,3]"
print(eval(a))  # >>> [1, 2, 3]
a = '1,2,3'
print(eval(a))  # >>> (1, 2, 3)
# 把字符串转化为相应的表达式
print(eval('pow(10, 2)'))  # >>> 100
print(eval("100 + 5"))     # >>> 105