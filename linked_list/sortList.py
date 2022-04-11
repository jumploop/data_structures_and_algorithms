#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:40
# @Author  : 一叶知秋
# @File    : sortList.py
# @Software: PyCharm
"""
148. 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# 思路：归并排序，找中点和合并操作

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 如果只有一个节点 直接就返回这个节点
        if not head or not head.next:
            return head
        # find middle
        middle = self.findMiddle(head)
        # 开中间节点
        tail = middle.next
        middle.next = None
        left = self.sortList(head)
        right = self.sortList(tail)
        return self.mergeTwoLists(left, right)

    def findMiddle(self, head):
        # 1->2->3->4->5
        slow, fast = head, head.next
        # 快指针先为nil
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mergeTwoLists(self, l1, l2):
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
        head.next = l1 or l2
        return dummy.next

    def sortList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left or right
        return res.next

    def sortList3(self, head: ListNode) -> ListNode:

        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break  # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next


