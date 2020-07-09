#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 15:44
# @Author  : 一叶知秋
# @File    : findMin.py
# @Software: PyCharm
"""
153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

    def findMin2(self, nums: List[int]) -> int:
        # 思路：最后一个值作为target，然后往左移动，最后比较start、end的值
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            # 最后一个元素值为target
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid
        if nums[left] > nums[right]:
            return nums[right]
        return nums[left]
