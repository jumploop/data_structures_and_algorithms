#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 12:27
# @Author  : 一叶知秋
# @File    : maxDepth.py
# @Software: PyCharm


"""
 二叉树的最大深度
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
基本思路就是递归，当前树的最大深度等于（1+max(左子树最大深度，右子树最大深度)）。代码如下：
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return (
            1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            if root
            else 0
        )
        # return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1) if root else 0

    def maxDepth2(self, root: TreeNode) -> int:
        # 思路：分治法
        if not root:
            return 0
        left = self.maxDepth2(root.left)
        right = self.maxDepth2(root.right)
        if left > right:
            return left + 1
        return right + 1


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

    result = Solution().maxDepth(a)
    print(result)
