""" 1. 概述
    
    栈 (stack) 是一个有次序的数据集；
    
    每个数据项仅从“栈顶”加入到栈中，从栈顶中移除；
    
    可以想像成一摞盘子，只能从最上面加盘子、拿走盘子；
    
    具有后进先出的特性，操作特点是：次序倒转
    
    比如浏览器的后退，先后退到的页面是最近访问的也买你。
    
"""


""" 2. 基于list实现栈 """

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

s = Stack()
print(s.isEmpty())
s.push(5)
s.push('cat')
s.push(100)
print(s.isEmpty())
s.peek()
s.size()
print(s.pop())
print(s.pop())


""" 3. 栈的应用 """

''' (1) 括号匹配识别算法 '''

def parchecker_1(string):
    ''' 识别小括号是否左右匹配 '''
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

print(parchecker_1('(()(()()))'))
print(parchecker_1('(()))'))


def parchecker_2(string):
    ''' 识别各类括号是否左右匹配 '''
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

print(parchecker_2('{[()][]}'))
print(parchecker_2('{[(]]}'))