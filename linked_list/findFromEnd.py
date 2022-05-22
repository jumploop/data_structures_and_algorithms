# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def findFromEnd(self, head: ListNode, k: int) -> ListNode:
        """返回链表的倒数第 k 个节点"""
        p1 = head
        # p1 先走 k 步
        for _ in range(k):
            p1 = p1.next
        p2 = head
        #  p1 和 p2 同时走 n - k 步
        while p1 != None:
            p2 = p2.next
            p1 = p1.next
        # p2 现在指向第 n - k 个节点
        return p2