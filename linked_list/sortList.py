#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 思路：归并排序，找中点和合并操作
        return self.mergeSort(head)

    def mergeSort(self, head):
        # 如果只有一个节点直接就返回这个节点
        if head is None or head.next is None:
            return head

        # find middle
        middle = self.findMiddle(head)
        # 断开中间节点
        tail = middle.next
        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(tail)
        result = self.mergeTwoLists(left, right)
        return result

    def findMiddle(self, head):
        #  1->2->3->4->5
        slow = head
        fast = head.next
        # 快指针先为nil
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        # 连接l1 未处理完节点
        if l1:
            head.next = l1
        else:
            # 连接l2 未处理完节点
            head.next = l2
        return dummy.next

# 注意点

# 快慢指针 判断 fast 及 fast.Next 是否为 nil 值
# 递归 mergeSort 需要断开中间节点
# 递归返回条件为 head 为 nil 或者 head.Next 为 nil