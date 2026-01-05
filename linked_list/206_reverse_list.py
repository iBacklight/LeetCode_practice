"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList_iteration(head: ListNode) -> ListNode:
        if not head:
                return None
        
        prev = None
        cur = head

        while cur != None:
            temp = cur.next
            cur.next = prev # point to last node
            prev = cur 
            cur = temp # Finally cur point to NOne

        return prev

def reverseList_recur(head: ListNode) -> ListNode:
    """
    Process: 比如输入链表:1 → 2 → 3

        调用 Recur(1)

            先递归到 Recur(2)

                再递归到 Recur(3)

                触发 base case:返回 (3, 3)

            收 (pre=3, last=3)

            执行：

            last.next = head   # 3.next = 2, 把当前节点连到上一个节点
            head.next = None   # 2.next = None, 再假设当前节点为最后一个节点
            return (pre=3, head=2)
            # 此时子链表已经变成 3 → 2

        回到 Recur(1):
        接收 (pre=3, last=2)

        执行：

        last.next = head   # 2.next = 1
        head.next = None   # 1.next = None
        return (pre=3, head=1)
        # 此时链表已经变成 3 → 2 → 1

    最终返回 (3, 1)，新头是 3, 新尾是 1。
    
    """
       
    def Recur(head):
        if head == None or head.next == None:  # base case
            return head, head # 原链表的最后一个节点，也就是是新链表的头节点

        pre, last = Recur(head.next)  # forward
        # ==========================  # backward
        last.next = head              # 把子链表的尾巴连回当前节点
        head.next = None              # 当前节点变成新的尾巴
        return pre, head              # pre: 整体新头; head: 当前尾巴
        
    rt, m = Recur(head)
    return rt

