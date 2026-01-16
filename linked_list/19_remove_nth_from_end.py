"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。


示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：
输入：head = [1], n = 1
输出：[]
示例 3：
输入：head = [1,2], n = 1
输出：[1]

提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

进阶：你能尝试使用一趟扫描实现吗？

medium
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head == None:
        return head 

    table_s = 0
    node = head
    # 找到链表size
    while node and node.next:
        table_s += 1
        node = node.next

    # 放置哨兵
    # 防止被弹出的是第一个node而找不到前节点
    # 哨兵可以保证任何链表中的node都有前节点以统一逻辑
    dummy = ListNode(0, head)
    count = 0
    node = dummy
    while count <= table_s - n:
        # 找到切断处链表
        count += 1
        node = node.next

    node.next = node.next.next
    return dummy.next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
    "快慢指针法"
    "fast先走n步，然后slow和fast一起走，当fast走到None时，slow走到倒数第n个节点"
    "然后删除slow的下一个节点"
    "返回dummy.next"
    "注意：必须使用哨兵节点，否则处理不了头节点"
    "因为头节点没有前节点，所以无法删除"
    "哨兵节点可以保证任何链表中的node都有前节点以统一逻辑"
    dummy = ListNode(0, head)
    slow = fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next


# 不加哨兵的话，要判断很多边界情况
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head == None:
        return head 

    table_s = 0
    node = head
    while node and node.next:
        table_s += 1
        node = node.next

    count = 0
    node = head
    last_node = None
    while count <= table_s - n:
        count += 1
        last_node = node
        node = node.next
        # print()
        # print(count, node)

    if last_node:
        if node.next:# pop的不是最后一个节点
            last_node.next = node.next
        else: # pop的是最后一个节点
            last_node.next = None
    elif head and head.next:
        head = head.next # pop的是第一个节点
    else:
        return last_node # pop以后链表为空

    return head