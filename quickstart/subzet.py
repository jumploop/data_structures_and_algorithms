#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 9:13
# @Author  : 一叶知秋
# @File    : subzet.py
# @Software: PyCharm

# 78. 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import itertools


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(list(tmp))
        return res


if __name__ == '__main__':
    nums=[1,2,3]
    solution = Solution()
    result = solution.subsets(nums)
    print(result)

'''思路一:库函数


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res
思路二:迭代


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
思路三:递归(回溯算法)

pythonjava

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res  

作者：powcai
链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''