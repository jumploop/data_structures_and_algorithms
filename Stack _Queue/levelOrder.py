#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 18:35
# @Author  : 一叶知秋
# @File    : levelOrder.py
# @Software: PyCharm
"""
二叉树层次遍历

"""
from typing import List
from collections import deque


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
        queue = deque([root])
        while queue:
            stack = []
            length = len(queue)
            for _ in range(length):
                level = queue.popleft()
                stack.append(level.val)
                if level.left:
                    queue.append(level.left)
                if level.right:
                    queue.append(level.right)
            result.append(stack)
        return result


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    print(Solution().levelOrder(a))
