""" · 目录
    |
    |—— 1. 概述
    |
    |—— 2. re库
    |   |
    |   |—— 2.1 ~ 2.4 search()  match()  findall()  finditer()
    |   |
    |   |—— 2.5 ~ 2.7 split()  sub()  compile()
    |
    |—— 3. match对象: .string  .re  .pos  .endpos  .group  .start  .end  .span
    |
    |—— 4. 贪婪匹配和最小匹配
"""



""" 1. 概述
    
    · 正则表达式（regular expression）用于简洁地表达一组字符串
      由re库实现，主要应用于字符串的匹配
      
    · 正则表达式由 字符 和 操作符 组成，常用操作符如下：
      |  .       |  表示任何单个字符
      |  []      |  字符集, 对单个字符给出取值范围（ [abc] 表示 a、b、c， [a‐z] 表示 a到z单个字符 ）
      |  [^]     |  非字符集, 对单个字符给出排除范围（ [^abc] 表示 非a或b或c的单个字符 ）
      |  *       |  前一个字符0次或无限次扩展（ abc* 表示 ab、abc、abcc、abccc等 ）
      |  +       |  前一个字符1次或无限次扩展（ abc+ 表示 abc、abcc、abccc等 ）
      |  ?       |  前一个字符0次或1次扩展（ abc? 表示 ab、abc ）
      |  |       |  左右表达式任意一个（ abc|def 表示 abc、def ）
      |  {m}     |  扩展前一个字符m次（ ab{2}c 表示 abbc ）
      |  {m, n}  |  扩展前一个字符m至n次（ ab{1,2}c 表示 abc、 abbc ）
      |  ^       |  匹配字符串开头（ ^abc 表示 abc且在一个字符串的开头 ）
      |  $       |  匹配字符串结尾（ abc$ 表示 abc且在一个字符串的结尾 ）
      |  ()      |  分组标记，内部只能使用 | 操作符（ (abc) 表示 abc，(abc|def) 表示 abc、def ）
      |  \d      |  数字，等价于[0‐9]
      |  \w      |  单词字符，等价于[A‐Za‐z0‐9_]

     · 经典正则表达式
      | ^[A-Za-z]+$             | 由26个字母组成的字符串
      | ^[A-Za-z0-9]+$          | 由26个字母和数字组成的字符串
      | ^-?\d+$                 | 整数形式的字符串
      | ^[e-9]*[1-9][0-9]*$     | 正整数形式的字符串
      | [1-9]\d{5}              | 中国境内邮政编码，6位
      | [\u4e00-\u9fa5]         | 匹配中文字符
      | \d{3}-\d{8}|\d{4}-\d{7} | 国内电话号码，010-68913536
      | \d+.\d+.\d+.\d+         | IP地址

     · 控制标记（flags）
      | re.I  | 忽略正则表达式的大小写，比如使[A‐Z]能够匹配小写字符
      | re.M  | 使^操作符能够将给定字符串的每行当作匹配开始
      | re.S  | 使.操作符不仅能匹配所有字符，还能匹配换行符
"""



""" 2. re库 """
import re

''' 2.1 search() ：返回正则表达式的第一个匹配项 '''
out = re.search(r'[1-9]\d{5}', 'BUCT 100029')
print(out.group(0))  # >>> 100029

''' 2.2  match() ：从字符串起始位置匹配 '''
out = re.match(r'[1-9]\d{5}', 'BUCT 100029')
print(out)  # >>> None  .match()方法从起始位置开始匹配，因此返回 None
out = re.match(r'[1-9]\d{5}', '100029 BUCT')
print(out.group(0))  # >>> 100029

''' 2.3 findall() ：以列表类型返回全部能匹配的子串 '''
out = re.findall(r'[1-9]\d{5}', 'BUCT100029, BIT100081')
print(out)  # >>> ['100029', '100081']

''' 2.4 finditer() ：搜索字符串，返回一个匹配结果的迭代类型 '''
for out in re.finditer(r'[1-9]\d{5}','BUCT100029 BIT100081'):
    print(out.group(0))  # >>> 100029 /n 100081

''' 2.5 split() ：将字符串按照正则表达式进行分割，返回去除匹配项的列表 '''
out = re.split(r'[1-9]\d{5}','BUCT100029 BIT100081')
print(out)

''' 2.6 sub() ：在一个字符串中替换所有匹配正则表达式的子串，返回替换结果 '''
out = re.sub(r'[1-9]\d{5}','zipcode','BUCT100029 BIT100081')
print(out)

''' 2.7 compile() ：编译正则表达式，以便使用 '''
regex = re.compile(r'[1-9]\d{5}')
print(regex.findall('BUCT100029 BIT100081'))  # >>> ['100029', '100081']  以 findall()为例



""" 3. match 对象 """
out = re.search(r'[1-9]\d{5}', 'BUCT 100029 BIT 100081')
print(type(out))  # >>> <class 're.Match'>

# (1) .string  返回待匹配的字符串
print(out.string) # >>> BUCT 100029 BIT 100081

# (2) .re  返回正则表达式
print(out.re)  # >>> re.compile('[1-9]\\d{5}')

# (3) .pos  返回第一个被匹配字符的索引
print(out.pos) # >>> 0

# (4) .endpos  返回最后一个被匹配字符的索引
print(out.endpos)  # >>> 22

# (5) .group(0) 返回匹配结果
print(out.group(0)) # >>> 100029

# (6) .start() 返回第一个符合匹配字符的索引
print(out.start())  # >>> 5

# (7) .end()   返回最后一个符合匹配字符的索引
print(out.end())    # >>> 11

# (8) .span()  返回 ( 第一个符合匹配字符的索引, 最后一个符合匹配字符的索引 )
print(out.span())   # >>> (5, 11)



""" 4. 贪婪匹配和最小匹配 """
# (1) re库默认贪婪匹配，即返回满足正则表达式的最长字符串
out = re.search(r'PY.*N', 'PYANBNCNDN')
print(out.group(0))  # >>> PYANBNCNDN

# (2) 最小匹配: 返回满足正则表达式的最短字符串
#     通过在对应操作符前增加 ? 实现，例如：r'PY.*N' → r'PY.*?N'
out = re.search(r'PY.*?N', 'PYANBNCNDN')
print(out.group(0))  # >>> PYAN