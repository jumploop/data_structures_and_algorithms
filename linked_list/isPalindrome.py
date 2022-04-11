#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 10:38
# @Author  : 一叶知秋
# @File    : isPalindrome.py
# @Software: PyCharm
"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
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
        if not head:
            return head
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

    def isPalindrome2(self, head: ListNode) -> bool:
        s = []
        slow = fast = head
        while fast and fast.next:
            s.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while s:
            if slow.val != s.pop():
                return False
            slow = slow.next
        return True

    def isPalindrome3(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
