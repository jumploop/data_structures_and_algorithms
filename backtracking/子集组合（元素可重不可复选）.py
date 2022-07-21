#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
90. 子集 II

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

 

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        path = []

        def backtrack(start):
            result.append(path[:])
            last = None
            for i in range(start, len(nums)):
                if last != nums[i]:
                    path.append(nums[i])
                    backtrack(i + 1)
                    last = path.pop()

        backtrack(0)
        return result

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        path = []

        def backtrack(start):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 2]))
    print(solution.subsetsWithDup2([1, 2, 2]))

