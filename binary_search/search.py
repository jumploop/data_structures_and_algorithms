#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 11:44
# @Author  : 一叶知秋
# @File    : search.py
# @Software: PyCharm
"""
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""
from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        #  二分查找模板 I
        """
           :type nums: List[int]
           :type target: int
           :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1

    # 区分语法
    #
    # 初始条件：left = 0, right = length-1
    # 终止：left > right
    # 向左查找：right = mid-1
    # 向右查找：left = mid+1

    def binarySearch2(self, nums: List[int], target: int) -> int:
        #  二分查找模板 II
        """
            :type nums: List[int]
            :type target: int
            :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # Post-processing:
        # End Condition: left == right
        if left != len(nums) and nums[left] == target:
            return left
        return -1
        # 区分语法
        #
        # 初始条件：left = 0, right = length
        # 终止：left == right
        # 向左查找：right = mid
        # 向右查找：left = mid+1

    def binarySearch3(self, nums: List[int], target: int) -> int:
        #  二分查找模板 III
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # Post-processing:
        # End Condition: left + 1 == right
        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1
        #   区分语法
        #
        # 初始条件：left = 0, right = length-1
        # 终止：left + 1 == right
        # 向左查找：right = mid
        # 向右查找：left = mid


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().binarySearch(nums, target))
    print(Solution().binarySearch2(nums, target))
    print(Solution().binarySearch3(nums, target))
