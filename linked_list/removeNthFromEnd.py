# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """19. 删除链表的倒数第 N 个结点"""
        # 虚拟头节点
        dummy = ListNode(-1)
        dummy.next = head
        # 删除倒数第 n 个，要先找倒数第 n + 1 个节点
        x = self.findFromEnd(dummy, n + 1)
        # 删掉倒数第 n 个节点
        x.next = x.next.next
        return dummy.next

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