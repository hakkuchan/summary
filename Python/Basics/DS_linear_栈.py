""" 1. 概述
    
    · 栈 (stack) 是一个有次序的数据集；
      每个数据项仅从“栈顶”加入栈，并从“栈顶”移除；
      可以想像成一摞盘子，只能从最上面加盘子和拿走盘子；
    
    · 栈具有后进先出的特性，可用于需要倒转次序的操作，
      比如浏览器的后退，先后退到的页面是最近访问的页面。
"""



""" 2. 基于list实现栈 """

class Stack:
    def __init__(self):
        ''' 初始化一个空栈 '''
        self.stack = []
    
    def is_empty(self):
        ''' 检查是否为空栈 '''
        return self.stack == []
    
    def add_tail(self, data):
        ''' 在栈顶加入数据 '''
        self.stack.append(data)
    
    def pop_tail(self):
        ''' 在栈顶移除数据 '''
        return self.stack.pop()

    def size(self):
        ''' 查看栈中数据个数 '''
        return len(self.stack)
    
    def show(self):
        ''' 显示栈 '''
        return self.stack

s = Stack()
print(s.is_empty())  # >>> True
s.add_tail(5)
s.add_tail('cat')
s.add_tail(100)
print(s.show())  # >>> [5, 'cat', 100]
print(s.is_empty()) # >>> False
print(s.size())     # >>> 3
print(s.pop_tail())      # >>> 100
print(s.pop_tail())      # >>> cat



""" 3. 栈的应用：一般用于倒转次序的操作 """

# 例 1：识别括号是否左右匹配
def parchecker(string):
    s = Stack()
    balanced = True  # 假定括号匹配成功
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]  # 提取 string 的第 index 个元素
        if symbol in '([{':
            s.add_tail(symbol)      # 如果是左括号，就将其加入栈
        else:
            if s.is_empty():     # 如果是右括号，且栈空了，说明右括号多了，匹配失败 
                balanced = False
            else:               # 如果是右括号，且栈未空
                top = s.pop_tail()   # 从栈顶移出一个元素
                if not matches(top, symbol):  # 利用matches函数检查括号类型是否匹配
                    balanced = False
        index = index + 1
    if balanced and s.is_empty(): # 如果遍历字符串全部元素后，栈空了，匹配成功
        return True
    else:                        # 如果遍历字符串全部元素后，栈未空，说明左括号多了
        return False
def matches(left, right):
    lefts = '([{'
    rights = ')]}'
    return lefts.index(left) == rights.index(right) # 检查左括号和右括号的索引是否一致，一致说明类型匹配
matches('(',']')

print(parchecker('{[()][]}'))  # >>> True
print(parchecker('{[(}]}'))    # >>> False


# 例 2: 十进制转化为十六位以下的任意进制
def dec_base(dec_num, base):     # base表示几进制
    digits = '0123456789ABCDEF'  # 十六进制中，A表示10，B表示11，以此类推，F表示15
    remstack = Stack()
    while dec_num > 0:
        rem = dec_num % base  # 取余
        remstack.add_tail(rem)    # 将余数存入栈
        dec_num = dec_num // base  # 整除
    base_num = ''
    while not remstack.is_empty():
        base_num = base_num + digits[remstack.pop_tail()]  # 从栈顶依次取出余数，拼接成base进制数
    return base_num

print(dec_base(92, 16)) # >>> 5C