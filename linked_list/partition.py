#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 10:43
# @Author  : 一叶知秋
# @File    : partition.py
# @Software: PyCharm
"""
86. 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""


# 思路：将大于 x 的节点，放到另外一个链表，最后连接这两个链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # check
        if not head:
            return head
        headDummy = ListNode(0)
        tailDummy = ListNode(0)
        tail = tailDummy
        headDummy.next = head
        head = headDummy
        while head.next:
            if head.next.val < x:
                head = head.next
            else:
                # 移除<x节点
                t = head.next
                head.next = head.next.next
                # 放到另外一个链表
                tail.next = t
                tail = tail.next
        # 拼接两个链表
        tail.next = None
        head.next = tailDummy.next
        return headDummy.next

    def partition2(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next
