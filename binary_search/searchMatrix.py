#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 两次二分，首先定位行数，接着定位列数
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                return True
        row = right
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            if target in item:
                return True
        else:
            return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # 思路：将2纬数组转为1维数组 进行二分搜索
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row * col - 1
        while left + 1 < right:
            mid = (left + right) // 2
            val = matrix[mid // col][mid % col]
            if val > target:
                right = mid
            elif val < target:
                left = mid
            else:
                return True
        if matrix[left // col][left % col] == target or matrix[right // col][right % col] == target:
            return True
        return False
