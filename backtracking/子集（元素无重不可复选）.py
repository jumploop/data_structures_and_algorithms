#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
78. 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        # 回溯算法核心函数，遍历子集问题的回溯树
        def backtrack(start):
            # 前序位置，每个节点的值都是一个子集
            result.append(path[:])
            for i in range(start, len(nums)):
                # 做选择
                path.append(nums[i])
                # 通过 start 参数控制树枝的遍历，避免产生重复的子集
                backtrack(i + 1)
                # 撤销选择
                path.pop()

        backtrack(0)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
