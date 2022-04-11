#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 13:10
# @Author  : 一叶知秋
# @File    : minDepth.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans, count = [root], 1
        while ans:
            n = len(ans)
            for _ in range(n):
                if r := ans.pop(0):
                    if not r.left and not r.right:
                        return count
                    ans.append(r.left or [])
                    ans.append(r.right or [])
            count += 1


def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.right:
        return 1 + minDepth(root.left)
    if not root.left:
        return 1 + minDepth(root.right)
    return 1 + min(minDepth(root.left), minDepth(root.right))


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
    result = minDepth(a)
    print(result)
    s = Solution().minDepth(a)
    print(s)
