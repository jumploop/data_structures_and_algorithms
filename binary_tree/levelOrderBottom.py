"""
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = [root]
        while queue:
            tmp = []
            #  记录当前层有多少元素（遍历当前层，再添加下一层）
            for _ in range(len(queue)):
                # 出队列
                level = queue[0]
                queue = queue[1:]
                tmp.append(level.val)
                if level.left:
                    queue.append(level.left)
                if level.right:
                    queue.append(level.right)
            result.append(tmp)
        return result[::-1]