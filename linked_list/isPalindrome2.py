#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)

    def traverse(self, right):
        if right is None:
            return True
        res = self.traverse(right.next)
        # 后序遍历代码
        res=res and right.val==self.left.val
        self.left=self.left.next
        return res
