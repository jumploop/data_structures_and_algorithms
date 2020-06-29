#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 10:02
# @Author  : 一叶知秋
# @File    : mergeTwoLists.py
# @Software: PyCharm
"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# 思路：通过 dummy node 链表，连接各个元素


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
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
        while l1:
            head.next = l1
            head = head.next
            l1 = l1.next
        # 连接l2 未处理完节点
        while l2:
            head.next = l2
            head = head.next
            l2 = l2.next
        return dummy.next
