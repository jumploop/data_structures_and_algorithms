#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
"""


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        # 思路 1：分治法，左边平衡 && 右边平衡 && 左右两边高度 <= 1，
        def depth(root):
            if root is None:
                return 0, True
            depth_left, balance_left = depth(root.left)
            depth_right, balance_right = depth(root.right)
            return max(depth_left,
                       depth_right) + 1, balance_left and balance_right and abs(depth_left - depth_right) < 2

        _, out = depth(root)
        return out

    def isBalanced2(self, root: TreeNode) -> bool:
        if not root: 
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: 
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
