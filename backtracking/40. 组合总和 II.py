#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
40. 组合总和 II

给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        if not candidates:
            return result
        # 记录 track 中的元素之和
        trackSum = 0
        # 先排序，让相同的元素靠在一起
        candidates = sorted(candidates)

        def backtrack(start, target):
            nonlocal trackSum
            # base case，达到目标和，找到符合条件的组合
            if trackSum == target:
                result.append(path[:])
                return
            # base case，超过目标和，直接结束
            if trackSum > target:
                return
            # 回溯算法标准框架
            for i in range(start, len(candidates)):
                # 剪枝逻辑，值相同的树枝，只遍历第一条
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # 做选择
                path.append(candidates[i])
                trackSum += candidates[i]
                # 递归遍历下一层回溯树
                backtrack(i + 1, target)
                # 撤销选择
                path.pop()
                trackSum -= candidates[i]

        backtrack(0, target)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
