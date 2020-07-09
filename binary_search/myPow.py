#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 8:38
# @Author  : 一叶知秋
# @File    : myPow.py
# @Software: PyCharm
"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

    def myPow2(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
if __name__ == '__main__':
    x=2
    n=3
    print(Solution().myPow2(x,n))