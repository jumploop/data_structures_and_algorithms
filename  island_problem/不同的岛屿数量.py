#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
不同的岛屿数量

力扣第 694 题「 不同的岛屿数量」，题目还是输入一个二维矩阵，0 表示海水，1 表示陆地，这次让你计算 不同的 (distinct) 岛屿数量，函数签名如下：
"""
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 记录所有岛屿的序列化结果
        islands = set()

        def dfs(grid, i, j, sb, dirs):
            # 从 (i, j) 开始，将与之相邻的陆地都变成海水
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            # 前序遍历位置：进入 (i, j)
            grid[i][j] = 1
            sb.append(dirs).append(',')
            dfs(grid, i - 1, j, sb, 1)  # 上
            dfs(grid, i + 1, j, sb, 2)  # 下
            dfs(grid, i, j - 1, sb, 3)  # 左
            dfs(grid, i, j + 1, sb, 4)  # 右

            # 后序遍历位置：离开(i, j)
            sb.append(-dirs)
            sb.append(',')

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 淹掉这个岛屿，同时存储岛屿的序列化结果
                    sb = []
                    # 初始的方向可以随便写，不影响正确性
                    dfs(grid, i, j, sb, 666)
                    islands.add(''.join(str(s) for s in sb))
        # 不相同的岛屿数量
        return len(islands)
