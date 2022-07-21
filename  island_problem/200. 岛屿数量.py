#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            # 从 (i, j) 开始，将与之相邻的陆地都变成海水
            m = len(grid)
            n = len(grid[0])
            if i < 0 or j < 0 or i >= m or j >= n:
                # 超出索引边界
                return
            if grid[i][j] == '0':
                # 已经是海水了
                return
            # 将 (i, j) 变成海水
            grid[i][j] = '0'
            # 淹没上下左右的陆地
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        # 遍历grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 每发现一个岛屿，岛屿数量加一
                    result += 1
                    # 然后使用 DFS 将岛屿淹了
                    dfs(grid, i, j)
        return result