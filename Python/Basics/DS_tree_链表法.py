class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None  # “左树根 ” 设为 None（注意左树根不是一个节点，它指向左子树的第一个节点）
        self.rightChild = None # “右树根 ” 设为 None（注意右树根不是一个节点，它指向右子树的第一个节点）
    
    def insertLeft(self, newNode):
        ''' 插入左节点 '''
        if self.leftChild == None:  # 如果左树根为None，即左子树未空
            self.leftChild = BinaryTree(newNode)  # 直接让左树根指向新节点
        else:  # 如果左子树不为空
            t = BinaryTree(newNode)  # 让新节点产生二叉树 t
            t.leftChild = self.leftChild  # 然后把新节点产生的二叉树 t 指向左树根当前指向的第一个节点
            self.leftChild = t  # 然后把左树根指向 t，这样一来，t 就成了左树根指向的第一个节点
    
    def insertRight(self, newNode):
        ''' 插入右节点 '''
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChildChild = self.rightChild
            self.rightChild = t
    
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
    

mytree = BinaryTree('a')  # >>> 根节点为 'a'
mytree.insertLeft('b')    # >>> 左节点为 'b'
mytree.insertRight('c')   # >>> 右节点为 'c'
mytree.getRightChild().setRootVal('hello')  # >>> 右节点设为'hello'