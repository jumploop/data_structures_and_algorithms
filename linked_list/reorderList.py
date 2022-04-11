#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 23:02
# @Author  : 一叶知秋
# @File    : reorderList.py
# @Software: PyCharm
"""
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


# 思路：找到中点断开，翻转后面部分，然后合并前后两个链表
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
        if not head:
            return
        mid = self.findMiddle(head)
        tail = self.reverseList(mid.next)
        mid.next = None
        head = self.mergeTwoLists(head, tail)
        return head

    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def reverseList(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

    def mergeTwoLists(self, l1, l2):
        head = dummy = ListNode(0)
        toggle = True
        while l1 and l2:
            if toggle:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            toggle = not toggle
            head = head.next
        head.next = l1 or l2
        return dummy.next
