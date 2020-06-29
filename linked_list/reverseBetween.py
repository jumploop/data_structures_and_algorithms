#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 23:38
# @Author  : 一叶知秋
# @File    : reverseBetween.py
# @Software: PyCharm
"""
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


# 思路：先遍历到 m 处，翻转，再拼接后续，注意指针处理
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        # 头部变化所以使用dummy node
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        # 最开始：0->1->2->3->4->5->nil
        pre = None
        i = 0
        while i < m:
            pre = head
            head = head.next
            i += 1
        # 遍历之后： 1(pre)->2(head)->3->4->5->NULL
        j = i
        next = None
        # 用于中间节点连接
        mid = head
        while head and j <= n:
            # 第一次循环： 1 nil<-2 3->4->5->nil
            temp = head.next
            head.next = next
            next = head
            head = temp
            j += 1
        # 循环需要执行四次
        # 循环结束：1 nil<-2<-3<-4 5(head)->nil
        pre.next = next
        mid.next = head
        return dummy.next

    def reverseBetween2(self, head: ListNode, m: int, n: int) -> ListNode:
            dummy = ListNode(-1)
            dummy.next = head
            pre = dummy
            # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
            for _ in range(m - 1):
                pre = pre.next
            # 用双指针,进行链表翻转
            node = None
            cur = pre.next
            for _ in range(n - m + 1):
                tmp = cur.next
                cur.next = node
                node = cur
                cur = tmp
            # 将翻转部分 和 原链表拼接
            pre.next.next = cur
            pre.next = node
            return dummy.next

