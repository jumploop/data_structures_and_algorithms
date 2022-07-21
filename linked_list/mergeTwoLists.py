#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import dummy
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个有序链表
        :param list1:
        :param list2:
        :return:
        """
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        while list1 and list2:
            # 比较 p1 和 p2 两个指针
            # 将值较小的的节点接到 p 指针
            if list1.val > list2.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next
            # p 指针不断前进
            p = p.next
        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return dummy.next

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail =tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
