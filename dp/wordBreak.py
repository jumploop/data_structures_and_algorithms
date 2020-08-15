#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 22:03
# @Author  : 一叶知秋
# @File    : wordBreak.py
# @Software: PyCharm
"""
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for j in range(len(s)):
            for i in range(j + 1):
                if dp[i - 1] and s[i:j + 1] in wordDict:
                    dp[j] = True
                    break

        return dp[len(s) - 1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    s = 'leetcode'
    wordDict = ["leet", "code"]
    result = Solution().wordBreak(s, wordDict)
    print(result)
    print(Solution().wordBreak(s,wordDict))
