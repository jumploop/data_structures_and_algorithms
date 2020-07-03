#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 15:09
# @Author  : 一叶知秋
# @File    : largestRectangleArea.py
# @Software: PyCharm
"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。




以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。




图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。



示例:

输入: [2,1,5,6,2,3]
输出: 10
"""
from typing import List


# 思路：求以当前柱子为高度的面积，即转化为寻找小于当前值的左右两边值

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        Max = 0
        for i in range(len(heights)):
            if i == len(heights):
                cur = 0
            else:
                cur = heights[i]
            # 当前高度小于栈，则将栈内元素都弹出计算面积
            while stack and cur <= heights[stack[len(stack) - 1]]:
                pop = stack[len(stack) - 1]
                stack = stack[:len(stack) - 1]
                h = heights[pop]
                # 计算宽度
                w = i
                if stack:
                    peek = stack[len(stack) - 1]
                    w = i - peek - 1
                Max = max(Max, h * w)
            # 记录索引即可获取对应元素
            stack.append(i)
        return Max

    def largestRectangleArea2(self, heights: List[int]) -> int:
        # 最简单的思路就是，就是暴力法，直接分别在 i 左右移动。
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res

    # 思路二：栈
    # 利用单调栈
    #
    # 维护一个单调递增的栈，就可以找到 left_i 和 right_i。
    def largestRectangleArea3(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res
if __name__ == '__main__':
    nums=[2,1,5,6,2,3]
    print(Solution().largestRectangleArea(nums))