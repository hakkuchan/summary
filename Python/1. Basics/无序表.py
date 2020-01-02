""" 1. 无序表（Unordered list）
    
    · 无序表是一种容器，其中数据项按照相对位置存放的，如第1个、第2个……
      Python 内置的 list 数据类型就是一种无序表
    
    · 无序表可基于链表实现
      链表由若干个节点串联组成，每个节点包含 信息 和 指针：
      信息即节点包含的数据，指针从当前节点指向下一节点，
      链表中数据前后位置的保持，是通过指针实现的，并不要求数据存放在连续的存储空间
"""

''' 例：基于链表创建无序表 '''

''' (1) 创建节点类 '''
class Node:

    ''' 初始化节点 '''
    def __init__(self, initdata):
        self.data = initdata  # 把数据传进节点
        self.next = None      # 下一个节点设置为空
    
    ''' 返回节点的数据 '''
    def getData(self):
        return self.data
    
    ''' 返回节点的下一个节点 '''
    def getNext(self):
        return self.next
    
    ''' 修改节点的数据项 '''
    def setData(self, newdata):
        self.data = newdata
    
    ''' 修改节点的下一个节点 '''
    def setNext(self, newnext):
        self.next = newnext

temp = Node(5)
print(temp.getData())  # >>> 5
print(temp.getNext())  # >>> None
temp.setData(100)
print(temp.getData())  # >>> 100
print(temp.getNext())  # >>> None
temp.setNext(1000)
print(temp.getNext())  # >>> 1000


''' (2) 创建无序表类 '''
class UnorderedList:
    def __init__(self):
        self.head = None  # 设置表头，默认为 None（注意：表头本身不是节点，而是指向链表中的第一个节点）
    
    
    ''' 判断链表是否为空 '''
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    
    ''' 在表首增加节点 ——— 相当于list的 .insert(0,data) '''
    def addFront(self, item):
        new_node = Node(item)  # 实例化一个新node
        new_node.setNext(self.head)  # 令新node指向表头当前所指向的第一个节点
        self.head = new_node   # 把表头指向新node，如此一来，新node就成了第一个节点
    
    
    ''' 遍历 '''
    def travel(self):
        current = self.head    # 令current指向表头指向的第一个节点
        while current != None:
            print(current.getData(), end=' ')  # 打印当前节点的信息
            current = current.getNext()        # current指向下一节点
        print()
    
    
    ''' 元素个数 ——— 相当于list的 len() '''
    def size(self):
        current = self.head    # 令current指向表头指向的第一个节点
        count = 0
        while current != None: # 只要current不为 None
            count += 1         # 计数
            current = current.getNext() # current指向下一节点
        return count
    
    
    ''' 在表尾增加节点 ——— 相当于list的.append() '''
    def addTail(self, item):
        new_node = Node(item)  # 实例化一个新node
        if self.head == None:  # 如果表头指向空（说明是空链表）
            self.head = new_node  # 把表头指向新node
        else: # 如果不是空列表
            current = self.head   # 令current指向表头指向的第一个节点
            while current.getNext() != None: # 只要current的下一个节点不是None
                current = current.getNext()  # 令current指向下一节点
            current.setNext(new_node)  # 当current的下一个节点为None时，将current的下一个节点设定为新node
    
    
    ''' 是否存在特定元素 '''
    def search(self, item):
        current = self.head  # 令current指向表头指向的第一个节点
        found = False  # 假定 “未找到特定元素”
        while current != None and not found:  # 只要表不为空且 “未找到特定元素” 为真
            if current.getData() == item:     # 检查当前current是否与待查数据匹配
                found = True  # 如果匹配，令 found = True，此时 “未找到特定数据” 为假，跳出循环
            else:
                 current = current.getNext()  # 如不匹配，current指向下一节点
        return found
    
    
    ''' 删除特定数据 ——— 相当于list的 .remove() '''
    def remove(self, item):
        current = self.head  # 令current指向表头指向的第一个节点
        previous = None      # 令current的前一个节点previous为 None
        found = False        # 假定未找到需删除的特定数据
        while current != None and not found:  # 只要表不为空且 “未找到特定数据” 为真
            if current.getData() == item: # 检查当前节点是不是特定数据
                found = True  # 如是，说明找到了
            else:  # 如不是，current和previous依次向后移动：
                previous = current # previous 指向 current
                current = current.getNext() # current 指向下一个节点
        # 当找到了待删除的特定数据
        if previous == None:  # 如果第一个节点就是特定数据
            self.head = current.getNext()  # 直接把表头指向current的下一个节点，实现对当前节点current的删除
        else:  # 如果第一个节点不是特定数据
            previous.setNext(current.getNext())  # 令previous的下一个节点指向current的下一个节点，实现对当前节点current的删除
    
    
    ''' 删除并返回最后一个数据（相当于list的.pop()） '''
    def del_re_tail(self):
        current = self.head  # 令current指向表头指向的第一个节点
        previous = None      # 令current的前一个节点previous为 None
        if current == None:  # 如果链表为空
            return None      # 返回None
        else:
            while current.getNext() != None:  # 如果current的下一个节点不为空
                previous = current  # previous前进一步
                current = current.getNext()  # current前进一步
            previous.setNext(current.getNext())  # 当current移动至最后一个节点，
                                                 # 让它的前一个节点 previous 直接指向current的下一节点 None
                                                 # 实现了对最后一个节点的删除
            return current.getData()  # 返回当前current中的数据
    

mylist = UnorderedList()
print(mylist.isEmpty())     # >>> True
mylist.addFront(3)
mylist.addFront(2)
mylist.addFront(1)
mylist.addTail('hello')
mylist.addTail('world')
print(mylist.isEmpty())     # >>> False
print(mylist.size())        # >>> 5
mylist.travel()  # >>> 1 2 3 hello world 

print(mylist.search(1))     # >>> True
print(mylist.search(100))   # >>> False

mylist.remove('hello')
mylist.travel()  # >>> 1 2 3 world 
print(mylist.del_re_tail()) # >>> world
mylist.travel()  # >>> 1 2 3