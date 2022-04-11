#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 23:48
# @Author  : 一叶知秋
# @File    : rangeBitwiseAnd.py
# @Software: PyCharm
"""
201. 数字范围按位与
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1:

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count

    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        while m < n:
            n &= n - 1
        return m & n
#