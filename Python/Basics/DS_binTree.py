""" 1. 树结构概述
    · 树结构以一种分层形式组织数据，比如二叉树
    · 越接近根节点的层越普遍，越接近底部的层越独特
      比如：动物界 → 脊索门 → 哺乳纲 → 食肉目 → 猫科 → 猫属 → 家猫种

    2. 相关术语    
    · 节点（Node）：具有名称（或称为“键值”），可保存额外数据项
    · 边（Edge）：连接节点，表示节点之间具有关联，有入边和出边之分
    · 根（Root）：初始节点
    · 路径（Path）：由边依次连接在一起的节点的有序列表
    · 子节点（Children）：入边均来自于同一个节点的若干节点，称为这个节点的子节点
    · 父节点（Parent）：一个节点是其所有出边所连接节点的父节点
    · 兄弟节点（Sibling）：具有同一个父节点的节点之间称为兄弟节点
    · 子树（Subtree）：一个节点和其所有子孙节点，以及相关边的集合
    · 叶节点（Leaf）：没有子节点的节点称为叶节点
    · 层级（Level）：从根节点开始到达一个节点的路径，所包含的边的数量，称为这个节点的层级，根节点的层级为0
    · 高度：树中所有节点的最大层级称为树的高度

    3. 二叉树
    · 每个节点（除叶节点）都有两个子节点（Left，Right）的树
    · 创建方法：嵌套列表法、链表法
"""

""" (1) 嵌套列表法 """
class BinaryTree:
    def __init__(self, root):
        ''' 初始化二叉树 '''
        self.root = root
        self.tree = [self.root, [], []]  # 总 []中第 1个 []存放左子节点，第 2个存放右子节点
        
    def insert_left(self, newBranch): 
        ''' 插入左子树 '''
        t = self.tree.pop(1)  # 取出左子树
        if len(t) > 1:  # 如果左子树不为空
            self.tree.insert(1, [newBranch, t, []])   # 把新节点插入根节点与当前左子树之间
        else:  # 如果左子树为空
            self.tree.insert(1, [newBranch, [], []])  # 把新子树 [newBranch, [], []] 插入为左子树
        return self.tree
    
    def insert_right(self, newBranch):
        ''' 插入右子树 '''
        t = self.tree.pop(2)
        if len(t) > 1:
            self.tree.insert(2, [newBranch, [], t])   # 把新节点插入根节点与当前右子树之间
        else:
            self.tree.insert(2, [newBranch, [], []])  # 把新子树 [newBranch, [], []] 插入为右子树
        return self.tree
    
    def traversal(self):
        ''' 查看树 '''
        return self.tree
    
    def get_left(self):
        ''' 获取左子树 '''
        return self.tree[1]
    
    def get_right(self):
        ''' 获取右子树 '''
        return self.tree[2]

mytree = BinaryTree(1)  # 初始化根节点为 1 的二叉树
print(mytree.traversal())  # >>> [1, [], []]
mytree.insert_left(2)    # 插入左子树 [2, [], []]
print(mytree.traversal())  # >>> [1, [2, [], []], []]
mytree.insert_left(3)    # 插入左子树 [3, [], []]
print(mytree.traversal())  # >>> [1, [3, [2, [], []], []], []]
mytree.insert_right(4)   # 插入右子树 [4, [], []]
print(mytree.traversal())  # >>> [1, [3, [2, [], []], []], [4, [], []]]
print(mytree.get_left())  # >>> [3, [2, [], []], []]
print(mytree.get_right()) # >>> [4, [], []]


""" (2) 链表法 """
class BinaryTree:
    def __init__(self, root):
        ''' 初始化二叉树 '''
        self.key = root
        self.leftChild = None  # “左树根 ” 设为 None（注意左树根不是一个节点，它指向左子树的第一个节点）
        self.rightChild = None # “右树根 ” 设为 None（注意右树根不是一个节点，它指向右子树的第一个节点）
    
    def insert_left(self, newNode):
        ''' 插入左子树 '''
        t = BinaryTree(newNode)  # 让新节点产生二叉树 t
        if self.leftChild == None:  # 如果左树根为None，即左子树为空
            self.leftChild = t   # 让左树根指向 t
        else:  # 如果左子树不为空 
            t.leftChild = self.leftChild    # 把二叉树 t 指向左树根当前指向的第一个子树
            self.leftChild = t   # 然后把左树根指向 t，这样一来，t 就成了左树根指向的第一个子树
    
    def insert_right(self, newNode):
        ''' 插入右子树 '''
        t = BinaryTree(newNode)  # 让新节点产生二叉树 t
        if self.rightChild == None:  # 如果右树根为None，即右子树为空
            self.rightChild = t  # 让右树根指向 t
        else:  # 如果右子树不为空 
            t.rightChild = self.rightChild  # 把二叉树 t 指向左树根当前指向的第一个子树
            self.rightChild = t  # 然后把右树根指向 t，这样一来，t 就成了右树根指向的第一个子树
    
    def get_root(self):
        ''' 查看根节点 '''
        return self.key
    
    def set_root(self, obj):
        ''' 修改根节点 '''
        self.key = obj
    
    def get_right(self):
        ''' 查看左子树 '''
        return self.rightChild
    
    def get_left(self):
        ''' 查看右子树 '''
        return self.leftChild

    
""" (3) 遍历：对一个数据集中的所有数据项进行访问 """
def pre_traversal(tree):
    ''' 前序遍历：先访问根节点，再递归地前序访问左子树、最后前序访问右子树 '''
    if tree:
        print(tree.get_root(), end=' ')
        pre_traversal(tree.get_left())
        pre_traversal(tree.get_right())

def mid_traversal(tree):
    ''' 中序遍历：先递归地中序访问左子树，再访问根节点，最后中序访问右子树 '''
    if tree:
        mid_traversal(tree.get_left())
        print(tree.get_root(),  end=' ')
        mid_traversal(tree.get_right())
        
def post_traversal(tree):
    ''' 后序遍历：先递归地后序访问左子树，再后序访问右子树，最后访问根节点 '''
    if tree:
        post_traversal(tree.get_left())
        post_traversal(tree.get_right())
        print(tree.get_root(), end=' ')

mytree = BinaryTree(1)
print(mytree.get_root()) # >>> 1
mytree.set_root('hello')
print(mytree.get_root()) # >>> hello
mytree.insert_left(2)
mytree.insert_left(3)
mytree.insert_right(4)
mytree.insert_right(5)
pre_traversal(mytree)   # >>> hello 3 2 5 4
print()
mid_traversal(mytree)   # >>> 2 3 hello 5 4 
print()
post_traversal(mytree)  # >>> 2 3 4 5 hello