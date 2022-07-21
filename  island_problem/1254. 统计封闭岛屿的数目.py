#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1254. 统计封闭岛屿的数目

二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

 

示例 1：



输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-closed-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            # 从 (i, j) 开始，将与之相邻的陆地都变成海水
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            # 已经是海水了
            if grid[i][j] == 1:
                return
            # 将 (i, j) 变成海水
            grid[i][j] = 1
            # 淹没上下左右的陆地
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        for j in range(n):
            # 把靠上边的岛屿淹掉
            dfs(grid, 0, j)
            # 把靠下边的岛屿淹掉
            dfs(grid, m - 1, j)

        for i in range(m):
            # 把靠左边的岛屿淹掉
            dfs(grid, i, 0)
            # 把靠右边的岛屿淹掉
            dfs(grid, i, n - 1)
        # 遍历 grid，剩下的岛屿都是封闭岛屿
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    dfs(grid, i, j)
        return res