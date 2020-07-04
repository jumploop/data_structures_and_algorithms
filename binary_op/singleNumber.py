#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 19:35
# @Author  : 一叶知秋
# @File    : singleNumber.py
# @Software: PyCharm
"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber2(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res

# 解题思路
# 0和任何数异或的结果都是这个数本身。
#
# 相同的数异或的结果为0。
#
# 这个数列里面除了一个数只出现了一次，其他数都出现了两次。
#
# 异或运算满足交换律和结合律。
#
# 因此从前往后依次异或即可。最终结果就是那个只出现一次的数。
#
# 比如 1 xor 1 xor 2 xor 3 xor 2 = (1 xor 1) xor (2 xor 2) xor 3 = 0 xor 0 xor 3 = 0 xor 3 = 3

if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]

    print(Solution().singleNumber(nums))
    print(Solution().singleNumber2(nums))
