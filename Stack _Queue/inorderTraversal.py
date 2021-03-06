#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 18:41
# @Author  : 一叶知秋
# @File    : inorderTraversal.py
# @Software: PyCharm
"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

# 思路：通过stack 保存已经访问的元素，用于原路返回
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if not root:
            return result
        while stack or root:
            while root:
                stack.append(root)
                root = root.left  # 一直向左
            # 弹出
            node = stack.pop()
            result.append(node.val)
            root = node.right
        return result

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        stack, result = [], []
        node = root

        while len(stack) > 0 or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result


if __name__ == '__main__':
    a = TreeNode(4)
    b = TreeNode(3)
    c = TreeNode(5)
    a.left = b
    a.right = c
    print(Solution().inorderTraversal(a))
