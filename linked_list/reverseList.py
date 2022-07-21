"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        # 思路：用一个 prev 节点保存向前指针，temp 保存向后的临时指针
        # 将当前结点放置到头结点
        prev = None
        while head:
            # 保存当前head.Next节点，防止重新赋值后被覆盖
            temp = head.next
            head.next = prev
            # pre 移动
            prev = head
            # head 移动
            head = temp
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:

        if head is None:
            return head
        tail = head
        while tail.next:
            # put tail.next to head
            tmp = tail.next
            tail.next = tail.next.next
            tmp.next = head
            head = tmp

        return head