#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 13:27
# @Author  : 一叶知秋
# @File    : climbStairs.py
# @Software: PyCharm
"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in {0, 1}:
            return n
        f = [0 for _ in range(n + 1)]
        print(f)
        f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        print(f)
        return f[n]

    def climbStairs2(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    n = 10
    print(Solution().climbStairs(n))
    print(Solution().climbStairs2(n))
