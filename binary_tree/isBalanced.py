#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 17:16
# @Author  : 一叶知秋
# @File    : isBalanced.py
# @Software: PyCharm
"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


# 思路：分治法，左边平衡 && 右边平衡 && 左右两边高度 <= 1， 因为需要返回是否平衡及高度，要么返回两个数据，要么合并两个数据， 所以用-1 表示不平衡，>0 表示树高度（二义性：一个变量有两种含义）。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root:
            return 0
        left = self.recur(root.left)
        if left == -1:
            return -1
        right = self.recur(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

    def isBalanced2(self, root: TreeNode) -> bool:
        # 分治法
        if self.maxDepth(root) == -1:
            return False
        return True

    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # 为什么返回-1呢？（变量具有二义性）
        if left == -1 or right == -1 or left - right > 1 or right - left > 1:
            return -1
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
    res = Solution().isBalanced(a)
    print(res)
