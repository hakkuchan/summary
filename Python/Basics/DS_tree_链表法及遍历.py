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

    
""" 遍历：对一个数据集中的所有数据项进行访问 """
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
mid_traversal(mytree)   # >>> 2 3 hello 5 4 
post_traversal(mytree)  # >>> 2 3 4 5 hello