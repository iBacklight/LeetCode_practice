"""
93. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

 

示例 1：

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # 直接剪枝
    if not head or left == right:
        return head
    # 用哨兵节点，否则处理不了 left=1
    dummy = ListNode(0, head)
    pre = dummy # pre 是left节点的前节点
    n = right - left

    for _ in range(left-1):
        pre = pre.next

    prev, curr = None, pre.next # curr指向left节点
    # tail锁定现节点，也是反转后的尾部
    # 这里tail只指向地址，只要节点变了它也会变（区分curr和节点）
    tail = curr

    # 这里需要循环n+1次，因为left到right共有right-left+1个节点
    for _ in range(n+1):
        temp = curr.next
        # tail会在这里做一次改变，只做一次
        curr.next = prev
        prev = curr
        # 注意，这个时候curr要和原来的tail节点脱钩
        # 所以以后curr的变化不会引起tail变化
        curr = temp

    # 把两端的节点接回反转后的链表
    tail.next = curr
    pre.next = prev

    return dummy.next