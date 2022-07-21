#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def helper(node):
            # base case
            if node is None:
                return float('-inf')
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(helper(node.left), 0)
            rightGain = max(helper(node.right), 0)
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain
            # 更新答案
            self.maxPath = max(self.maxPath, priceNewpath)
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        helper(root)
        return self.maxPath