#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 9:08
# @Author  : 一叶知秋
# @File    : layerTraverse.py
# @Software: PyCharm

# 层次遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def layerTraverse(node):
    if not node:
        return None

    queue = [node]
    while queue:
        tmp = queue.pop(0)
        print(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)

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

    layerTraverse(a)
    # res=maxDepth(a)
    # print(res)