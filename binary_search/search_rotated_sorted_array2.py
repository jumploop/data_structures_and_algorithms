#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 18:11
# @Author  : 一叶知秋
# @File    : search_rotated_sorted_array2.py
# @Software: PyCharm
"""
81. 搜索旋转排序数组 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 思路：两条上升直线，四种情况判断，并且处理重复数字
        if not nums:
            return False
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            # 处理重复数字
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = (left + right) >> 1
            # 相等直接返回
            if nums[mid] == target:
                return True
            # 判断在那个区间，可能分为四种情况
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[right] > nums[mid]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target or nums[right] == target:
            return True
        return False

    def search2(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return False
