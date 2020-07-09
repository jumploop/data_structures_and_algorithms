#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 11:53
# @Author  : 一叶知秋
# @File    : searchMatrix.py
# @Software: PyCharm
"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""
from typing import List
import numpy as np


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for num in matrix:
            if target in num:
                return True
            else:
                continue
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # 思路：将2纬数组转为1维数组 进行二分搜索
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        n=np.array(matrix)
        # matrix=np.matrix.flatten(n).tolist()
        # matrix = sum(matrix, [])
        matrix = [num for lst in matrix for num in lst]
        left = 0
        right = row * col - 1
        while left + 1 < right:
            mid = (left + right) // 2
            # 获取2纬数组对应值
            val = matrix[mid]
            if val > target:
                right = mid
            elif val < target:
                left = mid
            else:
                return True
        if matrix[left] == target or matrix[right] == target:
            return True
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    print(Solution().searchMatrix2(matrix, target))
