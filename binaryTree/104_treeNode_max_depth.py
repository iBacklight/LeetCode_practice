"""
104. 二叉树的最大深度

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

 

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：3
示例 2：

输入：root = [1,null,2]
输出：2
 

提示：

树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100

easy
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    max_len = 0

    def dfs(node, cur_len, max_len):
        # terminated condition
        if node == None:
            # 遍历到树的尽头在比较
            max_len = max(max_len, cur_len)
            return max_len
        # 只要不是None就+1
        cur_len += 1
        # 左右树的初始cur_len一样的
        max_len = dfs(node.left, cur_len, max_len)
        max_len = dfs(node.right, cur_len, max_len)

        return max_len

    max_len = dfs(root, 0, 0)
    return max_len