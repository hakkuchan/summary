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
print(s.peek())
print(s.size())
print(s.pop())
print(s.pop())