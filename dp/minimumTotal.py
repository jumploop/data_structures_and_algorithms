"""
120. 三角形最小路径和


给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 动态规划，自底向上
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        dp = triangle[-1].copy()
        for i in range(-2, -len(triangle) - 1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        # 动态规划，自顶向下
        if len(triangle) == 0:
            return 0
        dp = triangle[0]
        for row in triangle[1:]:
            dp_new = [row[0] + dp[0]]
            for i in range(len(dp) - 1):
                dp_new.append(row[i + 1] + min(dp[i], dp[i + 1]))
            dp_new.append(row[-1] + dp[-1])
            dp = dp_new

        return min(dp)