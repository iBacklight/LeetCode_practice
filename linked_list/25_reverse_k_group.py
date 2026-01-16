"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

示例 1：

输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：

输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

提示：

链表中的节点数目为 n
1 <= k <= n <= 5000
0 <= Node.val <= 1000

hard
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    pre_group_node = dummy
    next_group_node = None

    while True:
        kth = pre_group_node
        # 遍历当前截断组是否有k个节点
        for _ in range(k):
            kth = kth.next
            if kth == None:
                # 不满足k个，直接返回就行
                # 本身pre_group_node就是接在dummy上的
                return dummy.next

        # 下一个组的开头
        next_group_node = kth.next
        # 当前组头节点， 上一组的下一个
        cur_group_start = pre_group_node.next

        # 让 prev 初始化为，这样反转完，新尾巴自动就连上了下一组
        prev = next_group_node # 指向当前组尾节点的下一个
        curr = cur_group_start # 指向当前组头节点

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 把前一组的尾巴，连上本组的新头
        pre_group_node.next = prev

        # 迭代 pre_group_node向前
        pre_group_node = cur_group_start

    return dummy.next