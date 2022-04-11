#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 20:31
# @Author  : 一叶知秋
# @File    : lengthOfLIS.py
# @Software: PyCharm
"""
300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seq = [nums[0]]
        # print(seq)
        for i in range(1, len(nums)):
            ins = bisect.bisect_left(seq, nums[i])
            if ins == len(seq):
                seq.append(nums[i])
            else:
                seq[ins] = nums[i]
            # print(seq)
        return len(seq)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        """该方法超时"""
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            print(dp)
        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
    print(Solution().lengthOfLIS2(nums))
