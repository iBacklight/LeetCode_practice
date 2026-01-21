"""
102. 二叉树的层序遍历

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]
 

提示：

树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000

medium

"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    traverse = []
    if root == None:
        return traverse
    from collections import deque
    queue = deque([root])

    while queue:
        # 分层（每次循环相当于遍历一层）：结果加入当前节点 + 下一层入队
        layer_res = []
        # size 当前层宽度
        size = len(queue)
        for _ in range(size):
            # 从当前层的第一个节点（最先入队的节点）开始遍历
            node = queue.popleft()
            # 层当前节点值加入当前结果
            if node == None:
                continue
            layer_res.append(node.val)

            # 开始将当前节点下的下一层入队
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # 当前层遍历结束；添加当前层结果
        traverse.append(layer_res)

    return traverse