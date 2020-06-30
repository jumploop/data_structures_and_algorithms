#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 0:12
# @Author  : 一叶知秋
# @File    : hasCycle.py
# @Software: PyCharm
"""
141. 环形链表
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。



示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。




进阶：

你能用 O(1)（即，常量）内存解决此问题吗？
"""


# 思路：快慢指针，快慢指针相同则有环，证明：如果有环每走一步快慢指针距离会减 1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            # 比较指针是否相等（不要使用val比较！）
            if fast == slow:
                return True
            slow, fast = slow.next, fast.next.next
        return False
