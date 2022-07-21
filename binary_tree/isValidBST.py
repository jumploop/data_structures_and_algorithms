"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/validate-binary-search-tree
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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 思路 1：中序遍历，检查结果列表是否已经有序
        self.result = []

        def inOrder(node):
            # 中序遍历
            if not node:
                return None
            inOrder(node.left)
            self.result.append(node.val)
            inOrder(node.right)

        inOrder(root)
        for i in range(len(self.result)-1):
            if self.result[i] >= self.result[i + 1]:
                return False
        else:
            return True
