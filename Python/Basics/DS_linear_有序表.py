""" 有序表（Ordered list）
    
    · 表中数据依照某可比性质（如整数大小、字母先后）排位
    
    · 有序表也可基于链表实现
"""

''' 例：基于链表创建有序表 '''

''' (1) 创建节点类 '''
class Node:

    ''' 初始化节点 '''
    def __init__(self, initdata):
        self.data = initdata  # 把数据传进节点
        self.next = None      # 下一个节点设置为空
    
    ''' 返回节点的数据 '''
    def get_data(self):
        return self.data
    
    ''' 返回节点的下一个节点 '''
    def get_next(self):
        return self.next
    
    ''' 修改节点的数据项 '''
    def set_data(self, newdata):
        self.data = newdata
    
    ''' 修改节点的下一个节点 '''
    def set_next(self, newnext):
        self.next = newnext

temp = Node(5)
print(temp.get_data())  # >>> 5
print(temp.get_next())  # >>> None
temp.set_data(100)
print(temp.get_data())  # >>> 100
print(temp.get_next())  # >>> None
temp.set_next(1000)
print(temp.get_next())  # >>> 1000


''' (2) 创建有序表类 '''
class OrderedList:
    def __init__(self):
        self.head = None  # 设置表头，默认为 None（注意：表头本身不是节点，而是指向链表中的第一个节点）
    
    
    ''' 在表中增加节点 ——— 按照顺序添加 '''
    def add(self, item):
        current = self.head   # 令current指向表头指向的第一个节点
        previous = None       # 令current的前一个节点previous为 None
        stop = False
        while current != None and not stop:  # 只要当前节点不为空且未到达插入位置
            if current.get_data() > item:  # 如果发现当前节点比待增加的数据大，说明到了插入位置
                stop = True  # 跳出循坏
            else:
                previous = current  # previous前进一个节点
                current = current.get_next()  # current前进一个节点
        # while循环所包含的语句其目的是找到插入位置
        new_node = Node(item) # 实例化新节点
        if previous == None:  # 如果第一个节点前是插入位置（此时current指向第一个节点，previous为None）
            new_node.set_next(self.head)  # 让新节点指向表头指向的第一个节点
            self.head = new_node  # 让表头指向新节点（新节点变为第一个节点）
        else:  # 如果插在表中
            new_node.set_next(current)  # 让新节点指向current
            previous.set_next(new_node) # 让previous指向新节点，就把新节点插在previous和current之间了
        
        
    ''' 是否存在特定元素 '''
    def search(self, item):
        current = self.head  # 令current指向表头指向的第一个节点
        found = False  # 假定 “未找到特定元素”
        stop = False   # 如果待查找数据已大于当前current，说明肯定表中不存在待找数据，此时stop，先假定stop为假
        while current != None and not found and not stop:  # 只要表不为空，且 “未找到特定元素” 为真，且stop为假
            if current.get_data() == item:  # 检查当前current是否与待查数据匹配
                found = True  # 如果匹配，令 found = True，此时 “未找到特定数据” 为假，跳出循环
            if current.get_data() > item:
                stop = True
            else:
                current = current.get_next()  # 如不匹配，current指向下一节点
        return found
        
    
    ''' 判断链表是否为空 '''
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    
    ''' 遍历 '''
    def traversal(self):
        current = self.head    # 令current指向表头指向的第一个节点
        while current != None:
            print(current.get_data(), end=' ')  # 打印当前节点的信息
            current = current.get_next()        # current指向下一节点
        print()
    
    
    ''' 元素个数 ——— 相当于list的 len() '''
    def size(self):
        current = self.head    # 令current指向表头指向的第一个节点
        count = 0
        while current != None: # 只要current不为 None
            count += 1         # 计数
            current = current.get_next() # current指向下一节点
        return count
    

    ''' 删除特定数据 ——— 相当于list的 .remove() '''
    def remove(self, item):
        current = self.head  # 令current指向表头指向的第一个节点
        previous = None      # 令current的前一个节点previous为 None
        found = False        # 假定未找到需删除的特定数据
        while current != None and not found:  # 只要表不为空且 “未找到特定数据” 为真
            if current.get_data() == item: # 检查当前节点是不是特定数据
                found = True  # 如是，说明找到了
            else:  # 如不是，current和previous依次向后移动：
                previous = current # previous 指向 current
                current = current.get_next() # current 指向下一个节点
        # 当找到了待删除的特定数据
        if previous == None:  # 如果第一个节点就是特定数据
            self.head = current.get_next()  # 直接把表头指向current的下一个节点，实现对当前节点current的删除
        else:  # 如果第一个节点不是特定数据
            previous.set_next(current.get_next())  # 令previous的下一个节点指向current的下一个节点，实现对当前节点current的删除
    
    
    ''' 删除并返回最后一个数据（相当于list的.pop()） '''
    def pop_rear(self):
        current = self.head  # 令current指向表头指向的第一个节点
        previous = None      # 令current的前一个节点previous为 None
        if current == None:  # 如果链表为空
            return None      # 返回None
        else:
            while current.get_next() != None:  # 如果current的下一个节点不为空
                previous = current  # previous前进一步
                current = current.get_next()  # current前进一步
            previous.set_next(current.get_next())  # 当current移动至最后一个节点，
                                                 # 让它的前一个节点 previous 直接指向current的下一节点 None
                                                 # 实现了对最后一个节点的删除
            return current.get_data()  # 返回当前current中的数据
    

mylist = OrderedList()
print(mylist.is_empty())  # >>> True
mylist.add(7)
mylist.add(9)
mylist.add(5)
mylist.add(3)
print(mylist.is_empty())  # >>> False
mylist.traversal()  # >>> 3 5 7 9
mylist.remove(7)
mylist.traversal()  # >>> 3 5 9
print(mylist.size())  # >>> 3
print(mylist.search(9))  # >>> True
print(mylist.search(100))  # >>> False
print(mylist.pop_rear())  # >>> 9
mylist.traversal()  # >>> 3 5