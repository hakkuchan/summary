""" 栈的应用：一般用于次序倒转的操作 """

''' 定义栈类 '''
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        ''' 检查是否为空栈 '''
        return self.items == []    
    def push(self, item):
        ''' 在栈顶加入元素 item '''
        self.items.append(item)
    def pop(self):
        ''' 在栈顶移除元素 item '''
        return self.items.pop()
    def peek(self):
        ''' 查看栈顶元素 '''
        return self.items[len(self.items) - 1]
    def size(self):
        ''' 查看栈中有多少个数据 '''
        return len(self.items)


''' 1. 识别小括号是否左右匹配 '''
def parchecker(string):
    s = Stack()
    balanced = True  # 假定括号匹配成功
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]  # 提取 string 的第 index 个元素
        if symbol == '(':
            s.push(symbol)      # 如果是左括号，就将其加入栈
        else:
            if s.isEmpty():     # 如果是右括号，且栈空了，说明右括号多了，匹配失败 
                balanced = False
            else:               # 如果是右括号，且栈未空，从栈里面移出一个与这个右括号匹配的左括号
                s.pop()
        index = index + 1
    if balanced and s.isEmpty(): # 如果遍历字符串全部元素后，栈空了，匹配成功
        return True
    else:                        # 如果遍历字符串全部元素后，栈未空，说明左括号多了
        return False

print(parchecker('(()(()()))'))
print(parchecker('(()))'))


''' 2. 识别各类括号是否左右匹配 '''
def parchecker(string):
    s = Stack()
    balanced = True  # 假定括号匹配成功
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]  # 提取 string 的第 index 个元素
        if symbol in '([{':
            s.push(symbol)      # 如果是左括号，就将其加入栈
        else:
            if s.isEmpty():     # 如果是右括号，且栈空了，说明右括号多了，匹配失败 
                balanced = False
            else:               # 如果是右括号，且栈未空
                top = s.pop()   # 从栈顶移出一个元素
                if not matches(top, symbol):  # 利用matches函数检查括号类型是否匹配
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty(): # 如果遍历字符串全部元素后，栈空了，匹配成功
        return True
    else:                        # 如果遍历字符串全部元素后，栈未空，说明左括号多了
        return False
def matches(left, right):
    lefts = '([{'
    rights = ')]}'
    return lefts.index(left) == rights.index(right) # 检查左括号和右括号的索引是否一致，一致说明类型匹配
matches('(',']')

print(parchecker('{[()][]}'))
print(parchecker('{[(}]}'))


''' 3. 十进制转化为二进制 '''
# 将十进制整数不断除以 2，每次得到的余数就是由低到高的二进制数，输出则是从高到低，所以需要一个栈来反转次序
def dec_bin(dec_num):
    remstack = Stack()
    while dec_num > 0:
        rem = dec_num % 2       # 取余
        remstack.push(rem)      # 将余数存入栈
        dec_num = dec_num // 2  # 整除
    bin_num = ''
    while not remstack.isEmpty():
        bin_num = bin_num + str(remstack.pop())  # 从栈顶依次取出余数，拼接成二进制数
    return bin_num

print(dec_bin(35)) # ans = 100011
# 注：二进制转十进制，以 100011 为例，十进制为 1*2^5 + 0*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 35


''' 4. 十进制转化为十六位以下的任意进制 '''
def dec_base(dec_num, base):     # base表示几进制
    digits = '0123456789ABCDEF'  # 十六进制中，A表示10，B表示11，以此类推，F表示15
    remstack = Stack()
    while dec_num > 0:
        rem = dec_num % base  # 取余
        remstack.push(rem)    # 将余数存入栈
        dec_num = dec_num // base  # 整除
    base_num = ''
    while not remstack.isEmpty():
        base_num = base_num + digits[remstack.pop()]  # 从栈顶依次取出余数，拼接成base进制数
    return base_num

print(dec_base(92, 16)) # ans = 5C
# 注：十六进制转十进制，以 5C 为例，十进制为 5*16^1 + 12 = 92