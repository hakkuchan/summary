""" 遍历（Traversal）
    
    · 对一个数据集中的所有数据项进行访问的操作称为“遍历"
    
    · 树的遍历有三种：
      (1) 前序遍历：先访问根节点，再递归地前序访问左子树、最后前序访问右子树
      (2) 中序遍历：先递归地中序访问左子树，再访问根节点，最后中序访问右子树
      (3) 后序遍历：先递归地后序访问左子树，再后序访问右子树，最后访问根节点
"""

def preorder(tree): # 前序遍历
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
def inorder(tree):  # 中序遍历
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
        
def postorder(tree): # 后序遍历
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())