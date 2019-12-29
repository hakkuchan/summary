""" 1. 概述
    
    · 队列 (queue) 是一个有次序的数据集；
      在队列一端添加数据，在另一端移除数据，
      可以想像成生活中的排队
	  
	· 具有先进先出的特性；
      比如打印任务排队、进程排队等
"""


""" 2. 基于list实现队列 """

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        ''' 测试是否为空队列 '''
        return self.items == []
    
    def enquene(self, item):
        ''' 在 queue 首端添加数据 '''
        self.items.insert(0, item)
    
    def dequene(self):
        ''' 在 queue 尾端移除数据 '''
        return self.items.pop()
    
    def size(self):
        ''' 返回队列中数据项的个数 '''
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enquene(4)
q.enquene('Dog')
q.enquene(8)
print(q.size())
print(q.isEmpty())
print(q.dequene())
print(q.dequene())
print(q.size())