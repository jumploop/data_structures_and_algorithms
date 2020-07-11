#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 9:20
# @Author  : 一叶知秋
# @File    : minimumTotal.py
# @Software: PyCharm
"""
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。



例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。



说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""
from typing import List

# 动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        dp = triangle[-1].copy()
        print(dp)
        for i in range(-2, -len(triangle) - 1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimumTotal(triangle))
    print(Solution().minimumTotal2(triangle))
