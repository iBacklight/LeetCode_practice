"""
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal_recur(root: Optional[TreeNode]) -> List[int]:
        seq = []
        
        def recur_tree(node):
            if node:
                recur_tree(node.left)
                seq.append(node.val)
                recur_tree(node.right)
        recur_tree(root)

        return seq

def inorderTraversal_iteration(root: Optional[TreeNode]) -> List[int]:
        stack = []
        seq = []
        cur_node = root


        while cur_node or stack: # 当前节点为空，或者栈弹出了所有的节点

            while cur_node: # 遍历左边节点
                stack.append(cur_node)
                cur_node = cur_node.left
            
            # 跳出左边，ind在当前节点
            cur_node = stack.pop()
            seq.append(cur_node.val) # 只在左边回到根节点的时候记录是中序遍历的要求
            # stack.append(cur_node)
            cur_node = cur_node.right
        
        return seq