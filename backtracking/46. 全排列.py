"""
46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []
        used = [False] * n

        def backtrack():
            if len(path) == n:
                result.append(path[:])
                return
            for i in range(n):
                # 已经存在 track 中的元素，不能重复选择
                if used[i]:
                    continue
                # 做选择
                used[i] = True
                path.append(nums[i])
                # 进入下一层回溯树
                backtrack()
                # 撤销操作
                path.pop()
                used[i] = False

        backtrack()
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
