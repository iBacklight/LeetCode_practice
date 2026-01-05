"""
# 560 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""

from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode_doublepointer(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    让两个指针分别从 headA 和 headB 出发，同时前进。当某个指针走到链表尾部时，不是停下，而是“切换”到另一个链表的头部继续走。

    这样：

        指针 nodeA 实际走过的路径是:m + n

        指针 nodeB 实际走过的路径是:n + m

    两者都走了 m+n 步之后，要么在相交点相遇，要么都走到 None(不相交）。
    """
    if not headA or not headB:   # 边界：有一个空链表，不可能相交
        return None

    nodeA = headA
    nodeB = headB

    while nodeA != nodeB: # 当两个指针还没相遇
        # 如果 nodeA 没走完，就往下走；走完了就切换到 headB
        nodeA = nodeA.next if nodeA else headB
        # 如果 nodeB 没走完，就往下走；走完了就切换到 headA
        nodeB = nodeB.next if nodeB else headA

    return nodeA  # 相遇点（可能是交点节点，也可能是 None）

def getIntersectionNode_hash(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # Store and traverse
    val_rec = {}

    while headA!= None:
        val_rec[headA] = 0
        headA = headA.next

    while headB != None:
        if headB in val_rec:
            return headB
        headB = headB.next

    return headA # or headB, both are None

