#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:57
# @Author  : 一叶知秋
# @File    : deleteDuplicates.py
# @Software: PyCharm

"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        current = head
        while current:
            # 全部删除完再移动到下一个元素
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    a.next = a
    a.next.next = b
    print(Solution().deleteDuplicates(a))
    res = Solution().deleteDuplicates(a)
    while res:
        print(res.val)
        res = res.next
