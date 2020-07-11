#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 9:28
# @Author  : 一叶知秋
# @File    : minPathSum.py
# @Software: PyCharm
"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""
from typing import List
from copy import deepcopy


# 思路：动态规划 1、state: f[x][y]从起点走到 x,y 的最短路径 2、function: f[x][y] = min(f[x-1][y], f[x][y-1]) + A[x][y] 3、intialize: f[0][0] = A[0][0]、f[i][0] = sum(0,0 -> i,0)、 f[0][i] = sum(0,0 -> 0,i) 4、answer: f[n-1][m-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        grid = deepcopy(grid)
        """思路：动态规划"""
        if not grid or not grid[0]:
            return 0
        # 复用原来的矩阵列表
        # 初始化：f[i][0]、f[0][j]
        for i in range(1, len(grid)):
            grid[i][0] = grid[i][0] + grid[i - 1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] = grid[0][j] + grid[0][j - 1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]
        return grid[len(grid) - 1][len(grid[0]) - 1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        grid = deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    n = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(n)
    print(Solution().minPathSum(n))
    print(Solution().minPathSum2(n))
