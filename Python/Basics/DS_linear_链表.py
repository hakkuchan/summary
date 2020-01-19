""" 链表
    · 链表由若干个节点串联组成，每个节点包含 信息 和 指针：
      信息即节点包含的数据，指针从当前节点指向下一节点，
    
    · 链表中数据前后位置的保持，是通过指针实现的，并不要求数据存放于连续存储空间
"""


''' (1) 创建节点类 '''
class Node:
    def __init__(self, data):
        ''' 初始化节点 '''
        self.data = data  # 把数据传进节点
        self.next = None  # 下一个节点设置为空
    
    def get_data(self):
        ''' 返回节点的数据 '''
        return self.data
    
    def get_next(self):
        ''' 返回下一个节点 '''
        return self.next
    
    def set_data(self, newdata):
        ''' 修改节点数据 '''
        self.data = newdata
    
    def set_next(self, newnext):
        ''' 修改下一个节点 '''
        self.next = newnext

temp = Node(5)
print(temp.get_data())  # >>> 5
print(temp.get_next())  # >>> None
temp.set_data(100)
print(temp.get_data())  # >>> 100
print(temp.get_next())  # >>> None
temp.set_next(1000)
print(temp.get_next())  # >>> 1000


''' (2) 基于链表实现无序表
    
    · 无序表是一种容器，其中数据项按照相对位置存放
      Python 内置的 list 数据类型就是一种无序表 
'''
class UnorderedList:
    def __init__(self):
        ''' 初始化一个空无序表 '''
        self.head = None  # 设置表头，默认为 None（注意：表头本身不是节点，而是指向链表中的第一个节点）
    
    def is_empty(self):
        ''' 判断链表是否为空 '''
        return self.head == None
    
    def add_head(self, data):
        ''' 在表首增加节点 '''
        new_node = Node(data)  # 实例化一个新node
        new_node.set_next(self.head)  # 令新node指向表头当前所指向的第一个节点
        self.head = new_node   # 把表头指向新node，如此一来，新node就成了第一个节点
    
    def add_tail(self, data):
        ''' 在表尾增加节点 '''
        new_node = Node(data)  # 实例化一个新node
        if self.head == None:  # 如果表头指向空（说明是空链表）
            self.head = new_node  # 把表头指向新node
        else: # 如果不是空列表
            current = self.head   # 令current指向表头指向的第一个节点
            while current.get_next() != None: # 只要current的下一个节点不是None
                current = current.get_next()  # 令current指向下一节点
            current.set_next(new_node)  # 当current的下一个节点为None时，将current的下一个节点设定为新node
            
    def traverse(self):
        ''' 遍历 '''
        current = self.head    # 令current指向表头指向的第一个节点
        while current != None:
            print(current.get_data(), end=' ')  # 输出当前节点的信息
            current = current.get_next()        # current指向下一节点
        print()
        
    def size(self):
        ''' 元素个数 '''
        count = 0
        current = self.head    # 令current指向表头指向的第一个节点
        while current != None: # 只要current不为 None
            count += 1         # 计数
            current = current.get_next() # current指向下一节点
        return count
    
    def search(self, data):
        ''' 查找特定元素 '''
        current = self.head   # 令current指向表头指向的第一个节点
        found = False         # 假定 “未找到特定元素”
        while current != None and not found:   # 只要表不为空且 “未找到特定元素” 为真
            if current.get_data() == data:     # 检查当前current是否与待查数据匹配
                found = True  # 如果匹配，令 found = True，跳出循环
            else:
                 current = current.get_next()  # 如不匹配，current指向下一节点
        return found
    
    def remove(self, data):
        ''' 删除特定数据 '''
        current = self.head  # 令current指向表头指向的第一个节点
        previous = None      # 令current的前一个节点previous为 None
        found = False        # 假定未找到需删除的数据
        while current != None and not found:  # 只要表不为空且 “未找到特定数据” 为真
            if current.get_data() == data:    # 检查当前节点是不是特定数据
                found = True  # 如是，跳出循环
            else:  # 如不是，current 和 previous依次向后移动：
                previous = current # previous 指向 current
                current = current.get_next() # current 指向下一个节点
        # 当找到了待删除的特定数据
        if previous == None:  # 如果第一个节点就是特定数据
            self.head = current.get_next()  # 直接把表头指向current的下一个节点，实现对当前节点current的删除
        else:  # 如果第一个节点不是特定数据
            previous.set_next(current.get_next())  # 令previous的下一个节点指向current的下一个节点，实现对当前current节点的删除
    
    def pop_tail(self):
        ''' 删除并返回最后一个数据 '''
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
        

