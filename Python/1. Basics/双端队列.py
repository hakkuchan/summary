""" 1. 双端队列Deque
    
    · 一种有次序的数据集，跟队列相似，其两端可以称作“首”“尾”端，
      但deque中数据项既可以从队首加入，也可以从队尾加入；数据项也可以从两端移除。
    
    · 某种意义上说，双端队列集成了栈和队列的能力
"""


""" 2. 基于list实现双端队列 """

class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        ''' 检查双端队列是否未空 '''
        return self.items == []
    
    def addFront(self, item):
        ''' 队首加入数据 '''
        self.items.append(item)
    
    def addRear(self, item):
        ''' 队尾加入数据 '''
        self.items.insert(0, item)
    
    def removeFront(self):
        ''' 队首移除并返回数据 '''
        return self.items.pop()
    
    def removeRear(self):
        ''' 队尾移除并返回数据 '''
        return self.items.pop(0)
    
    def size(self):
        ''' 查看双端队列中元素的个数 '''
        return len(self.items)
    
d = Deque()
print(d.isEmpty())  # >>> Fasle
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())    # >>> 4
print(d.isEmpty()) # >>> False
print(d.removeRear())  # >>> dog
print(d.removeFront()) # >>> True



""" 3. 双端队列的应用：回文词判定 """

''' · 回文词：正读 和 反读 都一样的词，
      例如：“上海自来水来自海上”，“madam”
    
    · 先将需要判定的词从队尾加入deque
      再从两端同时移除字符判定是否相同，
      直到deque中剩下0个 或 1个字符
'''

def palchecker(astring):
    char_deque = Deque()
    for ele in astring:
        char_deque.addRear(ele)  # 把输入字符串中的字符加入双端队列
    stillEqual = True  # 假定其是回文词
    while char_deque.size() > 1 and stillEqual: # 当上端队列中元素多于 1 个且当前 stillEqual 为 True 时
        first = char_deque.removeFront()  # 从队首移除并返回一个元素
        last = char_deque.removeRear()    # 从队尾移除并返回一个元素
        if first != last:  # 如果队首和队尾移除的元素不相同
            stillEqual = False  # 说明不是回文词
        return stillEqual

print(palchecker('a-b-c-b-a')) # >>> True
print(palchecker('a-b-c-d'))   # >>> False