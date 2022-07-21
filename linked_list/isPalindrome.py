"""
234. 回文链表

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 请判断一个链表是否为回文链表。
    def isPalindrome(self, head: ListNode) -> bool:
        #  1 2 nil
        #  1 2 1 nil
        #  1 2 2 1 nil
        if head is None:
            return True
        slow = head
        # fast如果初始化为head.Next则中点在slow.Next
        #  fast初始化为head,则中点在slow
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = self.reverse(slow.next)
        # 断开两个链表(需要用到中点前一个节点)
        slow.next = None
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True

    def reverse(self, head):
        # 1->2->3
        if head is None:
            return head
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre