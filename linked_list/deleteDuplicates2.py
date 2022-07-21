"""
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
"""
# Definition for singly-linked list.
from multiprocessing import dummy


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(next=head)
        head = dummy
        rmval = None
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                # 记录已经删除的值，用于后续节点判断
                rmval = head.next.val
                while head.next and head.next.val == rmval:
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next
