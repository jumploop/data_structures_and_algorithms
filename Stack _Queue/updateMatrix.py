#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 17:43
# @Author  : 一叶知秋
# @File    : updateMatrix.py
# @Software: PyCharm
"""
542. 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""
import collections
from typing import List


#  BFS 从0进队列，弹出之后计算上下左右的结果，将上下左右重新进队列进行二层操作
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) == 0:
            return matrix

        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf')] * n for _ in range(m)]

        bfs = collections.deque([])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    bfs.append((i, j))

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(bfs) > 0:
            i, j = bfs.popleft()
            for dn_i, dn_j in neighbors:
                n_i, n_j = i + dn_i, j + dn_j
                if (
                    n_i >= 0
                    and n_i < m
                    and n_j >= 0
                    and n_j < n
                    and dist[n_i][n_j] > dist[i][j] + 1
                ):
                    dist[n_i][n_j] = dist[i][j] + 1
                    bfs.append((n_i, n_j))

        return dist

    # 思路 2: 2-pass DP，dist(i, j) = max{dist(i - 1, j), dist(i + 1, j), dist(i, j - 1), dist(i, j + 1)} + 1
    def updateMatrix2(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) == 0:
            return matrix

        m, n = len(matrix), len(matrix[0])

        dist = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i >= 1:
                        dist[i][j] = min(dist[i - 1][j] + 1, dist[i][j])
                    if j >= 1:
                        dist[i][j] = min(dist[i][j - 1] + 1, dist[i][j])
                else:
                    dist[i][j] = 0

        for i in range(-1, -m - 1, -1):
            for j in range(-1, -n - 1, -1):
                if matrix[i][j] == 1:
                    if i < -1:
                        dist[i][j] = min(dist[i + 1][j] + 1, dist[i][j])
                    if j < -1:
                        dist[i][j] = min(dist[i][j + 1] + 1, dist[i][j])

        return dist


if __name__ == '__main__':
    cases = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().updateMatrix2(cases))
