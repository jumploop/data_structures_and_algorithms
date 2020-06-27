#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 12:27
# @Author  : 一叶知秋
# @File    : maxDepth.py
# @Software: PyCharm


"""
 二叉树的最大深度

基本思路就是递归，当前树的最大深度等于（1+max(左子树最大深度，右子树最大深度)）。代码如下：
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


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

    result = maxDepth(a)
    print(result)
