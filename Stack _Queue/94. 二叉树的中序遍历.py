"""
94. 二叉树的中序遍历


给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

"""


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack, inorder = [], []
        node = root
        while len(stack) > 0 or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                inorder.append(node.val)
                node = node.right

        return inorder