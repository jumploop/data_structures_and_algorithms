#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 21:46
# @Author  : 一叶知秋
# @File    : levelOrder.py
# @Software: PyCharm

"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
# 思路：用一个队列记录一层的元素，然后扫描这一层元素添加下一层元素到队列（一个数进去出来一次，所以复杂度 O(logN)）
#

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = [root]
        while len(queue) > 0:
            stack = []
            length = len(queue)
            for i in range(length):
                level = queue.pop(0)
                stack.append(level.val)
                if level.left:
                    queue.append(level.left)
                if level.right:
                    queue.append(level.right)
            result.append(stack)
        return result

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:

        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    print(Solution().levelOrder(a))
