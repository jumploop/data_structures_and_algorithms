#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 12:30
# @Author  : 一叶知秋
# @File    : singleNumber3.py
# @Software: PyCharm
"""
260. 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
"""
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        data = Counter(nums)
        print(data)
        for k in data:
            if data[k] == 1:
                result.append(k)
        return result

    def singleNumber2(self, nums: List[int]) -> List[int]:
        diff = 0
        for i in range(len(nums)):
            diff ^= nums[i]
        print(diff)
        result = [diff, diff]
        # 去掉末尾的1后异或diff就得到最后一个1的位置
        diff = (diff & (diff - 1)) ^ diff
        for i in range(len(nums)):
            if diff & nums[i] == 0:
                result[0] ^= nums[i]
            else:
                result[1] ^= nums[i]
        return result

    def singleNumber3(self, nums: List[int]) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num

        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        print(diff)
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(nums))
    print(Solution().singleNumber2(nums))
    print(Solution().singleNumber3(nums))
