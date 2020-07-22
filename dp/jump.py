#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 16:50
# @Author  : 一叶知秋
# @File    : jump.py
# @Software: PyCharm
"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, step, end = 0, 0, 0
        for i in range(n - 1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    end = max_pos
                    step += 1
        return step

    def jump2(self, nums: List[int]) -> int:
        steps, end, maxPos = 0, 0, 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, nums[i] + i)
            if i == end:
                end = maxPos
                steps += 1
        return steps


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))
    print(Solution().jump2(nums))
