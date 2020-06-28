#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 21:22
# @Author  : 一叶知秋
# @File    : deleteDuplicates2.py
# @Software: PyCharm

"""
82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
"""


# 思路：链表头结点可能被删除，所以用 dummy node 辅助删除

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next=head
        head = dummy
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                # 记录已经删除的值，用于后续节点判断
                rmVal = head.next.val
                while head.next and head.next.val == rmVal:
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next

        # 注意点 • A->B->C 删除 B，A.next = C • 删除用一个 Dummy Node 节点辅助（允许头节点可变） • 访问 X.next 、X.value 一定要保证 X != nil
