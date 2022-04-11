#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 19:24
# @Author  : 一叶知秋
# @File    : minCut.py
# @Software: PyCharm
"""
132. 分割回文串 II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""


class Solution:
    def minCut(self, s: str) -> int:
        dp_min = [0] * len(s)
        dp_pal = [True] * len(s)
        print(dp_min)
        print(dp_pal)

        def isPal(i, j):
            dp_pal[i] = (s[i] == s[j] and dp_pal[i + 1])
            return dp_pal[i]

        for j in range(1, len(s)):
            min_cut = dp_min[j - 1] + 1
            if isPal(0, j):
                min_cut = 0
            for i in range(1, j):
                if isPal(i, j):
                    min_cut = min(min_cut, dp_min[i - 1] + 1)
            dp_min[j] = min_cut
        print(dp_min)
        return dp_min[-1]

    def minCut2(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0

        dp = list(range(size))
        check_palindrome = [[False for _ in range(size)] for _ in range(size)]
        print(check_palindrome)
        for right in range(size):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left + 1][right - 1]):
                    check_palindrome[left][right] = True

        for i in range(1, size):
            if check_palindrome[0][i]:
                dp[i] = 0
                continue
            # 枚举分割点
            dp[i] = min(dp[j] + 1 for j in range(i) if check_palindrome[j + 1][i])

        return dp[size - 1]


if __name__ == '__main__':
    s = "aab"
    print(s)
    print(Solution().minCut(s))
    print(Solution().minCut2(s))
