""" 二叉堆
    
    · 二叉堆 = 完全二叉树 + 堆
      
    · 完全二叉树：叶节点最多只出现在最底层和次底层，且最底层的叶节点都连续集中在左子树，
      每个内部节点都有两个子节点，最多可有1个节点例外
      
    · 堆：上层节点大于/小于下层节点，分别称为最大堆/最小堆
    
    · 二叉堆的重要性质：假如节点索引为 p ，其左子节点索引为 2p，右子节点索引为 2p+1
      基于该性质，二叉堆可以用非嵌套的列表实现，具体如下：
"""

class BinHeap:
    def __init__(self):
        ''' 初始化二叉堆（最小堆） '''
        self.heap_list = [1]  # 根据二叉堆的重要性质，索引 0 处需占位，在之后操作中无用
        self.idx = 0  # 初始化索引
    
    def insert(self, data):
        ''' 插入数据-主函数 '''
        self.heap_list.append(data) # 将数据先放在二叉堆的末尾
        self.idx = self.idx + 1 
        self.flow_up(self.idx)  # 令插入的数据 “上浮 ”，置于合适的位置
    
    def flow_up(self, i):  # 其中，i 对应 self.idx
        ''' 插入数据-上浮函数 '''
        while i // 2 > 0:  # 只要还有父节点
            if self.heap_list[i] < self.heap_list[i//2]: # 与父节点进行对比、交换
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i = i // 2    
    
    def del_min(self):
        ''' 删除根节点-主函数 '''
        remove_head = self.heap_list[1]  # 出队节点
        self.heap_list[1] = self.heap_list[self.idx]  # 令根节点为二叉堆的最后一个节点
        self.idx = self.idx - 1
        self.heap_list.pop()  # 把最后一个节点删除
        self.flow_down(1)  # 令根节点 “下沉 ” 至合理位置 
        return remove_head # 返回出队的节点
    
    def flow_down(self, i):
        ''' 删除根节点-下沉函数 
            该函数使根节点或父节点不断与其左子节点或右子节点对比、交换
        '''
        while (i*2) <= self.idx:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
    
    def min_child(self, i):
        ''' 删除根节点-选择函数
            该函数用于选择较小的子节点，与父节点进行交换
        '''
        if i*2+1 > self.idx:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1
    
    def traverse(self):
        ''' 遍历 '''
        print(self.heap_list[1:])
        
bh = BinHeap()
bh.insert(5)
bh.insert(24)
bh.insert(8)
bh.insert(15)
bh.insert(1)
bh.traverse() # >>> [1, 5, 8, 24, 15]
print(bh.del_min()) # >>> 1
print(bh.del_min()) # >>> 5
print(bh.del_min()) # >>> 8
print(bh.del_min()) # >>> 15
print(bh.del_min()) # >>> 24