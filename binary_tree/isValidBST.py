#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 12:44
# @Author  : 一叶知秋
# @File    : isValidBST.py
# @Software: PyCharm
""""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""
from collections import namedtuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 思路 1：中序遍历，检查结果列表是否已经有序
        result = []
        self.inOrder(root, result)
        print(result)
        return all(result[i] < result[i + 1] for i in range(len(result) - 1))

    def inOrder(self, root, result):
        if not root:
            return
        self.inOrder(root.left, result)
        result.append(root.val)
        self.inOrder(root.right, result)

    def isValidBST2(self, root: TreeNode) -> bool:
        def dfs(root, min_val, max_val):
            if not root:  # 边界条件，如果node为空肯定是二叉搜索树
                return True
            if not min_val < root.val < max_val:  # 如果当前节点超出上下界范围，肯定不是
                return False
            # 走到下面这步说明已经满足了如题所述的二叉搜索树的前两个条件
            # 那么只需要递归判断当前节点的左右子树是否同时是二叉搜索树即可
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

        return dfs(root, float('-inf'), float('inf'))  # 对于根节点，它的上下限为无穷大和无穷小

    #
    # 作者：LotusPanda
    # 链接：https: // leetcode - cn.com / problems / validate - binary - search - tree / solution / xiong - mao - shua - ti - python3 - tan - xin - wei - hu - ke - da - d - 5 /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)

    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.left = f

    b.left = a
    b.right = c
    # c.left = f
    print(Solution().isValidBST(b))
    print(Solution().isValidBST2(b))
