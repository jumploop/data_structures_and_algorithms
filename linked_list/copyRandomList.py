#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 19:27
# @Author  : 一叶知秋
# @File    : copyRandomList.py
# @Software: PyCharm
"""
138. 复制带随机指针的链表
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。


示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。

提示：
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
"""

"""
# Definition for a Node.
"""


# 思路：1、hash 表存储指针，2、复制节点跟在原节点后面

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        # 复制节点，紧挨到到后面
        # 1->2->3  ==>  1->1'->2->2'->3->3'
        cur = head
        while cur:
            clone = Node(cur.val, cur.next)
            tmp = cur.next
            cur.next = clone
            cur = tmp
        # 处理random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 分离两个链表
        cur = head
        cloneHead = cur.next
        while cur and cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            cur = tmp
        # 原始链表头：head 1->2->3
        # 克隆的链表头：cloneHead 1'->2'->3'
        return cloneHead

    def copyRandomList2(self, head: 'Node') -> 'Node':
        lookup = {}

        def dfs(head):
            if not head:
                return head
            if head in lookup:
                return lookup[head]
            clone = Node(head.val, None, None)
            lookup[head] = clone
            clone.next, clone.random = dfs(head.next), dfs(head.random)
            return clone

        return dfs(head)