mylist = UnorderedList()
print(mylist.is_empty())  # >>> True
mylist.add_head(3)
mylist.add_head(2)
mylist.add_head(1)
mylist.add_tail('hello')
mylist.add_tail('world')
print(mylist.is_empty())  # >>> False
print(mylist.size())      # >>> 5
mylist.traverse()  # >>> 1 2 3 hello world 
print(mylist.search(1))   # >>> True
print(mylist.search(100)) # >>> False
mylist.remove('hello')
mylist.traverse()  # >>> 1 2 3 world 
print(mylist.pop_tail()) # >>> world
mylist.traverse()  # >>> 1 2 3


''' (3) 基于链表实现有序表（Ordered list）
    
    · 有序表是一种容器，表中数据依照某可比性质（如整数大小、字母先后）排序
'''
class OrderedList:
    def __init__(self):
        ''' 初始化一个空有序表 '''
        self.head = None  # 设置表头，默认为 None（注意：表头本身不是节点，而是指向链表中的第一个节点）
    
    def add(self, item):
        ''' 在表中增加节点 ——— 按照顺序添加 '''
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
        
    def search(self, item):
        ''' 查找特定元素 '''
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
        
    def is_empty(self):
        ''' 判断链表是否为空 '''
        return self.head == None
    
    def traverse(self):
        ''' 遍历 '''
        current = self.head    # 令current指向表头指向的第一个节点
        while current != None:
            print(current.get_data(), end=' ')  # 打印当前节点的信息
            current = current.get_next()        # current指向下一节点
        print()
    
    
    ''' 元素个数 '''
    def size(self):
        current = self.head    # 令current指向表头指向的第一个节点
        count = 0
        while current != None: # 只要current不为 None
            count += 1         # 计数
            current = current.get_next() # current指向下一节点
        return count
    

    ''' 删除特定数据 '''
    def remove(self, data):
        current = self.head  # 令current指向表头指向的第一个节点
        previous = None      # 令current的前一个节点previous为 None
        found = False        # 假定未找到需删除的特定数据
        while current != None and not found:  # 只要表不为空且 “未找到特定数据” 为真
            if current.get_data() == data: # 检查当前节点是不是特定数据
                found = True  # 如是，说明找到了
            else:  # 如不是，current和previous依次向后移动：
                previous = current # previous 指向 current
                current = current.get_next() # current 指向下一个节点
        # 当找到了待删除的特定数据
        if previous == None:  # 如果第一个节点就是特定数据
            self.head = current.get_next()  # 直接把表头指向current的下一个节点，实现对当前节点current的删除
        else:  # 如果第一个节点不是特定数据
            previous.set_next(current.get_next())  # 令previous的下一个节点指向current的下一个节点，实现对当前节点current的删除
    
    
    ''' 删除并返回最后一个数据 '''
    def pop_tail(self):
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
mylist.traverse()  # >>> 3 5 7 9
mylist.remove(7)
mylist.traverse()  # >>> 3 5 9
print(mylist.size())  # >>> 3
print(mylist.search(9))  # >>> True
print(mylist.search(100))  # >>> False
print(mylist.pop_tail())  # >>> 9
mylist.traverse()  # >>> 3 5