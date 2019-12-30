""" 1. 单向链表（Single-Linked List）

    · 单向链表由若干个节点组成，每个节点包含 信息 和 指针：
      信息即节点包含的数据对象，
      指针从当前节点指向下一节点，
      链表中最后一个节点的指针指向空值，
      对单向链表的访问要通过从头部开始，依序往下读取
    
    · 链表中数据前后位置的保持，是通过指针实现的，并不要求数据存放在连续的存储空间
"""



""" 2. 实现单向链表 """

''' 创建节点类 '''
class Node: 
    def __init__(self, info):
        self.info = info     # 信息：存放数据
        self.pointer = None  # 指针：指向上一个节点，默认为 None
        
        
''' 创建单向链表类 '''
class SingleLinkedList:
    
    ''' 初始化单向链表，头节点(self.head)设置为 None '''
    def __init__(self):
        self.head = None
    
    ''' 从表首加入数据 data '''
    def addFront(self, data):
        node = Node(data)  # 实例化节点
        if self.head == None:  # 如果当前头节点为 None，说明是空链表
            self.head = node   # 把当前头节点指向刚实例化的节点
        else: # 如果当前头节点不为 None
            node.pointer = self.head # 令刚实例化的节点指向头节点（上一个节点）的内存位置
            self.head = node         # 令当前头节点指向刚实例化的节点（新节点 → 头节点）
    
    ''' 从表尾加入数据 data '''
    def addTail(self, data):
        node = Node(data)  # 实例化节点
        if self.head == None:  # 如果当前头节点为 None，说明是空链表
            self.head = node   # 把当前头节点指向刚实例化的节点
        else: # 如果当前链表不为空
            cursor = self.head     # 令游标 cursor 指向当前头节点
            while cursor.pointer != None:  # 如果当前游标所指的下一个节点不是 None
                cursor = cursor.pointer    # 是 cursor 不断指向下一个节点
            cursor.pointer = node  # 当游标 cursor 的下个节点变成 None 时，让它指向刚实例化的节点
    
    ''' 判断链表是否为空 '''
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    ''' 返回链表中元素个数 '''
    def length(self):
        count = 0
        cursor = self.head    # 设置一个游标，指向头节点所处的位置
        while cursor != None: # 如果头节点不为 None
            count += 1  # 计数
            cursor = cursor.pointer # 游标指向下一个节点
        return count
    
    ''' 遍历 '''
    def travel(self):
        cursor = self.head    # 使游标指向头节点
        while cursor != None: # 只要当前游标不为空
            print(cursor.info, end=' ')  # 打印当前节点的信息
            cursor = cursor.pointer  # 游标指向下一节点
        print()
    
    ''' 查找某个数据对象是否在链表中 '''
    def search(self, data):
        cursor = self.head     # 让游标指向当前头节点 
        while cursor != None:  # 如果当前游标不是 None 
            if cursor.info == data:  # 检查当前节点的信息是否匹配
                return True 
            else:
                cursor = cursor.pointer    # 如不匹配，让游标移动至下一个节点
        return False
    
    ''' 删除特定数据的第一个符合值 '''
    def remove(self, data):
        if self.is_empty(): # 若链表为空，直接返回
            return
        cursor1 = None      # 设置 游标-1 为 None
        cursor2 = self.head # 令 游标-2 为当前头节点
 
        while cursor2 != None:  # 只要游标-2不为空
            if cursor2.info != data:      # 如果游标-2的信息不匹配
                cursor1 = cursor2         # 游标-1 指向 游标-2
                cursor2 = cursor2.pointer # 游标-2 指向下一个节点
            else:  # 如果 游标-2 的信息匹配
                if cursor2 == self.head:  # 如果要删除的点是头节点（此时 游标2 指向头节点）
                    self.head = cursor2.pointer  # 让头节点指向 游标2 指向的节点，相当于把当前头节点跳过去，实现了删除
                    break
                else: # 如果要删除的点不是头节点
                    cursor1.pointer = cursor2.pointer  # 让 游标-1指向的节点，指向 游标-2指向的节点，相当于跳过了游标-2
                    break

                    
mylist = SingleLinkedList()
print(mylist.is_empty())  # >>> True
mylist.addFront(5)
mylist.addFront(6)    
mylist.addTail(True)
mylist.addFront(5)    
mylist.travel()  # >>> 5 6 5 True
mylist.remove(5)
mylist.travel()  # >>> 6 5 True
mylist.remove(True)
mylist.travel()  # >>> 6 5
print(mylist.length())     # >>> 2
print(mylist.search(6))    # >>> True
print(mylist.search('a'))  # >>> False