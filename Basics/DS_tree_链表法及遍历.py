class BinaryTree:
    
    def __init__(self, root):
        ''' 初始化二叉树 '''
        self.key = root
        self.leftChild = None  # “左树根 ” 设为 None（注意左树根不是一个节点，它指向左子树的第一个节点）
        self.rightChild = None # “右树根 ” 设为 None（注意右树根不是一个节点，它指向右子树的第一个节点）
    
    def insertLeft(self, newNode):
        ''' 插入左子树 '''
        t = BinaryTree(newNode)  # 让新节点产生二叉树 t
        if self.leftChild == None:  # 如果左树根为None，即左子树为空
            self.leftChild = t   # 让左树根指向 t
        else:  # 如果左子树不为空 
            t.leftChild = self.leftChild    # 把二叉树 t 指向左树根当前指向的第一个子树
            self.leftChild = t   # 然后把左树根指向 t，这样一来，t 就成了左树根指向的第一个子树
    
    def insertRight(self, newNode):
        ''' 插入右子树 '''
        t = BinaryTree(newNode)  # 让新节点产生二叉树 t
        if self.rightChild == None:  # 如果右树根为None，即右子树为空
            self.rightChild = t  # 让右树根指向 t
        else:  # 如果右子树不为空 
            t.rightChild = self.rightChild  # 把二叉树 t 指向左树根当前指向的第一个子树
            self.rightChild = t  # 然后把右树根指向 t，这样一来，t 就成了右树根指向的第一个子树
    
    def getRootVal(self):
        ''' 查看根节点 '''
        return self.key
    
    def setRootVal(self, obj):
        ''' 修改根节点 '''
        self.key = obj
    
    def getRightChild(self):
        ''' 查看左子树 '''
        return self.rightChild
    
    def getLeftChild(self):
        ''' 查看右子树 '''
        return self.leftChild

    
""" 遍历：对一个数据集中的所有数据项进行访问 """
def preorder(tree):
    ''' 前序遍历：先访问根节点，再递归地前序访问左子树、最后前序访问右子树 '''
    if tree:
        print(tree.getRootVal(), end=' ')
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    

def inorder(tree):
    ''' 中序遍历：先递归地中序访问左子树，再访问根节点，最后中序访问右子树 '''
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal(),  end=' ')
        inorder(tree.getRightChild())
        
def postorder(tree):
    ''' 后序遍历：先递归地后序访问左子树，再后序访问右子树，最后访问根节点 '''
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), end=' ')

        

mytree = BinaryTree(1)
print(mytree.getRootVal()) # >>> 1
mytree.setRootVal('hello')
print(mytree.getRootVal()) # >>> hello
mytree.insertLeft(2)
mytree.insertLeft(3)
mytree.insertRight(4)
mytree.insertRight(5)
preorder(mytree)   # >>> hello 3 2 5 4 
inorder(mytree)    # >>> 2 3 hello 5 4 
postorder(mytree)  # >>> 2 3 4 5 helloclass BinaryTree:
    
    def __init__(self, root):
        ''' 初始化二叉树 '''
        self.key = root
        self.leftChild = None  # “左树根 ” 设为 None（注意左树根不是一个节点，它指向左子树的第一个节点）
        self.rightChild = None # “右树根 ” 设为 None（注意右树根不是一个节点，它指向右子树的第一个节点）
    
    def insertLeft(self, newNode):
        ''' 插入左子树 '''
        t = BinaryTree(newNode)  # 让新节点产生二叉树 t
        if self.leftChild == None:  # 如果左树根为None，即左子树为空
            self.leftChild = t   # 让左树根指向 t
        else:  # 如果左子树不为空 
            t.leftChild = self.leftChild    # 把二叉树 t 指向左树根当前指向的第一个子树
            self.leftChild = t   # 然后把左树根指向 t，这样一来，t 就成了左树根指向的第一个子树
    
    def insertRight(self, newNode):
        ''' 插入右子树 '''
        t = BinaryTree(newNode)  # 让新节点产生二叉树 t
        if self.rightChild == None:  # 如果右树根为None，即右子树为空
            self.rightChild = t  # 让右树根指向 t
        else:  # 如果右子树不为空 
            t.rightChild = self.rightChild  # 把二叉树 t 指向左树根当前指向的第一个子树
            self.rightChild = t  # 然后把右树根指向 t，这样一来，t 就成了右树根指向的第一个子树
    
    def getRootVal(self):
        ''' 查看根节点 '''
        return self.key
    
    def setRootVal(self, obj):
        ''' 修改根节点 '''
        self.key = obj
    
    def getRightChild(self):
        ''' 查看左子树 '''
        return self.rightChild
    
    def getLeftChild(self):
        ''' 查看右子树 '''
        return self.leftChild

    
""" 遍历：对一个数据集中的所有数据项进行访问 """
def preorder(tree):
    ''' 前序遍历：先访问根节点，再递归地前序访问左子树、最后前序访问右子树 '''
    if tree:
        print(tree.getRootVal(), end=' ')
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    

def inorder(tree):
    ''' 中序遍历：先递归地中序访问左子树，再访问根节点，最后中序访问右子树 '''
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal(),  end=' ')
        inorder(tree.getRightChild())
        
def postorder(tree):
    ''' 后序遍历：先递归地后序访问左子树，再后序访问右子树，最后访问根节点 '''
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), end=' ')

        

mytree = BinaryTree(1)
print(mytree.getRootVal()) # >>> 1
mytree.setRootVal('hello')
print(mytree.getRootVal()) # >>> hello
mytree.insertLeft(2)
mytree.insertLeft(3)
mytree.insertRight(4)
mytree.insertRight(5)
preorder(mytree)   # >>> hello 3 2 5 4 
inorder(mytree)    # >>> 2 3 hello 5 4 
postorder(mytree)  # >>> 2 3 4 5 hello