#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 16:08
# @Author  : 一叶知秋
# @File    : findMin2.py
# @Software: PyCharm
"""
154. 寻找旋转排序数组中的最小值 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 思路：跳过重复元素，mid值和end值比较，分为两种情况进行处理
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            # 去除重复元素
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            mid = (left + right) >> 1
            # 中间元素和最后一个元素比较（判断中间点落在左边上升区，还是右边上升区）
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid
        if nums[left] > nums[right]:
            return nums[right]
        return nums[left]

    def findMin2(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1  # key
        return nums[left]
