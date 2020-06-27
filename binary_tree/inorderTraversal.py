#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 23:34
# @Author  : 一叶知秋
# @File    : inorderTraversal.py
# @Software: PyCharm

# 中序非递归

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 中序打印二叉树（递归）
def inOrderTraverse(node):
    if node is None:
        return None
    inOrderTraverse(node.left)
    print(node.val)
    inOrderTraverse(node.right)


# 思路：通过stack 保存已经访问的元素，用于原路返回
# 中序打印二叉树（非递归）
def inorderTraversal(node):
    if not node:
        return
    stack = []
    pos = node
    while pos or len(stack) > 0:
        if pos:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            print(pos.val)
            pos = pos.right


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
    inorderTraversal(a)