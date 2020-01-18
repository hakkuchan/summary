""" 用嵌套列表法实现二叉树
    
    · 二叉树中的每个节点（除叶节点）都有两个子节点（Left，Right）
    
    · 二叉树结构可推广至多叉树  
"""

# 例：
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