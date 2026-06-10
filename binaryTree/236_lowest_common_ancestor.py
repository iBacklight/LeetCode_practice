"""
236. 二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1


medium
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 分别找到p和q的祖先节点，然后从祖先节点中找到最近公共祖先
        from collections import deque

        if root == None:
            return None

        self.add_flag = True    # 用于标记是否找到目标节点
        self.anc_queue = deque([]) # 用于存储祖先节点
        
        def dfs(node, target):
            # 如果节点为空或已经找到目标节点，则提前返回
            if node == None or not self.add_flag: 
                return

            if node.val == target.val:
                self.anc_queue.append(node)
                self.add_flag = False

            if self.add_flag:
                self.anc_queue.append(node)

            dfs(node.left, target)
            dfs(node.right, target)

            if self.add_flag: # 如果没找到目标节点，则将当前节点从祖先节点中移除
                self.anc_queue.pop()
            
            return

        # 分别找到p和q的祖先节点
        dfs(root, p)
        anc_p = self.anc_queue

        self.anc_queue = deque([])
        self.add_flag = True

        dfs(root, q)
        anc_q = self.anc_queue
        common_anc = root

        # 从祖先节点中找到最近公共祖先
        while anc_p and anc_q:
            node_p = anc_p.popleft()
            node_q = anc_q.popleft()
            if node_p.val == node_q.val:
                common_anc = node_p
            else:
                return common_anc

        return common_anc


    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 基准条件：如果撞到空，或者撞到了 p 或 q，直接把当前节点交上去
        if not root or root == p or root == q:
            return root
        
        # 顺着左、右子树往下搜
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 【核心归纳判断】
        if left and right: 
            return root  # 如果左右子树都有收获，说明 p 和 q 分居两侧，当前节点就是最近公共祖先！
            
        return left if left else right  # 如果只有一边有收获，把那个收获顺着竹竿传上去