#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 10:31
# @Author  : 一叶知秋
# @File    : uniquePaths.py
# @Software: PyCharm
"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？



示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28


提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9
"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

    def uniquePaths2(self, m: int, n: int) -> int:
        # f[i][j] 表示i,j到0,0路径数
        dp = [[1] * n] * m
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                print(dp)
        return dp[m - 1][n - 1]

    def uniquePaths3(self, m: int, n: int) -> int:

        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


if __name__ == '__main__':
    m = 3
    n = 2
    print(Solution().uniquePaths(m, n))
    print(Solution().uniquePaths2(m, n))
    print(Solution().uniquePaths3(m, n))
