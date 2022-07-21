#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 思路：找到中点断开，翻转后面部分，然后合并前后两个链表
        if head is None:
            return head
        mid = self.findMiddle(head)
        tail = self.reverseList(mid.next)
        mid.next = None
        head = self.mergeTwoLists(head, tail)

    def findMiddle(self, head: ListNode):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        head = dummy
        toggle = True
        while l1 and l2:
            # 节点切换
            if toggle:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            toggle = not toggle
            head = head.next
        # 连接l1 未处理完节点
        if l1:
            head.next = l1
        else:
            # 连接l2 未处理完节点
            head.next = l2
        return dummy.next

    def reverseList(self, head: ListNode):
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