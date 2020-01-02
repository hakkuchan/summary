""" 嵌套列表法
    
    · 本节利用嵌套列表法实现二叉树，其方法可推广至多叉树
    
    · 二叉树中的每个节点（除叶节点）都有两个子节点（Left，Right）
    
"""

# 例：
class BinaryTree:
       
    def __init__(self, root):
        # 初始化二叉树
        self.root = root
        self.tree = [self.root, [], []]

    def insertLeft(self, newBranch):
        # 插入左子树
        t = self.tree.pop(1)  # 取出左子树
        if len(t) > 1:  # 如果左子树不为空
            self.tree.insert(1, [newBranch, t, []])   # 把新节点插入根节点与当前左子树之间（画出树图便于理解）
        else:  # 如果左子树为空
            self.tree.insert(1, [newBranch, [], []])  # 把新节点 [newBranch, [], []] 插入为左子树
        return self.tree

    def insertRight(self, newBranch):
        # 插入右子树
        t = self.tree.pop(2)
        if len(t) > 1:
            self.tree.insert(2, [newBranch, [], t])
        else:
            self.tree.insert(2, [newBranch, [], []])
        return self.tree
    
    def travel(self):
        # 查看树
        return self.tree
    
    def getLeftChild(self):
        # 获取左子树
        return self.tree[1]
    
    def getRightChild(self):
        # 获取右子树
        return self.tree[2]


mytree = BinaryTree(1)
mytree.insertLeft(2)
mytree.insertLeft(3)
mytree.insertRight(4)

print(mytree.travel())
print(mytree.getLeftChild())
print(mytree.getRightChild())