#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。
返回 nums 构建的 最大二叉树 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from typing import List
import sys


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, left, right):
        # 定义：将 nums[lo..hi] 构造成符合条件的树，返回根节点
        if left > right:  # base case
            return None
        # 找到数组中的最大值和对应的索引
        index, maxvalue = -1, -sys.maxsize - 1
        i = left
        while i <= right:
            if maxvalue < nums[i]:
                index = i
                maxvalue = nums[i]
            i += 1
        # 先构造出根节点
        root = TreeNode(maxvalue)
        # 递归调用构造左右子树
        root.left = self.build(nums, left, index - 1)
        root.right = self.build(nums, index + 1, right)
        return root
