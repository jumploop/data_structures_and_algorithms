#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 14:24
# @Author  : 一叶知秋
# @File    : canJump.py
# @Software: PyCharm
"""
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

    def canJump2(self, nums: List[int]) -> bool:
        # tail to head
        left = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            left = i if i + nums[i] >= left else left
        return left == 0

    def canJump3(self, nums: List[int]) -> bool:
        max_pos = nums[0]  # furthest index can reach
        for i in range(1, len(nums)):
            if max_pos < i:
                return False
            max_pos = max(max_pos, i + nums[i])  # DP
        return True


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().canJump(nums))
    print(Solution().canJump2(nums))
    print(Solution().canJump3(nums))
