#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 11:06
# @Author  : 一叶知秋
# @File    : zigzagLevelOrder.py
# @Software: PyCharm
"""
103. 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = [root]
        toggle = False
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if toggle:
                self.swap(level)
            result.append(level)
            toggle = not toggle
        return result

    def swap(self, level):
        for i in range(len(level) // 2):
            level[i], level[len(level) - 1 - i] = level[len(level) - 1 - i], level[i]

    def zigzagLevelOrder2(self, root):
        nodes = [(root,)]
        values = []
        step = 1
        while nodes:
            values.append([r.val for n in nodes[::step] for r in n[::step] if r])
            # print(values)
            step = -step
            nodes = [(r.left, r.right) for n in nodes for r in n if r]
        return values[:-1]

    def zigzagLevelOrder3(self, root):
        result = []
        if not root:
            return result
        queue = [root]
        depth = 0
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if depth % 2 == 1:
                result.append(level[::-1])
            else:
                result.append(level)
            depth += 1
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
    print(Solution().zigzagLevelOrder2(a))
    print(Solution().zigzagLevelOrder3(a))
