"""
98. 验证二叉搜索树

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效二叉搜索树定义如下：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

注意：除了存储值的大小关系，还需要存储每个节点的上下界，确保每个节点都在其上下界之间。
因为BST是所有的左子树都小于根节点，所有的右子树都大于根节点。这个根节点每递归一次，其上下界就会更新。

medium
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        if not root:
            return False

        highest = float('inf')
        lowest = float('-inf')
        queue = deque([(root, lowest, highest)])

        while queue:
            node, lowest, highest = queue.popleft()
            if not (lowest < node.val < highest): # None is impossible
                return False
            
            if node.left:
                queue.append((node.left, lowest, node.val))# there is no lower bound for left part

            if node.right:
                queue.append((node.right, node.val, highest)) # there is no upper bound for right part

        
        return True