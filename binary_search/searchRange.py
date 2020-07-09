#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 9:12
# @Author  : 一叶知秋
# @File    : searchRange.py
# @Software: PyCharm
"""
61. 搜索区间
中文English
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

如果目标值不在数组中，则返回[-1, -1]

样例
例1:

输入:
[]
9
输出:
[-1,-1]

例2:

输入:
[5, 7, 7, 8, 8, 10]
8
输出:
[3, 4]
挑战
时间复杂度 O(log n)
"""


# 思路：核心点就是找第一个 target 的索引，和最后一个 target 的索引，所以用两次二分搜索分别找第一次和最后一次的位置
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        first_pos = self.get_first_pos(A, target)
        cur = first_pos
        while 0 <= cur < len(A) - 1 and A[cur + 1] == target:
            cur += 1
        return [first_pos, cur]

    def get_first_pos(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


if __name__ == '__main__':
    A = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(A, target))
