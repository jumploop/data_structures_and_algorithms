#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 11:23
# @Author  : 一叶知秋
# @File    : preorderTraversal.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal(node):
    """
    前序递归
    :param node:
    :return:
    """
    # if node is None:
    if not node:
        return
    # // 先访问根再访问左右
    print(node.val)
    preorderTraversal(node.left)
    preorderTraversal(node.right)


# 通过非递归遍历
def preorderTraversal2(node):
    """
    前序非递归
    :param root:
    :return:
    """
    if node is None:
        return
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()


def main():
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
    preorderTraversal2(a)


if __name__ == '__main__':
    main()
