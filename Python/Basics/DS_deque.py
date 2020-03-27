""" 1. 双端队列Deque
    
    · 一种有次序的数据集，跟队列相似，其两端可以称作“首”“尾”端，
      但deque中数据项既可以从队首加入，也可以从队尾加入；数据项也可以从两端移除。
    
    · 某种意义上说，双端队列集成了栈和队列的能力
"""



""" 2. 基于list实现双端队列 """

class Deque:
    def __init__(self):
        ''' 初始化双端队列 '''
        self.deque = []
    
    def is_empty(self):
        ''' 检查双端队列是否未空 '''
        return self.deque == []
    
    def add_head(self, data):
        ''' 从队首加入数据 '''
        self.deque.insert(0, data)
    
    def add_tail(self, data):
        ''' 从队尾加入数据 '''
        self.deque.append(data)
       
    def pop_head(self):
        ''' 从队首移除并返回数据 '''
        return self.deque.pop(0)
    
    def pop_tail(self):
        ''' 从队尾移除并返回数据 '''
        return self.deque.pop()
    
    def size(self):
        ''' 查看双端队列中元素的个数 '''
        return len(self.deque)
    
    def show(self):
        ''' 遍历双端队列 '''
        return self.deque
    
d = Deque()
print(d.is_empty())  # >>> True
d.add_tail(4)
d.add_tail('dog')
d.add_head('cat')
d.add_head(True)
print(d.show())     # >>> [True,'cat', 4, 'dog']
print(d.size())     # >>> 4
print(d.is_empty()) # >>> False
print(d.pop_tail()) # >>> dog
print(d.pop_head()) # >>> True



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
        char_deque.add_tail(ele)  # 把输入字符串中的字符加入双端队列
    huiwen = True  # 假定其是回文词
    while char_deque.size() > 1 and huiwen: # 当上端队列中元素多于 1 个且当前 huiwen 为 True 时
        head = char_deque.pop_head()  # 从队首移除并返回一个元素
        tail = char_deque.pop_tail()  # 从队尾移除并返回一个元素
        if head != tail:  # 如果队首和队尾移除的元素不相同
            huiwen = False  # 说明不是回文词
        return huiwen

print(palchecker('a-b-c-b-a')) # >>> True
print(palchecker('a-b-c-d'))   # >>> False