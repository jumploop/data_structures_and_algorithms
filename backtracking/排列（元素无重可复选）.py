#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
排列（元素无重可复选）
"""
from typing import List


class Solution:
    def permuteRepeat(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums = sorted(nums)

        def backtrack():
            # base case，到达叶子节点
            if len(path) == len(nums):
                # 收集叶子节点上的值
                result.append(path[:])
                return
            # 回溯算法标准框架
            for i in range(len(nums)):
                # 做选择
                path.append(nums[i])
                # 进入下一层回溯树
                backtrack()
                # 取消选择
                path.pop()

        backtrack()
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteRepeat([1, 1, 2]))
