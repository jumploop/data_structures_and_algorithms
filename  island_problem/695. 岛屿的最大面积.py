#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
695. 岛屿的最大面积
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        # # 淹没与 (i, j) 相邻的陆地，并返回淹没的陆地面积
        def dfs(grid, i, j):
            # 超出索引边界
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            # 经是海水了
            if grid[i][j] == 0:
                return 0
            # 将 (i, j) 变成海水
            grid[i][j] = 0
            return dfs(grid, i + 1, j) + dfs(grid, i, j + 1) + dfs(grid, i - 1, j) + dfs(grid, i, j - 1) + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 淹没岛屿，并更新最大岛屿面积
                    res = max(res, dfs(grid, i, j))
        return res