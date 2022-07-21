#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1020. 飞地的数量

给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
示例 2：


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-enclaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            # 从 (i, j) 开始，将与之相邻的陆地都变成海水
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            # 已经是海水了
            if grid[i][j] == 0:
                return
            # 将 (i, j) 变成海水
            grid[i][j] = 0
            # 淹没上下左右的陆地
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        # 淹掉靠边的陆地
        for i in range(m):
            dfs(grid, i, 0)  # left
            dfs(grid, i, n - 1)  # right
        for j in range(n):
            dfs(grid, 0, j)  # up
            dfs(grid, m - 1, j)  # down
        res = 0
        # 数一数剩下的陆地
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        return res
