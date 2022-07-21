#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.valToIndex = {inorder[i]: i for i in range(0, len(inorder))}
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
            return None
        # root 节点对应的值就是前序遍历数组的第一个元素
        rootval = preorder[preStart]
        # rootVal 在中序遍历数组中的索引
        index = self.valToIndex.get(rootval)
        # 左子树的节点数为 leftSize
        leftSize = index - inStart
        # 先构造出根节点
        root = TreeNode(rootval)
        # 递归构造左右子树
        root.left = self.build(preorder, preStart + 1, preStart + leftSize, inorder, inStart, index - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd, inorder, index + 1, inEnd)
        return root
