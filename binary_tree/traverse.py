#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 13:25
# @Author  : 一叶知秋
# @File    : traverse.py
# @Software: PyCharm
"""
二叉树的所有路径

根节点到叶子节点的所有路径
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse(node):
    if not node.left and not node.right:
        return [str(node.val)]
    left, right = [], []
    if node.left:
        left = [str(node.val) + x for x in traverse(node.left)]
    if node.right:
        right = [str(node.val) + x for x in traverse(node.right)]

    return left + right


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    print(traverse(a))
