"""
234. 回文链表

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

示例 1：

输入：head = [1,2,2,1]
输出：true
示例 2：

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    vals = []
    dummy = head
    while dummy:
        vals.append(dummy.val)
        dummy = dummy.next

    return vals == vals[::-1] # [start:stop:step]

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # 递归
    left = head

    def is_pal(right: Optional[ListNode]) -> bool:
        # 「递」，先把 right 移到链表末尾
        if right.next and not is_pal(right.next):
            return False
        # 「归」的过程就是在从右到左遍历链表
        nonlocal left # 声明当前子函数内部的 left 变量不是局部变量，而是属于它外层（嵌套它）的那层函数的变量。
        if left.val != right.val:
            return False
        left = left.next  # left 往右走
        return True  # 归，right 会往左走

    return is_pal(head)


def isPalindrome(self, head: Optional[ListNode]) -> bool:
    import copy
    prev,curr = None, head
    dummy = copy.deepcopy(head)
	# 反转链表
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    while prev and dummy:
        if prev.val != dummy.val:
            return False  # 判定不相等
        # 同步执行重新赋值
        prev = prev.next
        dummy = dummy.next

    return True
