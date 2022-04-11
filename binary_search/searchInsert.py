#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 10:27
# @Author  : 一叶知秋
# @File    : searchInsert.py
# @Software: PyCharm
"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 思路：找到第一个 >= target 的元素位置
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target or nums[mid] <= target:
                left = mid  # 标记开始位置
            else:
                right = mid
        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        else:
            return right + 1  # 目标值比所有值都大
        return 0

    def searchInsert2(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0
        left = 0
        # 因为有可能数组的最后一个元素的位置的下一个是我们要找的，故右边界是 len
        right = size

        while left < right:
            mid = (left + right) >> 1
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            elif nums[mid] == target:
                # 根据本题特殊性，看到等于 target 的元素，返回任意一个即可
                return mid
            else:
                right = mid
        return left

    def searchInsert3(self, nums: List[int], target: int) -> int:
        # 不在里面，直接append
        if target not in nums:
            nums.append(target)
            # 然后再排序
            nums.sort()
            # 最后返回查找的index
        return nums.index(target)


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 0
    print(Solution().searchInsert(nums, target))
    print(Solution().searchInsert2(nums, target))
