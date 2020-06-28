#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 21:58
# @Author  : 一叶知秋
# @File    : reverseList.py
# @Software: PyCharm
"""
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

# 思路：用一个 prev 节点保存向前指针，temp 保存向后的临时指针

# 将当前结点放置到头结点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextNode

    # 解题思路
    # 链表是经典的递归定义的数据结构，链表相关的题目常常考察递归，翻转链表是其中的经典题目。
    # 在思考递归问题的时候，我们要从上到下思考：
    #
    # 子问题是什么
    # base case是什么
    # 在当前层要干什么
    # 对翻转链表来说，以1->2->3->4->5为例：
    # 子问题是：除去current node，翻转剩余链表，即除去1, reverseList(2->3->4->5),递归得到的解是 5->4->3->2
    # base case:当前节点为空，返回空，当前节点的next为空（只剩余一个节点），返回该节点
    # 在当前层要干什么：翻转链表，即把1->2变为2->1.
    # 最后return的是结果链表的头，也就是递归解的头。
    #
    # 作者：ame-9
    # 链接：https://leetcode-cn.com/problems/reverse-linked-list/solution/python3di-gui-jie-fa-zhu-yi-xu-xian-kuang-zai-shui/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    def reverseList2(self, head: ListNode) -> ListNode:
        # 申请两个链表 一个空链表，一个完整的链表
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre # 当前链表指向 新链表
            pre=cur # 赋值给新链表
            cur=temp
        return pre


