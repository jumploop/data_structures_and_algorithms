"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = [root]
        toggle = False
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
            if toggle:
                tmp = tmp[::-1]
            result.append(tmp)
            toggle = not toggle
        return result