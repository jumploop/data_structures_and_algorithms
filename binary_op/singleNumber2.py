#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 19:49
# @Author  : 一叶知秋
# @File    : singleNumber2.py
# @Software: PyCharm
"""
137. 只出现一次的数字 II
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99
"""
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 统计每位1的个数
        result = 0
        for i in range(64):
            sum = sum(num >> i & 1 for num in nums)
            # 还原位00^10=10 或者用| 也可以
            result ^= (sum % 3) << i
        return result

    def singleNumber2(self, nums):
        # 方法一：HashSet
        return (3 * sum(set(nums)) - sum(nums)) // 2

    def singleNumber3(self, nums):
        # 方法二：HashMap
        hashmap = Counter(nums)
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k

    def singleNumber4(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once


if __name__ == '__main__':
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(Solution().singleNumber(nums))
    nums = [2, 2, 3, 2]
    print(Solution().singleNumber4(nums))
    print(1 & ~1)
