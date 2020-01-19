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
        ''' 初始化一个空队列 '''
        self.queue = []
    
    def is_empty(self):
        ''' 测试是否为空队列 '''
        return self.queue == []
    
    def add_head(self, data):
        ''' 在 queue 首端添加数据 '''
        self.queue.insert(0, data)
    
    def pop_tail(self):
        ''' 在 queue 尾端移除数据 '''
        return self.queue.pop()
    
    def size(self):
        ''' 返回队列中数据项的个数 '''
        return len(self.queue)
    
    def show(self):
        ''' 显示队列 '''
        return self.queue

q = Queue()
print(q.is_empty()) # >>> True
q.add_head(5)
q.add_head('Dog')
q.add_head(6)
print(q.show()) # >>> [6, 'Dog', 5]
print(q.size()) # >>> 3
print(q.is_empty()) # >>> False
print(q.pop_tail()) # >>> 5



""" 3. 应用示例 —— 击鼓传花
    
    · 用队列来实现击鼓传花的算法，
      已知参加游戏的人名列表，每次传花次数固定，传到就出局，
    
    · 用算法返回最后剩下的人名
"""

def deliver(names, num):
    game_queue = Queue()
    for name in names:
        game_queue.add_head(name) # 把名字列表中的名字加入队列
    while game_queue.size() > 1:  # 只要队列中人数超过 1 人，游戏继续
        for i in range(num):      # 每轮的传递次数为 num 次
            game_queue.add_head(game_queue.pop_tail())  # 把队尾的人名取出，添加到队首，相当于花传给了当前队尾的人
        game_queue.pop_tail()      # 每轮 num 结束后，让队尾的人出局
    return game_queue.pop_tail()   # 返回最后剩下的人名

print(deliver(['Amy','Bill','Dave','Eva','Kay','Mike'], 12))